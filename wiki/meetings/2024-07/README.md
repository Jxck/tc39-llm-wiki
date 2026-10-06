# 103rd TC39 Meeting (2024-07)

- **Meeting**: 103rd meeting of Ecma TC39
- **Dates**: 2024-07-29 to 2024-07-31 (10:00-15:00 PDT)
- **Location**: Remote
- **Agenda**: [tc39/agendas 2024/07](https://github.com/tc39/agendas/blob/main/2024/07.md)

## Overview

A three-day remote meeting. Two proposals entered at **Stage 1**: [Concurrency Control](../../proposals/concurrency-control.md) (governor protocol + `Semaphore`, amid naming and abstraction skepticism) and [Unordered async iterator helpers](../../proposals/unordered-async-iterator-helpers.md) (split out of async iterator helpers). [RegExp.escape](../../proposals/regexp-escaping.md) reached **Stage 3** and [Intl Locale Info](../../proposals/intl-locale-info.md) got conditional consensus on its update PR (already Stage 3 since 2021). A normative PR on indirect eval was converted into a **Stage 2.7** proposal — [Avoid capturing lexical context in indirect eval](../../proposals/avoid-capturing-lexical-context.md) — and [Propagate active ScriptOrModule with JobCallback Record](https://github.com/tc39/ecma262/pull/3195) reached **Stage 2** as a host-requirement fix aligning with HTML. Four proposals did not advance: [Atomics.pause](../../proposals/atomics-pause.md) (no consensus for Stage 3 or for demotion, across two days), [Error.isError](../../proposals/error-is-error.md) (returns next meeting), [Decimal](../../proposals/decimal.md) (blocked), and [Array.isTemplateObject](../../proposals/is-template-object.md) (renamed `Reflect.isTemplateObject` only). Consensus also landed to drop `assert` from [import attributes](../../proposals/import-attributes.md) (Stage 4 planned next meeting) and on the how-we-work normative convention that new APIs pretend primitives aren't iterable. [Temporal](../../proposals/temporal.md) is nearly done and took two normative fixes; `Math.sqrt` was fully specified; and the [Joint Iteration](../../proposals/joint-iteration.md) `zipToObject` was renamed `Iterator.zipKeyed`. Secretary's report: four new Ecma members (Replay.io, HeroDevs, Sentry, JetBrains), and a TC55 (runtime) proposal with W3C; [BAN](../../people/BAN.md) was appointed to the ECMA-402 editor group. The agenda also scheduled a fourth day (Aug 1), but the notes contain only these three days.

## Stage transitions

| Proposal                                                                                               | Transition                                           | Day       |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- | --------- |
| [RegExp.escape](../../proposals/regexp-escaping.md)                                                    | 2 → 3                                                | Day 1     |
| [Concurrency Control](../../proposals/concurrency-control.md)                                          | new → 1                                              | Day 1     |
| [Unordered async iterator helpers](../../proposals/unordered-async-iterator-helpers.md)                | new → 1                                              | Day 2     |
| [Avoid capturing lexical context in indirect eval](../../proposals/avoid-capturing-lexical-context.md) | new → 2.7                                            | Day 3     |
| `Propagate active ScriptOrModule with JobCallback Record`                                              | new → 2                                              | Day 3     |
| [Atomics.pause](../../proposals/atomics-pause.md)                                                      | no advancement (no consensus for Stage 3 or Stage 2) | Days 1, 3 |
| [Error.isError](../../proposals/error-is-error.md)                                                     | no advancement (returns for Stage 2.7)               | Day 2     |
| [Joint Iteration](../../proposals/joint-iteration.md)                                                  | no advancement (`zipToObject` → `zipKeyed`)          | Day 2     |
| [Decimal](../../proposals/decimal.md)                                                                  | no advancement (blocked)                             | Day 3     |
| [Array.isTemplateObject](../../proposals/is-template-object.md)                                        | no advancement (renamed `Reflect.isTemplateObject`)  | Day 3     |

## Daily summaries

- [Day 1 — 2024-07-29](2024-07-29.md)
- [Day 2 — 2024-07-30](2024-07-30.md)
- [Day 3 — 2024-07-31](2024-07-31.md)

## Attendees

From the attendees in `raw/notes/meetings/2024-07/july-29.md` (abbreviation — name — affiliation):

| Abbreviation               | Name             | Affiliation      |
| -------------------------- | ---------------- | ---------------- |
| [CDA](../../people/CDA.md) | Chris de Almeida | IBM              |
| [USA](../../people/USA.md) | Ujjwal Sharma    | Igalia           |
| [WH](../../people/WH.md)   | Waldemar Horwat  | Invited Expert   |
| [BAN](../../people/BAN.md) | Ben Allen        | Igalia           |
| [JMN](../../people/JMN.md) | Jesse Alama      | Igalia           |
| [LGH](../../people/LGH.md) | Linus Groh       | Bloomberg        |
| [RBN](../../people/RBN.md) | Ron Buckton      | Microsoft        |
| [DLM](../../people/DLM.md) | Daniel Minor     | Mozilla          |
| [CM](../../people/CM.md)   | Chip Morningstar | Consensys        |
| [PFC](../../people/PFC.md) | Philip Chimento  | Igalia           |
| [MLS](../../people/MLS.md) | Michael Saboff   | Apple            |
| MBH                        | Mikhail Barash   | Uni. Bergen      |
| SHN                        | Samina Husain    | Ecma             |
| [KM](../../people/KM.md)   | Keith Miller     | Apple            |
| [RGN](../../people/RGN.md) | Richard Gibson   | Agoric           |
| [JRL](../../people/JRL.md) | Justin Ridgewell | Google           |
| AKI                        | Aki Braun        | Ecma Secretariat |
| [JHD](../../people/JHD.md) | Jordan Harband   | HeroDevs         |
| IS                         | Istvan Sebestyen | Ecma             |
| DGN                        | Dan Gohman       | Invited Expert   |
| JPB                        | Josh Blaney      | Apple            |
| [DJM](../../people/DJM.md) | Dmitry Makhnev   | JetBrains        |
| [CZW](../../people/CZW.md) | Chengzhong Wu    | Bloomberg        |
| [ACE](../../people/ACE.md) | Ashley Claymore  | Bloomberg        |

> Source: [tc39/notes/meetings/2024-07](https://github.com/tc39/notes/tree/main/meetings/2024-07). Dates, location, and the scheduled fourth day come from [tc39/agendas 2024/07](https://github.com/tc39/agendas/blob/main/2024/07.md).
