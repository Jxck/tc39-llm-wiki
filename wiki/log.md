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
