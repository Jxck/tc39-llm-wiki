# 104th TC39 Meeting (2024-10)

- **Meeting**: 104th meeting of Ecma TC39
- **Dates**: 2024-10-08 to 2024-10-10 (10:00-17:30 JST; day 3 until 17:00)
- **Location**: Tokyo, Japan
- **Host**: Sony Interactive Entertainment
- **Agenda**: [tc39/agendas 2024/10](https://github.com/tc39/agendas/blob/main/2024/10.md)

## Overview

A three-day in-person meeting hosted by Sony in Tokyo. Four proposals reached Stage 4: **[RegExp Modifiers](../../proposals/regexp-modifiers.md)**, **[Import Attributes](../../proposals/import-attributes.md)** and **[JSON Modules](../../proposals/json-modules.md)** (approved together in two minutes), and **[Iterator helpers](../../proposals/iterator-helpers.md)**; **[Promise.try](../../proposals/promise-try.md)** followed on day 2. **[Iterator sequencing](../../proposals/iterator-sequencing.md) reached Stage 2.7** alongside **[Error.isError](../../proposals/error-is-error.md)**, while **[Math.sumPrecise](../../proposals/math-sum-precise.md)** and **[Atomics.pause](../../proposals/atomics-pause.md) reached Stage 3**. **[Shared structs](../../proposals/shared-structs.md) and [Extractors](../../proposals/extractors.md) reached Stage 2**, **[Iterator chunking](../../proposals/iterator-chunking.md) reached Stage 2**, and **[Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md)** and **[Measure](../../proposals/amount.md)** both entered at **Stage 1** (Array.zip also reached Stage 1). The meeting's most contentious topic, **JSSugar/JS0** ([SYG](../../people/SYG.md)'s two-layer language pitch), drew heavy debate on both days without consensus. [import defer](../../proposals/import-defer.md) hit implementation-found bugs — the dynamic `import.defer` form is expected to be dropped — and the TG4 source map 2024 edition was approved for the Ecma GA with an editorial security note. Consensus also landed to strip species-style subclassing from TypedArray/ArrayBuffer/SharedArrayBuffer, and three normative ECMA-402 PRs got conditional consensus.

## Stage transitions

| Proposal                                                          | Transition                                                                                       | Day       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------- |
| [Iterator sequencing](../../proposals/iterator-sequencing.md)     | 2 → 2.7                                                                                          | Day 1     |
| [RegExp Modifiers](../../proposals/regexp-modifiers.md)           | 3 → 4                                                                                            | Day 1     |
| [Import Attributes](../../proposals/import-attributes.md)         | 3 → 4                                                                                            | Day 1     |
| [JSON Modules](../../proposals/json-modules.md)                   | 3 → 4                                                                                            | Day 1     |
| [Iterator helpers](../../proposals/iterator-helpers.md)           | 3 → 4                                                                                            | Day 1     |
| [Shared structs](../../proposals/shared-structs.md)               | 1 → 2                                                                                            | Day 1     |
| `JSSugar/JS0`                                                     | no advancement (no consensus; discussion continues)                                              | Days 1, 3 |
| [Math.sumPrecise](../../proposals/math-sum-precise.md)            | 2 → 3                                                                                            | Day 2     |
| [Extractors](../../proposals/extractors.md)                       | 1 → 2                                                                                            | Day 2     |
| [Promise.try](../../proposals/promise-try.md)                     | 3 → 4                                                                                            | Day 2     |
| [Atomics.pause](../../proposals/atomics-pause.md)                 | 2 → 3                                                                                            | Day 2     |
| [Array.zip](../../proposals/array-zip.md)                         | new → 1                                                                                          | Day 2     |
| [Iterator chunking](../../proposals/iterator-chunking.md)         | 1 → 2                                                                                            | Day 2     |
| [Error.isError](../../proposals/error-is-error.md)                | 2 → 2.7                                                                                          | Day 2     |
| [Immutable ArrayBuffer](../../proposals/immutable-arraybuffer.md) | new → 1                                                                                          | Day 3     |
| [Measure](../../proposals/amount.md) (`measure`)                  | new → 1                                                                                          | Day 3     |
| [import defer](../../proposals/import-defer.md)                   | no advancement (`import.defer` expected to be dropped)                                           | Day 3     |
| [Discard bindings](../../proposals/discard-bindings.md)           | no advancement (Stage 3 reviewers named: [ACE](../../people/ACE.md), [OMT](../../people/OMT.md)) | Days 2, 3 |

## Daily summaries

- [Day 1 — 2024-10-08](2024-10-08.md)
- [Day 2 — 2024-10-09](2024-10-09.md)
- [Day 3 — 2024-10-10](2024-10-10.md)

## Attendees

From the attendees in `raw/notes/meetings/2024-10/october-08.md` (abbreviation — name — affiliation):

| Abbreviation               | Name              | Affiliation     |
| -------------------------- | ----------------- | --------------- |
| [LGH](../../people/LGH.md) | Linus Groh        | Bloomberg       |
| [OMT](../../people/OMT.md) | Oliver Medhurst   | IE (Porffor)    |
| [WH](../../people/WH.md)   | Waldemar Horwat   | Invited Expert  |
| [CZW](../../people/CZW.md) | Chengzhong Wu     | Bloomberg       |
| [RBN](../../people/RBN.md) | Ron Buckton       | Microsoft       |
| [DLM](../../people/DLM.md) | Daniel Minor      | Mozilla         |
| [ACE](../../people/ACE.md) | Ashley Claymore   | Bloomberg       |
| [ABO](../../people/ABO.md) | Andreu Botella    | Igalia          |
| [RKG](../../people/RKG.md) | Ross Kirsling     | Sony            |
| [DRO](../../people/DRO.md) | Devin Rousso      | Invited Expert  |
| [USA](../../people/USA.md) | Ujjwal Sharma     | Igalia          |
| [DJM](../../people/DJM.md) | Dmitry Makhnev    | JetBrains       |
| BSH                        | Bradford Smith    | Google          |
| [CM](../../people/CM.md)   | Chip Morningstar  | Consensys       |
| [DE](../../people/DE.md)   | Daniel Ehrenberg  | Bloomberg       |
| [CDA](../../people/CDA.md) | Chris de Almeida  | IBM             |
| MBH                        | Mikhail Barash    | Univ. of Bergen |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo    | Igalia          |
| [PFC](../../people/PFC.md) | Philip Chimento   | Igalia          |
| [MM](../../people/MM.md)   | Mark Miller       | Agoric          |
| TKP                        | Tom Kopp          | Zalari          |
| [BAN](../../people/BAN.md) | Ben Allen         | Igalia          |
| [JHD](../../people/JHD.md) | Jordan Harband    | HeroDevs        |
| [SRV](../../people/SRV.md) | Sergey Rubanov    | Invited Expert  |
| IS                         | Istvan Sebestyen  | Ecma            |
| [YSV](../../people/YSV.md) | Yulia Startsev    | Mozilla         |
| MHA                        | Marja Hölttä      | Google          |
| [YSZ](../../people/YSZ.md) | Yusuke Suzuki     | Apple           |
| [KM](../../people/KM.md)   | Keith Miller      | Apple           |
| [MLS](../../people/MLS.md) | Michael Saboff    | Apple           |
| [JRL](../../people/JRL.md) | Justin Ridgewell  | Google          |
| API                        | Andrew Paprocki   | Bloomberg       |
| [JMN](../../people/JMN.md) | Jesse Alama       | Igalia          |
| JKP                        | Jonathan Kuperman | Bloomberg       |
| [SYG](../../people/SYG.md) | Shu-yu Guo        | Google          |
| LYL                        | Yilong Li         | Alibaba         |
| [JWK](../../people/JWK.md) | Jack Works        | Sujitech        |

> Source: [tc39/notes/meetings/2024-10](https://github.com/tc39/notes/tree/main/meetings/2024-10). Dates, location, and host come from [tc39/agendas 2024/10](https://github.com/tc39/agendas/blob/main/2024/10.md).
