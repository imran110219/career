# Career Repository

Public, evidence-driven career materials for Senior Backend Engineer, Lead Backend Engineer, and Software Architect applications. The repository preserves an ATS-safe, Markdown-first resume workflow while keeping private application data out of Git.

## Current Resume Versions

| Track | Status | Main focus |
| --- | --- | --- |
| [Senior Backend](resumes/senior-backend/) | Primary | Java, Spring Boot, PostgreSQL, APIs, performance |
| [Lead Backend](resumes/lead-backend/) | Primary | Hands-on delivery leadership, planning, review, mentoring |
| [Software Architect](resumes/software-architect/) | Primary | Distributed systems, API and data architecture |
| [Platform Engineer](resumes/platform-engineer/) | Exploratory | Deployment support and reliability evidence; significant gaps remain |
| [Engineering Manager](resumes/engineering-manager/) | Exploratory | Technical leadership evidence; formal people-management gaps remain |

## Source of Truth

`master/resume.md` is the canonical curated resume. Broader facts, evidence, projects, and verified skills belong in `master/*-inventory.md` and `master/achievements.md`; market-demand skills that lack resume-safe proof belong in `master/skill-gaps.md`. Role resumes select only relevant, defensible claims. Markdown is editable source, while DOCX/PDF files are generated artifacts.

## Generate a Resume

Public-safe output (default):

```bash
python3 scripts/build_master_resume.py
python3 scripts/build_senior_backend_designed_resume.py
python3 scripts/build_designed_resume.py resumes/lead-backend/resume.md resumes/lead-backend/resume.docx resumes/lead-backend/resume.pdf
```

For a local application-ready build, copy `config/contact-private.example.yml` to the ignored `config/contact-private.yml`, fill it locally, then append `--contact-file config/contact-private.yml` to a build command. Never commit that file.

## Check ATS Alignment

Use the local, transparent analyzer to compare a Markdown resume with a saved job description:

```bash
python3 scripts/analyze_ats.py \
  resumes/senior-backend/resume.md \
  job-descriptions/senior-backend-example.md \
  --output reports/senior-backend-example-ats.md
```

It scores keyword alignment, experience evidence, skills alignment, ATS-safe structure, and impact signals. The report shows every recognized match and gap; it is a review aid, not a proprietary ATS prediction. See [job-descriptions/README.md](job-descriptions/README.md) for the job-description format.

## Run Job Search

Job discovery is managed from [job-search/](job-search/). Use [job-search/AGENT.md](job-search/AGENT.md) with [config/job-search.yml](config/job-search.yml) to search current public vacancies, validate original vacancy pages, classify eligible roles, remove expired or duplicate listings, and replace [job-search/latest-jobs.md](job-search/latest-jobs.md).

Application progress belongs in the only application-state tracker, [applications/tracker.csv](applications/tracker.csv). [applications/target-companies.md](applications/target-companies.md) is the canonical company-monitoring source, and [job-search/latest-jobs.md](job-search/latest-jobs.md) is the only discovery output. A Job ID links discovery, tracking, and any company package. Discovery never automatically creates an application. Company-specific application packages remain under [companies/applications/](companies/applications/) so global tracking stays separate from per-company material.

## Privacy

Public builds intentionally omit phone and email. Existing Git history may still contain prior contact details; removing history is a separate, deliberate operation and is not performed automatically.

## Folder Map

`master/` canonical resume, inventories, evidence, and skill-gap backlog · `resumes/` targeted sources and exports · `sections/` reusable blocks · `job-descriptions/` saved job descriptions for tailoring and ATS analysis · `job-search/` discovery instructions and latest validated job report · `applications/` global tracker and target-company list · `companies/` company research and application packages · `portfolio/` public project/profile records · `interview/` role-based preparation roadmap, progress, evidence log, question bank, shared technical notes, and project case studies · `config/` public contact defaults and local workflow configuration · `scripts/` resume generation and analysis tools · `assets/` icons, logos, and profile-photo assets · `templates/` reusable document/application templates · `certifications/` certification records · `publications/` publication records · `archive/` retired or historical materials · `docs/` detailed operating guidance.

Read [workflow](docs/WORKFLOW.md), [checklists](docs/CHECKLISTS.md), [contributing guidance](docs/CONTRIBUTING.md), [AI usage](docs/AI_USAGE.md), and the [resume design system](docs/resume-design-system.md) for details.
