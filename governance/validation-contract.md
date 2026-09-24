# Validation Contract

Validation is an evidence record, not a confidence statement.

## Per-check statuses

- `PASS`: the check or review was performed successfully; record command/method and scope.
- `FAIL`: it was performed and produced a failure; record the relevant failure.
- `NOT_APPLICABLE`: it does not apply to this task/project; give a reason when non-obvious.
- `BLOCKED`: it should be performed but cannot; record the blocker and consequence.

Never use `PASS` for “not run,” “looks correct,” “should pass,” or a different narrower check.

## Default pipeline

```text
FORMAT
  -> LINT
  -> STATIC / TYPE ANALYSIS
  -> UNIT TESTS
  -> INTEGRATION TESTS
  -> BUILD
  -> SECURITY REVIEW
  -> FINAL DIFF REVIEW
```

Projects define actual commands and mandatory gates. Adapters help interpret them but do not invent them. Run only applicable checks, plus every project-required gate.

## Proportional validation

- LOW: the smallest checks that directly exercise the changed surface, plus required gates and diff review.
- MEDIUM: checks for affected code and boundaries, relevant regressions, build where applicable, and diff review.
- HIGH: approval first, then full relevant validation, security/data/compatibility evidence, recovery checks, and diff review.

## Evidence

For commands, record command, result, and useful scope/count. For manual reviews, record what was inspected and the conclusion. If the environment prevents a check, use `BLOCKED`; do not substitute a guess.

Any `FAIL` or `BLOCKED` required check prevents task status `COMPLETE`.
