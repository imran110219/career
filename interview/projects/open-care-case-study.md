# Open-Care Case Study

## Business Context

Open-Care is a personal open-source healthcare-information product for searchable provider, hospital, ambulance, blood-donation and medical-resource capabilities.

## Users and Scale

No public usage metrics are recorded. Use `Evidence needed` for traffic, users, latency or adoption.

## Personal Responsibilities

- Lead contributor; confirm whether founder wording is appropriate before use.
- Backend/API design.
- Security and authorization.
- Search-related product capabilities.
- Documentation and deployment work.

## Team Context

Personal/open-source project. Contributor model, collaborators and timeline: Evidence needed.

## Architecture

- Spring Boot backend.
- PostgreSQL database.
- Redis.
- Keycloak.
- MinIO.
- Liquibase.
- Swagger/OpenAPI.
- Docker.
- Next.js frontend.

## Module Boundaries

Evidence needed. Candidate modules: resource search, provider/hospital data, ambulance data, blood-donation data, admin/content management, authentication/authorization and file storage.

## Data Model

Evidence needed. Prepare an interview-safe model for providers, hospitals, resources, files, users/roles and search filters.

## Security

- Keycloak authorization is recorded.
- API authorization boundaries, role model, token handling and object-level authorization: Evidence needed.
- Avoid committing secrets, private user data or production configuration.

## Performance

Evidence needed for indexes, caching, search latency and usage patterns.

## Reliability

Evidence needed for health checks, backups, monitoring, alerts and incident history.

## Deployment

Dockerized deployment work is recorded. Hosting topology, CI/CD, rollout and rollback details: Evidence needed.

## Observability

Evidence needed for logging, metrics, tracing, dashboards and alerting.

## Important Technical Decisions

- Spring Boot and PostgreSQL for backend/data.
- Keycloak for authorization.
- MinIO for file storage.
- Liquibase for schema migration.
- Swagger/OpenAPI for API documentation.

Alternatives and trade-offs: Evidence needed.

## Trade-Offs

- Full-stack personal project scope versus production hardening.
- Keycloak capability versus operational complexity.
- PostgreSQL/Redis search and caching versus dedicated search service.
- MinIO object storage versus local or cloud storage.

## Constraints

- No recorded public usage metrics.
- Personal project claims must be separated from professional employment evidence.
- Security/privacy must be public-safe.

## Incidents or Difficult Problems

Evidence needed.

## Measurable Outcomes

No usage, performance or adoption metrics are recorded.

## What Would Be Redesigned Now

- Add automated tests and Testcontainers evidence.
- Add a public architecture diagram and ADRs.
- Add observability notes.
- Document deployment and rollback process.
- Add a security/threat model.

## Senior Backend Interview Angle

Use as a hands-on Spring Boot, PostgreSQL, Keycloak, Docker and OpenAPI example.

## Lead Backend Interview Angle

Use cautiously for product ownership, scope prioritization and quality decisions. Do not imply team leadership unless collaborators are verified.

## Software Architect Interview Angle

Use for architecture documentation practice: C4, ADRs, NFRs, threat model, deployment model and migration options.

## Unknown or Unverified Details

- Dates and current active maintenance level.
- Founder wording.
- Usage, traffic, uptime and performance metrics.
- Exact deployment topology.
- Test coverage and CI/CD evidence.
- Observability setup.
