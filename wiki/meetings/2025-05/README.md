# 108th TC39 Meeting (2025-05)

- **Meeting**: 108th meeting of Ecma TC39
- **Dates**: 2025-05-28 to 2025-05-30 (10:00-17:00 CEST on May 28-29; 10:00-16:00 CEST on May 30)
- **Location**: A Coruña, Galicia, Spain
- **Host**: Igalia
- **Agenda**: [tc39/agendas 2025/05](https://github.com/tc39/agendas/blob/main/2025/05.md)

## Overview

A three-day in-person meeting hosted by Igalia. **[Error.isError](../../proposals/error-is-error.md) reached Stage 4**, with **[Array.fromAsync](../../proposals/array-from-async.md) and [Explicit Resource Management](../../proposals/explicit-resource-management.md) reaching Stage 4 conditionally** (editor sign-off and Test262 respectively), while **[Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md) and the `Random` namespace ([More Random Functions](../../proposals/more-random-functions.md)) reached Stage 1**, and **[Math.clamp](../../proposals/math-clamp.md) (decided as `Number.prototype.clamp`) and [SeededPRNG](../../proposals/seeded-prng.md) (immediately renamed `Random.Seeded`) reached Stage 2**. [Temporal](../../proposals/temporal.md) shipped in Firefox as of May 27, with V8 integrating the Rust `temporal_rs` implementation. The [Comparisons](../../proposals/comparisons.md) presentation was split into Inspector / Modes / Comparisons, with the Inspector part reaching Stage 1 on day 3. [Iterator Chunking](../../proposals/iterator-chunking.md) was not advanced — the too-few-items `.windows()` question will be solved by splitting it into two methods — and [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md) presented its testing plan, targeting Stage 3 at the next meeting. The [Decimal](../../proposals/decimal.md) `Amount` design ran through all three days (with a 90-minute numerics breakout on day 3), converging on preserving the possibility of future decimal primitives while leaving String-backed versus Decimal-backed [Amount](../../proposals/amount.md) open. [AsyncContext](../../proposals/async-context.md)'s web-integration brainstorming ended with the DOM-side concerns to be taken to WHATWG, and four normative PRs (late errors for function-call assignment targets, the locale-sets note, Unicode 16 numbering systems, `Intl.Locale.prototype.variants`) reached consensus. SHN explained the Ecma framework (voting rights, document lead times), and the committee agreed to trial "TCQ reloaded" at the next plenary.

## Stage transitions

| Proposal                                                                        | Transition                                                          | Day   |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----- |
| [Error.isError](../../proposals/error-is-error.md)                              | 3 → 4                                                               | Day 1 |
| [Array.fromAsync](../../proposals/array-from-async.md)                          | 3 → 4 (conditional on editor sign-off of ecma262#3581)              | Day 1 |
| [Explicit Resource Management](../../proposals/explicit-resource-management.md) | 3 → 4 (conditional on Test262 and editor sign-off)                  | Day 1 |
| [Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md)         | new → 1                                                             | Day 1 |
| [Iterator Sequencing](../../proposals/iterator-sequencing.md)                   | no advancement (stays 2.7; Stage 3 ask deferred)                    | Day 1 |
| [Intl Locale Info](../../proposals/intl-locale-info.md)                         | normative: TG1 approves returning `undefined` for unknown direction | Day 1 |
| Late Errors for Function Call Assignment Targets (#3568)                        | normative PR consensus                                              | Day 1 |
| Locale sets note for web browsers (ecma402#780)                                 | normative PR consensus                                              | Day 1 |
| Numbering systems for Unicode 16 (ecma402#929)                                  | normative PR consensus                                              | Day 1 |
| `Intl.Locale.prototype.variants` (ecma402#960)                                  | normative PR consensus                                              | Day 1 |
| [Math.clamp](../../proposals/math-clamp.md)                                     | 1 → 2 (as `Number.prototype.clamp`)                                 | Day 2 |
| [SeededPRNG](../../proposals/seeded-prng.md)                                    | 1 → 2 (renamed `Random.Seeded`)                                     | Day 2 |
| [More Random Functions](../../proposals/more-random-functions.md)               | new → 1                                                             | Day 2 |
| [Iterator Chunking](../../proposals/iterator-chunking.md)                       | no advancement (stays 2)                                            | Day 2 |
| [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)               | no advancement (Stage 3 expected next meeting)                      | Day 2 |
| [Comparisons](../../proposals/comparisons.md)                                   | split into Inspector / Modes / Comparisons; Inspector reached 1     | Day 3 |

## Daily summaries

- [Day 1 — 2025-05-28](2025-05-28.md)
- [Day 2 — 2025-05-29](2025-05-29.md)
- [Day 3 — 2025-05-30](2025-05-30.md)

## Attendees

From the attendees in `raw/notes/meetings/2025-05/may-28.md` (abbreviation — name — affiliation):

| Abbreviation               | Name                | Affiliation        |
| -------------------------- | ------------------- | ------------------ |
| [USA](../../people/USA.md) | Ujjwal Sharma       | Igalia             |
| [RKG](../../people/RKG.md) | Ross Kirsling       | Sony               |
| [WH](../../people/WH.md)   | Waldemar Horwat     | Invited Expert     |
| [RPR](../../people/RPR.md) | Rob Palmer          | Bloomberg          |
| [DLM](../../people/DLM.md) | Daniel Minor        | Mozilla            |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser  | Microsoft          |
| [GCL](../../people/GCL.md) | Gus Caplan          | Deno Land Inc      |
| [DMM](../../people/DMM.md) | Duncan MacGregor    | ServiceNow Inc     |
| CHU                        | Christian Ulbrich   | Zalari             |
| [ZTZ](../../people/ZTZ.md) | Zbigniew Tenerowicz | MetaMask           |
| TKP                        | Tom Kopp            | Zalari             |
| TFA                        | Tooru Fujisawa      | Mozilla            |
| [JWK](../../people/JWK.md) | Jack Works          | Sujitech           |
| [JMN](../../people/JMN.md) | Jesse Alama         | Igalia             |
| [DJM](../../people/DJM.md) | Dmitry Makhnev      | JetBrains          |
| [OMT](../../people/OMT.md) | Oliver Medhurst     | IE (Porffor)       |
| [TAB](../../people/TAB.md) | Tab Atkins-Bittner  | Google             |
| JKP                        | Jonathan Kuperman   | Bloomberg          |
| [EAO](../../people/EAO.md) | Eemeli Aro          | Mozilla            |
| [RGN](../../people/RGN.md) | Richard Gibson      | Agoric             |
| [CZW](../../people/CZW.md) | Chengzhong Wu       | Bloomberg          |
| [SHS](../../people/SHS.md) | Steve Hicks         | Google             |
| MBH                        | Mikhail Barash      | Univ. of Bergen    |
| [YSZ](../../people/YSZ.md) | Yusuke Suzuki       | Apple              |
| [CM](../../people/CM.md)   | Chip Morningstar    | MetaMask           |
| [YSV](../../people/YSV.md) | Yulia Startsev      | Mozilla            |
| IS                         | Istvan Sebestyen    | Ecma               |
| [PFC](../../people/PFC.md) | Philip Chimento     | Igalia             |
| [JSC](../../people/JSC.md) | J. S. Choi          | IE (Univ. of Utah) |
| [RBN](../../people/RBN.md) | Ron Buckton         | IE                 |
| [LCA](../../people/LCA.md) | Luca Casonato       | Deno Land Inc      |
| SHN                        | Samina Husain       | Ecma               |
| [ABO](../../people/ABO.md) | Andreu Botella      | Igalia             |
| JHS                        | Jonas Haukenes      | Univ. of Bergen    |
| RCA                        | Romulo Cintra       | Igalia             |
| [JSH](../../people/JSH.md) | Jacob Smith         | OpenJS             |

> Source: [tc39/notes/meetings/2025-05](https://github.com/tc39/notes/tree/main/meetings/2025-05). Dates, location, and host come from [tc39/agendas 2025/05](https://github.com/tc39/agendas/blob/main/2025/05.md).
