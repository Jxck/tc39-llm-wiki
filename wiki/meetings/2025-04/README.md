# 107th TC39 Meeting (2025-04)

- **Meeting**: 107th meeting of Ecma TC39
- **Dates**: 2025-04-14 to 2025-04-17 (10:00-15:00 EDT each day)
- **Location**: Remote
- **Host**: Remote
- **Agenda**: [tc39/agendas 2025/04](https://github.com/tc39/agendas/blob/main/2025/04.md)

## Overview

A four-day remote meeting. **[Composite Keys](../../proposals/composite-keys.md) reached Stage 1** and **[Records & Tuples](../../proposals/records-and-tuples.md) was withdrawn** the same day, with composites positioned as its reimagining. **[Upsert](../../proposals/upsert.md) reached Stage 2.7**, and **[Non-extensible applies to Private](../../proposals/nonextensible-applies-to-private.md) went from nothing to Stage 2.7 in a single session**, while **[Enums](../../proposals/enums.md), [Object.propertyCount](../../proposals/object-propertycount.md), [Compare Strings by Codepoint](../../proposals/compare-strings-by-codepoint.md), and [Disposable AsyncContext](../../proposals/disposable-asynccontext.md) reached Stage 1**. [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)'s Stage 3 ask was deferred until its Test262 tests are merged, and `export defer` was reaffirmed at Stage 2 after `import defer` split off. The sync module evaluation promise PR (#3535) was blocked on day 1 over spec-internal promises reaching host hooks, and reached consensus on day 4. [AsyncContext](../../proposals/async-context.md) presented its dispatch-context web integration with framework testimonials — use cases found convincing, but browsers split on whether they justify the implementation cost. The consensus-policy reform proposal (a second blocker, not from the same member) drew objections from MM and WH and continues at future plenaries, and the decimal/measure Amounts design drew concerns over unit/precision commutativity and the proposed ban on bare decimals in Intl. WHATWG Observables was presented informally and received positive feedback.

## Stage transitions

| Proposal                                                                                 | Transition                                        | Day       |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------- | --------- |
| [Composite Keys](../../proposals/composite-keys.md)                                      | new → 1                                           | Day 1     |
| [Records & Tuples](../../proposals/records-and-tuples.md)                                | withdrawn                                         | Day 1     |
| [Upsert](../../proposals/upsert.md)                                                      | 2 → 2.7                                           | Day 1     |
| [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)                        | no advancement (stays 2.7; Stage 3 deferred)      | Day 1     |
| [Enums](../../proposals/enums.md)                                                        | new → 1                                           | Day 2     |
| [Object.propertyCount](../../proposals/object-propertycount.md)                          | new → 1                                           | Day 2     |
| [Non-extensible applies to Private](../../proposals/nonextensible-applies-to-private.md) | new → 2.7                                         | Day 2     |
| [Explicit Resource Management](../../proposals/explicit-resource-management.md)          | normative PR consensus (no `using` in bare case)  | Day 2     |
| [Compare Strings by Codepoint](../../proposals/compare-strings-by-codepoint.md)          | new → 1                                           | Day 3     |
| `export defer`                                                                           | reaffirmed Stage 2                                | Day 3     |
| [Disposable AsyncContext](../../proposals/disposable-asynccontext.md)                    | new → 1                                           | Day 4     |
| Sync module evaluation promise (#3535)                                                   | normative PR consensus (day 4, after day-1 block) | Days 1, 4 |

## Daily summaries

- [Day 1 — 2025-04-14](2025-04-14.md)
- [Day 2 — 2025-04-15](2025-04-15.md)
- [Day 3 — 2025-04-16](2025-04-16.md)
- [Day 4 — 2025-04-17](2025-04-17.md)

## Attendees

From the attendees in `raw/notes/meetings/2025-04/april-14.md` (abbreviation — name — affiliation):

| Abbreviation               | Name                   | Affiliation        |
| -------------------------- | ---------------------- | ------------------ |
| [WH](../../people/WH.md)   | Waldemar Horwat        | Invited Expert     |
| [DE](../../people/DE.md)   | Daniel Ehrenberg       | Bloomberg          |
| [ACE](../../people/ACE.md) | Ashley Claymore        | Bloomberg          |
| JKP                        | Jonathan Kuperman      | Bloomberg          |
| BLY                        | Ben Lickly             | Google             |
| BSH                        | Bradford C. Smith      | Google             |
| [CDA](../../people/CDA.md) | Chris de Almeida       | IBM                |
| [DLM](../../people/DLM.md) | Daniel Minor           | Mozilla            |
| [JMN](../../people/JMN.md) | Jesse Alama            | Igalia             |
| [CM](../../people/CM.md)   | Chip Morningstar       | Consensys          |
| [MLS](../../people/MLS.md) | Michael Saboff         | Apple              |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo         | Igalia             |
| [REK](../../people/REK.md) | Erik Marks             | Consensys          |
| [RGN](../../people/RGN.md) | Richard Gibson         | Agoric             |
| JKG                        | Josh Goldberg          | Invited Expert     |
| LFR                        | Luca Forstner          | Sentry             |
| [PFC](../../people/PFC.md) | Philip Chimento        | Igalia             |
| CHU                        | Christian Ulbrich      | Zalari             |
| MBH                        | Mikhail Barash         | Univ. of Bergen    |
| [EAO](../../people/EAO.md) | Eemeli Aro             | Mozilla            |
| [CZW](../../people/CZW.md) | Chengzhong Wu          | Bloomberg          |
| [DJM](../../people/DJM.md) | Dmitry Makhnev         | JetBrains          |
| [JSC](../../people/JSC.md) | J. S. Choi             | Invited Expert     |
| [KM](../../people/KM.md)   | Keith Miller           | Apple Inc          |
| AKI                        | Aki Rose Braun         | Ecma International |
| [LCA](../../people/LCA.md) | Luca Casonato          | Deno Land Inc      |
| SHN                        | Samina Husain          | Ecma International |
| IS                         | Istvan Sebestyen       | Ecma International |
| [DMM](../../people/DMM.md) | Duncan MacGregor       | ServiceNow Inc     |
| [MAH](../../people/MAH.md) | Mathieu Hofman         | Agoric             |
| [MM](../../people/MM.md)   | Mark Miller            | Agoric             |
| [RBN](../../people/RBN.md) | Ron Buckton            | Microsoft          |
| AWO                        | Andreas Woess          | Oracle             |
| RCA                        | Romulo Cintra          | Igalia             |
| [ABO](../../people/ABO.md) | Andreu Botella         | Igalia             |
| —                          | Ruben Bridgewater      | Invited Expert     |
| [MF](../../people/MF.md)   | Michael Ficarra        | F5                 |
| UGN                        | Ulises Gascon          | Open JS            |
| [KG](../../people/KG.md)   | Kevin Gibbons          | F5                 |
| [SYG](../../people/SYG.md) | Shu-yu Guo             | Google             |
| [JHD](../../people/JHD.md) | Jordan Harband         | HeroDevs           |
| [JHX](../../people/JHX.md) | John Hax               | Invited Expert     |
| —                          | Stephen Hicks          | Google             |
| TKP                        | Tom Kopp               | Zalari GmbH        |
| —                          | Veniamin Krol          | JetBrains          |
| [RMH](../../people/RMH.md) | Rezvan Mahdavi Hezaveh | Google             |
| LFP                        | Luis Pardo             | Microsoft          |
| [JRL](../../people/JRL.md) | Justin Ridgewell       | Google             |
| [USA](../../people/USA.md) | Ujjwal Sharma          | Igalia             |
| [JSL](../../people/JSL.md) | James Snell            | Cloudflare         |
| [JWK](../../people/JWK.md) | Jack Works             | Sujitech           |

> Source: [tc39/notes/meetings/2025-04](https://github.com/tc39/notes/tree/main/meetings/2025-04). Dates, location, and host come from [tc39/agendas 2025/04](https://github.com/tc39/agendas/blob/main/2025/04.md).
