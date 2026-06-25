# TC39 Wiki — Agent Schema

このリポジトリは TC39 plenary の議事録(`raw/notes`)を素材に、**「各提案がどういう経緯でステージを変えてきたか」「策定途中で何が論点になったか」を後から辿れる wiki** を LLM が構築・維持するためのものです。設計思想は [llm-wiki.md](llm-wiki.md) を参照。

このファイルは wiki の運用規約(schema)です。新しいセッションはまずこれを読み、規約に従って ingest / query / lint を行ってください。

## レイヤ

- **Raw sources** — `raw/`(submodule 群)。**読み取り専用・不変**。絶対に編集しない。これが真実の素材。
  - `raw/notes/`(tc39/notes) — plenary の逐語録。**経緯・論点・発言の一次ソース**。
  - `raw/proposals/`(tc39/proposals) — 提案の正典リスト(現ステージ別テーブル + champions)。**現ステージ・status・champion の確定値の一次ソース**。
- **The wiki** — `wiki/`。LLM が全面的に所有。提案ページ・index・log を生成/更新する。
- **Generated** — `wiki/_generated/` と `wiki/people/`。`tools/` のスクリプトによる機械抽出物。**手で編集しない**(再生成で上書きされる)。

**ソース間の優先順位(precedence)**: 食い違ったときにどれを信じるか。

- 経緯(ステージ遷移の年月・方向)・論点・発言の帰属 → **`raw/notes`** が一次。
- 提案の**現ステージ(`current_stage` / `status`)と champion** の確定値 → **`raw/proposals`** が一次。notes から推論した現ステージが proposals と食い違ったら、まず notes 側の読み取りを疑い、両者を辿り直して解決する。
- `raw/proposals` は**現在のスナップショット**であり経緯は持たない。逆に notes は経緯を語るが現ステージの確定には弱い。役割が異なるので、片方だけで埋めず両者を突き合わせる。

## ディレクトリ構成

```
raw/notes/meetings/<YYYY-MM>/<month-DD>.md   素材(逐語録)
raw/proposals/README.md                      Active 提案テーブル(Stage 3 / 2.7 / 2)
raw/proposals/finished-proposals.md          Stage 4(出荷済み)
raw/proposals/stage-1-proposals.md           Stage 1
raw/proposals/inactive-proposals.md          withdrawn / inactive
wiki/
  index.md                  提案カタログ(現ステージ付き、カテゴリ別)
  log.md                    時系列の ingest/query/lint ログ(append-only)
  proposals/<slug>.md       提案ごとの精読ページ(経緯+論点)
  families/<family>.md      カテゴリ横断のまとめ(複数提案を束ねる synthesis。個別の経緯は proposals を参照)
  meetings/<YYYY-MM>/        会合の日次要約(summarise の出力。日ごと 1 ファイル + index.md)
  people/<ABBR>.md          人物リファレンス(生成物。filename = 略号)
  _generated/
    agenda-index.md         全86会合の議題インデックス(grep 用バックボーン)
    agenda-index.jsonl      同上の機械可読版
tools/
  extract_agenda.py         agenda-index の生成スクリプト
  extract_people.py         提案ページに登場する人物の people/ ページ生成
  link_people.py            提案ページ中の略号を [ABBR](../people/ABBR.md) にリンク
```

## 言語規約

- 地の文(概要・経緯・論点の説明)は **日本語**。
- **提案名・Stage 表記・API 名・spec 用語・人物の略号(略号は原文のまま)は英語**。例: `Temporal`, `Stage 2.7`, `Array.fromAsync`, `[[Get]]`, `PFC`。
- **議事録から発言(セリフ)を引用するときは日本語に翻訳する**。原文が英文一文以上のときは訳文を載せる(例: WH「変えないでほしい」)。単語・短い専門句(`muddled`, `uninitialized function` 等)は英語のままでよい。提案名やアジェンダ項目名のような固有のタイトルは原文のまま。

## 提案ページの形式

`wiki/proposals/<slug>.md`。`<slug>` は kebab-case の英語(例: `temporal`, `decorators`, `records-and-tuples`)。

先頭に YAML frontmatter(Obsidian Dataview 用):

```yaml
---
title: Temporal
slug: temporal
status: shipped        # stage0 | stage1 | stage2 | stage2.7 | stage3 | shipped | withdrawn | inactive
current_stage: 4       # 0 / 1 / 2 / 2.7 / 3 / 4
ecma: [262, 402]       # 影響する仕様
champions: [PFC, ...]  # 略号
first_seen: "2017-09"  # 初出会合(YYYY-MM)
reached_stage4: "2026-03"
families: [date-time]  # 所属する family(任意・複数可。`wiki/families/<family>.md` と双方向に対応)
tags: [proposal, date-time]
---
```

本文セクション(見出しは固定):

1. `## 概要` — 1〜3 段落。何を解決する提案か。
2. `## ステージ遷移` — 時系列テーブル。1 行 = 1 イベント:

   | 会合                                     | できごと                             | Stage |
   | ---------------------------------------- | ------------------------------------ | ----- |
   | [2018-09](../_generated/agenda-index.md) | Stage 2 到達。`Temporal for Stage 2` | 1 → 2 |

   会合セルは `raw/notes` の該当ファイルへ相対リンク(例: `[2018-09](../../raw/notes/meetings/2018-09/sept-27.md)`)。Stage 列は遷移を `旧 → 新`、更新のみなら現ステージを記す。テーブルの直後に、下記のステージ推移グラフを置く。

3. ステージ推移グラフ — テーブルの下に mermaid `xychart-beta` の折れ線を埋め込む。**横軸は議事録のある全区間(2012〜2026 の年)固定**、縦軸は Stage (0〜4)。各年末時点の stage を下から積み上げる形で並べる。提案が存在しない年は 0。Stage 2.7 を経た提案は `2.7` を小数点で打つ。**撤回された提案は撤回年で線を止める**(line 配列をそこで終え、以降の点を描かない)。長期停滞は同じ値の横ばいで自然に表現される(特別な印は不要)。グラフ直後に読み方の注記(各遷移の年月)を `>` で添える。例:

   ````
   ```mermaid
   xychart-beta
       title "Temporal stage 2012-2026"
       x-axis [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
       y-axis "Stage" 0 --> 4
       line [0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4]
   ```
   ````

   注: `xychart-beta` は mermaid 10.3+ が必要。VSCode の `bierner.markdown-mermaid` の webview プレビューでは空描画になる(別の mermaid 拡張なら描画可)ため、レンダラ依存に注意。title は ASCII 推奨(全角・em ダッシュ・括弧で parse が崩れる環境がある)。

4. `## 主な論点` — 策定途中で問題になった点。論点ごとに小見出し `### <論点名>`。各論点に: 何が争点か / 誰が懸念したか(略号) / どの会合で / どう決着したか(または未決)。発言引用は `>` で(日本語訳)。
5. `## 関連提案` — `[Title](../proposals/other-slug.md)` 形式で相互リンク(未作成提案はコード表記の素テキスト)。
6. `## 出典` — 参照した会合ファイルの一覧(箇条書きリンク)。

リンク規約: **すべて標準の markdown 相対リンク**を使う(Obsidian の `[[wikilink]]` は VSCode の markdown プレビューで遷移できないため使わない。標準リンクは VSCode でも Obsidian でも動く)。

- 素材へ: `[2018-09](../../raw/notes/meetings/2018-09/sept-27.md)`
- 提案間: `[Temporal](../proposals/temporal.md)`。まだ作成していない提案はデッドリンクを避け、コード表記の素テキスト(例: `` `pattern-matching` ``)で書き、作成時にリンク化する。
- 人物の略号: `[PFC](../people/PFC.md)`。リンク付けは手作業ではなく `tools/link_people.py` が行う(下記。既存の `[[ABBR]]` も自動で markdown リンクへ移行する)。frontmatter の `champions` は YAML なのでリンクにしない(略号のまま)。

## family ページの形式

`wiki/families/<family>.md`。同じカテゴリにくくれる提案群(例: `iterator`, `modules`, `intl`, `date-time`, `class-features`, `concurrency`)を**横断的にまとめる synthesis ページ**。個別提案の経緯・論点は `proposals/` に置き、family からはリンクするだけ(ステージ遷移テーブルや mermaid を family に複製しない。二重メンテを避ける)。`<family>` は kebab-case。

先頭に YAML frontmatter:

```yaml
---
title: Iterator helpers and friends
slug: iterator
kind: family
members: [iterator-helpers, joint-iteration, iterator-chunking, ...]  # 提案 slug。未作成提案も slug で列挙してよい
tags: [family, iterator]
---
```

本文セクション(見出しは固定):

1. `## 概要` — 何が共通項か(この family がまとめる軸)。
2. `## メンバー` — テーブル `提案 | 現ステージ | 一言`。提案ページがあれば `[Title](../proposals/<slug>.md)`、無ければコード表記の素テキスト。
3. `## 横断テーマ` — family を貫く設計方針・論点(例: iterator の「文字列を暗黙 iterate しない」一貫方針、laziness、async 対応)。
4. `## 関連 family` — 隣接 family へのリンク(`[Title](../families/<slug>.md)`)。
5. `## 出典`(任意)。

**メンバーシップは双方向**で持つ: family ページの `members` と、各提案 frontmatter の `families`(上記)を一致させる。提案ページがあるメンバーは必ずその `families` に当該 family を含め、family の `members` にも slug を載せる。未作成提案は family の `members` 側だけに slug で載る(`proposals/` に実体が無いのは未精読を意味し、誤りではない)。`index.md` には families セクションを設けて各 family へリンクする。

## フォーマット

markdown / json は **oxfmt** で整形する(設定 `.oxfmtrc.json`、`proseWrap: preserve` で日本語の行は折り返さない、`embeddedLanguageFormatting: off`)。除外は `raw/**`(submodule・不変)と `wiki/_generated/**`(生成物・JSONL を含む)。

- 手動: `npm run fmt`(= `oxfmt`)、検査は `npm run fmt:check`。
- **自動強制**: Claude Code の PostToolUse hook(`.claude/settings.json`)が編集した .md/.json を即整形し、git の pre-commit hook(`.githooks/pre-commit`、`core.hooksPath` 要設定)が staged ファイルを整形して再 stage する。
- clone 直後は `git config core.hooksPath .githooks` を一度実行する。

## ワークフロー

各操作は Claude Code のスラッシュコマンドとしても用意してある(`.claude/commands/`): **`/ingest <提案>`**、**`/query <質問>`**、**`/lint [対象]`**、**`/update [合意]`**、**`/summarise [会合]`**。コマンドは手順を持たず、本ファイルの該当ワークフローを読んで実行するだけのポインタ(定義は AGENTS.md が唯一の正本。コマンド側に再掲しない)。

**コミット規約**: 変更はプレフィックス付きの英語メッセージでコミットする。プレフィックスは変更の起因で決める:

- 操作(コマンド)に起因する変更 → その**操作名**: `[ingest]` / `[query]` / `[lint]` / `[update]` / `[summarise]`(例: `[lint] fix champion attribution in records-and-tuples`)。
- いずれの操作にも起因しない **wiki 全体に関わる変更** → `[wiki]`: コマンド自体の追加・変更、`tools/` などツールの変更、リポジトリ構成や本ファイルの構造的変更など。

コミットはリポジトリ/環境の git 規約(署名・rebase・必要な trailer 等)に従う。コミットすべき変更が無いとき(Query で file back しなかった等)はスキップしてよい。

### Ingest(素材の取り込み)

1. 対象会合 or 提案を決める。`wiki/_generated/agenda-index.md` を grep して関連議題と会合を特定する(例: `grep -i -A4 decorators wiki/_generated/agenda-index.md`)。
2. 該当する `raw/notes` のセクションを読む(`### Conclusion` と `### Speaker's Summary of Key Points` がステージ判定の要)。
3. 提案ページを新規作成 or 更新: ステージ遷移テーブルに行を追加、ステージ推移グラフ(mermaid)を更新、論点を追記/更新、frontmatter の `current_stage`/`status` を最新化。発言引用は日本語訳で。
   - **champion の確定は delegates.txt だけで決めない**。当該会合の Presenter 行・本文で裏取りする。略号は会合ごとに振り直されることがある(例: 2019-10 は Robin Ricard を RRI と表記するが、delegates.txt の RRI=Reefath Rajali は別人)。発言の帰属・年月も原文で確認する(誤帰属が起きやすい箇所)。
4. **人物の生成とリンク**(提案ページを書き終えたら必ず実行):
   - `python3 tools/extract_people.py` — 提案ページに登場する略号を検出し、`wiki/people/<ABBR>.md` を生成/再生成(フルネーム=delegates.txt、所属・参加会合=出席者テーブル、担当ドラフト=各提案 frontmatter の `champions` を相互参照)。
   - `python3 tools/link_people.py` — 提案ページ本文中の略号を `[ABBR](../people/ABBR.md)` にリンク(冪等)。frontmatter・コードブロック・mermaid・既存リンクは保護。
   - 語と衝突する略号(`API`, `JS` 等)は `extract_people.py` の `NON_PERSON` で除外している。新たな誤検出が出たら追記する。
5. `wiki/index.md` のカタログ行を更新。
6. `wiki/log.md` に 1 行追記。

### Query(質問への回答)

1. `wiki/index.md` → 関連提案ページ → 必要なら `agenda-index.md` → `raw/notes` の順で掘る。
2. 回答は出典(会合リンク)付き。
3. 回答が価値ある分析(横断比較・新しい発見・再利用したい整理など)を含む場合は、**最後にユーザへ「これを wiki ページとして残すか」を確認する**(勝手に追加しない)。残すなら synthesis ページとして file back し、`wiki/index.md`・`wiki/log.md` を更新する。

### Lint(健全性チェック)

wiki の品質点検。次の **2 側面の両方**を含む(以前「Verify」と区別していた出典突き合わせも Lint に統合する)。

**(a) 内部健全性**(wiki 内部を見る)

- ページ間の矛盾、古くなった記述(新しい会合で覆された主張)、孤立ページ、相互リンク漏れ、論点の決着漏れを点検。
- `agenda-index.md` に出てくるが提案ページが無い重要提案を洗い出す。
- **family の双方向整合**: 各 `families/<family>.md` の `members` と、提案 frontmatter の `families` が一致しているか(提案ページを持つメンバーに当該 family の記載漏れが無いか、逆に提案の `families` が family の `members` に載っているか)を点検。

**(b) 出典との整合性**(wiki ↔ raw を突き合わせる)

- 各提案ページの主張を引用元の逐語録に照らして検証する。**誤りを探す姿勢**で点検し、見つけたら raw を真として修正する。
- 特に誤りが出やすい箇所: ステージ遷移の年月・方向、champion の人物特定、発言の帰属、引用の正確性。
- **`raw/proposals` との突き合わせ(現ステージ・champion の確定)**: 各提案ページの frontmatter `current_stage` / `status` / `champions` を正典リストと照合する。
  - 探し方: Stage 3/2.7/2 は `raw/proposals/README.md`、Stage 4 は `finished-proposals.md`、Stage 1 は `stage-1-proposals.md`、withdrawn/inactive は `inactive-proposals.md` を grep(`grep -i '<提案名>' raw/proposals/*.md`)。どのテーブルに載っているかが現ステージを示す。
  - 食い違ったら precedence(上記レイヤ節)に従う: 現ステージ/champion は proposals を一次として wiki を直し、**遷移の経緯は notes で裏取り**する。proposals に未掲載の提案(古い withdrawn 等)は notes のみで判断してよい。
  - 注意: proposals リストは現在のスナップショットなので**過去の遷移そのものは検証できない**。経緯テーブルの中間ステージは引き続き notes で確認する。

素材更新時(submodule pull 後)は `python3 tools/extract_agenda.py`、続けて `python3 tools/extract_people.py && python3 tools/link_people.py` で再生成。

### Update(運用方針の反映)

会話の中で **wiki の運用(規約・ページ形式・ワークフロー・ツールの使い方)に関する合意が新しくできたら、それをこの AGENTS.md に反映**し、`wiki/log.md` に `update` として 1 行記録する。これにより次セッション以降は更新後の規約で運用される。

- 判断基準: 「**チームメイトや別エージェントにも必要な、wiki の動き方に関する取り決めか**」。該当すれば AGENTS.md を編集する。
- 該当しないもの(その場限りの指示、私個人の振る舞いの好みなど)は AGENTS.md に書かない。
- 矛盾する旧記述があれば置き換える(追記で二重化しない)。

### Summarise(会合の日次要約)

会合まるごとを話題単位で日本語要約する(提案中心の Ingest とは別物)。出力は `wiki/meetings/<YYYY-MM>/`。既定の対象は `raw/notes/meetings/` の**最新会合**。

1. 対象会合の各日ファイル `raw/notes/meetings/<YYYY-MM>/<month-DD>.md` を読む。
2. **日ごとに 1 ファイル** `wiki/meetings/<YYYY-MM>/<YYYY-MM-DD>.md` を生成。各日の議題(`## <topic>`)ごとに:
   - 見出しは原文のトピック名(英語のまま、`##`)。
   - 発表者のスライドリンク(`* [slides](URL)`)があれば、**最初の箇条書き**に `- Slides: [link](URL)` として置く。
   - そのトピックに**該当する既存の提案ページ**(`wiki/proposals/<slug>.md`)があれば、Slides の次に `- 提案ページ: [Title](../../proposals/<slug>.md)` を置く(該当が無ければ付けない)。
   - 続けて **3〜5 行**で日本語要約(地の文は日本語・用語/API/略号は英語、wiki 共通の言語規約に従う)。
   - `### Conclusion` / `### Speaker's Summary of Key Points` があれば、**その結論を必ず要約に含める**(stage 遷移・consensus の有無など)。
   - 委員会の定型(Opening & Welcome / Secretary's Report / 各種 Status Update など議論性の薄いもの)は省いてよい。
3. `wiki/meetings/<YYYY-MM>/index.md` を生成:
   - **必ず tc39/agenda リポジトリの該当ページへのリンク**を貼る(`https://github.com/tc39/agendas/blob/main/<YYYY>/<MM>.md`)。
   - そこから引いた**概要**、会合名(例: 113th TC39 Meeting)、開催地、ホスト、参加者などをまとめる(会合名・参加者は raw の各日先頭 attendees テーブル、開催地は Opening の記述からも補える)。
   - 各日ファイルへのリンク一覧を置く。
4. 完了後 `[summarise]` でコミットし、`wiki/log.md` に記録。

**note(submodule)と wiki の同期**: `raw/notes` を pull したり PR を checkout したら、**必ずその submodule ポインタの変更をコミットする**(`[wiki]`)。wiki が要約・参照した note の状態を常に記録し、両者を同期させるため(ポインタを未コミットのまま放置しない)。

- 未マージ PR にしかない会合を要約する場合: `cd raw/notes && git fetch origin pull/<PR>/head:pr-<PR> && git checkout pr-<PR>` で checkout → **ポインタをコミット**(`[wiki]`)→ 要約を生成し `[summarise]` でコミット。
- 以後の運用: 定期的に `git submodule update --remote`(または `raw/notes` で `git fetch`)で更新を確認し、**その PR が main にマージされていたら main 追跡へ戻す**(`cd raw/notes && git checkout main && git pull --ff-only`)→ ポインタを再びコミット(`[wiki]`)。
- 注意: PR head のコミットは fork 由来だと plain な `git submodule update` で取得できないことがある(別クローンでの完全な再現性はマージ後に確保される)。

## 人物ページ(people/)

`wiki/people/<ABBR>.md` は**生成物**。提案ページと family ページに登場する略号について作られ、「フルネーム / 所属 / 担当ドラフト(champion)/ 言及される提案 / 言及される family / 参加したミーティング」を集約する。filename を略号にしてあるので `[ABBR](../people/ABBR.md)` がそのまま解決する(提案・family いずれも `../people/` で同じ深さ)。提案・family ページが増えるたび `extract_people.py` を再実行すれば対象人物も自動で増える。

- 全 578+ の delegate を作るのではなく、**登場した人物だけ**を扱う方針。
- フルネーム/所属/参加会合は `raw/notes`(delegates.txt と各会合の出席者テーブル)由来。早期の会合は出席者テーブルが略号列を持たないため `参加したミーティング: 0` になる人物がいる(フルネームは delegates.txt から補完)。これは抽出の限界であり誤りではない。
- 手で編集しない(再生成で上書き)。記述を足したいときはスクリプト側を直す。

## バックボーンの使い方(重要)

全 86 会合・2737 議題は `wiki/_generated/agenda-index.md` に機械抽出済み。これは精読の代替ではなく**索引**。提案ページを書く/辿るときは、まずここを grep して「どの会合で議論されたか」を掴み、その会合の原文を読んで論点を埋める。提案名は年で揺れる(改名・別名)ので、grep は別名でも試す。

## TC39 のステージ(参考)

- **Stage 0** Strawperson / **Stage 1** Proposal(検討開始) / **Stage 2** Draft(API 概形合意) / **Stage 2.7** (2023 新設) テスト・spec レビュー完了待ち / **Stage 3** Candidate(実装待ち) / **Stage 4** Finished(本体へマージ、出荷)。
- Stage 2.7 は 2023-11 前後に導入。それ以前の提案は 2 → 3 を直接遷移している。

## スコープの注記

素材は 334 ファイル・2012〜2026。全件の精読は段階的に行う。現時点で精読済みの提案は `wiki/index.md` の「精読済み」セクションに、未精読(バックボーンのみ)は agenda-index 参照とする。
