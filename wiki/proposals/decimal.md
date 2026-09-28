---
title: Decimal
slug: decimal
status: stage1
current_stage: 1
ecma: [262]
champions: [PFC, API, JMN]
first_seen: "2017-11"
tags: [proposal, numeric]
---

## Overview

Decimal adds exact base-10 arithmetic to JavaScript, backed by the IEEE 754 **Decimal128** format (128 bits, up to 34 significant digits). The motivating pain is that binary floating point (`Number`) cannot represent common decimal fractions exactly, which produces the classic `0.1 + 0.2 !== 0.3` class of bugs wherever human-facing numbers (money above all) are computed. A secondary motivation is data interchange: many databases, RPC schemas, and other languages (SQL, Java, Python, C#) have a native decimal type, and JavaScript sitting in the middle of such a system today has no faithful way to represent those values without going through strings.

The current design is a plain object/class (`Decimal`) with a constructor and static/instance methods for basic arithmetic (add, subtract, multiply, divide, remainder), not a new primitive: it has no operator overloading and no literal syntax. This is the result of years of back-and-forth — the proposal originally followed the `BigInt` model (new primitive, operator overloading, literal suffix), but dropped all three based on repeated, strong pushback from V8 and SpiderMonkey. Values always normalize to a single canonical mathematical value (no distinguishable trailing zeros); the precision/unit-carrying use cases that motivated keeping trailing zeros were split off into a separate proposal, now [Amount](../proposals/amount.md).

## Stage history

| Meeting                                                     | Event                                                                                                                                              | Stage    |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [2017-11](../../raw/notes/meetings/2017-11/nov-29.md)       | Presented by API as "Decimal"; reached Stage 0                                                                                                     | → 0      |
| [2020-02](../../raw/notes/meetings/2020-02/february-4.md)   | Presented by [DE](../people/DE.md) as "BigDecimal"; reached Stage 1                                                                                | 0 → 1    |
| [2021-12](../../raw/notes/meetings/2021-12/dec-15.md)       | [SHO](../people/SHO.md) takes over presenting alongside [PFC](../people/PFC.md)/API; temperature check favors a new primitive (13 for, 0 blocking) | 1 (kept) |
| [2023-07](../../raw/notes/meetings/2023-07/july-12.md)      | "Decimal: Open-ended discussion"; [SYG](../people/SYG.md) (V8) leans toward not doing this without operator overloading                            | 1 (kept) |
| [2023-09](../../raw/notes/meetings/2023-09/september-27.md) | Operator overloading, literal syntax, and primitive-ness dropped, per V8/SpiderMonkey feedback                                                     | 1 (kept) |
| [2024-04](../../raw/notes/meetings/2024-04/april-11.md)     | Stage 2 requested; blocked by [MM](../people/MM.md) and [JHD](../people/JHD.md)                                                                    | 1 (kept) |
| [2024-10](../../raw/notes/meetings/2024-10/october-09.md)   | Dropped trailing-zero/precision tracking to simplify; spun off "numeric value with precision"                                                      | 1 (kept) |
| [2025-02](../../raw/notes/meetings/2025-02/february-19.md)  | "A unified vision for measure and decimal" presented jointly; the spinoff is renamed Amount                                                        | 1 (kept) |
| [2026-07](../../raw/notes/meetings/2026-07/july-22.md)      | Presented by [CLA](../people/CLA.md); primitive-vs-object deadlock restated, [JHD](../people/JHD.md) treats it as a Stage 2 blocker                | 1 (kept) |

```mermaid
xychart-beta
    title "Decimal stage 2012-2026"
    x-axis [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    y-axis "Stage" 0 --> 4
    line [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
```

> Reached Stage 0 in 2017-11, Stage 1 in 2020-02, and has not moved since (stalled at Stage 1 for six years as of 2026-07).

## Main issues

### Primitive vs. object-based API

What's at stake is whether Decimal should be a new primitive type (like `BigInt`, with operator overloading and a literal suffix) or a plain object with methods. [JHD](../people/JHD.md) has argued since 2024-10 that an object-only Decimal is not worth shipping, because ergonomics without operators are poor enough that userland libraries remain competitive; at the 2026-07 meeting he stated this explicitly as a Stage 2 blocker ("I don't want the object form in the language if the primitive form isn't guaranteed to also be there eventually"). On the other side, V8 and SpiderMonkey implementers ([SYG](../people/SYG.md), [KM](../people/KM.md), [DLM](../people/DLM.md)) have repeatedly cited `BigInt`'s poor real-world return on investment (heavy implementation cost, adoption mostly limited to crypto-mining scripts) as their reason for refusing a new primitive; [ACE](../people/ACE.md) (Bloomberg, a primary driver of the proposal) explicitly said an object API is "absolutely perfectly" fine for their use case.

- Discussed at [2020-02](../../raw/notes/meetings/2020-02/february-4.md), [2021-12](../../raw/notes/meetings/2021-12/dec-15.md), [2023-07](../../raw/notes/meetings/2023-07/july-12.md), [2023-09](../../raw/notes/meetings/2023-09/september-27.md), [2024-04](../../raw/notes/meetings/2024-04/april-11.md), [2024-10](../../raw/notes/meetings/2024-10/october-09.md), and [2026-07](../../raw/notes/meetings/2026-07/july-22.md).
- Unresolved as of 2026-07. Champion [CLA](../people/CLA.md) summarized it directly: "There are major concerns with the current Object API and not being primitive. There are also major concerns from browsers to introduce the proposal as a Primitive."

### IEEE 754 Decimal128 conformance vs. developer ergonomics

[WH](../people/WH.md) pushed hard, across several meetings, for the proposal to follow IEEE 754 Decimal128 semantics precisely — keeping `NaN`, `+Infinity`/`-Infinity`, `-0`, and not inventing new math-library semantics — arguing that deviating creates "an anticoordination point" for anyone trying to interoperate with existing IEEE-754-based systems. Champions ([DE](../people/DE.md), [JMN](../people/JMN.md)) initially leaned toward making exceptional operations (division by zero, etc.) throw rather than produce `NaN`/infinities, on the theory that JS developers expect a receipt to never print "NaN". This was walked back after pushback (see [2023-09](../../raw/notes/meetings/2023-09/september-27.md), where API also argued for full IEEE-754 fidelity, citing cross-language interchange as the motivating case).

> [WH](../people/WH.md), [2023-07](../../raw/notes/meetings/2023-07/july-12.md): "This would be an enormous mistake. This is not cleaning up. This is introducing our own alternate standard for decimal which is different from what IEEE specified."

- Resolved in [WH](../people/WH.md)'s direction on the big questions (conformant arithmetic semantics); [WH](../people/WH.md) later praised the simplified, post-2024-10 design as "so much simpler" after trailing-zero tracking was dropped.

### Trailing zeros / precision (canonicalization) — spun off into Amount

IEEE 754 Decimal128 distinguishes `1.2` from `1.20` (the "cohort" concept), and [SFC](../people/SFC.md) argued strongly, from the Intl/formatting side, that this precision information must be preserved (e.g. "1 star" vs. "1.0 stars", or `-42.00` formatting to `-42.00` and not `-42`). Champions ([JMN](../people/JMN.md), [NRO](../people/NRO.md)) countered that preserving cohort distinctions forecloses ever making Decimal a primitive, and that IEEE's rules for propagating precision through arithmetic (a worked tax-calculation example in [2024-10](../../raw/notes/meetings/2024-10/october-09.md) needed six digits of precision to compute a two-digit answer) are confusing and arbitrary.

- Discussed in depth at [2024-10](../../raw/notes/meetings/2024-10/october-09.md) and [2025-02](../../raw/notes/meetings/2025-02/february-19.md) ("A unified vision for measure and decimal", presented jointly with [EAO](../people/EAO.md)).
- Resolved by scope-splitting: Decimal itself always normalizes to a single mathematical value (no observable trailing zeros), and the precision/unit-carrying use cases became a separate proposal — first called "numeric value with precision", then Measure, renamed **Amount** at [EAO](../people/EAO.md)'s suggestion. [Amount](../proposals/amount.md) reached Stage 2 in 2026-07 and is designed to be able to wrap a `Decimal` value if/when Decimal ships.

### Should Decimal exist in the language at all?

Some delegates ([SYG](../people/SYG.md), [MLS](../people/MLS.md), [EAO](../people/EAO.md) early on) questioned whether the use cases justify built-in support at all, versus continuing to rely on userland libraries (`decimal.js`, `big.js`, `bignumber.js`) — echoing the same ROI skepticism raised in the primitive debate. Champions countered with concrete production case studies: Bloomberg ([ACE](../people/ACE.md)) uses decimal pervasively for cross-language financial data interchange (C++/Python/JS via a shared schema), and Alibaba's DingTalk ([LIU](../people/LIU.md)) needs it for spreadsheet-formula calculations at scale.

- Discussed at [2021-12](../../raw/notes/meetings/2021-12/dec-15.md) ([SYG](../people/SYG.md): "we're currently unconvinced of the ROI for something like bigdecimal") and [2024-04](../../raw/notes/meetings/2024-04/april-11.md) (Bloomberg/DingTalk case studies presented).
- Not formally blocking on its own — the proposal has stayed at Stage 1 rather than being rejected — but it folds into the primitive-vs-object debate above: implementers are more willing to accept an object-only Decimal than to add a new primitive for it.

## Related proposals

- [Amount](../proposals/amount.md) — took over Decimal's precision/unit/trailing-zero use cases after the 2025-02 "unified vision" split; designed to wrap a `Decimal` value once Decimal exists.
- `Math.sumPrecise` / [Fused Multiply-Add](../proposals/fused-multiply-add.md) — reduce rounding error in binary-float arithmetic without introducing decimal arithmetic; cited in 2026-07 as adjacent proposals addressing part of the same motivating pain, but not a substitute for exact decimal math.
- [Temporal](../proposals/temporal.md) — cited repeatedly (2025-02) as the model for a strongly-typed API with explicit conversions, which Decimal/Amount's design discussions try to follow.

## Sources

- [2017-11](../../raw/notes/meetings/2017-11/nov-29.md) — Decimal for Stage 0
- [2020-02](../../raw/notes/meetings/2020-02/february-4.md) — BigDecimal for Stage 1
- [2021-12](../../raw/notes/meetings/2021-12/dec-15.md) — Decimals
- [2023-07](../../raw/notes/meetings/2023-07/july-12.md) — Decimal: Open-ended discussion
- [2023-09](../../raw/notes/meetings/2023-09/september-27.md) — Decimal: Stage 1 update and discussion
- [2024-04](../../raw/notes/meetings/2024-04/april-11.md) — Decimal for stage 2
- [2024-10](../../raw/notes/meetings/2024-10/october-09.md) — Decimal: Stage 1 Update
- [2025-02](../../raw/notes/meetings/2025-02/february-19.md) — A unified vision for measure and decimal
- [2026-07](../../raw/notes/meetings/2026-07/july-22.md) — Decimal stage 1 update
