---
title: Iterator Sequencing
slug: iterator-sequencing
status: shipped
current_stage: 4
ecma: [262]
champions: [MF]
first_seen: "2023-09"
reached_stage4: "2025-11"
families: [iterator]
tags: [proposal, iterator]
---

## Overview

Adds `Iterator.concat(...iterables)`: a function that produces a new iterator yielding all values of the passed iterables, in order. It is the concatenation counterpart for the iterator world (strings have `concat`, arrays have spread and `flat`), and pairs with the namespace methods of iterator helpers.

Championed by [MF](../people/MF.md) (Michael Ficarra). A member of the `iterator` family.

## Stage history

| Meeting                                                                             | What happened                                                                                                                                                                                                                                                     | Stage      |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [2023-09](https://github.com/tc39/notes/blob/main/meetings/2023-09/september-27.md) | First presented. Reached Stage 1                                                                                                                                                                                                                                  | → 1        |
| [2024-02](https://github.com/tc39/notes/blob/main/meetings/2024-02/feb-6.md)        | Stage 2 not sought: critical feedback on the naming/design ([JHD](../people/JHD.md): anything named `concat` should use array flattening semantics; [KG](../people/KG.md): variadic `Iterator.from` is inconsistent with every other `from`). Remained at Stage 1 | 1 (kept)   |
| [2024-06](https://github.com/tc39/notes/blob/main/meetings/2024-06/june-11.md)      | **Reached Stage 2**. Scope narrowed: the unbounded/infinite case dropped ("no desire at the moment to pursue that in a separate proposal"). Stage 2.7 reviewers: [NRO](../people/NRO.md), [JMN](../people/JMN.md), [RGN](../people/RGN.md)                        | 1 → 2      |
| [2024-10](https://github.com/tc39/notes/blob/main/meetings/2024-10/october-08.md)   | Reached Stage 2.7                                                                                                                                                                                                                                                 | 2 → 2.7    |
| [2024-12](https://github.com/tc39/notes/blob/main/meetings/2024-12/december-02.md)  | Stage 3 requested; not granted - [SYG](../people/SYG.md) wanted the Test262 PR merged first. [MF](../people/MF.md) to ask again once merged                                                                                                                       | 2.7 (kept) |
| [2025-05](https://github.com/tc39/notes/blob/main/meetings/2025-05/may-28.md)       | Stage 3 requested; not granted - the committee chose to back out the `yield*`-alignment changes (PRs #18, #19/#23), and [MF](../people/MF.md) left with the changes rather than ask for Stage 3 with modifications                                                | 2.7 (kept) |
| [2025-07](https://github.com/tc39/notes/blob/main/meetings/2025-07/july-28.md)      | **Reached Stage 3** (back-out landed as PR #26; support from [DLM](../people/DLM.md), [KG](../people/KG.md), [NRO](../people/NRO.md), [MM](../people/MM.md))                                                                                                      | 2.7 → 3    |
| [2025-11](https://github.com/tc39/notes/blob/main/meetings/2025-11/november-18.md)  | **Reached Stage 4** (two implementations for about a year: JSC, and SpiderMonkey shipping in Firefox 147)                                                                                                                                                         | 3 → 4      |

```mermaid
xychart-beta
    title "Iterator Sequencing stage 2012-2026"
    x-axis [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    y-axis "Stage" 0 --> 4
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2.7, 4, 4]
```

> Stage 1 in 2023-09, Stage 2 in 2024-06 (a 2024-02 request was not brought to consensus), Stage 2.7 in 2024-10, Stage 3 in 2025-07 (a 2025-05 request was deferred), Stage 4 in 2025-11.

## Main issues

### A quiet, fast track (2023-2025)

The proposal advanced briskly, with two hiccups. The 2024-02 Stage 2 request was not brought to a vote: [JHD](../people/JHD.md) argued anything named `concat` should use the same flattening semantics as `Array.prototype.concat` (which [MF](../people/MF.md) wasn't interested in adopting, prompting a name search), and [KG](../people/KG.md) objected that a variadic `Iterator.from` would be inconsistent with every other `from` method ("if you pass it two things, it's going to change the behavior and then also stick them together... not really how any of the existing `from` methods work"). [MF](../people/MF.md) came back in 2024-06 with `Iterator.concat`, the infinite case dropped, and Stage 2 followed. At the 2024-12 Stage 3 request [SYG](../people/SYG.md) felt strongly that the Test262 tests - sitting in an unmerged PR - had to land first ("I want them to be in the repo to be runnable"), and [MF](../people/MF.md) withdrew rather than put test262 maintainers on the spot. The 2025-05 request stalled the opposite way: since 2.7 the proposal had accumulated `yield*`-alignment changes at [ABL](../people/ABL.md)'s request (reusing IteratorResult objects, reading `.value` off the final result), and the discussion concluded these were chasing the wrong goal - `yield*` can leave the underlying iterator open where `Iterator.concat` always closes it, so "every time we get close to `yield*`, there's less desirable behavior" ([MF](../people/MF.md)). [RGN](../people/RGN.md), once the difference was confirmed: "we have got these differences... I am very enthusiastic about revisiting the past decisions that were based on matching `yield*`." [MF](../people/MF.md) took the back-out home instead of asking for Stage 3 with modifications ("I think it's probably best that I make all the changes... and then come back for Stage 3"). With the back-out landed (PR #26), Stage 3 came in 2025-07. JSC implemented it in 2024-10 behind a flag, SpiderMonkey followed in 2024-11; the Stage 4 request in 2025-11 noted two implementations for approximately one year and no signals from V8, which is not required for Stage 4.

## Related proposals

- [Joint Iteration](../proposals/joint-iteration.md) (`Iterator.zip`) / [Iterator Chunking](../proposals/iterator-chunking.md) / [Iterator Includes](../proposals/iterator-includes.md) / [Iterator Join](../proposals/iterator-join.md) - the same wave of iterator-helper follow-ons.
- family: [Iterator helpers and friends](../families/iterator.md)

## Sources

- [2023-09 september-27](https://github.com/tc39/notes/blob/main/meetings/2023-09/september-27.md) - Stage 1
- [2024-02 feb-6](https://github.com/tc39/notes/blob/main/meetings/2024-02/feb-6.md) - Stage 2
- [2024-10 october-08](https://github.com/tc39/notes/blob/main/meetings/2024-10/october-08.md) - Stage 2.7
- [2024-12 december-02](https://github.com/tc39/notes/blob/main/meetings/2024-12/december-02.md) - Stage 3 request deferred (Test262 tests unmerged)
- [2025-05 may-28](https://github.com/tc39/notes/blob/main/meetings/2025-05/may-28.md) - Stage 3 request deferred (back out the `yield*`-alignment changes)
- [2025-07 july-28](https://github.com/tc39/notes/blob/main/meetings/2025-07/july-28.md) - Stage 3
- [2025-11 november-18](https://github.com/tc39/notes/blob/main/meetings/2025-11/november-18.md) - Stage 4
