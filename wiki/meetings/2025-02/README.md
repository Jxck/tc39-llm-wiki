# 106th TC39 Meeting (2025-02)

- **Meeting**: 106th meeting of Ecma TC39
- **Dates**: 2025-02-18 to 2025-02-20 (10:00-17:00 PST on days 1-2, 10:00-16:00 PST on day 3)
- **Location**: Seattle, WA
- **Host**: F5
- **Agenda**: [tc39/agendas 2025/02](https://github.com/tc39/agendas/blob/main/2025/02.md)

## Overview

A three-day in-person meeting in Seattle. The new chairs and facilitators group was elected by acclamation on Day 1. **[Float16Array](../../proposals/float16array.md), [Redeclarable global eval vars](../../proposals/redeclarable-global-eval-vars.md), and [RegExp Escaping](../../proposals/regexp-escaping.md) reached Stage 4**, and **[import defer](../../proposals/import-defer.md) reached Stage 3**. **[Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md) reached Stage 2.7**, and **[Thenable Curtailment](../../proposals/thenable-curtailment.md), [Math.clamp](../../proposals/math-clamp.md), and [Error.captureStackTrace](../../proposals/error-capture-stack-trace.md) reached Stage 1**, while **[Error Stack Accessor](../../proposals/error-stack-accessor.md) went straight to Stage 2**. `Number.isSafeNumeric` did not advance (consensus for Stage 1 was withheld on day 3 despite a reworked problem statement), and Limited ArrayBuffer stays at Stage 1. Consensus was also reached on normative PRs: omitting well-known RegExp symbol lookups on primitives, missing `constructor` definitions in [Explicit Resource Management](../../proposals/explicit-resource-management.md), and [Temporal](../../proposals/temporal.md)'s `PlainMonthDay` RangeError for non-ISO calendars. The decimal/measure unification got no support for merging ([Amount](../../proposals/amount.md) was renamed and scoped, with skeptics asking for a protocol-only approach), and a conditional design goal — "things should layer; new capabilities need a particular reason" — was adopted as a reference point. A lengthy meta discussion on replacing single-veto consensus ended with no rule change, only shared recognition of the problem.

## Stage transitions

| Proposal                                                                          | Transition                     | Day       |
| --------------------------------------------------------------------------------- | ------------------------------ | --------- |
| [Float16Array](../../proposals/float16array.md)                                   | 3 → 4                          | Day 1     |
| [Redeclarable global eval vars](../../proposals/redeclarable-global-eval-vars.md) | 3 → 4                          | Day 1     |
| [RegExp Escaping](../../proposals/regexp-escaping.md)                             | 3 → 4                          | Day 1     |
| [import defer](../../proposals/import-defer.md)                                   | 2.7 → 3                        | Day 1     |
| [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)                 | 2 → 2.7                        | Day 1     |
| [Thenable Curtailment](../../proposals/thenable-curtailment.md)                   | new → 1                        | Day 1     |
| [Math.clamp](../../proposals/math-clamp.md)                                       | new → 1                        | Day 1     |
| Limited ArrayBuffer                                                               | no advancement (stays Stage 1) | Day 1     |
| `Number.isSafeNumeric`                                                            | no advancement (withheld)      | Days 1, 3 |
| [Error.captureStackTrace](../../proposals/error-capture-stack-trace.md)           | new → 1                        | Day 2     |
| [Error Stack Accessor](../../proposals/error-stack-accessor.md)                   | new → 2                        | Day 2     |

## Daily summaries

- [Day 1 — 2025-02-18](2025-02-18.md)
- [Day 2 — 2025-02-19](2025-02-19.md)
- [Day 3 — 2025-02-20](2025-02-20.md)

## Attendees

From the attendees in `raw/notes/meetings/2025-02/february-18.md` (abbreviation — name — affiliation):

| Abbreviation               | Name             | Affiliation        |
| -------------------------- | ---------------- | ------------------ |
| [KG](../../people/KG.md)   | Kevin Gibbons    | F5                 |
| [KM](../../people/KM.md)   | Keith Miller     | Apple Inc          |
| [OMT](../../people/OMT.md) | Oliver Medhurst  | Invited Expert     |
| [DJM](../../people/DJM.md) | Dmitry Makhnev   | JetBrains          |
| [GCL](../../people/GCL.md) | Gus Caplan       | Deno Land Inc      |
| [DE](../../people/DE.md)   | Daniel Ehrenberg | Bloomberg          |
| [JMN](../../people/JMN.md) | Jesse Alama      | Igalia             |
| [MLS](../../people/MLS.md) | Michael Saboff   | Apple Inc          |
| [USA](../../people/USA.md) | Ujjwal Sharma    | Igalia             |
| [ACE](../../people/ACE.md) | Ashley Claymore  | Bloomberg          |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo   | Igalia             |
| [PFC](../../people/PFC.md) | Philip Chimento  | Igalia             |
| [MF](../../people/MF.md)   | Michael Ficarra  | F5                 |
| [LGH](../../people/LGH.md) | Linus Groh       | Bloomberg          |
| SHN                        | Samina Husain    | Ecma               |
| [RBN](../../people/RBN.md) | Ron Buckton      | Microsoft          |
| [KKL](../../people/KKL.md) | Kris Kowal       | Agoric             |
| MBH                        | Mikhail Barash   | Univ. of Bergen    |
| [DLM](../../people/DLM.md) | Daniel Minor     | Mozilla            |
| AKI                        | Aki Rose Braun   | Ecma International |
| LFP                        | Luis Pardo       | Microsoft          |
| [CM](../../people/CM.md)   | Chip Morningstar | Consensys          |
| [EAO](../../people/EAO.md) | Eemeli Aro       | Mozilla            |
| BLY                        | Ben Lickly       | Google             |
| [MAH](../../people/MAH.md) | Mathieu Hofman   | Agoric             |
| [SRV](../../people/SRV.md) | Sergey Rubanov   | Invited Expert     |
| [CDA](../../people/CDA.md) | Chris de Almeida | IBM                |
| [LCA](../../people/LCA.md) | Luca Casonato    | Deno               |
| IS                         | Istvan Sebestyen | Ecma International |
| [WH](../../people/WH.md)   | Waldemar Horwat  | Invited Expert     |
| [RGN](../../people/RGN.md) | Richard Gibson   | Agoric             |
| [SFC](../../people/SFC.md) | Shane F Carr     | Google             |
| [REK](../../people/REK.md) | Erik Marks       | Consensys          |
| [JGT](../../people/JGT.md) | Justin Grant     | Invited Expert     |

> Source: [tc39/notes/meetings/2025-02](https://github.com/tc39/notes/tree/main/meetings/2025-02). Dates, location, and host come from [tc39/agendas 2025/02](https://github.com/tc39/agendas/blob/main/2025/02.md).
