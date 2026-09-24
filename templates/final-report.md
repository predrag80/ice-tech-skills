# ICE Tech Skills Final Report

Use one terminal task status: `COMPLETE`, `BLOCKED`, `APPROVAL_REQUIRED`, or `FAILED`.

```markdown
STATUS: <status>
SKILL: <primary skill>
RISK: <LOW | MEDIUM | HIGH>

## Summary

- <observable result or investigation/review conclusion>

## Files changed

- `<path>` — <reason>
- None (for a read-only task)

## Validation

| Check | Status | Evidence |
|---|---|---|
| Format | <PASS/FAIL/NOT_APPLICABLE/BLOCKED> | <command, scope, or reason> |
| Lint | <...> | <...> |
| Static/type analysis | <...> | <...> |
| Unit tests | <...> | <...> |
| Integration tests | <...> | <...> |
| Build | <...> | <...> |
| Security/data review | <...> | <reviewed scope and result> |
| Final diff review | <...> | <reviewed scope and result> |

## Tests

- Added/updated: <tests or None>
- Coverage rationale: <what behavior is evidenced; explain omissions>

## Review

- Scope: <respected or exception>
- Compatibility/risks: <result>
- Approvals: <not required, obtained with scope, or pending>

## Notes

- <limitations, pre-existing failures, follow-up observations, or None>
```

For `APPROVAL_REQUIRED`, add:

```markdown
## Approval request

- Proposed action: <exact operation and target>
- Reason: <why needed>
- Impact and risk: <users, system, data, reversibility>
- Validation/recovery: <plan>
- Alternatives: <lower-risk options or None>
- Decision needed: <precise approval question>
```
