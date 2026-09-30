# 114th TC39 Meeting (2026-05)

- **Meeting**: 114th meeting of Ecma TC39
- **Dates**: 2026-05-19 to 2026-05-21 (the 19th and 20th are 10:00-17:00, the 21st is 10:00-16:00 CEST)
- **Location**: Amsterdam, the Netherlands
- **Host**: JetBrains (on-site logistics by Dmitry Makhnev and others)
- **Agenda**: [tc39/agendas 2026/05](https://github.com/tc39/agendas/blob/main/2026/05.md)

## Overview

Three days in Amsterdam. **Reached Stage 4**: [Joint Iteration](../../proposals/joint-iteration.md) / `Atomics.pause` ([Dynamic Code Brand Checks](../../proposals/dynamic-code-brand-checks.md) got consensus only on a normative change, and Stage 4 will be asked again next time; [Explicit Resource Management](../../proposals/explicit-resource-management.md) is finished, its conditions having been met). [Iterator Chunking](../../proposals/iterator-chunking.md), [Iterator Includes](../../proposals/iterator-includes.md), and [Error stack accessor](../../proposals/error-stack-accessor.md) advanced to Stage 3, while **[Decorators](../../proposals/decorators.md) (the main proposal) and Decorator Metadata regressed from Stage 3 to Stage 2.7**. The iterator line and the area around [decorators](../../proposals/decorators.md) were the conspicuous movement. The committee also discussed Intl ([Stable Formatting](../../proposals/stable-formatting.md) / Sequence Units / Default Behaviours), a normative PR for ESM / Source Phase Imports, web integration of [AsyncContext](../../proposals/async-context.md), and module topics including `export defer` / `export all from` / Module Scope Ceiling. Stage 1 for "[Comparisons](../../proposals/comparisons.md)" (deep comparison / deviation reporting), and a briefing on the regulatory side: the **EU CRA (Cyber Resilience Act)**.

## Stage transitions

| Proposal                                                                            | Transition | Day   |
| ----------------------------------------------------------------------------------- | ---------- | ----- |
| [Joint Iteration](../../proposals/joint-iteration.md)                               | 3 → 4      | Day 1 |
| `Atomics.pause`                                                                     | 3 → 4      | Day 1 |
| [Decorators](../../proposals/decorators.md)                                         | 3 → 2.7    | Day 1 |
| Decorator Metadata                                                                  | 3 → 2.7    | Day 1 |
| [Iterator Chunking](../../proposals/iterator-chunking.md)                           | 2.7 → 3    | Day 2 |
| [Iterator Includes](../../proposals/iterator-includes.md)                           | 2.7 → 3    | Day 2 |
| [Stable Formatting](../../proposals/stable-formatting.md)                           | 1 → 2      | Day 2 |
| [Default Behaviours for some Intl APIs](../../proposals/intl-default-behaviours.md) | new → 1    | Day 2 |
| [Intl Sequence Units](../../proposals/intl-sequence-units.md)                       | 1 → 2      | Day 2 |
| [export all from](../../proposals/export-all-from.md)                               | new → 1    | Day 2 |
| [RegExp Buffer Boundaries](../../proposals/regexp-buffer-boundaries.md)             | 2.7 → 3    | Day 3 |
| [Error stack accessor](../../proposals/error-stack-accessor.md)                     | 2.7 → 3    | Day 3 |
| [Comparisons](../../proposals/comparisons.md)                                       | new → 1    | Day 3 |

## Daily summaries

- [Day 1 — 2026-05-19](2026-05-19.md)
- [Day 2 — 2026-05-20](2026-05-20.md)
- [Day 3 — 2026-05-21](2026-05-21.md)

## Attendees

From the attendees in `raw/notes/meetings/2026-05/may-19.md` (abbreviation — name — affiliation):

| Abbreviation               | Name                   | Affiliation        |
| -------------------------- | ---------------------- | ------------------ |
| [DLM](../../people/DLM.md) | Daniel Minor           | Mozilla            |
| [USA](../../people/USA.md) | Ujjwal Sharma          | Igalia             |
| SHN                        | Samina Husain          | Ecma               |
| [CDA](../../people/CDA.md) | Chris de Almeida       | IBM                |
| [WH](../../people/WH.md)   | Waldemar Horwat        | Invited Expert     |
| GTO                        | Gustavo Tonietto       | Mozilla            |
| [ZTZ](../../people/ZTZ.md) | Zbyszek Tenerowicz     | Consensys          |
| [YSZ](../../people/YSZ.md) | Yusuke Suzuki          | Apple              |
| [DJM](../../people/DJM.md) | Dmitry Makhnev         | JetBrains          |
| LGH                        | Linus Groh             | Bloomberg          |
| [JRL](../../people/JRL.md) | Justin Ridgewell       | Google             |
| [OFR](../../people/OFR.md) | Olivier Flückiger      | Google             |
| [AUR](../../people/AUR.md) | Aurèle Barrière        | CNRS               |
| LPR                        | Luna Pfeiffer          | Yavashark          |
| [CLA](../../people/CLA.md) | Caio Lima              | Igalia             |
| [RGN](../../people/RGN.md) | Richard Gibson         | Agoric             |
| [JHD](../../people/JHD.md) | Jordan Harband         | Socket             |
| [KM](../../people/KM.md)   | Keith Miller           | Apple              |
| BSH                        | Bradford C. Smith      | Google             |
| [MAH](../../people/MAH.md) | Mathieu Hofman         | Agoric             |
| [CM](../../people/CM.md)   | Chip Morningstar       | Consensys          |
| MBH                        | Mikhail Barash         | Univ. of Bergen    |
| [RBN](../../people/RBN.md) | Ron Buckton            | F5                 |
| [RBR](../../people/RBR.md) | Ruben Bridgewater      | Datadog            |
| [GCL](../../people/GCL.md) | Gus Caplan             | Deno               |
| [OMT](../../people/OMT.md) | Oliver Medhurst        | IE (Porffor)       |
| [ABO](../../people/ABO.md) | Andreu Botella         | Igalia             |
| CHU                        | Christian Ulbrich      | Zalari             |
| TKP                        | Tom Kopp               | Zalari             |
| [SRV](../../people/SRV.md) | Sergey Rubanov         | Invited Expert     |
| [EAO](../../people/EAO.md) | Eemeli Aro             | Mozilla            |
| [LVU](../../people/LVU.md) | Lea Verou              | OpenJS             |
| [JGT](../../people/JGT.md) | Justin Grant           | Invited Expert     |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo         | Igalia             |
| IS                         | Istvan Sebestyen       | Ecma               |
| [PFC](../../people/PFC.md) | Philip Chimento        | Igalia             |
| AKI                        | Aki Braun              | Ecma International |
| [KHG](../../people/KHG.md) | Kristen Hewell Garrett | Invited Expert     |
| [CPC](../../people/CPC.md) | Clément Pit-Claudel    | EPFL               |
| [LCA](../../people/LCA.md) | Luca Casonato          | Invited Expert     |
| [MF](../../people/MF.md)   | Michael Ficarra        | F5                 |
| PST                        | Patrick Soquet         | Moddable           |
| [SFC](../../people/SFC.md) | Shane Carr             | Google             |

> Source: summarized after checking out tc39/notes PR #411 (2026 May transcript, unmerged at the time). Dates, location, and the overview come from [tc39/agendas 2026/05](https://github.com/tc39/agendas/blob/main/2026/05.md) and each day's transcript.
