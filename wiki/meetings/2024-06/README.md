# 102nd TC39 Meeting (2024-06)

- **Meeting**: 102nd meeting of Ecma TC39
- **Dates**: 2024-06-11 to 2024-06-13 (10:00-17:00 EEST; day 3 until 16:00)
- **Location**: Helsinki, Finland (Aalto University)
- **Host**: Mozilla & Aalto University
- **Agenda**: [tc39/agendas 2024/06](https://github.com/tc39/agendas/blob/main/2024/06.md)

## Overview

A three-day in-person meeting in Helsinki. Nine proposals changed stage: [Promise.try](../../proposals/promise-try.md) reached **Stage 3**, while [RegExp.escape](../../proposals/regexp-escaping.md) (character escapes kept after a dead-heat temperature check), [import defer](../../proposals/import-defer.md), [Joint Iteration](../../proposals/joint-iteration.md) (`zipToArrays` renamed `zip`, one string-valued `mode` option instead of two booleans, no implicit string iteration) and [Atomics.pause](../../proposals/atomics-pause.md) (renamed from microwait, going straight to 2.7 with no recorded Stage 2) reached **Stage 2.7**. [Iterator Sequencing](../../proposals/iterator-sequencing.md), [Error.isError](../../proposals/error-is-error.md), [ESM Phase Imports](../../proposals/esm-phase-imports.md) and [Discard bindings](../../proposals/discard-bindings.md) entered **Stage 2**. [Decimal](../../proposals/decimal.md) did not advance: [JHD](../../people/JHD.md) blocked, arguing the object form does not carry its weight without primitives, and Agoric was unwilling given the contention. [Temporal](../../proposals/temporal.md) shrank by consensus - 96 of ~300 functions removed (custom calendars and custom time zones among them) plus two normative fixes - while removing `subtract()`/`since()` failed and [JHD](../../people/JHD.md)'s push to send it back to 2.7 found no consensus. Approved needs-consensus and normative work: the ECMA-402 time zone ID PR (#877), the base64 partial-write-on-error change and `omitPadding` option, the revised Trusted Types eval host hook, [Explicit Resource Management](../../proposals/explicit-resource-management.md)'s await-collapse PR #219, and an [Intl.DurationFormat](../../proposals/intl-durationformat.md) digital-clock grouping fix. The Secretary's report covered ECMA-262 15th / ECMA-402 11th heading to the June GA, TC54 (SBOM) nearing approval, a proposed TC55 (runtime) with W3C, and a Prince-based spec PDF pipeline. No advancement was sought by [Signals](../../proposals/signals.md) (algorithms deep-dive), [Shared structs](../../proposals/shared-structs.md) (methods impasse with [MM](../../people/MM.md)), TG4 sourcemaps, smart units, or cancellation; the Nova engine talk was informational, and the proposal scrub produced no stage changes.

## Stage transitions

| Proposal                                                      | Transition                                                                | Day   |
| ------------------------------------------------------------- | ------------------------------------------------------------------------- | ----- |
| [Promise.try](../../proposals/promise-try.md)                 | 2.7 → 3                                                                   | Day 1 |
| [RegExp.escape](../../proposals/regexp-escaping.md)           | 2 → 2.7                                                                   | Day 1 |
| [import defer](../../proposals/import-defer.md)               | 2 → 2.7                                                                   | Day 1 |
| [Iterator Sequencing](../../proposals/iterator-sequencing.md) | 1 → 2                                                                     | Day 1 |
| [Error.isError](../../proposals/error-is-error.md)            | 1 → 2                                                                     | Day 1 |
| [Joint Iteration](../../proposals/joint-iteration.md)         | 2 → 2.7                                                                   | Day 2 |
| [ESM Phase Imports](../../proposals/esm-phase-imports.md)     | 1 → 2                                                                     | Day 3 |
| [Discard bindings](../../proposals/discard-bindings.md)       | 1 → 2                                                                     | Day 3 |
| [Atomics.pause](../../proposals/atomics-pause.md)             | 1 → 2.7                                                                   | Day 3 |
| [Decimal](../../proposals/decimal.md)                         | no advancement (stays at Stage 1; [JHD](../../people/JHD.md) block)       | Day 3 |
| [Temporal](../../proposals/temporal.md)                       | no stage change (scope reduction; `subtract()`/`since()` removals failed) | Day 2 |

## Daily summaries

- [Day 1 — 2024-06-11](2024-06-11.md)
- [Day 2 — 2024-06-12](2024-06-12.md)
- [Day 3 — 2024-06-13](2024-06-13.md)

## Attendees

From the attendees in `raw/notes/meetings/2024-06/june-11.md` (abbreviation — name — affiliation):

| Abbreviation               | Name              | Affiliation        |
| -------------------------- | ----------------- | ------------------ |
| [KM](../../people/KM.md)   | Keith Miller      | Apple Inc          |
| [ACE](../../people/ACE.md) | Ashley Claymore   | Bloomberg          |
| [JMN](../../people/JMN.md) | Jesse Alama       | Igalia             |
| [WH](../../people/WH.md)   | Waldemar Horwat   | Invited Expert     |
| [JWS](../../people/JWS.md) | Jason Williams    | Bloomberg          |
| [DE](../../people/DE.md)   | Daniel Ehrenberg  | Bloomberg          |
| [DMM](../../people/DMM.md) | Duncan MacGregor  | ServiceNow         |
| BSH                        | Bradford C Smith  | Google             |
| BEL                        | Agata Belkius     | Bloomberg          |
| [SRV](../../people/SRV.md) | Sergey Rubanov    | Invited Expert     |
| [MAG](../../people/MAG.md) | Matthew Gaudet    | Mozilla            |
| [RGN](../../people/RGN.md) | Richard Gibson    | Agoric             |
| [CDA](../../people/CDA.md) | Chris de Almeida  | IBM                |
| [DLM](../../people/DLM.md) | Daniel Minor      | Mozilla            |
| [CM](../../people/CM.md)   | Chip Morningstar  | Consensys          |
| [PFC](../../people/PFC.md) | Philip Chimento   | Igalia             |
| [MLS](../../people/MLS.md) | Michael Saboff    | Apple Inc          |
| MBH                        | Mikhail Barash    | Uni. Bergen        |
| [JGT](../../people/JGT.md) | Justin Grant      | Invited Expert     |
| CHU                        | Christian Ulbrich | Zalari GmbH        |
| TKP                        | Tom Kopp          | Zalari GmbH        |
| DEN                        | David Enke        | Zalari GmbH        |
| [SFC](../../people/SFC.md) | Shane F Carr      | Google             |
| [CZW](../../people/CZW.md) | Chengzhong Wu     | Bloomberg          |
| SHN                        | Samina Husain     | Ecma International |
| [JHD](../../people/JHD.md) | Jordan Harband    | HeroDevs           |
| JKP                        | Jonathan Kuperman | Bloomberg          |
| IS                         | Istvan Sebestyen  | Ecma International |
| AKI                        | Aki Rose Braun    | Ecma International |
| RCA                        | Romulo Cintra     | Igalia             |
| LUC                        | Luca Casonato     | Deno               |
