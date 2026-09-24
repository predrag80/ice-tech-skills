# Human Approval

Approval preserves human control over material risk. It is required before any HIGH-risk mutation and any project-configured gate.

## Mandatory v1 gates

- destructive or irreversible database/data operations;
- significant authentication or authorization architecture changes;
- adding or removing production dependencies;
- significant development dependencies;
- breaking public API or persisted-data contract changes;
- significant production infrastructure or configuration changes;
- secret/credential creation, rotation, disclosure, or movement;
- major architectural changes.

Read-only analysis may continue only when it does not itself access restricted sensitive data or change state.

## Approval request contract

Before the gated action, set task status to `APPROVAL_REQUIRED` and state:

1. exact proposed operation and target;
2. why it is needed;
3. user, system, security, and data impact;
4. risk level and reversibility;
5. validation, rollout, and recovery plan;
6. lower-risk alternatives and tradeoffs, when meaningful;
7. the precise decision needed from the human.

Approval must be specific enough to cover the actual action. Approval for a feature is not automatically approval for a later-discovered destructive migration, new dependency, production mutation, or secret operation.

## After approval

Verify the target and assumptions again, perform only the approved action, and record the approval scope in the final report. If the action changes materially, stop and request fresh approval.

## Rejection or no response

Do not perform the gated action. Offer a safe alternative when one exists; otherwise finish `BLOCKED` or retain `APPROVAL_REQUIRED` according to the current state. Never simulate approval.
