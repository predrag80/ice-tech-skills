# Next.js Adapter

Load when a Next.js application is evidenced by its configuration, dependencies, or routing structure. Also load React and the project's JavaScript/TypeScript adapter.

## Apply

- Detect the project's Next.js version and router/layout conventions; do not assume App Router, Pages Router, or a particular release behavior.
- Preserve the server/client boundary. Add client execution only where interactivity or browser APIs require it; keep secrets and privileged data server-side.
- Treat route handlers, middleware, server actions, and API routes as trust boundaries with authentication, authorization, validation, and safe errors.
- Make caching, revalidation, dynamic rendering, streaming, redirects, and not-found behavior explicit where affected.
- Avoid passing non-serializable or sensitive values across the server/client boundary.
- Consider metadata, loading/error UI, hydration, accessibility, and runtime/edge compatibility.
- Do not expose server environment variables through client bundles.

## Validate

Use project scripts and CI. Depending on scope, validate lint/types/tests, production build, route behavior, server/client boundaries, and caching/revalidation. A development server rendering once does not prove a production build or cache policy.
