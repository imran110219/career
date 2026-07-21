# Project Deep Dives

Complete these before interviews. Mark unknown fields `NEEDS REVIEW`; never infer confidential details.

## Election Management System

| Topic | Verified starting point / prompt |
| --- | --- |
| Business problem | Election-management workflows, including nomination and reporting. |
| Users and scale | Reported: internal system supporting 50,000 users and ~100,000 daily requests during election periods; confirm disclosure context. |
| Team / exact role | Backend delivery activities within a 30-person development team; specify personal ownership. |
| Architecture and APIs | Nearly 25-service platform; service interactions and REST API contracts. |
| Data, security, performance | Sensitive workflow data; Keycloak authorization and validation. Metrics NEEDS REVIEW. |
| Deployment / incidents | Self-managed Kubernetes deployment support; prepare a verified incident. |
| Tradeoffs / redesign | [NEEDS REVIEW] |
| Confidentiality limits | Do not disclose client system names, internal URLs, credentials, or unpublished architecture. |

## Exam Management System

| Topic | Verified starting point / prompt |
| --- | --- |
| Business problem | Exam administration, registration, payment, reporting, and coordination. |
| Users / scale | 2,500+ administrators, 1,000 invigilators, 1,000 examinees; nearly 30,000 students in registration/payment workflows. |
| Team / exact role | Led development; requirements analysis and database schema design. |
| Architecture / APIs / database | Java, Spring Boot, PostgreSQL, Redis, Flutter, Crystal Reports. |
| Security / performance | Reported 30% response-time reduction through Redis and backend improvements. |
| Deployment / incidents / tradeoffs | [NEEDS REVIEW] |
| Redesign today / confidentiality | [NEEDS REVIEW]; do not disclose internal payment or customer details. |

## Open Care

| Topic | Verified starting point / prompt |
| --- | --- |
| Business problem | Healthcare-information access and searchable resources. |
| Users / scale | No public usage metric recorded. |
| Team / exact role | Lead contributor; confirm founder/ownership wording. |
| Architecture / APIs / database | Spring Boot, PostgreSQL, Redis, Keycloak, MinIO, Liquibase, Swagger/OpenAPI, Docker, Next.js. |
| Security / deployment | Keycloak authorization, Dockerized deployment; prepare exact configuration and tradeoffs. |
| Incidents / redesign / confidentiality | [NEEDS REVIEW]; public links may be used, but avoid secrets and private user data. |
