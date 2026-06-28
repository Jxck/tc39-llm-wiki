# Log

wiki の ingest / query / lint の時系列記録(append-only)。各行は `## [YYYY-MM-DD] <種別> | <内容>` で始める。`grep "^## \[" wiki/log.md | tail -5` で直近を確認できる。

## [2026-06-25] setup | wiki 初期構築

- 運用規約 [AGENTS.md](../AGENTS.md) を策定(レイヤ・提案ページ形式・言語規約・ワークフロー)。
- `tools/extract_agenda.py` を作成し、全 86 会合 / 2737 議題のバックボーン [\_generated/agenda-index.md](_generated/agenda-index.md) を生成。
- 代表 3 提案を精読してページ化:
  - [Temporal](proposals/temporal.md) — shipped(Stage 4 / 2026-03)。「長期で出荷に至った大型提案」の実例。
  - [Decorators](proposals/decorators.md) — stage3(Stage 3 / 2022-03)。「3 度再設計した難航提案」の実例。
  - [Records & Tuples](proposals/records-and-tuples.md) — withdrawn(2025-04)。「停滞の末に撤回された提案」の実例。
- [README.md](README.md) を作成。

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

## [2026-06-25] wiki | markdown フォーマッタ oxfmt を導入

- `oxfmt`(Rust 製・markdown 対応)を devDependency 導入。設定 `.oxfmtrc.json`(`proseWrap: preserve`、`embeddedLanguageFormatting: off`、除外 `raw/**`・`wiki/_generated/**`)。
- 既存の wiki 全 markdown を整形(表の桁揃え・見出し後の空行など。mermaid・日本語長文・リンクは保持)。
- **自動強制**: PostToolUse hook(`.claude/settings.json`)で編集ファイルを即整形、pre-commit hook(`.githooks/pre-commit` + `core.hooksPath`)で staged を整形・再 stage。AGENTS.md に「フォーマット」節を追加。

## [2026-06-25] summarise | 114th TC39 Meeting (2026-05)

- tc39/notes の未マージ PR #411(2026 May transcript)を submodule で checkout し、114th(Amsterdam, JetBrains)を日次要約。`wiki/meetings/2026-05/` に Day 1-3 + index.md を生成。Day 1 の Temporal/Decorators トピックは提案ページへリンク。submodule のポインタ変更はコミットしない(未マージ PR のため)。

## [2026-06-25] update | 未マージ PR からの要約と submodule 運用を明文化

- Summarise に submodule 運用を追加: 未マージ PR にしかない会合は `raw/notes` で PR を checkout して要約し、ポインタはコミットしない。定期的に submodule を update し、**PR が main にマージされたら submodule を main 追跡へ戻して**ポインタを通常更新(`[wiki]`)する。

## [2026-06-25] update | submodule ポインタは必ずコミット(note↔wiki 同期)

- 方針変更: 「未マージ PR のポインタはコミットしない」を撤回。**submodule を pull / PR checkout したら必ずポインタをコミットする**(`[wiki]`)ことに統一。wiki が参照した note の状態を常に記録し同期させるため。AGENTS.md の該当節を置き換え。

## [2026-06-25] lint | wiki 全体の健全性チェック(Decorators 降格の反映ほか)

内部健全性と出典(2026-05 は PR #411)を突合。発見と修正:

- **Decorators が陳腐化**: 2026-05(114th)で Stage 3 → **Stage 2.7 へ降格**(Decorator Metadata も lockstep)していたが提案ページが 2023-05 で止まっていた([raw may-19.md:1194](../raw/notes/meetings/2026-05/may-19.md) で確認)。frontmatter(`status: stage2.7` / `current_stage: 2.7`)・ステージ遷移テーブル(2026-05 行追加)・mermaid グラフ(2026 を 2.7 に)・概要・`### Stage 2.7 への降格` 論点・出典・index.md 行を更新。
- **AGENTS.md**: `status` enum に `stage2.7` を新設(降格を表現できなかったため。本 lint で合意し反映)。index.md の凡例も更新。
- **2026-05 index 概要の事実誤り 2 点**: (1) Dynamic Code Brand Checks を「Stage 4 到達」に誤記(実際は normative change の consensus のみ・次回再要求)→ 除外。(2) Decorators の 2.7 移行を「advancement/進む」と誤記 → 降格(regress)へ訂正。
- **人物数**: index.md 「43 名」は lint 開始時点では 42 ページとの不整合だったが、Decorators ページに [DLM](people/DLM.md) が登場し再生成で 43 ページとなったため 43 のまま整合(extract_people/link_people 実行済み)。
- 内部リンク・人物略号(43)・会合↔提案リンクは全て解決。Temporal の Stage 4(2026-03)は出典と整合。

## [2026-06-26] query | Unicode のなかでの Intl.MessageFormat の立ち位置

- 「MF2 本体(構文 DSL・データモデル)は Unicode、参照実装は ICU(ICU4C/4J, 2024-04 時点 tech preview)、JS API のみ TC39」という 3 層の垂直スタックと、TG2 が MF2 の評価を Unicode/業界に外注した位置づけ、を回答(出典: [2024-04 april-10](../raw/notes/meetings/2024-04/april-10.md))。先行質問「Intl.MessageFormat は Template Instantiation と被るか」には、Template Instantiation は W3C/WHATWG の HTML 提案で TC39 スコープ外・目的も別、と前提を訂正して回答。
- file back: [intl-messageformat.md](proposals/intl-messageformat.md) の `## 主な論点` に `### Unicode との分業構造 — 構文は Unicode、API は TC39` を追加。続けて `## 関連提案` に `### 混同しやすい別物 — Template Instantiation / DOM Parts(参考・TC39 スコープ外)` を追加(W3C/WHATWG WICG の DOM 側提案。DOM Parts=低レイヤのマーク/更新機構、Template Instantiation=その上の宣言的テンプレート API、という階層関係。外部資料に基づく参考注記で、出典は wiki 素材外として明示)。

## [2026-06-25] query | Decorator は結局誰が欲しいのか

- 「使う側(フレームワーク作者・TypeScript/Babel エコシステム・アプリ開発者)は強く欲しがるが、作る側(V8/SpiderMonkey/JSC のエンジン実装者)が誰も出荷したがらない」という需要/実装のミスマッチが停滞と 2026-05 降格の核心、と回答(出典: [2019-03](../raw/notes/meetings/2019-03/mar-27.md)・[2021-07](../raw/notes/meetings/2021-07/july-14.md)・[2023-01](../raw/notes/meetings/2023-01/feb-01.md)・[2026-05 may-19](../raw/notes/meetings/2026-05/may-19.md))。
- file back: [decorators.md](proposals/decorators.md) の `## 主な論点` に `### 需要と実装のミスマッチ(誰が欲しいのか)` を追加。
- 副次: 本文に [OFR](people/OFR.md) が新規登場し人物ページ生成(44 名)。"TS"(TypeScript の略)が delegate 略号 TS と誤一致してリンク化されたため、`extract_people.py` の `NON_PERSON` に `TS` を追記し、誤生成ページを除去・本文を `TypeScript` 表記へ修正。

## [2026-06-25] ingest | 2026 年に Stage 4 到達した提案を ingest

- 対象を「2026 年(113th 2026-03 / 114th 2026-05、および 111th 2026-01)に Stage 4 へ到達した提案」に確定。該当は 6 件(Temporal は既存ページで最新のため除外し、新規 5 件を ingest)。各提案は複数年の履歴を持つため、subagent で agenda-index + raw 横断の履歴調査を 5 件並列実行し、本体で検証・ページ化。
  - [Upsert](proposals/upsert.md)(`Map.prototype.getOrInsert`、ECMA-262、Stage 4 2026-01)
  - [Intl Era/Month Code](proposals/intl-era-month-code.md)(ECMA-402、Stage 4 2026-03、Temporal と同時)
  - [Joint Iteration](proposals/joint-iteration.md)(`Iterator.zip`、ECMA-262、Stage 4 2026-05)
  - [Atomics.pause](proposals/atomics-pause.md)(ECMA-262、Stage 4 2026-05、引数削除の normative change 込み)
  - [Explicit Resource Management](proposals/explicit-resource-management.md)(`using`、ECMA-262、Stage 4 2026-05。2025-05 conditional Stage 4)
- 各ページに frontmatter・ステージ遷移テーブル・mermaid グラフ・主な論点・出典を整備。発言引用は日本語訳。
- `extract_people.py` / `link_people.py` を実行し人物ページを 44 → 52 名に拡充(新規: BAN/BFS/EAO/EPR/FYT/KM/LCA/RPR)。誤検出なし。
- [README.md](README.md) のカタログに 5 行追加、`intl-era-month-code` を未作成リストから除去、人物数を 52 に更新。[Temporal](proposals/temporal.md) の関連提案を Intl Era/Month Code ページへリンク化。

## [2026-06-25] update | families レイヤを新設(カテゴリ横断のまとめ)

- 同じカテゴリにくくれる提案群を束ねる **family ページ**(`wiki/families/<family>.md`)を導入。個別の経緯は `proposals/` に置き、family は横断的なまとめ(メンバー一覧 + 横断テーマ)に徹する(二重メンテ回避)。AGENTS.md にディレクトリ構成・family ページ形式・lint 観点(family の双方向整合)を追記。
- **メンバーシップは双方向**: 提案 frontmatter に `families: [...]`、family ページに `members: [...]` を持ち、lint で不一致を検出する。未作成提案は family の `members` 側にだけ slug で載る。
- `extract_people.py` / `link_people.py` を `wiki/families/` も走査するよう拡張(family ページの人物リンクが解決・生成されるように)。人物ページに「言及される family」行を追加。これにより [GCL](people/GCL.md) が新規生成され 53 名に。
- 最初の family として [Iterator helpers and friends](families/iterator.md) を作成([MF](people/MF.md) の 2026-05 ロードマップを骨子に、helpers/concat/zip/chunking/includes/async 系など 11 提案を stage 付きで一覧化)。[joint-iteration](proposals/joint-iteration.md) に `families: [iterator]` を付与。index.md に families セクションを追加。

## [2026-06-25] ingest | modules (module harmony) family を作成

- 「module harmony」系(ES Modules と派生提案群)を [Modules](families/modules.md) family にまとめた。subagent で agenda-index + raw を横断調査し、ES Modules / dynamic import / import.meta / top-level await / import attributes / JSON modules / export-from(Stage 4)、source phase imports / import defer / import text(Stage 3)、ESM phase imports(2.7)、export defer(2、2.7 提案中)、export all from / module scope ceiling / module declarations / compartments(Stage 1〜停滞)の計 16 提案を現ステージ付きで一覧化。横断テーマ(import の phase、評価遅延、ホスト統合、`assert`→`with` 改名)を整理。
- 各提案ページは未作成のため members はコード表記。新規人物 [GB](people/GB.md)(Guy Bedford)を生成(54 名)。`vm`(Node module)を delegate 略号 `VM` と誤検出してリンク化したため `extract_people.py` の `NON_PERSON` に `VM` を追記し、誤生成ページを除去・本文をコード表記へ修正(`TS` と同種の対処)。
- index.md の families セクションに modules を追加。

## [2026-06-25] update | raw に tc39/proposals を追加し precedence を定義

- `raw/proposals`(tc39/proposals)を submodule 追加。現ステージ別テーブル + champions の正典リストを raw に取り込んだ。
- AGENTS.md のレイヤ節を 2 ソース構成に改訂し、precedence を明文化: 経緯・論点・発言は `raw/notes` が一次、現ステージ(`current_stage`/`status`)と champion の確定値は `raw/proposals` が一次。proposals はスナップショットで経緯を持たない点も注記。
- ディレクトリ構成に `raw/proposals/` の主要ファイルを追記。
- Lint(b) に proposals 突き合わせ手順を追加: frontmatter の `current_stage`/`status`/`champions` を README/finished/stage-1/inactive と grep 照合し、食い違いは precedence に従って解決(現ステージは proposals 一次、経緯は notes で裏取り)。

## [2026-06-25] ingest | Intl.MessageFormat (Stage 1, stuck)

- 新規提案ページ `wiki/proposals/intl-messageformat.md` を作成。MessageFormat 2.0 (MF2) を JS に公開する ECMA-402 提案。
- ステージ: 2022-03 に Stage 1 到達後、2026 まで Stage 1 で停滞。2024-02 に「parser を外しデータモデルのみで Stage 2」案、2024-04 に TG2(Google i18n)反対で頓挫し stuck に。論点は「実績の乏しい DSL/parser を言語に入れる是非」「error handling(throw しないモデル / option 1〜6)」「`message` 語の混乱」「`Intl.MessageResource` への分離(2022-11)」。
- champion は canonical の `raw/proposals/ecma402/README.md`(Stage 1 節)に従い EAO のみとした(DLM の co-champion 関与は経緯として本文に保持)。
- `extract_people.py` / `link_people.py` 実行、`index.md` に行追加。

## [2026-06-26] wiki | /update を「raw ソースの同期」コマンドへ再定義

- `/update` の役割を変更: 旧「会話で決まった運用合意を AGENTS.md に反映」を廃止し、**`raw/` 配下の submodule(notes / proposals)を最新に pull し、前回同期(コミット済みポインタ)からの差分を表示する**同期コマンドに置き換えた。
- AGENTS.md「### Update」を全面書き換え(手順: OLD ポインタ控え → pull → `OLD..HEAD` 差分提示 → `[update]` でポインタ commit + 生成物再生成 → log 記録)。Summarise 節の「以後の運用」を /update へ委譲し、ルーチン同期のポインタ commit を `[update]`(臨時 checkout は従来どおり `[wiki]`)と整理。
- `.claude/commands/update.md` と workflow 一覧の引数ヒントを更新。

## [2026-06-26] lint | raw/proposals 突き合わせ(stage/champion)と相互リンク補完

新 precedence(`raw/proposals` が現ステージ/champion の一次)に従い wiki 全体を点検。

- **提案 9 ページの現ステージ/status は全て canonical 一致**(Decorators=Stage 2.7 も canonical の 2.7 節で確認、Records & Tuples=inactive、Stage 4 群=finished、Intl.MessageFormat=Stage 1)。別セッション ingest の [intl-messageformat](proposals/intl-messageformat.md) も champion `EAO`・Stage 1 ともに canonical 一致で健全。
- **family の stage 誤りを修正**(canonical 照合): iterator の `iterator-join` を `1〜2`→**3**、modules の `module-declarations` を `1(停滞)`→**2** に訂正し、別 Stage 2 提案 `module-expressions` を分離・members 追加。
- **相互リンク漏れを補完**(前回 lint からの持ち越し): 2026-03/2026-05 要約の該当トピックに `- 提案ページ:` を 5 件追加(ERM×2・Intl Era/Month・Joint Iteration・Atomics.pause)。
- **champion 整合**(方針: 歴史的 champion 込みを維持し canonical の不足のみ補う): [Temporal](proposals/temporal.md) に canonical の champion 4 名 [PDL](people/PDL.md)(Philipp Dunkel)・[MAJ](people/MAJ.md)(Matt Johnson-Pint)・[BT](people/BT.md)(Brian Terlson)・[JWS](people/JWS.md)(Jason Williams)を追加(計 9 名)。Decorators/Upsert/Intl Era・Month は canonical champion が既に揃っており追加なし(YK/EPR 等の歴史的 champion は据え置き)。
- 副次: 人物ページ再生成で PDL/MAJ を新規生成(57→59 名)。index.md の人物数は 54 と stale だった(intl-messageformat ingest 時の更新漏れ、実際は 57)→ 59 に是正。
- fmt・デッドリンク・family 双方向整合は全てクリーン。

## [2026-06-26] wiki | 全提案ステージ一覧 proposals/index.md を生成化

- `tools/extract_proposals.py` を新設。`raw/proposals/`(canonical: README=Stage 3/2.7/2、finished=4、stage-1、stage-0、inactive と ecma402/ 同構成)から全提案を抽出し、ECMA-262 / ECMA-402 ごとに stage 別の完全一覧 [proposals/index.md](proposals/index.md) を生成(ECMA-262 286 件 / ECMA-402 34 件)。精読済み 9 ページはタイトル一致で各ページへリンク(別名は generator の ALIASES で吸収)。
- **生成物として常時最新化**: Update(`raw/proposals` pull)の step 4 再生成チェーンに `extract_proposals.py` を追加し、`raw/proposals` が動いたら必ず再生成する旨を AGENTS.md に明記。Generated レイヤ定義・ディレクトリ構成・Lint の再生成手順・wiki/index.md の導線も更新。
- churn 回避のため `wiki/proposals/index.md` を `.oxfmtrc.json` の ignore に追加(出力は generator が authoritative)。

## [2026-06-26] wiki | Update 再定義の整合(規約反映は [wiki] に集約)

- 別プロセスが `### Update` を「運用方針の反映」→「raw ソースの同期」に再定義済み(コミット ba4c278 に巻き込まれて記録)。新定義は AGENTS.md・`/update` コマンド・ワークフロー一覧で整合済みと確認。
- 抜けていた「規約合意の AGENTS.md 反映」の住所を明文化: コミット規約の `[wiki]` 行に「AGENTS.md への規約反映も `[wiki]`、専用操作・コマンドは設けず明示依頼時に行う、`/update` は raw 同期専用」を追記。

## [2026-06-26] wiki | proposals/index.md の Stage 4 を未収載分のみに絞り込み

- Stage 4 セクションを「まだ ECMAScript に入っていない=Expected Publication Year が当年以降」のものだけに限定(出荷済みの finished は省略)。`extract_proposals.py` が finished テーブルの出版予定年を読み、`>= 今年` で filter。Stage 3 以下は従来どおり全件。
- 結果: Stage 4 は ECMA-262 11 件 / ECMA-402 2 件(全 finished 77 / 18 件中)。当年判定は datetime ベースで自動繰り上がり。
- 注: 「今年 Stage 4 到達」の厳密判定は canonical に stage-4 日付列が無いため、出版予定年(ES エディション)を proxy にしている。pub 2026 には 2025 末に finished し ES2026 に入る分も含まれる。

## [2026-06-26] wiki | AGENTS.md にセッションの取り決めを反映

- `proposals/index.md` の記述を実態に整合: 「完全ステージ一覧」→「Stage 4 は未収載分のみ」。新セクション「全提案ステージ一覧(proposals/index.md)」を追加し、Stage 4 フィルタ(Expected Publication Year ≥ 当年)と ES エディション規則(3 月末 freeze + 6 月 GA、pub year=どの ES 版か=収載判定の確定信号)を明文化。
- Lint の champion 整合方針を追記: canonical の現 champion は満たす(不足は補う)が、canonical に無い歴史的 champion は削除せず残す(canonical に無い=誤りとしない)。

## [2026-06-26] ingest | Amount(旧 Measure)を精読

- `Amount`(`proposal-amount`、旧 `proposal-measure`)の提案ページ [amount.md](proposals/amount.md) を作成。数値+単位の immutable value type(`value`/`unit`/`convertTo()`/`toLocaleString()`)。ECMA-262、champion [BAN](people/BAN.md)、現 Stage 2(canonical で確認、reviewer WH/JHD)。
- ステージ遷移を notes で裏取り: 2024-10 に "Measure" として **Stage 1**(agenda-index は "stage 0" 表記だが Conclusion は Stage 1 承認 → notes を正とした)、2025-07 に Amount へ改名、Stage 2 は 2025-07/09 に未達で 2026-05 に到達。論点: Decimal との unified vision(merge せず)、i18n 用途 vs 汎用、conversion math の精度(WH 指摘)、no-unit/serialization。
- index.md の精読済みカタログに Amount を追加。extract_people/link_people/extract_proposals 再生成(人物 60 名、generated index が amount.md をリンク)。

## [2026-06-26] wiki | ステージグラフを折れ線(xychart-beta)へ戻す

- gantt 移行(1ff1489)を revert し、全 10 提案ページのステージ推移グラフを `xychart-beta` 折れ線へ復帰。AGENTS.md のグラフ規約も折れ線に戻した。
- 補足: 「目盛りを 1 刻みにしたい」は **xychart-beta では不可**(mermaid 公式ドキュメントで確認。y 軸は数値専用で tick interval/count/custom 値の指定オプションが無く、0–4 範囲では自動で 0.5 刻み。設定可能なのは show/hide のみ)。半端値は 2.7 のみで、2 と 3 の間に正しくプロットされる。0.5 グリッドが気になる場合の選択肢は「y 軸ラベル非表示」のみ。

## [2026-06-26] lint | wiki 全体(Amount 追加・gantt 往復後の点検)

- **内部健全性**: fmt クリーン、全 10 提案ページが xychart-beta 折れ線(gantt 残存なし)、人物数 60 が index 記載と一致、proposals/index.md は再生成で差分なし(最新)、デッドリンクなし、family 双方向メンバーシップ整合。
- **出典整合**: 全 11 提案ページの `current_stage`/`status` を raw/proposals(canonical)と照合し全て一致(Amount=Stage 2、Decorators=Stage 2.7、R&T=withdrawn ほか)。
- **修正(相互リンク漏れ)**: amount.md 作成後にできた会合トピックへのリンク漏れを補完。2026-03-10・2026-05-20 の「Amount for Stage 2」に `- 提案ページ: [Amount](../../proposals/amount.md)` を追加。

## [2026-06-27] ingest | 2026-05 会合のステージ変更討議トピックを提案ごとに取り込み

- 対象: 114th meeting (2026-05) で「ステージ変更を議論した」トピック(移動の有無不問)。status update のみ・normative PR・needs-consensus PR は除外。
- 新規提案ページ 13 件: iterator-chunking(S3)・iterator-includes(S3)・iterator-join(S3)・regexp-buffer-boundaries(S3)・dynamic-code-brand-checks(S3 据置/normative)・error-stack-accessor(S3)・intl-keep-trailing-zeros(S3)・stable-formatting(S2)・intl-sequence-units(S2)・intl-default-behaviours(S1)・export-all-from(S1)・comparisons(S1)・is-template-object(inactive 化)。
- 既存ページは 2026-05 行が反映済みのため更新不要を確認: joint-iteration(S4)・atomics-pause(S4)・decorators(+ metadata, 3→2.7)・amount(S2)・explicit-resource-management(S4 finished)。
- frontmatter は raw/proposals(canonical)で現ステージ・champion を裏取り。過去経緯は agenda-index と各 notes で確認(ユーザ指定によりスコープは 2026-05 中心、深掘りは後続)。
- family 整合: iterator.md の chunking/includes/join 行をページへリンク、modules.md の export-all-from 行をリンク(members は既存で一致)。
- tools 再生成: extract_people.py(64 人)・link_people.py 実行。index.md カタログに 13 行追加。

## [2026-06-27] ingest | 深堀り修正: 3 提案の Stage 遷移を notes で裏取りし訂正

- 前回 ingest で「裏取りが浅い」と明示した 2 留意点を raw/notes の `### Conclusion` で確定。
- **dynamic-code-brand-checks**: Stage 2 には未到達(2019-07「no for stage 2」/ 2019-12「NOT approved」/ 2021-01「Not advancing」)。2024-04 に NRO が「Stage 1 版を Stage 3 へ」と要求し **1 → 3 へ直接前進**。誤りだった「2021-01 Stage 2 到達」を訂正、mermaid を 2019-2023 を 1 に修正、論点・出典を追補。
- **is-template-object (Array.isTemplateObject)**: 2019-06 june-5 の結論が "Stage 2 acceptance" で **Stage 1 を経ず直接 Stage 2**。誤りだった「Stage 1 → 2020 年前後に Stage 2(推定)」を訂正、mermaid を 2019 から 2 に修正、出典を追補。
- **intl-keep-trailing-zeros**: 2025-07 で同会期中に **Stage 2(day 1 july-29)→ Stage 2.7(day 3 july-30)** を連続通過(WH の ToIntlMathematicalValue 懸念はスコープ外として分離)。誤りだった「2 → 3 直接」を訂正、Stage 2.7 行を追加、mermaid 2025 年末値を 2.7 に修正、論点追補。
- tools 再生成(extract_people / link_people)。mermaid は全 3 ページ 15 点を維持。index カタログのステージ値は不変(訂正は中間遷移のため)。

## [2026-06-28] lint | wiki 全体

- **内部健全性**: oxfmt クリーン、mermaid 全提案 15 点(records-and-tuples の 14 は撤回年止めで正常)、proposals/index.md 再生成で差分なし、デッドリンク無し(検出は説明用プレースホルダのみ)、family 双方向整合 OK。
- **出典整合**: ECMA-262 新規(iterator-chunking/includes/join・regexp-buffer-boundaries・dynamic-code-brand-checks・error-stack-accessor)は canonical の Stage 3 と一致。champions も canonical 一致(EAO/SFC ほか)。
- **修正(1) バグ**: regexp-buffer-boundaries.md の `\Z` 正規表現に実 U+2028/U+2029(行区切り)が混入しテーブルを破壊していた → ASCII テキスト `\u2028` / `\u2029` に置換。
- **修正(2) family 整合**: regexp-buffer-boundaries の `families: [regexp]` は families/regexp.md 不在のため frontmatter から除去。
- **修正(3) 人物数**: index.md「60 名」→「65 名」(JRL/JSH/KOT/MSL/ZTZ 追加分の反映漏れ)。
- **未解決(保留)**: Stable Formatting / Intl Sequence Units の現ステージで notes と canonical が食い違い。2026-05 notes は両者を「Stage 2 で consensus」と明記するが、canonical ecma402/README は両者を `### Stage 1` セクションに据え置き(2026-05 note 付き、`### Stage 2` は空)。section 移動の lag と推定。wiki は Stage 2 を維持し、次回 /update で raw/proposals を pull して section が Stage 2 へ移動したか確認のうえ確定する。

## [2026-06-29] lint | wiki 全体 + raw/proposals 突き合わせ

- **内部健全性**: リンク切れの実体破損なし(検出7件は `ABBR`/`slug`/`<slug>` プレースホルダか agenda-index 生成物・log 履歴記述)。直近の index.md→README.md リネームは健全。family の双方向整合(members ↔ 提案 frontmatter families)も問題なし。
- **出典整合(raw/proposals)**: 全23提案の stage/champion を canonical と照合。
  - **修正1件**: `is-template-object` の status を `inactive` → `withdrawn`。may-19 で champion JHD・CDA が "withdrawn" と明示、canonical inactive-proposals も "Withdrawn" 区分、同種の `records-and-tuples` も withdrawn。frontmatter / ステージ遷移セル(2 → withdrawn)/ 概要 / 論点見出し / README カタログ行を統一。
  - **canonical 追従遅れ(wiki が正・修正なし)**: `intl-sequence-units`・`stable-formatting` は wiki=stage2。`ecma402/README` は Stage 1 のままだが、2026-05 議事録(may-20 line 290 / 475-476)で Stage 2 consensus を確認。canonical README が 2026-05 の ECMA-402 結果を未反映なだけ。次回 lint で誤って降格しないこと。
  - champion 確認: `comparisons` の `JSH`=Jacob Smith(canonical 一致)、`temporal`/`decorators`/`intl-era-month-code` の歴史的 champion は方針どおり保持。

## [2026-06-30] summarise | 109th TC39 Meeting (2025-07)

- 2025-07(109th, リモート)を日次要約。`wiki/meetings/2025-07/` に Day 1-4(2025-07-28〜31)+ index.md を生成。Stage advancement: `Math.sumPrecise`・Uint8Array base64+hex が Stage 4、Iterator Sequencing・Upsert が Stage 3、Intl Era and Month Code・Intl Keep Trailing Zeros が Stage 2.7、Import Buffer が Stage 1→2、Module Import Hook/new Global・`Array.getNonIndexStringProperties`・`Object.getOwnPropertySymbols` options が Stage 1。Amount(旧 Measure)・`Object.propertyCount`・`Array.isSparse` は objection により不成立。既存提案ページ(temporal, upsert, iterator-chunking, intl-keep-trailing-zeros, amount, intl-era-month-code)へリンク。

## [2026-06-30] summarise | 110th TC39 Meeting (2025-09)

- 2025-09(110th, リモート)を日次要約。`wiki/meetings/2025-09/` に Day 1-3(2025-09-22〜24)+ index.md を生成。Stage advancement: Iterator Chunking・Import Bytes が Stage 2.7、Non-extensible Applies to Private が Stage 3、`Array.prototype.pushAll`・Native Promise Adoption・Native Promise Predicate(直後に Stage 2 へも)が新規 Stage 1。Amount は Stage 2 を目指したが significant digits・命名・数値変換メソッド等の懸念が late-breaking で噴出し3日間継続審議の末 Stage 2 未達(次回 Tokyo plenary へ持ち越し)。既存提案ページ(amount, iterator-chunking, intl-era-month-code, temporal)へリンク。
- **要注意**: `wiki/proposals/amount.md` の frontmatter は `status: stage2` / `current_stage: 2` だが、本会合の議事録では Amount は Stage 2 に到達していない(continuation のまま)。次回 lint で raw/proposals と突き合わせて要確認。

## [2026-06-30] summarise | 111th TC39 Meeting (2025-11)

- 2025-11(111th, Tokyo・Bloomberg ホスト)を日次要約。`wiki/meetings/2025-11/` に Day 1-3(2025-11-18〜20)+ index.md を生成。Stage advancement: Intl Locale Info API・Iterator Sequencing が Stage 4、Joint Iteration が Stage 3、await dictionary が Stage 2 を経ず直接 Stage 2.7、Import Text が Stage 1/2(条件付き2.7)、Intl Unit Protocol・Intl Energy Units・`Object.getNonIndexStringProperties` が新規 Stage 1、TypedArray Concatenation/Find Within が条件付き Stage 1(専用リポジトリ作成待ち)、`Object.keysLength` が Stage 2(`Object.propertyCount` は分離して Stage 1 のまま)。export defer は Stage 2.7 不成立、Declarations in Conditionals は Day Three まで継続も未決着、Class spread syntax・Class field introspection は Stage 0 のまま。Decorators は Test262 不足と実装間不一致で Stage 2.7 維持、Intl Era Monthcode は Stage 3 判断を2026年1月へ持ち越し。既存提案ページ(temporal, intl-keep-trailing-zeros, joint-iteration, error-stack-accessor, comparisons, intl-era-month-code, amount, decorators, iterator-join)へリンク。
