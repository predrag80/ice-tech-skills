---
name: code-review
description: Review existing changes for actionable correctness, regression, security, data, architecture, and test issues, reporting findings by severity with evidence. Use for review requests; do not modify code unless the user separately authorizes fixes.
---

# Code Review

Find concrete defects and risks. Do not turn style preference into a finding.

## Load context progressively

Read the request, project instructions, changed diff, and only the standards and stack adapters needed to assess those changes. Load surrounding code and tests only where they establish behavior or impact.

## Workflow

1. Establish review scope, intended behavior, comparison base, and any unavailable context.
2. Inspect the complete diff, then trace affected call paths, contracts, data flows, error paths, and tests.
3. Look first for correctness, regressions, security, data integrity, concurrency, compatibility, and missing tests; consider maintainability when it creates concrete risk.
4. Validate suspected issues with the smallest reliable check available. Distinguish verified defects from questions or residual risk.
5. Report findings in descending severity. For each, give location, trigger, impact, and a concise remediation direction.
6. If no actionable finding exists, say so and list meaningful validation gaps or residual risks.
7. Complete the final report. Review completion does not mean the reviewed code itself passed every project gate.

## Severity

- `P0`: catastrophic or actively exploitable; stop release/work.
- `P1`: high-impact correctness, security, or data issue likely in normal use.
- `P2`: real defect with limited conditions or impact.
- `P3`: low-impact issue worth fixing; avoid pure preference.

Do not edit files, commit, or widen scope unless explicitly requested. A review can be `COMPLETE` with findings because the deliverable is the review, not remediation.
