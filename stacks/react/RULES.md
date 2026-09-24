# React Adapter

Load when React components, hooks, context, or React-rendered behavior is in scope. Also load the JavaScript or TypeScript adapter used by the project.

## Apply

- Keep rendering pure. Put synchronization with external systems in effects, not derived values or ordinary event logic.
- Keep state minimal, colocated, and single-sourced; derive rather than duplicate when practical.
- Follow hook dependency and ordering rules. Handle cleanup, stale closures, races, and development-mode repeated execution.
- Preserve component identity and stable keys; do not use index keys when collection identity can change.
- Maintain controlled/uncontrolled contracts and avoid hydration-sensitive nondeterminism where server rendering exists.
- Preserve semantic HTML, keyboard behavior, focus management, labels, announcements, and contrast relevant to the change.
- Use memoization for measured or credible cost/identity needs, not by default.

## Validate

Test user-observable behavior and interactions rather than component internals. Use the project's commands for lint, component/unit tests, build, and any visual/accessibility checks relevant to the changed surface.
