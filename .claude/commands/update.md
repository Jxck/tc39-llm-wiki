---
description: raw/ 配下の submodule を最新に pull し、前回同期からの差分を表示する
argument-hint: "[対象 submodule (省略時は raw/ 配下すべて)]"
---

`AGENTS.md` の「## ワークフロー > ### Update」を読み、その手順に従って実行してください。対象: **$ARGUMENTS**(未指定なら `raw/` 配下のすべての submodule)。

- 手順・コミット規約・log 記録の定義は `AGENTS.md` が正本。ここには再掲しない。
- 前回同期の状態はコミット済みの submodule ポインタが基準。差分が無ければ「最新」と表示し commit はスキップする。
