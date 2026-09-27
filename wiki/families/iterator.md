---
title: Iterator helpers and friends
slug: iterator
kind: family
members: [iterator-helpers, iterator-sequencing, joint-iteration, iterator-chunking, iterator-includes, iterator-join, async-iterator-helpers, iterator-range, concurrency-control, unordered-async-iterator-helpers, iterator-unique]
tags: [family, iterator]
---

## Overview

A run of proposals that try to fill out a standard library for lazy iteration around `Iterator.prototype` and the `Iterator` namespace. The starting point is **Iterator Helpers** (`map` / `filter` / `take` / `drop` / `flatMap` / `reduce` / `toArray`, and others: lazy versions of the array-prototype equivalents), which has reached Stage 4. Since then the set has grown by porting operations that `Array.prototype` already has onto iterators: concatenation (not [Joint Iteration](../proposals/joint-iteration.md); it is `iterator-sequencing` = `Iterator.concat`), zipping ([Joint Iteration](../proposals/joint-iteration.md) = `Iterator.zip`), splitting (chunking), and search (includes).

There have been many recent agenda items. In 2026-05 [MF](../people/MF.md) presented a "roadmap for the iterator space" ([2026-05-19](../meetings/2026-05/2026-05-19.md)). This family uses that roadmap as its axis and collects the current state of each proposal in one place. Per-proposal history and issues live on the `proposals/` pages (where those pages exist).

## Members

| Proposal                                                                         | Current stage | In short                                                                                         |
| -------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------ |
| `iterator-helpers`                                                               | 4             | The MVP. Lazy `map` / `filter` / `take` / `drop` / `flatMap` / `reduce` / `toArray`, and others  |
| `iterator-sequencing` (`Iterator.concat`)                                        | 4             | Concatenates zero or more iterators and yields everything they yield                             |
| [Joint Iteration](../proposals/joint-iteration.md) (`Iterator.zip` / `zipKeyed`) | 4             | Zips several iterators by position (reached in 2026-05)                                          |
| [Iterator Chunking](../proposals/iterator-chunking.md) (`chunks` / `windows`)    | 3             | Consumes several values at once (no overlap = chunks, overlap = windows). Stage 3 in 2026-05     |
| [Iterator Includes](../proposals/iterator-includes.md)                           | 3             | The equivalent of `Array.prototype.includes`. Stage 3 in 2026-05                                 |
| [Iterator Join](../proposals/iterator-join.md)                                   | 3             | The equivalent of `Array.prototype.join` ([KG](../people/KG.md) champion). Stage 3 in 2026-05    |
| `async-iterator-helpers`                                                         | 2             | The async version of iterator helpers. Spec work in progress for concurrent pull on every method |
| `iterator-range` (`Iterator.range`)                                              | 2             | Numeric range generation. Long stall                                                             |
| `concurrency-control`                                                            | 1             | Controls how many async-iterator pulls run at once. Waiting on async helpers                     |
| `unordered-async-iterator-helpers`                                               | 1             | Async helpers that drop the order guarantee in exchange for performance                          |
| `iterator-unique` (`Iterator.prototype.unique`)                                  | 1             | Dedup. Stalled after [GCL](../people/GCL.md) pointed out a hidden cost                           |

> Stages follow [MF](../people/MF.md)'s roadmap ([2026-05-19](../meetings/2026-05/2026-05-19.md)) and the conclusions of recent meetings. Proposals without a link are not ingested in this wiki yet (no `proposals/` page). A `stage:` value in `agenda-index.md` is the stage asked for or discussed at that meeting, which is not necessarily the current stage.

[MF](../people/MF.md) also listed a wishlist that is not a formal proposal: a `.to(Set)` / `.to(Map)` protocol for collections, a short-circuiting reduce, `takeWhile` / `dropWhile`, `withCleanup`, `scan`, `into`, and `tap` (not even started at stage 0, so they are not in the table above).

## Cross-cutting themes

### The design principle of mirroring `Array.prototype`

Most of the iterator-helpers line shares one motivation: give the iterator an operation `Array.prototype` already has, while keeping consumption lazy (`includes` alongside `Array.prototype.includes`, `join` alongside `Array.prototype.join`, requests for an array version of `zip`, and so on). In the other direction, an operation that looks array-specific (`Array.zip`) was split out of the main proposal because the motivation was weak (see the issues on [Joint Iteration](../proposals/joint-iteration.md)).

### Do not iterate strings implicitly

The whole family shares the policy of not iterating a string that was passed as input, even though a string is iterable ([LCA](../people/LCA.md) argued for this as a consistent policy; [Joint Iteration](../proposals/joint-iteration.md), 2024-06).

### Async support is the rate limiter

`async-iterator-helpers` is taking time on spec text for "concurrent pull on every method," and `concurrency-control` and `unordered-async-iterator-helpers`, which depend on it, are waiting at Stage 1. The key for the async line is controlling how many pulls run concurrently, and integrating with web cancellation (AbortController).

## Related families

- (not yet written) `modules` / `intl` / `concurrency` — candidates to become families later. `concurrency` overlaps the concurrent-control part of async iterator helpers.

## Sources

- [2026-05-19](../meetings/2026-05/2026-05-19.md) — [MF](../people/MF.md)'s iterator roadmap (the spine of this family)
- [2026-05 meeting index](../meetings/2026-05/README.md) — Iterator Chunking / Includes to Stage 3
- [agenda-index](../_generated/agenda-index.md) — agenda items and stage signals for each proposal (an index)
