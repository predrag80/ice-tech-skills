# ICE Tech Skills Specification

**Version:** 1.0  
**Status:** Architecture Approved / Ready for Implementation  
**Project:** ICE Tech Skills  
**Repository:** `ice-tech-skills`

## 1. Purpose

ICE Tech Skills is a stack-agnostic software-engineering workflow for AI coding agents such as Codex. It defines how an agent understands work, selects a workflow, plans, implements, validates, reviews, protects scope, handles risk and approval, and decides whether a task is complete.

The system supports JavaScript, TypeScript, React, Next.js, PHP, WordPress, and PostgreSQL in v1. Additional stacks may be added without changing the core workflow.

## 2. Normative language and precedence

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` are normative. This file is the source of truth.

Resolution order:

1. explicit user request and authorization boundaries;
2. repository/project instructions and `project.config.yaml`;
3. this specification and governance rules;
4. selected core skill;
5. relevant engineering standards;
6. relevant stack adapters.

Lower layers specialize higher layers but must not weaken safety, approval, scope, or validation-integrity requirements. Conflicts must be reported.

## 3. Core principles

### 3.1 Stack agnostic

Core skills MUST NOT depend on a language, framework, database, package manager, or command. Technology behavior belongs in stack adapters; actual commands belong to the project.

### 3.2 Minimal change

The agent MUST make the smallest reasonable change that fully satisfies the request. Unrelated work MUST be reported, not silently added.

### 3.3 Evidence-based completion

The agent MUST NOT claim a validation passed unless it was performed and evidence was observed. Inspection and assumptions are not substitutes for commands when executable validation is required.

### 3.4 Tests are implementation

New behavior SHOULD include appropriate tests. Bug fixes SHOULD include a regression test when practical. Omissions require an explicit reason.

### 3.5 Human control

HIGH-risk work and explicitly gated operations require approval before the gated mutation. A general request to complete a task is not approval for a later-discovered destructive or materially different action.

### 3.6 Validation integrity

Checks MUST NOT be weakened merely to obtain a passing result. Changes to tests or rules require a product or correctness justification independent of the failure.

### 3.7 Progressive Context Loading

Only context relevant to the task is loaded:

```text
USER REQUEST -> PROJECT CONTEXT -> PRIMARY SKILL -> STACK EVIDENCE
             -> RISK -> RELEVANT GOVERNANCE/STANDARDS -> EXECUTION
```

The entire repository MUST NOT become default context for every task.

### 3.8 Proportional Validation

Validation depth MUST match scope and risk while preserving all project-required checks.

- `LOW`: focused relevant checks and diff review.
- `MEDIUM`: lint/static checks, relevant tests, build where applicable, and diff review.
- `HIGH`: approval, full relevant validation, security/data review, regression checks, and final diff review.

Proportionality MUST NOT be used to skip an explicitly required project check.

## 4. System architecture

```text
CORE WORKFLOW
  + PRIMARY SKILL
  + RELEVANT ENGINEERING STANDARDS
  + RELEVANT STACK ADAPTERS
  + PROJECT CONFIGURATION
  + GOVERNANCE
  = TASK EXECUTION CONTEXT
```

## 5. Core workflow

Implementation work follows:

```text
UNDERSTAND -> PLAN -> IMPLEMENT -> VALIDATE -> REVIEW -> QUALITY GATE -> COMPLETE
```

Before mutation, the agent MUST understand project context, select one primary skill, detect relevant stacks from evidence, classify risk, and evaluate approval gates.

## 6. Core skills

### 6.1 `implement-feature`

For new behavior. Outcome: requested behavior, appropriate tests, completed relevant validation, and reviewed diff.

### 6.2 `fix-bug`

For incorrect behavior: reproduce, establish root cause, create or update a regression test where practical, confirm the failure, implement the minimal fix, confirm the pass, run relevant regressions, and review.

### 6.3 `refactor`

For structural improvement without intended behavior change. Establish a passing baseline, refactor, repeat equivalent checks, and compare behavior.

### 6.4 `investigate`

For unknown cause. The outcome is evidence, conclusions with confidence, and next steps. It may finish without a code change and MUST NOT silently become an implementation task.

### 6.5 `database-change`

For schema, migration, persisted data, constraints, indexes, or material query changes. It adds integrity, compatibility, rollout, recovery, locking, and performance concerns.

### 6.6 `code-review`

For existing changes. Findings are prioritized by correctness, regressions, security, data integrity, architecture, and test coverage. Review does not imply authorization to edit.

## 7. Skill routing

Each task MUST have exactly one primary skill. Supporting workflows MAY be used. A feature containing a migration normally uses `implement-feature` as primary and applies `database-change` as supporting guidance. A standalone migration uses `database-change` as primary. Unknown causes route to `investigate` until evidence supports a different task.

## 8. Engineering standards

The v1 standards are code quality, testing, security, architecture, database, git, and definition of done. They remain technology-independent where practical and are loaded only when relevant.

## 9. Stack adapters

The v1 adapters are JavaScript, TypeScript, React, Next.js, PHP, WordPress, and PostgreSQL. Adapters translate general standards into stack-specific concerns, MUST NOT duplicate core workflow unnecessarily, and MUST NOT invent project commands.

## 10. Project configuration and detection

A project MAY define `project.config.yaml` with identity, stack, validation commands, required gates, risk overrides, and approval policy. It SHOULD remain small.

Context resolution priority is:

```text
EXPLICIT PROJECT CONFIG -> REPOSITORY CONFIGURATION -> SAFE AUTO-DETECTION
```

Detection evidence MAY include `package.json`, `composer.json`, `tsconfig.json`, `next.config.*`, `wp-config.php`, database schemas, migrations, and established CI configuration. The agent MUST NOT invent commands.

## 11. Risk classification

Every implementation task is `LOW`, `MEDIUM`, or `HIGH`.

- `LOW`: documentation, styling, isolated tests, or small local fixes with limited blast radius.
- `MEDIUM`: business logic, APIs, state management, database queries, or significant features.
- `HIGH`: destructive data operations, authentication/authorization, payments, secrets, production configuration, breaking APIs, irreversible migrations, or major architecture changes.

Risk is based on impact, reversibility, exposure, data sensitivity, and uncertainty—not file count alone. When levels differ across dimensions, use the highest credible level.

## 12. Human approval

Approval is required before HIGH-risk work and before:

1. destructive database operations;
2. significant authentication/authorization changes;
3. adding or removing production dependencies;
4. significant development dependencies in v1;
5. breaking public API changes;
6. significant production infrastructure/configuration changes;
7. handling or rotating secrets/credentials;
8. major architectural changes.

Before approval, the agent MUST report the proposed action, reason, impact, risk, exact operation, validation/recovery plan, and alternatives where relevant. The task status is `APPROVAL_REQUIRED`.

## 13. Validation contract

Every considered validation gate has exactly one status:

- `PASS`: performed successfully, with evidence.
- `FAIL`: performed and failed.
- `NOT_APPLICABLE`: does not apply, with a brief reason when non-obvious.
- `BLOCKED`: should run but cannot, with blocker and consequence.

Default pipeline:

```text
FORMAT -> LINT -> STATIC/TYPE ANALYSIS -> UNIT TESTS -> INTEGRATION TESTS
       -> BUILD -> SECURITY REVIEW -> FINAL DIFF REVIEW
```

Only applicable checks run, subject to project-required gates and proportional validation. Manual reviews identify their reviewed scope and evidence.

## 14. Failure policy

```text
FAIL -> INVESTIGATE -> FIX -> RE-RUN FAILED CHECK -> RELEVANT REGRESSIONS
```

The agent MAY make safe, in-scope corrections. It MUST stop when resolution needs new authority, broadens scope materially, risks damage, or repeats without useful new evidence. An unresolved required gate prevents `COMPLETE`.

## 15. Scope protection

Incidental improvements are not authorized merely because they are nearby. Required supporting edits are allowed when necessary and explained. Unrelated observations belong in final notes.

## 16. Validation integrity

Without an independent correctness justification, the agent MUST NOT remove or skip failing tests, weaken assertions, disable lint/security rules, add type suppressions, hide runtime errors, or change expected output merely to pass validation.

## 17. Definition of done

An implementation task is `COMPLETE` only when:

- requested behavior is implemented;
- appropriate tests exist or omission is justified;
- all required validations are `PASS` or justified `NOT_APPLICABLE`;
- security, data, and compatibility concerns relevant to the change were reviewed;
- scope was respected;
- final diff was reviewed;
- required approvals were obtained;
- no unresolved required quality gate remains.

Skill-specific completion rules also apply.

## 18. Task status

- `COMPLETE`: the selected skill's outcome and every required gate are satisfied.
- `BLOCKED`: an external condition or unavailable prerequisite prevents required progress or validation.
- `APPROVAL_REQUIRED`: a defined gate must be approved before continuing.
- `FAILED`: execution or validation ended unsuccessfully and no safe in-scope correction remains.

These task statuses are distinct from validation statuses.

## 19. Final report

Every task finishes with a concise report containing:

```text
STATUS
SKILL
RISK
SUMMARY
FILES CHANGED
VALIDATION
TESTS
REVIEW
NOTES
```

Claims MUST be specific enough to audit. Approval requests also include the exact gated action and expected impact.

## 20. Repository architecture

```text
ice-tech-skills/
├── README.md
├── SPEC.md
├── skills/
│   ├── implement-feature/SKILL.md
│   ├── fix-bug/SKILL.md
│   ├── refactor/SKILL.md
│   ├── investigate/SKILL.md
│   ├── database-change/SKILL.md
│   └── code-review/SKILL.md
├── standards/
│   ├── code-quality.md
│   ├── testing.md
│   ├── security.md
│   ├── architecture.md
│   ├── database.md
│   ├── git.md
│   └── definition-of-done.md
├── stacks/
│   ├── javascript/RULES.md
│   ├── typescript/RULES.md
│   ├── react/RULES.md
│   ├── nextjs/RULES.md
│   ├── php/RULES.md
│   ├── wordpress/RULES.md
│   └── postgresql/RULES.md
├── governance/
│   ├── skill-routing.md
│   ├── risk-classification.md
│   ├── human-approval.md
│   ├── validation-contract.md
│   ├── failure-policy.md
│   ├── scope-protection.md
│   └── validation-integrity.md
└── templates/
    ├── project.config.yaml
    └── final-report.md
```

## 21. v1 constraints

Version 1.0 MUST remain intentionally small. It does not replace project documentation or CI/CD, support every stack, deploy automatically, perform destructive production operations automatically, introduce approval gates without risk, or load the whole knowledge base for every task.

> Strong rules, small skills, progressive context.

## 22. Change control

Architectural or governance changes MUST be recorded here before they become part of ICE Tech Skills. Supporting documents MAY clarify this specification but MUST NOT silently redefine it.
