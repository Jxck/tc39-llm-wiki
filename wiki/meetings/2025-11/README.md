# 111th TC39 Meeting (2025-11)

- **Meeting**: 111th meeting of Ecma TC39
- **Dates**: 2025-11-18 to 2025-11-20
- **Location**: Tokyo, Japan
- **Host**: Bloomberg
- **Agenda**: [tc39/agendas 2025/11](https://github.com/tc39/agendas/blob/main/2025/11.md)

## Overview

Three in-person days at Bloomberg's Tokyo office (43 people signed up). **Intl Locale Info API** and **Iterator Sequencing** reached Stage 4, and **[Joint Iteration](../../proposals/joint-iteration.md) advanced to Stage 3**. **[await dictionary](../../proposals/await-dictionary.md)** reached **Stage 2.7** without passing through Stage 2, and **Import Text** advanced through Stage 1 and Stage 2, and conditionally to Stage 2.7. **Intl Unit Protocol**, **Intl Energy Units**, and **`Object.getNonIndexStringProperties`** were new at Stage 1. **TypedArray Concatenation** and **TypedArray Find Within** were conditional Stage 1, conditional on creating a dedicated repository. **`Object.propertyCount`** was split from `Object.keysLength`, and only the latter advanced to Stage 2. **export defer** (Stage 2.7 did not pass), **Declarations in Conditionals** (continued through Day Three and still unsettled), **Class spread syntax**, and **Class field introspection** (both still Stage 0, with concerns from [CM](../../people/CM.md) / [WH](../../people/WH.md) and from [MM](../../people/MM.md) / [GCL](../../people/GCL.md) / [JSL](../../people/JSL.md)) did not advance. **[Decorators](../../proposals/decorators.md)** had insufficient test262 coverage and disagreed implementation plans across V8, JSC, and SpiderMonkey reported, and stayed at Stage 2.7. **[Intl Era Monthcode](../../proposals/intl-era-month-code.md)** approved two normative changes and deferred the Stage 3 decision to January 2026. **[Amount](../../proposals/amount.md)** stayed at Stage 1, with the scope pulled back toward unit conversion. The choice of comparator for **Composites** got support, across two TCQ temperature checks, for interning and for throwing when inserting into a leaked WeakMap, but there was no formal stage request.

## Stage transitions

| Proposal                                                | Transition                                      | Day   |
| ------------------------------------------------------- | ----------------------------------------------- | ----- |
| Intl Locale Info API                                    | 3 → 4                                           | Day 1 |
| Iterator Sequencing                                     | 3 → 4                                           | Day 1 |
| [Joint Iteration](../../proposals/joint-iteration.md)   | 2 → 3                                           | Day 1 |
| [await dictionary](../../proposals/await-dictionary.md) | 2 → 2.7                                         | Day 1 |
| Import Text                                             | 1 → 2                                           | Day 1 |
| Import Text                                             | 2 → 2.7 (conditional on test262 and review)     | Day 1 |
| Intl Unit Protocol                                      | new → 1                                         | Day 1 |
| TypedArray Concatenation                                | new → 1 (conditional on a dedicated repository) | Day 1 |
| TypedArray Find Within                                  | new → 1 (conditional on a dedicated repository) | Day 1 |
| [Iterator Join](../../proposals/iterator-join.md)       | 2.7 → 3                                         | Day 2 |
| `Object.keysLength`                                     | 1 → 2                                           | Day 2 |
| Intl Energy Units                                       | new → 1                                         | Day 3 |
| `Object.getNonIndexStringProperties`                    | new → 1                                         | Day 3 |

## Daily summaries

- [Day 1 — 2025-11-18](2025-11-18.md)
- [Day 2 — 2025-11-19](2025-11-19.md)
- [Day 3 — 2025-11-20](2025-11-20.md)

## Attendees

From the attendees in `raw/notes/meetings/2025-11/november-18.md` (abbreviation — name — affiliation):

| Abbreviation               | Name                 | Affiliation        |
| -------------------------- | -------------------- | ------------------ |
| [WH](../../people/WH.md)   | Waldemar Horwat      | Invited Expert     |
| [RGN](../../people/RGN.md) | Richard Gibson       | Agoric             |
| JKG                        | Josh Goldberg        | Invited Expert     |
| RBR                        | Ruben Bridgewater    | Invited Expert     |
| [DJM](../../people/DJM.md) | Dmitry Makhnev       | JetBrains          |
| [FYT](../../people/FYT.md) | Frank Yung-Fong Tang | Google             |
| AFU                        | Anthony Fu           | Vercel             |
| [JSL](../../people/JSL.md) | James M Snell        | Cloudflare         |
| [DLM](../../people/DLM.md) | Daniel Minor         | Mozilla            |
| JKP                        | Jonathan Kuperman    | Bloomberg          |
| CHU                        | Christian Ulbrich    | Zalari             |
| AIS                        | Marina Aisa          | Apple              |
| MAE                        | Martin Alvarez       | Huawei             |
| [ACE](../../people/ACE.md) | Ashley Claymore      | Bloomberg          |
| ABO                        | Andreu Botella       | Igalia             |
| [DRO](../../people/DRO.md) | Devin Rousso         | Invited Expert     |
| JAD                        | Jake Archibald       | Mozilla            |
| [LVU](../../people/LVU.md) | Lea Verou            | OpenJS             |
| [MAH](../../people/MAH.md) | Mathieu Hofman       | Agoric             |
| CLA                        | Caio Lima            | Igalia             |
| YSZ                        | Yusuke Suzuki        | Apple              |
| [CM](../../people/CM.md)   | Chip Morningstar     | Consensys          |
| AKI                        | Aki Rose Braun       | Ecma International |
| [PFC](../../people/PFC.md) | Philip Chimento      | Igalia             |
| [EAO](../../people/EAO.md) | Eemeli Aro           | Mozilla            |
| MBH                        | Mikhail Barash       | Univ. of Bergen    |
| [KM](../../people/KM.md)   | Keith Miller         | Apple              |
| RKG                        | Ross Kirsling        | Sony               |
| [CDA](../../people/CDA.md) | Chris de Almeida     | IBM                |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo       | Igalia             |
| [RBN](../../people/RBN.md) | Ron Buckton          | F5                 |
| [SFC](../../people/SFC.md) | Shane F Carr         | Google             |
| IS                         | Istvan Sebestyen     | Ecma               |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser   | Microsoft          |
| [SHS](../../people/SHS.md) | Stephen Hicks        | Google             |
| [USA](../../people/USA.md) | Ujjwal Sharma        | Igalia             |
| [GB](../../people/GB.md)   | Guy Bedford          | Cloudflare         |
| CZW                        | Chengzhong Wu        | Bloomberg          |
| [GCL](../../people/GCL.md) | Gus Caplan           | Deno               |
| [JHD](../../people/JHD.md) | Jordan Harband       | Socket             |
| [JRL](../../people/JRL.md) | Justin Ridgewell     | Google             |
| [KG](../../people/KG.md)   | Kevin Gibbons        | F5                 |
| [MF](../../people/MF.md)   | Michael Ficarra      | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller       | Agoric             |
| [OFR](../../people/OFR.md) | Olivier Flückiger    | Google             |
| [RPR](../../people/RPR.md) | Rob Palmer           | Bloomberg          |

> Source: [tc39/notes/meetings/2025-11](https://github.com/tc39/notes/tree/main/meetings/2025-11). Dates and the overview come from [tc39/agendas 2025/11](https://github.com/tc39/agendas/blob/main/2025/11.md) and each day's transcript.
