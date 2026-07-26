# CLAUDE.md — Career Repository

This repository stores professional career materials for **Sadman Sobhan**, a Senior Java/Spring Boot Backend Engineer with 9 years of experience based in Bangladesh.

---

## Read before acting

| Task | Files to read first |
|---|---|
| Any resume, cover letter, or career-content work | `AGENTS.md`, `master/resume.md`, `master/skills-inventory.md`, `master/experience-inventory.md` |
| Job search / job report | `job-search/AGENT.md`, `config/job-search.yml`, `master/skills-inventory.md`, `master/experience-inventory.md` |
| Interview preparation | `AGENTS.md`, `interview/ROADMAP.md`, `interview/PROGRESS.md` |
| Application tracking | `applications/tracker.csv`, `applications/target-companies.md` |

`AGENTS.md` is the main instruction file for resume and career work.
`job-search/AGENT.md` is the full instruction file for job discovery runs.

---

## Hard rules (apply to every task)

- **Never invent** employers, dates, metrics, certifications, publications, skills, sponsorship status, or remote eligibility.
- **Never modify** resumes, configuration, evidence files, or `applications/tracker.csv` during a job-search run unless the user explicitly asks.
- **Never auto-apply** to jobs.
- When a fact cannot be verified, add a `NEEDS REVIEW` label rather than filling in a plausible value.
- Verified skills live in `master/skills-inventory.md`. Terms in `config/job-search.yml → market_demand` are search signals only, not verified candidate claims.
- Sensitive data (salary, phone, email, identity documents, offer details) must not be committed. Public builds use `config/contact-public.yml`.

---

## Candidate snapshot

| Field | Value |
|---|---|
| Name | Sadman Sobhan |
| Current role | Senior Software Engineer — Penta Global Ltd. (Aug 2023–Present) |
| Total experience | ~9 years (Oct 2016–present) |
| Core stack | Java, Spring Boot, REST APIs, PostgreSQL, Redis, Microservices, Docker |
| Target roles | Senior Backend Engineer, Lead Backend Engineer, Backend Technical Lead |
| Target markets | Malaysia, Singapore, UAE, Saudi Arabia, Qatar, Germany, Ireland, Global Remote |
| Based in | Bangladesh |

Full verified skills: `master/skills-inventory.md`
Full experience: `master/experience-inventory.md`

---

## Common task prompts

**Job search (run this verbatim):**
```
Read `job-search/AGENT.md` and `config/job-search.yml`.

Search the public web for currently open jobs matching the configured profile. Validate original vacancy pages, revalidate existing report entries, score and classify eligible roles, remove expired and duplicate jobs, and replace `job-search/latest-jobs.md`.

Do not modify resumes, configuration, evidence files, or `applications/tracker.csv`. Do not automatically apply.
```

**Tailor resume to a job description:**
```
Read AGENTS.md, master/resume.md, and master/skills-inventory.md. Tailor the <role> resume for this job description: <paste JD>. Do not invent skills or metrics.
```

**Improve resume bullets with new project details:**
```
Read AGENTS.md, master/resume.md, and master/achievements.md. Improve the <employer> bullets using these new details: <paste details>.
```

**Create a company application package:**
```
Read AGENTS.md and applications/target-companies.md. Create a company application folder under companies/applications/<company>/ and tailor the cover letter for <role>.
```

---

## Repo layout (quick reference)

```
master/          Canonical resume, inventories, achievements, evidence, skill gaps
resumes/         Role-targeted resume sources and PDF/DOCX exports
sections/        Reusable resume content blocks
job-search/      Job discovery instructions (AGENT.md) and latest validated report
job-descriptions/ Saved job descriptions for tailoring and ATS analysis
applications/    Global tracker (tracker.csv) and target-company list
companies/       Per-company research and application packages
interview/       Role-based preparation, question bank, case studies, progress log
config/          job-search.yml (scoring, markets, eligibility), contact defaults
scripts/         Resume generation and ATS analysis tools
docs/            Workflow, checklists, AI usage guide, design system
```

Output file for job search: `job-search/latest-jobs.md`
Application tracker: `applications/tracker.csv`
