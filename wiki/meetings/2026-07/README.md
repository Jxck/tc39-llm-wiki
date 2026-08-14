# 115th TC39 Meeting (2026-07)

- **会合**: 115th meeting of Ecma TC39
- **会期**: 2026-07-20 〜 2026-07-22(3 日間)
- **開催地**: リモート(次回は東京・Sony Interactive Entertainment(品川)でのオンサイト/ハイブリッド開催をアナウンス)
- **ホスト**: -(リモート会合のためホスト企業なし)
- **Agenda**: [tc39/agendas 2026/07](https://github.com/tc39/agendas/blob/main/2026/07.md)

## 概要

ECMA-262 / ECMA-402 の提案審議が中心の 3 日間リモート会合。**[Await Dictionary](../../proposals/await-dictionary.md)(`Promise.allKeyed` / `allSettledKeyed`)が Stage 3**、**[Thenable Curtailment](../../proposals/thenable-curtailment.md) が host hook の整備を経て Stage 2.7**、**[Error code property](../../proposals/error-code-property.md) と [Fused Multiply-Add](../../proposals/fused-multiply-add.md)(`Math.fma`)が Stage 2**、**bigint-from-exponential(needs-consensus PR から転換)・[Map take](../../proposals/map-get-and-delete.md)(`getAndDelete` へ rename)・[Linear Matching](../../proposals/linear-matching.md)(ReDoS 対策)・`Intl.DateTimeFormat` Alignment With Other Standards が Stage 1** に到達した。Declarations in Conditionals は pattern matching との調整未了で advancement を見送り。

normative では `Promise.try` の非エラー時 PromiseResolve 化、custom global object への built-ins 定義強制(PR #3728)、Import Defer の cycle root バグ修正、ECMA-402 の Intl Locale Info 系 4 PR に consensus。6 月 30 日の Ecma General Assembly では **ECMA-262 17th / ECMA-402 13th(= ES2026)が全会一致で承認**され、[KG](../../people/KG.md) が Ecma Recognition Award を受賞した。[MF](../../people/MF.md) による提案・delegate 情報の構造化データ(`@tc39/data`)構想、Composites の interning 方式への pivot、Decimal の object API vs primitive の膠着も注目点。

## 日次サマリー

- [Day 1 — 2026-07-20](2026-07-20.md)
- [Day 2 — 2026-07-21](2026-07-21.md)
- [Day 3 — 2026-07-22](2026-07-22.md)

## Stage 遷移まとめ

| 提案                                                                             | 遷移                                        | 日    |
| -------------------------------------------------------------------------------- | ------------------------------------------- | ----- |
| [Await Dictionary](../../proposals/await-dictionary.md)                          | 2.7 → 3                                     | Day 1 |
| [Thenable Curtailment](../../proposals/thenable-curtailment.md)                  | 2 → 2.7                                     | Day 3 |
| [Error code property](../../proposals/error-code-property.md)                    | 1 → 2(DOMException 整合が advancement 条件) | Day 2 |
| [Fused Multiply-Add](../../proposals/fused-multiply-add.md) (`Math.fma`)         | 1 → 2                                       | Day 3 |
| bigint-from-exponential                                                          | 新規 → 1(needs-consensus PR #3857 から転換) | Day 1 |
| [Map take](../../proposals/map-get-and-delete.md)(`getAndDelete` へ rename 予定) | 新規 → 1                                    | Day 2 |
| [Linear Matching](../../proposals/linear-matching.md)                            | 新規 → 1                                    | Day 3 |
| `Intl.DateTimeFormat` Alignment With Other Standards                             | 新規 → 1                                    | Day 3 |
| Declarations in Conditionals                                                     | 見送り(pattern matching と要調整)           | Day 2 |

## 参加者

各日冒頭の出席者テーブルより(3 日間の合算、順不同): [CDA](../../people/CDA.md), [USA](../../people/USA.md), [JRL](../../people/JRL.md), [DLM](../../people/DLM.md)(chairs/facilitators)、[WH](../../people/WH.md), BSH, [LVU](../../people/LVU.md), [KM](../../people/KM.md), [ACE](../../people/ACE.md), AKI, LGH, IS, [NRO](../../people/NRO.md), [PFC](../../people/PFC.md), [CM](../../people/CM.md), [EAO](../../people/EAO.md), CLA, [OFR](../../people/OFR.md), NPU, [RGN](../../people/RGN.md), [JSL](../../people/JSL.md), [GB](../../people/GB.md), [DRO](../../people/DRO.md), SHN, LPR, [KG](../../people/KG.md), [MF](../../people/MF.md), [MM](../../people/MM.md), PKA, [SHS](../../people/SHS.md), [DJM](../../people/DJM.md), [JHD](../../people/JHD.md), [MAG](../../people/MAG.md), [SFC](../../people/SFC.md), [AUR](../../people/AUR.md), [CPC](../../people/CPC.md) ほか。
