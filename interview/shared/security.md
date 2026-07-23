# Security Preparation

Security is part of backend and architecture readiness, not a separate job identity for this repository.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Authentication | JWT, OAuth2, OpenID Connect, Keycloak, token validation. |
| Authorization | RBAC, method security, least privilege, workflow-level authorization. |
| Secrets | Secret management, rotation, avoiding sensitive data in logs and commits. |
| Data protection | Encryption in transit and at rest, privacy boundaries, audit logging. |
| API security | Input validation, rate limiting, object-level authorization, error disclosure. |
| OWASP risks | Injection, broken access control, auth failures, insecure design, vulnerable components. |
| Threat modelling | Assets, trust boundaries, abuse cases, mitigations, residual risk. |
| Secure delivery | SAST, dependency scanning, container scanning, SBOM, supply-chain basics. |
| Security testing | Authorization tests, negative tests, dependency and image checks. |

## Experience-Based Questions

- How would you validate authorization for a sensitive workflow transition?
- How would you design audit logging for candidate, payment, or reporting workflows?
- What would you do if a root-level role could expose the wrong data view?
- How would you threat model an API that accepts identity or payment-linked data?
- What belongs in CI security checks for a Java/Spring Boot service?
- How would you handle secrets in local development, CI, and production?

## Practice Tasks

- Create a threat model for one project case study.
- Add a security test plan for role-based access and object-level authorization.
- Document a secure CI/CD checklist covering SAST, dependency scanning, container scanning, secrets, and SBOM fundamentals.

## Evidence Notes

Keycloak, JWT token introspection, role-based authorization, data privacy and integrity are recorded in [skills inventory](../../master/skills-inventory.md). Supply-chain security and scanning topics should remain evidence gaps until implemented or documented in a lab.
