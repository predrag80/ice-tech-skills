# Git Standard

Load this standard when preparing, reviewing, or handing off repository changes.

## Working tree safety

- Inspect status and relevant diffs before editing and before reporting completion.
- Treat pre-existing changes as user-owned. Do not overwrite, revert, stage, or include them without authorization.
- Keep the task diff minimal; separate generated artifacts from source where the project expects that distinction.
- Do not use destructive history or working-tree operations without explicit authorization and exact target verification.

## Commits and history

- Commit only when requested or required by the workflow.
- Keep commits coherent and messages focused on intent and impact.
- Do not amend, rebase, force-push, tag, or publish without explicit scope and authorization.
- Never claim a commit, push, or clean tree unless verified.

## Review evidence

The final diff review checks changed and untracked files, generated or secret material, accidental formatting churn, temporary diagnostics, and scope. Report files changed rather than relying only on commit identifiers.
