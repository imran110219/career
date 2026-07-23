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

## Practice Systems

- Election nomination and reporting platform.
- Healthcare resource search API.
- Audit log service.
- Notification platform.
- File upload and document processing service.
- Multi-tenant SaaS backend.

## Experience-Based Questions

- How would you define RTO and RPO for an election platform?
- How do you prevent retries from causing duplicate processing?
- When would you choose a modular monolith instead of microservices?
- How would you migrate a monolith toward independently deployable services?
- Where would you place audit logging in a sensitive workflow?
- What would you monitor first after a high-risk release?

## Evidence Notes

Use [projects](../projects/) case studies for experience-backed examples. Mark unknown capacity, SLA, deployment, or incident details as `Evidence needed`.
