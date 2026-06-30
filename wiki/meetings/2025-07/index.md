# 109th TC39 Meeting (2025-07)

- **会合**: 109th meeting of Ecma TC39
- **会期**: 2025-07-28 〜 2025-07-31(リモート開催、米国太平洋時間)
- **開催地**: リモート(次回はオンサイト・東京、Bloomberg ホスト予定とアナウンス)
- **ホスト**: -(リモート会合のためホスト企業なし)
- **Agenda**: [tc39/agendas 2025/07](https://github.com/tc39/agendas/blob/main/2025/07.md)

## 概要

ECMA-262 / ECMA-402 の提案審議が中心の4日間リモート会合。**`Math.sumPrecise`・Uint8Array base64+hex が Stage 4 到達**、**Iterator Sequencing・Upsert が Stage 3 到達**。Intl 関連では **Intl Era and Month Code・Intl Keep Trailing Zeros が Stage 2.7 到達**、**Amount(旧 Measure)は WH の非有限値懸念で Stage 2 不成立**。Import Buffer は Stage 1 から一気に Stage 2 まで到達(`Uint8Array` + `type: "bytes"` に変更)。Module Import Hook and new Global は問題文の見直しを経て Stage 1 を取得。一方、`Object.propertyCount`・`Array.isSparse` の Stage advancement は objection により不成立(`Array.getNonIndexStringProperties`・`Object.getOwnPropertySymbols` options は Stage 1 到達)。TypedArray copyWithin の normative 修正、module evaluation promise の順序統一、Temporal の option 処理順序変更などの normative PR にも consensus が得られた。"write your own comments" という LLM 生成コメント規制を `AI_policy.md` に記載する方針も合意された。

## 日次サマリー

- [Day 1 — 2025-07-28](2025-07-28.md)
- [Day 2 — 2025-07-29](2025-07-29.md)
- [Day 3 — 2025-07-30](2025-07-30.md)
- [Day 4 — 2025-07-31](2025-07-31.md)

## 参加者

`raw/notes/meetings/2025-07/july-28.md` の attendees より(略号 — 氏名 — 所属):

| 略号 | 氏名                   | 所属                |
| ---- | ---------------------- | ------------------- |
| JMN  | Jesse Alama            | Igalia              |
| DJM  | Dmitry Makhnev         | JetBrains           |
| WH   | Waldemar Horwat        | Invited Expert      |
| GB   | Guy Bedford            | Cloudflare          |
| DLM  | Daniel Minor           | Mozilla             |
| ZTZ  | Zbyszek Tenerowicz     | Consensys           |
| JHD  | Jordan Harband         | HeroDevs            |
| SRV  | Sergey Rubanov         | Invited Expert      |
| CM   | Chip Morningstar       | Consensys           |
| NRO  | Nicolò Ribaudo         | Igalia              |
| MBH  | Mikhail Barash         | Univ. of Bergen     |
| KM   | Keith Miller           | Apple Inc.          |
| AKI  | Aki Rose Braun         | Ecma International  |
| SHN  | Samina Husain          | Ecma International  |
| OFR  | Olivier Flückiger      | Google              |
| RGN  | Richard Gibson         | Agoric              |
| RMH  | Rezvan Mahdavi Hezaveh | Google              |
| JSC  | J. S. Choi             | Invited Expert      |
| EAO  | Eemeli Aro             | Mozilla             |
| TAB  | Tab Atkins-Bittner     | Google              |
| IS   | Istvan Sebestyen       | Ecma                |
| DRR  | Daniel Rosenwasser     | Microsoft           |
| ABO  | Andreu Botella         | Igalia              |
| CDA  | Chris de Almeida       | IBM                 |
| CZW  | Chengzhong Wu          | Bloomberg           |
| JRL  | Justin Ridgewell       | Google              |
| KG   | Kevin Gibbons          | F5                  |
| MAH  | Mathieu Hofman         | Agoric              |
| MF   | Michael Ficarra        | F5                  |
| MM   | Mark S. Miller         | Agoric              |
| RPR  | Rob Palmer             | Bloomberg           |
| SHS  | Stephen Hicks          | Google              |
| USA  | Ujjwal Sharma          | Igalia              |

> 出典: [raw/notes/meetings/2025-07](../../../raw/notes/meetings/2025-07/)。会期・開催地・概要は [tc39/agendas 2025/07](https://github.com/tc39/agendas/blob/main/2025/07.md) と各日逐語録より。
