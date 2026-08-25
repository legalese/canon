
# Conversion report — sg-child-support (primary)

|             |                                                                                  |
| ----------- | -------------------------------------------------------------------------------- |
| run id      | `2026-08-25-36663f00-001`                                                                     |
| encoding    | primary — the committed encoding, replayed. It is driven through every reachable projection; nothing is encoded from source.                                        |
| subject     | sg-child-support                                                                  |
| repo HEAD   | `ebb1977c51e9e0b298898c92e0e2a262ca219b18` (dirty)                                         |
| clock       | `2025-01-31T00:00:00Z`                                                              |
| `l4` binary | `/Users/mengwong/src/legalese/l4wt/sg-family-gia/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4`                                                              |
| journal     | `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-08-25-36663f00-001/journal.ndjson` — 22 records, chain verifies |
| verdict     | **COMPLETE**                                                              |

> COMPLETE means every declared stage has a receipt, no receipt is BROKEN, every non-PASS receipt carries a reason that appears below, and every gate is signed or explicitly waived. It is completeness of accounting, NOT greenness: legs below may report NOT-EXECUTABLE, DEGRADED or NOT-REGENERATED, and each says why.

---

## Gates

| gate | state | how |
| --- | --- | --- |
| HG1 | waived | **waived**: The encoding is two days old and states an ANNOUNCEMENT, not law: no Bill exists for a domain expert to review it against, and the administrative pages it encodes may still change before implementation. The isomorphism claim HG1 certifies is therefore not yet available to be made, and saying so is more honest than collecting a signature over a moving target. Re-open this gate when a Bill is introduced. |

---

## What the source said

**ABSENT.** SPEC.md §P1 requires the source bundle with provenance — the retrieval of each source document, its integrity digest or immutable capture, the publisher's in-force statement, and the citation of the instrument and of each amendment. No stage in this run wrote it; `p1-ingest` is not declared for this run: the corpus is REPLAYED, not re-derived from source, so no ingest happened and none is claimed. (The stage itself no longer refuses — on the deposit path it validates a deposited source bundle — but a bundle is not what this run read.)

What this run did read, and its exact content:

| file | sha256 |
| --- | --- |
| `jl4/examples/legal/sg-child-support/sg-child-support-domain.l4` | `sha256:0a1fed48f13c10e775262694cda3f1d67a0cf0da93aaea07bc34afdc11c50f85` |
| `jl4/examples/legal/sg-child-support/sg-csp.l4` | `sha256:5a951dff22f5db3c7bf76bd3fd77e5d69048c19e6a85d16c55c658a62beddf1c` |
| `jl4/examples/legal/sg-child-support/sg-childcare-leave.l4` | `sha256:03b52f5a9aebab8a04c22d0d6fc0e1a57e541f486f62c499ac29b0fee11ab07c` |
| `jl4/examples/legal/sg-child-support/sg-csp-openfisca.l4` | `sha256:76038acb8d9e384e7171820cc47c9c5894845d60491256f3ef118a6a8be966ec` |
| `jl4/examples/legal/sg-child-support/sg-child-support.l4` | `sha256:d0baeac3252903f37623fee328b2a68376be45d742c1595af9938e3b1b5f9e05` |
| `jl4/examples/legal/sg-child-support/sg-child-support-cases.l4` | `sha256:e9c18bdd49bd7e0a21d38bc496ae69e108a4edc00e56344c621ff24d8a6c428b` |

---

## What the external-modification sweep searched and surfaced

**ABSENT.** SPEC.md §P2 requires the external-modification register, and requires this report to state what was SEARCHED, not only what was found — "no modification found" is a checked claim, not a default. No stage in this run wrote it; `p2-sweep` is not declared for this run. Nothing was searched, so nothing may be reported as searched, and this report makes no claim that the encoding is current with respect to courts striking or reading down a provision, the regulator's interpretive guidance, or instruments in flight. (On the deposit path the stage validates a deposited register — but note that validating a register is not performing a sweep: no procedure enumerates the searches that should have run.)

---

## What the encoding decided

**ABSENT.** SPEC.md §P3/§P4 require what the encoding decided, including every ambiguity fork and every externally-settled resolution. No stage in this run wrote it; `p3-encode`, `p4-forks` and `p5-gate` are not declared for this run — they validate de novo deposits, and this run replayed the committed encoding — so this run made no encoding decisions and opened no forks. The encoding it exercised is the committed corpus.

**What was checked about the committed encoding:** PASS — 

Oracle (`structural`): `l4 check sg-child-support-domain.l4 && l4 check sg-csp.l4 && l4 check sg-childcare-leave.l4 && l4 check sg-csp-openfisca.l4 && l4 check sg-child-support.l4 && l4 check sg-child-support-cases.l4 && no ELSE IF chain && temporal closure NOT CHECKED (0 matched arms, floor 0 — see note)`

typechecking is the compiler's own verdict on the module; the two grep checks are the mechanisable half of P3's house rules, and the dated-arm floor stops the second one passing over an empty matched set (a 0 floor demotes that sub-check to NOT CHECKED on the receipt rather than passing it). Faithfulness to the source regulation is NOT covered and is carried by HG1.

> *claimed, not verified* (phase-script): temporal closure NOT CHECKED (does not affect status): 0 dated arms matched and the pinned floor for this encoding (checks.min_dated_arms) is 0, so the @ref-per-dated-arm rule had nothing to hold — a vacuous pass refused, not a green earned; see the sidecar's NOTES.md for the population census

> *claimed, not verified* (phase-script): isomorphism against SG Child Support Package and childcare leave (National Day Rally 2026); Child Development Co-Savings Act 2001 is unverified by this stage and is HG1's subject

---

## What each projection preserved and lost

| leg | status | oracle class | what it says |
| --- | --- | --- | --- |
| `p7-lts` | NOT-BUILT | replayed | l4 state-graph exited 1; it exits 1 with 'No regulative rules found in module' when a module has none |
| `p7-mcp` | SKIPPED | none | JL4_GO_SERVICE_URL is unset, so no jl4-service was contacted and no deployment was made. The deployable zip was still built and hashed. Set JL4_GO_SERVICE_URL to a LOOPBACK service (./dev-start.sh brings one up on 8080) to exercise the deployment half. |
| `p7-akn` | UNVERIFIED (EXTRA) | replayed | an Akoma Ntoso 3.0 document was emitted and is well formed at the shallow level checked here (declaration, AKN namespace, one balanced root). It is UNVERIFIED because well-formedness is the only oracle available: this repo carries no AKN schema and no AKN checker, so nothing establishes that the document is schema-valid, let alone that it says what SG Child Support Package and childcare leave (National Day Rally 2026); Child Development Co-Savings Act 2001 says. etc/go/lib/verdict.mjs bars a wellformedness-class oracle from PASS for exactly this reason. |

### `p7-lts` — NOT-BUILT

l4 state-graph exited 1; it exits 1 with 'No regulative rules found in module' when a module has none

**Blocker.** No regulative rules found in module

**Oracle:** none in this receipt — see the replay note below, which names the receipt whose oracle did run.

*Replayed across runs* from receipt `sha256:a6e3177edc273b2f976007b715fb6bcd4d106969ec86789bbf576f967d59adee`, earned in run `2026-08-25-ff0db4d5-001` — the declared inputs were byte-identical, so the oracle did not run again. That run's artifacts were COPIED into this one, so every hash below is checkable from this run directory alone.

### `p7-mcp` — SKIPPED

JL4_GO_SERVICE_URL is unset, so no jl4-service was contacted and no deployment was made. The deployable zip was still built and hashed. Set JL4_GO_SERVICE_URL to a LOOPBACK service (./dev-start.sh brings one up on 8080) to exercise the deployment half.

**Oracle:** none ran.

### `p7-akn` — UNVERIFIED (EXTRA)

an Akoma Ntoso 3.0 document was emitted and is well formed at the shallow level checked here (declaration, AKN namespace, one balanced root). It is UNVERIFIED because well-formedness is the only oracle available: this repo carries no AKN schema and no AKN checker, so nothing establishes that the document is schema-valid, let alone that it says what SG Child Support Package and childcare leave (National Day Rally 2026); Child Development Co-Savings Act 2001 says. etc/go/lib/verdict.mjs bars a wellformedness-class oracle from PASS for exactly this reason.

**Oracle:** none in this receipt — see the replay note below, which names the receipt whose oracle did run.

`bytes=41169`

> *claimed, not verified* (phase-script): EXTRA leg. render --format akn is UNDOCUMENTED (its own command description lists only html|text|json|plan) and appears in no P7 projection table. Surfaced here because a demo arguing 'cooperate with the standards' should not be sitting on an unlisted LegalDocML output.

*Replayed across runs* from receipt `sha256:f9349fb8f4df81267d22413a0cbc572c9d7e196d8e6aaa5221dbfda7c9b3a493`, earned in run `2026-08-25-ff0db4d5-001` — the declared inputs were byte-identical, so the oracle did not run again. That run's artifacts were COPIED into this one, so every hash below is checkable from this run directory alone.


---

## Test results

**PASS**

Oracle (`execution`): `node etc/go/lib/assert-report.mjs sg-child-support-domain.run.json sg-csp.run.json sg-childcare-leave.run.json sg-csp-openfisca.run.json sg-child-support.run.json sg-child-support-cases.run.json `

the module's own #ASSERT directives were evaluated by the L4 evaluator and every result[] entry of kind 'assertion' is true with no entries of kind 'error'. The process exit code and the envelope's 'ok' field are BOTH ignored: measured, a failing #ASSERT yields ok:true and exit 0.

`assertions_total=79` · `encoding_id=primary`

> *claimed, not verified* (phase-script): these are the committed encoding's own assertions, already in the tree before this run: a run about the committed encoding does no encoding, so none of them were written to discriminate between the fork register's readings

---

## Every other stage that reported

The stages above are narrated under the heading they belong to. These are the rest — reporting stages, and anything added to the pipeline that has no heading of its own yet. They are here because the verdict gloss at the top of this report promises that every non-PASS receipt's reason appears below, and a stage with no site is how that promise quietly stops being true.

**`p8-verify`:** PASS

Oracle (`structural`): `l4 verify <module> --format json  (x6), plus 5 control fixtures with declared verdicts`

the oracle is not 'the corpus came back clean' — a checker that cannot go red reports every corpus clean, so that would be a presence check wearing a stronger word. It is that the same binary, in the same run, reproduced the declared verdict of all 5 control fixtures: one clean module reporting zero findings, and one module per finding family (unsat, dead-branch, vacuous-guard, unreachable-outcome) each reporting exactly the family it is named for and exiting 1. Only then is 'zero findings over 5 analysed decisions' evidence of anything.

`encoding_id=primary` · `sg-child-support-domain.decisions=5` · `sg-child-support-domain.analysed=1` · `sg-child-support-domain.skipped=4` · `sg-child-support-domain.nested_not_visited=2` · `sg-child-support-domain.findings=0` · `sg-csp.decisions=39` · `sg-csp.analysed=1` · `sg-csp.skipped=38` · `sg-csp.nested_not_visited=10` · `sg-csp.findings=0` · `sg-childcare-leave.decisions=20` · `sg-childcare-leave.analysed=3` · `sg-childcare-leave.skipped=17` · `sg-childcare-leave.nested_not_visited=4` · `sg-childcare-leave.findings=0` · `sg-csp-openfisca.decisions=11` · `sg-csp-openfisca.analysed=0` · `sg-csp-openfisca.skipped=11` · `sg-csp-openfisca.nested_not_visited=0` · `sg-csp-openfisca.findings=0` · `sg-child-support.decisions=7` · `sg-child-support.analysed=0` · `sg-child-support.skipped=7` · `sg-child-support.nested_not_visited=17` · `sg-child-support.findings=0` · `sg-child-support-cases.decisions=25` · `sg-child-support-cases.analysed=0` · `sg-child-support-cases.skipped=25` · `sg-child-support-cases.nested_not_visited=0` · `sg-child-support-cases.findings=0` · `controls_reproduced=5/5` · `decisions=107` · `analysed=5` · `skipped_non_boolean=102` · `nested_not_visited=33` · `findings=0` · `merged_atom_occurrences=0`

> *claimed, not verified* (phase-script): A clean run is a WEAK statement and the receipt refuses to imply otherwise. The analysis is propositional: every leaf (a projection, a comparison, an arithmetic test, a call to another DECIDE) is an opaque atom, so no numeric, interval, date or string contradiction is in range, and neither is anything that only appears once two named rules are unfolded against each other. Each DECIDE is read on its own. Findings are sound; silence is not a consistency proof. Full statement: l4 verify --help.

> *claimed, not verified* (phase-script): Rung 1 of 3. R5 (2026-08-02) ordered the P8 ladder as ROBDD first, the R4 fork-space agreement/divergence sweep second, an external model checker (TLA+/NuSMV/UPPAAL class) last. Rungs 2 and 3 are unbuilt: rung 2 needs the fork register P4 does not yet produce, rung 3 waits on the LTS semantics. 102 of 107 decisions are outside rung 1 entirely because they do not return BOOLEAN — they are counted, named in the artifact, and not reported as clean. A further 33 are outside it for a different reason: they are defined inside a WHERE clause, and neither this command nor the ladder's own entry point descends into one, so they are in NEITHER the analysed nor the skipped column. That is why the figure is on the receipt: 'analysed + skipped' does not total the corpus, and an exclusion nobody can size is an exclusion nobody believes.

**`p9-explain`:** SKIPPED — subject 'sg-child-support' declares no 'explainer' section in subject.json, so it has no checked-in narrative to render. Declaring the directory is deliberate rather than discovered: a mistyped directory name would otherwise yield a fully-absent document with no error anywhere.

**`p9-report`:** PASS

Oracle (`structural`): `node etc/go/report/render-report.mjs $RUN --format md,html && every section SPEC.md §P9 requires is present`

the renderer reads journal.ndjson and nothing else, refuses a template containing a typed number, refuses an unresolved placeholder, and prints a chain-verification failure in the report itself; the section-presence check then confirms nothing §P9 requires was dropped

> *claimed, not verified* (phase-script): PASS here means the report accounts for everything the journal holds. It says nothing about whether the projections it describes are good.

> *claimed, not verified* (phase-script): this is the PRELIMINARY render, taken before this stage's own receipt and the run_end record exist. go.sh renders the final $RUN/report.md after run_end; it is derived rather than attested, and re-derivable by anyone with 'go.sh verify'.


---

## Where another system published its own representation of the same rule

**ABSENT.** SPEC.md §P9 requires a factual note of disagreement wherever another system has published its own representation of the same rule. No stage in this run wrote it; no stage in this run reads another system's representation. Making that comparison is R2's read-only probe, and any contact is HG2's subject.

---

## Triage

**ABSENT.** SPEC.md §8's triage table classifies each disagreement between the de novo encoding and the committed corpus as encoding error / genuine ambiguity / improvement over the hand corpus. No stage in this run wrote it; `p8-diff` — the stage that runs the diff oracle (`etc/go/lib/denovo-diff.mjs`) over the subject's declared surface map — has no receipt in this run. It is declared on the deposit path; a run about the committed encoding replays one encoding and compares nothing.

---

## What this run cost

**Attested — measured by the driver.** It started each clock and stopped it; `go.sh verify` refuses any row claiming more than a second more time than the interval between its own `stage_begin` and `stage_end` — a second of slack, because the clock falls back to whole seconds on a shell without `EPOCHREALTIME`.

| stage | status | ran for | dispatch | |
| ----- | ------ | ------: | -------: | - |
| `p0-preflight` | PASS | 8s | 371 ms |  |
| `p3-check` | PASS | 14s | 395 ms |  |
| `p6-tests` | PASS | 19s | 440 ms |  |
| `p8-verify` | PASS | 27s | 489 ms |  |
| `p7-lts` | NOT-BUILT | 1s | — | replayed |
| `p7-mcp` | SKIPPED | 65 ms | 533 ms |  |
| `p7-akn` | UNVERIFIED | 1s | — | replayed |
| `p9-cost` | PASS | 553 ms | 218 ms |  |
| `p9-report` | PASS | 222 ms | 276 ms |  |
| `p9-explain` | SKIPPED | 20 ms | 205 ms |  |
| **total** | | **1m 14s** | **2s** | |

`dispatch` is the driver's own time before each stage started — asking the stage for its inputs, digesting and itemising them, and searching for a replayable receipt. It is spent on every stage, including the ones that then replay in milliseconds, and on an EXECUTED stage it is listed separately rather than folded in, because it is the harness's cost and not the stage's work.

**A replayed row's number is not the same measurement as the rest of the column.** 2 stage(s) replayed an earlier receipt rather than executing, costing 3s between them. Two things follow, and neither is visible from the table alone. First, that figure is what the REPLAY cost — declaring inputs, digesting them, finding the receipt and materialising its artifacts — not what the work costs; the work was done, and timed, in the run the receipt came from. Second, the driver has nowhere to put a separate dispatch figure for a row it writes itself, so on these rows dispatch is INSIDE the "ran for" number and the dispatch cell is blank. The dispatch total below therefore omits their dispatch and the "ran for" total contains it — which matters most in the replay-heavy runs where harness overhead dominates. A replay also writes no `stage_begin`, so it has no interval and contributes nothing to any wall-clock union.


**Attributed — what the agent sessions spent.** Read out of the harness's own JSONL transcripts, 1 of them, each named in `cost-ledger.json` with its sha256 so a second party can repeat the derivation. Nobody typed these numbers; the transcript is nonetheless an ordinary file, which is why they are attributed rather than attested.

| | in this run's window | across the whole session |
| --- | ---: | ---: |
| API requests | 0 | 150 |
| output tokens | 0 | 194,563 |
| of which reasoning | 0 | |
| input tokens | 0 | |
| cache writes | 0 | |
| cache reads | 0 | |
| tool calls | 0 | 167 |

The right-hand column is an upper bound, not a second measurement: it is everything the session did, including whatever else it was asked to do. The left column clips to this run's own window, from its first journal record to its last.

Both columns are attributions **by clock**, and a clock cannot tell work on this run apart from work that merely happened at the same time. So the left column misses what came before the driver was first invoked — reading the source, deciding what to encode — and includes anything else the session did between the first record and the last, which on a human-gated pipeline can be days. It understates at one end and overstates at the other; the honest reading is that the true figure lies between the two columns, nearer the left.

Model(s): `claude-opus-5`. Across the whole session — the right-hand column, not the left — 0 requests were made by subagents, spending 0 output tokens across 0 workflow fan-out(s). Those are measured from the subagents' own transcripts, which the session file does not contain at all: a ledger that read only the session file would report a fraction and look complete.

**Network, model-initiated.** In this run's window — the left-hand column above, not the right — 0 web search(es), 0 fetch(es) and 0 external-service call(s), taking 0 ms between them. Across the whole session: 6 web search(es).

That counts calls the MODEL made, by tool name. A stage that runs `curl` reaches the network inside a shell call and is invisible to it, so the pipeline's own retrievals are counted separately, by the stage that makes them:

> This run declared no `p1-ingest` stage, so there is no source-side figure. On the committed-encoding path the sources were fetched in an earlier run; on the deposit path `p1-ingest` validates the bundle that records them.

**Wall clock.** The run spans 1m 18s from its first journal record to its last. Of that, 1m 10s is attested stage execution (over the stages that actually EXECUTED, which is why it can sit far below the "ran for" total above when most stages replayed), and at least 0 ms is measured tool-call time, giving a floor of 1m 10s during which something was demonstrably running. Both component figures stop where the attributed ones do; the span does not.

The gap between the span and that floor is mostly not idleness in the ordinary sense: this pipeline stops at a human gate and waits. The floor is a floor and not an estimate — it unions attested stage brackets with measured tool intervals, and counts nothing at all for the time a model spends reasoning between two tool calls, which is real work that leaves no interval to measure.

**No money.** Token counts are facts about this run; prices are facts about a contract and change without notice. A stale rate table would put a confident wrong figure in a report whose whole premise is that every number has a row behind it. A reader with a rate card can multiply.

The attributed figures stop at `p7-akn` — the last stage that had written a receipt when `p9-cost` read the journal. `p9-cost` runs before the reporting stages so that this section can exist, so it cannot count itself, `p9-report` or `p9-explain`. The per-stage table above is rendered after `run_end` and does see them, which is why the two totals differ by exactly the stages between them.

One further boundary: 1 of the transcripts read is the session that did the reading, so its own figures stop at the moment it measured itself. Two reads of a live transcript minutes apart differ by exactly the calls that did the reading.

> *claimed, not verified* (phase-script): The stage timings are ATTESTED — measured by the driver, and ledger.verify refuses any elapsed_ms more than a second longer than the bracket its own row sits in (the second of slack is for the whole-second clock fallback in lib/clock.sh). The token and tool figures are ATTRIBUTED: read from the harness's transcripts, which are named with their sha256 so the derivation can be repeated, but which are ordinary files. Figures stop at this stage; p9-report and p9-explain run after it. What each figure covers, and what it cannot, is stated in the report section that renders them, so it is written once.

---

## Every artifact this run put on disk

| stage | artifact | bytes (recorded) | sha256 (recorded) | state now |
| --- | --- | --- | --- | --- |
| `p0-preflight` | `probes.json` | 1742 | `sha256:cf7ec6f79d91c3ad…` | on disk |
| `p0-preflight` | `cli-surface.txt` | 81 | `sha256:e20fc97289bb520e…` | on disk |
| `p0-preflight` | `tripwire.json` | 519 | `sha256:fd9c2a98bc456d22…` | on disk |
| `p3-check` | `p3-check.txt` | 1374 | `sha256:c660188a39469c91…` | on disk |
| `p6-tests` | `p6-assertions.txt` | 948 | `sha256:52ee66e2643be4b9…` | on disk |
| `p6-tests` | `sg-child-support-domain.run.json` | 165 | `sha256:8114b934b288d4ed…` | on disk |
| `p6-tests` | `sg-csp.run.json` | 148 | `sha256:b119cc094044b54a…` | on disk |
| `p6-tests` | `sg-childcare-leave.run.json` | 160 | `sha256:74ded3f1bf547aeb…` | on disk |
| `p6-tests` | `sg-csp-openfisca.run.json` | 2350 | `sha256:0fd972da010f5581…` | on disk |
| `p6-tests` | `sg-child-support.run.json` | 158 | `sha256:a14f4caececb90bb…` | on disk |
| `p6-tests` | `sg-child-support-cases.run.json` | 19664 | `sha256:765f0698075c83fd…` | on disk |
| `p8-verify` | `verify-clean.verify.json` | 652 | `sha256:e54fd98acc83f21f…` | on disk |
| `p8-verify` | `verify-unsat.verify.json` | 723 | `sha256:be8a47d8888088d3…` | on disk |
| `p8-verify` | `verify-dead-branch.verify.json` | 755 | `sha256:f1cc277b700e9cd7…` | on disk |
| `p8-verify` | `verify-vacuous-guard.verify.json` | 759 | `sha256:03f90a8fc2b185cb…` | on disk |
| `p8-verify` | `verify-seam.verify.json` | 1434 | `sha256:f3886286eb0b0eba…` | on disk |
| `p8-verify` | `sg-child-support-domain.verify.json` | 1089 | `sha256:a5f7aafd0013d26c…` | on disk |
| `p8-verify` | `sg-child-support-domain.verify.txt` | 3748 | `sha256:a138ec2352352e76…` | on disk |
| `p8-verify` | `sg-csp.verify.json` | 6152 | `sha256:73a3be153ff11d0a…` | on disk |
| `p8-verify` | `sg-csp.verify.txt` | 8130 | `sha256:162b2f2e644247ed…` | on disk |
| `p8-verify` | `sg-childcare-leave.verify.json` | 3301 | `sha256:d4d913d3f439f3b2…` | on disk |
| `p8-verify` | `sg-childcare-leave.verify.txt` | 5647 | `sha256:686433dd35640700…` | on disk |
| `p8-verify` | `sg-csp-openfisca.verify.json` | 1896 | `sha256:2ba528a19f38095e…` | on disk |
| `p8-verify` | `sg-csp-openfisca.verify.txt` | 4318 | `sha256:118d993d66bff099…` | on disk |
| `p8-verify` | `sg-child-support.verify.json` | 1483 | `sha256:2d5b239071680c6f…` | on disk |
| `p8-verify` | `sg-child-support.verify.txt` | 4108 | `sha256:b142ba6f75a670cd…` | on disk |
| `p8-verify` | `sg-child-support-cases.verify.json` | 3794 | `sha256:1b32d0f17ef81c67…` | on disk |
| `p8-verify` | `sg-child-support-cases.verify.txt` | 5936 | `sha256:46cc9f24cf0eb28e…` | on disk |
| `p8-verify` | `p8-verify.txt` | 1138 | `sha256:3e96df42a31108ed…` | on disk |
| `p7-lts` | `p7-lts.stderr` | 36 | `sha256:0d882bf9d3984abc…` | on disk |
| `p7-mcp` | `sg-child-support-deployable.zip` | 23308 | `sha256:31669250ef3539dd…` | on disk |
| `p7-mcp` | `p7-mcp.txt` | 162 | `sha256:959b2005df8baf76…` | on disk |
| `p7-akn` | `sg-child-support.akn.xml` | 41169 | `sha256:87d1eb7d8ce97788…` | on disk |
| `p7-akn` | `p7-akn.txt` | 99 | `sha256:03e720285a3db890…` | on disk |
| `p9-cost` | `cost-ledger.json` | 9798 | `sha256:4d3faab4e21542e8…` | on disk |
| `p9-cost` | `p9-cost.txt` | 0 | `sha256:e3b0c44298fc1c14…` | on disk |
| `p9-report` | `report.md` | 26184 | `sha256:364bd54c1dd6b172…` | on disk |
| `p9-report` | `report.html` | 26611 | `sha256:8b145673ddf752f2…` | on disk |
| `p9-report` | `p9-report.txt` | 242 | `sha256:5ac6b76783ac2b27…` | on disk |

---

## How to re-derive this report without trusting it

```
etc/go/go.sh verify --run-id 2026-08-25-36663f00-001 --gates
```

That re-reads `journal.ndjson`, re-hashes every artifact a receipt names, checks
that each granted gate was recorded before the first stage it gates began (by
record of either kind, so gated work run outside the driver is caught), and
recomputes the run verdict. It runs no build, calls no model, and makes no
network request. A second party can run it later against the same run directory
and does not have to believe anything this report says.

*Generated by `etc/go/report/render-report.mjs` from `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-08-25-36663f00-001/journal.ndjson`. Nothing in this report was typed; every figure resolves from a journal row.*
