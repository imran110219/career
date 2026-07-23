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

## Evidence Notes

RabbitMQ use is recorded for the election platform. Message-flow ownership, delivery guarantees, retry behavior, and production outcomes still need evidence review before being expanded in résumés.
