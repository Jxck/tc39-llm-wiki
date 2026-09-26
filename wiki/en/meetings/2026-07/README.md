# 115th TC39 Meeting (2026-07)

- **Meeting**: 115th meeting of Ecma TC39
- **Dates**: 2026-07-20 to 2026-07-22 (3 days)
- **Location**: remote (the next meeting was announced as onsite/hybrid in Tokyo, at Sony Interactive Entertainment in Shinagawa)
- **Host**: — (no host company; this was a remote meeting)
- **Agenda**: [tc39/agendas 2026/07](https://github.com/tc39/agendas/blob/main/2026/07.md)

## Overview

A three-day remote meeting centered on ECMA-262 / ECMA-402 proposals. **[Await Dictionary](../../proposals/await-dictionary.md) (`Promise.allKeyed` / `allSettledKeyed`) reached Stage 3**, **[Thenable Curtailment](../../proposals/thenable-curtailment.md) reached Stage 2.7** once the host hook was in place, **[Error code property](../../proposals/error-code-property.md) and [Fused Multiply-Add](../../proposals/fused-multiply-add.md) (`Math.fma`) reached Stage 2**, and **bigint-from-exponential (converted from a needs-consensus PR), [Map take](../../proposals/map-get-and-delete.md) (to be renamed `getAndDelete`), [Linear Matching](../../proposals/linear-matching.md) (ReDoS mitigation), and `Intl.DateTimeFormat` Alignment With Other Standards reached Stage 1**. Declarations in Conditionals did not advance; alignment with pattern matching is still open.

On the normative side, the committee reached consensus on making `Promise.try` use PromiseResolve in the non-error case, requiring hosts that provide a custom global object to allow initializing built-ins on it (PR #3728), an Import Defer cycle-root bugfix, and four ECMA-402 Intl Locale Info PRs. At the Ecma General Assembly on 30 June, **ECMA-262 17th / ECMA-402 13th (= ES2026) were approved unanimously**, and [KG](../../people/KG.md) received the Ecma Recognition Award. Other notable threads were [MF](../../people/MF.md)'s plan for structured proposal and delegate data (`@tc39/data`), Composites pivoting to interning, and Decimal stuck between an object API and a primitive.

## Daily summaries

- [Day 1 — 2026-07-20](2026-07-20.md)
- [Day 2 — 2026-07-21](2026-07-21.md)
- [Day 3 — 2026-07-22](2026-07-22.md)

## Stage transitions

| Proposal                                                                     | Transition                                                                 | Day   |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----- |
| [Await Dictionary](../../proposals/await-dictionary.md)                      | 2.7 → 3                                                                    | Day 1 |
| [Thenable Curtailment](../../proposals/thenable-curtailment.md)              | 2 → 2.7                                                                    | Day 3 |
| [Error code property](../../proposals/error-code-property.md)                | 1 → 2 (alignment with DOMException is a condition for further advancement) | Day 2 |
| [Fused Multiply-Add](../../proposals/fused-multiply-add.md) (`Math.fma`)     | 1 → 2                                                                      | Day 3 |
| bigint-from-exponential                                                      | new → 1 (converted from needs-consensus PR #3857)                          | Day 1 |
| [Map take](../../proposals/map-get-and-delete.md) (rename to `getAndDelete`) | new → 1                                                                    | Day 2 |
| [Linear Matching](../../proposals/linear-matching.md)                        | new → 1                                                                    | Day 3 |
| `Intl.DateTimeFormat` Alignment With Other Standards                         | new → 1                                                                    | Day 3 |
| Declarations in Conditionals                                                 | no advancement (needs alignment with pattern matching)                     | Day 2 |

## Attendees

From the attendee table at the start of each day (union of the three days, unordered): [CDA](../../people/CDA.md), [USA](../../people/USA.md), [JRL](../../people/JRL.md), [DLM](../../people/DLM.md) (chairs/facilitators), [WH](../../people/WH.md), BSH, [LVU](../../people/LVU.md), [KM](../../people/KM.md), [ACE](../../people/ACE.md), AKI, LGH, IS, [NRO](../../people/NRO.md), [PFC](../../people/PFC.md), [CM](../../people/CM.md), [EAO](../../people/EAO.md), CLA, [OFR](../../people/OFR.md), NPU, [RGN](../../people/RGN.md), [JSL](../../people/JSL.md), [GB](../../people/GB.md), [DRO](../../people/DRO.md), SHN, LPR, [KG](../../people/KG.md), [MF](../../people/MF.md), [MM](../../people/MM.md), PKA, [SHS](../../people/SHS.md), [DJM](../../people/DJM.md), [JHD](../../people/JHD.md), [MAG](../../people/MAG.md), [SFC](../../people/SFC.md), [AUR](../../people/AUR.md), [CPC](../../people/CPC.md), and others.
