---
name: implement-feature
description: Implement new software behavior with scoped design, appropriate tests, proportional validation, and a reviewed final diff. Use for features or enhancements; use fix-bug for incorrect existing behavior and investigate when the cause or requirement is still unknown.
---

# Implement Feature

Deliver the smallest complete behavior that satisfies the request.

## Load context progressively

1. Read project instructions and validation configuration.
2. Read [`skill-routing`](../../governance/skill-routing.md), then classify risk with [`risk-classification`](../../governance/risk-classification.md).
3. Load only stack adapters evidenced by the files in scope.
4. Load testing plus any security, architecture, database, or code-quality standard relevant to the design.
5. If a gate may apply, read [`human-approval`](../../governance/human-approval.md) before mutation.

## Workflow

1. Restate the expected observable behavior and acceptance criteria.
2. Inspect the existing implementation, tests, conventions, and actual project commands.
3. Choose the smallest coherent design; identify compatibility and edge cases.
4. If approval is required, report `APPROVAL_REQUIRED` and stop before the gated action.
5. Implement only required behavior and supporting changes.
6. Add or update tests at the lowest useful level; explain when a test is impractical.
7. Run project-required and risk-proportional validation. Record each considered gate using the validation contract.
8. Review the complete diff for correctness, security, regressions, accidental scope, and temporary artifacts.
9. Apply [`definition-of-done`](../../standards/definition-of-done.md) and issue the final report.

## Required outcomes

- Acceptance criteria are satisfied.
- Relevant tests and validation provide evidence.
- Compatibility and failure behavior are considered.
- No unrelated changes are included.
- Required approvals are documented.

Never invent a project command or call the task complete with a failed or blocked required gate.
