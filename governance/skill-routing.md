# Skill Routing

Select exactly one primary skill from the user's requested outcome, not merely from files touched.

## Decision table

| Requested outcome | Primary skill |
|---|---|
| Add or enhance behavior | `implement-feature` |
| Correct known/reproducible incorrect behavior | `fix-bug` |
| Improve structure without intended behavior change | `refactor` |
| Determine an unknown cause or explain behavior | `investigate` |
| Deliver a database-centered migration/schema/data/query change | `database-change` |
| Assess existing changes and report findings | `code-review` |

## Mixed tasks

Use supporting guidance without creating multiple primary completion contracts.

- Feature plus migration: `implement-feature` primary; apply `database-change` as supporting guidance.
- Standalone schema/index/backfill: `database-change` primary.
- Unknown incident plus requested diagnosis only: `investigate` primary.
- Investigation that proves a fix is needed: stop at the investigation deliverable unless implementation was also requested; then explicitly transition to `fix-bug`, re-evaluate risk, scope, and approval.
- Requested refactor that reveals a bug: preserve the bug as a finding unless it blocks safe completion or the user expands scope.
- Review plus requested remediation: use `code-review` until findings are established, then select the primary skill matching the authorized remediation.

## Routing rules

1. Prefer the narrowest skill that describes the deliverable.
2. Do not infer permission to implement from a request to investigate or review.
3. If the request contains multiple independent outcomes, split or report the ambiguity rather than hiding it under one skill.
4. Record the selected skill and any supporting guidance in the final report.
5. Re-route only when evidence materially changes the task; repeat risk and approval evaluation before new mutations.
