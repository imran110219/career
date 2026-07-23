# Architecture Patterns

## Pattern Comparison

| Pattern | Use when | Watch-outs |
| --- | --- | --- |
| Layered architecture | Team needs familiar separation across API, service and persistence layers. | Can become anemic or tightly coupled if boundaries are weak. |
| Modular monolith | Domain boundaries are useful but independent deployment is not yet justified. | Requires discipline around module dependencies and data ownership. |
| Hexagonal architecture | External systems, databases and frameworks should be replaceable at the edges. | Can add ceremony if the domain is small. |
| Clean architecture | Business rules need isolation from delivery mechanisms. | Over-abstraction can slow simple CRUD workflows. |
| Microservices | Independent scaling, deployment or ownership justifies operational cost. | Distributed data, testing, observability and release coordination become harder. |
| Event-driven architecture | Loose coupling and asynchronous workflows matter. | Ordering, replay, idempotency and debugging need explicit design. |
| Service-oriented architecture | Enterprise integration and service reuse are central. | Service contracts and ownership can become unclear. |
| CQRS | Read and write models have different needs. | Adds consistency and synchronization complexity. |
| Event sourcing | Full state history is a core requirement. | Operational, query and migration complexity are high. |
| Serverless | Event-driven workloads benefit from managed scaling and low ops. | Cold starts, observability and vendor coupling must be considered. |

## Documentation Artifacts

- C4 context diagram.
- C4 container diagram.
- C4 component diagram.
- Sequence diagram.
- Deployment diagram.
- Data-flow diagram.
- Architecture Decision Record.
- Threat model.
- Non-functional requirements sheet.
- Capacity estimate.
- Reliability target.
- Migration roadmap.

## Practice Questions

- When would you keep a system as a modular monolith?
- What evidence justifies splitting a service?
- How would you define data ownership across services?
- How would you document and revisit an architecture decision?
