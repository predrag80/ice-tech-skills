# ICE Tech Skills

**Repository:** `ice-tech-skills`  
**Version:** 1.0  
**Status:** Ready for use

ICE Tech Skills is a stack-agnostic software-engineering workflow library for Codex. It keeps reusable engineering process separate from framework-specific rules and from each project's actual commands.

`SPEC.md` is the source of truth. If another document conflicts with it, follow `SPEC.md` and update the conflicting document.

## Architecture

```text
user request
  -> project context
  -> one primary skill
  -> relevant governance and standards
  -> detected/configured stack adapters
  -> implementation and proportional validation
  -> structured final report
```

```text
ice-tech-skills/
├── README.md
├── SPEC.md
├── skills/       # short, operational workflows
├── standards/    # stack-independent quality rules
├── stacks/       # technology adapters
├── governance/   # routing, risk, approval, and validation contracts
└── templates/    # project configuration and final report
```

## Core skills

| Primary skill | Use it for |
|---|---|
| `implement-feature` | New externally observable behavior |
| `fix-bug` | Incorrect behavior with a known or reproducible symptom |
| `refactor` | Structural improvement without intended behavior change |
| `investigate` | Evidence gathering when the cause is unknown |
| `database-change` | Schema, migration, persisted data, index, constraint, or material query change |
| `code-review` | Review of existing changes; findings first |

Every task has exactly one primary skill. Other skills may support it without creating a second completion contract.

## Using the system with Codex

ICE Tech Skills is packaged as one Codex plugin. Installing the plugin keeps all six skills and their shared governance, standards, adapters, and templates in one versioned unit.

For local development:

1. Clone this repository into a local plugin directory, such as `~/.codex/plugins/ice-tech-skills`.
2. Add the plugin to a personal or repository marketplace in Codex. Point the marketplace entry at the complete plugin directory, not at an individual skill folder.
3. Restart the Codex app, install **ICE Tech Skills** from that marketplace, and test it in a new task.
4. Add a project-local configuration based on [`templates/project.config.yaml`](templates/project.config.yaml), or expose equivalent commands and rules in project documentation.

The portable [`plugin.json`](plugin.json) is the canonical package manifest. [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) is retained as a compatibility manifest. Codex discovers all folders under `skills/` from the plugin root, so shared relative references remain inside the installed package.

Run the repository preflight before publishing a change:

```bash
python3 scripts/validate_repository.py
```

See the [official OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins) for current marketplace and installation steps.

A project should normally contain only its own source, project instructions, and a small configuration file. A WordPress task may load PHP, WordPress, and JavaScript adapters; a Next.js task may load TypeScript, React, Next.js, and PostgreSQL only when the database is in scope.

## Context-loading contract

Start with the selected `SKILL.md`. Then load only:

- project instructions and configured validation commands;
- governance documents required by the current decision;
- standards referenced by the skill and task;
- stack adapters evidenced by the files being changed.

Do not load every standard or adapter by default. Explicit project rules override adapter defaults unless they conflict with safety, approval, or validation integrity.

## Status contracts

Validation checks use `PASS`, `FAIL`, `NOT_APPLICABLE`, or `BLOCKED`.

Tasks use `COMPLETE`, `BLOCKED`, `APPROVAL_REQUIRED`, or `FAILED`.

`COMPLETE` requires evidence for every required quality gate. A failed or blocked required check can never be described as complete.

## Adding a stack

Add `stacks/<name>/RULES.md`. Include detection evidence, stack-specific concerns, validation discovery, and task-sensitive guidance. Do not duplicate core workflow or stack-independent standards, and do not hardcode project commands.

## Versioning

Version 1.0 is intentionally small. Architecture or governance changes must first be reflected in [`SPEC.md`](SPEC.md). Project-specific conventions belong in the project, not in this repository.
