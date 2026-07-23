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

`master/resume.md` is the canonical curated resume. Broader facts, evidence, projects, and skills belong in `master/*-inventory.md` and `master/achievements.md`; role resumes select only relevant, defensible claims. Markdown is editable source, while DOCX/PDF files are generated artifacts.

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

## Privacy

Public builds intentionally omit phone and email. Existing Git history may still contain prior contact details; removing history is a separate, deliberate operation and is not performed automatically.

## Folder Map

`master/` canonical resume, inventories, and evidence · `resumes/` targeted sources and exports · `sections/` reusable blocks · `portfolio/` public project records · `applications/` tracker/templates · `interview/` preparation assets · `docs/` detailed operating guidance.

Read [workflow](docs/WORKFLOW.md), [checklists](docs/CHECKLISTS.md), [contributing guidance](docs/CONTRIBUTING.md), [AI usage](docs/AI_USAGE.md), and the [resume design system](docs/resume-design-system.md) for details.
