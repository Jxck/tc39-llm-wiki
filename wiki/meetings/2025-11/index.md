# 111th TC39 Meeting (2025-11)

- **会合**: 111th meeting of Ecma TC39
- **会期**: 2025-11-18 〜 2025-11-20
- **開催地**: Tokyo, Japan
- **ホスト**: Bloomberg
- **Agenda**: [tc39/agendas 2025/11](https://github.com/tc39/agendas/blob/main/2025/11.md)

## 概要

東京・Bloomberg オフィスでの3日間の対面開催(43名がサインアップ)。**Intl Locale Info API**・**Iterator Sequencing** が Stage 4 に到達し、**Joint Iteration が Stage 3** へ前進。**await dictionary** は Stage 2 を経ず直接 **Stage 2.7** に到達し、**Import Text** が Stage 1・Stage 2、条件付きで Stage 2.7 まで進んだ。**Intl Unit Protocol**・**Intl Energy Units**・**`Object.getNonIndexStringProperties`** が新規に Stage 1、**TypedArray Concatenation**・**TypedArray Find Within** は専用リポジトリ作成を条件に条件付き Stage 1 となった。**`Object.propertyCount`** は `Object.keysLength` と分離され、後者のみ Stage 2 へ前進。一方 **export defer**(Stage 2.7 不成立)、**Declarations in Conditionals**(Day Three まで継続するも未決着)、**Class spread syntax**・**Class field introspection**(いずれも Stage 0 のまま、CM/WH や MM/GCL/JSL から懸念表明)は前進せず。**Decorators** は Test262 カバレッジ不足と V8/JSC/SpiderMonkey 間の実装方針の不一致が報告され Stage 2.7 のまま。**Intl Era Monthcode** は Normative 変更2件を承認しつつ Stage 3 判断を2026年1月へ持ち越し。**Amount** はスコープを単位変換中心へ戻す方針で Stage 1 のまま継続。**Composites** の比較子選択は2回の TCQ 温度感確認で内部化方式・WeakMap 漏えい時の例外方針が支持されたが正式な Stage 提起は無し。

## 日次サマリー

- [Day 1 — 2025-11-18](2025-11-18.md)
- [Day 2 — 2025-11-19](2025-11-19.md)
- [Day 3 — 2025-11-20](2025-11-20.md)

## 参加者

`raw/notes/meetings/2025-11/november-18.md` の attendees より(略号 — 氏名 — 所属):

| 略号 | 氏名                 | 所属               |
| ---- | -------------------- | ------------------ |
| WH   | Waldemar Horwat      | Invited Expert     |
| RGN  | Richard Gibson       | Agoric             |
| JKG  | Josh Goldberg        | Invited Expert     |
| RBR  | Ruben Bridgewater    | Invited Expert     |
| DJM  | Dmitry Makhnev       | JetBrains          |
| FYT  | Frank Yung-Fong Tang | Google             |
| AFU  | Anthony Fu           | Vercel             |
| JSL  | James M Snell        | Cloudflare         |
| DLM  | Daniel Minor         | Mozilla            |
| JKP  | Jonathan Kuperman    | Bloomberg          |
| CHU  | Christian Ulbrich    | Zalari             |
| AIS  | Marina Aisa          | Apple              |
| MAE  | Martin Alvarez       | Huawei             |
| ACE  | Ashley Claymore      | Bloomberg          |
| ABO  | Andreu Botella       | Igalia             |
| DRO  | Devin Rousso         | Invited Expert     |
| JAD  | Jake Archibald       | Mozilla            |
| LVU  | Lea Verou            | OpenJS             |
| MAH  | Mathieu Hofman       | Agoric             |
| CLA  | Caio Lima            | Igalia             |
| YSZ  | Yusuke Suzuki        | Apple              |
| CM   | Chip Morningstar     | Consensys          |
| AKI  | Aki Rose Braun       | Ecma International |
| PFC  | Philip Chimento      | Igalia             |
| EAO  | Eemeli Aro           | Mozilla            |
| MBH  | Mikhail Barash       | Univ. of Bergen    |
| KM   | Keith Miller         | Apple              |
| RKG  | Ross Kirsling        | Sony               |
| CDA  | Chris de Almeida     | IBM                |
| NRO  | Nicolò Ribaudo       | Igalia             |
| RBN  | Ron Buckton          | F5                 |
| SFC  | Shane F Carr         | Google             |
| IS   | Istvan Sebestyen     | Ecma               |
| DRR  | Daniel Rosenwasser   | Microsoft          |
| SHS  | Stephen Hicks        | Google             |
| USA  | Ujjwal Sharma        | Igalia             |
| GB   | Guy Bedford          | Cloudflare         |
| CZW  | Chengzhong Wu        | Bloomberg          |
| GCL  | Gus Caplan           | Deno               |
| JHD  | Jordan Harband       | Socket             |
| JRL  | Justin Ridgewell     | Google             |
| KG   | Kevin Gibbons        | F5                 |
| MF   | Michael Ficarra      | F5                 |
| MM   | Mark S. Miller       | Agoric             |
| OFR  | Olivier Flückiger    | Google             |
| RPR  | Rob Palmer           | Bloomberg          |

> 出典: [raw/notes/meetings/2025-11](../../../raw/notes/meetings/2025-11/)。会期・概要は [tc39/agendas 2025/11](https://github.com/tc39/agendas/blob/main/2025/11.md) と各日逐語録より。
