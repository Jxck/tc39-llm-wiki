# 110th TC39 Meeting (2025-09)

- **会合**: 110th meeting of Ecma TC39
- **会期**: 2025-09-22 〜 2025-09-24
- **開催地**: Remote only
- **ホスト**: なし(リモート開催。次回 2025-11 は Tokyo・Bloomberg ホスト予定)
- **Agenda**: [tc39/agendas 2025/09](https://github.com/tc39/agendas/blob/main/2025/09.md)

## 概要

リモート開催の3日間。**[Iterator Chunking](../../proposals/iterator-chunking.md) が Stage 2.7**、**Import Bytes が Stage 2.7**、**Non-extensible Applies to Private が Stage 3** に到達。`Array.prototype.pushAll`(スタックオーバーフロー対策)・Native Promise Adoption・Native Promise Predicate(直後に Stage 2 へも到達)が新規に Stage 1 へ進んだ。一方 **[Amount](../../proposals/amount.md) は Stage 2 を目指したが、significant digits・命名・数値変換メソッド(`toNumber`/`toBigInt`)・internal slot による brand check 等の懸念が late-breaking で噴出し、3日間にわたり議論が継続したものの Stage 2 には到達せず、次回 Tokyo plenary へ持ち越し**となった。Intl Era Month Code は normative changes(leap month の overflow 挙動の revert、reference year 探索範囲の拡張)に consensus を得て Stage 3 を視野に、[Temporal](../../proposals/temporal.md) は DST 切替時の符号反転バグ修正で normative change consensus を獲得し Stage 4 への道筋を提示。ほかに `Intl.PluralRules` への `[[CompactDisplay]]` slot 追加・Intl mathematical value 化の normative PR、IntlMV の指数・有効桁数上限拡張(Decimal128 を見据えた将来対応)、`how-we-work` への enum kebab-case 規約の consensus、module-global(Compartment)提案の Stage 1 update(ShadowRealm との関係性が論点)などを議論。

## 日次サマリー

- [Day 1 — 2025-09-22](2025-09-22.md)
- [Day 2 — 2025-09-23](2025-09-23.md)
- [Day 3 — 2025-09-24](2025-09-24.md)

## 参加者

`raw/notes/meetings/2025-09/september-22.md` の attendees より(略号 — 氏名 — 所属):

| 略号                       | 氏名               | 所属               |
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

> 出典: [raw/notes/meetings/2025-09](../../../raw/notes/meetings/2025-09/)。会期・概要は [tc39/agendas 2025/09](https://github.com/tc39/agendas/blob/main/2025/09.md) と各日逐語録より。
