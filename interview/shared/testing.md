# Testing Preparation

Testing is a high-priority evidence gap because [skill gaps](../../master/skill-gaps.md) records no project-specific test-suite ownership yet.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Unit tests | Boundaries, fast feedback, pure logic, mocks, parameterized tests. |
| Integration tests | Database, security, messaging, configuration, real framework behavior. |
| Testcontainers | PostgreSQL, Redis, external dependency simulation, CI runtime cost. |
| API tests | Contract behavior, validation, auth paths, error responses. |
| Contract testing | Consumer/provider compatibility, backward compatibility. |
| Test pyramid | Balancing confidence, speed, maintainability, and cost. |
| Test data | Builders, fixtures, migrations, isolation, deterministic cleanup. |
| Mocking trade-offs | Over-mocking, brittle tests, behavior versus implementation. |
| CI stages | Lint, unit, integration, security, performance smoke checks. |
| Reliability | Flaky-test prevention, retries, quarantine rules, diagnostics. |
| Performance and security | Locust, baseline testing, SAST, dependency and API security tests. |

## Experience-Based Questions

- How would you test a payment-linked workflow without hitting the real provider?
- When should a Spring Boot test use mocks versus Testcontainers?
- How would you prevent flaky integration tests in CI?
- What tests would you require before changing authorization rules?
- How would you structure tests for idempotent retry handling?
- What evidence would make automated testing résumé-safe?

## Practice Tasks

- Add a small lab or portfolio example with unit, integration, and API tests.
- Document a CI test-stage design: fast checks, integration checks, security checks, release gates.
- Create one test-data strategy note for PostgreSQL-backed APIs.
- Record implementation evidence in [EVIDENCE_LOG.md](../EVIDENCE_LOG.md) before promoting any résumé claim.

## Evidence Notes

Current repository evidence supports Locust load testing and Jenkins use for the exam-management system, but not broad automated test ownership. Treat this as `Practising` or `Implementing` until a concrete project example exists.
