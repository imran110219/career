# API Design Preparation

Use this for REST and API lifecycle preparation across all tracks.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| REST resources | Resource naming, nouns, relationships, subresources, consistency. |
| HTTP semantics | Methods, status codes, headers, caching, content negotiation. |
| Query behavior | Pagination, filtering, sorting, search, validation. |
| Errors | Stable error shape, field errors, trace IDs, client-actionable messages. |
| Idempotency | Idempotency keys, retries, duplicate prevention, state transitions. |
| Versioning | Backward compatibility, deprecation, consumer migration. |
| Security | Authentication, authorization, rate limiting, data exposure control. |
| OpenAPI | Documentation, examples, generated clients, review workflow. |
| Lifecycle | API ownership, change review, contract testing, observability. |

## Experience-Based Questions

- Describe an API contract you designed or maintained under changing requirements.
- How would you design idempotent final submission for a multi-step nomination form?
- How should APIs return validation errors for frontend and integration clients?
- How would you version an API without breaking existing consumers?
- How do you prevent pagination from becoming unstable under concurrent writes?
- What should be logged for sensitive API workflows, and what should not be logged?

## Practice Tasks

- Draft OpenAPI for one case-study workflow and include validation and error examples.
- Create an API review checklist for authentication, authorization, idempotency, compatibility, and observability.
- Document one API evolution scenario with migration and rollback.

## Evidence Notes

REST API contracts are recorded for the Election Management System and Open-Care. Keep personal ownership precise and avoid implying sole ownership of the full election platform.
