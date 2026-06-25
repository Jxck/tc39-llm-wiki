# 114th TC39 Meeting (2026-05)

- **会合**: 114th meeting of Ecma TC39
- **会期**: 2026-05-19 〜 2026-05-21(19・20 日は 10:00-17:00、21 日は 10:00-16:00 CEST)
- **開催地**: Amsterdam, the Netherlands
- **ホスト**: JetBrains(現地ロジは Dmitry Makhnev ほか)
- **Agenda**: [tc39/agendas 2026/05](https://github.com/tc39/agendas/blob/main/2026/05.md)

## 概要

Amsterdam での3日間。**Stage 4 到達**が複数(Joint Iteration / `Atomics.pause` / Dynamic Code Brand Checks)。Stage 3 へ Iterator Chunking・Iterator Includes・Error stack accessor、Stage 2.7 へ Decorators(本体)と Decorator Metadata が進むなど iterator 系・decorators 周りの advancement が目立った。ほかに Intl(Stable Formatting / Sequence Units / Default Behaviours)、ESM/Source Phase Imports の normative PR、AsyncContext の web 統合、`export defer` / `export all from` / Module Scope Ceiling など module 系を議論。Stage 1 の "Comparisons"(deep comparison/deviation reporting)や、規制動向として **EU CRA(Cyber Resilience Act)** の解説セッションもあった。

## 日次サマリー

- [Day 1 — 2026-05-19](2026-05-19.md)
- [Day 2 — 2026-05-20](2026-05-20.md)
- [Day 3 — 2026-05-21](2026-05-21.md)

## 参加者

`raw/notes/meetings/2026-05/may-19.md` の attendees より(略号 — 氏名 — 所属):

| 略号 | 氏名                   | 所属               |
| ---- | ---------------------- | ------------------ |
| DLM  | Daniel Minor           | Mozilla            |
| USA  | Ujjwal Sharma          | Igalia             |
| SHN  | Samina Husain          | Ecma               |
| CDA  | Chris de Almeida       | IBM                |
| WH   | Waldemar Horwat        | Invited Expert     |
| GTO  | Gustavo Tonietto       | Mozilla            |
| ZTZ  | Zbyszek Tenerowicz     | Consensys          |
| YSZ  | Yusuke Suzuki          | Apple              |
| DJM  | Dmitry Makhnev         | JetBrains          |
| LGH  | Linus Groh             | Bloomberg          |
| JRL  | Justin Ridgewell       | Google             |
| OFR  | Olivier Flückiger      | Google             |
| AUR  | Aurèle Barrière        | CNRS               |
| LPR  | Luna Pfeiffer          | Yavashark          |
| CLA  | Caio Lima              | Igalia             |
| RGN  | Richard Gibson         | Agoric             |
| JHD  | Jordan Harband         | Socket             |
| KM   | Keith Miller           | Apple              |
| BSH  | Bradford C. Smith      | Google             |
| MAH  | Mathieu Hofman         | Agoric             |
| CM   | Chip Morningstar       | Consensys          |
| MBH  | Mikhail Barash         | Univ. of Bergen    |
| RBN  | Ron Buckton            | F5                 |
| RBR  | Ruben Bridgewater      | Datadog            |
| GCL  | Gus Caplan             | Deno               |
| OMT  | Oliver Medhurst        | IE (Porffor)       |
| ABO  | Andreu Botella         | Igalia             |
| CHU  | Christian Ulbrich      | Zalari             |
| TKP  | Tom Kopp               | Zalari             |
| SRV  | Sergey Rubanov         | Invited Expert     |
| EAO  | Eemeli Aro             | Mozilla            |
| LVU  | Lea Verou              | OpenJS             |
| JGT  | Justin Grant           | Invited Expert     |
| NRO  | Nicolò Ribaudo         | Igalia             |
| IS   | Istvan Sebestyen       | Ecma               |
| PFC  | Philip Chimento        | Igalia             |
| AKI  | Aki Braun              | Ecma International |
| KHG  | Kristen Hewell Garrett | Invited Expert     |
| CPC  | Clément Pit-Claudel    | EPFL               |
| LCA  | Luca Casonato          | Invited Expert     |
| MF   | Michael Ficarra        | F5                 |
| PST  | Patrick Soquet         | Moddable           |
| SFC  | Shane Carr             | Google             |

> 出典: tc39/notes PR #411(2026 May transcript、未マージ)を checkout して要約。会期・開催地・概要は [tc39/agendas 2026/05](https://github.com/tc39/agendas/blob/main/2026/05.md) と各日逐語録より。
