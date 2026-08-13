# 115th TC39 Meeting (2026-07)

- **会合**: 115th meeting of Ecma TC39
- **会期**: 2026-07-20 〜 2026-07-22(3 日間)
- **開催地**: リモート(次回は東京・Sony Interactive Entertainment(品川)でのオンサイト/ハイブリッド開催をアナウンス)
- **ホスト**: -(リモート会合のためホスト企業なし)
- **Agenda**: [tc39/agendas 2026/07](https://github.com/tc39/agendas/blob/main/2026/07.md)

## 概要

ECMA-262 / ECMA-402 の提案審議が中心の 3 日間リモート会合。**Await Dictionary(`Promise.allKeyed` / `allSettledKeyed`)が Stage 3**、**Thenable Curtailment が host hook の整備を経て Stage 2.7**、**Error code property と Fused Multiply-Add(`Math.fma`)が Stage 2**、**bigint-from-exponential(needs-consensus PR から転換)・Map take(`getAndDelete` へ rename)・Linear Matching(ReDoS 対策)・`Intl.DateTimeFormat` Alignment With Other Standards が Stage 1** に到達した。Declarations in Conditionals は pattern matching との調整未了で advancement を見送り。

normative では `Promise.try` の非エラー時 PromiseResolve 化、custom global object への built-ins 定義強制(PR #3728)、Import Defer の cycle root バグ修正、ECMA-402 の Intl Locale Info 系 4 PR に consensus。6 月 30 日の Ecma General Assembly では **ECMA-262 17th / ECMA-402 13th(= ES2026)が全会一致で承認**され、KG が Ecma Recognition Award を受賞した。MF による提案・delegate 情報の構造化データ(`@tc39/data`)構想、Composites の interning 方式への pivot、Decimal の object API vs primitive の膠着も注目点。

## 日次サマリー

- [Day 1 — 2026-07-20](2026-07-20.md)
- [Day 2 — 2026-07-21](2026-07-21.md)
- [Day 3 — 2026-07-22](2026-07-22.md)

## Stage 遷移まとめ

| 提案                                                 | 遷移                                        | 日    |
| ---------------------------------------------------- | ------------------------------------------- | ----- |
| Await Dictionary                                     | 2.7 → 3                                     | Day 1 |
| Thenable Curtailment                                 | 2 → 2.7                                     | Day 3 |
| Error code property                                  | 1 → 2(DOMException 整合が advancement 条件) | Day 2 |
| Fused Multiply-Add (`Math.fma`)                      | 1 → 2                                       | Day 3 |
| bigint-from-exponential                              | 新規 → 1(needs-consensus PR #3857 から転換) | Day 1 |
| Map take(`getAndDelete` へ rename 予定)              | 新規 → 1                                    | Day 2 |
| Linear Matching                                      | 新規 → 1                                    | Day 3 |
| `Intl.DateTimeFormat` Alignment With Other Standards | 新規 → 1                                    | Day 3 |
| Declarations in Conditionals                         | 見送り(pattern matching と要調整)           | Day 2 |

## 参加者

各日冒頭の出席者テーブルより(3 日間の合算、順不同): CDA, USA, JRL, DLM(chairs/facilitators)、WH, BSH, LVU, KM, ACE, AKI, LGH, IS, NRO, PFC, CM, EAO, CLA, OFR, NPU, RGN, JSL, GB, DRO, SHN, LPR, KG, MF, MM, PKA, SHS, DJM, JHD, MAG, SFC, AUR, CPC ほか。
