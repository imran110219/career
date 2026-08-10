# System Design Preparation

This file provides the shared design framework. Architect-specific documentation and governance belong in [software-architect](../software-architect/README.md).

## Design Framework

| Step | Questions to answer |
| --- | --- |
| Clarify | Users, use cases, constraints, scale, latency, availability, consistency, compliance. |
| Requirements | Functional requirements, non-functional requirements, out-of-scope items. |
| Interfaces | APIs, events, authentication, authorization, idempotency, versioning. |
| Data | Entities, ownership, relationships, indexes, retention, audit needs. |
| Architecture | Services/modules, storage, queues, caches, external integrations. |
| Reliability | Timeouts, retries, backoff, DLQs, circuit breakers, failure recovery. |
| Operations | Metrics, logs, traces, alerts, runbooks, deployments, rollbacks. |
| Trade-offs | Simplicity versus scale, cost versus reliability, consistency versus availability. |
| Evolution | Migration path, compatibility, technical-debt containment. |

## Time-Boxed Interview Flow

Use this order for a 45–60 minute design interview. State assumptions explicitly when scale, SLO, data classification, or operational constraints are not provided.

| Time | Goal | What to cover |
| --- | --- | --- |
| 0–5 min | Frame the problem | Primary user journey, success condition, in/out of scope, known constraints, and clarifying questions. |
| 5–10 min | Define requirements | Prioritized functional requirements, quality attributes, correctness needs, privacy/compliance, and explicit assumptions. |
| 10–15 min | Estimate and choose a shape | Request rate, peak factor, payload/storage growth, read/write mix, availability target, and the simplest architecture that fits. |
| 15–25 min | Present the high-level design | Clients, API boundary, core modules/services, data stores, cache, queue, external systems, and ownership. |
| 25–35 min | Deep-dive the critical path | API/event contract, data model, state transitions, idempotency, authorization, transaction boundary, and sequence of calls. |
| 35–45 min | Handle failure and scale | Timeouts, retries, duplicate work, backpressure, consistency, partitioning/caching/replicas only where justified, and recovery. |
| Final minutes | Operate and evolve | SLIs/SLOs, logging/metrics/tracing, alerts, rollout/rollback, migrations, trade-offs, and deferred work. |

Do not try to design every subsystem. Spend depth on the highest-risk workflow and name the assumptions that could change the design.

## Clarifying Questions and Assumptions

Ask questions that materially change the design:

- Who are the users and which workflow must never lose, duplicate, or expose data?
- What are the expected and peak request rates, read/write mix, payload sizes, retention, and growth? If unknown, choose conservative assumptions and label them.
- Which operations need strong read-after-write behavior or atomic state transitions, and which can be eventually consistent?
- What latency, availability, recovery-time (RTO), and data-loss (RPO) targets matter? Treat them as design assumptions unless project evidence verifies them.
- Is the system multi-tenant? What data is sensitive, who may access it, and what audit/retention rules apply?
- Which external dependencies exist, and what must happen when they are slow, unavailable, or send duplicates?
- What existing systems, deployment constraints, team boundaries, or migration limits must be respected?

Separate functional requirements from quality attributes and explicitly state out-of-scope features. This prevents adding complexity for hypothetical needs.

## Estimation and Capacity Reasoning

Use rough estimates to justify design choices, not to create false precision:

1. Estimate average and peak requests per second from active users, request frequency, and a peak multiplier.
2. Estimate data growth from records per day, average record/file size, retention period, replication, and index overhead.
3. Identify the dominant read/write paths and whether bursts, reports, or uploads need separate treatment.
4. Reserve headroom for traffic spikes, retries, background work, maintenance, and failover.
5. State what you would measure before final capacity decisions: latency percentiles, database CPU/I/O, queue depth, connection utilization, cache hit rate, and dependency behavior.

For example, say “I would start with a modular service and a relational database because the assumed volume is moderate and the workflow needs transactions; I would introduce a queue or read model only after a measured bottleneck or decoupling need.” Avoid presenting unverified project volumes as facts.

## High-Level Design and Data Boundaries

Start with the smallest maintainable architecture that satisfies the requirements. A modular monolith is often a good default when independent scaling, deployment, team ownership, or data isolation is not yet justified.

- Define module/service ownership around business capabilities, not technical layers alone. Name the owner of each mutable data set and avoid shared-write databases across independently deployed services.
- Describe API contracts: resource/action, authentication/authorization, validation, idempotency key or natural uniqueness constraint where duplicates matter, response/error contract, and versioning/compatibility plan.
- Model the critical entities, identifiers, relationships, lifecycle states, indexes, audit fields, retention, and privacy classification. Constraints enforce invariants that application code alone cannot reliably protect.
- Use synchronous calls when the caller needs an immediate, bounded answer. Use asynchronous messaging for durable decoupling, long-running work, or independent consumers—but define delivery, ordering, duplicate, and failure behavior.
- Add caches, read replicas, search systems, partitioning, or separate read models only when an access pattern and measurement justify their consistency and operational cost.

## Critical Workflow Template

For the most important write path, narrate a sequence like this:

1. Authenticate and authorize the caller, including resource/tenant ownership where relevant.
2. Validate the request and apply an idempotency rule before irreversible work.
3. Perform the local transaction: validate allowed state transition, write the authoritative record, enforce uniqueness/constraints, and record an audit event if required.
4. Publish downstream work reliably. If a message must agree with the database update, use an outbox-like pattern or a documented reconciliation process rather than assuming a dual write is atomic.
5. Make consumers idempotent and able to handle retries, duplicates, delay, reordering where applicable, and poison messages.
6. Return a response that reflects completed versus accepted-for-processing work. Provide status/reconciliation paths for asynchronous operations.

Draw the sequence for the caller, core service, database, and one dependency or worker. Then name the failure behavior at each boundary: timeout, retry, duplicate request, dependency outage, partial completion, and recovery.

## Reliability, Consistency, and Recovery

- Set bounded timeouts for every network call. Retries must be selective, bounded, backed off with jitter, and safe through idempotency; retrying all failures can amplify an outage.
- Use circuit breakers, concurrency limits, rate limits, queues, or load shedding to protect the system when a dependency or downstream store is saturated. Define the user-visible degraded behavior.
- Treat DLQs as an investigation and recovery mechanism, not a place where failures disappear. Define alerting, inspection, replay safeguards, and ownership.
- Use strong consistency for correctness-sensitive state transitions; accept eventual consistency only with a visible freshness/reconciliation model. Read replicas and caches can return stale data.
- Design for reconciliation: identify authoritative state, record correlation identifiers, make repair actions safe, and retain enough audit data to investigate discrepancies.
- State disaster-recovery goals in RPO/RTO terms. Backups, replication, and failover need restore testing, ownership, and a runbook; replicas alone are not backups.

## Security, Privacy, and Multi-Tenancy

- Validate identity and enforce authorization at every relevant boundary. Roles alone may be insufficient; check resource ownership, tenant membership, and workflow state.
- Keep tenant identifiers server-controlled and include tenant/ownership predicates in data access. Test cross-tenant and object-level authorization failures.
- Minimize collection and retention of sensitive data; encrypt in transit, use appropriate encryption/storage controls at rest, protect secrets, and avoid sensitive values in logs, events, and metrics.
- Design audit records around the question they must answer: actor, action, target, time, result, correlation identifier, and appropriate tamper/retention requirements. Avoid recording secrets or unnecessary personal data.
- Use threat modeling to identify spoofing, privilege escalation, data exposure, unsafe uploads, dependency compromise, and denial-of-service risks for the critical path.

## Operations, Rollout, and Evolution

- Define SLIs that represent user outcomes: successful request rate, latency percentile, queue processing age, freshness, or workflow completion. Choose SLOs and alerts only after agreeing on service importance and expected behavior.
- Instrument the critical path with structured logs, metrics, traces/correlation IDs, dependency health, database/pool signals, and business counters. Do not claim ownership of a specific observability stack unless evidence supports it.
- Release safely with backward-compatible API/event changes, feature flags or controlled rollout where appropriate, clear ownership, monitoring, and a rollback or forward-recovery plan.
- Use expand/contract migration for data/schema changes: add compatible structures, deploy compatibility code, backfill/validate, switch traffic, then retire old paths after the transition.
- Review significant decisions using a lightweight ADR: context, decision, alternatives, consequences, owner, review trigger, and evidence. Revisit decisions when scale, organization, or constraints change.

## Production-Ownership Answer Structure

For every design decision, connect it to the workflow impact and risk, the evidence or assumptions used, the simplest safe design, the trade-offs rejected, and the operational work required to keep it reliable. Use an experience-backed example only within verified scope; otherwise present the answer as a proposed design or lab exercise.

## Practice Systems

- Election nomination and reporting platform.
- Healthcare resource search API.
- Audit log service.
- Notification platform.
- File upload and document processing service.
- Multi-tenant SaaS backend.

## Practice Deliverable

For each practice system, produce a one- to two-page design outline:

1. Requirements, non-goals, assumptions, and rough estimates.
2. A high-level component diagram and one critical-path sequence diagram.
3. API/event contract and minimal data model with ownership and key constraints.
4. Three failure modes with mitigation, recovery, and prevention.
5. Security/privacy boundaries and audit needs.
6. SLIs/operational signals, rollout/migration plan, and three explicit trade-offs.
7. Evidence label for every project-specific statement: professional evidence, personal project evidence, lab/proposed design, or `Evidence needed`.

## Experience-Based Questions

- How would you define RTO and RPO for an election platform?
- How do you prevent retries from causing duplicate processing?
- When would you choose a modular monolith instead of microservices?
- How would you migrate a monolith toward independently deployable services?
- Where would you place audit logging in a sensitive workflow?
- What would you monitor first after a high-risk release?

## Evidence Notes

Use [projects](../projects/) case studies for experience-backed examples. Mark unknown capacity, SLA, deployment, incident, topology, or performance details as `Evidence needed`. The project cases support technical discussion within their recorded scope; they do not establish broad production-operations, architecture-governance, or reliability-ownership claims.
