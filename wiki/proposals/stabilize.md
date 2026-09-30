---
title: Stabilize
slug: stabilize
status: stage1
current_stage: 1
ecma: [262]
champions: [MM, CM, RGN, MAH]
first_seen: "2024-12"
tags: [proposal, object-model, integrity]
---

## Overview

"Stabilize and other integrity traits": a full unbundling of JavaScript's object integrity system into orthogonal, opt-in **traits**. The existing ladder - non-extensible → sealed → frozen - bundles several independent guarantees, and each bundle has friction: hardening an API surface breaks legacy prototype code, and frozen objects can still grow private fields via `return override`, which dooms fixed-shape implementations.

The traits on the table: **fixed** (no private-field extension via return override - the trait structs need for fixed shapes, and the retcon for the window proxy's special dispensation), **overridable** (exempts an object from the assignment-override mistake, so freezing primordials stops breaking pre-class prototype code), **non-trapping** (proxies on the target forward everything without invoking handler traps - closing the one remaining re-entrancy hazard in defensive programming), plus a possible split of non-extensible into "no new properties" and "prototype locked". Everything is explored against two counter-proposals: the minimal picture (just `fixed` broken out of a rebundled stable) and a parameterized `protect`/`isProtected` proxy trap pair instead of ten new traps.

## Stage history

| Meeting                                                                            | Event                                                                                                                                                                   | Stage |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| [2024-12](https://github.com/tc39/notes/blob/main/meetings/2024-12/december-03.md) | Presented by [MM](../people/MM.md). Stage 1 with explicit support from [SYG](../people/SYG.md), weak support from [JWK](../people/JWK.md), plus [JHD](../people/JHD.md) | → 1   |

```mermaid
xychart-beta
    title "Stabilize stage 2012-2026"
    x-axis [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    y-axis "Stage" 0 --> 4
    line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
```

> First presented in 2024-12 and granted Stage 1 in the same session; presented as the distillation of years of Agoric hardening work, but new to the committee as a proposal.

## Main issues

### Unbundle - and the structs tail wagging the dog

The framing came from a hallway conversation with [SYG](../people/SYG.md): a single stronger "stable" level (implying frozen) could not apply to shared structs, which must stay mutable yet need fixed shapes. Hence "bundle or unbundle" - the traits were split so `fixed` alone could apply to non-frozen objects. [SYG](../people/SYG.md) supported Stage 1 _because_ of `fixed` for shared structs, and floated V8's simplification preference: **retcon non-extensible to imply fixed** if web-compatible, measured with a use counter on globalThis mutations. [MM](../people/MM.md) liked it on the spot: neither the return-override nor assignment-override mistake has known intentional production use. The window-proxy rationale for keeping `fixed` unbundled, [MM](../people/MM.md) conceded, is "not" compelling.

### Is the object model getting too complex?

[KG](../people/KG.md) endorsed the exploration but named the cost: "changes to the object model are very, very conceptually expensive for developers... Having more states that things can be in is at least potentially very expensive in terms of reasoning" - not convinced any of it is worth doing, happy to explore in Stage 1. [KM](../people/KM.md) warned of implementation complexity (the frozen-logic long tail of security bugs). [NRO](../people/NRO.md) argued the opposite reading: the fully unbundled picture is _simpler_ to explain, because developers already struggle to distinguish sealed from non-extensible - one labeled trait at a time beats three at once - and asked for a glossary in the proposal. [MM](../people/MM.md)'s own preference: the minimal picture, though he presented it as an open Stage 1 question.

## Related proposals

- [nonextensible-applies-to-private](nonextensible-applies-to-private.md) - the existing-spec corner (private fields landing on non-extensible objects) that `fixed` would close.
- `shared structs` - the fixed-shape consumer that motivated breaking `fixed` out (no page yet).

## Sources

- [2024-12 december-03](https://github.com/tc39/notes/blob/main/meetings/2024-12/december-03.md) - Stage 1 ([MM](../people/MM.md))
