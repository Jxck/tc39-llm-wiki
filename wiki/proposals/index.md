# Proposal stage index

> **Generated.** `tools/extract_proposals.py` builds this from `raw/proposals/` (canonical). Do not edit by hand (regenerated whenever Update pulls `raw/proposals`).
> Current stage comes from raw/proposals. Ingested proposals link as `[Title](<slug>.md)`; unlinked titles are catalog-only in this wiki.
> **Stage 4 lists only proposals not yet in ECMAScript (publication year 2026 or later)** (shipped finished proposals are omitted). Stage 3 and below are listed in full.
> Counts: ECMA-262 222 / ECMA-402 20.

## ECMA-262

### Stage 4 — not yet in ECMAScript (publication year 2026 or later) (14 / 80 including already shipped)

- [Array.fromAsync](array-from-async.md) — expected publication 2026
- [Atomics.pause](atomics-pause.md) — expected publication 2027
- [Error.isError](error-is-error.md) — expected publication 2026
- [Explicit Resource Management](explicit-resource-management.md) — expected publication 2027
- [iterator chunking](iterator-chunking.md) — expected publication 2027
- [Iterator Includes](iterator-includes.md) — expected publication 2027
- [Iterator Join](iterator-join.md) — expected publication 2027
- [Iterator Sequencing](iterator-sequencing.md) — expected publication 2026
- [Joint Iteration](joint-iteration.md) — expected publication 2027
- [JSON.parse source text access](json-source-text.md) — expected publication 2026
- [Math.sumPrecise](math-sum-precise.md) — expected publication 2026
- [Temporal](temporal.md) — expected publication 2027
- [Uint8Array to/from Base64](uint8array-base64.md) — expected publication 2026
- [Upsert](upsert.md) — expected publication 2026

### Stage 3 (10)

- [Await Dictionary](await-dictionary.md)
- [Curtailing the power of "Thenables"](thenable-curtailment.md)
- [Deferring Module Evaluation](import-defer.md)
- [Dynamic Code Brand Checks](dynamic-code-brand-checks.md)
- [Error Stack Accessor](error-stack-accessor.md)
- [Import Text](import-text.md)
- Legacy RegExp features in JavaScript
- [Non-extensible Applies to Private](nonextensible-applies-to-private.md)
- [RegExp Buffer Boundaries (\A, \z, \Z)](regexp-buffer-boundaries.md)
- Source Phase Imports

### Stage 2.7 (9)

- Decorator Metadata
- [Decorators](decorators.md)
- Deferred Re-exports
- [ESM Phase Imports](esm-phase-imports.md)
- [export all from](export-all-from.md)
- [Immutable ArrayBuffers](immutable-arraybuffer.md)
- [Import Bytes](import-bytes.md)
- JSON.parse options
- [ShadowRealm](shadowrealm.md)

### Stage 2 (28)

- ["Discard" (void) Bindings](discard-bindings.md)
- [Amount](amount.md)
- [Async Context](async-context.md)
- Async Iterator helpers
- [Bigint from exponential](bigint-from-exponential.md)
- collection normalization
- [Composites](composite-keys.md)
- Destructure Private Fields
- [Error code property](error-code-property.md)
- [Error.captureStackTrace](error-capture-stack-trace.md)
- [Extractors](extractors.md)
- Function implementation hiding
- function.sent metaproperty
- [Fused Multiply-Add](fused-multiply-add.md)
- Iterator.range
- [Math.clamp](math-clamp.md)
- Module Declarations
- Module Expressions
- [Native Promise Predicate](native-promise-predicate.md)
- Object.keysLength
- Pipeline Operator
- Propagate active ScriptOrModule with JobCallback Record
- [SeededPRNG](seeded-prng.md)
- String.dedent
- [Structs: Fixed Layout Objects and Some Synchronization Primitives](shared-structs.md)
- Symbol Predicates
- [Sync Imports](import-sync.md)
- [throw expressions](throw-expressions.md)

### Stage 1 (106)

- Abort Controller
- Alias Accessors
- Array Equality
- Array filtering
- Array.prototype.unique()
- [Array.zip and Array.zipKeyed](array-zip.md)
- Asset References
- async do expressions
- Async initialization
- await operations
- BigInt Math
- Binary AST
- Block Params
- Built In Modules (aka JS Standard Library)
- [Bulk-add array elements](bulk-add-array-elements.md)
- Call-this operator
- Cancellation API
- class Access Expressions
- Class Brand Checks
- Class Method Parameter Decorators
- Collection methods
- [Compare Strings by Codepoint](compare-strings-by-codepoint.md)
- [Comparisons](comparisons.md)
- Compartments
- Composable Accessors via built-in decorators
- [Concurrency Control](concurrency-control.md)
- Cryptographically Secure Random Number Generation
- DataView get/set Uint8Clamped methods
- [Decimal](decimal.md)
- Declarations in Conditionals
- Deep Path Properties in Record Literals
- [Disposable AsyncContext.Variable](disposable-asynccontext.md)
- do expressions
- Double-Ended Iterator and Destructuring
- Dynamic Modules
- Emitter
- [Enums](enums.md)
- Error option framesAbove
- Error option limit
- Error stacks
- export v from "mod"; statements
- Extensions
- [Faster Promise adoption](native-promise-adoption.md)
- First-class protocols
- Freezing prototypes
- [Function and Object Literal Decorators](function-and-object-literal-decorators.md)
- Function Memoization
- Function once
- Get Intrinsic
- Grouped Accessors and Auto-Accessors
- IDL for ECMAScript
- [Improved Escapes for Template Literals](improve-template-literals.md)
- Inspector
- [Iterator unique](iterator-unique.md)
- Legacy reflection features for functions in JavaScript
- Limited ArrayBuffer
- [Linear Matching](linear-matching.md)
- Locale Extensions
- [Map get and delete](map-get-and-delete.md)
- Mass Proxy Revocation
- Maximally minimal mixins
- [Module Global](module-global.md)
- Module Keys
- Module sync assert
- Modulus and Additional Integer Math
- [More Random Functions](more-random-functions.md)
- Negated in and instanceof operators
- new.initialize
- Object pick/omit
- Object.freeze + Object.seal syntax
- [Object.getNonIndexStringProperties()](object-get-non-index-string-properties.md)
- [Object.propertyCount](object-propertycount.md)
- Observable
- of and from on collection constructors
- [OOM Fails Fast](dont-remember-panicking.md)
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
- [Signals](signals.md)
- Slice notation
- [Stabilize](stabilize.md)
- Standardized Debug
- [Strict Enforcement of 'using'](using-enforcement.md)
- String.cooked
- String.prototype.codePoints
- Support for Distributed Promise Pipelining
- Type Annotations
- [TypedArray Concat](typedarray-concat.md)
- [TypedArray Find Within](typedarray-find-within.md)
- uniform parsing of quasi-standard Date.parse input
- [Unordered Async Iterator Helpers](unordered-async-iterator-helpers.md)
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

### Inactive / Withdrawn (41)

- "use module" — Inactive
- ArrayBuffer.prototype.transfer — Withdrawn
- Blöcks — Withdrawn
- Builtins.typeOf() and Builtins.is() — Withdrawn
- Callable class constructors — Withdrawn
- Cancelable Promises — Withdrawn
- Date.parse fallback semantics — Inactive
- Distinguishing literal strings — Withdrawn
- Dynamic Import Host Adjustment — Withdrawn
- Dynamic Module Reform — Withdrawn
- Extensible numeric literals — Withdrawn
- Function helpers — Presented
- Function.pipe and flow — Withdrawn
- Generator arrow functions — Withdrawn
- Generic Comparison — Withdrawn
- Getting last element of Array — Withdrawn
- Improving iteration on Objects — Withdrawn
- [isTemplateObject](is-template-object.md) — Withdrawn
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
- RegExp Atomic Groups & Possessive Quantifiers — engines
- Sequence properties in Unicode property escapes — Withdrawn
- SIMD.JS - SIMD APIs — Stage
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

### Stage 4 — not yet in ECMAScript (publication year 2026 or later) (2 / 18 including already shipped)

- [Intl Era and MonthCode Proposal](intl-era-month-code.md) — expected publication 2026
- [Intl Locale Info](intl-locale-info.md) — expected publication 2026

### Stage 3 (1)

- [Keep trailing zeros in Intl.NumberFormat and Intl.PluralRules](intl-keep-trailing-zeros.md)

### Stage 2 (2)

- eraDisplay option for Intl.DateTimeFormat
- [More Currency Display Choices](more-currency-display-choices.md)

### Stage 1 (12)

- [Default Behaviours for some Intl APIs](intl-default-behaviours.md)
- [explore associating a unit with a number](intl-unit-protocol.md)
- [Intl Energy Units](intl-energy-units.md)
- Intl LocaleMatcher
- [Intl Sequence Units](intl-sequence-units.md)
- [Intl.DateTimeFormat Alignment With Other Standards](intl-datetimeformat-alignment.md)
- [Intl.MessageFormat](intl-messageformat.md)
- Intl.MessageResource
- Intl.Segmenter v2
- Intl.ZonedDateTimeFormat
- Smart Unit Preferences in Intl.NumberFormat
- [Stable Formatting](stable-formatting.md)

### Stage 0 (2)

- Fix 9.2.3 LookupMatcher algorithm
- Intl.NumberFormat round option

### Inactive / Withdrawn (1)

- Intl.UnitFormat — Withdrawn
