# TC39 Wiki — Agent Schema

This repository uses the TC39 plenary notes (`raw/notes`) as raw material for a wiki that an LLM builds and maintains, one that lets you trace **how each proposal changed stage over time and what issues came up along the way**. See [llm-wiki.md](llm-wiki.md) for the design rationale.

This file is the wiki's operating schema. A new session should read this first and follow it when doing ingest / query / lint.

## Layers

- **Raw sources** — `raw/` (a set of submodules). **Read-only, immutable**. Never edit. This is the ground-truth material.
  - `raw/notes/` (tc39/notes) — verbatim plenary transcripts. **The primary source for history, issues, and speaker attribution**.
  - `raw/proposals/` (tc39/proposals) — the canonical proposal list (tables by current stage + champions). **The primary source for a proposal's confirmed current stage / status / champion**.
- **The wiki** — `wiki/`. Fully owned by the LLM. It generates/updates proposal pages, indexes, and the log.
- **Generated** — `wiki/_generated/`, `wiki/people/`, `wiki/proposals/index.md`. Machine-extracted output from `tools/` scripts. **Do not hand-edit** (regeneration overwrites it).

**Precedence between sources**: which one to trust when they disagree.

- History (the year/month and direction of stage transitions), issues, and speaker attribution → **`raw/notes`** is primary.
- A proposal's confirmed **current stage (`current_stage` / `status`) and champion** → **`raw/proposals`** is primary. If a current stage inferred from notes disagrees with proposals, first suspect the notes-side reading and re-trace both to resolve it.
- `raw/proposals` is a **current snapshot** and carries no history. Conversely, notes tell the history but are weak for confirming the current stage. The two play different roles, so cross-check both rather than filling in from just one.

## Directory layout

```
raw/notes/meetings/<YYYY-MM>/<month-DD>.md   material (verbatim transcripts)
raw/proposals/README.md                      Active proposal tables (Stage 3 / 2.7 / 2)
raw/proposals/finished-proposals.md          Stage 4 (shipped)
raw/proposals/stage-1-proposals.md           Stage 1
raw/proposals/inactive-proposals.md          withdrawn / inactive
wiki/
  README.md                 proposal catalog (with current stage, by category)
  log.md                    chronological ingest/query/lint log (append-only)
  proposals/<slug>.md       a deep-read page per proposal (history + issues)
  proposals/index.md        stage list of all proposals (generated. Stage 4 lists only what's unshipped. Built from raw/proposals. Do not hand-edit)
  families/<family>.md      cross-cutting synthesis (bundles multiple proposals; per-proposal history/issues stay in proposals)
  meetings/<YYYY-MM>/        per-meeting daily summaries (output of summarise. One file per day + README.md)
  people/<ABBR>.md          person reference (generated. filename = abbreviation)
  _generated/
    agenda-index.md         agenda index for all 86 meetings (a grep-able backbone)
    agenda-index.jsonl       the same, machine-readable
tools/
  extract_agenda.py         generates agenda-index
  extract_proposals.py      generates the all-proposals stage list wiki/proposals/index.md from raw/proposals (filters Stage 4 to unshipped only)
  extract_people.py         generates people/ pages for people appearing in proposal pages
  link_people.py            links abbreviations in proposal/family/meeting-summary pages to [ABBR](<rel>/people/ABBR.md)
  link_proposals.py         links proposal names in meeting summaries to proposal pages, and ensures the topic-opening meta line (wiki → proposal → slide)
```

## Language convention

- Body text (overview, history, discussion of issues) is **English**. Fully migrated from the Japanese version in 2026-09 (the old Japanese version survives only in git history).
- **Proposal names, stage notation, API names, spec terminology, and person abbreviations (abbreviations stay as-is) are English**. e.g. `Temporal`, `Stage 2.7`, `Array.fromAsync`, `[[Get]]`, `PFC`.
- **When quoting a speaker from the notes, keep the original English as-is** (do not translate). Summaries and paraphrases in body text are also in English.

## Proposal page format

`wiki/proposals/<slug>.md`. `<slug>` is kebab-case English (e.g. `temporal`, `decorators`, `records-and-tuples`).

YAML frontmatter at the top (for Obsidian Dataview):

```yaml
---
title: Temporal
slug: temporal
status: shipped        # stage0 | stage1 | stage2 | stage2.7 | stage3 | shipped | withdrawn | inactive
current_stage: 4       # 0 / 1 / 2 / 2.7 / 3 / 4
ecma: [262, 402]       # affected specs
champions: [PFC, ...]  # abbreviations
first_seen: "2017-09"  # meeting first proposed (YYYY-MM)
reached_stage4: "2026-03"
families: [date-time]  # families it belongs to (optional, can be multiple. Corresponds both ways with `wiki/families/<family>.md`)
tags: [proposal, date-time]
---
```

Body sections (headings are fixed, in English):

1. `## Overview` — 1-3 paragraphs. What problem the proposal solves.
2. `## Stage history` — a chronological table, one row per event:

   | Meeting                                  | Event                                   | Stage |
   | ---------------------------------------- | --------------------------------------- | ----- |
   | [2018-09](../_generated/agenda-index.md) | Reached Stage 2. `Temporal for Stage 2` | 1 → 2 |

   The meeting cell is a relative link to the corresponding `raw/notes` file (e.g. `[2018-09](../../raw/notes/meetings/2018-09/sept-27.md)`). The Stage column records a transition as `old → new`, or just the current stage for an update-only row. Place the stage-history chart (below) right after the table.

3. Stage-history chart — embed a mermaid `xychart-beta` line chart right below the table. **The x-axis is fixed to the full span with any notes (years 2012-2026)**, and the y-axis is Stage (0-4). Plot the stage as of the end of each year, stacked from the bottom. A year in which the proposal didn't exist yet is 0. For a proposal that passed through Stage 2.7, plot `2.7` as a decimal point. **For a withdrawn proposal, stop the line at the withdrawal year** (end the `line` array there; do not plot further points). Long stalls are naturally expressed as a flat run at the same value (no special marker needed). Right after the chart, add a `>` note on how to read it (the year/month of each transition). Example:

   ````
   ```mermaid
   xychart-beta
       title "Temporal stage 2012-2026"
       x-axis [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
       y-axis "Stage" 0 --> 4
       line [0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4]
   ```
   ````

   Note: `xychart-beta` requires mermaid 10.3+. VSCode's `bierner.markdown-mermaid` webview preview renders it blank (another mermaid extension can render it), so be aware this is renderer-dependent. ASCII is recommended for the title (full-width characters, em dashes, and parentheses can break parsing in some environments).

4. `## Main issues` — points that became contentious during development. One subheading `### <issue name (English)>` per issue. For each: what was at stake / who raised concerns (abbreviation) / at which meeting / how it was resolved (or that it's unresolved). Quote with `>` (kept in the original English).
5. `## Related proposals` — cross-links in the form `[Title](../proposals/other-slug.md)` (a proposal not yet created is written as plain code-formatted text).
6. `## Sources` — a bulleted list of the meeting files referenced.

Link convention: **always use standard markdown relative links** (do not use Obsidian's `[[wikilink]]` syntax, since it doesn't navigate in VSCode's markdown preview; standard links work in both VSCode and Obsidian).

- To source material: `[2018-09](../../raw/notes/meetings/2018-09/sept-27.md)`
- Between proposals: `[Temporal](../proposals/temporal.md)`. To avoid a dead link to a proposal that doesn't have a page yet, write it as plain code-formatted text (e.g. `` `pattern-matching` ``) and turn it into a link once the page is created.
- Person abbreviations: `[PFC](../people/PFC.md)`. Linking is done by `tools/link_people.py`, not by hand (below; it also migrates any existing `[[ABBR]]` to a markdown link automatically). Frontmatter's `champions` is YAML, so don't linkify it (keep it as abbreviations).

## Family page format

`wiki/families/<family>.md`. A **cross-cutting synthesis page** that bundles a group of proposals in the same category (e.g. `iterator`, `modules`, `intl`, `date-time`, `class-features`, `concurrency`). Each proposal's own history/issues stay in `proposals/`; a family page only links to them (don't duplicate the stage-history table or mermaid chart in the family page — avoid maintaining it twice). `<family>` is kebab-case.

YAML frontmatter at the top:

```yaml
---
title: Iterator helpers and friends
slug: iterator
kind: family
members: [iterator-helpers, joint-iteration, iterator-chunking, ...]  # proposal slugs. A proposal without a page yet may still be listed by slug
tags: [family, iterator]
---
```

Body sections (headings are fixed, in English):

1. `## Overview` — what the members have in common (the axis this family groups around).
2. `## Members` — a table `Proposal | Current stage | One-liner`. `[Title](../proposals/<slug>.md)` if the proposal has a page, otherwise plain code-formatted text.
3. `## Cross-cutting themes` — the design principles/issues that run through the family (e.g. iterator's consistent policy of "don't implicitly iterate strings," laziness, async support).
4. `## Related families` — links to neighboring families (`[Title](../families/<slug>.md)`).
5. `## Sources` (optional).

**Membership is bidirectional**: keep the family page's `members` in sync with each proposal's frontmatter `families` (above). Any member that has a proposal page must include this family in its `families`, and the family's `members` must include that slug too. A proposal without a page yet is listed only on the family's `members` side (its absence from `proposals/` means it hasn't been deep-read, not that something's wrong). `README.md` (the wiki's top page) has a families section linking to each family.

## Formatting

Markdown / JSON is formatted with **oxfmt** (config `.oxfmtrc.json`, `proseWrap: preserve` so lines aren't rewrapped, `embeddedLanguageFormatting: off`). Excluded: `raw/**` (submodules, immutable) and `wiki/_generated/**` (generated output, including JSONL).

- Manual: `npm run fmt` (= `oxfmt`), check with `npm run fmt:check`.
- **Enforced automatically**: Claude Code's PostToolUse hook (`.claude/settings.json`) formats any edited .md/.json file immediately, and git's pre-commit hook (`.githooks/pre-commit`, requires `core.hooksPath`) formats staged files and re-stages them.
- Right after cloning, run `git config core.hooksPath .githooks` once.

## Workflow

Each operation also has a Claude Code slash command (`.claude/commands/`): **`/ingest <proposal>`**, **`/query <question>`**, **`/lint [target]`**, **`/update [target submodule]`**, **`/summarise [meeting]`**. The commands hold no procedure of their own — they're just pointers that read the matching workflow in this file and execute it (AGENTS.md is the single source of truth; commands don't restate it).

**Commit convention**: commit changes with an English message carrying a prefix. The prefix is chosen by what caused the change:

- A change caused by an operation (command) → that **operation's name**: `[ingest]` / `[query]` / `[lint]` / `[update]` / `[summarise]` (e.g. `[lint] fix champion attribution in records-and-tuples`).
- A **wiki-wide change not caused by any operation** → `[wiki]`: adding/changing the commands themselves, changes to tools such as `tools/`, structural changes to the repo layout or this file, etc. **Reflecting a convention change into this AGENTS.md (page format, workflow, operating policy additions/changes) is also `[wiki]`**. There's no separate operation/command for reflecting conventions (it's done only when the user explicitly asks for it). `/update` is dedicated to syncing raw sources.

Commits follow the repo/environment's git conventions (signing, rebase, required trailers, etc). Skip committing when there's nothing to commit (e.g. a Query that didn't file anything back).

### Ingest (bringing in material)

1. Decide the target meeting or proposal. Grep `wiki/_generated/agenda-index.md` to identify the relevant agenda items and meetings (e.g. `grep -i -A4 decorators wiki/_generated/agenda-index.md`).
2. Read the matching section in `raw/notes` (`### Conclusion` and `### Speaker's Summary of Key Points` are key for judging the stage).
3. Create or update the proposal page: add a row to the stage-history table, update the stage-history chart (mermaid), add/update issues, refresh frontmatter's `current_stage`/`status`. Keep quotes in the original English.
   - **Don't settle a champion from delegates.txt alone**. Corroborate with that meeting's Presenter line and body text. Abbreviations can be reassigned meeting to meeting (e.g. 2019-10 labels Robin Ricard as RRI, but delegates.txt's RRI=Reefath Rajali is a different person). Also verify speaker attribution and dates against the original text (a spot where misattribution is common).
4. **Generate and link people** (always run this once the proposal page is written):
   - `python3 tools/extract_people.py` — detects abbreviations appearing in proposal pages and generates/regenerates `wiki/people/<ABBR>.md` (full name = delegates.txt, affiliation/meetings attended = attendee tables, champion drafts = cross-referenced from each proposal's frontmatter `champions`).
   - `python3 tools/link_people.py` — links abbreviations in the body of proposal/family/meeting-summary pages to `[ABBR](<rel>/people/ABBR.md)` (idempotent). Frontmatter, code blocks, mermaid, and existing links are protected.
   - `python3 tools/link_proposals.py` — links proposal names in meeting summaries to newly created pages (idempotent). **Always run this after creating a new proposal page** (turns plain-text proposal names scattered across past summaries into links).
   - Abbreviations that collide with ordinary words (`API`, `JS`, etc.) are excluded via `extract_people.py`'s `NON_PERSON`. Add to it when a new false positive shows up.
5. Update the catalog row in `wiki/README.md`.
6. Append one line to `wiki/log.md`.

### Query (answering a question)

1. Dig in this order: `wiki/README.md` → the relevant proposal page → `agenda-index.md` if needed → `raw/notes`.
2. Answer with sources (meeting links) attached.
3. If the answer contains valuable analysis (a cross-cutting comparison, a new finding, an organization worth reusing, etc.), **ask the user at the end whether to keep it as a wiki page** (never add it unprompted). If they want to keep it, file it back as a synthesis page and update `wiki/README.md` / `wiki/log.md`.

### Lint (health check)

A quality check of the wiki. It covers **both of the following two aspects** (source cross-checking, previously kept separate as "Verify," is now folded into Lint).

**(a) Internal health** (looking within the wiki)

- Check for contradictions between pages, stale statements (claims overturned by a newer meeting), orphan pages, missing cross-links, and unresolved issues left dangling.
- Flag important proposals that appear in `agenda-index.md` but have no proposal page yet.
- **Bidirectional family consistency**: check that each `families/<family>.md`'s `members` matches proposals' frontmatter `families` (no member with a proposal page missing that family, and conversely that a proposal's `families` is listed in that family's `members`).

**(b) Consistency with sources** (cross-checking wiki against raw)

- Verify each proposal page's claims against the source transcripts. Check **looking to find errors**, and when found, fix the wiki treating raw as ground truth.
- Spots especially prone to error: the year/month and direction of stage transitions, champion identification, speaker attribution, quote accuracy.
- **Cross-check against `raw/proposals` (confirming current stage / champion)**: check each proposal page's frontmatter `current_stage` / `status` / `champions` against the canonical list.
  - How to find it: grep Stage 3/2.7/2 in `raw/proposals/README.md`, Stage 4 in `finished-proposals.md`, Stage 1 in `stage-1-proposals.md`, withdrawn/inactive in `inactive-proposals.md` (`grep -i '<proposal name>' raw/proposals/*.md`). Which table it appears in indicates the current stage.
  - On a disagreement, follow precedence (the Layers section above): treat proposals as primary for current stage/champion and fix the wiki, then **corroborate the history of the transition against notes**. A proposal not listed in proposals (e.g. an old withdrawn one) may be judged from notes alone.
  - **Champion consistency policy**: frontmatter `champions` must **cover** the canonical current champions (add any missing). However, **keep a historical champion not in canonical (e.g. an original champion who has since left) rather than deleting them** (canonical is a current snapshot and doesn't carry past champions). Don't treat "not in canonical" as "wrong."
  - Note: since the proposals list is a current snapshot, **it cannot verify past transitions themselves**. Continue to confirm intermediate stages in the history table against notes.

After material updates (post submodule-pull), regenerate with `python3 tools/extract_agenda.py`, `python3 tools/extract_proposals.py`, then `python3 tools/extract_people.py && python3 tools/link_people.py && python3 tools/link_proposals.py`.

### Update (syncing raw sources)

The operation of pulling the submodules under `raw/` (`raw/notes` = tc39/notes, `raw/proposals` = tc39/proposals) to latest and showing **the diff since the last sync**. The state of the last sync is recorded by the submodule pointers already committed in the superproject. Used to see whether new meetings/proposals have come in, and as the starting point for ingest / summarise.

1. Note the pointers before syncing (= the state as of the last pull): `git submodule status` (call each submodule's current SHA OLD).
2. Pull each submodule to latest:
   - Normally (tracking main): `git -C raw/<sub> checkout main && git -C raw/<sub> pull --ff-only` (or `git submodule update --remote` for all at once).
   - If `raw/notes` is sitting on an unmerged PR branch (e.g. `pr-411`): if that PR has been merged to main, switch back to tracking main then pull; if not yet merged, fetch and update the PR (see the Summarise section for PR handling details).
3. **Show the diff**: for each submodule, `git -C raw/<sub> log --oneline OLD..HEAD` and `git -C raw/<sub> diff --stat OLD..HEAD`. Pull out and summarize especially **added meeting files (`meetings/<YYYY-MM>/`) and proposal status changes**. If there's no diff, say "up to date (no changes)" and skip the commit that follows.
4. If a pointer moved, commit in the superproject (`[update]`). Then regenerate the generated files: `python3 tools/extract_agenda.py` (from notes), **`python3 tools/extract_proposals.py` (from proposals — always refreshes the all-proposals stage list `wiki/proposals/index.md`)**, `python3 tools/extract_people.py && python3 tools/link_people.py && python3 tools/link_proposals.py`. Always re-run `extract_proposals.py` if `raw/proposals` moved.
5. Record one line in `wiki/log.md` (what range was synced, whether there were new meetings or proposal status changes).

### Summarise (daily meeting summaries)

Summarize an entire meeting topic-by-topic in English (distinct from proposal-centric Ingest). Output goes to `wiki/meetings/<YYYY-MM>/`. The target is specified as either **a meeting (YYYY-MM)** or **an unmerged tc39/notes PR (number or URL)**. If a PR is given, check out `pr-<PR>` first following "Summarising a meeting that exists only on an unmerged PR" below, then target the meeting(s) that PR adds. If unspecified, use the **latest meeting** under `raw/notes/meetings/`.

1. Read each day's file for the target meeting, `raw/notes/meetings/<YYYY-MM>/<month-DD>.md`.
2. Generate **one file per day**, `wiki/meetings/<YYYY-MM>/<YYYY-MM-DD>.md`. For each day's agenda item (`## <topic>`):
   - The heading is the topic's original name (kept in English, as `##`).
   - Place the opening meta bullet list in **wiki → proposal → slide order** (omit any that don't apply; labels are all lowercase):
     - `- wiki: [Title](../../proposals/<slug>.md)` — the **existing proposal page** this topic is discussing. **Always first**. `tools/link_proposals.py` auto-fills and moves this to the front when the heading contains a proposal name, but add it by hand for a topic whose heading doesn't name a proposal (e.g. a needs-consensus PR).
     - `- proposal: [name](URL)` — a link to the original proposal repo (`* [proposal](URL)`).
     - `- slide: [link](URL)` — the presenter's slide link (`* [slides](URL)`).
   - Follow with a **3-5 line** summary in English (follows the wiki's shared language convention). Person abbreviations and existing proposal names in the body **may be written as plain text** (the scripts in step 4 turn them into links).
   - If there's a `### Conclusion` / `### Speaker's Summary of Key Points`, **always include that conclusion in the summary** (stage transition, whether consensus was reached, etc).
   - Committee boilerplate with little actual discussion (Opening & Welcome, Secretary's Report, various status updates, etc) may be omitted.
3. Generate `wiki/meetings/<YYYY-MM>/README.md`:
   - **Always link to the matching page in the tc39/agendas repo** (`https://github.com/tc39/agendas/blob/main/<YYYY>/<MM>.md`).
   - Summarize the **overview** drawn from it, the meeting name (e.g. 113th TC39 Meeting), location, host, attendees, etc (the meeting name/attendees can also be filled in from each day's leading attendees table in raw, and the location from the Opening description).
   - Include a list of links to each day's file.
4. **Generate links** (always run this once the summary is written):
   - `python3 tools/extract_people.py` — a person page's "Meetings attended" toggles whether a meeting is linked based on whether a summary exists (`wiki/meetings/<YYYY-MM>/README.md`), so if you summarize a new meeting and don't regenerate this, existing person pages are left with that meeting as plain text.
   - `python3 tools/link_people.py` — links person abbreviations in the summary body to `[ABBR](../../people/ABBR.md)` (idempotent. Only abbreviations that have a page. An ambiguous abbreviation like JSC is not auto-linked — link it by hand only where it refers to the person).
   - `python3 tools/link_proposals.py` — links proposal names in the summary body to `[Title](../../proposals/<slug>.md)`, and ensures the topic-opening meta bullet list (`- wiki:` first, in wiki → proposal → slide order) (idempotent. Only proposals that have a page. Add wording variants to the script's `ALIASES`).
5. Once done, commit with `[summarise]` and record it in `wiki/log.md`.

**Syncing notes (the submodule) with the wiki**: whenever you pull `raw/notes` or check out a PR, **always commit the submodule pointer change** (`[wiki]`). This keeps a permanent record of which state of notes the wiki summarized/referenced, and keeps the two in sync (don't leave the pointer uncommitted).

- When summarising a meeting that exists only on an unmerged PR:
- `cd raw/notes && git fetch origin pull/<PR>/head:pr-<PR> && git checkout pr-<PR>` to check it out → **commit the pointer** (`[wiki]`) → generate the summary and commit with `[summarise]`.
- Routine sync afterward (checking for updates, showing the diff, returning to tracking main once the PR is merged) is done via **/update** ("Update (syncing raw sources)"). A pointer commit that moves during that sync operation is `[update]` (a pointer that moves from a temporary checkout during Summarise is `[wiki]`, as above).
- Note: a PR head commit can be unreachable via a plain `git submodule update` if it comes from a fork (full reproducibility from a separate clone is only guaranteed once merged).

## Person pages (people/)

`wiki/people/<ABBR>.md` is **generated**. Built for abbreviations appearing on proposal and family pages, gathering "Full name / Affiliation / Champion drafts / Mentioned on proposal pages / Mentioned on family pages / Meetings attended". The filename is the abbreviation, so `[ABBR](../people/ABBR.md)` resolves directly (`../people/` from proposals/family, `../../people/` from a meeting summary; `link_people.py` computes this automatically from the file's location). Re-running `extract_people.py` picks up new people automatically as more proposal/family pages are added.

- `link_people.py` links within proposal, family, and **meeting-summary** pages (`wiki/meetings/<YYYY-MM>/`). It only links abbreviations that have a page, so a person who appears only in meetings stays as plain text (no dead links).
- **Ambiguous abbreviations are not auto-linked**: `JSC` mostly refers to the engine (JavaScriptCore), so it's excluded via `link_people.py`'s `AMBIGUOUS`. Link only the occurrences that refer to the person (J. S. Choi) by hand. Add any similar collision to `AMBIGUOUS`.

- The policy is to cover only **people who actually appear**, not all 578+ delegates.
- Full name/affiliation/meetings attended come from `raw/notes` (delegates.txt and each meeting's attendee table). Early meetings' attendee tables have no abbreviation column, so some people end up with `Meetings attended: 0` (full name is still filled in from delegates.txt). This is a limitation of the extraction, not an error.
- Don't hand-edit (regeneration overwrites it). To add something, change the script instead.

## Stage list of all proposals (proposals/index.md)

`wiki/proposals/index.md` is **generated by `extract_proposals.py` from raw/proposals (canonical)**, a stage-by-stage catalog of all proposals (ECMA-262 / ECMA-402). Don't hand-edit. Deep-read proposals link to their page. Regenerated every time Update pulls `raw/proposals`.

- **Stage 4 lists only proposals not yet in ECMAScript** (shipped finished proposals are omitted). Judged by whether the finished table's **Expected Publication Year is the current year (by `datetime`) or later** (i.e. not in the latest ratified edition). Stage 3 and below are listed in full.
- Background (the ES-edition rule): a proposal that is **at Stage 4 and merged into the spec by the end-of-March freeze** goes into that year's ES edition, **announced at the end-of-June Ecma GA** (e.g. ES2026 = ECMA-262 17th / ECMA-402 13th, GA 2026-06-30). So a proposal's **Expected Publication Year is the definitive signal of which ES edition it's in / whether it has shipped**, and is more accurate than the Stage 4 date (a large proposal can reach Stage 4 but miss the freeze on merging, pushing it to the following year's edition — e.g. Temporal reached Stage 4 in 2026-03 but wasn't fully merged, so it goes into ES2027).

## Using the backbone (important)

All 86 meetings and 2737 agenda items are machine-extracted into `wiki/_generated/agenda-index.md`. This is not a substitute for deep reading — it's an **index**. When writing/tracing a proposal page, grep this first to grasp which meetings discussed it, then read that meeting's original text to fill in the issues. Proposal names shift by year (renames, aliases), so also try alternate names when grepping.

## TC39 stages (reference)

- **Stage 0** Strawperson / **Stage 1** Proposal (discussion begins) / **Stage 2** Draft (API shape agreed) / **Stage 2.7** (introduced 2023) waiting on tests and spec review completion / **Stage 3** Candidate (awaiting implementation) / **Stage 4** Finished (merged into the spec body, shipped).
- Stage 2.7 was introduced around 2023-11. Proposals before that transition directly from 2 to 3.

## Scope note

The material spans 334 files, 2012-2026. Full deep-reading happens incrementally. Proposals deep-read so far are listed in `wiki/README.md`'s "Ingested proposals" section; those not yet deep-read (backbone only) are referenced via agenda-index.
