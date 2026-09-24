# Architecture Standard

Load this standard when a change crosses module/service boundaries, introduces a new dependency or abstraction, changes a public contract, or affects a major runtime/data flow.

## Principles

- Fit the existing architecture unless the task explicitly authorizes changing it.
- Keep domain rules independent from delivery, persistence, and framework details where the project already supports that separation.
- Direct dependencies toward stable contracts; avoid cycles and hidden coupling.
- Prefer a local change over a new subsystem when both satisfy the requirement safely.
- Define ownership of state, transactions, retries, lifecycle, and failure handling.
- Preserve backward compatibility across independently deployed components or plan an ordered transition.
- Make observability proportional to operational impact.

## Decision record

For a material choice, record: context, constraints, considered options, decision, tradeoffs, compatibility, and rollback. A major architecture change is HIGH risk and requires approval before implementation.
