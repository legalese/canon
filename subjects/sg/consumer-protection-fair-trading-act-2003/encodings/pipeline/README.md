# The pipeline run on this encoding

Run `2026-09-30-0ee01ac6-006`, subject sidecar `sg-consumer-protection`, `--encoding primary`, `--fixed-now 2026-09-30T00:00:00Z`, `l4` `unstable-20260926-c76e6b0`.

**Verdict: `PROVISIONAL`.** The accounting is complete and the review is not: HG1 has no signer enrolled and no review on record, so the driver granted it provisionally. Nothing here is servable and nothing was published (P10 was not run; HG2 is a human's).

| stage | status | what it measured |
| --- | --- | --- |
| p0-preflight | PASS | the CLI surface the stages depend on; the three regulative rules were found by `l4 export bpmn` |
| p3-check | PASS | `l4 check` over all 15 modules |
| p6-tests | PASS | 626 assertions, 0 failed, 0 errors, per module as `check.sh` prints them |
| p8-verify | PASS | propositional consistency of the boolean decision skeleton: 5 controls reproduced, then 0 findings in 150 analysed decisions (148 in the seven rule modules: 16 + 15 + 44 + 21 + 26 + 14 + 12; 2 in a tests module); 306 further decisions skipped as non-boolean (16 in rule modules, 290 in tests modules). A clean run is a weak statement, and the receipt says so |
| p9-cost | PASS | |
| p9-report | PASS | `report-2026-09-30-0ee01ac6-006.md` beside this file; 7 of the 11 required sections render ABSENT with a stated reason |
| p9-explain | SKIPPED | the subject declares no `explainer` narrative |
| p7-* projections | **not declared** | no leg is declared in the sidecar, so no projection stage ran; see below |

## What the pipeline did not do

- **No projection legs.** A leg needs committed goldens and, for DMN, a cases file, none of which exists for this subject. The DMN and BPMN in `../projections/` were produced by running `l4 export` directly; they are **not** a pipeline artefact, carry no receipt, and were not executed on any engine. The DMN exports report 1 to 19 blocking findings per module (record-typed parameters, `REFUSE`, boxed literal expressions), listed in each `.fidelity.txt`. Read them as "emitted, not verified".
- **P1, P2, P4, P5 were not run.** They validate registers a depositor writes (source bundle, external-modification sweep, fork register, adversarial gate). This encoding has a source bundle stub, and its forks are in `NOTES.md` section 4, not in the pipeline's fork-register schema. P2 (what has happened to the text since it was printed: amendments after the PDF's date, court rulings) was not searched at all.
- **HG1 is provisional, not granted.** Nobody has signed.

## Reproducing the run: the driver does not run natively on Windows

The l4-ide driver (`etc/go/`) assumes a POSIX host. On this Windows machine (Git Bash, no WSL) it failed silently or with path errors until patched. Nothing in `legalese/l4-ide` was changed; the run used a **scratch copy** of `etc/`, `specs/todo/single-instruction-demo/`, `.claude/skills/` and `jl4/tests-cli/fixtures/`, with these edits to the copy only:

1. **15 `.mjs` files** guard their CLI with ``import.meta.url === `file://${process.argv[1]}` ``, which is never true on Windows (`file:///C:/...` against `C:\...`). Every `node etc/go/lib/*.mjs` command therefore did nothing and exited 0, and `go.sh` then died on an unbound `GO_S_ENCODING`. Replaced with ``import.meta.url === new URL(`file:///${process.argv[1].replace(/\/g, '/')}`).href``.
2. **`cost-ledger.mjs`** compares `new URL(import.meta.url).pathname` (`/C:/...`) with a resolved path; it exited 0 and wrote no ledger, so `p9-cost` was BROKEN. The leading slash before the drive letter is stripped.
3. **`go.sh` line 113**: `GO_ROOT` uses `pwd -W`, so Node sees `C:/...` rather than `/c/...`.
4. **Seven `import("...ledger.mjs")` sites** in `go.sh`, `phases/p7-tnr.sh` and `lib/phase-prelude.sh` are given a `file:///` prefix.
5. `jl4-core/libraries` is filled from the binary's own bundled `libraries/`, because the driver points `JL4_LIBRARY_PATH` at that directory.
6. `L4` and `TMPDIR` are set with `C:/` style paths.

These are worth fixing upstream in `legalese/l4-ide`. The sidecar used is in `sidecar/`; to register it, place it at `etc/go/subjects/sg-consumer-protection/` and vendor this encoding at `jl4/examples/canon/sg/consumer-protection-fair-trading-act-2003/encodings/`.
