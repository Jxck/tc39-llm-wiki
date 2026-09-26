# 110th TC39 Meeting (2025-09)

- **Meeting**: 110th meeting of Ecma TC39
- **Dates**: 2025-09-22 to 2025-09-24
- **Location**: Remote only
- **Host**: none (remote meeting. The next one, 2025-11, is planned to be hosted by Bloomberg in Tokyo)
- **Agenda**: [tc39/agendas 2025/09](https://github.com/tc39/agendas/blob/main/2025/09.md)

## Overview

Three remote days. **[Iterator Chunking](../../proposals/iterator-chunking.md) reached Stage 2.7**, **Import Bytes reached Stage 2.7**, and **Non-extensible Applies to Private reached Stage 3**. `Array.prototype.pushAll` (a defense against stack overflow), Native Promise Adoption, and Native Promise Predicate (which then also reached Stage 2) newly advanced to Stage 1. **[Amount](../../proposals/amount.md) aimed at Stage 2, but late-breaking concerns erupted — significant digits, the name, numeric conversion methods (`toNumber` / `toBigInt`), a brand check by internal slot, and others — and although the discussion continued across all three days it did not reach Stage 2, and carried over to the next Tokyo plenary.** Intl Era Month Code got consensus on normative changes (reverting leap-month overflow behavior, extending the reference-year search range) and has Stage 3 in view. [Temporal](../../proposals/temporal.md) got consensus on a normative change that fixes a sign-flip bug at a DST transition, and laid out a path to Stage 4. The committee also discussed a normative PR that adds a `[[CompactDisplay]]` slot to `Intl.PluralRules` and switches it to Intl mathematical values, raising the exponent and significant-digit limits of IntlMV (looking ahead to Decimal128), consensus on an enum kebab-case convention for `how-we-work`, and a Stage 1 update of the module-global (Compartment) proposal (the relationship to ShadowRealm was an issue).

## Daily summaries

- [Day 1 — 2025-09-22](2025-09-22.md)
- [Day 2 — 2025-09-23](2025-09-23.md)
- [Day 3 — 2025-09-24](2025-09-24.md)

## Attendees

From the attendees in `raw/notes/meetings/2025-09/september-22.md` (abbreviation — name — affiliation):

| Abbreviation               | Name               | Affiliation        |
| -------------------------- | ------------------ | ------------------ |
| [CDA](../../people/CDA.md) | Chris de Almeida   | IBM                |
| SHN                        | Samina Husain      | Ecma               |
| [KM](../../people/KM.md)   | Keith Miller       | Apple              |
| [BAN](../../people/BAN.md) | Ben Allen          | Igalia             |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo     | Igalia             |
| [DLM](../../people/DLM.md) | Daniel Minor       | Mozilla            |
| [DJM](../../people/DJM.md) | Dmitry Makhnev     | JetBrains          |
| [EAO](../../people/EAO.md) | Eemeli Aro         | Mozilla            |
| [RBN](../../people/RBN.md) | Ron Buckton        | F5                 |
| [JMN](../../people/JMN.md) | Jesse Alama        | Igalia             |
| ABO                        | Andreu Botella     | Igalia             |
| [WH](../../people/WH.md)   | Waldemar Horwat    | Invited Expert     |
| [ZTZ](../../people/ZTZ.md) | Zbyszek Tenerowicz | Consensys          |
| [MLS](../../people/MLS.md) | Michael Saboff     | Invited Expert     |
| [RGN](../../people/RGN.md) | Richard Gibson     | Agoric             |
| BSH                        | Bradford C. Smith  | Google             |
| [PFC](../../people/PFC.md) | Philip Chimento    | Igalia             |
| [CM](../../people/CM.md)   | Chip Morningstar   | Consensys          |
| MBH                        | Mikhail Barash     | Univ. of Bergen    |
| DMM                        | Duncan MacGregor   | ServiceNow         |
| [MAH](../../people/MAH.md) | Mathieu Hofman     | Agoric             |
| [JSL](../../people/JSL.md) | James Snell        | Cloudflare         |
| IS                         | Istvan Sebestyen   | Ecma               |
| REK                        | Erik Marks         | Consensys          |
| AKI                        | Aki Braun          | Ecma International |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser | Microsoft          |
| [JHD](../../people/JHD.md) | Jordan Harband     | HeroDevs           |
| [JRL](../../people/JRL.md) | Justin Ridgewell   | Google             |
| [KG](../../people/KG.md)   | Kevin Gibbons      | F5                 |
| [MF](../../people/MF.md)   | Michael Ficarra    | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller     | Agoric             |
| [OFR](../../people/OFR.md) | Olivier Flückiger  | Google             |
| RCH                        | Ryan Cavanaugh     | Microsoft          |
| [RPR](../../people/RPR.md) | Rob Palmer         | Bloomberg          |
| [SFC](../../people/SFC.md) | Shane Carr         | Google             |
| [SHS](../../people/SHS.md) | Stephen Hicks      | Google             |
| [USA](../../people/USA.md) | Ujjwal Sharma      | Igalia             |

> Source: [raw/notes/meetings/2025-09](../../../../raw/notes/meetings/2025-09/). Dates and the overview come from [tc39/agendas 2025/09](https://github.com/tc39/agendas/blob/main/2025/09.md) and each day's transcript.
