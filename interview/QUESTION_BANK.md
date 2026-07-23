# Curated Interview Question Bank

Use these prompts for practice. Favor experience-backed answers; if evidence is missing, say what evidence would be needed.

## Java and Spring Boot

- Describe a transaction boundary that caused unexpected behavior.
- How would you diagnose a Spring service that is slow only under concurrent load?
- How do you prevent N+1 queries in a JPA-backed API?
- When would you choose JDBC or native SQL instead of JPA?
- How would you test authorization rules in a Keycloak-backed service?
- What Java collection choice has caused a trade-off in performance, ordering, or correctness?
- How would you review AI-generated Spring Boot code before merging it?

## PostgreSQL and Data

- How did you diagnose a slow PostgreSQL query?
- How would you choose between composite, partial, and covering indexes?
- How would you size a HikariCP connection pool?
- How would you handle a deadlock in a workflow-heavy system?
- When would you choose keyset pagination over offset pagination?
- How would you design backup and recovery expectations for a critical workflow?

## API Design

- How would you design idempotent final submission for a multi-step workflow?
- How should API validation and business-rule errors be returned to clients?
- How do you version APIs without breaking existing frontend or integration clients?
- How would you add rate limiting and audit logging without exposing sensitive data?
- What evidence would make API lifecycle management résumé-safe?

## Distributed Systems and System Design

- When would you choose a modular monolith instead of microservices?
- How do you prevent retries from causing duplicate processing?
- How would you design dead-letter queue handling and investigation?
- How would you define RTO and RPO for an election platform?
- How would you migrate a monolith toward independently deployable services?
- How would you design observability for a distributed workflow across payment, identity and reporting services?

## Testing and Quality

- What tests would you require before changing a critical workflow transition?
- When should integration tests use real containers instead of mocks?
- How would you prevent flaky tests from blocking releases?
- How would you design CI stages for a Spring Boot backend?
- How would you measure whether testing improved delivery quality?

## Security, Cloud and DevOps

- How would you threat model an API that handles identity or payment-linked data?
- What belongs in secure CI/CD for Java services?
- How would you prevent secrets from leaking through logs, CI or container images?
- What Kubernetes responsibilities are defensible based on current evidence?
- What AWS services would you choose for a Spring Boot API backed by PostgreSQL and Redis?
- Which DevSecOps topics are useful for these roles but not core positioning?

## Lead Backend

- Describe a difficult delivery you led.
- How did you break ambiguous requirements into deliverable backend tasks?
- Describe a technical disagreement you resolved.
- How did you improve code-review quality?
- How did you balance delivery speed and technical quality?
- Describe an incident where you coordinated people and technical diagnosis.
- How did you mentor a developer while still keeping delivery moving?

## Software Architect

- How would you define service boundaries and data ownership for an election platform?
- What would you document in a C4 context and container diagram?
- When would CQRS or event sourcing be worth the complexity?
- How would you govern architecture decisions without slowing delivery?
- How would you define availability, SLO, SLA, RTO and RPO for a critical system?
- How would you plan a migration from tightly coupled services to clearer bounded contexts?

## Candidate Questions

### Hiring Manager

- What outcomes would define success in the first 90 days?
- Which system risks or delivery bottlenecks matter most this year?
- How are architecture decisions documented and revisited?

### Engineering Peers

- How do services communicate and how are API changes coordinated?
- What do code review, incident follow-up and on-call practices look like?
- Which reliability or performance signals guide priorities?

### Recruiter

- What are the work-location, relocation and visa-sponsorship expectations?
- What is the interview process and expected timeline?
- Which role requirements are essential versus preferred?
- What is the approved compensation range for this level?
