---
title: Modules (module harmony)
slug: modules
kind: family
members: [es-modules, dynamic-import, import-meta, top-level-await, import-attributes, json-modules, import-bytes, export-from, source-phase-imports, import-defer, import-text, esm-phase-imports, import-sync, export-defer, export-all-from, module-scope-ceiling, module-expressions, module-declarations, compartments]
tags: [family, modules]
---

## Overview

The static module system of `import` / `export` that entered in ES2015 (once called "module harmony"), and the run of proposals stacked on top of it. On top of ES modules, extensions have continued along these axes: (1) **runtime import** (`import()`), (2) **meta information** (`import.meta`), (3) **async dependencies** (top-level await), (4) **import attributes** (import attributes / JSON modules), (5) **import phase** (source phase / defer), (6) **host integration** (HTML / Node / Wasm).

Recently (2024–2026) the active threads are **deferred evaluation** for startup performance (`import defer` / `export defer`), the **notion of a phase** (`import source` obtains a compiled source rather than an instance), **new import kinds** (`type: "text"`), and **scope isolation** in a supply-chain-security context (Module Scope Ceiling). Per-proposal history is on each proposal page (names with no page are inline code).

## Members

| Proposal                                                                            | Current stage    | In short                                                                                                                                 |
| ----------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `es-modules`                                                                        | 4 (ES2015)       | The static module system of `import` / `export`. The base of every module proposal                                                       |
| `dynamic-import` (`import()`)                                                       | 4 (2019-06)      | A function form that passes a specifier at runtime and imports a module asynchronously                                                   |
| `import-meta` (`import.meta`)                                                       | 4 (2020-03)      | Access to host-specific meta information of the running module (`import.meta.url` and others)                                            |
| `top-level-await`                                                                   | 4 (2021-05)      | Allows `await` at module top level, so a module can be awaited as an async dependency                                                    |
| [Import Attributes](../proposals/import-attributes.md) (formerly import assertions) | 4 (2024-10)      | Passes attributes to the host at import time, as `with { type: "json" }`. Renamed `assert` → `with`                                      |
| [JSON Modules](../proposals/json-modules.md)                                        | 4 (2024-10)      | Import JSON as a module with `import data from "./x.json" with { type: "json" }`                                                         |
| [Import Bytes](../proposals/import-bytes.md) (`type: "bytes"`)                      | 2.7 (2025-09)    | Import a file's bytes as an immutable `Uint8Array` with `with { type: "bytes" }`. Isomorphic asset reads                                 |
| `export-from` (`export * as ns from`)                                               | 4 (ES2020)       | Re-export syntax such as `export * as ns from "mod"`                                                                                     |
| `source-phase-imports`                                                              | 3 (2023-07)      | `import source x from` obtains a compiled source phase rather than an instance (Wasm and others)                                         |
| [import defer](../proposals/import-defer.md)                                        | 3 (2025-02)      | `import defer * as ns from` defers evaluation and evaluates synchronously on first access. For startup                                   |
| `import-text` (`type: "text"`)                                                      | 3 (2026-03)      | Import a file as a string with `with { type: "text" }`. Most of the spec is on the HTML / Fetch / CSP side                               |
| [ESM Phase Imports](../proposals/esm-phase-imports.md)                              | 2.7 (2024-12)    | Extends the source phase to ESM / Wasm. Obtain a compiled module and instantiate it with a custom import                                 |
| [Import Sync](../proposals/import-sync.md)                                          | 2 (2026-01)      | Synchronously obtain an already-loaded module ("the last feature of CommonJS"). Strict variant shares import defer's execution semantics |
| `export-defer`                                                                      | 2 (2.7 proposed) | Split from `import defer`. Propagates deferred evaluation / loading along a re-export path. For barrel files                             |
| [export all from](../proposals/export-all-from.md)                                  | 1 (2026-05)      | Solves `export * from` not re-exporting `default` (proxy / CDN module use)                                                               |
| `module-scope-ceiling`                                                              | 1                | Replaces a module's scope so lexical lookup does not reach the global. Supply-chain security                                             |
| `module-expressions`                                                                | 2                | Define a module inline as an expression outside a file (`module { ... }`). Motivated by handing one to a worker                          |
| `module-declarations`                                                               | 2                | Define a module declaratively inside a file (the sibling of module expressions)                                                          |
| `compartments`                                                                      | 1 (stalled)      | A module loader / isolated execution environment from SES. The loading layer of module harmony. Now split into other proposals           |

> Stages follow the conclusion of the meeting that last discussed each proposal (a `stage:` value in `agenda-index.md` is the stage requested at that meeting, which is not necessarily the current stage). `export-defer` proposed Stage 2.7 in 2025-11, but [GB](../people/GB.md) reserved judgment toward Stage 3, and as of 2026-05 it is still treated as a Stage 2 status update. `source-phase-imports` remains at Stage 3 (the latest meeting discussed a normative change, not an advancement). Proposals without a link are not ingested in this wiki yet.
>
> **Dynamic Import Host Adjustment** is in the module line, but withdrawal was confirmed in 2026-03 ([2026-03-10](../meetings/2026-03/2026-03-10.md)). CSS / HTML Modules are on the HTML (WHATWG) side, not TC39, so they are not members.

## Cross-cutting themes

### Import phase (source / instance / defer)

The recent center is an axis that chooses, in syntax, how far an import proceeds. Besides the ordinary instance phase, `import source` (compiled source phase) and `import defer` (deferred evaluation) share the same `import` grammar space. `source-phase-imports` → `esm-phase-imports` spreads this phase idea to Wasm / ESM.

### Deferred evaluation for startup performance (`import defer` / `export defer`)

The line that lowers the cost of evaluating a large dependency graph. `import defer` defers evaluation on the consumer side (Stage 3). `export defer` propagates the deferral along a re-export path on the library side (Stage 2). Using both together with a namespace import loses tree shaking, and filtered namespaces and similar ideas are under discussion ([2026-05-19](../meetings/2026-05/2026-05-19.md)). The champion is mainly [NRO](../people/NRO.md).

### Host integration (HTML / Node / Wasm)

The weight of the module spec is split between ECMA-262 and the host (HTML / Fetch / CSP, Node's `vm` module, Wasm). For `import-text`, "most of the spec is on the HTML side." For `esm-phase-imports`, clarifying Node integration was an issue ([2026-03-11](../meetings/2026-03/2026-03-11.md)).

### `assert` → `with` (how import attributes were renamed)

The attribute syntax for import flipped more than once: `with` → `if` → `assert` → `with`. `assert` carried a mental model of "does not affect the cache key" that did not fit the host's interpretation, so it was downgraded from Stage 3 to Stage 2, and in the end `with` was unified on and `assert` was dropped (downgrade in 2023-01, drop in 2024-07). The champion is [NRO](../people/NRO.md).

## Related families

- [Iterator helpers and friends](../families/iterator.md) — a proposal group in another category. An earlier example of a family.
- (not yet written) `concurrency` — adjacent to top-level await and AsyncContext.

## Sources

- [2019-06 june-4](https://github.com/tc39/notes/blob/main/meetings/2019-06/june-4.md) — dynamic `import()` Stage 4
- [2020-03 april-1](https://github.com/tc39/notes/blob/main/meetings/2020-03/april-1.md) — `import.meta` Stage 4 / Compartments Stage 1
- [2021-05 may-25](https://github.com/tc39/notes/blob/main/meetings/2021-05/may-25.md) — top-level await Stage 4
- [2023-01 jan-31](https://github.com/tc39/notes/blob/main/meetings/2023-01/jan-31.md) — import assertions downgraded from Stage 3 to 2
- [2023-07 july-12](https://github.com/tc39/notes/blob/main/meetings/2023-07/july-12.md) — Source Phase Imports Stage 3
- [2024-07 july-29](https://github.com/tc39/notes/blob/main/meetings/2024-07/july-29.md) — drop `assert` and unify on `with`
- [2024-10 october-08](https://github.com/tc39/notes/blob/main/meetings/2024-10/october-08.md) — Import Attributes + JSON Modules Stage 4
- [2025-02 february-18](https://github.com/tc39/notes/blob/main/meetings/2025-02/february-18.md) — `import defer` Stage 3
- [2025-11 november-18](https://github.com/tc39/notes/blob/main/meetings/2025-11/november-18.md) — `export defer` Stage 2.7 proposed (with a reservation)
- [2026-03 march-11](https://github.com/tc39/notes/blob/main/meetings/2026-03/march-11.md) — Import Text Stage 3 / ESM Phase Imports update
- [2026-05 may-20](https://github.com/tc39/notes/blob/main/meetings/2026-05/may-20.md) — export all from Stage 1 / Module Scope Ceiling / normative PRs for phase imports
- [agenda-index](../_generated/agenda-index.md) — agenda items and stage signals for each proposal (an index)
