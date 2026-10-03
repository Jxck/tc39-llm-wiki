# 115th TC39 Meeting (2026-07)

- **Meeting**: 115th meeting of Ecma TC39
- **Dates**: 2026-07-20 to 2026-07-22 (3 days)
- **Location**: remote (the next meeting was announced as onsite/hybrid in Tokyo, at Sony Interactive Entertainment in Shinagawa)
- **Host**: — (no host company; this was a remote meeting)
- **Agenda**: [tc39/agendas 2026/07](https://github.com/tc39/agendas/blob/main/2026/07.md)

## Overview

A three-day remote meeting centered on ECMA-262 / ECMA-402 proposals. **[Await Dictionary](../../proposals/await-dictionary.md) (`Promise.allKeyed` / `allSettledKeyed`) reached Stage 3**, **[Thenable Curtailment](../../proposals/thenable-curtailment.md) reached Stage 2.7** once the host hook was in place, **[Error code property](../../proposals/error-code-property.md) and [Fused Multiply-Add](../../proposals/fused-multiply-add.md) (`Math.fma`) reached Stage 2** (Fused Multiply-Add went from new to Stage 2 via Stage 1 in one session), and **bigint-from-exponential (converted from a needs-consensus PR), [Map take](../../proposals/map-get-and-delete.md) (to be renamed `getAndDelete`), [Linear Matching](../../proposals/linear-matching.md) (ReDoS mitigation), and `Intl.DateTimeFormat` Alignment With Other Standards reached Stage 1**. Declarations in Conditionals did not advance; alignment with pattern matching is still open.

On the normative side, the committee reached consensus on making `Promise.try` use PromiseResolve in the non-error case, requiring hosts that provide a custom global object to allow initializing built-ins on it (PR #3728), an [Import Defer](../../proposals/import-defer.md) cycle-root bugfix, and four ECMA-402 [Intl Locale Info](../../proposals/intl-locale-info.md) PRs. At the Ecma General Assembly on 30 June, **ECMA-262 17th / ECMA-402 13th (= ES2026) were approved unanimously**, and [KG](../../people/KG.md) received the Ecma Recognition Award. Other notable threads were [MF](../../people/MF.md)'s plan for structured proposal and delegate data (`@tc39/data`), Composites pivoting to interning, and [Decimal](../../proposals/decimal.md) stuck between an object API and a primitive.

## Stage transitions

| Proposal                                                                     | Transition                                                                 | Day   |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----- |
| [Await Dictionary](../../proposals/await-dictionary.md)                      | 2.7 → 3                                                                    | Day 1 |
| bigint-from-exponential                                                      | new → 1 (converted from needs-consensus PR #3857)                          | Day 1 |
| [Error code property](../../proposals/error-code-property.md)                | 1 → 2 (alignment with DOMException is a condition for further advancement) | Day 2 |
| [Map take](../../proposals/map-get-and-delete.md) (rename to `getAndDelete`) | new → 1                                                                    | Day 2 |
| Declarations in Conditionals                                                 | no advancement (needs alignment with pattern matching)                     | Day 2 |
| [Thenable Curtailment](../../proposals/thenable-curtailment.md)              | 2 → 2.7                                                                    | Day 3 |
| [Fused Multiply-Add](../../proposals/fused-multiply-add.md) (`Math.fma`)     | new → 1 → 2                                                                | Day 3 |
| [Linear Matching](../../proposals/linear-matching.md)                        | new → 1                                                                    | Day 3 |
| `Intl.DateTimeFormat` Alignment With Other Standards                         | new → 1                                                                    | Day 3 |

## Daily summaries

- [Day 1 — 2026-07-20](2026-07-20.md)
- [Day 2 — 2026-07-21](2026-07-21.md)
- [Day 3 — 2026-07-22](2026-07-22.md)

## Attendees

From the attendees in `raw/notes/meetings/2026-07/july-20.md` (abbreviation — name — affiliation; duplicate rows merged, first affiliation kept):

| Abbreviation               | Name                | Affiliation        |
| -------------------------- | ------------------- | ------------------ |
| [DJM](../../people/DJM.md) | Dmitry Makhnev      | JetBrains          |
| [WH](../../people/WH.md)   | Waldemar Horwat     | Invited Expert     |
| BSH                        | Bradford C. Smith   | Google             |
| [LVU](../../people/LVU.md) | Lea Verou           | OpenJS             |
| [KM](../../people/KM.md)   | Keith Miller        | Apple Inc          |
| [ACE](../../people/ACE.md) | Ashley Claymore     | Bloomberg          |
| AKI                        | Aki Rose Braun      | Ecma International |
| [LGH](../../people/LGH.md) | Linus Groh          | Bloomberg          |
| IS                         | Istvan Sebestyen    | Ecma International |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo      | Igalia             |
| [PFC](../../people/PFC.md) | Philip Chimento     | Igalia             |
| [CM](../../people/CM.md)   | Chip Morningstar    | Consensys          |
| [USA](../../people/USA.md) | Ujjwal Sharma       | Igalia             |
| [EAO](../../people/EAO.md) | Eemeli Aro          | Mozilla            |
| [CLA](../../people/CLA.md) | Caio Lima           | Igalia             |
| [OFR](../../people/OFR.md) | Olivier Flückiger   | Google             |
| NPU                        | Nikolaos Papaspyrou | Google             |
| [CDA](../../people/CDA.md) | Chris de Almeida    | IBM                |
| [RGN](../../people/RGN.md) | Richard Gibson      | Agoric             |
| [JSL](../../people/JSL.md) | James Snell         | Cloudflare         |
| [GB](../../people/GB.md)   | Guy Bedford         | Cloudflare         |
| [DRO](../../people/DRO.md) | Devin Rousso        | Invited Expert     |
| SHN                        | Samina Husain       | Ecma International |
| LPR                        | Luna Pfeiffer       | Invited Expert     |
| [DLM](../../people/DLM.md) | Dan Minor           | Mozilla Foundation |
| [JRL](../../people/JRL.md) | Justin Ridgewell    | Google             |
| [KG](../../people/KG.md)   | Kevin Gibbons       | Invited Expert     |
| [MF](../../people/MF.md)   | Michael Ficarra     | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller      | Agoric             |
| PKA                        | Peter Klecha        | Bloomberg LP       |
| [SHS](../../people/SHS.md) | Stephen Hicks       | Google             |

> Source: [tc39/notes/meetings/2026-07](https://github.com/tc39/notes/tree/main/meetings/2026-07). Dates and the overview come from [tc39/agendas 2026/07](https://github.com/tc39/agendas/blob/main/2026/07.md) and each day's transcript.
