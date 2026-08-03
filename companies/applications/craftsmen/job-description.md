# Craftsmen — Senior Backend Software Engineer

## Posting

- **Company:** Craftsmen
- **Role:** Senior Backend Software Engineer
- **Location:** Bangladesh
- **Source:** https://careers.craftsmensoftware.com/jobs/7482205-senior-backend-software-engineer
- **Captured:** 2026-08-03
- **Application status:** Researching — not marked as applied

## Role focus

Design, build, and operate backend systems that scale, remain reliable under load, and evolve without unnecessary complexity. The role emphasizes end-to-end ownership, architectural judgment, production debugging, and measurable reliability, latency, or efficiency improvements.

## Responsibilities

- Design and operate production backend systems; understand bottlenecks, trade-offs, and failure modes.
- Own services through design, implementation, deployment, monitoring, and production stability.
- Investigate production issues, mitigate impact, identify root causes, and implement durable fixes.
- Make architecture decisions that balance performance, cost, simplicity, and scalability.
- Improve reliability, latency, and efficiency; set engineering standards through reviews and design feedback.
- Mentor engineers and challenge unclear product or technical decisions when necessary.
- Use AI tools to accelerate development and reasoning while retaining critical evaluation and ownership.

## Requirements

### System design and scale

- Experience designing and operating meaningful production scale: high request volumes, large datasets, or multi-tenant systems.
- Ability to explain system architecture, bottlenecks, and latency/consistency/cost/complexity trade-offs.
- Experience evolving existing systems, not only greenfield development.

### Distributed systems and data

- Production experience with consistency, concurrency, and failure scenarios.
- Practical knowledge of eventual consistency, idempotency, retries, failure handling, queues, background jobs, and asynchronous workflows.
- Judgment about when distributed systems are useful versus unnecessarily complex.

### Production ownership and performance

- Direct involvement in incidents: debugging, mitigation, recovery, root-cause analysis, and prevention.
- Accountability for uptime, performance, and system health; ability to use logs, metrics, and tracing.
- Experience diagnosing CPU, memory, I/O, database, and network bottlenecks, with measurable improvements.

### Quality, leadership, and AI-assisted development

- Maintainable, testable, production-ready code; effective code reviews and design feedback.
- Technical decision-making under incomplete requirements and constraints.
- Daily, critical use of AI tools (e.g., Claude, Cursor, or Copilot) for iteration, debugging, edge cases, and option evaluation; must verify correctness before production use.
- Strong data-structures, algorithms, and software-design fundamentals; typically 7+ years of backend experience.

## Strong signals / nice to have

- High-scale or strict-SLA operations.
- AWS, GCP, or Azure.
- Docker and Kubernetes.
- Monolith/distributed-system migrations or simplification of over-engineered systems.
- Significant performance or infrastructure-cost improvements.
- Fast-moving product experience.

## Initial evidence mapping

| Job signal | Existing public-safe evidence | Preparation gap |
| --- | --- | --- |
| Production scale | Election platform: nearly 25 services; reported 50,000 users and ~100,000 daily requests during election periods | Clearly define personal ownership and operational safeguards. |
| Performance | Verified 30% response-time reduction using Redis; read-replica routing improved responsiveness, no measured delta | Capture baseline/after metrics for read replicas and query work. |
| Distributed systems | Microservices, RabbitMQ, payment/identity/reporting integrations | Prepare concrete idempotency, retry, ordering, and failure-handling examples. |
| Deployment and operations | Docker, Nginx, self-managed Kubernetes; 15 pre-election production deployments | Prepare incident, mitigation, RCA, and prevention stories. |
| Quality and leadership | Code reviews, task allocation, mentoring, SonarQube and Trivy CI checks | Prepare examples of standards raised and feedback that changed a design. |
| AI-assisted development | No candidate-specific evidence recorded | Document truthful examples and verification practices before claiming this requirement. |
| Cloud | Self-managed Kubernetes evidence | Cloud-provider experience is not currently evidenced. |

