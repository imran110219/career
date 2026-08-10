# PostgreSQL Preparation

Use this for shared database depth across the backend, lead-backend, architecture, platform, and engineering-management tracks. Keep role-specific delivery stories in the role folders.

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

## Query-Tuning Answer Framework

For a slow-query question, answer in this order:

1. Define the symptom and scope: endpoint, affected workflow, latency/error rate, traffic change, and whether it is one query or system-wide contention.
2. Collect evidence before changing anything: normalized query, parameters, `EXPLAIN (ANALYZE, BUFFERS)`, database load, active sessions, and recent schema/deployment changes.
3. Compare estimated and actual row counts. Large gaps usually point to stale or insufficient statistics, skewed data, or a query predicate the planner cannot estimate well.
4. Locate the expensive node: sequential/index scan, sort, hash, nested-loop join, aggregate, or rows removed by a filter. Check buffer reads as well as elapsed time.
5. Make the smallest safe change: query shape, index, statistics refresh, pagination, batching, or caching. Consider write cost, storage, and operational risk.
6. Verify with the same representative workload; record before/after latency, plan, and resource impact. Monitor after release and retain a rollback path.

Do not say an index is always the answer. A sequential scan can be correct for a small table or a query that returns a large share of it.

## Plan Reading and Index Design

- Use `EXPLAIN` to see the planner's proposed plan; use `EXPLAIN ANALYZE` to execute it and compare estimates with actual rows and timings. Add `BUFFERS` when investigating I/O.
- Look for an unexpectedly high actual row count, expensive sorts, repeated nested-loop work, a large number of filtered rows, or disk reads that do not match the expected workload.
- B-tree is the normal choice for equality, range predicates, and ordered access. Composite B-tree indexes are most useful when their leading columns match common filters and ordering; column order follows real query patterns, not a universal rule.
- A partial index is useful when a stable predicate selects a small, frequently queried subset. The query must use a compatible predicate for PostgreSQL to use it.
- `INCLUDE` can make an index cover returned columns and enable an index-only scan when visibility-map conditions permit it; it is not a guarantee of zero heap access.
- Every index costs disk, cache, and write work. Reassess unused or overlapping indexes with production-safe evidence rather than adding indexes speculatively.
- For expression, JSONB, full-text, geometric, or similarity searches, explain that the index type must match the operator and query shape; validate it with an actual plan.

## Transactions, Locks, and Blocking

PostgreSQL's default `READ COMMITTED` isolation gives each statement a fresh view of committed data. Use a stronger isolation level only for a specific correctness requirement and design for the resulting retries or contention.

When a query blocks for minutes:

1. Establish impact and avoid making the situation worse: identify the workflow and whether a safe traffic reduction, rollback, or pause is appropriate.
2. Inspect active sessions, query age, transaction age, wait events, and blocking relationships (for example through `pg_stat_activity`, `pg_locks`, and the blocking-process functions).
3. Find the blocker and why its transaction is open: long-running work, an idle transaction, a migration, an application retry, or inconsistent lock ordering.
4. Mitigate carefully. Cancel a query or terminate a session only after understanding transaction and customer-impact consequences.
5. Prevent recurrence with short transactions, consistent resource/row ordering, appropriate indexes, bounded lock/statement timeouts, monitoring, and an application retry policy where safe.

Deadlocks are expected in concurrent systems, not a sign that PostgreSQL is broken. PostgreSQL aborts one participant; the application should handle SQLSTATE `40P01` with a bounded retry only when the operation is idempotent or protected against duplicate effects. Serializable transactions can also fail with SQLSTATE `40001`; retrying those safely is part of the design.

Useful lock options include `FOR UPDATE` when a workflow needs to protect selected rows, `NOWAIT` when waiting is worse than failing quickly, and `SKIP LOCKED` for work-queue patterns where skipped work is acceptable. Explain the business semantics before choosing one.

## Pagination, SQL Shape, and ORM Boundaries

- Prefer keyset pagination for large, frequently traversed result sets: use a stable, indexed order and a cursor composed of the sort key plus a unique tiebreaker. It avoids the growing work and shifting-page behavior of large offsets.
- Offset pagination remains reasonable for shallow pages, small datasets, or interfaces that require direct page-number jumps.
- Use window functions for ranking, running totals, and partitioned comparisons; verify their sort and memory costs on representative data.
- CTE behavior and planner choices are version- and query-dependent. Treat a CTE as a readability or semantic tool first, then inspect the plan before assuming it improves or harms performance.
- In a JPA-backed service, first check emitted SQL, N+1 fetching, fetch joins, pagination behavior, and transaction scope. Use JDBC or native SQL when it makes a data-heavy query clearer or more controllable, while retaining parameterization and test coverage.

## Operations and Connection Pools

- PostgreSQL MVCC needs routine vacuuming. Long-running transactions can prevent cleanup, contribute to table/index bloat, and make operational incidents worse; monitor transaction age and autovacuum health.
- Use query and session observability proportionately: application latency/error metrics, database connection utilization, slow-query capture, `pg_stat_activity`, and—where enabled—`pg_stat_statements`. Avoid logging sensitive parameters.
- Size HikariCP from measured concurrency, query latency, database CPU/I/O capacity, and the total of all application instances. A larger pool can increase database contention; leave capacity for migrations, administration, and failover.
- Set explicit acquisition, connection-lifetime, and validation expectations. Investigate pool exhaustion through checkout wait time, active/idle connections, slow queries, and leaked or overlong transactions—not by only increasing `maximumPoolSize`.
- Define recovery in business terms: RPO (acceptable data loss) and RTO (acceptable recovery time). Backups are only credible when restores are tested; point-in-time recovery requires suitable WAL retention and operational procedures.

## Replication, Scaling, and Migrations

- Read replicas can protect primary capacity for read-oriented workloads, but asynchronous replication may return stale data. Keep writes and read-after-write or correctness-sensitive paths on the primary unless freshness behavior is deliberately designed.
- A replica is not a backup. Discuss replication lag, failover ownership, connection routing, monitoring, and the operational runbook before presenting replicas as a scaling solution.
- Consider partitioning only when it solves a demonstrated access, retention, or maintenance problem. It adds query, migration, and operational complexity.
- For an online schema change, use expand/contract: add compatible structures, deploy code that supports both shapes, backfill in bounded batches, validate, switch reads/writes, and remove old structures only after the transition.
- Review lock levels and execution behavior for every migration. For example, `CREATE INDEX CONCURRENTLY` reduces blocking but has constraints, including that it cannot run inside a transaction block. Test migrations at realistic scale and define rollback or forward-recovery steps.

## Experience-Based Questions

- How did you diagnose a slow PostgreSQL query?
- How would you choose indexes for a multi-column search and sort query?
- How would you size a database connection pool for a Spring Boot service?
- Describe a deadlock scenario and how you would prevent or recover from it.
- When would you use keyset pagination instead of offset pagination?
- How would you design a migration that avoids downtime?
- What evidence would make query optimization résumé-safe?

## Practice Tasks

- Create a query-tuning note with a baseline query, `EXPLAIN (ANALYZE, BUFFERS)`, row-estimate comparison, index or query decision, and measured result.
- Rehearse a blocking investigation using `pg_stat_activity` and `pg_locks`; state the safe mitigation and prevention plan.
- Write one expand/contract schema migration plan with lock review, rollback or forward-recovery, and data-consistency checks.
- Prepare an isolation-level example using order or workflow status changes, including retry/idempotency behavior.
- Document HikariCP sizing assumptions for a backend API, including total service replicas and database headroom.
- Create a replica-routing decision note covering allowed stale reads, read-after-write behavior, lag monitoring, and failover.

## Production-Ownership Answer Structure

For database incidents and design questions, state the workflow impact and correctness risk first. Then describe the evidence you would collect, the immediate safe mitigation, the root-cause decision and trade-offs, and the prevention work: index/query change, timeout, migration process, alert, test, runbook, or capacity adjustment.

Use a proposed design or lab example when a production detail is not supported by evidence. Never infer access to database topology, query logs, table names, or performance metrics that are not safe to disclose.

## Evidence Notes

PostgreSQL, data modeling, Redis caching, query optimization and Liquibase are recorded in [skills inventory](../../master/skills-inventory.md). The election-management read-replica routing story supports a qualitative discussion of protecting primary capacity and accepting replica-consistency trade-offs; do not quote latency, load, topology, or configuration details without evidence. Specific before-and-after query evidence still needs capture in [EVIDENCE_LOG.md](../EVIDENCE_LOG.md).
