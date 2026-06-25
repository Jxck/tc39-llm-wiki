# Log

wiki の ingest / query / lint の時系列記録(append-only)。各行は `## [YYYY-MM-DD] <種別> | <内容>` で始める。`grep "^## \[" wiki/log.md | tail -5` で直近を確認できる。

## [2026-06-25] setup | wiki 初期構築

- 運用規約 [AGENTS.md](../AGENTS.md) を策定(レイヤ・提案ページ形式・言語規約・ワークフロー)。
- `tools/extract_agenda.py` を作成し、全 86 会合 / 2737 議題のバックボーン [_generated/agenda-index.md](_generated/agenda-index.md) を生成。
- 代表 3 提案を精読してページ化:
  - [Temporal](proposals/temporal.md) — shipped(Stage 4 / 2026-03)。「長期で出荷に至った大型提案」の実例。
  - [Decorators](proposals/decorators.md) — stage3(Stage 3 / 2022-03)。「3 度再設計した難航提案」の実例。
  - [Records & Tuples](proposals/records-and-tuples.md) — withdrawn(2025-04)。「停滞の末に撤回された提案」の実例。
- [index.md](index.md) を作成。

## [2026-06-25] update | 人物ページ・引用翻訳・ステージ推移グラフ

- 提案ページの英文引用(セリフ)を日本語訳に統一。AGENTS.md の言語規約に翻訳ルールを追記。
- `tools/extract_people.py` / `tools/link_people.py` を追加。提案ページに登場する 43 名の人物ページを [people/](people/) に生成し、本文の略号を `[[ABBR]]` にリンク。語と衝突する `API`/`JS` は denylist で除外。
- [Temporal](proposals/temporal.md) のステージ遷移テーブル下に mermaid `xychart-beta` のステージ推移グラフ(横軸=2012-2026 全区間、縦軸=Stage、下から積み上がる折れ線)を追加。bierner.markdown-mermaid では空描画だったが別の mermaid 拡張で描画可と確認。AGENTS.md に xychart-beta 形式を規約化(title は ASCII 推奨)。

## [2026-06-25] update | グラフを全提案へ展開・リンクを markdown 化

- ステージ推移グラフを [Decorators](proposals/decorators.md)(2016-2021 が Stage 2 横ばい→2022 Stage 3)と [Records & Tuples](proposals/records-and-tuples.md)(2025-04 撤回で線を止める)にも追加。
- **VSCode の markdown プレビューは Obsidian `[[wikilink]]` を遷移できない**ため、wiki 内のリンクをすべて標準 markdown 相対リンクに変更。`link_people.py` は人物略号を `[ABBR](../people/ABBR.md)` にリンク(既存 `[[ABBR]]` も自動移行)、`extract_people.py` は人物ページの提案リンクを `[Title](../proposals/slug.md)` 出力に変更。未作成提案向けの `[[slug]]` はデッドリンク回避でコード表記の素テキストに。AGENTS.md のリンク規約を更新。
