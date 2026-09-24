# Database Standard

Load this standard for schema, migration, persisted-data, index, constraint, transaction, or material query changes.

## Data integrity

- State invariants explicitly and enforce them at the strongest practical layer.
- Use constraints and transactions deliberately; define behavior on partial failure and retry.
- Consider nullability, defaults, uniqueness, referential integrity, collation/time zones, and concurrent writers.
- Preserve confidentiality in queries, logs, dumps, fixtures, and error messages.

## Safe evolution

- Prefer additive, backward-compatible changes and expand/migrate/contract when mixed application versions may run.
- Treat backfills as operational work: bound batches, locks, runtime, retries, observability, and restart safety.
- Do not rewrite applied migration history unless project policy explicitly permits it.
- Destructive or irreversible work requires explicit approval, backup/recovery readiness, and exact targeting.

## Performance

- Evaluate selectivity, indexes, query plans, cardinality, lock duration, and write amplification where material.
- Test with representative shape/volume when practical; tiny fixtures do not prove production performance.
- Avoid indexes without a supported access pattern and account for their write/storage cost.

## Evidence

Report migration application, integrity checks, rollback/recovery method, compatibility window, and performance evidence as applicable. Never execute a production mutation merely to validate a migration.
