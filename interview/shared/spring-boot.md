# Spring Boot Preparation

Use this for shared Spring Boot review. Keep role-specific delivery stories in the role folders.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Dependency injection | Constructor injection, bean lifecycle, scopes, circular dependencies, testability. |
| Configuration | Auto-configuration, configuration properties, profiles, environment separation. |
| Web APIs | Controllers, validation, global exception handling, filters, interceptors. |
| Security | Spring Security, JWT, OAuth2, OpenID Connect, Keycloak, method security, CORS and CSRF. |
| Transactions | Boundaries, propagation, isolation, rollback rules, distributed workflow limits. |
| Persistence | JPA fetching, N+1 problems, pagination, batching, custom queries. |
| Caching and async | Cache invalidation, Redis patterns, async processing, executor sizing. |
| Operations | Actuator, health checks, metrics, logging, tracing, production troubleshooting. |
| Testing | Unit tests, slice tests, integration tests, Testcontainers, security tests. |

## Secure Endpoint Answer Framework

For “walk me through a Spring Boot endpoint” questions, describe the request path in this order:

1. Authenticate the caller and establish the security context; authorize the action and resource access at the appropriate boundary.
2. Bind and validate a purpose-built request DTO. Reject malformed or unauthorized input before business processing; do not bind external input directly to persistence entities.
3. Keep the controller thin: translate HTTP concerns to an application/service call and return a stable response contract.
4. Put business rules and the transaction boundary in the service layer. Keep transactions short and avoid remote calls, unbounded work, or slow file operations inside them.
5. Use repositories or a deliberately chosen SQL layer for persistence. Make query shape, pagination, locking, and constraints explicit when they affect correctness or scale.
6. Translate expected domain failures into consistent, safe API errors. Log enough context for diagnosis without exposing tokens, personal data, or internal implementation details.
7. Add tests and observability appropriate to the risk: authorization, validation, happy and failure paths, latency/error signals, and audit requirements.

State the business outcome and correctness risk before implementation details. For example, an idempotent submission endpoint needs a durable uniqueness/idempotency decision, not merely a retry annotation.

## Transactions and Persistence

- `@Transactional` is normally applied through a Spring proxy. A self-invocation does not pass through that proxy, so its transactional annotation may not take effect. Put boundaries in a separate Spring-managed component or structure calls intentionally.
- Know rollback rules: runtime exceptions normally trigger rollback; checked exceptions require explicit configuration if they should roll back. Do not catch and suppress an exception inside a transaction without deliberately handling its rollback implications.
- Choose propagation for a business reason. `REQUIRED` joins or starts the normal business transaction; `REQUIRES_NEW` creates an independent transaction but can complicate consistency, connections, and failure behavior. Avoid using propagation as a substitute for workflow design.
- Choose isolation and locking with the database's actual behavior in mind. Keep database transactions local; do not present distributed transactions across HTTP or messaging as an automatic Spring capability.
- Diagnose N+1 queries by observing emitted SQL and query counts under representative data. Fix only the required access path with fetch joins, entity graphs, batching, projections, or a dedicated query; do not make every association eagerly loaded.
- Be careful combining collection fetch joins with pagination: duplicated rows and in-memory pagination can produce incorrect or expensive behavior. Often page root IDs first, then fetch the required graph.
- Use JPA for ordinary domain persistence. Choose JDBC or native SQL for data-heavy, database-specific, batch, reporting, or performance-sensitive queries when it is clearer and easier to verify. Keep parameterization, transaction behavior, and tests.

## Security and API Boundaries

- Separate authentication (who is the caller) from authorization (what may that caller do to this resource). Verify both role/permission checks and ownership or tenant boundaries where relevant.
- For JWT/OAuth2 resource servers, validate issuer, signature, expiry, audience where applicable, and claim-to-authority mapping. Do not trust a client-provided role or user identifier as an authorization decision.
- With Keycloak or another identity provider, explain the boundary: the identity provider issues identity/claims; the service maps and enforces its own authorization rules. Test missing, malformed, expired, insufficient-role, and cross-tenant cases.
- CORS controls which browser origins may make cross-origin requests; it is not authentication. CSRF primarily matters for browser-based cookie/session authentication and is not a reason to disable all security controls for a bearer-token API without understanding the client model.
- Centralize cross-cutting, expected HTTP error formatting in `@ControllerAdvice`; keep domain decisions in the application layer. Return stable public codes/messages and correlation identifiers, not stack traces or internal exception text.
- Use DTOs and explicit serialization rules to avoid mass assignment and accidental exposure of sensitive fields. Apply request-size, content-type, and upload controls where endpoints accept them.

## Caching, Async Work, and Resilience

- Cache only data with an understood freshness and authorization model. Define keys, TTL, invalidation/update behavior, stampede protection, and what happens on a cache miss or outage.
- Never treat a cache as the source of truth for a sensitive workflow without a deliberate consistency design. Scope cached data so one user's or tenant's data cannot be served to another.
- `@Async` changes execution context and failure handling. Use bounded executors, define queue/rejection behavior, propagate needed security/logging context safely, and surface exceptions rather than losing them in background threads.
- Retries belong at a clearly owned boundary and must be bounded, back off, and be safe for the operation. Pair retries with idempotency, timeouts, and circuit-breaking or load-shedding decisions where dependencies can fail.
- Use scheduled/background work with a single-execution or coordination strategy when multiple service instances exist; otherwise every replica may run the same job.

## Production Troubleshooting

For a service that is healthy but timing out under load:

1. Establish customer impact, affected endpoints, error rate, latency distribution, traffic pattern, and the time of the first regression.
2. Compare the current deployment, configuration, dependencies, and database behavior with the last known-good state.
3. Use available logs, metrics, traces, thread dumps, heap evidence, pool utilization, database sessions, and downstream latency to narrow the bottleneck. Do not claim a specific observability tool unless it is supported by evidence.
4. Mitigate safely: rollback, reduce traffic, disable a noncritical feature, adjust a proven safe limit, or degrade optional work before making broad capacity changes.
5. Confirm root cause and prevention: query/index work, bounded concurrency, timeout/retry correction, memory fix, test, alert, runbook, or deployment safeguard.

Common signals include HTTP latency/error rates, JVM heap and GC behavior, thread-pool queue/rejection rates, HikariCP checkout wait/active connections, downstream timeouts, database query latency, and recent configuration changes. A green health endpoint only proves the chosen health checks passed; it does not prove the service can meet its latency or correctness objective.

## Testing Strategy

- Unit tests are fast feedback for business rules and edge cases; mock collaborators only when the test remains meaningful.
- Slice tests validate a focused Spring layer, such as web MVC binding/validation/security or persistence mapping/query behavior, with less setup than a full application test.
- Integration tests validate real boundaries: Spring configuration, serialization, authorization, transaction behavior, migrations, and database interaction. Keep fixtures deterministic and clean up or isolate data.
- Use test cases for authorization boundaries, invalid input, expected domain failures, idempotency/duplicate delivery where relevant, and regression paths—not only happy paths.
- Testcontainers is a valid lab or personal-project approach for realistic PostgreSQL/Redis integration tests, but do not describe it as professional-project use until evidence supports that claim.

## Production-Ownership Answer Structure

For implementation, incident, and design questions: explain the workflow and correctness risk; the signals or tests used to understand it; the smallest safe mitigation or decision; the trade-offs considered; and the prevention work. Use a proposed design or lab example when the repository does not support a production-specific story.

## Experience-Based Questions

- Describe a transaction boundary that caused unexpected behavior.
- How would you find and fix an N+1 query problem?
- How would you secure APIs used by internal services and external clients?
- What belongs in a global exception handler, and what should stay local?
- How would you test authorization rules backed by Keycloak?
- How would you troubleshoot a Spring service that is healthy but timing out under load?
- When would you choose JPA, JDBC, or a hand-written SQL query?

## Practice Tasks

- Build a small endpoint with validation, consistent error responses, and OpenAPI documentation.
- Add integration tests with PostgreSQL, a security boundary, and representative failure cases.
- Create a transaction propagation example that demonstrates rollback behavior, self-invocation limitations, and a safe retry/idempotency decision.
- Capture emitted SQL for an N+1 example; fix it with the narrowest appropriate fetch or query strategy and compare query counts.
- Document a production troubleshooting checklist for one Spring service, including deployment comparison, JVM/pool/database signals, mitigation, and prevention.
- Design one cache and one async workflow with explicit freshness, authorization, timeout, failure, and multi-instance behavior.

## Evidence Notes

Spring Boot, Hibernate, REST APIs, Keycloak, Redis, RabbitMQ, Jenkins and GitHub Actions are recorded in [skills inventory](../../master/skills-inventory.md). Professional use of JUnit, Mockito, Spring Boot Test, and Postman in pull-request validation is also recorded. Automated testing depth, tool-specific observability ownership, complete incident narratives, and Testcontainers in professional projects remain evidence gaps in [skill gaps](../../master/skill-gaps.md).
