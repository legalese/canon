# FinMont-demo — machine evaluation report

**Run date:** 2026-09-09
**Verdict:** 0 type errors across all 8 modules; **80 of 82 assertions satisfied**, 2 not
runnable on the available engine. One genuine defect found and fixed.

This supersedes the "nothing has been machine-evaluated" statement in earlier revisions of
`report/conversion-report.md` §6.

---

## 1. How it was run

No `jl4` CLI exists in this environment — no Haskell toolchain, no Docker, and the tree
carries only `jl4-lsp.exe` (from `thailand-cosmetics/tmp-vsix/`, a VS Code extension build
dated **March 2026**). The `jl4-core.wasm` next to it is a GHC WASM build whose `.mjs` is
only the JSFFI shim, with no evaluation entry point wired up.

So the language server was driven directly as a batch checker. This works because
`jl4-core/src/L4/Diagnostic.hs` publishes directive results as LSP diagnostics:

| directive result | severity |
| --- | --- |
| assertion holds | Information — "assertion satisfied" |
| assertion fails / errors | **Error** — "assertion failed" |
| `REFUSE`d assertion | Warning |
| `#EVAL` reduction | Information — the value |

The harness is ~150 lines of Node: spawn `jl4-lsp.exe`, LSP `initialize` with the subject
directory as `rootUri`, `textDocument/didOpen` one file, collect
`textDocument/publishDiagnostics`, classify by severity, exit non-zero on any Error. Files
are opened **one per server process** — the server sets a single "file of interest" and
does not reliably publish for the others.

It is not committed here. This repository holds law; `l4-ide` holds tools, and a batch
checker belongs there (or, better, is made unnecessary by shipping the `l4` CLI). It is
reproducible from this description in well under an hour.

## 2. The harness was validated before it was trusted

Run first against a known-good corpus file, `canon/Companies_Act/sg-companies-part9.l4`:
0 errors and exactly 7 "assertion satisfied", matching that file's 7 `#ASSERT` lines. The
harness genuinely evaluates; it is not reporting silence as success.

## 3. Two compensations for a stale engine, and exactly what they cost

The available binary predates the `jl4-core` worktree beside it. Two gaps had to be worked
around **in throwaway scratch copies — no file in this repository was modified for the
run**, other than the genuine fix in §5.

### 3.1 `prelude.l4` does not parse under this binary

The current `prelude.l4` uses `@nonexhaustive` (line 127) and `@infixl` (line 1235), and
`daydate.l4` and `prelude.l4` both use `REFUSE` — all newer than the binary's parser. The
parse failed at the first of these, so **the entire prelude was silently empty** and every
use of `count`, `null`, `min`, `filter` and `elem` reported "could not find a definition".

That looked exactly like an encoding defect and was not one. Confirmed by a four-line probe
importing only `prelude` and calling `count`, which failed identically.

Worked around by copying the libraries to scratch, stripping the three unknown annotations,
and stubbing the two `REFUSE` sites (`TBD` in `prelude`, the out-of-range guard in
`YMD`). Neither is used by this encoding. After that, `count [1,2,3]` = 3, `null` = FALSE,
`min 3 5` = 3, `elem 2 [1,2,3]` = TRUE — the prelude works, and every prelude-dependent
error in this subject disappeared.

**Cost to confidence: none.** This restores the library to what the current engine would
provide; it does not relax anything about the encoding under test.

### 3.2 `RULES EFFECTIVE DATE` postdates this binary

`chapter-vi-final-provisions.l4` reported `RULES EFFECTIVE DATE` undefined, and the cases
file reported `EVAL UNDER RULES EFFECTIVE AT` "expected to be of type NUMBER but is here of
type DATE".

**This is the engine, not the encoding.** The official l4-ide tutorial for the feature —
`l4-ide/doc/tutorials/multi-temporal-modeling/gst-rate-change-example.l4` — fails on this
binary in precisely the same way, on both counts. The law-time axis was rebuilt from
`NUMBER` to `DATE` after this binary was cut.

Worked around by stubbing `the SCA-RTS is in application` and
`the article 30(3) and (5) obligations are in application` to `TRUE` in the scratch copy,
and neutralising Case 15's two `#EVAL` and two `#ASSERT` directives.

**Cost to confidence: this is the real limit of the run.** Unverified as a result:

- the two dated-arm definitions in `chapter-vi-final-provisions.l4`;
- Case 15's two law-time assertions (that Case 1 is out of scope under the rules effective
  1 June 2019, and exempt under those effective 9 September 2026).

Everything else was evaluated with the gate open, which is the correct setting for a
present-day assessment and is what all 15 other cases assume.

**Re-run these four directives first on a current engine.** They are the only part of this
subject with no machine evidence behind it.

## 4. Results

| module | errors | assertions satisfied |
| --- | --- | --- |
| `types.l4` | 0 | — (declarations only) |
| `chapter-i-general-provisions.l4` | 0 | 3 |
| `chapter-ii-authentication.l4` | 0 | 4 |
| `chapter-iii-exemptions.l4` | 0 | 17 |
| `chapter-vi-final-provisions.l4` | 0 | — (see §3.2) |
| `psd2-refunds-and-liability.l4` | 0 | 6 |
| `finmont-sca-orchestration.l4` | 0 | — (no directives) |
| `cases/finmont-travel-cases.l4` | 0 | 50 |
| **total** | **0** | **80 of 82** |

The 50 in the cases file are 15 of the 17 scenarios in full; Case 15 is the law-time one
held back by §3.2.

Worth singling out, because they were computed rather than asserted from memory:

- **the Annex band arithmetic** — all 15 band-and-reference-rate assertions in
  `chapter-iii-exemptions.l4` hold, including that EUR 500.01 falls into no band at all;
- **the business-day arithmetic** in `psd2-refunds-and-liability.l4` — the Art 73(1) D+1
  deadline correctly skips a weekend (Friday 11 Sep 2026 → Monday 14 Sep), and 10 business
  days from Wednesday 9 Sep lands on Wednesday 23 Sep;
- **the Art 71 and Art 77 windows** — 13 months from 9 Sep 2026 = 9 Oct 2027; 8 weeks from
  3 Aug 2026 = 28 Sep 2026;
- **Case 12 and Case 13** — the same EUR 480 transaction is exempt through a 0.008 %
  acquirer, not exempt through a 0.09 % one, and not exempt through one in an Art 20
  cessation. The provider-dependence of Art 18 behaves as `NOTES.md` §8 claims.

## 5. The one genuine defect, found and fixed

**A `#ASSERT` expression may not break across lines at the top level.** It may only
continue while a bracket is open. Four assertions in `cases/finmont-travel-cases.l4` were
written as

```
#ASSERT `who bears the loss` `case 16 claim`
            EQUALS `the payee or the payment service provider of the payee bears the loss`
```

which is a **parse error** — `unexpected EQUALS expecting ... end of input`. A parse error
kills the whole module, so this single mistake was suppressing all 52 assertions in the
cases file.

Isolated with a purpose-built probe testing four layout forms. Fixed by wrapping the whole
comparison in one paren pair:

```
#ASSERT (`who bears the loss` `case 16 claim`
            EQUALS `the payee or the payment service provider of the payee bears the loss`)
```

Four sites, all in the cases file. This is the only change this run made to the repository.

Note the near-miss: with the prelude broken (§3.1) and the temporal gate broken (§3.2), the
first full run reported **18 failing assertions**. All 18 were cascade. Had they been taken
at face value, the "fixes" would have damaged correct code. Every failure was traced to a
root cause before anything was changed.

## 6. What machine evaluation does not establish

It says the encoding is well-formed and self-consistent. It says nothing about whether it
is a faithful reading of the law.

Unchanged by this run:

- the 45 `UNVERIFIED` markers on Directive-sourced rules — no source text was deposited, so
  no assertion can test fidelity (`NOTES.md` §3);
- the ten interpretive choices in `registers/ambiguity-register.md`, **AR-07** above all:
  a passing assertion about one-leg-out only confirms the encoding does what the encoder
  intended, not that the intention is right;
- `status` stays `draft`, and no human gate has been granted. Assertions are not HG1.
