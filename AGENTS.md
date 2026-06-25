# TC39 Wiki — Agent Schema

このリポジトリは TC39 plenary の議事録(`raw/notes`)を素材に、**「各提案がどういう経緯でステージを変えてきたか」「策定途中で何が論点になったか」を後から辿れる wiki** を LLM が構築・維持するためのものです。設計思想は [llm-wiki.md](llm-wiki.md) を参照。

このファイルは wiki の運用規約(schema)です。新しいセッションはまずこれを読み、規約に従って ingest / query / lint を行ってください。

## レイヤ

- **Raw sources** — `raw/notes/`(tc39/notes の submodule)。**読み取り専用・不変**。絶対に編集しない。これが唯一の真実。
- **The wiki** — `wiki/`。LLM が全面的に所有。提案ページ・index・log を生成/更新する。
- **Generated** — `wiki/_generated/`。`tools/` のスクリプトによる機械抽出物。**手で編集しない**(再生成で上書きされる)。

## ディレクトリ構成

```
raw/notes/meetings/<YYYY-MM>/<month-DD>.md   素材(逐語録)
wiki/
  index.md                  提案カタログ(現ステージ付き、カテゴリ別)
  log.md                    時系列の ingest/query/lint ログ(append-only)
  proposals/<slug>.md       提案ごとの精読ページ(経緯+論点)
  _generated/
    agenda-index.md         全86会合の議題インデックス(grep 用バックボーン)
    agenda-index.jsonl      同上の機械可読版
tools/
  extract_agenda.py         agenda-index の生成スクリプト
```

## 言語規約

- 地の文(概要・経緯・論点の説明)は **日本語**。
- **提案名・Stage 表記・API 名・spec 用語・人物の略号(略号は原文のまま)は英語**。例: `Temporal`, `Stage 2.7`, `Array.fromAsync`, `[[Get]]`, `PFC`。
- 引用は原文(英語)のまま短く引く。

## 提案ページの形式

`wiki/proposals/<slug>.md`。`<slug>` は kebab-case の英語(例: `temporal`, `decorators`, `records-and-tuples`)。

先頭に YAML frontmatter(Obsidian Dataview 用):

```yaml
---
title: Temporal
slug: temporal
status: shipped        # stage0 | stage1 | stage2 | stage3 | shipped | withdrawn | inactive
current_stage: 4       # 0 / 1 / 2 / 2.7 / 3 / 4
ecma: [262, 402]       # 影響する仕様
champions: [PFC, ...]  # 略号
first_seen: "2017-09"  # 初出会合(YYYY-MM)
reached_stage4: "2026-03"
tags: [proposal, date-time]
---
```

本文セクション(見出しは固定):

1. `## 概要` — 1〜3 段落。何を解決する提案か。
2. `## ステージ遷移` — 時系列テーブル。1 行 = 1 イベント:

   | 会合 | できごと | Stage |
   |------|----------|-------|
   | [2018-09](../_generated/agenda-index.md) | Stage 2 到達。`Temporal for Stage 2` | 1 → 2 |

   会合セルは `raw/notes` の該当ファイルへ相対リンク(例: `[2018-09](../../raw/notes/meetings/2018-09/sept-27.md)`)。Stage 列は遷移を `旧 → 新`、更新のみなら現ステージを記す。
3. `## 主な論点` — 策定途中で問題になった点。論点ごとに小見出し `### <論点名>`。各論点に: 何が争点か / 誰が懸念したか(略号) / どの会合で / どう決着したか(または未決)。短い原文引用を `>` で添えてよい。
4. `## 関連提案` — `[[other-slug]]` 形式で相互リンク。
5. `## 出典` — 参照した会合ファイルの一覧(箇条書きリンク)。

リンク規約: 提案間は Obsidian wikilink `[[slug]]`。素材へは相対パスの markdown リンク。

## ワークフロー

### Ingest(素材の取り込み)

1. 対象会合 or 提案を決める。`wiki/_generated/agenda-index.md` を grep して関連議題と会合を特定する(例: `grep -i -A4 decorators wiki/_generated/agenda-index.md`)。
2. 該当する `raw/notes` のセクションを読む(`### Conclusion` と `### Speaker's Summary of Key Points` がステージ判定の要)。
3. 提案ページを新規作成 or 更新: ステージ遷移テーブルに行を追加、論点を追記/更新、frontmatter の `current_stage`/`status` を最新化。
4. `wiki/index.md` のカタログ行を更新。
5. `wiki/log.md` に 1 行追記。

### Query(質問への回答)

1. `wiki/index.md` → 関連提案ページ → 必要なら `agenda-index.md` → `raw/notes` の順で掘る。
2. 回答は出典(会合リンク)付き。価値ある分析は新しい wiki ページとして還元してよい。

### Lint(健全性チェック)

- ページ間の矛盾、古くなった記述(新しい会合で覆された主張)、孤立ページ、相互リンク漏れ、論点の決着漏れを点検。
- `agenda-index.md` に出てくるが提案ページが無い重要提案を洗い出す。
- 素材更新時(submodule pull 後)は `python3 tools/extract_agenda.py` で再生成。

## バックボーンの使い方(重要)

全 86 会合・2737 議題は `wiki/_generated/agenda-index.md` に機械抽出済み。これは精読の代替ではなく**索引**。提案ページを書く/辿るときは、まずここを grep して「どの会合で議論されたか」を掴み、その会合の原文を読んで論点を埋める。提案名は年で揺れる(改名・別名)ので、grep は別名でも試す。

## TC39 のステージ(参考)

- **Stage 0** Strawperson / **Stage 1** Proposal(検討開始) / **Stage 2** Draft(API 概形合意) / **Stage 2.7** (2023 新設) テスト・spec レビュー完了待ち / **Stage 3** Candidate(実装待ち) / **Stage 4** Finished(本体へマージ、出荷)。
- Stage 2.7 は 2023-11 前後に導入。それ以前の提案は 2 → 3 を直接遷移している。

## スコープの注記

素材は 334 ファイル・2012〜2026。全件の精読は段階的に行う。現時点で精読済みの提案は `wiki/index.md` の「精読済み」セクションに、未精読(バックボーンのみ)は agenda-index 参照とする。
