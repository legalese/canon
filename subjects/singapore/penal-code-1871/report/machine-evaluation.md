# Penal Code 1871 — machine evaluation report

**Run date:** 2026-09-11 (first run 2026-09-09)
**Verdict:** **0 type errors across all 23 modules; 154 of 154 assertions satisfied.**
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

> **Retracted 11 Sep 2026.** This does not reproduce. A syntax error appended to `types.l4`
> is reported against `types.l4` and nothing else, and `agent-cases.l4` comes back clean.
> Do not rely on the conclusion in this paragraph: every module must be opened and checked
> in its own right. See §7.2.

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

## 4. Results — first run, 09 Sep 2026

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
- everything named in `NOTES.md` §2 as absent — no assertion can fail for a rule that was
  never written, so the screen's remaining over-inclusiveness on defences survives a clean
  run untouched. Chapter 4A was the largest instance of this until 11 Sep and is now
  encoded; **Chapter 16**, the whole of the offences affecting the human body, is now the
  largest;
- the three freestanding modules (`chapter-2-definitions`, `chapter-2-participation`,
  `chapter-3-punishments`) are checked in isolation and their 22 assertions hold, but
  nothing in this subject calls them, so nothing here exercises them in combination with
  the offence tests;
- `status` stays `draft`, and no human gate has been granted. Assertions are not HG1.


---

## 7. Second run — 11 Sep 2026

**Verdict: 18 modules, 0 type errors, 88 of 88 assertions satisfied.** 55 of those assertions
are the ones that existed before this pass, all still holding unchanged; 33 are new.

| module | errors | assertions satisfied |
| --- | ---: | --- |
| `types.l4` | 0 | — (declarations only) |
| `chapter-1-preliminary.l4` | 0 | — (no directives) |
| `chapter-2-definitions.l4` | 0 | 8 |
| `chapter-2-explanations.l4` | 0 | 4 |
| `chapter-2-participation.l4` | 0 | 5 |
| `chapter-3-punishments.l4` | 0 | 9 |
| `chapter-4-exceptions.l4` | 0 | — (no directives) |
| `chapter-4a-private-defence.l4` | 0 | — (no directives) |
| `chapter-5-abetment.l4` | 0 | — (no directives) |
| `chapter-5a-conspiracy.l4` | 0 | 4 |
| `chapter-17-cheating.l4` | 0 | 6 |
| `chapter-17-property.l4` | 0 | 2 |
| `chapter-17-fraud.l4` | 0 | 4 |
| `chapter-18-forgery.l4` | 0 | — (no directives) |
| `chapter-21-22-speech.l4` | 0 | 2 |
| `chapter-23-attempts.l4` | 0 | 2 |
| `agent-compliance.l4` | 0 | — (no directives) |
| `agent-cases.l4` | 0 | **42** |
| **total** | **0** | **88 of 88** |

The harness is the one described in §1, rebuilt from this description — the same
`jl4-lsp.exe`, the same patched library copy, the same one-process-per-file discipline. It
was revalidated before it was trusted: a deliberately false assertion (`1 PLUS 1 EQUALS 3`)
appended to `agent-cases.l4` was reported as `[ERROR] assertion failed`, and a bogus record
selector inserted into `chapter-4-exceptions.l4` was reported as "I could not find a
definition for the identifier".

Directive-free modules still publish nothing at all, so as in §4.1 each was run in a scratch
copy with a single `#EVAL TRUE` appended to force a publish. All eight returned `errors 0`
and `TRUE`.

### 7.1 The screen, end to end

The `#EVAL` added by this pass is the wiring test for Chapter 4A. On `disarming an assailant`
— a taking that satisfies every element of s 378, done by a person fending off an assault —
the screen reduces to:

```
`Offence Screen` OF TRUE, FALSE, TRUE, FALSE, FALSE, … , FALSE
                 │      │      │      │                   └ any screened offence indicated
                 │      │      │      └ another written law may still apply (s 5)
                 │      │      └ a private defence justification applies (s 96)
                 │      └ a general exception applies (Chapter 4)
                 └ Singapore has territorial reach
```

Territorial reach yes; no Chapter 4 exception; private defence yes; `theft s 378` FALSE. On
the same facts before this pass the screen returned theft.

### 7.2 Two blind spots in this engine that the run does not cover

§2.2 of this report recorded that an error injected into `types.l4` collapsed every assertion
in `agent-cases.l4`, and concluded that a clean run of the importing file was evidence about
the whole import graph beneath it. **That does not reproduce.** Re-probing it on 11 Sep:

1. **Dependency errors do not propagate to importers.** A syntax error appended to `types.l4`
   is reported against `types.l4` and against nothing else; `chapter-4-exceptions.l4` and
   `agent-cases.l4` both come back clean. Errors *within* an opened module are caught
   normally, including through a forced `#EVAL TRUE`. The practical consequence is that
   **every module must be opened and checked in its own right**, which is what the run above
   does — rather than relying on `agent-cases.l4` as a proxy. The §2.2 conclusion should not
   be relied on.

2. **A record literal that omits a declared field is not flagged.** Adding a field to a
   `DECLARE ... HAS` without updating the `X MEANS T WITH` fixtures produces no error and no
   failing assertion. Since record construction appears to be positional, a fixture whose
   fields are in a different order from the declaration is a silent wrong answer rather than
   an error.

   Blind spot 2 is not something the engine can be made to catch here, so it is covered by a
   separate check written for this pass: for every `X MEANS T WITH` block in the subject,
   compare the fields set against the fields `T` declares, in order, and fail on any
   difference. It found all five fixtures that this pass put out of step, and it detects a
   deliberate reordering. Like the batch checker, it is not committed here; it is about 100
   lines and belongs in `l4-ide`.

Neither blind spot affects the verdict above, because the run opens and checks all eighteen
modules individually and the fixture check passes on all of them. Both affect how a *future*
run should be read.


---

## 8. Third run — 11 Sep 2026, after the Chapter 16 pass

**Verdict: 21 modules, 0 type errors, 133 of 133 assertions satisfied.** 88 of those are the
assertions that existed after the Chapter 4A pass, all still holding; 45 are new.

The three new modules -- `chapter-16-life.l4`, `chapter-16-hurt.l4` and
`chapter-16-restraint-and-force.l4` -- carry no directives of their own and were run in a
scratch copy with `#EVAL TRUE` appended, as in §4.1. All three returned `errors 0` and `TRUE`.
All 45 new assertions live in `agent-cases.l4`, which now carries 87.

The fixture-completeness check described in §7.2 was run after every change to `types.l4` in
this pass. It caught all four `Proposed Act` fixtures when `homicide`, `bodily harm` and
`personal liberty` were added, which is precisely the blind spot it exists for: the engine
reported those same fixtures as clean.

### 8.1 A third trap, in the coverage tooling rather than the engine

`missing-sections.md` §4 already warned that a citation like `s 28 Explanation 2` must have
its "Explanation N" tail stripped or the 2 reads as a section number. Chapter 16 brought the
same trap in a new form: `s 300 Exception 1`, and `s 300 Exceptions 1 to 7`. Before it was
caught it inflated Chapter 1 to 7 of 7 and Chapter 2 to 50 of 54 -- both wrong, and both
wrong in the flattering direction. The stripping rule now covers `Explanation`, `Exception`
and their plurals, with or without a `to` range.

This is the second time the same class of bug has produced a wrong coverage count. Any future
regeneration should treat a coverage number that *improves* without new rules as a defect in
the tooling until proved otherwise.


---

## 9. Fourth run — 11 Sep 2026, after the second Chapter 16 pass

**Verdict: 23 modules, 0 type errors, 154 of 154 assertions satisfied.** 133 of those are the
assertions that existed after the first Chapter 16 pass, all still holding; 21 are new.

The two new modules -- `chapter-16-unborn-and-infants.l4` and `chapter-16-kidnapping.l4` --
carry no directives of their own and were run with `#EVAL TRUE` appended, as in §4.1. Both
returned `errors 0` and `TRUE`. All 21 new assertions live in `agent-cases.l4`, which now
carries 108.

### 9.1 The harness needed a longer settle time, and said so misleadingly

`agent-cases.l4` is now about 3,500 lines and its first run at the old timeout returned
**"NO DIAGNOSTICS PUBLISHED"** -- which the harness treats as a failure, and which looks
exactly like a module that cannot be parsed. It was neither: the server had simply not
finished within the 180-second hard limit. Re-run with a 540-second limit and an 8-second
settle, the same file returned `errors 0, satisfied 108`.

Worth recording because the failure mode is silent and misleading in the *safe* direction
only by luck. A reader who saw that line and concluded the file was broken would have been
wrong; a reader who ignored it would have missed a real parse failure on another day. The
harness distinguishes "no diagnostics" from "clean" and exits non-zero on it, which is the
right default -- but the timeout must scale with the file.
