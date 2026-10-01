# 105th TC39 Meeting (2024-12)

- **Meeting**: 105th meeting of Ecma TC39
- **Dates**: 2024-12-02 to 2024-12-05 (10:00-15:00 MST / UTC-7 each day)
- **Location**: Remote (the agenda lists Albuquerque, New Mexico)
- **Host**: Remote
- **Agenda**: [tc39/agendas 2024/12](https://github.com/tc39/agendas/blob/main/2024/12.md)

## Overview

A four-day remote meeting. **[Intl.DurationFormat](../../proposals/intl-durationformat.md) reached Stage 4** and **[Error.isError](../../proposals/error-is-error.md) reached Stage 3**; **[More Currency Display Choices](../../proposals/more-currency-display-choices.md) went straight to Stage 2** on first presentation. **[Stabilize](../../proposals/stabilize.md) reached Stage 1** (integrity traits) and **[Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md) reached Stage 2**. **[Import Sync](../../proposals/import-sync.md) reached Stage 1** as a problem-space exploration, and **[ESM Phase Imports](../../proposals/esm-phase-imports.md) obtained conditional Stage 2.7** (pending [MM](../../people/MM.md)'s asynchronous approval via TG3). **[Error Stacks Structure](../../proposals/error-stacks.md) did not advance** and was instead split — a new accessor-only proposal ([Error Stack Accessor](../../proposals/error-stack-accessor.md)) was spun off with [MM](../../people/MM.md) co-championing. [ShadowRealm](../../proposals/shadowrealm.md)'s Stage 3 request was withdrawn pending browser DOM-team consensus, [iterator sequencing](../../proposals/iterator-sequencing.md)'s Stage 3 was deferred until its test262 tests merge, and [Upsert](../../proposals/upsert.md) settled on the non-throwing design without advancing. [import defer](../../proposals/import-defer.md) reached consensus on three changes (key-list queries trigger evaluation, `then` hidden on deferred namespaces, `"deferred module"` `toStringTag`) targeting Stage 3 next meeting. Status overviews included the Module Harmony landscape and a briefing on WinterCG's move into Ecma as TC55.

## Stage transitions

| Proposal                                                                          | Transition                                                   | Day       |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| [Intl.DurationFormat](../../proposals/intl-durationformat.md)                     | 3 → 4                                                        | Day 1     |
| [Error.isError](../../proposals/error-is-error.md)                                | 2 → 3                                                        | Day 1     |
| [More Currency Display Choices](../../proposals/more-currency-display-choices.md) | new → 2                                                      | Day 1     |
| [Upsert](../../proposals/upsert.md)                                               | no advancement (non-throwing design chosen; reviewers named) | Day 1     |
| [iterator sequencing](../../proposals/iterator-sequencing.md)                     | no advancement (deferred until test262 merges)               | Day 1     |
| [ShadowRealm](../../proposals/shadowrealm.md)                                     | Stage 3 request withdrawn                                    | Day 1     |
| [Stabilize](../../proposals/stabilize.md)                                         | new → 1                                                      | Day 2     |
| [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)                 | 1 → 2                                                        | Day 2     |
| `error-stacks`                                                                    | no advancement (split; accessor spun off)                    | Days 2, 4 |
| [Import Sync](../../proposals/import-sync.md)                                     | new → 1                                                      | Day 3     |
| [ESM Phase Imports](../../proposals/esm-phase-imports.md)                         | 2 → 2.7 (conditional on [MM](../../people/MM.md)'s approval) | Day 3     |
| [import defer](../../proposals/import-defer.md)                                   | stays 2.7 (consensus changes; Stage 3 targeted next)         | Days 2, 4 |

## Daily summaries

- [Day 1 — 2024-12-02](2024-12-02.md)
- [Day 2 — 2024-12-03](2024-12-03.md)
- [Day 3 — 2024-12-04](2024-12-04.md)
- [Day 4 — 2024-12-05](2024-12-05.md)

## Attendees

From the attendees in `raw/notes/meetings/2024-12/december-02.md` (abbreviation — name — affiliation):

| Abbreviation               | Name             | Affiliation        |
| -------------------------- | ---------------- | ------------------ |
| [WH](../../people/WH.md)   | Waldemar Horwat  | Invited Expert     |
| [DE](../../people/DE.md)   | Daniel Ehrenberg | Bloomberg          |
| IS                         | Istvan Sebestyen | Ecma               |
| [JHD](../../people/JHD.md) | Jordan Harband   | HeroDevs           |
| [DJM](../../people/DJM.md) | Dmitry Makhnev   | JetBrains          |
| [CDA](../../people/CDA.md) | Chris de Almeida | IBM                |
| [SRV](../../people/SRV.md) | Sergey Rubanov   | Invited Expert     |
| [MLS](../../people/MLS.md) | Michael Saboff   | Apple              |
| [JMN](../../people/JMN.md) | Jesse Alama      | Igalia             |
| [ABO](../../people/ABO.md) | Andreu Botella   | Igalia             |
| JMK                        | Jirka Marsik     | Oracle             |
| [RPR](../../people/RPR.md) | Rob Palmer       | Bloomberg          |
| [EAO](../../people/EAO.md) | Eemeli Aro       | Mozilla            |
| JKG                        | Josh Goldberg    | Invited Expert     |
| AKI                        | Aki Rose Braun   | Ecma International |
| [RBN](../../people/RBN.md) | Ron Buckton      | Microsoft          |
| LFR                        | Luca Forstner    | Sentry             |
| MBH                        | Mikhail Barash   | Univ. Bergen       |
| [USA](../../people/USA.md) | Ujjwal Sharma    | Igalia             |
| [JSC](../../people/JSC.md) | J. S. Choi       | Invited Expert     |
| [LGH](../../people/LGH.md) | Linus Groh       | Bloomberg          |
| [KM](../../people/KM.md)   | Keith Miller     | Apple              |
| [RGN](../../people/RGN.md) | Richard Gibson   | Agoric             |
| [JSL](../../people/JSL.md) | James M Snell    | Cloudflare         |
| SHN                        | Samina Husain    | Ecma International |
| [DRO](../../people/DRO.md) | Devin Rousso     | Invited Expert     |
| [NRO](../../people/NRO.md) | Nicolo Ribaudo   | Igalia             |
| JOM                        | Jan Olaf Martin  | Google             |
| [DLM](../../people/DLM.md) | Daniel Minor     | Mozilla            |
| [PFC](../../people/PFC.md) | Philip Chimento  | Igalia             |

> Source: [tc39/notes/meetings/2024-12](https://github.com/tc39/notes/tree/main/meetings/2024-12). Dates, location, and host come from [tc39/agendas 2024/12](https://github.com/tc39/agendas/blob/main/2024/12.md).
