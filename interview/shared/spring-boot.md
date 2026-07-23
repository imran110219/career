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
- Add integration tests with PostgreSQL and a security boundary.
- Create a transaction propagation example that demonstrates rollback behavior.
- Document a production troubleshooting checklist for one Spring service.

## Evidence Notes

Spring Boot, Hibernate, REST APIs, Keycloak, Redis, RabbitMQ, Jenkins and GitHub Actions are recorded in [skills inventory](../../master/skills-inventory.md), but automated testing depth and observability ownership remain evidence gaps in [skill gaps](../../master/skill-gaps.md).
