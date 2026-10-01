# 112th TC39 Meeting (2026-01)

- **Meeting**: 112th meeting of Ecma TC39
- **Dates**: 2026-01-20 to 2026-01-21 (10:00-15:00 EST on both days)
- **Location**: Remote (meeting time zone America/Port-au-Prince, UTC-5)
- **Host**: Remote
- **Agenda**: [tc39/agendas 2026/01](https://github.com/tc39/agendas/blob/main/2026/01.md)

## Overview

A two-day remote meeting (34 attendees on day 1, 29 on day 2; the next meeting, the 113th, is hosted by Google in New York in March). **[Upsert](../../proposals/upsert.md) reached Stage 4**, and **[Intl Era/Month Code](../../proposals/intl-era-month-code.md) reached Stage 3** together with a batch of normative changes (a closed list of supported calendars, ignoring `islamic-rgsa`, the 6 Meiji start date for the Japanese calendar, and reference years for extremely rare leap months and days). **[Import Sync](../../proposals/import-sync.md) advanced to Stage 2**, and two error-constructor options proposals from RBR, `limit` and `framesAbove`, were new at Stage 1. **Composable value-backed accessors** was split under pressure against new syntax: both **composable accessors via built-in decorators** and **alias accessors** advanced to Stage 1 as separate tracks. Consensus was reached on two [Temporal](../../proposals/temporal.md) normative PRs (restricting `PlainYearMonth` arithmetic to years and months, and making `toLocaleString` of the Plain types independent of the formatter's time zone), both part of the path to a joint Stage 4 with Era/Month Code, and on the annual ECMA-402 numbering-system update adding `tols` from Unicode 17. `function.sent` was conditionally withdrawn pending champion approval (JHX later said he wants to keep it, so it stays), and Intl.UnitFormat was formally withdrawn as deprecated. The deferred re-exports champions presented three options for the import defer interaction problem without reaching a conclusion, and the Stage 3/2.7 proposal review flagged Legacy RegExp Features, Dynamic Code Brand Checks, and Atomics.pause as possibly ready for Stage 4 soon.

## Stage transitions

| Proposal                                                      | Transition                                                          | Day   |
| ------------------------------------------------------------- | ------------------------------------------------------------------- | ----- |
| [Upsert](../../proposals/upsert.md)                           | 3 → 4                                                               | Day 1 |
| [Intl Era/Month Code](../../proposals/intl-era-month-code.md) | 2.7 → 3                                                             | Day 1 |
| [Import Sync](../../proposals/import-sync.md)                 | 1 → 2                                                               | Day 1 |
| Error option `limit`                                          | new → 1                                                             | Day 1 |
| Error option `framesAbove`                                    | new → 1                                                             | Day 1 |
| function.sent                                                 | conditional withdrawal; not carried out (champion wants to keep it) | Day 1 |
| Intl.UnitFormat                                               | withdrawn (deprecated in favor of Intl.NumberFormat units)          | Day 1 |
| Composable accessors via built-in decorators                  | new → 1 (split from Composable value-backed accessors)              | Day 2 |
| Alias accessors                                               | new → 1 (split from Composable value-backed accessors)              | Day 2 |

## Daily summaries

- [Day 1 — 2026-01-20](2026-01-20.md)
- [Day 2 — 2026-01-21](2026-01-21.md)

## Attendees

From the attendees in `raw/notes/meetings/2026-01/january-20.md` (abbreviation — name — affiliation):

| Abbreviation | Name              | Affiliation        |
| ------------ | ----------------- | ------------------ |
| CDA          | Chris de Almeida  | IBM                |
| WH           | Waldemar Horwat   | Invited Expert     |
| DMM          | Duncan MacGregor  | ServiceNow Inc     |
| DJM          | Dmitry Makhnev    | JetBrains          |
| RBR          | Ruben Bridgewater | Datadog            |
| KM           | Keith Miller      | Apple              |
| USA          | Ujjwal Sharma     | Igalia             |
| BAN          | Ben Allen         | Igalia             |
| NRO          | Nicolò Ribaudo    | Igalia             |
| CLA          | Caio Lima         | Igalia             |
| JKG          | Josh Goldberg     | Invited Expert     |
| SFC          | Shane F Carr      | Google             |
| SHN          | Samina Husain     | Ecma International |
| SHS          | Steve Hicks       | Google             |
| OFR          | Olivier Flückiger | Google             |
| LGH          | Linus Groh        | Bloomberg          |
| MBH          | Mikhail Barash    | Univ. of Bergen    |
| PFC          | Philip Chimento   | Igalia             |
| IOA          | Ioanna Dimitriou  | Igalia             |
| CM           | Chip Morningstar  | Consensys          |
| DLM          | Daniel Minor      | Mozilla            |
| AKI          | Aki Braun         | Ecma International |
| LVU          | Lea Verou         | OpenJS             |
| RGN          | Richard Gibson    | Agoric             |
| JHS          | Jonas Haukenes    | Univ. of Bergen    |
| IS           | Istvan Sebestyen  | Ecma               |
| GB           | Guy Bedford       | Cloudflare         |
| JWK          | Jack Works        | Sujitech           |
| CZW          | Chengzhong Wu     | Bloomberg          |
| JHD          | Jordan Harband    | Socket             |
| KG           | Kevin Gibbons     | F5                 |
| MF           | Michael Ficarra   | F5                 |
| MM           | Mark S. Miller    | Agoric             |
| RPR          | Rob Palmer        | Bloomberg          |

> Source: [tc39/notes/meetings/2026-01](https://github.com/tc39/notes/tree/main/meetings/2026-01). Dates, location, and host come from [tc39/agendas 2026/01](https://github.com/tc39/agendas/blob/main/2026/01.md).
