---
description: Pull the raw/ submodules to the latest state and show the diff since the previous sync
argument-hint: "[target submodule (defaults to all under raw/)]"
---

Read `AGENTS.md`'s "## Workflow > ### Update" and execute those steps. Target: **$ARGUMENTS** (if omitted, all submodules under `raw/`).

- `AGENTS.md` is the source of truth for the procedure, commit convention, and log entry format. Do not repeat them here.
- The previous sync state is defined by the committed submodule pointers. If there is no diff, report "up to date" and skip the commit.
