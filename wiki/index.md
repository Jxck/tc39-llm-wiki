# TC39 Wiki — Index

TC39 plenary 議事録(`raw/notes`、2012-05〜2026-03 / 86 会合 / 334 ファイル)から、**各提案のステージ遷移の経緯と策定中の論点**を辿るための wiki です。運用規約は [AGENTS.md](../AGENTS.md)、設計思想は [llm-wiki.md](../llm-wiki.md) を参照。

## 使い方

- **全提案の現ステージを一覧する** → [proposals/index.md](proposals/index.md)(`raw/proposals` から生成した全提案の完全ステージ一覧。精読済みはページへリンク)。
- **特定の提案を辿る** → 下の「精読済みの提案」から該当ページへ。各ページに `## ステージ遷移`(時系列テーブル + mermaid グラフ)と `## 主な論点` がある。
- **人物を辿る** → 提案ページ中の人物リンク(例: `[PFC](people/PFC.md)`)をたどると [people/](people/) の人物ページ(フルネーム・所属・担当ドラフト・参加会合)へ。
- **未精読の提案/会合を探す** → [\_generated/agenda-index.md](_generated/agenda-index.md) を grep。全 86 会合・2737 議題を機械抽出したバックボーン。例: `grep -i -A4 'pattern matching' wiki/_generated/agenda-index.md`。
- **新しい提案を ingest** → AGENTS.md の「ワークフロー > Ingest」に従う。

## 精読済みの提案

| 提案                                                                      | 現ステージ          | 状態      | 概要                                                                                             |
| ------------------------------------------------------------------------- | ------------------- | --------- | ------------------------------------------------------------------------------------------------ |
| [Temporal](proposals/temporal.md)                                         | Stage 4 (2026-03)   | shipped   | `Date` を置き換える immutable な日付時刻 API。約 9 年がかりで Stage 4 到達。                     |
| [Decorators](proposals/decorators.md)                                     | Stage 2.7 (2026-05) | stage2.7  | class への `@expr` 注釈。3 度の再設計を経て 2022 Stage 3 も、出荷ゼロで 2026-05 に 2.7 へ降格。  |
| [Records & Tuples](proposals/records-and-tuples.md)                       | Stage 2(撤回)       | withdrawn | deeply immutable な value type `#{}` / `#[]`。2025-04 に撤回。                                   |
| [Upsert](proposals/upsert.md)                                             | Stage 4 (2026-01)   | shipped   | `Map.prototype.getOrInsert` / `getOrInsertComputed`。命名と責務分割で約 6 年難航。               |
| [Intl Era/Month Code](proposals/intl-era-month-code.md)                   | Stage 4 (2026-03)   | shipped   | 非 ISO 8601 カレンダーの era/monthCode を ECMA-402 に規定。Temporal と同時に Stage 4。           |
| [Joint Iteration](proposals/joint-iteration.md)                           | Stage 4 (2026-05)   | shipped   | `Iterator.zip` / `Iterator.zipKeyed`。複数 iterator を位置対応でまとめる。                       |
| [Atomics.pause](proposals/atomics-pause.md)                               | Stage 4 (2026-05)   | shipped   | spin loop 向けの CPU pause ヒント(x86 PAUSE / ARM ISB)。                                         |
| [Explicit Resource Management](proposals/explicit-resource-management.md) | Stage 4 (2026-05)   | shipped   | `using` / `await using` による決定的リソース解放。約 8 年がかり。                                |
| [Intl.MessageFormat](proposals/intl-messageformat.md)                     | Stage 1 (2022-03)   | stage1    | MessageFormat 2.0 (MF2) を JS に公開。DSL/parser を言語に入れる是非で stuck。                    |
| [Amount](proposals/amount.md)                                             | Stage 2 (2026-05)   | stage2    | 数値+単位の immutable value type(旧 Measure)。`convertTo()` と i18n 連携。                       |
| [Iterator Chunking](proposals/iterator-chunking.md)                       | Stage 3 (2026-05)   | stage3    | `Iterator.prototype.chunks` / `windows`。固定長/スライディングで複数値消費。                     |
| [Iterator Includes](proposals/iterator-includes.md)                       | Stage 3 (2026-05)   | stage3    | `Array.prototype.includes` の iterator 版。                                                      |
| [Iterator Join](proposals/iterator-join.md)                               | Stage 3 (2026-05)   | stage3    | `Array.prototype.join` の iterator 版。                                                          |
| [RegExp Buffer Boundaries](proposals/regexp-buffer-boundaries.md)         | Stage 3 (2026-05)   | stage3    | `\A` / `\z` / `\Z` の buffer 境界アンカー(`m` flag 非依存)。2026-05 に一気に Stage 3。           |
| [Dynamic Code Brand Checks](proposals/dynamic-code-brand-checks.md)       | Stage 3 (2024-04)   | stage3    | `eval` / `new Function` の Trusted Types 連携。2026-05 は normative change で Stage 4 持ち越し。 |
| [Error Stack Accessor](proposals/error-stack-accessor.md)                 | Stage 3 (2026-05)   | stage3    | `Error.prototype.stack` を accessor として標準化(Error Stacks からの carve-out)。                |
| [Intl Keep Trailing Zeros](proposals/intl-keep-trailing-zeros.md)         | Stage 3 (2026-05)   | stage3    | `Intl.NumberFormat` / `PluralRules` で末尾の小数ゼロを保持。                                     |
| [Stable Formatting](proposals/stable-formatting.md)                       | Stage 2 (2026-05)   | stage2    | `zxx` ロケールで locale 非依存の安定整形。`Intl` の誤用/テスト用途の代替。                       |
| [Intl Sequence Units](proposals/intl-sequence-units.md)                   | Stage 2 (2026-05)   | stage2    | 複合単位の並び(例 `6 ft 0 in`)整形。object ベース入力で Stage 2。                                |
| [Intl Default Behaviours](proposals/intl-default-behaviours.md)           | Stage 1 (2026-05)   | stage1    | `Collator` / `Segmenter` の locale 非依存デフォルト(`und` root)。Stable Formatting の補完。      |
| [export all from](proposals/export-all-from.md)                           | Stage 1 (2026-05)   | stage1    | `export * from` 系の re-export 構文拡張。                                                        |
| [Comparisons](proposals/comparisons.md)                                   | Stage 1 (2026-05)   | stage1    | 深い比較と差分報告(deviation)を native 化。旧 "Assertions"。                                     |
| [Array.isTemplateObject](proposals/is-template-object.md)                 | Stage 2(inactive)   | inactive  | template call-site object の判定。2026-05 に inactive 化(需要不足 + realm 懸念)。                |

## family(カテゴリ横断のまとめ)

同じカテゴリにくくれる提案群を横断的にまとめた synthesis ページ。個別の経緯は各提案ページ、全体像と stage 一覧は family ページで辿れる。

- [Iterator helpers and friends](families/iterator.md) — `Iterator.prototype` まわりの lazy 反復ライブラリ群(helpers / zip / concat / chunking / includes / async 系ほか)。
- [Modules (module harmony)](families/modules.md) — ES Modules と派生提案群(dynamic import / import.meta / TLA / import attributes / phase imports / import-export defer ほか)。

## 未作成(リンク先候補)

精読済みページから参照されているが、まだ作成されていない提案ページ:

- `class-fields` — Decorators と sigil(`@` / `#`)を巡って密接に関係。
- `private-methods` — class fields 関連。
- `pipeline-operator` — Decorators の議論で言及。

## 人物ページ(people/)

提案ページ・family ページに登場する人物を [people/](people/) に集約(現在 60 名)。各ページは略号をファイル名とし、フルネーム・所属・担当ドラフト(champion)・言及される提案/family・参加したミーティングを持つ。`tools/extract_people.py` が提案・family ページから登場略号を検出して生成し、`tools/link_people.py` が本文の略号を `[ABBR](../people/ABBR.md)` にリンクする(VSCode プレビューで遷移できる標準 markdown リンク)。登場人物のみを対象とし、ページの追加に追従して自動で増える。

## バックボーン(機械抽出)

[\_generated/agenda-index.md](_generated/agenda-index.md) — 全会合の議題見出し・Stage シグナル・Conclusion を `tools/extract_agenda.py` で抽出したもの。手で編集しない(再生成で上書き)。素材(submodule)更新後は `python3 tools/extract_agenda.py && python3 tools/extract_proposals.py && python3 tools/extract_people.py && python3 tools/link_people.py` で更新。

## 状態の凡例

`stage0`〜`stage3`(`stage2.7` を含む) / `shipped`(Stage 4 到達) / `withdrawn`(撤回) / `inactive`(長期停滞)。各ページ frontmatter の `status` と対応。
