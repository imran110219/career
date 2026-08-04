# Testing Preparation

Testing is a high-priority evidence-capture area, not an unsupported skill. Professional evidence records JUnit, Mockito, Spring Boot Test, and Postman use for unit, API, and integration testing during pull-request validation across multiple projects. A project-specific example and outcome still need capture.

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

Current evidence supports professional pull-request validation using JUnit, Mockito, Spring Boot Test, and Postman, alongside Locust load testing and Jenkins use for the exam-management system. Treat automated testing as `Practising` with professional evidence. Testcontainers is hands-on lab/personal-project evidence only; do not present it as professional-project use. Capture one representative PR, including its scope and outcome, before making broader ownership or quality-impact claims.
