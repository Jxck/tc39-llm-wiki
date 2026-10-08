# 101st TC39 Meeting (2024-04)

- **Meeting**: 101st meeting of Ecma TC39
- **Dates**: 2024-04-08 to 2024-04-11 (10:00-15:00 ET each day)
- **Location**: Remote
- **Host**: Remote
- **Agenda**: [tc39/agendas 2024/04](https://github.com/tc39/agendas/blob/main/2024/04.md)

## Overview

A four-day remote meeting with nine stage changes. [Duplicate named capture groups](../../proposals/duplicate-named-capture-groups.md) and [New Set methods](../../proposals/set-methods.md) reached **Stage 4**; [Dynamic Code Brand Checks](../../proposals/dynamic-code-brand-checks.md) (the Trusted Types integration for `eval` / `new Function`) jumped **1 → 3** with a reworked host hook, and [Redeclarable global eval-introduced vars](../../proposals/redeclarable-global-eval-vars.md) went **→ 2.7 on day 1 and 2.7 → 3 on day 4**; [Promise.try](../../proposals/promise-try.md) and [Math.sumPrecise](../../proposals/math-sum-precise.md) (renamed from `sumExact` at [MM](../../people/MM.md)'s suggestion) reached **Stage 2.7**; and [Error.isError](../../proposals/error-is-error.md) (revived nine years after its rejection), [Strict Enforcement of 'using'](../../proposals/using-enforcement.md) and [Signals](../../proposals/signals.md) entered **Stage 1**. The `Array.prototype.last` proposal was withdrawn (`Array.prototype.at` covers it). Notable non-advancements: [Decimal](../../proposals/decimal.md) stayed at Stage 1 after [WH](../../people/WH.md)'s review found the spec short of Stage 2 criteria, and [Extractors](../../proposals/extractors.md) held off on Stage 2 over cover-grammar issues. The committee reached consensus on non-binding coercion guidelines (Stop Coercing Things pt 4). Editors reported ES2024 frozen and in opt-out, with AWB doing one more manual print-PDF run while TC39 asks Ecma to budget a long-term solution; [TG3](../../people/CDA.md) doubled its cadence to weekly with KKL joining as convener, and TG4 (Source Maps) consolidated its repos ahead of the June Munich meeting.

## Stage transitions

| Proposal                                                                                     | Transition                                 | Day   |
| -------------------------------------------------------------------------------------------- | ------------------------------------------ | ----- |
| [Duplicate named capture groups](../../proposals/duplicate-named-capture-groups.md)          | 3 → 4                                      | Day 1 |
| [New Set methods](../../proposals/set-methods.md)                                            | 3 → 4                                      | Day 1 |
| Array.last                                                                                   | withdrawn (`Array.prototype.at` covers it) | Day 1 |
| [Promise.try](../../proposals/promise-try.md)                                                | 2 → 2.7                                    | Day 1 |
| [Redeclarable global eval-introduced vars](../../proposals/redeclarable-global-eval-vars.md) | → 2.7                                      | Day 1 |
| [Math.sumPrecise](../../proposals/math-sum-precise.md)                                       | 2 → 2.7 (renamed from `sumExact`)          | Day 2 |
| [Dynamic Code Brand Checks](../../proposals/dynamic-code-brand-checks.md)                    | 1 → 3                                      | Day 3 |
| [Error.isError](../../proposals/error-is-error.md)                                           | → 1 (revived)                              | Day 3 |
| [Strict Enforcement of 'using'](../../proposals/using-enforcement.md)                        | → 1                                        | Day 4 |
| [Signals](../../proposals/signals.md)                                                        | → 1                                        | Day 4 |
| [Redeclarable global eval-introduced vars](../../proposals/redeclarable-global-eval-vars.md) | 2.7 → 3                                    | Day 4 |
| [Decimal](../../proposals/decimal.md)                                                        | no advancement (stays at Stage 1)          | Day 4 |
| [Extractors](../../proposals/extractors.md)                                                  | no advancement (cover-grammar issues)      | Day 4 |

## Daily summaries

- [Day 1 — 2024-04-08](2024-04-08.md)
- [Day 2 — 2024-04-09](2024-04-09.md)
- [Day 3 — 2024-04-10](2024-04-10.md)
- [Day 4 — 2024-04-11](2024-04-11.md)

## Attendees

From the attendees in `raw/notes/meetings/2024-04/april-08.md` (abbreviation — name — affiliation):

| Abbreviation | Name               | Affiliation        |
| ------------ | ------------------ | ------------------ |
| WH           | Waldemar Horwat    | Invited Expert     |
| LGH          | Linus Groh         | Bloomberg          |
| DMM          | Duncan MacGregor   | ServiceNow         |
| DLM          | Daniel Minor       | Mozilla            |
| NRO          | Nicolò Ribaudo     | Igalia             |
| CDA          | Chris de Almeida   | IBM                |
| JMN          | Jesse Alama        | Igalia             |
| KG           | Kevin Gibbons      | F5                 |
| MF           | Michael Ficarra    | F5                 |
| JHD          | Jordan Harband     | HeroDevs           |
| BAN          | Ben Allen          | Igalia             |
| JWS          | Jason Williams     | Bloomberg          |
| BSH          | Bradford C Smith   | Google             |
| USA          | Ujjwal Sharma      | Igalia             |
| PFC          | Philip Chimento    | Igalia             |
| SRV          | Sergey Rubanov     | Invited Expert     |
| MM           | Mark Miller        | Agoric             |
| DRR          | Daniel Rosenwasser | Microsoft          |
| JWK          | Jack Works         | Sujitech           |
| IS           | Istvan Sebestyen   | Ecma International |
| ACE          | Ashley Claymore    | Bloomberg          |
| MAH          | Mathieu Hofman     | Agoric             |
| SHN          | Samina Husain      | Ecma International |
| MBH          | Mikhail Barash     | Univ. of Bergen    |
