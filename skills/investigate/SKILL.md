---
name: investigate
description: Investigate an unknown software problem through bounded, read-first evidence gathering and produce a supported conclusion or next experiment. Use when the cause is unknown; do not silently implement a fix unless the request explicitly includes it.
---

# Investigate

Turn uncertainty into auditable evidence. A successful investigation may change no files.

## Load context progressively

Read project instructions and only the stack adapters or standards needed to interpret the observed system. Load risk and approval governance before any invasive experiment, production access, secret handling, or persistent mutation.

## Workflow

1. State the question, observed symptom, scope, constraints, and what evidence would discriminate between plausible causes.
2. Inspect existing code, configuration, tests, logs, and history using read-only methods first.
3. Form a small set of ranked hypotheses. Label assumptions explicitly.
4. Run the least invasive discriminating check for the leading hypothesis. Keep experiments reversible and avoid persistent changes unless authorized.
5. Update hypotheses from evidence; stop repeating an experiment that yields no new information.
6. Conclude with root cause and confidence, or list what remains unknown and the next evidence needed.
7. Report changed files, if any, and validation of any temporary diagnostic edit. Remove temporary artifacts.

## Required outcomes

- Evidence is separated from inference.
- Commands, observations, and relevant limitations are recorded.
- The conclusion states confidence and competing explanations.
- Recommended remediation identifies likely skill, risk, validation, and approval needs.

Use `BLOCKED` when required evidence is inaccessible. Use `COMPLETE` when the investigation question has been answered even if no fix was requested.
