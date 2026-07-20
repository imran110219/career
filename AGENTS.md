# AI Agent Instructions

This repository stores professional career materials for Sadman Sobhan. Treat it as a versioned career operations workspace, not a generic document folder.

## Primary Goal

Help maintain accurate, polished, role-targeted career materials for backend engineering, technical leadership, software architecture, platform engineering, and engineering management opportunities.

## Source Of Truth

| Source | Use |
| --- | --- |
| `master/resume.md` | Canonical resume content and first place to update career facts. |
| `master/achievements.md` | Complete achievement inventory, especially measurable impact. |
| `sections/` | Reusable resume, LinkedIn, portfolio, and application content blocks. |
| `master/linkedin-export.pdf` | Imported LinkedIn profile snapshot. Use for reference, not as the only truth. |
| `resumes/<role>/` | Tailored output for specific job families. |

When facts conflict, prefer the most recently edited Markdown source over generated `.docx` or `.pdf` exports.

## Working Rules

- Do not invent employers, dates, metrics, certifications, publications, project names, or degrees.
- If a detail is missing, add a clear review item rather than fabricating it.
- Keep personal contact information consistent across resume, LinkedIn, portfolio, and cover letters.
- Prefer achievement bullets with scope, action, technical detail, and measurable impact.
- Keep wording professional, direct, and credible for senior engineering roles.
- Avoid exaggerated claims such as "expert in everything", "world-class", or unsupported leadership scope.
- Do not commit secrets, references, identity documents, salary details, or offer details.

## Best Update Sequence

1. Update `master/resume.md` with new facts.
2. Add or refine measurable outcomes in `master/achievements.md`.
3. Sync reusable content in `sections/`.
4. Generate or tailor role-specific resumes under `resumes/<role>/`.
5. Update matching cover letters.
6. Add company-specific material under `companies/applications/<company>/`.
7. Update `CHANGELOG.md`.

## Resume Quality Bar

Every resume version should satisfy this checklist:

- [ ] Header has correct name, location, email, phone, LinkedIn, website, and relevant links.
- [ ] Summary targets the role directly in 3-5 lines.
- [ ] Skills are grouped and aligned with the target job description.
- [ ] Current role has the strongest, most specific bullets.
- [ ] Bullets avoid passive responsibility-only wording.
- [ ] Metrics are preserved when available: users, response time, adoption, volume, engagement, scale.
- [ ] Older roles are concise unless directly relevant.
- [ ] Education, publications, certifications, languages, and awards are included only when useful.
- [ ] PDF and DOCX exports match the Markdown source.

## Role Positioning

| Resume Version | Positioning |
| --- | --- |
| `senior-backend` | Hands-on Java/Spring backend delivery, APIs, PostgreSQL, reliability, performance. |
| `lead-backend` | Backend delivery plus mentoring, planning, code review, ownership, stakeholder collaboration. |
| `software-architect` | System design, distributed systems, API architecture, data modeling, security, scalability. |
| `platform-engineer` | Developer experience, CI/CD, observability, automation, reliability, operational standards. |
| `engineering-manager` | People leadership, delivery execution, planning, hiring, technical credibility. |

## Writing Style

- Use strong verbs: designed, led, implemented, optimized, deployed, reduced, improved, mentored.
- Prefer concise bullets over paragraphs in resume files.
- Keep summaries specific to Sadman’s profile: Java, Spring Boot, backend architecture, distributed systems, health-tech, government, education, enterprise systems.
- Use quantified evidence when present:
  - `30% reduction in system response time`
  - `40% increase in system usage and user satisfaction`
  - `2,500+ administrators`
  - `1,000 exam invigilators`
  - `1,000 examinees`
  - `nearly 30,000 students`
  - `80% increase in user engagement`

## Document Generation

Use `scripts/build_designed_resume.py` to regenerate the master outputs from `master/resume.md` using the approved resume design system. Use the dedicated Senior Backend builder for its finalized two-page composition.

```bash
python3 scripts/build_designed_resume.py master/resume.md master/resume.docx master/resume.pdf
python3 scripts/build_senior_backend_designed_resume.py
```

Notes:

- `master/resume.docx` and `master/resume.pdf` are generated using the approved design system.
- Role-specific outputs use `resumes/<role>/resume.docx` and `resumes/<role>/resume.pdf`.
- The approved visual reference is the Senior Backend resume; preserve its single-column, ATS-safe design.
- If LibreOffice or another reliable renderer is available, visually inspect exported DOCX/PDF before final delivery.
- Do not treat generated binary files as the only editable source.

## Privacy And Safety

Do not add these to Git unless the user explicitly requests and confirms:

- National ID, passport, tax, bank, or legal documents.
- Reference contact details.
- Private salary expectations, offer letters, or negotiation limits.
- Employer-confidential system names, client names, credentials, URLs, logs, or screenshots.

Use `companies/applications/**/private-notes.md` for local-only sensitive notes; it is ignored by Git.

## Future AI Task Prompts

Use these prompts for efficient future sessions:

```text
Read AGENTS.md and master/resume.md. Create a 2-page Senior Backend Engineer resume tailored to this job description: <paste JD>.
```

```text
Read AGENTS.md, master/resume.md, and master/achievements.md. Improve the Penta Global bullets using these new project details: <paste details>.
```

```text
Read AGENTS.md and companies/README.md. Create a company application package for <company> and tailor the cover letter for <role>.
```

```text
Read AGENTS.md and interview/system-design.md. Build a focused interview preparation plan for a backend architect interview.
```

## Open Data Gaps

- [ ] GitHub profile URL.
- [ ] Current Penta Global project names that are safe to disclose.
- [ ] Current project scale, user count, SLA, deployment volume, or performance metrics.
- [ ] Certification providers, dates, and verification links.
- [ ] Publication venue, publication date, and links.
- [ ] Preferred target countries and job markets.
- [ ] Preferred resume length by role.
