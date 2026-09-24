# JavaScript Adapter

Load when JavaScript source or configuration is in scope. Evidence may include `.js`, `.mjs`, `.cjs`, `package.json`, or established JavaScript tooling.

## Apply

- Respect the repository's module system, runtime targets, package manager, and lockfile; do not mix ESM/CommonJS or managers casually.
- Preserve async error propagation. Await or deliberately return promises, handle cancellation/timeouts where boundaries require them, and avoid unhandled rejections.
- Treat coercion, mutation, prototype behavior, sparse/empty values, dates, and number precision as explicit design concerns.
- Validate data crossing network, storage, process, or user-input boundaries; runtime values are not protected by editor inference.
- Avoid changing generated bundles or lockfiles unless the task requires it. Dependency additions require approval policy evaluation.

## Validate

Discover commands from project scripts and CI. Depending on scope, consider formatting, lint, tests, runtime compatibility, package/build output, and browser/server behavior. Do not invent `npm` commands or assume Node.js is the only runtime.
