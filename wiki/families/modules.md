---
title: Modules (module harmony)
slug: modules
kind: family
members: [es-modules, dynamic-import, import-meta, top-level-await, import-attributes, json-modules, export-from, source-phase-imports, import-defer, import-text, esm-phase-imports, export-defer, export-all-from, module-scope-ceiling, module-expressions, module-declarations, compartments]
tags: [family, modules]
---

## 概要

ES2015 で入った `import`/`export` の静的 module system(かつて "module harmony" と呼ばれた構想)と、その上に積み重なってきた一連の提案群です。土台の ES Modules に対し、(1) **実行時 import**(`import()`)、(2) **メタ情報**(`import.meta`)、(3) **非同期依存**(top-level await)、(4) **import の属性**(import attributes / JSON modules)、(5) **import の phase**(source phase / defer)、(6) **ホスト統合**(HTML/Node/Wasm)といった軸で拡張が続いています。

近年(2024〜2026)は、起動性能のための**評価遅延**(`import defer` / `export defer`)、**phase の概念**(`import source` で instance ではなく compile 済み source を取得)、**新しい import 種別**(`type: "text"`)、そして supply-chain security 文脈の **scope 隔離**(Module Scope Ceiling)が活発です。個別の経緯は各提案ページ(未作成のものはコード表記)を参照してください。

## メンバー

| 提案                                      | 現ステージ    | 一言                                                                                         |
| ----------------------------------------- | ------------- | -------------------------------------------------------------------------------------------- |
| `es-modules`                              | 4 (ES2015)    | `import`/`export` の静的 module system。すべての module 提案の土台                           |
| `dynamic-import`(`import()`)              | 4 (2019-06)   | 実行時に specifier を渡して module を非同期 import する関数形式                              |
| `import-meta`(`import.meta`)              | 4 (2020-03)   | 実行中 module のホスト固有メタ情報(`import.meta.url` 等)へのアクセス                         |
| `top-level-await`                         | 4 (2021-05)   | module トップレベルで `await` を許可し、module を非同期依存として待機可能に                  |
| `import-attributes`(旧 import assertions) | 4 (2024-10)   | `with { type: "json" }` 形式で import 時にホストへ属性を渡す。`assert`→`with` に改名         |
| `json-modules`                            | 4 (2024-10)   | `import data from "./x.json" with { type: "json" }` で JSON を module として import          |
| `export-from`(`export * as ns from`)      | 4 (ES2020)    | `export * as ns from "mod"` 等の re-export 構文                                              |
| `source-phase-imports`                    | 3 (2023-07)   | `import source x from` で instance でなく compile 済み source phase を取得(Wasm 等)          |
| `import-defer`                            | 3 (2025-02)   | `import defer * as ns from` で評価を遅延し、初回アクセス時に同期評価。起動性能向け           |
| `import-text`(`type: "text"`)             | 3 (2026-03)   | `with { type: "text" }` でファイルを文字列として import。仕様の大半は HTML/Fetch/CSP 側      |
| `esm-phase-imports`                       | 2.7 (2024-12) | source phase を ESM/Wasm へ拡張。compiled module を得て custom import で instantiate         |
| `export-defer`                            | 2(2.7 提案中) | `import defer` から分離。re-export 経路でも評価/読み込み遅延を伝播。barrel file 向け         |
| `export-all-from`                         | 1 (2026-05)   | `export * from` が `default` を再 export しない問題を解決(proxy/CDN module 用途)             |
| `module-scope-ceiling`                    | 1             | module の lexical lookup を global に到達させない scope 差し替え。supply-chain security 動機 |
| `module-expressions`                      | 2             | module をファイル外で式としてインライン定義(`module { ... }`)。worker への受け渡し等が動機   |
| `module-declarations`                     | 2             | module をファイル内で宣言的に定義(module expressions の姉妹提案)                             |
| `compartments`                            | 1(停滞)       | SES 由来の module loader / 分離実行環境。module harmony の loading 層。現在は他提案へ分流    |

> ステージは各提案を最後に審議した会合の結論に基づく(`agenda-index.md` の `stage:` は「その回で要求された stage」で現ステージとは限らない)。`export-defer` は 2025-11 に Stage 2.7 を提案したが [GB](../people/GB.md) が Stage 3 への留保を表明し、2026-05 時点でも Stage 2 の status update 扱い。`source-phase-imports` は Stage 3 のまま(直近会合は normative change の審議で advancement ではない)。リンクの無い提案は本 wiki で未精読。
>
> なお **Dynamic Import Host Adjustment** は module 系だが 2026-03 に取り下げ確認([2026-03-10](../meetings/2026-03/2026-03-10.md))。CSS/HTML Modules は TC39 ではなく HTML(WHATWG)側のため member に含めない。

## 横断テーマ

### import の phase(source / instance / defer)

import を「どの段階まで進めるか」を構文で選ぶ軸が近年の中心です。通常の instance phase に加え、`import source`(compile 済み source phase)・`import defer`(評価遅延)が同じ `import` 文法空間を共有します。`source-phase-imports` → `esm-phase-imports` はこの phase 概念を Wasm/ESM に広げるものです。

### 起動性能のための評価遅延(`import defer` / `export defer`)

大きな依存グラフの評価コストを下げる系統です。`import defer` が consumer 側で評価を遅延(Stage 3)、`export defer` が library 側で re-export 経路に遅延を伝播(Stage 2)。両者を namespace import と併用すると tree-shaking を失う課題があり、filtered namespaces 等が検討されています([2026-05-19](../meetings/2026-05/2026-05-19.md))。champion は主に [NRO](../people/NRO.md)。

### ホスト統合(HTML / Node / Wasm)

module 仕様の重心は ECMA-262 とホスト(HTML/Fetch/CSP、Node の `vm` module、Wasm)に分かれます。`import-text` は「仕様の大半が HTML 側」、`esm-phase-imports` は Node 統合の明確化が論点でした([2026-03-11](../meetings/2026-03/2026-03-11.md))。

### `assert` → `with`(import attributes 改名の経緯)

import の属性構文は `with`→`if`→`assert`→`with` と二転三転しました。`assert` は「cache key に影響しない」という mental model がホスト解釈と噛み合わず Stage 3 から Stage 2 へ downgrade され、最終的に `with` に統一して `assert` を drop しました(2023-01 downgrade、2024-07 drop)。champion は [NRO](../people/NRO.md)。

## 関連 family

- [Iterator helpers and friends](../families/iterator.md) — 別カテゴリの提案群。families の先行例。
- (未作成)`concurrency` — top-level await や AsyncContext と隣接。

## 出典

- [2019-06 june-4](../../raw/notes/meetings/2019-06/june-4.md) — dynamic `import()` Stage 4
- [2020-03 april-1](../../raw/notes/meetings/2020-03/april-1.md) — `import.meta` Stage 4 / Compartments Stage 1
- [2021-05 may-25](../../raw/notes/meetings/2021-05/may-25.md) — top-level await Stage 4
- [2023-01 jan-31](../../raw/notes/meetings/2023-01/jan-31.md) — import assertions Stage 3 → 2 downgrade
- [2023-07 july-12](../../raw/notes/meetings/2023-07/july-12.md) — Source Phase Imports Stage 3
- [2024-07 july-29](../../raw/notes/meetings/2024-07/july-29.md) — `assert` を drop し `with` へ統一
- [2024-10 october-08](../../raw/notes/meetings/2024-10/october-08.md) — Import Attributes + JSON Modules Stage 4
- [2025-02 february-18](../../raw/notes/meetings/2025-02/february-18.md) — `import defer` Stage 3
- [2025-11 november-18](../../raw/notes/meetings/2025-11/november-18.md) — `export defer` Stage 2.7 提案(留保あり)
- [2026-03 march-11](../../raw/notes/meetings/2026-03/march-11.md) — Import Text Stage 3 / ESM Phase Imports update
- [2026-05 may-20](../../raw/notes/meetings/2026-05/may-20.md) — export all from Stage 1 / Module Scope Ceiling / phase imports の normative PR
- [agenda-index](../_generated/agenda-index.md) — 各提案の議題・stage シグナル(索引)
