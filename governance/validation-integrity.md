# Validation Integrity

Validation must measure the requested system, not a weakened substitute.

## Prohibited shortcuts

Unless independently justified by changed requirements or a verified defect in the check, do not:

- remove, skip, quarantine, or disable a failing test;
- weaken assertions, expected values, coverage thresholds, or representative fixtures;
- disable lint, static-analysis, security, or build rules merely to silence failure;
- add type suppressions or unsafe casts solely to obtain a pass;
- catch, ignore, or hide runtime errors;
- mock away the behavior or boundary under validation;
- edit expected output to match a regression;
- report a narrower check as proof of a broader gate.

## Legitimate check changes

A test or rule may change when requirements changed, the check is incorrect/outdated, or the tool configuration does not represent the intended system. The report must state the independent reason, evidence, and lost/gained coverage.

## Audit

Review validation-related diffs separately. A green result obtained by reducing meaningful coverage is a task failure, not `PASS`.
