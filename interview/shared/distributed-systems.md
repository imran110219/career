# Distributed Systems Preparation

Use this for backend and architecture interviews where service interaction and failure handling matter.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Communication | Synchronous APIs versus asynchronous messaging, coupling, latency, failure modes. |
| Messaging | RabbitMQ, queues, exchanges, delivery guarantees, acknowledgements. |
| Event-driven design | Producers, consumers, schemas, ordering, replay, eventual consistency. |
| Reliability patterns | Retries, exponential backoff, dead-letter queues, circuit breakers, timeouts, bulkheads. |
| Correctness | Idempotent consumers, duplicate processing, distributed transactions, saga pattern. |
| Caching | Cache invalidation, stampede prevention, TTLs, consistency trade-offs. |
| Platform patterns | Service discovery, API gateways, observability, deployment coordination. |

## Experience-Based Questions

- How do you prevent retries from causing duplicate processing?
- What would you put in a dead-letter queue investigation runbook?
- When is eventual consistency acceptable in an election or payment-linked workflow?
- How would you coordinate API and event contract changes across teams?
- When would you avoid microservices and choose a modular monolith?
- How would you debug failure across SMS, payment, identity, and reporting integrations?

## Practice Tasks

- Write a message-flow note for one verified RabbitMQ-backed workflow, with unknowns marked `Evidence needed`.
- Design retry, timeout, and idempotency behavior for one project case study.
- Add an observability plan for a distributed transaction or saga-like workflow.

## Production-Ownership Answer Structure

For a production-focused senior-backend interview, answer each incident or failure-mode question in this order:

1. State the customer or workflow impact and the immediate safety/correctness concern.
2. Explain the signals used to narrow the issue: logs, metrics, traces, queue depth, database queries, deployment history, or dependency health.
3. Describe mitigation before deep diagnosis: rollback, traffic control, retry pause, safe degradation, or manual recovery as appropriate.
4. Explain the root cause and the rejected alternatives, including consistency, latency, cost, or complexity trade-offs.
5. Finish with prevention: idempotency, timeout/retry policy, alert, dashboard, test, runbook, or architecture simplification.

Keep professional examples factual. Use a proposed design when tool-specific production evidence is unavailable.

## Evidence Notes

RabbitMQ use is recorded for the election platform. Message-flow ownership, delivery guarantees, retry behavior, and production outcomes still need evidence review before being expanded in résumés.
