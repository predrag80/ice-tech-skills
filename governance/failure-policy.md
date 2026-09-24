# Failure Policy

Treat a failure as evidence to investigate, not as permission to weaken a gate.

## Recovery loop

```text
FAIL -> IDENTIFY CAUSE -> SAFE IN-SCOPE FIX -> RE-RUN FAILED CHECK
     -> RUN RELEVANT REGRESSIONS -> REVIEW
```

## Rules

1. Separate failures caused by the task from verified pre-existing failures.
2. Preserve the original output needed to explain the failure; redact secrets and irrelevant noise.
3. Make only safe, authorized, in-scope corrections.
4. Re-run the failed check before broader regressions.
5. Do not repeatedly apply speculative fixes without new evidence.
6. Stop when resolution requires new authorization, materially broader scope, destructive action, unavailable infrastructure, or unacceptable risk.

## Terminal outcomes

- `COMPLETE`: all required gates now pass or are justified `NOT_APPLICABLE`.
- `BLOCKED`: an external prerequisite or environment prevents required progress/evidence.
- `APPROVAL_REQUIRED`: the next legitimate recovery action is gated.
- `FAILED`: an attempted implementation or validation remains unsuccessful and no safe in-scope correction remains.

A report must never say “complete except for failing tests.”
