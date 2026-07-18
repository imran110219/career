# System Design Interview Notes

## Design Framework

| Step | Questions |
| --- | --- |
| Clarify | Users, core use cases, scale, latency, availability, consistency. |
| Model | Entities, relationships, APIs, events, state transitions. |
| Architecture | Services, storage, queues, caches, search, external integrations. |
| Reliability | Failure modes, retries, idempotency, backups, disaster recovery. |
| Operations | Metrics, logs, tracing, alerts, runbooks, rollout strategy. |
| Tradeoffs | Consistency versus availability, simplicity versus scale, cost versus performance. |

## Practice Systems

- URL shortener.
- Job application tracker.
- Notification platform.
- File upload and document processing service.
- Audit log service.
- Multi-tenant SaaS backend.

## Checklist

- [ ] Start with requirements before components.
- [ ] State assumptions explicitly.
- [ ] Define APIs and data model before scaling details.
- [ ] Discuss failure modes and operational visibility.
- [ ] Close with bottlenecks and future improvements.
