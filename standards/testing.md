# Testing Standard

Load this standard when behavior changes, a bug is fixed, or a refactor needs behavioral evidence.

## Test selection

- Test externally meaningful behavior at the lowest layer that gives sufficient confidence.
- Add unit tests for isolated logic, integration tests for boundaries, and end-to-end tests only for critical cross-system paths.
- New behavior SHOULD cover the primary path, important boundary cases, and meaningful failures.
- Bug fixes SHOULD include a regression test that fails for the intended reason before the fix.
- Refactors require comparable before/after evidence; add characterization tests when important behavior is otherwise unprotected.

## Integrity

- A passing test is evidence only for what it asserts.
- Do not replace assertions with snapshots or mocks that reduce useful coverage merely to pass.
- Mock unstable or expensive boundaries, not the behavior under test.
- Keep tests deterministic: control time, randomness, network, and shared state when relevant.
- Do not delete, skip, or weaken a failing test without an independent requirement or correctness reason recorded in the report.

## Execution and reporting

Use project-defined commands. Run focused tests during iteration, then all project-required and relevant regression checks. Report the exact command or check, result, and scope. If a test is omitted, state why and what evidence substitutes for it; omission never becomes `PASS`.
