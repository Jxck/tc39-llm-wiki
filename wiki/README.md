# TC39 Wiki — Index

A wiki for tracing **how each proposal changed stage, and which issues came up along the way**, drawn from the TC39 plenary notes (`raw/notes`, 2012-05 through 2026-07 / 88 meetings / 340 files). The operating rules are [AGENTS.md](../AGENTS.md); the design notes are [llm-wiki.md](../llm-wiki.md).

## How to use

- **List every proposal's current stage** → [proposals/index.md](proposals/index.md) (full stage catalog generated from `raw/proposals`. Ingested proposals link to their pages).
- **Follow one proposal** → the "Ingested proposals" table below. Each page has `## Stage history` (a timeline table plus a mermaid chart) and `## Main issues`.
- **Follow a person** → a person link on a proposal page (for example `[PFC](people/PFC.md)`) opens a [people/](people/) page (full name, affiliation, champion drafts, meetings attended).
- **Find a proposal or meeting that is not ingested yet** → grep [\_generated/agenda-index.md](_generated/agenda-index.md). Machine-extracted backbone of all 88 meetings and 2814 agenda items. Example: `grep -i -A4 'pattern matching' wiki/_generated/agenda-index.md`.
- **Ingest a new proposal** → follow "Workflow > Ingest" in AGENTS.md.

## Ingested proposals

| Proposal                                                                                  | Current stage       | Status    | Summary                                                                                                                                  |
| ----------------------------------------------------------------------------------------- | ------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Temporal](proposals/temporal.md)                                                         | Stage 4 (2026-03)   | shipped   | Immutable date-time API that replaces `Date`. Reached Stage 4 after about nine years.                                                    |
| [Decorators](proposals/decorators.md)                                                     | Stage 2.7 (2026-05) | stage2.7  | `@expr` annotations on classes. Redesigned three times, Stage 3 in 2022, regressed to 2.7 in 2026-05 with zero shipping implementations. |
| [Records & Tuples](proposals/records-and-tuples.md)                                       | Stage 2 (withdrawn) | withdrawn | Deeply immutable value types `#{}` / `#[]`. Withdrawn in 2025-04.                                                                        |
| [Upsert](proposals/upsert.md)                                                             | Stage 4 (2026-01)   | shipped   | `Map.prototype.getOrInsert` / `getOrInsertComputed`. About six years, mostly on naming and splitting responsibilities.                   |
| [Intl Era/Month Code](proposals/intl-era-month-code.md)                                   | Stage 4 (2026-03)   | shipped   | era / monthCode for non-ISO 8601 calendars in ECMA-402. Stage 4 alongside Temporal.                                                      |
| [Joint Iteration](proposals/joint-iteration.md)                                           | Stage 4 (2026-05)   | shipped   | `Iterator.zip` / `Iterator.zipKeyed`. Zips several iterators by position.                                                                |
| [Atomics.pause](proposals/atomics-pause.md)                                               | Stage 4 (2026-05)   | shipped   | CPU pause hint for spin loops (x86 PAUSE / ARM ISB).                                                                                     |
| [Explicit Resource Management](proposals/explicit-resource-management.md)                 | Stage 4 (2026-05)   | shipped   | Deterministic resource disposal with `using` / `await using`. About eight years.                                                         |
| [Intl.MessageFormat](proposals/intl-messageformat.md)                                     | Stage 1 (2022-03)   | stage1    | Expose MessageFormat 2.0 (MF2) to JS. Stuck on whether a DSL/parser belongs in the language.                                             |
| [Amount](proposals/amount.md)                                                             | Stage 2 (2026-05)   | stage2    | Immutable value type for a number plus a unit (formerly Measure). `convertTo()` and i18n.                                                |
| [Iterator Chunking](proposals/iterator-chunking.md)                                       | Stage 3 (2026-05)   | stage3    | `Iterator.prototype.chunks` / `windows`. Consumes several values in fixed or sliding windows.                                            |
| [Iterator Includes](proposals/iterator-includes.md)                                       | Stage 3 (2026-05)   | stage3    | Iterator version of `Array.prototype.includes`.                                                                                          |
| [Iterator Join](proposals/iterator-join.md)                                               | Stage 3 (2026-05)   | stage3    | Iterator version of `Array.prototype.join`.                                                                                              |
| [RegExp Buffer Boundaries](proposals/regexp-buffer-boundaries.md)                         | Stage 3 (2026-05)   | stage3    | Buffer-boundary anchors `\A` / `\z` / `\Z` (independent of the `m` flag). Straight to Stage 3 in 2026-05.                                |
| [Dynamic Code Brand Checks](proposals/dynamic-code-brand-checks.md)                       | Stage 3 (2024-04)   | stage3    | Trusted Types integration for `eval` / `new Function`. 2026-05 was a normative change; Stage 4 deferred.                                 |
| [Error Stack Accessor](proposals/error-stack-accessor.md)                                 | Stage 3 (2026-05)   | stage3    | Standardize `Error.prototype.stack` as an accessor (carve-out from Error Stacks).                                                        |
| [Intl Keep Trailing Zeros](proposals/intl-keep-trailing-zeros.md)                         | Stage 3 (2026-05)   | stage3    | Keep trailing fractional zeros in `Intl.NumberFormat` / `PluralRules`.                                                                   |
| [Stable Formatting](proposals/stable-formatting.md)                                       | Stage 2 (2026-05)   | stage2    | Locale-independent stable formatting via the `zxx` locale. A substitute for misusing `Intl` in tests.                                    |
| [Intl Sequence Units](proposals/intl-sequence-units.md)                                   | Stage 2 (2026-05)   | stage2    | Format a sequence of compound units (for example `6 ft 0 in`). Stage 2 with object input.                                                |
| [Intl Default Behaviours](proposals/intl-default-behaviours.md)                           | Stage 1 (2026-05)   | stage1    | Locale-independent defaults for `Collator` / `Segmenter` (`und` root). Complements Stable Formatting.                                    |
| [export all from](proposals/export-all-from.md)                                           | Stage 1 (2026-05)   | stage1    | Syntax extensions for `export * from` style re-exports.                                                                                  |
| [Comparisons](proposals/comparisons.md)                                                   | Stage 1 (2026-05)   | stage1    | Native deep comparison and deviation reporting. Formerly "Assertions".                                                                   |
| [Array.isTemplateObject](proposals/is-template-object.md)                                 | Stage 2 (withdrawn) | withdrawn | Detect a template call-site object. Withdrawn in 2026-05 (weak demand plus realm concerns).                                              |
| [Await Dictionary](proposals/await-dictionary.md)                                         | Stage 3 (2026-07)   | stage3    | `Promise.allKeyed` / `allSettledKeyed`. Named `Promise.all`. Skipped Stage 2 for 2.7 in 2025-11.                                         |
| [Thenable Curtailment](proposals/thenable-curtailment.md)                                 | Stage 2.7 (2026-07) | stage2.7  | `SafePromiseResolve`, which resolves a Promise without running user code. Aimed at WebIDL and thenable CVEs.                             |
| [Error code property](proposals/error-code-property.md)                                   | Stage 2 (2026-07)   | stage2    | `code` on `Error` via an options bag. Alignment with DOMException is a condition for advancement.                                        |
| [Fused Multiply-Add](proposals/fused-multiply-add.md)                                     | Stage 2 (2026-07)   | stage2    | `Math.fma` (required by IEEE 754-2008). Straight from 0 to 2 on first presentation. Motivated by Amount conversion precision.            |
| [BigInt from exponential](proposals/bigint-from-exponential.md)                           | Stage 1 (2026-07)   | stage1    | Accept exponential-notation strings in `BigInt`. Converted from needs-consensus PR #3857.                                                |
| [Map get and delete](proposals/map-get-and-delete.md)                                     | Stage 1 (2026-07)   | stage1    | `Map.prototype.getAndDelete` (formerly take). Get and delete in one hash lookup.                                                         |
| [Linear Matching](proposals/linear-matching.md)                                           | Stage 1 (2026-07)   | stage1    | Built-in mitigation for ReDoS. Exploring regexp execution with a linear-time guarantee.                                                  |
| [Intl.DateTimeFormat Alignment](proposals/intl-datetimeformat-alignment.md)               | Stage 1 (2026-07)   | stage1    | Align datetime formatting options with HTML `<time format>` and MessageFormat.                                                           |
| [Decimal](proposals/decimal.md)                                                           | Stage 1 (2020-02)   | stage1    | Exact base-10 arithmetic via IEEE 754 Decimal128. Stalled since 2020 on a primitive-vs-object-API disagreement with V8/SpiderMonkey.     |
| [JSON.parse source text access](proposals/json-source-text.md)                            | Stage 4 (2025-11)   | shipped   | Source text access for `JSON.parse` / `JSON.stringify`. Presented in 2018-09, seven years to Stage 4.                                    |
| [Error.captureStackTrace](proposals/error-capture-stack-trace.md)                         | Stage 2 (2025-11)   | stage2    | Standardize Chrome's `captureStackTrace`. Accessor design specified but marked legacy for new implementations.                           |
| [Intl Locale Info](proposals/intl-locale-info.md)                                         | Stage 4 (2025-11)   | shipped   | `firstDayOfWeek` / week data etc. on `Intl.Locale`. Five years in Stage 3; PR 92 (explicit fallback) unblocked Stage 4.                  |
| [Iterator Sequencing](proposals/iterator-sequencing.md)                                   | Stage 4 (2025-11)   | shipped   | `Iterator.concat`. One stage per meeting from Stage 1 (2023-09) to Stage 3 (2024-12).                                                    |
| [Intl Unit Protocol](proposals/intl-unit-protocol.md)                                     | Stage 2 (2026-03)   | stage2    | Per-format-call unit association for `Intl.NumberFormat`. Split out of Amount; conversion waits on Amount.                               |
| [Import Text](proposals/import-text.md)                                                   | Stage 3 (2026-03)   | stage3    | `import ... with { type: "text" }`. Stage 1 and 2 in one session (2025-11); encoding is a host concern (UTF-8 assumed).                  |
| [TypedArray Concatenation](proposals/typedarray-concat.md)                                | Stage 1 (2025-11)   | stage1    | Optimizable multi-`TypedArray` concat. Zero-copy framing pushed back by V8 (rope performance cliffs).                                    |
| [TypedArray Find Within](proposals/typedarray-find-within.md)                             | Stage 1 (2025-11)   | stage1    | Subsequence search for `TypedArray`. Naming consistency with `indexOf` / `includes` to be settled.                                       |
| [Intl Energy Units](proposals/intl-energy-units.md)                                       | Stage 1 (2025-11)   | stage1    | W / kW / kWh in `Intl.NumberFormat`. Narrow use-case-driven batches over a holistic units proposal.                                      |
| [Object.getNonIndexStringProperties](proposals/object-get-non-index-string-properties.md) | Stage 1 (2025-11)   | stage1    | Non-index string keys of array-likes. Stage 1 without asking; KG requires a motivation case before Stage 2.                              |

## Families (cross-cutting summaries)

Synthesis pages that group proposals in the same category. Per-proposal history stays on the proposal page; the family page holds the shared picture and the stage list.

- [Iterator helpers and friends](families/iterator.md) — the lazy iteration library around `Iterator.prototype` (helpers, zip, concat, chunking, includes, async variants, and others).
- [Modules (module harmony)](families/modules.md) — ES modules and the proposals that grew out of them (dynamic import, import.meta, TLA, import attributes, phase imports, import-export defer, and others).

## Not yet written (link targets)

Proposal pages referenced from ingested pages but not created yet:

- `class-fields` — tightly tied to Decorators through the sigils (`@` / `#`).
- `private-methods` — related to class fields.
- `pipeline-operator` — mentioned in the Decorators discussion.

## Person pages (people/)

People who appear on proposal or family pages are collected under [people/](people/) (86 at the moment). Each file is named by abbreviation and lists full name, affiliation, champion drafts, proposals and families that mention them, and meetings attended. `tools/extract_people.py` detects abbreviations on proposal and family pages and generates the pages. `tools/link_people.py` turns abbreviations in proposal, family, and meeting-summary prose into `[ABBR](<rel>/people/ABBR.md)` (standard markdown links that work in the VS Code preview). `tools/link_proposals.py` links proposal names in meeting summaries to proposal pages. Only people who actually appear are included, and the set grows as pages are added.

## Backbone (machine-extracted)

[\_generated/agenda-index.md](_generated/agenda-index.md) — agenda headings, stage signals, and conclusions for every meeting, extracted by `tools/extract_agenda.py`. Do not edit by hand (regeneration overwrites it). After a submodule update, refresh with `python3 tools/extract_agenda.py && python3 tools/extract_proposals.py && python3 tools/extract_people.py && python3 tools/link_people.py`.

## Status legend

`stage0` through `stage3` (including `stage2.7`) / `shipped` (reached Stage 4) / `withdrawn` / `inactive` (long stall). These match the `status` field in each page's frontmatter.
