# System Design Cases

Use the shared [system design framework](../shared/system-design.md). Mark unknown capacity, SLA, deployment or incident details as `Evidence needed`.

## Case 1: Election Nomination and Reporting Platform

- Clarify users, roles, workflow states, reporting needs and disclosure limits.
- Design APIs for multi-step nomination, payment completion, final submission and report generation.
- Model candidate, nomination, payment, schedule, report and audit entities.
- Discuss Keycloak authorization, workflow validation, audit logging and privacy.
- Address RabbitMQ or asynchronous processing only where evidence supports it.
- Define RTO, RPO, SLO and failure recovery as assumptions unless verified.

## Case 2: Open-Care Healthcare Resource Search

- Clarify user search needs, provider/resource data, admin workflows and privacy concerns.
- Design REST APIs, search/filtering, pagination, authorization and OpenAPI documentation.
- Model provider, hospital, ambulance, blood donation, file storage and user roles.
- Discuss PostgreSQL, Redis, Keycloak, MinIO, Docker and deployment trade-offs.
- Avoid usage metrics because none are recorded.

## Case 3: Exam Management Workflow

- Clarify administrator, invigilator, examinee, registration, payment and reporting use cases.
- Discuss Redis caching and backend improvements behind the recorded 30% response-time reduction.
- Address PostgreSQL schema design, transaction boundaries and reporting.
- Include Jenkins CI/CD and Locust load testing only within recorded scope.

## Case 4: Procurement Workflow Platform

- Clarify enterprise workflow, uploads, data privacy and integrity constraints.
- Use this mainly for legacy enterprise workflow and data modeling discussion.
- Do not use the reported 80% engagement metric until measurement context is verified.
