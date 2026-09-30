# Log

Chronological append-only record of ingest / query / lint operations. Each line starts with `## [YYYY-MM-DD] <type> | <content>`. You can check the latest entries with `grep "^## \[" wiki/log.md | tail -5`.

## [2026-06-25] setup | Initial wiki bootstrap

- Established the operating rules in [AGENTS.md](../AGENTS.md) (layers, proposal page format, language rules, workflow).
- Created `tools/extract_agenda.py` and generated the backbone [\_generated/agenda-index.md](_generated/agenda-index.md) for all 86 meetings / 2737 agenda items.
- Deep-read and turned three representative proposals into pages:
  - [Temporal](proposals/temporal.md) — shipped (Stage 4 / 2026-03). A large proposal that ultimately reached shipping.
  - [Decorators](proposals/decorators.md) — stage3 (Stage 3 / 2022-03). A difficult proposal redesigned three times.
  - [Records & Tuples](proposals/records-and-tuples.md) — withdrawn (2025-04). A proposal withdrawn after stalling.
- Created [README.md](README.md).

## [2026-06-25] update | People pages, quote translation, and stage-history graphs

- Standardized quoted dialogue on proposal pages to English. Added translation rules to the language policy in AGENTS.md.
- Added `tools/extract_people.py` and `tools/link_people.py`. Generated person pages for the 43 people appearing on proposal pages under [people/](people/) and linked inline abbreviations as `[[ABBR]]`. The ambiguous abbreviations `API` and `JS` were excluded via a denylist.
- Added a mermaid `xychart-beta` stage-history graph below Temporal's stage-transition table (x-axis = full 2012-2026 span, y-axis = Stage, line stacked from the bottom). It rendered blank in bierner.markdown-mermaid, but did render in another mermaid extension. Codified `xychart-beta` in AGENTS.md (title should preferably be ASCII).

## [2026-06-25] update | Expanded the graph to all proposals and converted links to markdown

- Added the stage-history graph to [Decorators](proposals/decorators.md) (flat at Stage 2 through 2016-2021, then Stage 3 in 2022) and [Records & Tuples](proposals/records-and-tuples.md) (line stops at the 2025-04 withdrawal).
- Because **VS Code's markdown preview cannot navigate Obsidian `[[wikilink]]` links**, all wiki links were converted to standard markdown relative links. `link_people.py` links person abbreviations as `[ABBR](../people/ABBR.md)` (and automatically migrates existing `[[ABBR]]` links), and `extract_people.py` now emits proposal links on person pages as `[Title](../proposals/slug.md)`. Uncreated proposals stay plain text instead of dead links. AGENTS.md's link conventions were updated.

## [2026-06-25] lint | Fact-checking and correcting three deep-read pages

Cross-checked the claims on each proposal page against the source transcripts and fixed the errors found:

- **Temporal**: (1) The quote about "V8 ... this scope reduction" was a SYG prepared statement, not JGT's, so the speaker was clarified. (2) The IDL/JSIDL section was not part of the Temporal discussion; it belonged to the separate agenda item "IDL for JavaScript" in the same meeting, so that was corrected. (3) 2025-04 was a planned shipping date, not "shipped in Firefox 139".
- **Decorators**: (1) AWB's note about the `@` syntax collision was in 2015-01, not 2014-01. (2) The resistance to the 2016-09 sigil swap had been misattributed to EFT/AWB; EFT only raised a question, and AWB's argument pointed in the opposite direction. (3) The `toString` argument for export ordering was originally made by **MM**; the WH quote was from 2018-05 and was conditional. (4) Updated 2021-07 from "reviewer appointment" to "reviewer call".
- **Records & Tuples**: Corrected a **person mix-up** in the champion attribution. `RRI` (Reefath Rajali in delegates.txt) had been confused with Robin Ricard. On this wiki Robin Ricard is normalized to `RRD` (a local attendee table in 2019-10 reused the same abbreviation for a different delegate, which caused the confusion). Regenerated the frontmatter, body, and people pages, and removed the incorrect person page RRI.md (42 people total).

The stage-transition skeleton and most speaker attributions matched the transcripts; there were no fatal factual errors.

## [2026-06-25] update | Reflected the operating agreements in AGENTS.md and added the Update command

- Documented the wiki operating agreements reached in this session in AGENTS.md:
  - Stage-history graphs should use **xychart-beta line charts** (fixed 2012-2026 x-axis, stacked from the bottom); **withdrawn proposals stop the line at the withdrawal year**, and stalls remain flat.
  - **Champions must not be decided from delegates.txt alone; they must be verified against the Presenter line in the relevant meeting** (abbreviations can be reassigned per meeting. Lesson from RRI/RRD). Speaker attribution and dates should also be checked against the original text.
  - (Already reflected) quotes should be translated into English; links should use standard markdown relative links; person pages should be generated only for people who actually appear.
- Added **Update** to the workflow: an operation that reflects agreed wiki behavior changes into AGENTS.md and records them in the log. The criterion is whether the change is an operational rule other agents need.

## [2026-06-25] update | Expanded the definition of Lint (integrating Verify)

- Expanded Lint so it now includes both (a) internal health checks (inconsistencies, orphaned pages, staleness, and coverage) and (b) consistency with sources (cross-checking wiki against raw, formerly Verify). There is no separate Verify operation anymore; it was folded into Lint.

## [2026-06-25] update | Added the file-back confirmation step to Query

- Added an explicit Query step: if the answer contains valuable analysis, ask the user at the end whether it should be kept as a wiki page instead of adding it unprompted. If it should be kept, file it back as a synthesis page and update the index/log.

## [2026-06-25] update | Turned Ingest/Lint into slash commands

- Added `.claude/commands/ingest.md` and `lint.md` so `/ingest <proposal>` and `/lint [target]` can be used to invoke them. Each is a thin wrapper that points to the corresponding AGENTS.md workflow. The workflow introduction in AGENTS.md also mentions them.

## [2026-06-25] update | Turned all workflows into commands and centralized the definitions in AGENTS.md

- Added `/query` and `/update`, so all four operations (ingest/query/lint/update) now have slash commands.
- Removed the duplicated workflow text from the existing ingest/lint commands and **consolidated all commands into pointers that simply say "read the relevant AGENTS.md section and execute it"**. AGENTS.md is now the single source of truth.

## [2026-06-25] update | Added the commit convention

- Added a shared workflow rule to AGENTS.md: after each operation, commit with a message prefix matching the operation (`[ingest]`, `[query]`, `[lint]`, `[update]`). The definition lives in one place in AGENTS.md, with the commands only referring to it.

## [2026-06-25] wiki | Added the `[wiki]` commit prefix

- Added a convention that wiki-wide changes not caused by an operation (command additions/changes, changes under `tools/`, repository structure changes, AGENTS.md structure changes, etc.) should be committed with the `[wiki]` prefix.

## [2026-06-25] wiki | Added the Summarise command

- Added `/summarise` to produce daily topic-by-topic meeting summaries (output under `wiki/meetings/<YYYY-MM>/`, one file per day plus index.md). The format is defined in AGENTS.md under Workflow > Summarise. Added `[summarise]` as the commit prefix.

## [2026-06-25] update | Added the link rule from Summarise to existing proposal pages

- Added a rule to AGENTS.md's Summarise workflow: when a summary topic corresponds to an existing proposal page (`wiki/proposals/<slug>.md`), place `- proposal page: [Title](../../proposals/<slug>.md)` after Slides.

## [2026-06-25] summarise | 113th TC39 Meeting (2026-03)

- Summarized the latest meeting, 2026-03 (113th, New York), into daily files. Generated Day 1-3 plus index.md under `wiki/meetings/2026-03/`. The index links to tc39/agendas 2026/03 and summarizes the venue, dates, attendees, and overview. The Temporal topic on Day 2 links to [Temporal](proposals/temporal.md).

## [2026-06-25] wiki | Introduced the oxfmt markdown formatter

- Added `oxfmt` (Rust-based, markdown-aware) as a devDependency. Configuration lives in `.oxfmtrc.json` (`proseWrap: preserve`, `embeddedLanguageFormatting: off`, excludes `raw/**` and `wiki/_generated/**`).
- Formatted the existing wiki markdown (table alignment, blank lines after headings, etc.); mermaid, long Japanese text, and links were preserved.
- **Automatic enforcement**: editing files are formatted immediately via the PostToolUse hook (`.claude/settings.json`), and staged files are formatted and re-staged via the pre-commit hook (`.githooks/pre-commit` + `core.hooksPath`). Added a "Formatting" section to AGENTS.md.

## [2026-06-25] summarise | 114th TC39 Meeting (2026-05)

- Checked out tc39/notes pull request #411 (the 2026 May transcript) as a submodule and summarized the 114th meeting (Amsterdam, JetBrains) daily. Generated Day 1-3 plus index.md under `wiki/meetings/2026-05/`. The Temporal/Decorators topics on Day 1 link to proposal pages. The submodule pointer change was not committed because this was an unmerged PR.

## [2026-06-25] update | Documented the summarizing-of-unmerged-PRs workflow and submodule handling

- Added submodule handling to Summarise: meetings that exist only in an unmerged PR are summarized by checking out the PR in `raw/notes`, and the pointer is not committed. Submodules are updated regularly, and **once the PR merges to main, the submodule is returned to tracking main** so the pointer can be updated normally (`[wiki]`).

## [2026-06-25] update | Always commit submodule pointers (keep notes and wiki in sync)

- Changed policy: the previous rule of "do not commit pointers for unmerged PRs" was withdrawn. The rule is now to **always commit the submodule pointer after a pull / PR checkout** (`[wiki]`). This keeps a permanent record of the notes state the wiki referenced and keeps them in sync. Replaced the relevant AGENTS.md section.

## [2026-06-25] lint | Health check for the whole wiki (including Decorators downgrading)

Cross-checked internal health and the source material for 2026-05 (PR #411). Findings and fixes:

- **Decorators became stale**: In 2026-05 (114th), it was **downgraded from Stage 3 to Stage 2.7** (Decorator Metadata moved in lockstep), but the proposal page had stopped at 2023-05 ([verified in tc39/notes may-19.md:1194](https://github.com/tc39/notes/blob/main/meetings/2026-05/may-19.md#L1194)). Updated frontmatter (`status: stage2.7` / `current_stage: 2.7`), the stage-transition table (added the 2026-05 row), the mermaid graph (set 2026 to 2.7), the overview, the `### Stage 2.7 downgrade` issue, the sources, and the index.md row.
- **AGENTS.md**: Added `stage2.7` to the `status` enum (the downgrade could not be expressed before, and we agreed to reflect it in this lint pass). Updated the index legend as well.
- **Two factual errors in the 2026-05 index summary**: (1) Dynamic Code Brand Checks had been incorrectly described as reaching Stage 4, when in fact there was only consensus on a normative change and it was re-requested later. (2) Decorators' 2.7 move had been described as an advancement; corrected to a downgrade (regress).
- **Person count**: index.md said "43 people"; at the start of lint it was inconsistent with 42 pages, but once DLM appeared on the Decorators page and the pages were regenerated it became 43, so it is now consistent (extract_people/link_people already ran).
- Internal links, person abbreviations (43), and meeting-to-proposal links were all resolved. Temporal's Stage 4 (2026-03) matches the source.

-## [2026-06-26] query | Where Intl.MessageFormat sits within Unicode

- Answered that MF2 has a three-layer vertical stack: the core (syntax DSL and data model) belongs to Unicode, the reference implementation is ICU (ICU4C/4J, tech preview as of 2024-04), and only the JS API belongs to TC39. Also explained that TG2 effectively outsourced MF2 evaluation to Unicode / the broader industry (source: [2024-04 april-10](https://github.com/tc39/notes/blob/main/meetings/2024-04/april-10.md)). For the earlier question about whether Intl.MessageFormat overlaps with Template Instantiation, clarified that Template Instantiation is a W3C/WHATWG HTML proposal outside TC39's scope and serves a different purpose.
- file back: added `### Division of labor with Unicode — syntax at Unicode, API at TC39` under `## Main issues` in [intl-messageformat.md](proposals/intl-messageformat.md). Also added `### A different thing that is easy to confuse — Template Instantiation / DOM Parts (reference, outside TC39 scope)` under `## Related proposals` (a DOM-side WICG proposal from W3C/WHATWG; DOM Parts is the lower-level marking/update mechanism, and Template Instantiation is the declarative template API layered on top. This was added as a reference note based on external material, not on wiki source material).

## [2026-06-25] query | Who actually wants Decorators?

- Answered that the demand/implementation mismatch is the core reason for the stagnation and the 2026-05 downgrade: users (framework authors, the TypeScript/Babel ecosystem, and app developers) strongly want the feature, while implementers (engine teams in V8/SpiderMonkey/JSC) do not want to ship it. Sources: [2019-03](https://github.com/tc39/notes/blob/main/meetings/2019-03/mar-27.md), [2021-07](https://github.com/tc39/notes/blob/main/meetings/2021-07/july-14.md), [2023-01](https://github.com/tc39/notes/blob/main/meetings/2023-01/feb-01.md), and [2026-05 may-19](https://github.com/tc39/notes/blob/main/meetings/2026-05/may-19.md).
- file back: added `### Demand vs. implementation mismatch (who wants it?)` under `## Main issues` in [decorators.md](proposals/decorators.md).
- Side effect: [OFR](people/OFR.md) appeared for the first time in the body text, generating a person page (44 people). The abbreviation "TS" (meaning TypeScript) collided with the delegate abbreviation TS, so `extract_people.py`'s `NON_PERSON` list was updated with `TS`, the bad page was removed, and the body text was changed to `TypeScript`.

## [2026-06-25] ingest | Proposals that reached Stage 4 in 2026

- Narrowed the target to "proposals that reached Stage 4 in 2026 (113th 2026-03 / 114th 2026-05, and 111th 2026-01)." There were six such proposals (Temporal was omitted because it already had an existing page, so five new pages were ingested). Since each proposal has a multi-year history, five parallel subagent runs investigated the history across agenda-index and raw, and the main agent verified and wrote the pages.
  - [Upsert](proposals/upsert.md) (`Map.prototype.getOrInsert`, ECMA-262, Stage 4 in 2026-01)
  - [Intl Era/Month Code](proposals/intl-era-month-code.md) (ECMA-402, Stage 4 in 2026-03, alongside Temporal)
  - [Joint Iteration](proposals/joint-iteration.md) (`Iterator.zip`, ECMA-262, Stage 4 in 2026-05)
  - [Atomics.pause](proposals/atomics-pause.md) (ECMA-262, Stage 4 in 2026-05, including a normative change that removed the argument)
  - [Explicit Resource Management](proposals/explicit-resource-management.md) (`using`, ECMA-262, Stage 4 in 2026-05; conditional Stage 4 in 2025-05)
- Prepared frontmatter, stage-transition tables, mermaid graphs, main issues, and sources for each page. Quoted speech was translated into English.
- Ran `extract_people.py` / `link_people.py` and expanded the people pages from 44 to 52 (new: BAN/BFS/EAO/EPR/FYT/KM/LCA/RPR). No false positives.
- Added five rows to the catalog in [README.md](README.md), removed `intl-era-month-code` from the uncreated list, and updated the person count to 52. Linked Temporal's related proposal to the Intl Era/Month Code page.

## [2026-06-25] update | Added the family layer for cross-cutting summaries

- Introduced **family pages** (`wiki/families/<family>.md`) to group proposals that belong to the same category. Individual histories stay in `proposals/`, while families focus on cross-cutting summaries (member list + shared themes) to avoid duplicate maintenance. AGENTS.md was updated with the directory structure, family page format, and lint checks for bidirectional family consistency.
- **Membership is bidirectional**: proposal frontmatter carries `families: [...]`, and the family page carries `members: [...]`; lint detects mismatches. Uncreated proposals are listed only on the family's `members` side as slugs.
- Extended `extract_people.py` / `link_people.py` to scan `wiki/families/` as well, so person links in family pages resolve and generate correctly. Added a "mentioned on family pages" line to person pages. This generated [GCL](people/GCL.md), bringing the total to 53 people.
- Created the first family, [Iterator helpers and friends](families/iterator.md), using [MF](people/MF.md)'s 2026-05 roadmap as the outline, and listing 11 proposals with their stages (helpers/concat/zip/chunking/includes/async, etc.). Added `families: [iterator]` to [joint-iteration](proposals/joint-iteration.md). Added a families section to index.md.

## [2026-06-25] ingest | Created the modules (module harmony) family

- Grouped the "module harmony" proposals (ES Modules and related proposals) into the [Modules](families/modules.md) family. After a cross-cutting subagent review of agenda-index and raw, listed 16 proposals with current stages: ES Modules / dynamic import / import.meta / top-level await / import attributes / JSON modules / export-from (Stage 4), source phase imports / import defer / import text (Stage 3), ESM phase imports (2.7), export defer (2, with a 2.7 proposal in progress), and export all from / module scope ceiling / module declarations / compartments (Stage 1 to stalled). Organized the shared themes: import phase, evaluation delay, host integration, and the `assert` → `with` rename.
- The individual proposal pages do not yet exist, so the members are written as code-formatted slugs. Generated the new person [GB](people/GB.md) (Guy Bedford), bringing the total to 54. Because `vm` (the Node module) was misdetected as the delegate abbreviation `VM`, `extract_people.py`'s `NON_PERSON` list was updated with `VM`, the bad page was removed, and the body text was corrected to code formatting (the same fix as for TS).
- Added modules to the families section of index.md.

## [2026-06-25] update | Added raw/proposals and defined precedence

- Added `raw/proposals` (tc39/proposals) as a submodule. Imported the canonical current-stage tables and champions lists into raw.
- Revised the layers section of AGENTS.md to a two-source model and made the precedence explicit: history, issues, and speaker attribution come primarily from `raw/notes`, while current `current_stage` / `status` and champion values come primarily from `raw/proposals`. Also noted that proposals are snapshots and do not carry history.
- Updated the directory-structure listing with the key files in `raw/proposals/`.
- Added proposal cross-checking steps to Lint(b): grep-compare frontmatter `current_stage` / `status` / `champions` against README / finished / stage-1 / inactive, and resolve disagreements according to precedence (current stage comes from proposals; history is verified in notes).

## [2026-06-25] ingest | Intl.MessageFormat (Stage 1, stuck)

- Created the new proposal page `wiki/proposals/intl-messageformat.md`. This is the ECMA-402 proposal to expose MessageFormat 2.0 (MF2) in JS.
- Stage history: reached Stage 1 in 2022-03 and then remained stuck at Stage 1 through 2026. In 2024-02 there was a proposal to remove the parser and move to Stage 2 with only the data model; in 2024-04 the proposal stalled because TG2 (Google i18n) opposed it. Main issues include whether to standardize a DSL/parser with little prior art, error handling (non-throwing model / options 1-6), confusion around the word `message`, and splitting into `Intl.MessageResource` (2022-11).
- Following the canonical `raw/proposals/ecma402/README.md` Stage 1 section, the champion list was set to EAO only (DLM's co-champion involvement is retained in the body as history).
- Ran `extract_people.py` / `link_people.py` and added the page to index.md.

## [2026-06-26] wiki | Redefined /update as the raw-source sync command

- Changed the role of `/update`: the old meaning of "reflect agreed wiki operations into AGENTS.md" was removed, and it was replaced with a sync command that **pulls the submodules under `raw/` (notes / proposals) to the latest state and shows the diff since the previous sync (the committed pointer)**.
- Rewrote AGENTS.md's `### Update` section completely (steps: record old pointers → pull → show `OLD..HEAD` diff → commit pointers with `[update]` + regenerate outputs → record in the log). Delegated the future handling of Summarise to /update and clarified that routine sync pointer commits are `[update]` (temporary checkouts remain `[wiki]`).
- Updated `.claude/commands/update.md` and the workflow argument hints.

## [2026-06-26] lint | Cross-checking stage/champion against raw/proposals and filling in missing links

Checked the entire wiki according to the new precedence (`raw/proposals` is the primary source for current stage / champion).

- **All 9 proposal pages matched the canonical current stage/status** (Decorators = Stage 2.7 confirmed in the canonical 2.7 section, Records & Tuples = inactive, Stage 4 proposals = finished, Intl.MessageFormat = Stage 1). The separate-session ingest of [intl-messageformat](proposals/intl-messageformat.md) was also healthy, matching the canonical champion `EAO` and Stage 1.
- **Fixed family stage errors** (canonical cross-check): corrected iterator's `iterator-join` from `1~2` to **3**, and modules' `module-declarations` from `1 (stalled)` to **2**; also separated the Stage 2 proposal `module-expressions` and added it to the members list.
- **Filled in missing cross-links** (carried over from the previous lint): added `- proposal page:` to five summary topics from 2026-03 / 2026-05 (ERM x2, Intl Era/Month, Joint Iteration, Atomics.pause).
- **Champion consistency** (policy: keep historical champions and only add missing canonical ones): added the canonical four champions to [Temporal](proposals/temporal.md) — [PDL](people/PDL.md) (Philipp Dunkel), [MAJ](people/MAJ.md) (Matt Johnson-Pint), [BT](people/BT.md) (Brian Terlson), and [JWS](people/JWS.md) (Jason Williams) — for a total of 9 champions. No additions were needed for Decorators / Upsert / Intl Era- Month because their canonical champions were already present (historical champions like YK/EPR remain).
- Side effect: person-page regeneration created PDL and MAJ (57→59 people). index.md's person count had been stale at 54 (a missed update during the intl-messageformat ingest) and was corrected to 59.
- Formatting, dead links, and family bidirectional consistency were all clean.

## [2026-06-26] wiki | Generated the all-proposals stage list in proposals/index.md

- Added `tools/extract_proposals.py`. It extracts all proposals from `raw/proposals/` (canonical structure: README = Stage 3/2.7/2, finished = 4, stage-1, stage-0, inactive, plus the same structure under ecma402/) and generates a complete stage-by-stage list in [proposals/index.md](proposals/index.md) (ECMA-262: 286 items / ECMA-402: 34 items). The 9 deep-read pages are linked by title match (aliases are handled by the generator's ALIASES map).
- **Always keep generated output current**: added `extract_proposals.py` to the update regeneration chain in step 4 when pulling `raw/proposals`, and documented in AGENTS.md that if `raw/proposals` moves, regeneration is mandatory. Updated the generated-layer definition, directory structure, lint regeneration steps, and the wiki/index.md navigation path as well.
- Added `wiki/proposals/index.md` to `.oxfmtrc.json`'s ignore list to avoid churn (the generator is the authoritative output).

## [2026-06-26] wiki | Aligned the Update redefinition (rule reflections are centralized under [wiki])

- Another process had already redefined `### Update` from "reflect operating policy" to "sync raw sources" (recorded while landing commit ba4c278). Confirmed the new definition was already aligned across AGENTS.md, the `/update` command, and the workflow list.
- Clarified the previously missing destination for "reflect rule agreements into AGENTS.md": in the commit convention's `[wiki]` line, added that reflections of AGENTS.md rules also use `[wiki]`, that there is no dedicated operation or command for them, and that `/update` is reserved for raw sync only.

## [2026-06-26] wiki | Restricted proposals/index.md Stage 4 to not-yet-shipped items

- Limited the Stage 4 section to items that are "not yet in ECMAScript = Expected Publication Year is this year or later" (omitting finished items that already shipped). `extract_proposals.py` reads the publication year from the finished table and filters with `>= this year`. Stage 3 and below remain complete.
- Result: Stage 4 now contains 11 ECMA-262 items and 2 ECMA-402 items (out of 77 / 18 finished items total). The current-year check advances automatically via datetime.
- Note: the exact "reached Stage 4 this year" determination uses publication year (ES edition) as a proxy because canonical has no stage-4 date column. For pub year 2026, this includes items that finished at the end of 2025 and entered ES2026.

## [2026-06-26] wiki | Reflected the session agreements into AGENTS.md

- Aligned the description of `proposals/index.md` with reality: "complete stage list" became "Stage 4 only includes not-yet-shipped items." Added a new section, "All proposal stages (proposals/index.md)", and documented the Stage 4 filter (Expected Publication Year ≥ current year) and the ES edition rule (end-of-March freeze + June GA; publication year is the decisive signal for which ES edition it belongs to).
- Added the champion-consistency policy to Lint: canonical current champions must be covered (add missing ones), but historical champions not present in canonical should not be deleted (not being in canonical does not imply error).

## [2026-06-26] ingest | Deep-read Amount (formerly Measure)

- Created the proposal page [amount.md](proposals/amount.md) for `Amount` (formerly `proposal-measure`). It is an immutable value type for number + unit (`value` / `unit` / `convertTo()` / `toLocaleString()`). ECMA-262, champion [BAN](people/BAN.md), current Stage 2 (verified in canonical, reviewers WH/JHD).
- Verified the stage transitions in notes: in 2024-10 it was introduced as "Measure" and approved for **Stage 1** (agenda-index says "stage 0", but the conclusion was Stage 1 approval, so notes were taken as authoritative), renamed to Amount in 2025-07, and did not reach Stage 2 until 2026-05 (not in 2025-07/09). Main issues: whether to merge with Decimal, i18n use cases vs general-purpose use, conversion math precision (WH's concern), and no-unit / serialization behavior.
- Added Amount to the deep-read catalog in index.md. Regenerated extract_people / link_people / extract_proposals (people count 60, and the generated index now links to amount.md).

## [2026-06-26] wiki | Restored the stage graphs to line charts (xychart-beta)

- Reverted the gantt migration (1ff1489) and restored all 10 proposal pages' stage-history graphs to `xychart-beta` line charts. Also reverted the AGENTS.md graph rule back to line charts.
- Note: asking for tick marks at every 1 is **not possible in xychart-beta** (confirmed in the mermaid docs. The y-axis is numeric-only, with no tick interval/count/custom-value option; in the 0-4 range it auto-renders at 0.5 increments. The only configurable option is show/hide). The only non-integer is 2.7, and it plots correctly between 2 and 3. If the 0.5 grid is distracting, the only option is to hide the y-axis labels.

## [2026-06-26] lint | Whole-wiki check after adding Amount and round-tripping gantt

- **Internal health**: formatting was clean, all 10 proposal pages used `xychart-beta` line charts (no gantt remnants), the person count 60 matched the index, proposals/index.md had no diff after regeneration (up to date), there were no dead links, and family membership was bidirectionally consistent.
- **Source consistency**: all 11 proposal pages' `current_stage` / `status` matched raw/proposals (canonical) exactly (Amount = Stage 2, Decorators = Stage 2.7, R&T = withdrawn, etc.).
- **Fix (missing cross-link)**: filled in the link missing from the meeting topics created after amount.md. Added `- proposal page: [Amount](../../proposals/amount.md)` to the 2026-03-10 and 2026-05-20 "Amount for Stage 2" topics.

## [2026-06-27] ingest | Pulled in the 2026-05 meeting topics where stage changes were discussed

- Target: topics in the 114th meeting (2026-05) that discussed stage changes (regardless of whether the stage moved). Status-update-only items, normative PRs, and needs-consensus PRs were excluded.
- 13 new proposal pages: iterator-chunking (S3), iterator-includes (S3), iterator-join (S3), regexp-buffer-boundaries (S3), dynamic-code-brand-checks (S3 hold / normative), error-stack-accessor (S3), intl-keep-trailing-zeros (S3), stable-formatting (S2), intl-sequence-units (S2), intl-default-behaviours (S1), export-all-from (S1), comparisons (S1), and is-template-object (made inactive).
- Existing pages were unchanged because their 2026-05 rows had already been reflected: joint-iteration (S4), atomics-pause (S4), decorators (+ metadata, 3→2.7), amount (S2), and explicit-resource-management (S4 finished).
- Frontmatter stage/champion values were verified against canonical raw/proposals. Earlier history was verified in agenda-index and the individual notes (the user asked to focus on 2026-05, with deeper follow-up later).
- Family consistency: linked the chunking/includes/join rows in iterator.md and the export-all-from row in modules.md (members already matched).
- Regenerated tools: extract_people.py (64 people) and link_people.py. Added 13 rows to the index.md catalog.

## [2026-06-27] ingest | Deep-follow-up: verified and corrected the stage transitions for three proposals

- Confirmed the two items explicitly marked as "not yet sufficiently verified" in the previous ingest by checking the raw/notes `### Conclusion` sections.
- **dynamic-code-brand-checks**: It never reached Stage 2 (2019-07 "no for stage 2" / 2019-12 "NOT approved" / 2021-01 "Not advancing"). In 2024-04, NRO requested "the Stage 1 version to Stage 3," so it advanced directly from **1 → 3**. Corrected the mistaken "reached Stage 2 in 2021-01", fixed the mermaid graph so 2019-2023 stays at 1, and added supporting issues/sources.
- **is-template-object (Array.isTemplateObject)**: The conclusion in 2019-06 june-5 was "Stage 2 acceptance", so it went **directly to Stage 2 without passing through Stage 1**. Corrected the mistaken assumption of "Stage 1 → Stage 2 around 2020", fixed the mermaid graph to start at 2 in 2019, and added sources.
- **intl-keep-trailing-zeros**: In 2025-07 it moved **Stage 2 (day 1, july-29) → Stage 2.7 (day 3, july-30)** within the same meeting (WH's ToIntlMathematicalValue concern was split off as out of scope). Corrected the mistaken "directly 2 → 3", added the Stage 2.7 row, fixed the 2025 year-end mermaid value to 2.7, and added the issues.
- Regenerated extract_people / link_people. The mermaid graphs retained 15 points across the 3 pages. The index catalog stage values did not change (these were intermediate transitions only).

## [2026-06-28] lint | Whole wiki

- **Internal health**: formatting was clean; all proposal pages used xychart-beta line charts (15 points total, with records-and-tuples' 14 ending at the withdrawal year as expected); proposals/index.md had no diff after regeneration; there were no real dead links (only explanatory placeholders); and family bidirectional consistency was OK.
- **Source consistency**: the ECMA-262 new items (iterator-chunking/includes/join, regexp-buffer-boundaries, dynamic-code-brand-checks, error-stack-accessor) all matched canonical Stage 3. The champions also matched canonical (EAO/SFC, etc.).
- **Fix (bug)**: the `\Z` regexp in regexp-buffer-boundaries.md had accidentally included actual U+2028/U+2029 line-separator characters and broke the table; replaced them with ASCII text `\u2028` / `\u2029`.
- **Fix (family consistency)**: removed `families: [regexp]` from regexp-buffer-boundaries because `families/regexp.md` does not exist.
- **Fix (person count)**: updated index.md from "60 people" to "65 people" (a missed reflection of the JRL/JSH/KOT/MSL/ZTZ additions).
- **Unresolved**: Stable Formatting and Intl Sequence Units disagree between notes and canonical. The 2026-05 notes explicitly say both reached Stage 2 consensus, but canonical ecma402/README still leaves both under `### Stage 1` (with a 2026-05 note), and `### Stage 2` is empty. This is probably a lag in moving the section. The wiki keeps Stage 2 for now; after the next /update, pull raw/proposals and confirm whether the section moved to Stage 2.

## [2026-06-29] lint | Whole wiki + raw/proposals cross-check

- **Internal health**: no real broken links (the seven detected ones were placeholders such as `ABBR`, `slug`, `<slug>`, or generated agenda-index / log-history text). The recent index.md→README.md rename was healthy. Family bidirectional consistency (members ↔ proposal frontmatter families) was also fine.
- **Source consistency (raw/proposals)**: checked stage/champion for all 23 proposals against the canonical source.
  - **One fix**: changed `is-template-object` status from `inactive` to `withdrawn`. In may-19, champion JHD/CDA explicitly said "withdrawn," the canonical inactive-proposals also uses a "Withdrawn" section, and records-and-tuples is likewise withdrawn. Aligned frontmatter, stage-transition cell (2 → withdrawn), overview, issue headings, and the README catalog row.
  - **Canonical lag (wiki is correct; no fix needed)**: `intl-sequence-units` and `stable-formatting` are wiki=stage2. `ecma402/README` still says Stage 1, but the 2026-05 notes (may-20 line 290 / 475-476) confirm Stage 2 consensus. The canonical README just has not caught up to the 2026-05 ECMA-402 result yet. Do not accidentally downgrade them in the next lint.
  - Champion check: `comparisons`' `JSH` is Jacob Smith (matches canonical), and the historical champions for `temporal` / `decorators` / `intl-era-month-code` were kept as intended.

## [2026-06-30] summarise | 109th TC39 Meeting (2025-07)

- Summarized the 2025-07 meeting (109th, remote) into daily files. Generated Day 1-4 (2025-07-28 to 2025-07-31) plus index.md under `wiki/meetings/2025-07/`. Stage advancements: `Math.sumPrecise` and Uint8Array base64+hex reached Stage 4, Iterator Sequencing and Upsert reached Stage 3, Intl Era and Month Code and Intl Keep Trailing Zeros reached Stage 2.7, Import Buffer moved from Stage 1 to 2, and Module Import Hook / new Global / `Array.getNonIndexStringProperties` / `Object.getOwnPropertySymbols` options reached Stage 1. Amount (formerly Measure), `Object.propertyCount`, and `Array.isSparse` did not advance because of objections. Linked to existing proposal pages (temporal, upsert, iterator-chunking, intl-keep-trailing-zeros, amount, intl-era-month-code).

## [2026-06-30] summarise | 110th TC39 Meeting (2025-09)

- Summarized the 2025-09 meeting (110th, remote) into daily files. Generated Day 1-3 (2025-09-22 to 2025-09-24) plus index.md under `wiki/meetings/2025-09/`. Stage advancements: Iterator Chunking and Import Bytes reached Stage 2.7, Non-extensible Applies to Private reached Stage 3, and `Array.prototype.pushAll` / Native Promise Adoption / Native Promise Predicate (and immediately after, Stage 2 as well) became new Stage 1 items. Amount aimed for Stage 2, but late-breaking concerns about significant digits, naming, numeric conversion methods, etc. surfaced and after three days of continued discussion it still did not reach Stage 2 (carried forward to the next Tokyo plenary). Linked to existing proposal pages (amount, iterator-chunking, intl-era-month-code, temporal).
- **Note**: the frontmatter in `wiki/proposals/amount.md` is `status: stage2` / `current_stage: 2`, but this meeting's notes show that Amount had not yet reached Stage 2 (it was still in continuation). Next lint should cross-check against raw/proposals.

## [2026-06-30] summarise | 111th TC39 Meeting (2025-11)

- Summarized the 2025-11 meeting (111th, Tokyo, hosted by Bloomberg) into daily files. Generated Day 1-3 (2025-11-18 to 2025-11-20) plus index.md under `wiki/meetings/2025-11/`. Stage advancements: Intl Locale Info API and Iterator Sequencing reached Stage 4, Joint Iteration reached Stage 3, await dictionary jumped directly to Stage 2.7 without passing through Stage 2, Import Text is Stage 1/2 (conditionally 2.7), Intl Unit Protocol / Intl Energy Units / `Object.getNonIndexStringProperties` are new Stage 1 items, TypedArray Concatenation / Find Within are conditional Stage 1 items (waiting for a dedicated repo), and `Object.keysLength` reached Stage 2 (`Object.propertyCount` remains a separate Stage 1 item). export defer did not make Stage 2.7; Declarations in Conditionals continued through Day Three but was unresolved; Class spread syntax and Class field introspection stayed at Stage 0. Decorators stayed at Stage 2.7 due to insufficient Test262 coverage and implementation disagreement, and Intl Era Monthcode postponed the Stage 3 decision to January 2026. Linked to existing proposal pages (temporal, intl-keep-trailing-zeros, joint-iteration, error-stack-accessor, comparisons, intl-era-month-code, amount, decorators, iterator-join).
- Family consistency: linked the chunking/includes/join rows in iterator.md and the export-all-from row in modules.md (members already matched).
- Regenerated tools: ran extract_people.py (64 people) and link_people.py. Added 13 rows to the index.md catalog.

## [2026-06-27] ingest | Deep-follow-up: verified and corrected the stage transitions for three proposals

- The two items explicitly marked as "not yet sufficiently verified" in the previous ingest were confirmed by checking the raw/notes `### Conclusion` sections.
- **dynamic-code-brand-checks**: It never reached Stage 2 (2019-07 "no for stage 2" / 2019-12 "NOT approved" / 2021-01 "Not advancing"). In 2024-04, NRO requested "the Stage 1 version to Stage 3," so it advanced directly from **1 → 3**. Corrected the mistaken "2021-01 Stage 2 reached," fixed the mermaid graph so 2019-2023 stays at 1, and added supporting issues/sources.
- **is-template-object (Array.isTemplateObject)**: The conclusion in 2019-06 june-5 was "Stage 2 acceptance", so it went **directly to Stage 2 without passing through Stage 1**. Corrected the mistaken assumption of "Stage 1 → around 2020 Stage 2 (estimated)", fixed the mermaid graph to start at 2 in 2019, and added sources.
- **intl-keep-trailing-zeros**: In 2025-07 it moved **Stage 2 (day 1 july-29) → Stage 2.7 (day 3 july-30)** within the same meeting (WH's ToIntlMathematicalValue concern was split off as out of scope). Corrected the mistaken "directly 2 → 3", added the Stage 2.7 row, fixed the 2025 year-end mermaid value to 2.7, and added the issues.
- Regenerated extract_people / link_people. The mermaid graphs retained 15 points across the 3 pages. The index catalog stage values did not change (these were intermediate transitions only).

## [2026-06-28] lint | Whole wiki

- **Internal health**: formatting was clean, all proposal pages had 15 mermaid points (with records-and-tuples' 14 ending at the withdrawal year as expected), proposals/index.md had no diff after regeneration, there were no dead links (only explanatory placeholders), and family bidirectional consistency was OK.
- **Source consistency**: the new ECMA-262 items (iterator-chunking/includes/join, regexp-buffer-boundaries, dynamic-code-brand-checks, error-stack-accessor) all matched canonical Stage 3. The champions also matched canonical (EAO/SFC, etc.).
- **Fix (bug)**: the `\Z` regexp in regexp-buffer-boundaries.md had accidentally included actual U+2028/U+2029 line-separator characters and broke the table; replaced them with ASCII text `\u2028` / `\u2029`.
- **Fix (family consistency)**: removed `families: [regexp]` from regexp-buffer-boundaries because `families/regexp.md` does not exist.
- **Fix (person count)**: updated index.md from "60 people" to "65 people" (a missed reflection of the JRL/JSH/KOT/MSL/ZTZ additions).
- **Unresolved**: Stable Formatting and Intl Sequence Units disagree between notes and canonical. The 2026-05 notes explicitly say both reached Stage 2 consensus, but canonical ecma402/README still leaves both under `### Stage 1` (with a 2026-05 note), and `### Stage 2` is empty. This is probably a lag in moving the section. The wiki keeps Stage 2 for now; after the next /update, pull raw/proposals and confirm whether the section moved to Stage 2.

## [2026-06-29] lint | Whole wiki + raw/proposals cross-check

- **Internal health**: no real broken links (the seven detections were placeholders such as `ABBR`, `slug`, `<slug>`, or generated agenda-index / log-history text). The recent index.md→README.md rename was healthy. Family bidirectional consistency (members ↔ proposal frontmatter families) was also fine.
- **Source consistency (raw/proposals)**: checked stage/champion for all 23 proposals against the canonical source.
  - **One fix**: changed `is-template-object` status from `inactive` to `withdrawn`. In may-19, champion JHD/CDA explicitly said "withdrawn," the canonical inactive-proposals also uses a "Withdrawn" section, and records-and-tuples is likewise withdrawn. Aligned frontmatter, stage-transition cell (2 → withdrawn), overview, issue headings, and the README catalog row.
  - **Canonical lag (wiki is correct; no fix needed)**: `intl-sequence-units` and `stable-formatting` are wiki=stage2. `ecma402/README` still says Stage 1, but the 2026-05 notes (may-20 line 290 / 475-476) confirm Stage 2 consensus. The canonical README just has not caught up to the 2026-05 ECMA-402 result yet. Do not accidentally downgrade them in the next lint.
  - Champion check: `comparisons`' `JSH` is Jacob Smith (matches canonical), and the historical champions for `temporal` / `decorators` / `intl-era-month-code` were kept as intended.

## [2026-06-30] summarise | 109th TC39 Meeting (2025-07)

- 2025-07 (109th, remote) was summarized into daily files. `wiki/meetings/2025-07/` now contains Day 1-4 (2025-07-28 to 2025-07-31) plus index.md. Stage advancement: `Math.sumPrecise` and Uint8Array base64+hex reached Stage 4; Iterator Sequencing and Upsert reached Stage 3; Intl Era and Month Code and Intl Keep Trailing Zeros reached Stage 2.7; Import Buffer moved from Stage 1 to 2; and Module Import Hook / new Global / `Array.getNonIndexStringProperties` / `Object.getOwnPropertySymbols` options reached Stage 1. Amount (formerly Measure), `Object.propertyCount`, and `Array.isSparse` did not advance because of objections. Linked to the existing proposal pages for temporal, upsert, iterator-chunking, intl-keep-trailing-zeros, amount, and intl-era-month-code.

## [2026-06-30] summarise | 110th TC39 Meeting (2025-09)

- 2025-09 (110th, remote) was summarized into daily files. `wiki/meetings/2025-09/` now contains Day 1-3 (2025-09-22 to 2025-09-24) plus index.md. Stage advancement: Iterator Chunking and Import Bytes reached Stage 2.7; Non-extensible Applies to Private reached Stage 3; `Array.prototype.pushAll`, Native Promise Adoption, and Native Promise Predicate became new Stage 1 items; and Amount aimed for Stage 2 but did not get there after late-breaking concerns about significant digits, naming, and numeric-conversion methods surfaced over three days of continued discussion. Linked to the existing proposal pages for amount, iterator-chunking, intl-era-month-code, and temporal.
- **Note**: `wiki/proposals/amount.md` frontmatter is `status: stage2` / `current_stage: 2`, but this meeting's notes show that Amount had not reached Stage 2 yet and was still in continuation. The next lint should cross-check raw/proposals.

## [2026-06-30] summarise | 111th TC39 Meeting (2025-11)

- 2025-11 (111th, Tokyo, hosted by Bloomberg) was summarized into daily files. `wiki/meetings/2025-11/` now contains Day 1-3 (2025-11-18 to 2025-11-20) plus index.md. Stage advancement: Intl Locale Info API and Iterator Sequencing reached Stage 4; Joint Iteration reached Stage 3; await dictionary moved directly to Stage 2.7 without passing through Stage 2; Import Text is Stage 1/2 (conditionally 2.7); Intl Unit Protocol, Intl Energy Units, and `Object.getNonIndexStringProperties` are new Stage 1 items; TypedArray Concatenation and Find Within are conditional Stage 1 items pending a dedicated repository; and `Object.keysLength` reached Stage 2 while `Object.propertyCount` remains a separate Stage 1 item. export defer did not reach Stage 2.7, Declarations in Conditionals remained unresolved through Day Three, Class spread syntax and Class field introspection stayed at Stage 0, Decorators stayed at Stage 2.7 because of insufficient Test262 coverage and implementation mismatch, and Intl Era Monthcode's Stage 3 decision was pushed to January 2026. Linked to the existing proposal pages for temporal, intl-keep-trailing-zeros, joint-iteration, error-stack-accessor, comparisons, intl-era-month-code, amount, decorators, and iterator-join.

## [2026-07-02] lint | Whole wiki after importing the 2025 three-meeting summaries

- **Fix (1) policy violation**: the three summarize runs from another session (2025-07/09/11) had been generated under the old `index.md` convention → moved them to `README.md` with `git mv` (the current convention and `extract_people.py`'s link-detection logic both assume README.md). The backlinks were all self-contained source lines, so there were no broken links.
- **Fix (2) missed rerun**: `extract_people.py` had not been run after those summarizes (a violation of Summarise step 4) → reran it. Around 40 person pages now link 2025-07/09/11 in their "Meetings attended" section. Also used `link_people.py` to fill in the missing abbreviation links from the previous lint edit on is-template-object.md (JHD/CDA).
- **Fix (3) freshness of generated output**: `agenda-index.md` / `.jsonl` had not reflected the 2026-05 meeting agenda items (80+43 lines) → regenerated with `extract_agenda.py`. `extract_proposals.py` had no diff.
- **Fix (4) formatting**: two files under `wiki/meetings/2025-07/` were not formatted by oxfmt → formatted. All 123 files are clean.
- **Resolved**: the 2025-09 Summarise "note of caution" (concern about a mismatch with the amount frontmatter stage2) was not actually a contradiction in time order. The transition table includes the 2025-09 non-advancement (still 1), and `stage2` is the current value after the 2026-05 advancement, which matches canonical (Stage 2 table, champion Ben Allen).
- **Deferred**: `stable-formatting` / `intl-sequence-units` had not changed in raw/proposals since the last lint (same SHA), so they remain "canonical lag, wiki is correct (Stage 2)". Recheck after the next /update.
- **Internal health**: no real broken links (the only detections were placeholders and inline-code quotes), family bidirectional consistency is OK, all 15 mermaid points are correct (records-and-tuples' 14 ends at the withdrawal year), and the README catalog matches the 23 proposals in proposals/.

## [2026-07-03] query | Expanded the Comparisons proposal page via file-back

- Answered the question "Comparisons" using the existing page + meeting summaries + agenda-index. Per user request, filed it back.
- Expanded `proposals/comparisons.md` with the 2026-05 may-21 raw transcript: added production use cases (HTTP patch delta / React state / logging) and a two-mode API idea (`compare` fast/full, or split into `deepEqual` / `compare`) to the overview. Added new issues for "what equality means itself" (OFR), skepticism about performance benefits (KM/OFR), whether separating walk and filter reduces complexity (MM / KM / MAH), and encapsulation leakage (OFR). Merged the motivation/AI-context notes with EAO's motivation statement history and SFC's correctness argument, and added a Stage 2 concern section with MF/MAH's forewarning and SFC's Collator-model hint.
- Reran extract_people / link_people (no new abbreviations; Comparisons now appears on the pages for EAO/KM/MAH/MF/MM/OFR/SFC).

## [2026-08-13] update | Synced raw/notes and raw/proposals

- Pointers before sync: `raw/notes` ced9ef3 (pr-411) → **8b76916** (origin/main, 7 commits). `raw/proposals` 1eb7ced → **600a427** (13 commits).
- **raw/notes**: no new meeting files. Added three delegates to `delegates.txt` (roster 597→600). Made a minor speaker-name correction in the closing remarks of `meetings/2026-05/may-21.md` (outside summarization scope, no impact). The old pr-411 (the unmerged PR for the 2026-05 notes) could not be fast-forwarded (`merge-base --is-ancestor` NO), but the content had already been merged into main through PR #415 and related work (the diff is only the three may-21 lines above). The detached HEAD is expected behavior for `git submodule update --remote` (an accepted form documented in AGENTS.md).
- **raw/proposals**: the diff mainly consisted of backfilled notes links to older meetings (not stage changes). Regenerating `extract_proposals.py` changed ECMA-262 from 220→225 items and ECMA-402 from 18→20 items (new / new-stage catalog-only proposals not yet deep-read in the wiki: Await Dictionary became Stage 3, Fused Multiply-Add became Stage 2, Error code property / Map get and delete / Bigint from exponential / Linear Matching / Intl.DateTimeFormat Alignment / Intl Energy Units were newly added).
- **precedence note**: the stage-change commits above came from meetings `per 2026.07.20-22 TC39`, but raw/notes still did not contain the corresponding 2026-07 meeting yet (notes were not yet published / pulled). When handling 2026-07 in a future `/summarise` or `/ingest`, wait for raw/notes to arrive.
- **No impact on the 23 deep-read proposals**: grep cross-checks confirmed all stage/section positions were unchanged. In particular, the pending `stable-formatting` and `intl-sequence-units` were still under `### Stage 1` in `ecma402/README.md`, which remains **unresolved** (wiki keeps Stage 2 and will re-check next time).
- Regenerated outputs: `extract_agenda.py` (87 meetings / 2780 agenda items; no diff because it had already been refreshed in the previous lint), `extract_proposals.py` (as above), `extract_people.py` / `link_people.py` (one delegate spelling correction: Sathya Gunasekaran in `wiki/people/SGN.md`).
- oxfmt clean (all 123 files). Committed the submodule pointers and generated outputs together as `[update]`.

## [2026-08-13] summarise | 115th TC39 Meeting (2026-07)

- Checked out unmerged PR tc39/notes#420 (the 2026 July transcript) as `pr-420` and committed the pointer as `[wiki]` (base is main's 8b76916, so this is effectively fast-forward-equivalent).
- Summarized the 2026-07 meeting (115th, remote, 3 days) into daily files. Generated Day 1-3 (2026-07-20 to 2026-07-22) plus README.md under `wiki/meetings/2026-07/`.
- Stage advancements: **Await Dictionary reached Stage 3**, **Thenable Curtailment reached Stage 2.7** (on Day 1, host-hook work was deferred as homework, then Day 3 continuation reached consensus), **Error code property and Fused Multiply-Add (`Math.fma`) reached Stage 2**, and **bigint-from-exponential (transitioning from needs-consensus PR #3857), Map take (renamed to `getAndDelete`), Linear Matching, and `Intl.DateTimeFormat` Alignment With Other Standards reached Stage 1**. Declarations in Conditionals did not advance because pattern matching was still unresolved. All of this matched the stage changes already confirmed in raw/proposals during the previous update.
- Normative items: `Promise.try` was changed to use PromiseResolve, built-ins were forced on custom globals (#3728), the `[[CycleRoot]]` bug in Import Defer was fixed, and four ECMA-402 PRs (1086/1074/1072/1051) landed. GA approved ES2026 (ECMA-262 17th / ECMA-402 13th), and KG received the Ecma Recognition Award.
- Linked to the relevant proposal pages: joint-iteration / atomics-pause / explicit-resource-management (Editors Report), amount (BigInt exponential notation, FMA, duration units), intl-sequence-units / temporal / intl-keep-trailing-zeros (Day 3), and records-and-tuples (JSON.parseImmutable / Composites).
- Drafts for Day 2/3 were produced in parallel by subagents, and all agenda items' `### Conclusion` sections were verified against raw before being accepted.
- Regenerated outputs: `extract_agenda.py` (88 meetings / 2814 agenda items, with 34 July 2026 items added), `extract_people.py` / `link_people.py` (2026-07 links were added to the person pages' meeting lists). Updated the meeting count in wiki/README.md to 88 meetings / 340 files / 2814 agenda items.

## [2026-08-13] ingest | 8 proposals whose stage changed in the 2026-07 meeting, plus 2 existing page updates

- New proposal pages: await-dictionary (S3; 2023-03 S1 → skipped Stage 2, then 2.7 in 2025-11 → S3 in 2026-07), thenable-curtailment (S2.7; 2025-02 S1 → 2026-03 S2 → 2026-07 2.7), error-code-property (S2; advancement depends on DOMException alignment), fused-multiply-add (S2; went directly from 0 to 2 on first presentation), bigint-from-exponential (S1; transitioned from needs-consensus PR #3857), map-get-and-delete (S1; old Map take, renamed to `getAndDelete`), linear-matching (S1; ReDoS mitigation, champion group MF+AUR+CPC), and intl-datetimeformat-alignment (S1, ECMA-402).
- The stage histories were verified from each meeting's `### Conclusion` section (2023-03 mar-22 / 2025-02 feb-18 / 2025-09 sep-23 / 2025-11 nov-18 / 2026-03 mar-11 and mar-12 / 2026-05 may-19 through may-21 / 2026-07 all 3 days). Frontmatter was cross-checked against canonical raw/proposals.
- **Canonical lag (wiki is correct)**: thenable-curtailment remained in the Stage 2 section of canonical README (the 2026-07 2.7 consensus had not yet been reflected). The wiki uses Stage 2.7 based on the notes. Do not downgrade it in the next /update lint pass (same pattern as stable-formatting / intl-sequence-units).
- **Champion note**: linear-matching's frontmatter champions include canonical MF plus AUR (Aurèle Barrière) and CPC (Clément Pit-Claudel), which the 2026-07 notes explicitly named as the champion group.
- Existing page updates: amount.md (added the 2026-07 row, an issue about downstream proposals, and related proposals bigint-from-exponential / fused-multiply-add) and intl-sequence-units.md (added the 2026-07 row and an issue about whether time/duration units should be included).
- Tools: added "Curtailing the power of Thenables" → thenable-curtailment.md to the ALIASES map in `extract_proposals.py` (to handle the mismatch between the canonical name and the wiki title). Regenerating index.md linked all 8 pages. `extract_people.py` increased the people count from 65 to 75 (added AUR/AVK/CPC/DJM/DRO/JFI/JSL/LVU/MAG/SHS), and `link_people.py` linked the abbreviations on the 8 pages.
- Added 8 lines to the README catalog (deep-read proposals 23 → 31). oxfmt clean (all 145 files).
- Operational note: eight parallel subagents for page drafting all failed with API 529 (Overloaded), so I wrote the pages inline by reading the raw sections directly.

## [2026-08-14] wiki | Link conventions for meeting summaries (people/proposals) and Summarise PR support

- **Extended link_people.py**: added `wiki/meetings/<YYYY-MM>/` to the link target set (relative paths are computed automatically from file location). It only links abbreviations that have pages, so people who only appear in meetings stay as plain text (no dead links). Added an `AMBIGUOUS` exclusion list and registered `JSC` (mostly JavaScriptCore engine).
- **New link_proposals.py**: links proposal names in meeting summaries (frontmatter title plus alias spellings) to proposal pages. Also guarantees that for daily files, the **first bullet** of a topic whose `##` heading names a proposal is `- wiki:` (before Slides; existing bullets are moved to the front). Idempotent.
- **Applied to all existing meeting summaries (the 6 meetings / 25 files from 2025-07 through 2026-07)**: linked person abbreviations and proposal names, and normalized the first bullet line to `- wiki:`. Two topics whose headings do not mention a proposal (the 2026-07 BigInt needs-consensus PR / temperature checks) were added manually.
- **Corrected false links**: converted 17 person links for `JSC` that actually referred to JavaScriptCore back to plain text (14 in meetings + 3 in decorators.md; 4 links referring to person J. S. Choi were kept). The 3 decorators.md occurrences had been wrong even before this change.
- **AGENTS.md**: clarified that Summarise can target a tc39/notes PR number/URL (connected to the checkout step). Step 2 now requires the proposal-page bullet first (before Slides), and step 4 now says link generation consists of extract_people / link_people / link_proposals. Also added link_proposals.py to the regeneration steps for Ingest and Lint/Update, and documented the meetings/AMBIGUOUS policy in the person-pages section.
- **Command**: updated the argument hint in `.claude/commands/summarise.md` to "meeting (YYYY-MM) | PR number/URL".
- Synchronized wiki/README.md's person-pages section with the current state (75 people, meetings support, link_proposals).

## [2026-08-15] wiki | Normalized meeting-summary meta lines to "wiki → proposal → Slides"

- Renamed the label from `- proposal page:` to `- wiki:` and standardized the order of the meta bullet list at the start of topics to **wiki → proposal → Slides** (per user request).
- Revised `link_proposals.py`: implemented automatic migration of the old label and extraction/reordering of the three meta bullets (keeps the fixed point with oxfmt, idempotent). Applied it to all 6 meetings / 18 files and confirmed that no `proposal page:` labels remain.
- Synchronized AGENTS.md's Summarise step 2 (meta-line definition and order), step 4, and the tools list with the new convention.
- Added: the slide label should be lowercase singular `- slide:` (updated AGENTS.md and link_proposals.py accordingly; the user will do any bulk conversion of existing files).

## [2026-09-27] wiki | Split the English translation into wiki/en

- Added a rule to AGENTS.md's language policy: English translations live in `wiki/en/` at the same relative paths, rather than replacing `wiki/`.
- The translated content includes meetings 2026-07 / 2026-05 / 2026-03, the linked proposals / families, people pages, proposal index, and the English README. Links to untranslated pages still point to the Japanese version.
- 2025-11 / 2025-09 / 2025-07 and unreached proposals (`decorators` and others) are still untranslated.

## [2026-09-27] wiki | Translated 2025-11 into wiki/en

- Added `wiki/en/meetings/2025-11/`. Also translated the previously untranslated linked proposals [Decorators](en/proposals/decorators.md), [Comparisons](en/proposals/comparisons.md), and [Intl Era/Month Code](en/proposals/intl-era-month-code.md), and switched existing English-page links over to `wiki/en`.

## [2026-09-27] wiki | Translated 2025-09 into wiki/en

- Added `wiki/en/meetings/2025-09/`. The linked proposals were already present under `wiki/en/proposals/`.

## [2026-09-27] wiki | Translated 2025-07 into wiki/en

- Added `wiki/en/meetings/2025-07/`. Also translated the previously untranslated [Upsert](en/proposals/upsert.md) and switched existing English-page links over. All summarized meetings are now under `wiki/en/meetings/`.

## [2026-09-27] wiki | Translated the remaining proposals into wiki/en

- Added the previously untranslated [Intl.MessageFormat](en/proposals/intl-messageformat.md) and [Array.isTemplateObject](en/proposals/is-template-object.md) to `wiki/en/proposals/`, and switched the links from the existing English pages. All proposal pages are now covered in both languages.

## [2026-09-27] wiki | Made the English translation canonical and retired wiki/en

- `wiki/en/` reached full 1:1 coverage of the wiki (proposals, families, meetings, people, README), so per the user's request it became the canonical body text everywhere in English and `wiki/en/` was removed (the old Japanese pages remain only in git history).
- Curated pages (`proposals/*.md` except `index.md`, `families/*.md`, `meetings/**`, `README.md`) were copied from their `wiki/en/` counterparts. Generated pages (`people/*.md`, `proposals/index.md`) were not copied: `tools/extract_people.py` and `tools/extract_proposals.py` were rewritten to emit English and then rerun, because a manually copied `wiki/en/people/PFC.md` had an inconsistent relative-link depth for two meeting links; regenerating from the now-English proposal/family pages avoided reproducing that bug.
- The `wiki/en/` tree had one extra directory level relative to `wiki/`, so every link that escaped the mirrored subtree (to `raw/notes`, `AGENTS.md`, `llm-wiki.md`, `wiki/_generated/`) had one extra `../`. A link-resolution sweep across all curated pages found 366 broken links after the copy; all were corrected by stripping the extra level, and a second sweep confirmed zero broken links remain.
- AGENTS.md's language policy (`## language policy`), the fixed section headings for proposal/family pages, and the Ingest/Summarise wording were updated to say body text is English (quotes are kept in the original English rather than translated). The `en/` line was removed from the directory-structure listing.
- Historical `wiki/log.md` entries were left as an append-only record; only new entries follow the English convention going forward.

## [2026-09-28] ingest | Decimal

- New proposal page `decimal.md` (Stage 1, unchanged since reaching it in 2020-02). Read 9 meetings spanning 2017-11 through 2026-07 (nov-29 / february-4 / dec-15 / july-12 / september-27 / april-11 / october-09 / february-19 / july-22).
- Main issues: primitive-vs-object-based API (unresolved, restated as a Stage 2 blocker by JHD in 2026-07), IEEE 754 Decimal128 conformance vs. ergonomics (WH's long-running critique, mostly resolved in his direction), trailing-zero/precision tracking (resolved by scope-splitting the use case into what became Amount), and whether Decimal should exist in the language at all (folded into the primitive debate).
- Champions per canonical `raw/proposals/stage-1-proposals.md`: PFC, API, JMN. Note: API (Andrew Paprocki)'s abbreviation collides with the common term "API" and is excluded from person-page generation by `extract_people.py`'s `NON_PERSON`, so no `people/API.md` is generated; this is expected, not an error.
- Linked `amount.md`'s existing plain-text `decimal` reference to the new page.
- Ran `extract_people.py` (75 → 78 people; added CLA, LIU, SHO) then `link_people.py` / `link_proposals.py`, which also retroactively linked "Decimal" mentions in 7 meeting-summary files that referenced it before the page existed.
- Added the catalog row to `wiki/README.md` (Ingested proposals 38 → 39) and updated the people count note.

## [2026-09-30] lint | Full-wiki health check

- Cross-checked all 32 proposal pages' frontmatter against canonical `raw/proposals` (stage/status): 29 match cleanly. The 3 conflicts are all **stale upstream tables, wiki correct per notes**: thenable-curtailment (notes 2026-07-22 "Consensus for Stage 2.7" vs `raw/proposals` README still Stage 2), stable-formatting and intl-sequence-units (notes 2026-05-20 approve Stage 2 / Stage 1+2 vs `raw/proposals/ecma402` README still Stage 1). No wiki changes made; consequence is the generated `wiki/proposals/index.md` inherits the stale stages until upstream updates.
- Champion coverage: all canonical champions covered. Apparent misses were name-variant false alarms (Nicolò/Nicolo Ribaudo = NRO, James Snell = JSL, Mark S. Miller = MM, Matt/Maggie Johnson-Pint = MPT/MAJ, Daniel Minor = DLM) and a parser mis-match on the isTemplateObject inactive row (actual champions MSU/KOT/JHD/ZTZ are covered).
- Internal checks all pass: family `members` ↔ frontmatter `families` bidirectional consistency, README catalog rows ↔ pages (32/32), no orphan pages, no broken relative links (2 grep hits are intentional template text in `index.md`/`README.md`).
- Quote spot-check on the newest page (`decimal.md`): the WH 2023-07 "enormous mistake" quote is verbatim in `raw/notes/meetings/2023-07/july-12.md` (leading filler "Yeah," dropped).
- Flagged notable proposals still without pages (by agenda-index mentions): ShadowRealm (21), Pattern Matching (8), ESM Phase Imports (8), throw expressions (7), Source Phase Imports (7), Observable (6), Decorator Metadata (6), Async Iterator helpers (6), Symbol Predicates (5), Signals (5), Pipeline Operator (5).
- Fixed AGENTS.md stale counts (86 → 88 meetings, 2737 → 2814 agenda items, 334 → 340 files; README already had the correct numbers).

## [2026-09-30] ingest | 2025-11 meeting

- Deep-read the 2025-11 plenary (november-18/20) and created 10 proposal pages: `json-source-text` (Stage 4), `error-capture-stack-trace` (Stage 2), `intl-locale-info` (Stage 4), `iterator-sequencing` (Stage 4), `intl-unit-protocol` (Stage 2, 2026-03), `import-text` (Stage 3, 2026-03), `typedarray-concat` (Stage 1), `typedarray-find-within` (Stage 1), `intl-energy-units` (Stage 1), `object-get-non-index-string-properties` (Stage 1).
- Canonical-lag note: `intl-unit-protocol` is stale at Stage 1 in `raw/proposals/ecma402` (notes 2026-03 approve Stage 2); all other stages matched the canonical tables.
- Added the `iterator-sequencing` member row to `wiki/families/iterator.md`.
- Added the 10 catalog rows to `wiki/README.md`.
- Ran `extract_people.py` (78 → 86 people; added among others DRR, STY, MAH, LVU, JAD, PHE) then `link_people.py` / `link_proposals.py`, which also retroactively linked proposal names and person abbreviations in the 2025-07/09/11 and 2026-03/05/07 meeting summaries.

## [2026-09-30] ingest | 2025-09 meeting

- Deep-read the 2025-09 plenary (september-22/23/24; Day 1 verified against the raw notes) and created 5 proposal pages: `bulk-add-array-elements` (Stage 1, DRR), `native-promise-adoption` (Stage 1, MAH), `native-promise-predicate` (Stage 2, MAH), `import-bytes` (Stage 2.7; history traced back to 2025-07 where "Import Buffer" reached Stage 1 and 2 in one session), `nonextensible-applies-to-private` (Stage 3; 2025-04 cleared Stage 1/2/2.7 in one session, 2025-07 update, 2025-09 Stage 3).
- Canonical notes: Native Promise Adoption is not listed anywhere in `raw/proposals` (wiki follows the notes); Native Promise Predicate matches canonical (Stage 2, MAH, reviewers JHD/JSL/JRL).
- Updated `temporal.md` (2025-09 normative fix: DST sign-flip bug in `ZonedDateTime` difference / `Duration` round/total) and added `import-bytes` to the modules family (members + table row).
- Existing pages already carried their 2025-09 rows (iterator-chunking's 2.7 was 2025-05, not 09; await-dictionary's temperature check, amount's failed Stage 2 attempt, intl-era-month-code's normative changes were all in place).
- Added the 5 catalog rows to `wiki/README.md`; person-page generation was rerun in the 2025-11 commit (shared regeneration).

## [2026-09-30] ingest | 2025-07 meeting

- Deep-read the 2025-07 plenary (july-28/29/30/31) and created 5 proposal pages: `math-sum-precise` (Stage 4; 2023-11 Stage 1, 2024-04 Stage 2.7 as `sumPrecise` at MM's naming push, 2024-10 Stage 3), `uint8array-base64` (Stage 4; full history from 2021-07 Stage 1, incl. the 2023-09 Moddable streaming block and the 2025-07 get-validate-get-validate options precedent), `immutable-arraybuffer` (Stage 3, conditional on test262; 2024-10 Stage 1, 2024-12 Stage 2, 2025-02 Stage 2.7, 2025-04/05 test-driven holds), `module-global` (Stage 1; "Module Import Hook and new Global", continuation granted Stage 1 with a refined problem statement, 2025-09 update redesign merging Compartment ideas and owing a ShadowRealm-redundancy justification), `object-getownpropertysymbols-options` (Stage 1; not in the canonical list, wiki follows notes; KG's options-bag-vs-new-method 2x2 matrix objection and MM's four-proposals-as-one critique).
- **Fixed a wiki error** in `object-get-non-index-string-properties.md`: the 2025-07 row claimed "no advancement", but the july-31 notes granted Stage 1 at the end of the day ("So congratulations. You have stage one for this one."). 2025-11 corrected to a rename (Array→Object, options bag dropped) with Stage 1 re-affirmed though RBR had not planned to ask; added a 2025-07 shape issue section (MM on non-enumerables/ownKeys framing, array-like restriction, index definitions, proxies; GCL's key-iterator idea).
- Updated `temporal.md` (2025-07 normative PR: options-bag get/cast/validate reordering to match V8, NRO presenting for PFC) — the same discussion that flowed into the base64 Stage 4 options precedent.
- Existing pages already carried their 2025-07 rows (iterator-sequencing Stage 3, upsert Stage 3, error-capture-stack-trace update, intl-keep-trailing-zeros Stage 2/2.7, thenable-curtailment discussions, amount rename, intl-era-month-code 2.7, nonextensible update, import-bytes Stage 1+2). `array-issparse` and `object-propertycount` had no transitions (isSparse denied Stage 1; propertyCount denied Stage 2) — no pages.
- Added the 5 catalog rows to `wiki/README.md`. Ran `extract_people.py` (86 → 89 people; added JLS, OMT, RMH) then `link_people.py` / `link_proposals.py`. Two false positives caught and fixed at the source: `KB` (kilobytes) and engine `JSC` in prose were rephrased so no phantom person pages/links are generated (KB.md deleted before commit; the existing JSC page regenerates unchanged).

## [2026-09-30] ingest | 2025-05 meeting

- Deep-read the 2025-05 plenary (may-28/29/30) and created 5 proposal pages: `array-from-async` (conditional Stage 4 on editor sign-off of ecma262#3581; first proposal on the built-in async function infrastructure #2942; history from 2021-08 Stage 1, the 2022-01 double-await stall on issue #19, and the #2600 behavior-change advisory), `error-is-error` (Stage 4; first presented 2015-11 and rejected on brand-check principle, resurrected 2024-04, proxy piercing removed 2024-07, one stage per meeting thereafter), `math-clamp` (Stage 2; `Number.prototype.clamp` decided over `Math.clamp`, BigInt deferred, the +0/-0 throw resolved in the same-day continuation with JHD relenting on no-throw and NaN handling left open), `seeded-prng` (Stage 2; ChaCha12, entropy-quarantine discussion with MM's comms-channel walk-back after KG's seed caveat, renamed `Random.Seeded`; history includes the 2018-01 `Math.seededRandoms()` Stage 1 and seven-year dormancy), `more-random-functions` (Stage 1 scoped to the `Random` namespace + number/int; MF's omnibus split; KG's "how do you specify an unobservable PRNG" question).
- Updated `decimal.md` (2025-05 row; new "Decimal.Amount and the polymorphic-Amount question" issue: MM/EAO for a polymorphic Amount vs SFC's Decimal-only backing, NRO's string-parsing asymmetry, WH's 0.15 double-rounding example and ties-to-even gap, the dropped `equals` and its composites coupling) and `amount.md` (2025-05 row + cross-reference in the unified-vision issue).
- Existing pages already carried their 2025-05 rows (explicit-resource-management, intl-keep-trailing-zeros, comparisons, iterator-sequencing, iterator-chunking, intl-locale-info).
- Added the 5 catalog rows to `wiki/README.md`. Ran `extract_people.py` (89 → 91 people; added DMM, TAB) then `link_people.py` / `link_proposals.py`, which also linked TAB/DMM retroactively in the 2025-07/2025-09 meeting summaries.

## [2026-09-30] ingest | 2025-04 meeting

- Deep-read the 2025-04 plenary (april-14/15/16/17) and created 7 proposal pages: `async-context` (Stage 2; history traced to the 2020-06 first presentation and rejected 2020-07 Stage 1 ask, the 2023-01 revival by JRL and 2023-03 Stage 2, the 2024-12 reviewers JSL/MM, and the 2025-04 dispatch-context web-integration redesign answering Mozilla's memory-leak feedback with framework testimonials from React/Vue/Solid/Svelte; follow-ups 2025-05/07/09 and 2026-05 folded in), `composite-keys` (Stage 1; successor to the withdrawn Records & Tuples, same meeting; the 2025-11 comparator research — interning got most support), `enums` (Stage 1, RBN/TypeScript; motivated by Node type stripping), `compare-strings-by-codepoint` (Stage 1, MAH/MM/CHR), `disposable-asynccontext` (Stage 1, CZW/LCA/GCL; solutions A/B/C with SYG's "deeply unpalatable" objection to B/C), `object-propertycount` (Stage 1; Stage 2 declined 2025-07, `Object.key[sLength|Count]` split out 2025-11), and `dont-remember-panicking` (Stage 1 since 2019-10 as "OOM Fails Fast"; renamed; the 2025-04 update + continuation ended with no conclusion, SYG's host-hook position recorded).
- Updated `decimal.md` (2025-04 row + the 2025-04 "Amounts" precursor paragraph in the Decimal.Amount issue: WH's foreclosing-options/non-commutativity objections, NRO's "difficult to make a mistake" defense, SFC's commutativity note) and hand-linked the plain-text `composites`/Composites mentions in `upsert.md` and `records-and-tuples.md` to the new page.
- Existing pages already carried their 2025-04 rows (amount, array-from-async, immutable-arraybuffer, explicit-resource-management, intl-era-month-code, temporal, upsert, records-and-tuples withdrawal).
- Added the 7 catalog rows to `wiki/README.md`. Ran `extract_people.py` (91 → 95 people; added CHR, JH, JHX, SRV) then `link_people.py` / `link_proposals.py`, which also retroactively linked AsyncContext / Object.propertyCount mentions in the 2025-07/2025-09/2026-05 meeting summaries. One false positive caught at the source: "ADT" (algebraic data type) in `enums.md` collides with a delegate abbreviation, so it was added to `extract_people.py`'s `NON_PERSON` and the phantom `people/ADT.md` deleted before commit.

## [2026-09-30] ingest | 2025-02 meeting

- Deep-read the 2025-02 plenary (february-18/19/20) and created 4 proposal pages: `float16array` (Stage 4; 2017-05 Stage 1 by LEO then six-year dormancy, the 2023-03 revival by KG on canvas/WebGPU/ML demand with SYG refusing a same-day Stage 3 and WH's bfloat16 question, 2023-05 Stage 3 with SYG's "basically for interchange with GPUs" performance expectations, 2025-02 Stage 4 with JSC/SpiderMonkey shipping and Chrome 135 default), `redeclarable-global-eval-vars` (Stage 4; a needs-consensus PR converted to a proposal at 2024-04, Stage 2.7 and Stage 3 in the same meeting, `[[VarNames]]` removal with SYG's "Nevertheless, don't do this" on the newly-allowed shadowing), `regexp-escaping` (Stage 4; the ten-year arc from the 2015-07 presentation through KG's context-safety analysis, MM's endorsement, the 2024-02 hex-escape reversal away from new identity escapes, the 2024-04 safety follow-ups (leading letters, line terminators, WH's surrogate-dribbling attack), the 2024-06 3-3 temperature check keeping character escapes, and 2024-07 Stage 3), and `import-defer` (Stage 3; 2021-01 Stage 1 by YSV, 2023-07 Stage 2 conditional on Wasm/TLA interaction, the 2024-10 thenable problem — promise resolution reading `.then` forcing evaluation — resolved 2024-12 by export-name-read triggers, no `then` on deferred namespaces, `toStringTag` "deferred module", and dropping `Symbol.evaluated`, 2025-02 Stage 3 with Test262 merged and WebKit implemented, the 2025-04 `export defer` split-off, and the 2026-03/07 follow-ups).
- Limited ArrayBuffer was evaluated and correctly excluded: its 2025-02 session ("Stay in stage 1. Continue exploring.") is an update-only row and its Stage 1 dates to 2021-04 — no 2025 transition, no page. Existing pages already carried their 2025-02 Stage 4 rows (temporal-adjacent Float16/Redeclarable/RegExp Escaping were the only transitions that day; decorators had an informational implementation update only).
- Updated `families/modules.md`: the `import-defer` members row is now a link to the new page.
- Added the 4 catalog rows to `wiki/README.md`. Ran `extract_people.py` (95 → 96 people; added LEO = Leo Balter, Float16 champion) then `link_people.py` / `link_proposals.py`, which also linked `import defer` mentions in the 2026-03/2026-07 meeting summaries retroactively.

## [2026-09-30] ingest | 2024-12 meeting

- Deep-read the 2024-12 plenary (december-02/03/04/05) and created 5 proposal pages: `more-currency-display-choices` (Stage 2 same-session; EAO; formalSymbol/never currencyDisplay values; TG2 debated a normative PR instead; not listed in tc39/proposals, so Stage 2 rests on the notes), `intl-durationformat` (Stage 4; full history traced back to the 2020-02 "Time Duration Format" Stage 1 and 2020-06 Stage 2, 2021-10 Stage 3, then the three-year Stage 3 drip of PRs (formatToParts overhaul #126, negative-sign fix, digital-style grouping separators) to the 2024-12 Stage 4 with DLM/PFC support; USA presented for the absent BAN; PFC's Temporal-hat support; also absent from tc39/proposals' finished list), `stabilize` (Stage 1; MM's unbundling of integrity levels into orthogonal traits - fixed/overridable/non-trapping - with SYG backing fixed for shared structs and floating V8's retcon-non-extensible-implies-fixed use counter, KG's object-model complexity concern, NRO's unbundled-is-simpler counter; champions MM/CM/RGN/MAH from the canonical Stage 1 table), `import-sync` (Stage 1; GB presenting the Node require(esm) demand with "I have no desire to see import sync today", SYG's cranky sync-path objection entered into the record, JSL's ecosystem pre-emption argument, MM supplying the Stage 1 tie-breaker; canonical Stage 2 (2026-01, per the proposals list) recorded as current_stage), and `esm-phase-imports` (Stage 2.7 conditional on MM interrogating semantics via TG3; the generalization of Stage 3 source phase imports restarted at Stage 1 in 2024-02, Stage 2 in 2024-06; 2026-03 update and 2026-05 PR #61 consensus folded in from the existing summaries).
- Verified existing pages' 2024-12 rows and **fixed `iterator-sequencing.md`: the page claimed Stage 3 at 2024-12, but the notes conclude "MF will wait until the test262 tests have been merged before asking for Stage 3 again" (SYG: "I want them to be in the repo to be runnable")** - the row is now a deferral and Stage 3 moved to 2025-05 (the page had also mislabeled that row "Stage 3 update"); mermaid and reading note corrected (2024 end-of-year 2.7). Added the JMN/MF Stage 2 reviewers to `upsert.md`'s 2024-12 row. error-is-error (Stage 3), immutable-arraybuffer (Stage 2), amount (Measure update), async-context, and import-defer already carried correct rows. ShadowRealm's 2024-12 Stage 3 request was withdrawn in-session (belongs to the 2024-02 page via its 2→2.7 transition); Error Stacks Structure did not advance (a smaller accessor proposal was announced instead - covered by `error-stack-accessor.md`).
- Updated `families/modules.md`: `esm-phase-imports` row linked to the new page; `import-sync` added to members and the Members table (Stage 2, 2026-01).
- Added the 5 catalog rows to `wiki/README.md`. Ran `extract_people.py` (96 → 97 people; CM = Chip Morningstar and MAH = Mathieu Hofman joined the roster via stabilize's champions) then `link_people.py` / `link_proposals.py`, which also linked ESM Phase Imports mentions in the 2026-03/2026-05 meeting summaries retroactively.

## [2026-09-30] ingest | 2024-10 meeting

- Deep-read the 2024-10 plenary (october-08/09/10) and created 8 proposal pages: `regexp-modifiers` (Stage 4; the withdrawn Babel-driven early-error tweak with SYG's "we made a decision already", the two-year Stage 3 tests gap), `import-attributes` (Stage 4; full Module Attributes → Import Assertions → Import Attributes arc including the 2023-01 demotion to Stage 2 and the 2024-07 `assert` drop validated by Chrome/Node unshipping), `json-modules` (Stage 4; the 2020-11 split from import assertions, Stage 3 granted 2021-01 with mutable semantics after the committee's immutable temperature read proved wrong - DDC's "this turned out not to be correct" and CM's "It's just, I'm cranky"), `iterator-helpers` (Stage 4; traced back to 2019-01 Stage 1 / 2019-07 Stage 2, the 2020-06 generator-semantics impasse, 2022-11 Stage 3 conditional on Iterator.from strings, the 2023-01 async split, and the regenerator × airgap.js unshipping with its accessor resolution seeding Stabilize), `promise-try` (Stage 4; 2016-11 Stage 1 "not ready for Stage 2, pending more evidence of motivation", the seven-year dormancy, and the 2024-02 revival where the Stage 2 grant came from a same-day "revisit" session after SYG's motivation push - JRL's AMP sync-throw war story as the concrete case), `shared-structs` (Stage 2; 2021-08 Stage 1 as "Fixed layout objects", the 2023-03 V8 experience report (shared cage per process, publication fence), 2024 WasmGC convergence, and the 2024-10 Stage 2 with open questions on WeakMap keys (YSV: "frankly extremely prohibitively expensive") and unsafe blocks (WH's "may be a mirage" vs MM's "unacceptable")), `extractors` (Stage 2; object extractors dropped 2024-02, the 2024-04 Stage 2 request failed on the ASI/NoLineTerminator fix, 2024-10 Stage 2 with SYG's "prime candidate for a JS sugar feature" objection answered by DE's resolve-by-2.7 agreement), and `array-zip` (Stage 1 only; asked 1/2/2.7, granted 1, gated on Joint Iteration Stage 3+ usage data per MF's "no cheating by putting them in a bunch of your libraries").
- Verified existing pages already carried their 2024-10 rows (upsert/Map.emplace update, math-sum-precise, atomics-pause, error-is-error, immutable-arraybuffer, iterator-chunking, amount, decimal); temporal's 2024-10 item was update-only.
- Updated `families/modules.md` (import-attributes + json-modules rows linked) and `families/iterator.md` (iterator-helpers row linked; array-zip added to members and the Members table). `shared-structs` gets no `families` entry until a `concurrency` family page exists.
- Added the 8 catalog rows to `wiki/README.md`. Ran `extract_people.py` (97 → 106 people; added AMP, DDC, DT, JKN, JTO, LGH, MBS, RKG, SSA via the new pages) then `link_people.py` / `link_proposals.py`.

## [2026-09-30] ingest | 2024-07 meeting

- Deep-read the 2024-07 plenary (july-29/30/31) and created 2 proposal pages: `unordered-async-iterator-helpers` (Stage 1; split out of Async Iterator Helpers, MF's commitment not to seek Stage 2 until the parent advances, the DLM/SYG "down the rabbit hole" concern with SYG's missing-web-developer-demand objection, the no-inheritance object model with MM's instanceof/Liskov exchange and KG's counter, and the open naming/coercion/concurrency-parameter questions), and `avoid-capturing-lexical-context` (Stage 2.7; normative PR ecma262#3374 converted to a proposal at KM's two-implementations suggestion - dynamic import() through indirect eval capturing the caller's referrer as the one remaining dynamic-scoping leak, SYG's "corner casey ... likely to be deprioritized" no-false-promises caveat, DLM's won't-implement-first caution, KKL's confinement motivation; not in the tc39/proposals canonical list, so the stage rests on the notes).
- Updated `decimal.md`: added the missing 2024-07 row (Stage 2 requested again, blocked by JHD with his position unchanged since June; SFC explicitly supportive from the Intl side; PFC's object-doesn't-foreclose-primitives argument), extended the primitive-vs-object issue with JHD's Java/Ruby ergonomics case from that session, and corrected "argued since 2024-10" to "since 2024-04" (the page's own 2024-04 row already recorded his block).
- Verified existing pages already carried their 2024-07 rows (regexp-escaping Stage 3, import-attributes drop-assert, atomics-pause both sessions, error-is-error proxy-piercing removal, joint-iteration zipKeyed rename, is-template-object failed 2.7 ask). Update-only items correctly skipped: Intl.Locale PR 83 consensus, AsyncContext ("Stage 2 update ... will seek 2.7 at the 104th meeting"), source phase imports, concurrency control, Temporal, Scrub of Stage 2 Proposals.
- Updated `families/iterator.md` (unordered-async-iterator-helpers row linked). Added the 2 catalog rows to `wiki/README.md`. Ran `extract_people.py` (roster unchanged at 106; KKL already had a page) then `link_people.py` / `link_proposals.py`.

## [2026-09-30] ingest | 2024-06 meeting

- Deep-read the 2024-06 plenary (june-11/12/13) and created 1 proposal page: `discard-bindings` (Stage 2; traced 2024-02 Stage 1 - RGN's "unusual in actually seeming to pay for itself", the MLS/RBN undefined-vs-elision exchange, DE's "left-hand side feature" scoping - through the 2024-04 WH cover-grammar block (issue #5) resolved by PR #9, the 2024-06 Stage 2 with the underscore-vs-void decision deferred (lodash prevalence per RBN, DMM's Java formalization story), and the 2024-10 pattern-matching coupling debate - JRL/JWK's "Rust shows another way" vs SFC's "a proposal needs to be motivated by itself" and RBN's cross-cutting counter; Stage 3 reviewers ACE/OMT at october-10).
- Updated `decimal.md` with the missing 2024-06 row (Stage 2 requested with fleshed-out spec text; critical feedback keeps it at Stage 1 - rounding/quanta definition, ecosystem-usage evidence, deeper Intl.PluralRules integration) and `iterator-sequencing.md` with its 2024-06 row (infinite case dropped, NRO/JMN/RGN Stage 2.7 reviewers; kept at Stage 2). `extractors.md` now links the new discard-bindings page.
- Verified existing pages already carried their 2024-06 rows (import-defer Stage 2.7, joint-iteration Stage 2.7 with the zip rename + no-strings + mode-string decisions, atomics-pause 1 → 2.7 without recorded Stage 2, promise-try Stage 3, regexp-escaping 2.7). Update-only items correctly skipped: ESM Phase Imports Stage 2, Intl.MessageFormat error-handling options (no transition; options 4-6 to be considered), Temporal scope reduction, Intl.DurationFormat normative PRs, ShadowRealm update, Proposal Scrub.
- Added the 1 catalog row to `wiki/README.md`. Ran `extract_people.py` (roster unchanged at 106) then `link_people.py` / `link_proposals.py`.

## [2026-09-30] ingest | 2024-04 meeting

- Deep-read the 2024-04 plenary (april-08/09/10/11) and created 4 proposal pages: `duplicate-named-capture-groups` (Stage 4; conditional Stage 2 on first presentation in 2022-06 with WH's review folded in, Stage 3 the next month, then two years waiting on engines - SpiderMonkey reuses V8's RegExp engine - before Safari/Chrome 125 shipping carried Stage 4; deterministic groups-object iteration order fixed during the Stage 2 window), `set-methods` (Stage 4; Stage 2 at its first presentation in 2018-05 as the Set-specific split of a collection-methods proposal, a three-and-a-half-year stall with champion turnover from SGN to KG, revived 2022-07/09 on argument handling ("option 2"), Stage 3 in 2022-11 with SYG's ordering-implementability caveat, blocked on tests at the Stage 4 gate), `signals` (Stage 1; the cross-framework working-group proposal presented by DE - State/Computed plus "subtle" APIs, MAH's observable-global-mutable-state concern, RBN's events/observables modeling question, JHD's rules-of-hooks/capability-separation follow-ups, and DE's explicit "no Stage 2 within the next 12 months"), and `using-enforcement` (Stage 1; RBN's opt-in `[Symbol.enter]` follow-on to Explicit Resource Management - MM preferred the getter alternative, KG argued the getter gives no enforcement at all, SYG found no mechanical story, adopted for Stage 1 anyway).
- Updated `records-and-tuples.md`: replaced the "(2023-2024) long stall" row with the 2024-04 "Discussing new directions for R&T" session (ACE's retrospective plus the first sketch of the no-primitives/composite-key direction - WeakMap-trie keys via proposal-keyby and `uniqueBy` APIs; contrasting views, no conclusions), added the source line, and noted the 2024-04 session as the precursor of the 2025-02 composite-key redesign.
- Verified existing pages already carried their 2024-04 rows (promise-try Stage 2.7, regexp-escaping 2.7 request with safety follow-ups, import-defer 2.7 without tree-shakeable exports, math-sum-precise 2.7 as `sumPrecise`, dynamic-code-brand-checks 1 → 3, is-template-object stayed at 2, async-context update, joint-iteration issue-1, extractors ASI failure, discard-bindings cover-grammar block, decimal Stage 2 block, shared-structs). Update-only/no-transition items correctly skipped: Module sync assert (JWK, denied Stage 2 - "no spec so not qualified"), Iterator.range 2.7 (deferred on the floating-point discussion), "array last" withdrawal, Temporal normative bugfix, Stop Coercing pt 4, property-key-resolution-timing discussion.
- Added the 4 catalog rows to `wiki/README.md`. Ran `extract_people.py` (roster 106 → 112: DGY, JRA, LZU, MLM, NVP, SYL) then `link_people.py` / `link_proposals.py`.

## [2026-09-30] ingest | 2024-02 meeting

- Deep-read the 2024-02 plenary (feb-6/7/8) and created 5 proposal pages: `shadowrealm` (Stage 2.7; the long Realms lineage - 2017-01 Stage 1, 2018-05 Stage 2, Stage 3 in 2022-11, the 2023-09 demotion to Stage 2 over the unimplementable-without-audit web API exposure list, 2024-02 Stage 2.7 with WHATWG HTML + Mozilla entrance criteria for Stage 3, and the 2024-12 Stage 3 request withdrawn in-session with SYG's "If we agree to Stage 3 and no browser ships it, that's bad"; the W3C TAG "only purely computational features are exposed everywhere" principle and the HTML `Exposed everywhere` attribute as the settled answer), `iterator-unique` (Stage 1; MF's mapper-vs-comparator design with KG's groupBy-consistency and SYG's set-oriented-vs-quadratic confirmation, the hidden unbounded memory "pit of success" objection (SYG: "It's not the unbounded part that worries me. It's the hidden part"), MLS's why-not-a-library challenge that MF accepted as a possible outcome, JHD's arrays-too request, and LCA's pass-your-own-set alternative), `arraybuffer-transfer` (Stage 4, ES2024; 2018-07 Stage 2 by DD on the race-condition/Node thread-read motivation, folded into resizable buffers, broken back out and demoted 3 to 2 in 2022 because the original semantics did not preserve resizability, 2023-01 Stage 3 as `transfer`/`transferToFixedLength` + the `detached` getter with MAH's copy-on-write pushback answered by SYG's fixed-data-pointer security-mitigation argument, and the one-method-vs-two temperature check), `improve-template-literals` (Stage 1; presented as "Raw String Literals" by JHX with Rust/Swift-style hash-wrapped delimiters, DE's "not sure whether this topic is worthy" skepticism, MM's "very big regret" about template literal escapeability coupled with skepticism about a coexisting second syntax, LCA's don't-burn-`#`, JRL's unrepresentable trailing backslash, DRR's "kicking the can down the road", and the renamed Stage 1 scoped to "an investigation on how to deal with the limits of template strings"), and `function-and-object-literal-decorators` (Stage 1; RBN's decorator-reuse/consistency case with the Amazon Chalice `addInitializer` registration example, KG's motivation challenge - "a new way of calling functions... almost indistinguishable" - answered one argument at a time, SYG's "it basically boils down to vibes" plus the before/after-rewrites price for Stage 2 and the explicit parameter-decorators carve-out, Angular's internal regrets, KG's support hinging on the object-literal half adding real expressivity, and the same-day hoisting session where the champion's "don't hoist decorated function declarations" option 3 met DE's Bloomberg-internal "technically correct answer, but that is not universal").
- Corrected a factual error in `iterator-sequencing.md` found while cross-checking: the page claimed Stage 2 at 2024-02, but the notes conclude "Did not seek consensus for Stage 2, due to critical feedback. The proposal remains at Stage 1" (JHD's concat-flattening objection, KG's variadic-`Iterator.from` inconsistency). Fixed the history row (Stage 2 actually reached 2024-06 with the infinite case dropped), the reading note, and the issues section.
- Scope decisions: `atomics-microwait` needs no page (the lineage incl. the 2024-02 Stage 1 and the 2024-04 withdrawal is already covered by `atomics-pause.md`); Module sync assert (JWK) was denied Stage 2 - no transition, no page; Iterator.range's 2.7 deferral is update-only on `iterator-range` (no page yet, backbone only); Source Phase Imports and ESM Phase Imports stayed at existing stages (covered by `esm-phase-imports.md`).
- Updated `families/iterator.md` (iterator-unique row turned from a member-without-page into a link). Added the 5 catalog rows to `wiki/README.md`. Ran `extract_people.py` (112 -> 115: CP, JFP, YNP via the ShadowRealm/ArrayBuffer transfer frontmatter) then `link_people.py` / `link_proposals.py`. Avoided an `AWS` false positive (Amazon's Chalice framework, not delegate Ashley Williams) by rewording to "Amazon Chalice" instead of adding to NON_PERSON.

## [2026-10-01] ingest | 2025-05 meeting (verification and corrections)

- Re-verified all 15 proposal-relevant topics of the 2025-05 plenary against their pages. 12 already carried accurate rows from the earlier pass (explicit-resource-management, array-from-async, error-is-error, intl-keep-trailing-zeros, seeded-prng, more-random-functions, comparisons, decimal, async-context, intl-locale-info, immutable-arraybuffer; comparisons correctly records 2025-05 as a Stage 1 ask that did not advance).
- **Fixed `iterator-sequencing.md`: the 2025-05 row claimed "Reached Stage 3", but the notes conclude the opposite** - MF backs out the `yield*`-alignment changes (PRs #18, #19/#23: IteratorResult reuse, final `.value` access) because matching `yield*` is unachievable and "every time we get close to `yield*`, there's less desirable behavior" (RGN: "very enthusiastic about revisiting the past decisions that were based on matching `yield*`"), and he will "come back for Stage 3 at a later meeting". Stage 3 was actually reached 2025-07 (july-28, back-out landed as PR #26; DLM/KG/NRO/MM support). Corrected the row (2.7 kept), the chart reading note, the issue section (now tells the 2024-12 Test262 deferral and the 2025-05 `yield*` backtrack together), and the sources. Third deferral-recorded correction on this page (2024-02, 2024-12, now 2025-05) - its row-accuracy is now fully notes-checked through Stage 3.
- Enriched `iterator-chunking.md` with the 2025-05 issue that had been left out: the `.windows()` undersized-tail edge case (options: no windows / throw / undersized / padded; language-and-library survey favoring option 1; NRO/PFC vs DMM on dropping values, JHD's done-result idea rejected because chaining loses it, MM/RGN's worthiness skepticism answered by SFC/KG/CM/LCA evidence) and the conclusion to split `.windows()` into two methods; row updated.
- Added the missing 2025-05 row to `temporal.md` (Firefox ship confirmed the day before, SpiderMonkey ~99% Test262; consensus on the UTC-offset-matching normative change: optional seconds present in an offset must match exactly, else RangeError - the -11:19:40/-11:20:00 case) plus the source line.
- **Root cause of the Temporal omission, fixed in `tools/extract_agenda.py` [wiki]**: the BOILERPLATE filter's `.*status update` clause swallowed every proposal "status update" heading, hiding the 2025-05 Temporal item from the backbone and ~30 historical items besides (BigInt, Class fields, Decorators, Record & Tuple, WeakRefs, Top-level await, ShadowRealm, ...). Replaced with a subject-scoped STATUS_BOILERPLATE (spec documents / Test262 / task groups / IP policy stay boilerplate; proposal updates are kept) plus leading agenda-number stripping for old transcripts. Regenerated `agenda-index.md`/`.jsonl` (2814 -> 2844 items; ECMA-262/402/404/Test262/TG boilerplate still excluded). This lossy filter is also the likely reason past ingests under-recorded update-only items.
- Ran `extract_agenda.py`, `extract_people.py` (115 pages; ABL's page now cites iterator-sequencing), `link_people.py` (linked the DLM/KG/NRO/MM plain-text names in the new iterator-sequencing row), `link_proposals.py` (no changes). No catalog changes needed (all 15 rows already present).
