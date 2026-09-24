# Code Quality Standard

Load this standard when implementation or refactoring changes executable code.

## Required qualities

- Prefer the smallest clear solution that fits existing project conventions.
- Keep responsibilities and dependencies explicit; avoid hidden global effects.
- Preserve public contracts unless a change is requested and approved.
- Use names that communicate domain intent. Comments explain non-obvious reasons, not syntax.
- Handle errors at the layer that has enough context to act; do not silently discard them.
- Validate inputs at trust boundaries and keep outputs deterministic where practical.
- Remove temporary diagnostics, dead branches, unused imports, and accidental artifacts introduced by the task.
- Avoid speculative abstraction. Extract only when it improves a real boundary, reuse, or testability.

## Review questions

1. Is the behavior readable from the code and tests?
2. Are mutation, ownership, lifecycle, and side effects bounded?
3. Are null, empty, error, concurrency, and retry cases handled where relevant?
4. Does the change preserve compatibility and performance expectations?
5. Is complexity proportional to the requirement?

Formatting tools and local conventions take precedence over personal style. A quality improvement outside the request is a note, not automatic scope.
