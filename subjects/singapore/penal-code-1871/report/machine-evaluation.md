# Penal Code 1871 — machine evaluation report

**Run date:** 2026-09-09
**Verdict:** **0 type errors across all 17 modules; 55 of 55 assertions satisfied.**
No directive was skipped, stubbed or held back.

---

## 1. How it was run

No `jl4` CLI exists in this environment — no Haskell toolchain, no Docker, and the
`l4-rules` MCP server (`http://127.0.0.1:19415/mcp`, the VS Code extension's proxy) was not
running. What the tree does carry is `jl4-lsp.exe`, a **March 2026** language-server build,
at `thailand-cosmetics/tmp-vsix/extension/bin/win32-x64/`.

So the language server was driven directly as a batch checker. This works because
`jl4-core/src/L4/Diagnostic.hs` publishes directive results as LSP diagnostics:

| directive result | severity |
| --- | --- |
| assertion holds | Information — "assertion satisfied" |
| assertion fails / errors | **Error** — "assertion failed" |
| `REFUSE`d assertion | Warning |
| `#EVAL` reduction | Information — the value |

The harness is 118 lines of Node: spawn `jl4-lsp.exe`, LSP `initialize` with the subject
directory as `rootUri`, `textDocument/didOpen` one file, collect
`textDocument/publishDiagnostics` for that file's URI, settle 4 s after the last publish,
classify by severity, exit non-zero on any Error. Files are opened **one per server
process** — the server sets a single "file of interest" and does not reliably publish for
the others.

It is not committed here. This repository holds law; `l4-ide` holds tools, and a batch
checker belongs there (or, better, is made unnecessary by shipping the `l4` CLI). It is
reproducible from this description in well under an hour.

## 2. The harness was validated twice before it was trusted

A checker that reports silence as success is worse than no checker. Two probes:

**2.1 It sees a satisfied assertion.** A four-line file with two `#ASSERT`s and one `#EVAL`
returned exactly `errors 0, satisfied 2`.

**2.2 It sees an error injected into a dependency.** The concern is real, because six
modules in this subject carry no directives at all and were checked only through the
modules that import them. A deliberate type error — `1 PLUS TRUE` — was appended to a
scratch copy of `types.l4`, and `agent-cases.l4`, which reaches `types.l4` only
transitively through `agent-compliance.l4`, was re-run against it:

```
### agent-cases.l4 — errors 11, satisfied 0, warnings 0
  [ERROR] line 338-346: assertion failed          (all 9)
  [ERROR] line 348-349: Internal error: `wholly in Singapore` is not in scope.
```

All nine assertions collapsed. So an error anywhere in the import graph does surface on the
importing file, and a clean run of `agent-cases.l4` is real evidence about the whole graph
beneath it.

## 3. One compensation for a stale engine, and exactly what it costs

The available binary predates the `jl4-core` worktree beside it. The current `prelude.l4`
uses `@nonexhaustive` (3 sites) and `@infixl` (3 sites), and `prelude.l4` and `daydate.l4`
each contain a `REFUSE` — all newer than this binary's parser. The parse failed at the first
of them, so the **entire prelude was silently empty** and every prelude identifier reported
"could not find a definition".

That looks exactly like an encoding defect and is not one. Worked around by copying
`l4-ide/jl4-core/libraries/` to scratch, commenting out the six unknown annotations, and
stubbing the two `REFUSE` sites, then pointing `JL4_LIBRARY_PATH` at the scratch copy. **No
file in this repository was modified for the run.**

**Cost to confidence: none, and here rather less than none.** This subject uses no prelude
function at all — no `count`, `filter`, `elem`, `null`, `min`, `max`, no `LIST OF`, no
`DATE`, no `REFUSE`. It is booleans, records, enums and integer arithmetic throughout. The
prelude is imported for its operators and nothing else, so the patched library and the real
one are indistinguishable from where this encoding sits.

There is **no law-time axis** in this subject — nothing dated, no `RULES EFFECTIVE DATE` —
so the temporal gap that limited the `FinMont-demo` run does not arise here at all.

## 4. Results

| module | errors | assertions satisfied |
| --- | ---: | --- |
| `types.l4` | 0 | — (declarations only) |
| `chapter-1-preliminary.l4` | 0 | — (no directives) |
| `chapter-2-definitions.l4` | 0 | 8 |
| `chapter-2-explanations.l4` | 0 | 4 |
| `chapter-2-participation.l4` | 0 | 5 |
| `chapter-3-punishments.l4` | 0 | 9 |
| `chapter-4-exceptions.l4` | 0 | — (no directives) |
| `chapter-5-abetment.l4` | 0 | — (no directives) |
| `chapter-5a-conspiracy.l4` | 0 | 4 |
| `chapter-17-cheating.l4` | 0 | 6 |
| `chapter-17-property.l4` | 0 | 2 |
| `chapter-17-fraud.l4` | 0 | 4 |
| `chapter-18-forgery.l4` | 0 | — (no directives) |
| `chapter-21-22-speech.l4` | 0 | 2 |
| `chapter-23-attempts.l4` | 0 | 2 |
| `agent-compliance.l4` | 0 | — (no directives) |
| `agent-cases.l4` | 0 | 9 |
| **total** | **0** | **55 of 55** |

### 4.1 The six modules with no directives

A module with nothing to report publishes **no diagnostics at all** — not an empty list —
so the six directive-free modules first came back as "no diagnostics published", which is
not the same statement as "clean". They were re-run in a scratch copy of the whole subject
with a single `#EVAL TRUE` appended to each, purely to force a publish. All six returned
`errors 0` and the expected `TRUE`. That is a direct result for each of them, not an
inference from their dependents.

### 4.2 What the two `#EVAL`s in `agent-cases.l4` reduce to

Both reduce to a full `Offence Screen` record rather than erroring, which is the point of
having them:

```
line 348: `Offence Screen` OF TRUE, FALSE, TRUE, FALSE, … , TRUE
line 349: `Offence Screen` OF TRUE, TRUE, FALSE, FALSE, … , FALSE
```

## 5. Changes made to the repository by this run

**None by the machine run itself.** Every rule type-checked and every assertion held on the
first full run, before and after the fidelity work described below.

This matters for how the two kinds of defect are told apart. The twelve defects in
`registers/verification-register.md` and the four in
`registers/verification-register-pass-2.md` were **all** found by reading the statute, and
**none** of them by running the engine. A rule that says the wrong thing type-checks
perfectly. W1 in pass 2 is the sharpest illustration: the s 74B exclusion list shared a
boolean with ss 73 and 74A, which is well-formed L4 and a misreading of the Code.

The assertion count rose from 53 to 55 because pass 2 added a regression fixture
(`section 335A offence against a child below 14`) with two assertions, to hold W1 fixed.

## 6. What machine evaluation does not establish

It says the encoding is well-formed and self-consistent. It says nothing about whether it is
a faithful reading of the law.

Unchanged by this run:

- the sixteen interpretive choices in `NOTES.md` §3 — a passing assertion about s 38 or
  s 405 confirms only that the encoding does what the encoder intended, not that the
  intention is right;
- everything named in `NOTES.md` §2 as absent, above all **Chapter 4A** (private defence,
  ss 96 to 106): no assertion can fail for a rule that was never written, so the screen's
  known over-inclusiveness on defences survives a clean run untouched;
- the three freestanding modules (`chapter-2-definitions`, `chapter-2-participation`,
  `chapter-3-punishments`) are checked in isolation and their 22 assertions hold, but
  nothing in this subject calls them, so nothing here exercises them in combination with
  the offence tests;
- `status` stays `draft`, and no human gate has been granted. Assertions are not HG1.
