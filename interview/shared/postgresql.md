# PostgreSQL Preparation

Use this for database depth across all three target roles.

## Focus Areas

| Area | Practical interview focus |
| --- | --- |
| Index design | B-tree, composite indexes, partial indexes, covering indexes, write overhead. |
| Query optimization | `EXPLAIN ANALYZE`, cardinality, joins, sequential scans, statistics. |
| Advanced SQL | Window functions, aggregation, CTE trade-offs, keyset pagination. |
| Transactions | Isolation levels, row locks, deadlocks, retries, consistency guarantees. |
| Operations | HikariCP, connection pooling, backups, recovery, replication fundamentals. |
| Scaling | Read/write splitting, partitioning, archiving, migration strategy. |
| Data integrity | Constraints, schema migration, auditability, sensitive-data handling. |

## Experience-Based Questions

- How did you diagnose a slow PostgreSQL query?
- How would you choose indexes for a multi-column search and sort query?
- How would you size a database connection pool for a Spring Boot service?
- Describe a deadlock scenario and how you would prevent or recover from it.
- When would you use keyset pagination instead of offset pagination?
- How would you design a migration that avoids downtime?
- What evidence would make query optimization résumé-safe?

## Practice Tasks

- Create a query-tuning note with baseline query, `EXPLAIN ANALYZE`, index decision, and measured result.
- Write one schema migration plan with rollback and data-consistency checks.
- Prepare an isolation-level example using order or workflow status changes.
- Document HikariCP sizing assumptions for a backend API.

## Evidence Notes

PostgreSQL, data modeling, Redis caching, query optimization and Liquibase are recorded in [skills inventory](../../master/skills-inventory.md). Specific before-and-after query evidence still needs capture in [EVIDENCE_LOG.md](../EVIDENCE_LOG.md).
