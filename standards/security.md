# Security Standard

Load this standard when a task touches trust boundaries, identity, authorization, sensitive data, user input, dependencies, network exposure, file access, secrets, or production configuration.

## Required review

- Identify assets, actors, trust boundaries, and the new or changed attack surface.
- Enforce authorization server-side at the resource/action boundary; authentication alone is insufficient.
- Validate, normalize, and constrain untrusted input; encode output for its destination context.
- Use parameterized data access and safe platform APIs.
- Protect sensitive data in storage, transit, logs, errors, fixtures, and telemetry.
- Preserve CSRF, replay, rate-limit, session, origin, and permission controls where applicable.
- Use least privilege and secure defaults. Failure must not silently become access.
- Evaluate dependency provenance and necessity before addition or upgrade.

## Secrets

Never invent, expose, log, commit, or copy live credentials. Secret creation, rotation, or movement across trust boundaries requires explicit authorization and a redacted plan.

## Reporting

A security review is `PASS` only when the relevant surface was actually inspected and no blocking issue remains. Automated scanners supplement, not replace, contextual review. Significant auth changes, secret handling, and security-control removal require approval.
