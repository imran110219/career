# Career Repository

This repository is the source of truth for professional career materials: master resume files, targeted resume versions, reusable resume sections, company-specific applications, interview notes, portfolio links, certifications, publications, and archived materials.

The goal is to keep every career asset versioned, reusable, and easy to update before applying to roles.

## Folder Structure

| Path | Purpose |
| --- | --- |
| `assets/` | Profile photos, company logos, icons, and other visual assets used in resumes or portfolio pages. |
| `master/` | Canonical resume, LinkedIn export, and complete achievement inventory. |
| `resumes/` | Role-specific resume and cover letter versions tailored for target positions. |
| `sections/` | Reusable Markdown blocks for resume and profile content. |
| `companies/` | Company research, application trackers, and customized application packages. |
| `interview/` | Technical, behavioral, compensation, and general interview preparation notes. |
| `portfolio/` | Public-facing project, GitHub, writing, LinkedIn, and website content. |
| `certifications/` | Certificates, credential notes, renewal dates, and verification links. |
| `publications/` | Articles, talks, papers, and external writing references. |
| `templates/` | Base templates for resumes, cover letters, outreach emails, and follow-ups. |
| `archive/` | Historical materials that should be preserved but are no longer active. |

## Resume Versions

| Version | Target Roles | Primary Emphasis |
| --- | --- | --- |
| `master/` | Internal source document | Complete career history, metrics, achievements, and references. |
| `resumes/senior-backend/` | Senior Backend Engineer | Java, Spring, APIs, PostgreSQL, performance, reliability. |
| `resumes/lead-backend/` | Lead Backend Engineer | Technical leadership, delivery ownership, mentoring, architecture. |
| `resumes/software-architect/` | Software Architect | System design, platform strategy, standards, scalability, governance. |
| `resumes/platform-engineer/` | Platform Engineer | Developer experience, CI/CD, observability, infrastructure automation. |
| `resumes/engineering-manager/` | Engineering Manager | People leadership, planning, execution, hiring, stakeholder management. |

## Workflow

1. Update `master/achievements.md` whenever a measurable accomplishment happens.
2. Keep reusable content current in `sections/`.
3. Refresh `master/resume.docx` and `master/resume.pdf` from the latest source material.
4. Copy the relevant master content into a role-specific resume folder.
5. Tailor the summary, skills, experience bullets, and project selection to the job description.
6. Save company-specific notes under `companies/applications/`.
7. Commit each meaningful update with a clear message.

## Job Application Workflow

| Step | Output | Location |
| --- | --- | --- |
| Research company and role | Company brief, role requirements, risks, questions | `companies/applications/<company>/` |
| Select resume version | Targeted `.docx` and `.pdf` | `resumes/<role>/` |
| Draft cover letter | Customized message | `resumes/<role>/cover-letter.md` or company folder |
| Prepare outreach | Recruiter or hiring manager message | `templates/email-template.md` |
| Track submission | Date, role, link, status, next action | `companies/applications/` |
| Prepare interview | Focused technical and behavioral notes | `interview/` |
| Archive outcome | Final resume, notes, and outcome | `archive/2026/` |

## Git Commit Conventions

Use short, specific commit messages. Prefer one logical change per commit.

| Prefix | Use For | Example |
| --- | --- | --- |
| `resume:` | Resume edits or generated versions | `resume: tailor backend version for fintech roles` |
| `cover-letter:` | Cover letter changes | `cover-letter: draft platform engineer version` |
| `profile:` | LinkedIn, GitHub, portfolio updates | `profile: refresh GitHub project descriptions` |
| `interview:` | Interview preparation notes | `interview: add postgres indexing scenarios` |
| `application:` | Company-specific application materials | `application: add Acme backend role tracker` |
| `archive:` | Moving inactive material | `archive: store Q1 application package` |
| `chore:` | Repository maintenance | `chore: update gitignore for exports` |

## Checklists

### Resume

- [ ] Master resume reflects the latest role, scope, and measurable outcomes.
- [ ] Each targeted resume matches the target role and seniority level.
- [ ] Top summary is specific, credible, and keyword-aligned.
- [ ] Skills section prioritizes technologies used professionally.
- [ ] Experience bullets include scope, action, technical detail, and impact.
- [ ] PDF export has been reviewed for formatting, links, and page breaks.

### LinkedIn

- [ ] Headline matches the target market and current positioning.
- [ ] About section aligns with the master summary.
- [ ] Experience section includes quantified achievements.
- [ ] Featured section links to portfolio projects, writing, or case studies.
- [ ] Skills and endorsements reflect current role targets.
- [ ] LinkedIn export is saved in `master/linkedin-export.pdf`.

### GitHub

- [ ] Profile README communicates technical focus clearly.
- [ ] Pinned repositories represent strongest current work.
- [ ] Project READMEs explain problem, architecture, setup, and tradeoffs.
- [ ] Public repositories avoid secrets, private data, and unfinished experiments.
- [ ] Contribution history supports the professional narrative.

### Portfolio

- [ ] Project list includes business context and technical ownership.
- [ ] Each project has concise impact metrics where possible.
- [ ] Website links, GitHub links, and article links are current.
- [ ] Screenshots or diagrams are polished and stored under `assets/`.
- [ ] Portfolio content aligns with the resume version being used.

### Interview Preparation

- [ ] Java, Spring, PostgreSQL, and system design notes are reviewed.
- [ ] Behavioral stories use a clear situation, action, result structure.
- [ ] Salary range, constraints, and negotiation points are documented.
- [ ] Questions for hiring manager, peers, and recruiters are prepared.
- [ ] Recent projects can be explained at architecture and implementation levels.

### Job Applications

- [ ] Company research is saved before applying.
- [ ] Resume is tailored to the job description.
- [ ] Cover letter or outreach message is customized.
- [ ] Application date, role link, contact, and status are tracked.
- [ ] Follow-up reminders are scheduled.
- [ ] Outcome and lessons learned are archived.

## TODO

- [ ] Add the current master resume content.
- [ ] Export a fresh LinkedIn profile PDF.
- [ ] Add recent achievements with metrics.
- [ ] Create the first company application tracker.
- [ ] Refresh GitHub and portfolio project descriptions.
- [ ] Add certification verification links and renewal dates.
- [ ] Review interview notes before active applications.
