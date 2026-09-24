---
name: refactor
description: Improve internal code structure while preserving externally observable behavior, using equivalent validation before and after. Use for explicitly requested structural work, not feature changes, bug fixes, or opportunistic cleanup.
---

# Refactor

Improve structure without intentionally changing behavior.

## Load context progressively

Read project instructions, relevant stack adapters, [`code-quality`](../../standards/code-quality.md), [`architecture`](../../standards/architecture.md) when boundaries change, and the validation/risk governance needed for the scope.

## Workflow

1. Define the structural goal, boundaries, and behaviors that must remain unchanged.
2. Identify objective evidence: existing tests, public contracts, snapshots, types, performance constraints, or targeted characterization tests.
3. Run the relevant baseline checks before editing. If the baseline already fails, record it and do not attribute it to the refactor.
4. Make small, reviewable structural changes. Do not bundle features or unrelated cleanup.
5. Run equivalent checks after the change plus any validation required by affected boundaries.
6. Compare before/after behavior and review the full diff for accidental semantic change.
7. Apply [`definition-of-done`](../../standards/definition-of-done.md) and report baseline and final evidence separately.

## Required outcomes

- The structural improvement is clear and scoped.
- Observable behavior is preserved by evidence, not assumption.
- Baseline and after-validation are reported.
- Public contracts, data shape, side effects, errors, and performance remain compatible unless explicitly authorized otherwise.

If behavior must change to finish, reclassify the work and obtain any newly required approval before continuing.
