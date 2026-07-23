# Skill Gaps and Evidence Backlog

This file separates market-demand skills from verified experience. An entry here is **not evidence that the skill is absent**; it means the repository does not yet contain resume-safe proof of current, hands-on experience.

Use this list to prioritize learning, projects, and evidence capture. Move a skill to `master/skills-inventory.md` only after recording a concrete project or role example and confirming it is interview-defensible.

## Current Job-Description Signals

This backlog was refreshed against these public role descriptions on 2026-07-23:

- [`micro1 Backend Engineer`](../job-descriptions/micro1-backend-engineer.md): remote backend role seeking cloud, containers, NoSQL, CI/CD, automated testing, and event-driven or serverless familiarity.
- [`InScale / Teletrac Navman Senior Java Developer`](../job-descriptions/inscale-senior-java-developer.md): fully remote Java role seeking AI-assisted development, AWS/DevOps, test automation and CI, and microservices with messaging or streaming.

The table records repeat market signals across those roles. It does not turn any of them into resume claims.

| Recurring signal | Job-description source | Backlog treatment |
| --- | --- | --- |
| Automated testing and CI/CD | micro1, InScale | Highest-priority evidence gap. |
| AWS/cloud and DevOps delivery | micro1, InScale | Highest-priority evidence gap. |
| Messaging, streaming, and event-driven design | micro1, InScale | Targeted backend-expansion gap. |
| NoSQL data-store experience | micro1 | Targeted backend-expansion gap. |
| AI-assisted development tools | InScale | New evidence gap. |

## Highest Priority for Senior Backend Roles

| Gap | Why it matters | Current repository evidence | Evidence needed before resume use |
| --- | --- | --- | --- |
| Automated testing | Required or preferred by both current job descriptions. | No project-specific test-suite evidence recorded. | Frameworks used, unit/integration/contract test types, and an example of ownership or quality impact. |
| CI/CD | Both roles seek delivery ownership beyond implementation. | Deployment support is documented; CI/CD ownership is not. | Pipeline/tool, stages owned, deployment environment, and a concrete improvement. |
| Cloud platform | micro1 requests AWS, GCP, or Azure; InScale specifically names AWS in a DevOps environment. | No cloud-platform ownership recorded. Cloudflare file storage is documented for FactLens. | Provider, services used, deployment or operations responsibility, and scope. |

## Targeted Backend Expansion

| Gap | Why it matters | Current repository evidence | Evidence needed before resume use |
| --- | --- | --- | --- |
| Messaging / event-driven systems | InScale names Kafka, RabbitMQ, SQS, and Kinesis; micro1 prefers event-driven architectures. | No Kafka, RabbitMQ, or event-driven implementation recorded. | Technology, message flow, delivery/retry or ordering tradeoff, and production or project usage. |
| Serverless architecture | Preferred in the micro1 role and adjacent to the cloud/event-driven demand. | No serverless implementation or operations ownership is recorded. | Provider/service, trigger or event flow, deployment/monitoring responsibility, and project outcome. |
| NoSQL databases | micro1 requires relational and NoSQL proficiency. | Redis caching is documented; no NoSQL data-store ownership is recorded. | Database, data model, query/access pattern, and operational context. |
| AI-assisted development | InScale lists experience with AI-assisted development tools as a must-have. | No specific tool, workflow, review practice, or delivery example is recorded. | Tool(s) used, concrete engineering workflow, verification/quality safeguards, and a defensible delivery example. |
| Observability and reliability | Useful for production backend and platform-adjacent roles. | Logging, alerting, runbook, and operational-support statements exist, but no tool ownership or measured reliability outcome is recorded. | Tools, dashboards/alerts/traces, incident or error-rate impact, and scope. |

## Role-Track Boundaries

| Track | Missing evidence that limits targeting |
| --- | --- |
| Platform Engineer | Terraform, CI/CD platform engineering, cloud infrastructure ownership, advanced Kubernetes administration, observability, and SRE ownership. |
| Engineering Manager | Direct reports, hiring, formal feedback/performance reviews, promotions, capacity planning, team health, and budget ownership. |
| Software Architect | Formal architecture governance and long-term platform reliability or scale metrics. |

## Evidence Capture Template

When a gap is addressed, record the following before adding it to a resume:

- Project or employer and dates
- Personal ownership and collaborators
- Technology and level of use
- Technical decision, tradeoff, or problem solved
- Measurable outcome or operational result, if available
- Evidence location and disclosure level
