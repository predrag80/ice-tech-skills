# Scope Protection

Make the smallest reasonable change that fully satisfies the request.

## In scope

- files and behavior explicitly requested;
- supporting edits strictly necessary for correctness, tests, compatibility, or validation;
- newly discovered issues that directly block safe completion, after explaining their necessity;
- approved gated actions within their exact approved bounds.

## Out of scope by default

- opportunistic refactors, renames, formatting, dependency upgrades, or cleanup;
- unrelated test/lint failures;
- adjacent feature ideas;
- broad architecture changes motivated only by preference;
- editing user-owned pre-existing changes.

## Decision test

Before an additional change, ask:

1. Is it required to satisfy the request or a mandatory gate?
2. Is it the least invasive safe option?
3. Does it introduce new risk, behavior, dependency, or approval needs?
4. Can it instead be reported as an observation?

If the work materially expands scope, stop and request direction. Final review must identify incidental observations separately from changed behavior.
