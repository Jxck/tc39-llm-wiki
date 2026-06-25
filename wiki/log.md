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

## [2026-06-25] lint | 精読3ページの事実検証と修正

各提案ページの主張を引用元逐語録と突合(誤りを探す検証)。発見した誤りを修正:

- **Temporal**: (1) 「V8 はこの scope reduction を…」の引用は JGT ではなく **SYG の prepared statement** → 発話者を明記。(2) IDL/JSIDL 節は Temporal 審議ではなく同会合の**別アジェンダ「IDL for JavaScript」** → その旨補正。(3) 2025-04 は「Firefox 139 で出荷」ではなく**出荷予定** → 修正。
- **Decorators**: (1) `@` 文法衝突の AWB 指摘は 2014-01 ではなく **2015-01**。(2) 2016-09 sigil swap の反対理由を EFT/AWB に誤帰属していた点を補正(EFT は疑問提起のみ、AWB の論拠は逆向き)。(3) export ordering の `toString` 論拠の主唱者は **MM**、WH 引用は **2018-05** かつ条件付き → 修正。(4) 2021-07「reviewer 任命」→「募集」。
- **Records & Tuples**: champion の**人物取り違えを修正**。`RRI`(delegates.txt=Reefath Rajali)を Robin Ricard と混同していた。Robin Ricard は本 wiki では `RRD` に統一(2019-10 の出席者表が局所的に Robin へ別 delegate と同じ略号を当てていたのが原因)。frontmatter・本文・people ページを再生成し、誤った人物ページ RRI.md を除去(人物 42 名)。

ステージ遷移の骨格・大半の発言帰属は逐語録と整合しており、致命的な事実誤認はなし。

## [2026-06-25] update | 運用合意を AGENTS.md に反映・Update コマンド追加

- 今セッションで決まった wiki 運用の合意を AGENTS.md に明文化:
  - ステージ推移グラフは **xychart-beta 折れ線**(横軸 2012-2026 固定・下から積み上げ)、**撤回は撤回年で線を止める**・停滞は横ばい。
  - **champion の確定は delegates.txt だけで決めず、当該会合の Presenter 行で裏取り**する(略号は会合ごとに振り直されうる。RRI/RRD の教訓)。発言帰属・年月も原文確認。
  - (既反映)発言引用は日本語訳/リンクは標準 markdown 相対リンク/人物ページは登場者のみ生成。
- ワークフローに **Update** を追加:会話で決まった「wiki の動き方に関する取り決め」を AGENTS.md に反映し log に記録する操作。判断基準は「他エージェントにも必要な運用上の取り決めか」。

## [2026-06-25] update | Lint の定義拡張(Verify を統合)

- Lint の定義を拡張し、(a) 内部健全性(矛盾・孤立・陳腐化・カバレッジ)に加え、(b) 出典との整合性(wiki ↔ raw の突き合わせ検証=旧 Verify)の両方を含むものとした。独立した Verify 操作は設けず Lint に一本化。

## [2026-06-25] update | Query に file back 確認ステップを追加

- Query の手順に「回答が価値ある分析を含む場合は、最後にユーザへ wiki ページとして残すか確認する(勝手に追加しない)」を明記。残す場合は synthesis ページとして file back し index/log を更新。

## [2026-06-25] update | Ingest/Lint をスラッシュコマンド化

- `.claude/commands/ingest.md`・`lint.md` を追加し、`/ingest <提案>`・`/lint [対象]` で起動可能に。中身は AGENTS.md の該当ワークフローを正本として参照する薄いラッパ。AGENTS.md のワークフロー冒頭にも存在を明記。

## [2026-06-25] update | 全ワークフローをコマンド化・定義を AGENTS.md に一本化

- `/query`・`/update` を追加し、4 操作(ingest/query/lint/update)すべてをスラッシュコマンド化。
- 既存の ingest/lint コマンドから再掲していた手順を削除し、**全コマンドを「AGENTS.md の該当セクションを読んで実行するだけ」のポインタに統一**。定義の正本は AGENTS.md のみ(二重メンテ解消)。

## [2026-06-25] update | コミット規約を追加

- AGENTS.md ワークフローに「各操作の完了時に、操作名プレフィックス付きメッセージでコミットする(`[ingest]`/`[query]`/`[lint]`/`[update]`)」を全操作共通ルールとして追加。定義は AGENTS.md の1か所のみ(各コマンドは参照)。

## [2026-06-25] wiki | コミットプレフィックス [wiki] を追加

- 操作(ingest/query/lint/update)に起因しない wiki 全体の変更(コマンドの追加・変更、tools/ の変更、リポジトリ構成や AGENTS.md の構造変更など)は `[wiki]` プレフィックスでコミットする規約を追加。

## [2026-06-25] wiki | Summarise コマンドを追加

- 会合を話題単位で日次要約する `/summarise` を追加(出力 `wiki/meetings/<YYYY-MM>/`、日ごとに 1 ファイル + index.md)。フォーマット定義は AGENTS.md の「ワークフロー > Summarise」。コミットプレフィックスに `[summarise]` を追加。

## [2026-06-25] update | Summarise に既存提案ページへのリンク規約を追加

- 要約のトピックが既存の提案ページ(`wiki/proposals/<slug>.md`)に該当する場合、Slides の次に `- 提案ページ: [Title](../../proposals/<slug>.md)` を置く規約を AGENTS.md の Summarise に追加。

## [2026-06-25] summarise | 113th TC39 Meeting (2026-03)

- 最新会合 2026-03(113th, New York)を日次要約。`wiki/meetings/2026-03/` に Day 1-3 + index.md を生成。index は tc39/agendas 2026/03 へリンクし、会期・開催地・概要・参加者をまとめた。Day 2 の Temporal トピックは [Temporal](proposals/temporal.md) 提案ページへリンク。
