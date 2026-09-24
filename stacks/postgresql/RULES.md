# PostgreSQL Adapter

Load for PostgreSQL schema, SQL, migration, index, constraint, transaction, policy, or material query work. Also load the database standard.

## Apply

- Use constraints to encode durable invariants and explicit transactions for atomic multi-step changes.
- Account for PostgreSQL locking, MVCC, transaction isolation, deadlocks, long transactions, vacuum/bloat, and replication where relevant.
- Evaluate migration statements for table rewrites, lock duration, mixed-version application compatibility, and safe retry.
- Create indexes from demonstrated access patterns; consider column order, partial/expression indexes, uniqueness, concurrent creation, and write/storage cost.
- Inspect query plans with representative statistics/data where performance matters; distinguish estimated from actual execution evidence.
- Parameterize values and quote identifiers correctly. Treat dynamic SQL, extensions, functions, triggers, roles, and row-level security as security boundaries.
- Plan backfills in bounded, observable, restart-safe batches when data volume may be material.

## Validate

Use project migration and test tooling. Consider forward migration, transaction behavior, constraints, representative queries/plans, application compatibility, and recovery. Destructive or production operations require approval; validation should occur in a safe environment.
