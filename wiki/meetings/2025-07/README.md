# 109th TC39 Meeting (2025-07)

- **Meeting**: 109th meeting of Ecma TC39
- **Dates**: 2025-07-28 to 2025-07-31 (remote, US Pacific time)
- **Location**: remote (the next meeting was announced as onsite in Tokyo, to be hosted by Bloomberg)
- **Host**: — (no host company; this was a remote meeting)
- **Agenda**: [tc39/agendas 2025/07](https://github.com/tc39/agendas/blob/main/2025/07.md)

## Overview

A four-day remote meeting centered on ECMA-262 / ECMA-402 proposals. **`Math.sumPrecise` and [Uint8Array base64](../../proposals/uint8array-base64.md)+hex reached Stage 4**, and **[Iterator Sequencing](../../proposals/iterator-sequencing.md), [Upsert](../../proposals/upsert.md), and [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md) reached Stage 3**. On Intl, **[Intl Era and Month Code](../../proposals/intl-era-month-code.md) and [Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md) reached Stage 2.7**, and **[Amount](../../proposals/amount.md) (formerly Measure) did not reach Stage 2** because of [WH](../../people/WH.md)'s concern about non-finite values. [Import Buffer](../../proposals/import-bytes.md) was newly proposed for Stage 1 and went straight through to Stage 2 (changed to `Uint8Array` + `type: "bytes"`). [Module Import Hook and new Global](../../proposals/module-global.md) obtained Stage 1 after the problem statement was revised. Advancement of `Object.propertyCount` and `Array.isSparse` did not pass, because of objections (`Array.getNonIndexStringProperties` and `Object.getOwnPropertySymbols` options reached Stage 1). Consensus was also reached on normative PRs including a TypedArray copyWithin fix, unifying the order of module-evaluation promises, and changing the order of [Temporal](../../proposals/temporal.md) option processing. It was also agreed to write a "write your own comments" rule against LLM-generated comments into `AI_policy.md`.

## Stage transitions

| Proposal                                                                | Transition                                   | Day      |
| ----------------------------------------------------------------------- | -------------------------------------------- | -------- |
| `Math.sumPrecise`                                                       | 3 → 4                                        | Day 1    |
| [Uint8Array base64](../../proposals/uint8array-base64.md)+hex           | 3 → 4                                        | Day 1    |
| [Iterator Sequencing](../../proposals/iterator-sequencing.md)           | 2.7 → 3                                      | Day 1    |
| [Upsert](../../proposals/upsert.md)                                     | 2.7 → 3                                      | Day 1    |
| [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)       | 2.7 → 3 (conditional on test262 PRs merging) | Day 2    |
| [Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md) | 1 → 2                                        | Day 2    |
| Intl Keep Trailing Zeros                                                | 2 → 2.7                                      | Day 3    |
| [Amount](../../proposals/amount.md)                                     | no advancement (did not reach Stage 2)       | Days 2-3 |
| [Intl Era and Month Code](../../proposals/intl-era-month-code.md)       | 2 → 2.7 (conditional on editor review)       | Day 3    |
| [Import Buffer](../../proposals/import-bytes.md)                        | new → 2                                      | Day 3    |
| [Module Import Hook and new Global](../../proposals/module-global.md)   | new → 1                                      | Day 3    |
| `Object.propertyCount`                                                  | 1 → 2 (did not pass)                         | Day 4    |
| `Array.isSparse`                                                        | new → 1 (did not pass)                       | Day 4    |
| `Array.getNonIndexStringProperties`                                     | new → 1                                      | Day 4    |
| `Object.getOwnPropertySymbols` options                                  | new → 1                                      | Day 4    |

## Daily summaries

- [Day 1 — 2025-07-28](2025-07-28.md)
- [Day 2 — 2025-07-29](2025-07-29.md)
- [Day 3 — 2025-07-30](2025-07-30.md)
- [Day 4 — 2025-07-31](2025-07-31.md)

## Attendees

From the attendees in `raw/notes/meetings/2025-07/july-28.md` (abbreviation — name — affiliation):

| Abbreviation               | Name                   | Affiliation        |
| -------------------------- | ---------------------- | ------------------ |
| [JMN](../../people/JMN.md) | Jesse Alama            | Igalia             |
| [DJM](../../people/DJM.md) | Dmitry Makhnev         | JetBrains          |
| [WH](../../people/WH.md)   | Waldemar Horwat        | Invited Expert     |
| [GB](../../people/GB.md)   | Guy Bedford            | Cloudflare         |
| [DLM](../../people/DLM.md) | Daniel Minor           | Mozilla            |
| [ZTZ](../../people/ZTZ.md) | Zbyszek Tenerowicz     | Consensys          |
| [JHD](../../people/JHD.md) | Jordan Harband         | HeroDevs           |
| [SRV](../../people/SRV.md) | Sergey Rubanov         | Invited Expert     |
| [CM](../../people/CM.md)   | Chip Morningstar       | Consensys          |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo         | Igalia             |
| MBH                        | Mikhail Barash         | Univ. of Bergen    |
| [KM](../../people/KM.md)   | Keith Miller           | Apple Inc.         |
| AKI                        | Aki Rose Braun         | Ecma International |
| SHN                        | Samina Husain          | Ecma International |
| [OFR](../../people/OFR.md) | Olivier Flückiger      | Google             |
| [RGN](../../people/RGN.md) | Richard Gibson         | Agoric             |
| [RMH](../../people/RMH.md) | Rezvan Mahdavi Hezaveh | Google             |
| [JSC](../../people/JSC.md) | J. S. Choi             | Invited Expert     |
| [EAO](../../people/EAO.md) | Eemeli Aro             | Mozilla            |
| [TAB](../../people/TAB.md) | Tab Atkins-Bittner     | Google             |
| IS                         | Istvan Sebestyen       | Ecma               |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser     | Microsoft          |
| [ABO](../../people/ABO.md) | Andreu Botella         | Igalia             |
| [CDA](../../people/CDA.md) | Chris de Almeida       | IBM                |
| [CZW](../../people/CZW.md) | Chengzhong Wu          | Bloomberg          |
| [JRL](../../people/JRL.md) | Justin Ridgewell       | Google             |
| [KG](../../people/KG.md)   | Kevin Gibbons          | F5                 |
| [MAH](../../people/MAH.md) | Mathieu Hofman         | Agoric             |
| [MF](../../people/MF.md)   | Michael Ficarra        | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller         | Agoric             |
| [RPR](../../people/RPR.md) | Rob Palmer             | Bloomberg          |
| [SHS](../../people/SHS.md) | Stephen Hicks          | Google             |
| [USA](../../people/USA.md) | Ujjwal Sharma          | Igalia             |

> Source: [tc39/notes/meetings/2025-07](https://github.com/tc39/notes/tree/main/meetings/2025-07). Dates, location, and the overview come from [tc39/agendas 2025/07](https://github.com/tc39/agendas/blob/main/2025/07.md) and each day's transcript.
