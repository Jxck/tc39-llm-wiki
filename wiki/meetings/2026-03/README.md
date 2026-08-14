# 113th TC39 Meeting (2026-03)

- **会合**: 113th meeting of Ecma TC39
- **会期**: 2026-03-10 〜 2026-03-12(10・11 日は 10:00-17:00、12 日は 10:00-16:00 EDT)
- **開催地**: New York, NY(米国)
- **ホスト**: Google(室内ロジは Justin Ridgewell が担当)
- **Agenda**: [tc39/agendas 2026/03](https://github.com/tc39/agendas/blob/main/2026/03.md)

## 概要

ECMA-262 / ECMA-402 の提案審議が中心の3日間。**[Temporal](../../proposals/temporal.md) が Stage 4 到達**(約5年の Stage 3 を経て出荷済み)、**[Intl Era/Month Code](../../proposals/intl-era-month-code.md) も Stage 4**。Stage 2.7 へ [Error Stack Accessor](../../proposals/error-stack-accessor.md)・[RegExp Buffer Boundaries](../../proposals/regexp-buffer-boundaries.md)・[Iterator Includes](../../proposals/iterator-includes.md)、Stage 3 へ Import Text・[Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md) が進むなど多数の advancement があった。ほかに Abort Protocol / Structured Concurrency / [Explicit Resource Management](../../proposals/explicit-resource-management.md) の Stage 4 条件付き状況、test262 のカバレッジ戦略、tree-shakeable methods などを議論。年次の chair/editor/convener 選挙も実施(冒頭で新たに 262 editor が増員)。

## 日次サマリー

- [Day 1 — 2026-03-10](2026-03-10.md)
- [Day 2 — 2026-03-11](2026-03-11.md)
- [Day 3 — 2026-03-12](2026-03-12.md)

## 参加者

`raw/notes/meetings/2026-03/march-10.md` の attendees より(略号 — 氏名 — 所属):

| 略号                       | 氏名               | 所属               |
| -------------------------- | ------------------ | ------------------ |
| AKI                        | Aki Rose Braun     | Ecma International |
| [ACE](../../people/ACE.md) | Ashley Claymore    | Bloomberg          |
| [BAN](../../people/BAN.md) | Ben Allen          | Igalia             |
| CZW                        | Chengzhong Wu      | Bloomberg          |
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
| LGH                        | Linus Groh         | Bloomberg          |
| MBH                        | Mikhail Barash     | Univ. of Bergen    |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo     | Igalia             |
| [OFR](../../people/OFR.md) | Olivier Flückiger  | Google             |
| PKA                        | Peter Klecha       | Bloomberg          |
| [PFC](../../people/PFC.md) | Philip Chimento    | Igalia             |
| [RGN](../../people/RGN.md) | Richard Gibson     | Agoric             |
| [RBN](../../people/RBN.md) | Ron Buckton        | F5                 |
| RBR                        | Ruben Bridgewater  | Invited Expert     |
| SHN                        | Samina Husain      | Ecma International |
| [SHS](../../people/SHS.md) | Stephen Hicks      | Google             |
| [WH](../../people/WH.md)   | Waldemar Horwat    | Invited Expert     |
| YNP                        | Yagiz Nizipli      | Cloudflare         |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser | Microsoft          |
| [JMN](../../people/JMN.md) | Jesse Alama        | Igalia             |
| [KG](../../people/KG.md)   | Kevin Gibbons      | F5                 |
| [MF](../../people/MF.md)   | Michael Ficarra    | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller     | Agoric             |
| [RPR](../../people/RPR.md) | Rob Palmer         | Bloomberg          |
| [SFC](../../people/SFC.md) | Shane Carr         | Google             |
| [ZB](../../people/ZB.md)   | Zibi Braniecki     | —                  |

> 出典: [raw/notes/meetings/2026-03](../../../raw/notes/meetings/2026-03/)。会期・開催地・概要は [tc39/agendas 2026/03](https://github.com/tc39/agendas/blob/main/2026/03.md) と各日逐語録より。
