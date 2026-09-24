---
name: database-change
description: Design and implement schema, migration, constraint, index, persisted-data, or material query changes with integrity, rollout, recovery, and performance checks. Use as primary for database-centered work or as supporting guidance inside a broader feature.
---

# Database Change

Protect data first; optimize for a safe, observable rollout rather than migration brevity.

## Load context progressively

Read project instructions, [`database`](../../standards/database.md), [`risk-classification`](../../governance/risk-classification.md), [`human-approval`](../../governance/human-approval.md), and only the database/ORM stack adapters evidenced by the project.

## Workflow

1. Describe the current and desired data model, invariants, data volume assumptions, and application compatibility window.
2. Classify additive, backfill, constraint, destructive, index, and query effects separately; use the highest credible risk.
3. Design forward migration, rollout sequence, verification, and rollback or recovery. Account for mixed-version application instances where relevant.
4. Stop for approval before destructive, irreversible, production, or otherwise HIGH-risk operations.
5. Implement migration and application compatibility changes without editing already-applied migration history unless the project explicitly allows it.
6. Validate on a safe environment: migration application, representative data, constraints, transactions, locks, query plans/performance, and application tests as applicable.
7. Review the diff and operational plan for partial failure, retry safety, backups, observability, and data exposure.
8. Apply [`definition-of-done`](../../standards/definition-of-done.md) and report exact evidence.

## Required outcomes

- Invariants and compatibility are explicit.
- Migration order and recovery path are documented.
- Destructive actions have explicit approval.
- Relevant integrity and performance evidence exists.
- No production mutation is performed merely because implementation was requested.
