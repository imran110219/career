# Skill Gaps and Evidence Backlog

This file separates market-demand skills from verified experience. An entry here is **not evidence that the skill is absent**; it means the repository does not yet contain resume-safe proof of current, hands-on experience.

Use this list to prioritize learning, projects, and evidence capture. Move a skill to `master/skills-inventory.md` only after recording a concrete project or role example and confirming it is interview-defensible.

## Current Job-Description Signals

This backlog was refreshed against these public role descriptions on 2026-11-09:

- [`micro1 Backend Engineer`](../job-descriptions/micro1-backend-engineer.md): remote backend role seeking cloud, containers, NoSQL, CI/CD, automated testing, and event-driven or serverless familiarity.
- [`InScale / Teletrac Navman Senior Java Developer`](../job-descriptions/inscale-senior-java-developer.md): fully remote Java role seeking AI-assisted development, AWS/DevOps, test automation and CI, and microservices with messaging or streaming.
- [`Craftsmen Senior Backend Software Engineer`](../companies/applications/craftsmen/job-description.md): Bangladesh-based senior backend role centered on production ownership, distributed-systems failure handling, measurable performance, engineering judgment, and AI-assisted development.
- [`Camunda Senior Architect`](../companies/applications/camunda-senior-architect/job-description.md): global-remote architecture role emphasizing enterprise process orchestration, BPMN, stakeholder discovery, integrations, and production agentic automation.
- [`Silent Eight Solution Architect`](../worldwide-remote-jobs.csv): APAC-facing customer architecture role emphasizing Kubernetes troubleshooting, cloud/on-premise deployment, customer delivery, and regulated-industry implementations.
- Recent worldwide-remote search signals: AI platform/GPU infrastructure, production LLM systems, Rust edge networking, proxy infrastructure, and customer-facing solution architecture. These are market signals only and are not candidate claims.

The table records repeat market signals across those roles. It does not turn any of them into resume claims.

| Recurring signal | Job-description source | Backlog treatment |
| --- | --- | --- |
| Production ownership, incident response, and reliability | Craftsmen | Highest-priority interview and evidence gap. |
| Measurable performance and efficiency | Craftsmen, micro1, InScale | Highest-priority evidence-capture gap. |
| Automated testing | micro1, InScale | Highest-priority evidence gap. |
| AWS/cloud and DevOps delivery | micro1, InScale, Craftsmen | Targeted backend-expansion gap; not required for every role. |
| Messaging, streaming, and event-driven design | micro1, InScale, Craftsmen | High-priority senior-backend depth gap. |
| NoSQL data-store experience | micro1 | Targeted backend-expansion gap. |
| AI-assisted development tools | InScale, Craftsmen | High-priority evidence gap where explicitly required. |
| Enterprise process orchestration and BPMN | Camunda | Targeted architect expansion gap; workflow and service-integration experience exists, but formal BPMN and end-to-end process-consulting evidence is not recorded. |
| Customer-facing solution architecture | Camunda, Silent Eight | Architect/solution-architect gap; technical stakeholder collaboration is recorded, but independent discovery workshops, proof-of-value ownership, and customer-facing delivery outcomes need evidence. |
| Production agentic/LLM systems | Camunda, recent remote roles | Optional specialization gap; no production LLM or agentic-system delivery is recorded. |

## Highest Priority for Senior Backend Roles

| Gap | Why it matters | Current repository evidence | Evidence needed before resume use |
| --- | --- | --- | --- |
| Production incident ownership | Craftsmen expects independent debugging, mitigation, recovery, RCA, and long-term prevention. This is central to production-owning senior-backend roles. | Deployment troubleshooting, distributed-integration investigation, validation/logging/runbook improvement, and 15 pre-election production deployments are recorded; no complete incident narrative or measured recovery outcome is recorded. | One or more truthful incident stories: context, symptoms, personal role, logs/metrics/traces or queries used, mitigation, root cause, prevention, and outcome. |
| Production observability | Craftsmen explicitly requires diagnosing with logs, metrics, and tracing. | Operational-support statements exist, but no tool-specific monitoring or tracing ownership is recorded. | Tool(s), signals/dashboards/alerts, trace or log investigation example, and scope. Do not claim tools not used. |
| Measurable system performance | Craftsmen expects latency, throughput, efficiency, or cost improvements. | Verified 30% response-time reduction with Redis; read-replica routing improved responsiveness and primary-database load, without a recorded delta. | Before/after baseline, measurement method, workload, personal contribution, and trade-offs for performance or efficiency work. |
| Automated testing | Required or preferred by both current job descriptions. | Professional use of JUnit, Mockito, Spring Boot Test, and Postman for unit, API, and integration testing in pull-request validation is recorded. Testcontainers is lab/personal-project evidence only. | One project-specific example, ownership boundary, CI scope if applicable, and quality outcome. |
| CI/CD and release ownership | These roles value safe delivery and production responsibility; Craftsmen also values deployment through stable operation. | CI/CD pipeline use across projects, GitHub Actions, Jenkins, Docker, Nginx, Kubernetes deployment support, and pre-election deployments are recorded. | For broader ownership claims: release gates, rollback decision, deployment environment, personal scope, and a concrete reliability or delivery improvement. |
| Cloud platform | micro1 requests AWS, GCP, or Azure; InScale specifically names AWS; Craftsmen lists cloud as a strong signal. | No cloud-platform ownership recorded. Cloudflare file storage is documented for FactLens. | Provider, services used, deployment or operations responsibility, and scope. |

## Targeted Backend Expansion

| Gap | Why it matters | Current repository evidence | Evidence needed before resume use |
| --- | --- | --- | --- |
| Messaging / event-driven systems | InScale names Kafka, RabbitMQ, SQS, and Kinesis; micro1 prefers event-driven architectures; Craftsmen expects practical idempotency, retries, and asynchronous failure handling. | RabbitMQ use is recorded for the election-management platform. | Message flow, personal ownership, delivery/retry/ordering/idempotency tradeoff, failure-handling approach, and production outcome. |
| Serverless architecture | Preferred in the micro1 role and adjacent to the cloud/event-driven demand. | No serverless implementation or operations ownership is recorded. | Provider/service, trigger or event flow, deployment/monitoring responsibility, and project outcome. |
| NoSQL databases | micro1 requires relational and NoSQL proficiency. | Redis caching is documented; no NoSQL data-store ownership is recorded. | Database, data model, query/access pattern, and operational context. |
| AI-assisted development | InScale and Craftsmen list active, critically evaluated AI-tool use as required. | Candidate-confirmed use of OpenAI Codex and Claude for agentic programming is recorded at skills level; workflow, review practice, safeguards, and outcomes are not yet documented. | Tool(s) used, concrete engineering workflow, verification/quality safeguards, privacy controls, and a defensible delivery example. |

## Role-Track Boundaries

| Track | Missing evidence that limits targeting |
| --- | --- |
| Platform Engineer | Terraform, CI/CD platform engineering, cloud infrastructure ownership, advanced Kubernetes administration, observability, and SRE ownership. |
| Engineering Manager | Direct reports, hiring, formal feedback/performance reviews, promotions, capacity planning, team health, and budget ownership. |
| Software Architect | Formal architecture governance and long-term platform reliability or scale metrics. |

## Recent Specialized Signals

These topics appeared in the 2026-11-09 worldwide-remote search but should remain optional unless a target vacancy makes them central:

| Topic | Current evidence | Treatment |
| --- | --- | --- |
| ML platform engineering and GPU infrastructure | No verified production ML-platform, GPU scheduling, Flyte/Ray, or model-training infrastructure experience. | Optional; do not prioritize over backend fundamentals. |
| Rust edge/proxy infrastructure | No verified professional Rust, proxy-gateway, NAT, or residential-fleet infrastructure experience. | Low priority; reject roles requiring deep Rust/proxy experience. |
| BPMN and enterprise process mining | Workflow and distributed-service design are recorded; formal BPMN modeling and process-mining tools are not. | Targeted architect learning topic. |
| Customer-facing architecture delivery | Technical collaboration and delivery guidance are recorded; independent customer workshops and proof-of-value ownership are not. | Practise stories and document evidence before claiming solution-architecture depth. |

## Evidence Capture Template

When a gap is addressed, record the following before adding it to a resume:

- Project or employer and dates
- Personal ownership and collaborators
- Technology and level of use
- Technical decision, tradeoff, or problem solved
- Measurable outcome or operational result, if available
- Evidence location and disclosure level
