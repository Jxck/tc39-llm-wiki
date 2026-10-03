# 113th TC39 Meeting (2026-03)

- **Meeting**: 113th meeting of Ecma TC39
- **Dates**: 2026-03-10 to 2026-03-12 (the 10th and 11th are 10:00-17:00, the 12th is 10:00-16:00 EDT)
- **Location**: New York, NY (United States)
- **Host**: Google (in-room logistics by Justin Ridgewell)
- **Agenda**: [tc39/agendas 2026/03](https://github.com/tc39/agendas/blob/main/2026/03.md)

## Overview

Three days in New York centered on ECMA-262 / ECMA-402 proposals. **[Temporal](../../proposals/temporal.md) reached Stage 4** after about five years at Stage 3, and **[Intl Era/Month Code](../../proposals/intl-era-month-code.md) also reached Stage 4**. [Import Text](../../proposals/import-text.md) advanced through Stage 2.7 to Stage 3, [Error Stack Accessor](../../proposals/error-stack-accessor.md) advanced to Stage 2.7, [Iterator Includes](../../proposals/iterator-includes.md) went from new to Stage 2.7 in one session, [Intl Unit Protocol](../../proposals/intl-unit-protocol.md) and [Thenable Curtailment](../../proposals/thenable-curtailment.md) reached Stage 2, and [Error code property](../../proposals/error-code-property.md) reached Stage 1; Dynamic Import Host Adjustment was withdrawn. [RegExp Buffer Boundaries](../../proposals/regexp-buffer-boundaries.md) was blocked for insufficient review time, and [Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md) resolved two open issues without requesting advancement. The committee also heard a status update on [Explicit Resource Management](../../proposals/explicit-resource-management.md)'s conditional Stage 4, discussion items on an Abort Protocol and on Structured Concurrency (neither is a staged proposal), a test262 coverage strategy, and tree-shakeable methods. The 2026 chair group, convenors, and editors slate was unanimously approved.

## Stage transitions

| Proposal                                                        | Transition    | Day   |
| --------------------------------------------------------------- | ------------- | ----- |
| Dynamic Import Host Adjustment                                  | 2 → withdrawn | Day 1 |
| [Intl Era/Month Code](../../proposals/intl-era-month-code.md)   | 3 → 4         | Day 1 |
| [Error Stack Accessor](../../proposals/error-stack-accessor.md) | 2 → 2.7       | Day 1 |
| [Iterator Includes](../../proposals/iterator-includes.md)       | new → 2.7     | Day 1 |
| [Temporal](../../proposals/temporal.md)                         | 3 → 4         | Day 2 |
| [Import Text](../../proposals/import-text.md)                   | 2 → 2.7 → 3   | Day 2 |
| [Intl Unit Protocol](../../proposals/intl-unit-protocol.md)     | 1 → 2         | Day 2 |
| [Error code property](../../proposals/error-code-property.md)   | new → 1       | Day 2 |
| [Thenable Curtailment](../../proposals/thenable-curtailment.md) | 1 → 2         | Day 3 |

## Daily summaries

- [Day 1 — 2026-03-10](2026-03-10.md)
- [Day 2 — 2026-03-11](2026-03-11.md)
- [Day 3 — 2026-03-12](2026-03-12.md)

## Attendees

From the attendees in `raw/notes/meetings/2026-03/march-10.md` (abbreviation — name — affiliation):

| Abbreviation               | Name               | Affiliation        |
| -------------------------- | ------------------ | ------------------ |
| AKI                        | Aki Rose Braun     | Ecma International |
| [ACE](../../people/ACE.md) | Ashley Claymore    | Bloomberg          |
| [BAN](../../people/BAN.md) | Ben Allen          | Igalia             |
| [CZW](../../people/CZW.md) | Chengzhong Wu      | Bloomberg          |
| [CM](../../people/CM.md)   | Chip Morningstar   | Consensys          |
| [CDA](../../people/CDA.md) | Chris de Almeida   | IBM                |
| DLP                        | Dan Lapid          | Cloudflare         |
| [DLM](../../people/DLM.md) | Daniel Minor       | Mozilla            |
| [DJM](../../people/DJM.md) | Dmitry Makhnev     | JetBrains          |
| [EAO](../../people/EAO.md) | Eemeli Aro         | Mozilla            |
| [GB](../../people/GB.md)   | Guy Bedford        | Cloudflare         |
| IS                         | Istvan Sebestyen   | Ecma               |
| [JSL](../../people/JSL.md) | James Snell        | Cloudflare         |
| [JWS](../../people/JWS.md) | Jason Williams     | Bloomberg          |
| JPO                        | Jeffrey Posnick    | Bloomberg          |
| JSI                        | Joe Sepi           | Cloudflare         |
| JKP                        | Jonathan Kuperman  | Bloomberg          |
| [JHD](../../people/JHD.md) | Jordan Harband     | Socket             |
| [JRL](../../people/JRL.md) | Justin Ridgewell   | Google             |
| [JSC](../../people/JSC.md) | J. S. Choi         | Invited Expert     |
| [KM](../../people/KM.md)   | Keith Miller       | Apple              |
| [LVU](../../people/LVU.md) | Lea Verou          | OpenJS             |
| [LGH](../../people/LGH.md) | Linus Groh         | Bloomberg          |
| MBH                        | Mikhail Barash     | Univ. of Bergen    |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo     | Igalia             |
| [OFR](../../people/OFR.md) | Olivier Flückiger  | Google             |
| PKA                        | Peter Klecha       | Bloomberg          |
| [PFC](../../people/PFC.md) | Philip Chimento    | Igalia             |
| [RGN](../../people/RGN.md) | Richard Gibson     | Agoric             |
| [RBN](../../people/RBN.md) | Ron Buckton        | F5                 |
| [RBR](../../people/RBR.md) | Ruben Bridgewater  | Invited Expert     |
| SHN                        | Samina Husain      | Ecma International |
| [SHS](../../people/SHS.md) | Stephen Hicks      | Google             |
| [WH](../../people/WH.md)   | Waldemar Horwat    | Invited Expert     |
| [YNP](../../people/YNP.md) | Yagiz Nizipli      | Cloudflare         |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser | Microsoft          |
| [JMN](../../people/JMN.md) | Jesse Alama        | Igalia             |
| [KG](../../people/KG.md)   | Kevin Gibbons      | F5                 |
| [MF](../../people/MF.md)   | Michael Ficarra    | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller     | Agoric             |
| [RPR](../../people/RPR.md) | Rob Palmer         | Bloomberg          |
| [SFC](../../people/SFC.md) | Shane Carr         | Google             |
| [ZB](../../people/ZB.md)   | Zibi Braniecki     | —                  |

> Source: [tc39/notes/meetings/2026-03](https://github.com/tc39/notes/tree/main/meetings/2026-03). Dates, location, and the overview come from [tc39/agendas 2026/03](https://github.com/tc39/agendas/blob/main/2026/03.md) and each day's transcript.
