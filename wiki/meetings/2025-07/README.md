# 109th TC39 Meeting (2025-07)

- **会合**: 109th meeting of Ecma TC39
- **会期**: 2025-07-28 〜 2025-07-31(リモート開催、米国太平洋時間)
- **開催地**: リモート(次回はオンサイト・東京、Bloomberg ホスト予定とアナウンス)
- **ホスト**: -(リモート会合のためホスト企業なし)
- **Agenda**: [tc39/agendas 2025/07](https://github.com/tc39/agendas/blob/main/2025/07.md)

## 概要

ECMA-262 / ECMA-402 の提案審議が中心の4日間リモート会合。**`Math.sumPrecise`・Uint8Array base64+hex が Stage 4 到達**、**Iterator Sequencing・[Upsert](../../proposals/upsert.md) が Stage 3 到達**。Intl 関連では **[Intl Era and Month Code](../../proposals/intl-era-month-code.md)・[Intl Keep Trailing Zeros](../../proposals/intl-keep-trailing-zeros.md) が Stage 2.7 到達**、**[Amount](../../proposals/amount.md)(旧 Measure)は [WH](../../people/WH.md) の非有限値懸念で Stage 2 不成立**。Import Buffer は Stage 1 から一気に Stage 2 まで到達(`Uint8Array` + `type: "bytes"` に変更)。Module Import Hook and new Global は問題文の見直しを経て Stage 1 を取得。一方、`Object.propertyCount`・`Array.isSparse` の Stage advancement は objection により不成立(`Array.getNonIndexStringProperties`・`Object.getOwnPropertySymbols` options は Stage 1 到達)。TypedArray copyWithin の normative 修正、module evaluation promise の順序統一、[Temporal](../../proposals/temporal.md) の option 処理順序変更などの normative PR にも consensus が得られた。"write your own comments" という LLM 生成コメント規制を `AI_policy.md` に記載する方針も合意された。

## 日次サマリー

- [Day 1 — 2025-07-28](2025-07-28.md)
- [Day 2 — 2025-07-29](2025-07-29.md)
- [Day 3 — 2025-07-30](2025-07-30.md)
- [Day 4 — 2025-07-31](2025-07-31.md)

## 参加者

`raw/notes/meetings/2025-07/july-28.md` の attendees より(略号 — 氏名 — 所属):

| 略号                       | 氏名                   | 所属               |
| -------------------------- | ---------------------- | ------------------ |
| [JMN](../../people/JMN.md) | Jesse Alama            | Igalia             |
| [DJM](../../people/DJM.md) | Dmitry Makhnev         | JetBrains          |
| [WH](../../people/WH.md)   | Waldemar Horwat        | Invited Expert     |
| [GB](../../people/GB.md)   | Guy Bedford            | Cloudflare         |
| [DLM](../../people/DLM.md) | Daniel Minor           | Mozilla            |
| [ZTZ](../../people/ZTZ.md) | Zbyszek Tenerowicz     | Consensys          |
| [JHD](../../people/JHD.md) | Jordan Harband         | HeroDevs           |
| SRV                        | Sergey Rubanov         | Invited Expert     |
| [CM](../../people/CM.md)   | Chip Morningstar       | Consensys          |
| [NRO](../../people/NRO.md) | Nicolò Ribaudo         | Igalia             |
| MBH                        | Mikhail Barash         | Univ. of Bergen    |
| [KM](../../people/KM.md)   | Keith Miller           | Apple Inc.         |
| AKI                        | Aki Rose Braun         | Ecma International |
| SHN                        | Samina Husain          | Ecma International |
| [OFR](../../people/OFR.md) | Olivier Flückiger      | Google             |
| [RGN](../../people/RGN.md) | Richard Gibson         | Agoric             |
| RMH                        | Rezvan Mahdavi Hezaveh | Google             |
| [JSC](../../people/JSC.md) | J. S. Choi             | Invited Expert     |
| [EAO](../../people/EAO.md) | Eemeli Aro             | Mozilla            |
| TAB                        | Tab Atkins-Bittner     | Google             |
| IS                         | Istvan Sebestyen       | Ecma               |
| [DRR](../../people/DRR.md) | Daniel Rosenwasser     | Microsoft          |
| ABO                        | Andreu Botella         | Igalia             |
| [CDA](../../people/CDA.md) | Chris de Almeida       | IBM                |
| CZW                        | Chengzhong Wu          | Bloomberg          |
| [JRL](../../people/JRL.md) | Justin Ridgewell       | Google             |
| [KG](../../people/KG.md)   | Kevin Gibbons          | F5                 |
| [MAH](../../people/MAH.md) | Mathieu Hofman         | Agoric             |
| [MF](../../people/MF.md)   | Michael Ficarra        | F5                 |
| [MM](../../people/MM.md)   | Mark S. Miller         | Agoric             |
| [RPR](../../people/RPR.md) | Rob Palmer             | Bloomberg          |
| [SHS](../../people/SHS.md) | Stephen Hicks          | Google             |
| [USA](../../people/USA.md) | Ujjwal Sharma          | Igalia             |

> 出典: [raw/notes/meetings/2025-07](../../../raw/notes/meetings/2025-07/)。会期・開催地・概要は [tc39/agendas 2025/07](https://github.com/tc39/agendas/blob/main/2025/07.md) と各日逐語録より。
