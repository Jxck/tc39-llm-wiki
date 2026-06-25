# 全提案ステージ一覧

> **生成物**。`tools/extract_proposals.py` が `raw/proposals/`(canonical)から生成。手で編集しない(Update で `raw/proposals` を pull するたび再生成)。
> 現ステージの一次ソースは raw/proposals。精読済みの提案は `[Title](<slug>.md)` でページへリンク、未リンクは本 wiki で未精読(カタログのみ)。
> **Stage 4 はまだ ECMAScript に入っていないもの(2026 年以降に出版予定)だけを掲載**(出荷済みの finished は省略)。Stage 3 以下は全件。
> 掲載件数: ECMA-262 220 件 / ECMA-402 18 件。

## ECMA-262

### Stage 4 — まだ ECMAScript 未収載(2026 年以降に出版予定)(11 / 出荷済み含む全 77 件)

- Array.fromAsync — 出版予定 2026
- [Atomics.pause](atomics-pause.md) — 出版予定 2027
- Error.isError — 出版予定 2026
- [Explicit Resource Management](explicit-resource-management.md) — 出版予定 2027
- Iterator Sequencing — 出版予定 2026
- [Joint Iteration](joint-iteration.md) — 出版予定 2027
- JSON.parse source text access — 出版予定 2026
- Math.sumPrecise — 出版予定 2026
- [Temporal](temporal.md) — 出版予定 2027
- Uint8Array to/from Base64 — 出版予定 2026
- [Upsert](upsert.md) — 出版予定 2026

### Stage 3 (11)

- Deferring Module Evaluation
- Dynamic Code Brand Checks
- Error Stack Accessor
- Import Text
- iterator chunking
- Iterator Includes
- Iterator Join
- Legacy RegExp features in JavaScript
- Non-extensible Applies to Private
- RegExp Buffer Boundaries (\A, \z, \Z)
- Source Phase Imports

### Stage 2.7 (7)

- Await Dictionary
- Decorator Metadata
- [Decorators](decorators.md)
- ESM Phase Imports
- Immutable ArrayBuffers
- Import Bytes
- ShadowRealm

### Stage 2 (27)

- "Discard" (void) Bindings
- [Amount](amount.md)
- Async Context
- Async Iterator helpers
- collection normalization
- Curtailing the power of "Thenables"
- Deferred Re-exports
- Destructure Private Fields
- Error.captureStackTrace
- Extractors
- Function implementation hiding
- function.sent metaproperty
- Iterator.range
- JSON.parseImmutable
- Math.clamp
- Module Declarations
- Module Expressions
- Native Promise Predicate
- Object.keysLength
- Pipeline Operator
- Propagate active ScriptOrModule with JobCallback Record
- SeededPRNG
- String.dedent
- Structs: Fixed Layout Objects and Some Synchronization Primitives
- Symbol Predicates
- Sync Imports
- throw expressions

### Stage 1 (105)

- Alias Accessors
- Array Equality
- Array filtering
- Array.prototype.unique()
- Array.zip and Array.zipKeyed
- Asset References
- async do expressions
- Async initialization
- await operations
- BigInt Math
- Binary AST
- Block Params
- Built In Modules (aka JS Standard Library)
- Bulk-add array elements
- Call-this operator
- Cancellation API
- class Access Expressions
- Class Brand Checks
- Class Method Parameter Decorators
- Collection methods
- Compare Strings by Codepoint
- Comparisons
- Compartments
- Composable Accessors via built-in decorators
- Composites
- Concurrency Control
- Cryptographically Secure Random Number Generation
- DataView get/set Uint8Clamped methods
- Decimal
- Declarations in Conditionals
- Deep Path Properties in Record Literals
- Disposable AsyncContext.Variable
- do expressions
- Double-Ended Iterator and Destructuring
- Dynamic Modules
- Emitter
- Enums
- Error option framesAbove
- Error option limit
- Error stacks
- export all from
- export v from "mod"; statements
- Extensions
- Faster Promise adoption
- First-class protocols
- Freezing prototypes
- Function and Object Literal Decorators
- Function Memoization
- Function once
- Get Intrinsic
- Grouped Accessors and Auto-Accessors
- IDL for ECMAScript
- Improved Escapes for Template Literals
- Inspector
- Iterator unique
- Legacy reflection features for functions in JavaScript
- Limited ArrayBuffer
- Locale Extensions
- Mass Proxy Revocation
- Maximally minimal mixins
- Module Global
- Module Keys
- Module sync assert
- Modulus and Additional Integer Math
- More Random Functions
- Negated in and instanceof operators
- new.initialize
- Object pick/omit
- Object.freeze + Object.seal syntax
- Object.getNonIndexStringProperties()
- Object.propertyCount
- Observable
- of and from on collection constructors
- OOM Fails Fast
- Optional chaining in assignment LHS
- Partial application
- Pattern Matching
- Policy Maps and Sets
- Preserve Host Virtualizability
- Private declarations
- Prototype pollution mitigation
- Readonly Collections
- RegExp \R Escape
- RegExp Atomic Operators
- RegExp Extended Mode and Comments
- Restrict subclassing support in built-in methods
- Reverse iteration
- Reversible string split
- Richer Keys
- SES (Secure EcmaScript)
- Signals
- Slice notation
- Stabilize
- Standardized Debug
- Strict Enforcement of 'using'
- String.cooked
- String.prototype.codePoints
- Support for Distributed Promise Pipelining
- Type Annotations
- TypedArray Concat
- TypedArray Find Within
- uniform parsing of quasi-standard Date.parse input
- Unordered Async Iterator Helpers
- Wavy Dot: Syntactic Support for Promise Pipelining
- {BigInt,Number}.fromString

### Stage 0 (14)

- Additional metaproperties
- as destructuring patterns
- Catch Guard
- Defensible Classes
- Function bind syntax
- Function expression decorators
- Method parameter decorators
- Nested import declarations
- Object Shorthand Improvements
- Orthogonal Classes
- Reflect.{isCallable,isConstructor}
- Relationships
- String trim characters
- Structured Clone

### Inactive / Withdrawn (45)

- "use module" — Inactive
- %constructor%.construct — Never
- ArrayBuffer.prototype.transfer — Withdrawn
- Blöcks — Withdrawn
- Builtins.typeOf() and Builtins.is() — Withdrawn
- Callable class constructors — Withdrawn
- Cancelable Promises — Withdrawn
- Date.parse fallback semantics — Inactive
- deprecated — Never
- Distinguishing literal strings — Withdrawn
- Dynamic Import Host Adjustment — Withdrawn
- Dynamic Module Reform — Withdrawn
- Extensible numeric literals — Withdrawn
- from ... import — Never
- Function helpers — Presented
- Function.pipe and flow — Withdrawn
- Generator arrow functions — Withdrawn
- Generic Comparison — Withdrawn
- Getting last element of Array — Withdrawn
- Improving iteration on Objects — Withdrawn
- isTemplateObject — Withdrawn
- JSON.tryParse — Rejected
- Math Extensions — Withdrawn
- Math.signbit: IEEE-754 sign bit — Withdrawn
- Normative ICU Reference — Withdrawn
- Object enumerables — Rejected
- Object.shallowEqual — Withdrawn
- Operator overloading — Withdrawn
- Proposed Grammar change to ES Modules — Rejected
- [Record & Tuple](records-and-tuples.md) — Withdrawn
- RefCollection — Withdrawn
- RegExp Atomic Groups & Possessive Quantifiers — Never
- Sequence properties in Unicode property escapes — Withdrawn
- SIMD.JS - SIMD APIs — Stage
- String.prototype.at — Obsoleted
- Symbol.thenable — Withdrawn
- Tagged Collection Literals — Withdrawn
- Typed Objects — Postponed
- TypedArray stride parameter — Withdrawn
- Unused Function Parameters — Rejected
- Updates to Tail Calls to include an explicit syntactic opt-in — Inactive
- UUID — Withdrawn
- WeakRefs cleanupSome — Withdrawn
- Zones — Withdrawn
- {Set,Map}.prototype.toJSON — Rejected

## ECMA-402

### Stage 4 — まだ ECMAScript 未収載(2026 年以降に出版予定)(2 / 出荷済み含む全 18 件)

- [Intl Era and MonthCode Proposal](intl-era-month-code.md) — 出版予定 2026
- Intl Locale Info — 出版予定 2026

### Stage 3 (1)

- Keep trailing zeros in Intl.NumberFormat and Intl.PluralRules

### Stage 2 (2)

- eraDisplay option for Intl.DateTimeFormat
- More Currency Display Choices

### Stage 1 (10)

- Default Behaviours for some Intl APIs
- explore associating a unit with a number
- Intl LocaleMatcher
- Intl Sequence Units
- [Intl.MessageFormat](intl-messageformat.md)
- Intl.MessageResource
- Intl.Segmenter v2
- Intl.ZonedDateTimeFormat
- Smart Unit Preferences in Intl.NumberFormat
- Stable Formatting

### Stage 0 (2)

- Fix 9.2.3 LookupMatcher algorithm
- Intl.NumberFormat round option

### Inactive / Withdrawn (1)

- Intl.UnitFormat — Withdrawn
