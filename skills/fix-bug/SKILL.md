---
name: fix-bug
description: Diagnose and minimally correct reproducible incorrect behavior, preferably with a regression test that fails before and passes after the fix. Use when a concrete bug is in scope; use investigate when the cause cannot yet be bounded.
---

# Fix Bug

Fix the root cause without expanding the task into a refactor.

## Load context progressively

Read project instructions, [`risk-classification`](../../governance/risk-classification.md), relevant stack adapters, [`testing`](../../standards/testing.md), and only the standards implicated by the failure. Read [`human-approval`](../../governance/human-approval.md) before any gated mutation.

## Workflow

1. Translate the report into expected behavior, actual behavior, and a reproducible case.
2. Reproduce the failure when safe. If reproduction is blocked, state the missing evidence and avoid guessing.
3. Trace the failure to a root cause and record the evidence that separates it from symptoms.
4. Add or update the narrowest useful regression test when practical; confirm it fails for the intended reason.
5. Implement the smallest fix that addresses the root cause.
6. Confirm the regression test passes, then run relevant neighboring tests and project-required checks.
7. Review the full diff for behavior changes, compatibility, security, test manipulation, and unrelated edits.
8. Apply [`definition-of-done`](../../standards/definition-of-done.md) and report using the standard template.

## Required outcomes

- Root cause is explained with evidence.
- The original symptom is no longer reproducible.
- A regression test exists, or the report explains why it is impractical.
- Relevant regressions and required validation pass.
- The fix does not weaken a test, rule, or error path merely to obtain `PASS`.

If evidence reveals a materially different or HIGH-risk fix, stop at the appropriate approval or scope boundary.
