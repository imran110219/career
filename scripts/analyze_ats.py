#!/usr/bin/env python3
"""Produce a transparent ATS-alignment report for a resume and job description.

This is a heuristic review aid, not a simulation of a proprietary ATS.  It
never recommends adding a skill or claim that is not supported by evidence.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


TERM_ALIASES = {
    "java": ("java",), "spring boot": ("spring boot",),
    "hibernate": ("hibernate",), "rest api": ("rest api", "restful", "rest"),
    "microservices": ("microservices", "microservice"),
    "distributed systems": ("distributed systems", "distributed system"),
    "api design": ("api design", "api architecture", "api contracts"),
    "postgresql": ("postgresql", "postgres"), "sql": ("sql",),
    "redis": ("redis",), "kubernetes": ("kubernetes", "k8s"), "docker": ("docker",),
    "aws": ("aws", "amazon web services"), "gcp": ("gcp", "google cloud"),
    "azure": ("azure",), "ci/cd": ("ci/cd", "continuous integration", "continuous delivery"),
    "terraform": ("terraform",), "linux": ("linux",), "graphql": ("graphql",),
    "kafka": ("kafka",), "rabbitmq": ("rabbitmq",), "elasticsearch": ("elasticsearch",),
    "mongodb": ("mongodb", "mongo db"), "mysql": ("mysql",), "sql server": ("sql server",),
    "keycloak": ("keycloak",), "oauth": ("oauth", "openid connect", "oidc"),
    "authentication": ("authentication",), "authorization": ("authorization",),
    "security": ("security", "secure"), "data integrity": ("data integrity",),
    "database design": ("database design", "database modeling", "data modeling", "schema design"),
    "query optimization": ("query optimization", "performance tuning"),
    "performance optimization": ("performance optimization", "performance improvements"),
    "system design": ("system design", "systems design"), "scalability": ("scalability", "scalable"),
    "reliability": ("reliability", "reliable"), "observability": ("observability", "monitoring"),
    "testing": ("testing", "test automation", "unit test", "integration test"),
    "agile": ("agile", "scrum", "kanban"), "code review": ("code review", "code reviews"),
    "mentoring": ("mentoring", "mentor"), "technical leadership": ("technical leadership",),
    "requirements analysis": ("requirements analysis", "requirements gathering"),
    "deployment": ("deployment", "deployments", "deployed"), "architecture": ("architecture", "architectural"),
}

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def clean(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"[`*_#>|]", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def contains(text: str, aliases: tuple[str, ...]) -> bool:
    return any(re.search(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", text) for alias in aliases)


def sections(markdown: str) -> dict[str, str]:
    found = list(SECTION_RE.finditer(markdown))
    result: dict[str, str] = {}
    for index, match in enumerate(found):
        end = found[index + 1].start() if index + 1 < len(found) else len(markdown)
        result[match.group(1).strip().lower()] = markdown[match.end():end]
    return result


def jd_terms(job_description: str) -> list[str]:
    normalized = clean(job_description)
    return [term for term, aliases in TERM_ALIASES.items() if contains(normalized, aliases)]


def bullets(text: str) -> list[str]:
    return [clean(line) for line in text.splitlines() if re.match(r"^\s*[-*]\s+", line)]


def has_markdown_table(text: str) -> bool:
    lines = text.splitlines()
    return any(
        lines[index].count("|") >= 2
        and bool(re.match(r"^\s*\|?\s*:?-{3,}", lines[index + 1]))
        for index in range(len(lines) - 1)
    )


def score(resume: str, jd: str) -> tuple[dict, dict]:
    resume_clean, jd_clean = clean(resume), clean(jd)
    resume_sections = sections(resume)
    terms = jd_terms(jd)
    if not terms:
        raise ValueError("No recognized requirements were found in the job description. Include a fuller JD or extend TERM_ALIASES.")

    skill_text = clean(resume_sections.get("technical skills", "") + resume_sections.get("skills", ""))
    evidence_text = clean("\n".join(
        value for name, value in resume_sections.items()
        if any(label in name for label in ("experience", "highlights", "projects"))
    ))
    matched = [term for term in terms if contains(resume_clean, TERM_ALIASES[term])]
    skill_matches = [term for term in terms if contains(skill_text, TERM_ALIASES[term])]
    evidence_matches = [term for term in terms if contains(evidence_text, TERM_ALIASES[term])]
    missing = [term for term in terms if term not in matched]

    keyword_score = round(35 * len(matched) / len(terms))
    skills_score = round(15 * len(skill_matches) / len(terms))
    evidence_score = round(25 * len(evidence_matches) / len(terms))

    headings = set(resume_sections)
    format_checks = {
        "Name/title present": bool(re.search(r"^#\s+.+", resume, re.MULTILINE)),
        "Professional summary": any("summary" in heading for heading in headings),
        "Skills section": any("skill" in heading for heading in headings),
        "Experience section": any("experience" in heading for heading in headings),
        "Contact placeholder or details": "{{contact." in resume or bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", resume)),
        "No Markdown tables": not has_markdown_table(resume),
    }
    format_score = round(15 * sum(format_checks.values()) / len(format_checks))

    all_bullets = bullets(resume)
    impact_checks = {
        "Quantified outcomes": bool(re.search(r"\b\d+(?:[,.]\d+)?\s*(?:%|\+|users?|requests?|services?|students?)", resume_clean)),
        "Strong delivery verbs": bool(re.search(r"\b(designed|led|implemented|optimized|deployed|reduced|improved|built)\b", resume_clean)),
        "Leadership/ownership": bool(re.search(r"\b(lead|led|mentoring|mentor|planning|code review|ownership)\b", resume_clean)),
        "Experience bullets": len(all_bullets) >= 6,
    }
    impact_score = round(10 * sum(impact_checks.values()) / len(impact_checks))
    categories = {
        "Required keyword alignment": {"score": keyword_score, "max": 35},
        "Relevant experience evidence": {"score": evidence_score, "max": 25},
        "Skills alignment": {"score": skills_score, "max": 15},
        "ATS formatting/readability": {"score": format_score, "max": 15},
        "Impact and seniority signals": {"score": impact_score, "max": 10},
    }
    details = {"terms": terms, "matched": matched, "missing": missing, "skill_matches": skill_matches,
               "evidence_matches": evidence_matches, "format_checks": format_checks, "impact_checks": impact_checks}
    return categories, details


def report(resume_path: Path, jd_path: Path, categories: dict, details: dict) -> str:
    total = sum(item["score"] for item in categories.values())
    lines = ["# ATS Alignment Report", "", f"- Resume: `{resume_path}`", f"- Job description: `{jd_path}`",
             f"- Overall heuristic score: **{total}/100**", "",
             "This is an explainable alignment review, not a proprietary ATS prediction. Match missing requirements only when supported by verifiable experience.",
             "", "## Score Breakdown", "", "| Area | Score |", "| --- | ---: |"]
    lines.extend(f"| {name} | {item['score']}/{item['max']} |" for name, item in categories.items())
    lines.extend(["", "## Job-Description Terms", "", "**Matched:** " + (", ".join(details["matched"]) or "None"), "",
                  "**Missing or not explicitly stated:** " + (", ".join(details["missing"]) or "None"), "",
                  "## Evidence", "", "**Supported in experience/highlights/projects:** " + (", ".join(details["evidence_matches"]) or "None"), "",
                  "**Appears in the skills section:** " + (", ".join(details["skill_matches"]) or "None"), "",
                  "## Checks", ""])
    for label, passed in {**details["format_checks"], **details["impact_checks"]}.items():
        lines.append(f"- {'Pass' if passed else 'Review'}: {label}")
    lines.extend(["", "## Safe Next Steps", ""])
    if details["missing"]:
        lines.append("- Review these missing terms against `master/achievements.md` and the inventories. Add them only with a concrete, truthful bullet or skill evidence: " + ", ".join(details["missing"]) + ".")
    else:
        lines.append("- All recognized JD terms appear in the resume. Review whether the most important ones are supported by specific experience bullets.")
    lines.append("- Treat the score as a prioritization aid; recruiter judgment and clear, defensible writing matter more than keyword density.")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze transparent ATS alignment between Markdown resume and job description.")
    parser.add_argument("resume", type=Path)
    parser.add_argument("job_description", type=Path)
    parser.add_argument("--output", "-o", type=Path, help="Write Markdown report to this path.")
    parser.add_argument("--json-output", type=Path, help="Optionally write machine-readable results.")
    args = parser.parse_args()
    categories, details = score(args.resume.read_text(encoding="utf-8"), args.job_description.read_text(encoding="utf-8"))
    markdown = report(args.resume, args.job_description, categories, details)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(markdown, end="")
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps({"score": sum(c["score"] for c in categories.values()), "categories": categories, **details}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
