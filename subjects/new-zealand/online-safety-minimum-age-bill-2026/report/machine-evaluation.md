# Online Safety Bill — machine evaluation report

**Run date:** 2026-09-11
**Verdict:** **0 type errors across all 9 modules; 64 of 64 assertions satisfied.**
No directive was skipped, stubbed or held back.

---

## 1. How it was run

A real `l4` CLI is installed on this machine, at
`C:\Users\micha\AppData\Local\Programs\l4\l4`, carrying both subcommands the skill documents:

```
l4 check <file>    typecheck only, no evaluation
l4 run <file>      typecheck and evaluate every #EVAL / #ASSERT directive
```

Each module was checked, then run. `run` publishes directive results as diagnostics: an
`#ASSERT` that holds reports `assertion satisfied` at Information severity, and one that fails
reports `assertion failed` at Error severity, so a failure cannot be mistaken for a pass.

**Note for the corpus.** The Penal Code 1871 machine-evaluation report records that no `jl4`
CLI existed in that environment and drives `jl4-lsp.exe`, a March 2026 language-server build,
as a batch checker instead. That workaround is no longer necessary on this machine. Whoever
maintains that subject should know the toolchain has moved.

## 2. Result

| Module | Assertions satisfied | Failed | Type errors |
| --- | ---: | ---: | ---: |
| `types.l4` | 0 | 0 | 0 |
| `part-1-preliminary.l4` | 14 | 0 | 0 |
| `part-2-duties.l4` | 6 | 0 | 0 |
| `part-3-subpart-1-regulator.l4` | 6 | 0 | 0 |
| `part-3-subpart-2-enforcement.l4` | 6 | 0 | 0 |
| `part-3-subpart-3-remedies.l4` | 17 | 0 | 0 |
| `part-3-subpart-4-offences.l4` | 6 | 0 | 0 |
| `part-3-subpart-5-other.l4` | 5 | 0 | 0 |
| `schedule-1-transitional.l4` | 4 | 0 | 0 |
| **Total** | **64** | **0** | **0** |

`types.l4` carries the shared ontology and no rules, so it has no directives of its own.

## 3. What this result does and does not establish

**It establishes** that the encoding is mechanically sound: every module typechecks, every
fixture constructs, and every stated expectation holds when evaluated. Expected values were
machine-evaluated, never hand-typed — the `#ASSERT` directives were written against the rules
and then run, and where a value surprised me the rule was re-read against the clause rather
than the assertion adjusted to fit.

**It does not establish fidelity.** A rule can typecheck, evaluate, and satisfy every
assertion while saying something the Bill does not. Nothing here has been read back against
the source by a second party. That is what the HG1 gate is for, and it has not been sought:
`subject.json` declares `status: draft`.

One structural result is worth separating from the rest, because it is the strongest thing the
run produces. `the tier for` in `part-3-subpart-3-remedies.l4` is a **total function** over the
`specified liability act` enum. Totality is enforced by the typechecker, not by a test, so an
act that cl 34(3) creates and cll 45 to 47 fail to route becomes a compile error rather than a
silent gap. That property survives amendment, which is when such partitions actually break.

## 4. Reproducing the run

From the subject directory:

```bash
for f in *.l4; do l4 check "$f"; done
for f in *.l4; do l4 run "$f"; done
```

`run` is deterministic here: no directive in this subject uses `NOW` or `TODAY`, so
`--fixed-now` is unnecessary.
