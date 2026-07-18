# PostgreSQL Interview Notes

## Core Topics

| Topic | Review Focus |
| --- | --- |
| Indexes | B-tree, composite indexes, partial indexes, covering indexes. |
| Query Planning | `EXPLAIN`, `ANALYZE`, cardinality, sequential scans, joins. |
| Transactions | Isolation levels, locks, deadlocks, retries, consistency. |
| Schema Design | Normalization, constraints, foreign keys, migrations. |
| Performance | Vacuum, statistics, connection pooling, pagination, batching. |

## Practice Prompts

- Diagnose a slow query using `EXPLAIN ANALYZE`.
- Choose indexes for a multi-column search and sort query.
- Explain transaction isolation levels with examples.
- Design a migration that avoids downtime.
- Compare offset pagination with keyset pagination.

## Checklist

- [ ] Review common index patterns.
- [ ] Prepare examples of query tuning.
- [ ] Review lock and deadlock troubleshooting.
- [ ] Prepare a database migration story.
