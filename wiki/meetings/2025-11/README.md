# 111th TC39 Meeting (2025-11)

- **Meeting**: 111th meeting of Ecma TC39
- **Dates**: 2025-11-18 to 2025-11-20 (3 days)
- **Location**: Tokyo, Japan (in person, with remote participation over Zoom)
- **Host**: Bloomberg (Tokyo office)
- **Agenda**: [tc39/agendas 2025/11](https://github.com/tc39/agendas/blob/main/2025/11.md)

## Overview

A three-day in-person meeting at Bloomberg in Tokyo (43 sign-ups, against 25 two years earlier), with heavy agenda overflow. The closing tally was "at least 12 proposals advanced". **[JSON.parse source text access](../../proposals/json-source-text.md), [Intl Locale Info](../../proposals/intl-locale-info.md) and [Iterator Sequencing](../../proposals/iterator-sequencing.md) reached Stage 4**, and **[Joint Iteration](../../proposals/joint-iteration.md) reached Stage 3**. **[Await Dictionary](../../proposals/await-dictionary.md)** went from Stage 1 straight to 2.7, the new **[Iterator Join](../../proposals/iterator-join.md)** went to 2.7 in one session, and the new **[Import Text](../../proposals/import-text.md)** got Stage 1 and 2 plus a conditional 2.7. **[Error.captureStackTrace](../../proposals/error-capture-stack-trace.md)** and a split-out `Object.keysLength` / `keyCount` reached Stage 2. **[Intl Unit Protocol](../../proposals/intl-unit-protocol.md), [Intl Energy Units](../../proposals/intl-energy-units.md), [TypedArray Concatenation](../../proposals/typedarray-concat.md) and [TypedArray Find Within](../../proposals/typedarray-find-within.md)** (the last two conditionally) reached Stage 1.

Things that did not advance: export defer (2.7), Declarations in Conditionals (Stage 2 needs spec semantics, and the else-scope question is forced by `using`), [Comparisons](../../proposals/comparisons.md), class spread syntax, and class field introspection (all stay at Stage 0). On the normative side, the committee approved the ECMA-262 / ECMA-402 copyright corrigenda by vote, an `Intl.PluralRules` `compactDisplay` fix, the ambiguous-binding fix for re-exported namespaces, a [Temporal](../../proposals/temporal.md) `Duration` rounding fix (PR #3172), and two [Intl Era/Month Code](../../proposals/intl-era-month-code.md) changes (Stage 3 deferred to January).

Discussion topics included the following:

- [Amount](../../proposals/amount.md) returning to a model with arithmetic and unit conversion.
- Interning for Composites, which won non-binding temperature checks.
- [Decorators](../../proposals/decorators.md) (Stage 3) stalled, with sparse test262 coverage and browsers each waiting for others to ship.
- The WHATWG stage process.
- Spec-defined vs implementation-defined limits.
- Module-declaration-like proposals elsewhere on the web.

## Daily summaries

- [Day 1 — 2025-11-18](2025-11-18.md)
- [Day 2 — 2025-11-19](2025-11-19.md)
- [Day 3 — 2025-11-20](2025-11-20.md)

## Stage transitions

| Proposal                                                                                        | Transition                                                                                                                 | Day   |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----- |
| [JSON.parse source text access](../../proposals/json-source-text.md)                            | 3 → 4                                                                                                                      | Day 1 |
| [Intl Locale Info](../../proposals/intl-locale-info.md)                                         | 3 → 4 (after merging PR 92)                                                                                                | Day 1 |
| [Iterator Sequencing](../../proposals/iterator-sequencing.md)                                   | 3 → 4                                                                                                                      | Day 1 |
| [Joint Iteration](../../proposals/joint-iteration.md)                                           | 2.7 → 3                                                                                                                    | Day 1 |
| [Await Dictionary](../../proposals/await-dictionary.md)                                         | 1 → 2.7 (skipping Stage 2)                                                                                                 | Day 1 |
| [Error.captureStackTrace](../../proposals/error-capture-stack-trace.md)                         | 1 → 2                                                                                                                      | Day 1 |
| [Import Text](../../proposals/import-text.md)                                                   | new → 2 (Stage 1 and 2 in one session), plus conditional 2.7 pending [SFC](../../people/SFC.md)'s confirmation on encoding | Day 1 |
| [Intl Unit Protocol](../../proposals/intl-unit-protocol.md)                                     | new → 1                                                                                                                    | Day 1 |
| [TypedArray Concatenation](../../proposals/typedarray-concat.md)                                | new → 1 (conditional on creating the repository)                                                                           | Day 1 |
| [TypedArray Find Within](../../proposals/typedarray-find-within.md)                             | new → 1 (conditional on creating the repository)                                                                           | Day 1 |
| export defer                                                                                    | no advancement (2.7 not reached; stays at 2)                                                                               | Day 1 |
| Declarations in Conditionals                                                                    | no advancement (Stage 2 needs spec work)                                                                                   | Day 1 |
| [Iterator Join](../../proposals/iterator-join.md)                                               | new → 2.7 (Stage 1, 2 and 2.7 in one session)                                                                              | Day 2 |
| `Object.keysLength` / `keyCount`                                                                | new → 2 (split out of [Object.propertyCount](../../proposals/object-propertycount.md), which stays at 1)                   | Day 2 |
| [Comparisons](../../proposals/comparisons.md)                                                   | no advancement (stays at 0)                                                                                                | Day 2 |
| [Intl Energy Units](../../proposals/intl-energy-units.md)                                       | new → 1                                                                                                                    | Day 3 |
| [Object.getNonIndexStringProperties](../../proposals/object-get-non-index-string-properties.md) | 1 (recorded as advancing to Stage 1 under the new name; Stage 1 since 2025-07 as `Array.getNonIndexStringProperties`)      | Day 3 |
| Class spread syntax                                                                             | no advancement (stays at 0)                                                                                                | Day 3 |
| Class field introspection                                                                       | no advancement (stays at 0)                                                                                                | Day 3 |

## Attendees

From the attendee table at the start of each day (union of the three days, unordered): [RPR](../../people/RPR.md), [CDA](../../people/CDA.md), [USA](../../people/USA.md) (chairs), [DLM](../../people/DLM.md), [JRL](../../people/JRL.md) (facilitators), AKI, IS, SHN (Ecma), [WH](../../people/WH.md), [RGN](../../people/RGN.md), JKG, [RBR](../../people/RBR.md), [DJM](../../people/DJM.md), [FYT](../../people/FYT.md), AFU, [JSL](../../people/JSL.md), JKP, CHU, AIS, MAE, [ACE](../../people/ACE.md), [ABO](../../people/ABO.md), [DRO](../../people/DRO.md), [JAD](../../people/JAD.md), [LVU](../../people/LVU.md), [MAH](../../people/MAH.md), [CLA](../../people/CLA.md), [YSZ](../../people/YSZ.md), [CM](../../people/CM.md), [PFC](../../people/PFC.md), [EAO](../../people/EAO.md), MBH, [KM](../../people/KM.md), [RKG](../../people/RKG.md), [NRO](../../people/NRO.md), [RBN](../../people/RBN.md), [SFC](../../people/SFC.md), [DRR](../../people/DRR.md), [SHS](../../people/SHS.md), [GB](../../people/GB.md), [CZW](../../people/CZW.md), [GCL](../../people/GCL.md), [JHD](../../people/JHD.md), [KG](../../people/KG.md), [MF](../../people/MF.md), [MM](../../people/MM.md), [OFR](../../people/OFR.md), [MAG](../../people/MAG.md), [JSH](../../people/JSH.md), [JMN](../../people/JMN.md), [BAN](../../people/BAN.md).
