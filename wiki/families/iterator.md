---
title: Iterator helpers and friends
slug: iterator
kind: family
members: [iterator-helpers, iterator-sequencing, joint-iteration, iterator-chunking, iterator-includes, iterator-join, async-iterator-helpers, iterator-range, concurrency-control, unordered-async-iterator-helpers, iterator-unique]
tags: [family, iterator]
---

## 概要

`Iterator.prototype` / `Iterator` 名前空間まわりに、lazy な反復処理の標準ライブラリを揃えようとする一連の提案群です。出発点は **Iterator Helpers**(`map`/`filter`/`take`/`drop`/`flatMap`/`reduce`/`toArray` ほか、array prototype 相当の遅延版)で Stage 4 到達済み。以後、連結([Iterator Sequencing](../proposals/joint-iteration.md) ではなく `iterator-sequencing` = `Iterator.concat`)・併走([Joint Iteration](../proposals/joint-iteration.md) = `Iterator.zip`)・分割(chunking)・探索(includes)など、`Array.prototype` に既にある操作を iterator へ移植する形で広がっています。

近年の議題数が多く、2026-05 に [MF](../people/MF.md) が「iterator space のロードマップ」を提示しました([2026-05-19](../meetings/2026-05/2026-05-19.md))。本 family はそのロードマップを軸に、提案単位の現況を一望できるようにまとめたものです。個別の経緯・論点は各 `proposals/` ページ(作成済みのもの)を参照してください。

## メンバー

| 提案                                                                          | 現ステージ | 一言                                                                      |
| ----------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------- |
| `iterator-helpers`                                                            | 4          | MVP。`map`/`filter`/`take`/`drop`/`flatMap`/`reduce`/`toArray` ほか遅延版 |
| `iterator-sequencing`(`Iterator.concat`)                                      | 4          | 0 個以上の iterator を連結し、その yield をすべて流す                     |
| [Joint Iteration](../proposals/joint-iteration.md)(`Iterator.zip`/`zipKeyed`) | 4          | 複数 iterator を位置対応でまとめる(2026-05 到達)                          |
| `iterator-chunking`(`chunks`/`windows`)                                       | 3          | 複数値をまとめて消費(重なり無し=chunks / 重なり有り=windows)              |
| `iterator-includes`                                                           | 3          | `Array.prototype.includes` 相当                                           |
| `iterator-join`                                                               | 1〜2       | `Array.prototype.join` 相当([KG](../people/KG.md) champion)               |
| `async-iterator-helpers`                                                      | 2          | iterator helpers の async 版。全 method の並行 pull 対応 spec を作業中    |
| `iterator-range`(`Iterator.range`)                                            | 2          | 数値レンジ生成。長期停滞                                                  |
| `concurrency-control`                                                         | 1          | async iterator の並行数制御。async helpers の進行待ち                     |
| `unordered-async-iterator-helpers`                                            | 1          | 順序保証を捨てて性能を取る async helpers                                  |
| `iterator-unique`(`Iterator.prototype.unique`)                                | 1          | 重複除去。[GCL](../people/GCL.md) の指摘(隠れたコスト)で stalled          |

> ステージは [MF](../people/MF.md) のロードマップ([2026-05-19](../meetings/2026-05/2026-05-19.md))と直近会合の結論に基づく。リンクの無い提案は本 wiki で未精読(`proposals/` ページ未作成)。`agenda-index.md` の `stage:` 値は「その回で要求/議論された stage」であり現ステージとは限らない点に注意。

このほか [MF](../people/MF.md) は formal な提案にはなっていない wishlist として、collection への `.to(Set)`/`.to(Map)` protocol、short-circuiting reduce、`takeWhile`/`dropWhile`、`withCleanup`、`scan`、`into`、`tap` を挙げています(stage 0 にも未着手のため上表には含めない)。

## 横断テーマ

### `Array.prototype` の写像という設計原則

iterator helpers 系の多くは「`Array.prototype` に既にある操作を、消費を遅延したまま iterator に与える」という一貫した動機を持ちます(`includes` ↔ `Array.prototype.includes`、`join` ↔ `Array.prototype.join`、`zip` の array 版要望など)。逆に array 専用に見える操作(`Array.zip`)は motivation が弱いとして本体から分離されました([Joint Iteration](../proposals/joint-iteration.md) の論点参照)。

### 文字列を暗黙に iterate しない

入力として渡された文字列を(iterable であっても)iterate しない、という方針が family 全体で共有されています([LCA](../people/LCA.md) が一貫方針として主張、[Joint Iteration](../proposals/joint-iteration.md) 2024-06)。

### async 対応が律速

`async-iterator-helpers` が「全 method の並行 pull 対応」の spec text 作業に時間を要しており、それに依存する `concurrency-control` と `unordered-async-iterator-helpers` が Stage 1 で待機しています。async 系の鍵は「並行してどれだけ pull するか」の制御と、web の cancellation(AbortController)との統合です。

## 関連 family

- (未作成)`modules` / `intl` / `concurrency` — 今後 family 化する候補。`concurrency` は async iterator helpers の並行制御と重なる領域。

## 出典

- [2026-05-19](../meetings/2026-05/2026-05-19.md) — [MF](../people/MF.md) の iterator ロードマップ(本 family の骨子)
- [2026-05 会合 index](../meetings/2026-05/index.md) — Iterator Chunking / Includes が Stage 3 へ
- [agenda-index](../_generated/agenda-index.md) — 各提案の議題・stage シグナル(索引)
