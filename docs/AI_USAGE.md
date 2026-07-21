# AI Usage Guide

This guide explains how to use AI effectively with this career repository.

## How To Start A Future AI Session

Paste this at the beginning of a new AI conversation:

```text
You are helping maintain my career repository. Read AGENTS.md, master/resume.md, master/achievements.md, and the relevant master inventories first. Do not invent facts. Label unclear items NEEDS REVIEW and preserve claim status, ownership, and disclosure limits.
```

For targeted resumes, add:

```text
Target role:
Target country or market:
Preferred resume length:
Job description:
```

## Recommended AI Workflow

| Task | Input To Provide | Expected Output |
| --- | --- | --- |
| Improve master CV | Latest profile, project details, metrics | Updated `master/resume.md` and exports |
| Tailor resume | Job description, target role, location | Updated `resumes/<role>/resume.docx` and `resume.pdf` |
| Write cover letter | Company name, role, job description | Updated `cover-letter.md` |
| Prepare interview | Role, company, interview type | Focused notes under `interview/` |
| Track application | Company, role link, recruiter, status | Company folder under `companies/applications/` |
| Update portfolio | Project links, screenshots, write-ups | Updated `portfolio/` files |

## Best Information To Provide

AI can produce much stronger career documents when the source information includes measurable proof.

### Current Role Details

```markdown
Company:
Role:
Dates:
Team size:
Product or platform:
Users or customers:
Tech stack:
Systems owned:
Major features delivered:
Performance improvements:
Reliability improvements:
Security improvements:
Leadership responsibilities:
Business impact:
```

### Achievement Format

Use this pattern:

```markdown
Accomplished <result> by <action> using <technology or method>, improving <metric or business outcome>.
```

Examples based on current source material:

- Reduced system response time by 30% by implementing Redis caching.
- Built a real-time administrator dashboard associated with a reported 40% increase in system usage.
- Deployed an exam management system used by 2,500+ administrators, 1,000 exam invigilators, and 1,000 examinees.

## Resume Optimization Rules

| Rule | Why It Matters |
| --- | --- |
| Lead with the target role | Recruiters scan for fit quickly. |
| Put strongest evidence in the top half | The first page carries most screening weight. |
| Keep current role strongest | Recent impact matters most. |
| Use metrics where available | Numbers make seniority and impact credible. |
| Remove weak or outdated details | Older technologies should not distract from target positioning. |
| Match keywords honestly | ATS alignment helps, but unsupported keyword stuffing hurts interviews. |

## Targeting Guidance

### Senior Backend Engineer

Emphasize:

- Java, Spring Boot, Hibernate, REST APIs.
- PostgreSQL and database modeling.
- Redis caching and performance optimization.
- Secure backend systems with Keycloak.
- Production systems used by large user groups.

### Lead Backend Engineer

Emphasize:

- Team mentoring.
- Grooming, planning, code review.
- Delivery ownership.
- Stakeholder collaboration.
- Architecture decisions and execution quality.

### Software Architect

Emphasize:

- Distributed systems.
- System design.
- API architecture.
- Data modeling.
- Authentication and authorization.
- Long-term maintainability and scalability.

### Platform Engineer

Emphasize:

- DevOps and SRE learning path.
- Performance, caching, reliability.
- Deployment and maintenance.
- Developer workflow improvements.
- Observability details if available.

### Engineering Manager

Emphasize:

- Mentoring and team leadership.
- Planning and delivery.
- Stakeholder communication.
- Code review culture.
- Technical credibility from backend experience.

## AI Review Checklist

Before accepting AI-generated career content:

- [ ] All facts are true.
- [ ] Dates are correct.
- [ ] Metrics are accurate and defensible.
- [ ] No confidential client or employer details are exposed.
- [ ] Tone sounds like a senior engineer, not a marketing brochure.
- [ ] Bullets are specific enough to discuss in an interview.
- [ ] The resume version matches the target job.
- [ ] Markdown source and generated documents are in sync.
- [ ] Public builds use `config/contact-public.yml`; private contact data is read only from ignored local configuration.
- [ ] Planned project features are not described as delivered.

## File Maintenance Rules

- Update `master/resume.md` before updating generated documents.
- Keep role-specific resumes focused; do not copy every master detail into every resume.
- Store job-specific research under `companies/applications/<company>/`.
- Move obsolete outputs to `archive/2026/` or `archive/old/`.
- Add important changes to `CHANGELOG.md`.

## High-Value Next Prompts

```text
Use AGENTS.md. Create a senior-backend targeted resume from master/resume.md, optimized for Java Spring Boot backend roles.
```

```text
Use AGENTS.md. Ask me only for missing high-impact details needed to make my Penta Global experience stronger.
```

```text
Use AGENTS.md. Rewrite my resume bullets to be more achievement-driven while preserving all facts.
```

```text
Use AGENTS.md. Create a company application folder and tailor my resume and cover letter for this job description: <paste JD>.
```
