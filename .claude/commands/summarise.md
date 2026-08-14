---
description: 会合を話題単位で日次要約し wiki/meetings/ にまとめる
argument-hint: "[会合 (YYYY-MM) | tc39/notes の PR 番号/URL (省略時は raw/notes の最新会合)]"
---

`AGENTS.md` の「## ワークフロー > ### Summarise」を読み、その手順とフォーマットに従って会合を要約してください。対象: **$ARGUMENTS**(未指定なら `raw/notes/meetings/` の最新会合)。

- 対象が tc39/notes の PR 番号または URL の場合は、AGENTS.md の「未マージ PR にしかない会合を要約する場合」の手順で `pr-<PR>` を checkout してから、その PR が追加する会合を要約する。
- フォーマット・出力先・index の作り方・リンク生成(人物/提案)の定義は `AGENTS.md` が正本。ここには再掲しない。
- 各日ファイルは独立して読めるので、日ごとに並列で処理してよい。
