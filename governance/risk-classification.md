# Risk Classification

Classify every implementation task before mutation. Investigation and review experiments are classified when they can change state or expose sensitive data.

## Dimensions

Assess:

- blast radius and user/operational impact;
- reversibility and recovery cost;
- data sensitivity and integrity;
- security/trust-boundary effect;
- compatibility and deployment coordination;
- uncertainty, novelty, and observability.

Use the highest credible level across dimensions. File count and diff size are not sufficient proxies.

## LOW

Limited, local, easily reversible, and well understood.

Examples: documentation, styling, isolated test improvement, small local fix with no public contract or persisted-data effect.

Expected validation: focused relevant checks, any project-required gates, and final diff review.

## MEDIUM

Meaningful application behavior or boundary impact, but reversible through normal delivery practices.

Examples: business logic, API implementation without breaking change, state management, database reads, significant feature, dependency upgrade already authorized by policy.

Expected validation: lint/static analysis, relevant unit/integration tests, build where applicable, boundary review, and final diff review.

## HIGH

Large impact, sensitive trust/data boundary, difficult recovery, or irreversible/production consequence.

Examples: destructive data change, authentication/authorization, payment logic, secret handling, production configuration, breaking API, irreversible migration, major architecture change.

Expected handling: explicit approval before mutation, full relevant validation, recovery/rollback plan, security/data review, regression checks, and final diff review.

## Escalation

Reclassify immediately when new evidence increases risk. Do not downgrade solely because the code change is small. Project configuration may raise a level but MUST NOT lower a clearly HIGH-risk operation below HIGH.
