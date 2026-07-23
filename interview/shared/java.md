# Java Preparation

Use this as shared technical preparation for [Senior Backend](../senior-backend/README.md), [Lead Backend](../lead-backend/README.md), and [Software Architect](../software-architect/README.md) interviews.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Java 17 and 21 | Records, sealed classes, pattern matching, virtual-thread awareness, migration trade-offs, compatibility risk. |
| Collections | `HashMap`, ordering, complexity, concurrent collections, memory impact, choosing data structures under load. |
| Generics | Type safety, bounded types, wildcards, erasure, API design implications. |
| Immutability | Value objects, defensive copying, thread safety, JPA and serialization trade-offs. |
| Equality | `equals()` / `hashCode()` contracts, collection bugs, entity identity problems. |
| Streams and Optional | Readability, performance pitfalls, null handling, overuse in hot paths. |
| Exceptions | Checked versus unchecked exceptions, domain exceptions, API error mapping. |
| JVM memory and GC | Heap, stack, metaspace, allocation pressure, GC logs, leak diagnosis. |
| Concurrency | Thread safety, executors, locks, atomics, `CompletableFuture`, deadlock and starvation. |
| Performance | Profiling, heap dumps, flame graphs, query versus application bottlenecks. |
| Code quality | Clean code, refactoring, dependency boundaries, testing Java code. |

## Experience-Based Questions

- Describe a Java collection choice that affected performance or correctness.
- How would you diagnose a memory leak in a long-running Spring service?
- Where have you seen `equals()` and `hashCode()` cause production or test issues?
- How would you design a thread-safe cache with expiration?
- When would `CompletableFuture` help, and when would it make troubleshooting harder?
- How would you review AI-generated Java code before merging it?
- What Java 17 or 21 feature would you introduce cautiously in an existing backend?

## Practice Tasks

- Implement and test a small in-memory cache with expiry and concurrency protection.
- Refactor a service method to reduce mutation and improve testability.
- Compare iterative, stream-based, and concurrent implementations for one data-processing task.
- Capture notes on one JVM troubleshooting workflow: symptom, hypothesis, measurement, fix, verification.

## Evidence Notes

Professional Java and Spring Boot experience is recorded in [skills inventory](../../master/skills-inventory.md) and [achievements](../../master/achievements.md). Do not claim Java 21 production ownership until a project example is added to [EVIDENCE_LOG.md](../EVIDENCE_LOG.md).
