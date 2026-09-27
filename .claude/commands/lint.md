---
description: Check wiki health (internal consistency plus source cross-checks)
argument-hint: "[target page/proposal (defaults to the whole wiki)]"
---

Read `AGENTS.md`'s "## Workflow > ### Lint" and follow those steps to run the health check. Target: **$ARGUMENTS** (if omitted, the whole wiki).

- `AGENTS.md` is the source of truth for the review criteria (internal consistency and source consistency). Do not repeat them here.
- Report findings as a list, confirm before fixing them, and then make the fixes (obvious mistakes may be fixed before reporting). Finally, record the run in `wiki/log.md` as `lint`.
