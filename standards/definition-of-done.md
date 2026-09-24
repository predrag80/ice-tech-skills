# Definition of Done

This is the final quality gate. Apply it together with the selected skill's outcome.

## Implementation tasks

A task is `COMPLETE` only when all are true:

- The requested observable behavior and acceptance criteria are satisfied.
- Only necessary files and supporting changes are included.
- Appropriate tests exist, or omission has a concrete, visible justification.
- Every project-required and applicable validation is `PASS` or justified `NOT_APPLICABLE`.
- No required check is `FAIL` or `BLOCKED`.
- Relevant security, data, compatibility, accessibility, and operational risks were reviewed.
- Required approvals were obtained before gated actions.
- The complete diff was reviewed and contains no temporary, secret, or unrelated material.
- Documentation/configuration is updated where users or operators need it.

## Non-implementation tasks

- `investigate` is complete when the question is answered with evidence, confidence, limitations, and a next step; no code change is required.
- `code-review` is complete when the scoped review is performed and findings or a clear no-findings statement plus residual risks are delivered; reviewed code may still contain defects.

## Terminal status selection

- Use `APPROVAL_REQUIRED` before a pending gated action.
- Use `BLOCKED` when an external condition or unavailable prerequisite prevents required work/evidence.
- Use `FAILED` when attempted execution remains unsuccessful and no safe in-scope correction remains.
- Never soften these statuses with language implying completion.

Finish with the fields in [`templates/final-report.md`](../templates/final-report.md).
