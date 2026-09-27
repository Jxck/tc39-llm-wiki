---
description: Summarize a meeting by topic into daily files under wiki/meetings/
argument-hint: "[meeting (YYYY-MM) | tc39/notes PR number/URL (defaults to the latest meeting in raw/notes)]"
---

Read `AGENTS.md`'s "## Workflow > ### Summarise" and follow the procedure and format to summarize the meeting. Target: **$ARGUMENTS** (if omitted, the latest meeting under `raw/notes/meetings/`).

- If the target is a tc39/notes PR number or URL, check out `pr-<PR>` using the steps in `AGENTS.md` for summarizing a meeting that exists only in an unmerged PR, then summarize the meetings added by that PR.
- `AGENTS.md` is the source of truth for the format, output location, index generation, and link generation (people/proposals). Do not repeat them here.
- Each daily file can be read independently, so it is fine to process them in parallel by day.
