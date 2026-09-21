
# Conversion report — sg-miles-card (primary)

|              |                                                                                  |
| ------------ | -------------------------------------------------------------------------------- |
| run id       | `2026-09-21-430aa01d-002`                                                                     |
| encoding     | primary — the committed encoding, replayed. It is driven through every reachable projection; nothing is encoded from source.                                        |
| subject      | sg-miles-card                                                                  |
| repo HEAD    | `28c8a1864ff56337a4cfd5c0e6fa39184e80910f` (clean)                                         |
| clock        | `2025-01-31T00:00:00Z`                                                              |
| `l4` binary  | `/Users/mengwong/src/legalese/l4wt/miles-card/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4`                                                              |
| journal      | `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-09-21-430aa01d-002/journal.ndjson` — 26 records, chain verifies |
| verdict      | **COMPLETE**                                                              |
| destined for | _no `canon` block in this subject's sidecar, so no destination is declared. A guessed path on a public repository is worse than an absent one._                                                        |

> COMPLETE means every declared stage has a receipt, no receipt is BROKEN, every non-PASS receipt carries a reason that appears below, and every gate is signed or explicitly waived. It is completeness of accounting, NOT greenness: legs below may report NOT-EXECUTABLE, DEGRADED or NOT-REGENERATED, and each says why.

---

## Gates

| gate | state | how |
| --- | --- | --- |
| HG1 | waived | **waived**: waived by Meng, 2026-09-21 — does not have time to review; corpus PASS on p6-tests (848/848), p7-catala PASS, p8-verify's four findings dispositioned in NOTES §6.1, no self-review substitute intended |

---

## What the source said

**ABSENT.** SPEC.md §P1 requires the source bundle with provenance — the retrieval of each source document, its integrity digest or immutable capture, the publisher's in-force statement, and the citation of the instrument and of each amendment. No stage in this run wrote it; `p1-ingest` is not declared for this run: the corpus is REPLAYED, not re-derived from source, so no ingest happened and none is claimed. (The stage itself no longer refuses — on the deposit path it validates a deposited source bundle — but a bundle is not what this run read.)

What this run did read, and its exact content:

| file | sha256 |
| --- | --- |
| `jl4/examples/legal/miles-card/miles-card-domain.l4` | `sha256:f89afa4822e09e28930dbc8711ba6ace9a5a4e4c9b0a0554b2708c3b44552d99` |
| `jl4/examples/legal/miles-card/classify.l4` | `sha256:a83fb5eda493131548d93374b9893432a7a24a6309e6a553f302f48c58f138da` |
| `jl4/examples/legal/miles-card/categorize.l4` | `sha256:b0a8cb5064f3520b90346448191b3cc9d72dc10c6ae93c4d8afe48bfa7c346cf` |
| `jl4/examples/legal/miles-card/dbs-yuu.l4` | `sha256:b92b7cfc0e742d294d18e6c649c95b072a0f0091b6e0834208d66899308a702a` |
| `jl4/examples/legal/miles-card/dbs-womans-world.l4` | `sha256:bb41f5814ff9afbe5fc3afc32e297b433647506b7798779b38526a97bcbfb451` |
| `jl4/examples/legal/miles-card/citi-rewards.l4` | `sha256:a072ffd93a3f94ba1453b071741ad2f0fbe12ec6e2ee19b059fe55a75e9c5e5b` |
| `jl4/examples/legal/miles-card/hsbc-revolution.l4` | `sha256:f7f7832969640a5248a1eaa497eb5adfe9a4a5e9fc37e2a80aa2e1b174e01ca9` |
| `jl4/examples/legal/miles-card/uob-ladys-solitaire.l4` | `sha256:396e525514bb07e7cf7f181f7a761d699eb45f1faa38f475315f77b514c5d367` |
| `jl4/examples/legal/miles-card/posb-passion.l4` | `sha256:512784aedcc118614666399bb4cd8776a8a07fc2e663d21bc01d29fae0926b9f` |
| `jl4/examples/legal/miles-card/flat-cards.l4` | `sha256:ba4f5045e8c5eb444a40976631963e7548d6489ca759221fe2ea0c981fdbd9e0` |
| `jl4/examples/legal/miles-card/miles-card.l4` | `sha256:1eba759862df6b16a7e75a76d03d3e14b75e3dff9ba4629b9dbacdef4bdd6f65` |
| `jl4/examples/legal/miles-card/miles-card-cases.l4` | `sha256:17b402124a521b4da68af9c11577b7bb65bf62cbfa2c880b294372455fa16359` |
| `jl4/examples/legal/miles-card/miles-card-disputed.l4` | `sha256:6752887cbf20830057e6f49e013022a7f3dfce21ee91246048f3d78b54b0bc42` |

---

## What the external-modification sweep searched and surfaced

**ABSENT.** SPEC.md §P2 requires the external-modification register, and requires this report to state what was SEARCHED, not only what was found — "no modification found" is a checked claim, not a default. No stage in this run wrote it; `p2-sweep` is not declared for this run. Nothing was searched, so nothing may be reported as searched, and this report makes no claim that the encoding is current with respect to courts striking or reading down a provision, the regulator's interpretive guidance, or instruments in flight. (On the deposit path the stage validates a deposited register — but note that validating a register is not performing a sweep: no procedure enumerates the searches that should have run.)

---

## What the encoding decided

**ABSENT.** SPEC.md §P3/§P4 require what the encoding decided, including every ambiguity fork and every externally-settled resolution. No stage in this run wrote it; `p3-encode`, `p4-forks` and `p5-gate` are not declared for this run — they validate de novo deposits, and this run replayed the committed encoding — so this run made no encoding decisions and opened no forks. The encoding it exercised is the committed corpus.

**What was checked about the committed encoding:** PASS — 

Oracle (`structural`): `l4 check miles-card-domain.l4 && l4 check classify.l4 && l4 check categorize.l4 && l4 check dbs-yuu.l4 && l4 check dbs-womans-world.l4 && l4 check citi-rewards.l4 && l4 check hsbc-revolution.l4 && l4 check uob-ladys-solitaire.l4 && l4 check posb-passion.l4 && l4 check flat-cards.l4 && l4 check miles-card.l4 && l4 check miles-card-cases.l4 && l4 check miles-card-disputed.l4 && no ELSE IF chain && temporal closure NOT CHECKED (0 matched arms, floor 0 — see note)`

typechecking is the compiler's own verdict on the module; the two grep checks are the mechanisable half of P3's house rules, and the dated-arm floor stops the second one passing over an empty matched set (a 0 floor demotes that sub-check to NOT CHECKED on the receipt rather than passing it). Faithfulness to the source regulation is NOT covered and is carried by HG1.

> *claimed, not verified* (phase-script): temporal closure NOT CHECKED (does not affect status): 0 dated arms matched and the pinned floor for this encoding (checks.min_dated_arms) is 0, so the @ref-per-dated-arm rule had nothing to hold — a vacuous pass refused, not a green earned; see the sidecar's NOTES.md for the population census

> *claimed, not verified* (phase-script): isomorphism against Issuer terms and conditions for eight Singapore consumer credit/debit card reward programmes (DBS yuu, DBS Woman's World, UOB Lady's Solitaire, HSBC Revolution, Citi Rewards, POSB PAssion, UOB PRVI Miles, Citi PremierMiles), as published by the issuers and retrieved 2026-09-21. Private contract terms, not law. is unverified by this stage and is HG1's subject

---

## What each projection preserved and lost

| leg | status | oracle class | what it says |
| --- | --- | --- | --- |
| `p7-mcp` | SKIPPED | none | JL4_GO_SERVICE_URL is unset, so no jl4-service was contacted and no deployment was made. The deployable zip was still built and hashed. Set JL4_GO_SERVICE_URL to a LOOPBACK service (./dev-start.sh brings one up on 8080) to exercise the deployment half. |
| `p7-tnr` | PASS | differential | this run REGENERATED the prose with 'l4 nlg' and it reproduces every committed .nlg.golden byte for byte. The goldens are defended by a separate gate — jl4-test's jl4NlgAnnotationsGolden writes them in-process and fails on drift — and l4-cli-test pins that the CLI emits the same expression as that producer, so this compares against something another gate already holds still rather than against itself. |
| `p7-akn` | UNVERIFIED (EXTRA) | none | an Akoma Ntoso 3.0 document was emitted and is well formed at the shallow level checked here (declaration, AKN namespace, one balanced root). It is UNVERIFIED because well-formedness is the only oracle available: this repo carries no AKN schema and no AKN checker, so nothing establishes that the document is schema-valid, let alone that it says what Issuer terms and conditions for eight Singapore consumer credit/debit card reward programmes (DBS yuu, DBS Woman's World, UOB Lady's Solitaire, HSBC Revolution, Citi Rewards, POSB PAssion, UOB PRVI Miles, Citi PremierMiles), as published by the issuers and retrieved 2026-09-21. Private contract terms, not law. says. etc/go/lib/verdict.mjs bars a wellformedness-class oracle from PASS for exactly this reason. |
| `p7-catala` | PASS | execution | Catala's own interpreter RAN the emitted modules and agreed. `clerk test` re-executed all 1218 ```catala-test-cli block(s) across 8 emission(s) with 0 failures, and every expected value in those blocks was computed by L4's evaluator (R7), so this is two independently written evaluators returning the same answers over the same rules — the artifact ran on its target engine, on cases, and agreed. Layers 1 and 2 ran first and are structural rather than executional: `catala typecheck` accepted all 8, and `catala proof` reported no overlapping exceptions on all 8, which is the only check anywhere that would notice a Mode B ladder whose rungs stopped being linear. The class is claimed on layer 3 alone; layers 1 and 2 would only license `structural`. |

### `p7-mcp` — SKIPPED

JL4_GO_SERVICE_URL is unset, so no jl4-service was contacted and no deployment was made. The deployable zip was still built and hashed. Set JL4_GO_SERVICE_URL to a LOOPBACK service (./dev-start.sh brings one up on 8080) to exercise the deployment half.

**Oracle:** none ran.

### `p7-tnr` — PASS


**Oracle** (`differential`, exit 0): `l4 nlg <module> -o <run>/<stem>.nlg && diff <golden> <run>/<stem>.nlg  (x1)`
this run REGENERATED the prose with 'l4 nlg' and it reproduces every committed .nlg.golden byte for byte. The goldens are defended by a separate gate — jl4-test's jl4NlgAnnotationsGolden writes them in-process and fails on drift — and l4-cli-test pins that the CLI emits the same expression as that producer, so this compares against something another gate already holds still rather than against itself.

`miles-card.lines=8` · `miles-card.bytes=1274` · `pairs=1` · `differing=0`

> *claimed, not verified* (phase-script): This leg reproduces prose; it does not yet round-trip it. SPEC.md §P7 names Times-New-Roman prose regeneration whose edits can be carried back into the L4, and the return leg (the TNR prototype on the unpushed nlg-roundtrip branch) is reachable from no l4 subcommand. What is measured here is the forward direction only.

### `p7-akn` — UNVERIFIED (EXTRA)

an Akoma Ntoso 3.0 document was emitted and is well formed at the shallow level checked here (declaration, AKN namespace, one balanced root). It is UNVERIFIED because well-formedness is the only oracle available: this repo carries no AKN schema and no AKN checker, so nothing establishes that the document is schema-valid, let alone that it says what Issuer terms and conditions for eight Singapore consumer credit/debit card reward programmes (DBS yuu, DBS Woman's World, UOB Lady's Solitaire, HSBC Revolution, Citi Rewards, POSB PAssion, UOB PRVI Miles, Citi PremierMiles), as published by the issuers and retrieved 2026-09-21. Private contract terms, not law. says. etc/go/lib/verdict.mjs bars a wellformedness-class oracle from PASS for exactly this reason.

**Oracle:** none ran.

`bytes=206265`

> *claimed, not verified* (phase-script): EXTRA leg. render --format akn is UNDOCUMENTED (its own command description lists only html|text|json|plan) and appears in no P7 projection table. Surfaced here because a demo arguing 'cooperate with the standards' should not be sitting on an unlisted LegalDocML output.

### `p7-catala` — PASS


**Oracle** (`execution`, exit 0): `l4 catala <module> -o <run>/<stem>.catala_en --fixed-now 2025-01-31T00:00:00Z  (x8) && node etc/validate-catala.mjs <emitted…>`
Catala's own interpreter RAN the emitted modules and agreed. `clerk test` re-executed all 1218 ```catala-test-cli block(s) across 8 emission(s) with 0 failures, and every expected value in those blocks was computed by L4's evaluator (R7), so this is two independently written evaluators returning the same answers over the same rules — the artifact ran on its target engine, on cases, and agreed. Layers 1 and 2 ran first and are structural rather than executional: `catala typecheck` accepted all 8, and `catala proof` reported no overlapping exceptions on all 8, which is the only check anywhere that would notice a Mode B ladder whose rungs stopped being linear. The class is claimed on layer 3 alone; layers 1 and 2 would only license `structural`.

`modules_total=13` · `modules_emitted=8` · `modules_without_export=5` · `basenames_rewritten=8` · `test_blocks_emitted=602` · `typecheck_ok=8` · `proof_ok=8` · `clerk_tests_passed=1218` · `clerk_tests_total=1218` · `clerk_tests_failed=0` · `clerk_files=8`

> *claimed, not verified* (phase-script): WHAT AGREEMENT HERE DOES NOT ESTABLISH. The expected values clerk re-checked were produced by L4 during this same emission, so a misreading of the source law that both languages share agrees with itself and passes. This leg falsifies a LOWERING that changes the answer; whether the L4 says what Issuer terms and conditions for eight Singapore consumer credit/debit card reward programmes (DBS yuu, DBS Woman's World, UOB Lady's Solitaire, HSBC Revolution, Citi Rewards, POSB PAssion, UOB PRVI Miles, Citi PremierMiles), as published by the issuers and retrieved 2026-09-21. Private contract terms, not law. says is HG1's, and no count on this row bears on it.

> *claimed, not verified* (phase-script): 5 of the 13 declared module(s) carry no `@export` and were not lowered: a module with no deployable surface emits no callable scope. They are counted, not failed. Skipped: jl4/examples/legal/miles-card/miles-card-domain.l4 jl4/examples/legal/miles-card/classify.l4 jl4/examples/legal/miles-card/categorize.l4 jl4/examples/legal/miles-card/miles-card-cases.l4 jl4/examples/legal/miles-card/miles-card-disputed.l4


---

## Test results

**PASS**

Oracle (`execution`): `node etc/go/lib/assert-report.mjs miles-card-domain.run.json classify.run.json categorize.run.json dbs-yuu.run.json dbs-womans-world.run.json citi-rewards.run.json hsbc-revolution.run.json uob-ladys-solitaire.run.json posb-passion.run.json flat-cards.run.json miles-card.run.json miles-card-cases.run.json miles-card-disputed.run.json `

the module's own #ASSERT directives were evaluated by the L4 evaluator and every result[] entry of kind 'assertion' is true with no entries of kind 'error'. The process exit code and the envelope's 'ok' field are BOTH ignored: measured, a failing #ASSERT yields ok:true and exit 0.

`assertions_total=848` · `encoding_id=primary`

> *claimed, not verified* (phase-script): these are the committed encoding's own assertions, already in the tree before this run: a run about the committed encoding does no encoding, so none of them were written to discriminate between the fork register's readings

---

## Every other stage that reported

The stages above are narrated under the heading they belong to. These are the rest — reporting stages, and anything added to the pipeline that has no heading of its own yet. They are here because the verdict gloss at the top of this report promises that every non-PASS receipt's reason appears below, and a stage with no site is how that promise quietly stops being true.

**`p8-verify`:** DEGRADED — the verifier ran over 13 module(s) of the primary encoding and reported 4 propositional finding(s) across 113 analysed decision(s). Each finding names its decision, its site in the ladder, the atoms involved and what is wrong with it; see the .verify.txt artifacts. All 5 controls reproduced, so the checker was working when it said so — these are findings about the encoding, not about the harness.

`encoding_id=primary` · `miles-card-domain.decisions=0` · `miles-card-domain.analysed=0` · `miles-card-domain.skipped=0` · `miles-card-domain.nested_not_visited=0` · `miles-card-domain.findings=0` · `classify.decisions=5` · `classify.analysed=3` · `classify.skipped=2` · `classify.nested_not_visited=0` · `classify.findings=0` · `categorize.decisions=1` · `categorize.analysed=0` · `categorize.skipped=1` · `categorize.nested_not_visited=0` · `categorize.findings=0` · `dbs-yuu.decisions=101` · `dbs-yuu.analysed=21` · `dbs-yuu.skipped=80` · `dbs-yuu.nested_not_visited=16` · `dbs-yuu.findings=3` · `dbs-womans-world.decisions=61` · `dbs-womans-world.analysed=13` · `dbs-womans-world.skipped=48` · `dbs-womans-world.nested_not_visited=6` · `dbs-womans-world.findings=1` · `citi-rewards.decisions=85` · `citi-rewards.analysed=22` · `citi-rewards.skipped=63` · `citi-rewards.nested_not_visited=0` · `citi-rewards.findings=0` · `hsbc-revolution.decisions=69` · `hsbc-revolution.analysed=14` · `hsbc-revolution.skipped=55` · `hsbc-revolution.nested_not_visited=1` · `hsbc-revolution.findings=0` · `uob-ladys-solitaire.decisions=84` · `uob-ladys-solitaire.analysed=21` · `uob-ladys-solitaire.skipped=63` · `uob-ladys-solitaire.nested_not_visited=0` · `uob-ladys-solitaire.findings=0` · `posb-passion.decisions=76` · `posb-passion.analysed=18` · `posb-passion.skipped=58` · `posb-passion.nested_not_visited=0` · `posb-passion.findings=0` · `flat-cards.decisions=15` · `flat-cards.analysed=1` · `flat-cards.skipped=14` · `flat-cards.nested_not_visited=0` · `flat-cards.findings=0` · `miles-card.decisions=4` · `miles-card.analysed=0` · `miles-card.skipped=4` · `miles-card.nested_not_visited=0` · `miles-card.findings=0` · `miles-card-cases.decisions=40` · `miles-card-cases.analysed=0` · `miles-card-cases.skipped=40` · `miles-card-cases.nested_not_visited=0` · `miles-card-cases.findings=0` · `miles-card-disputed.decisions=0` · `miles-card-disputed.analysed=0` · `miles-card-disputed.skipped=0` · `miles-card-disputed.nested_not_visited=0` · `miles-card-disputed.findings=0` · `controls_reproduced=5/5` · `decisions=541` · `analysed=113` · `skipped_non_boolean=428` · `nested_not_visited=23` · `findings=4` · `merged_atom_occurrences=224`

> *claimed, not verified* (phase-script): A clean run is a WEAK statement and the receipt refuses to imply otherwise. The analysis is propositional: every leaf (a projection, a comparison, an arithmetic test, a call to another DECIDE) is an opaque atom, so no numeric, interval, date or string contradiction is in range, and neither is anything that only appears once two named rules are unfolded against each other. Each DECIDE is read on its own. Findings are sound; silence is not a consistency proof. Full statement: l4 verify --help.

> *claimed, not verified* (phase-script): Rung 1 of 3. R5 (2026-08-02) ordered the P8 ladder as ROBDD first, the R4 fork-space agreement/divergence sweep second, an external model checker (TLA+/NuSMV/UPPAAL class) last. Rungs 2 and 3 are unbuilt: rung 2 needs the fork register P4 does not yet produce, rung 3 waits on the LTS semantics. 428 of 541 decisions are outside rung 1 entirely because they do not return BOOLEAN — they are counted, named in the artifact, and not reported as clean. A further 23 are outside it for a different reason: they are defined inside a WHERE clause, and neither this command nor the ladder's own entry point descends into one, so they are in NEITHER the analysed nor the skipped column. That is why the figure is on the receipt: 'analysed + skipped' does not total the corpus, and an exclusion nobody can size is an exclusion nobody believes.

**`p9-explain`:** SKIPPED — subject 'sg-miles-card' declares no 'explainer' section in subject.json, so it has no checked-in narrative to render. Declaring the directory is deliberate rather than discovered: a mistyped directory name would otherwise yield a fully-absent document with no error anywhere.

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
| `p0-preflight` | PASS | 10s | 228 ms |  |
| `p3-check` | PASS | 29s | 197 ms |  |
| `p6-tests` | PASS | 49s | 238 ms |  |
| `p8-verify` | DEGRADED | 1m 17s | 275 ms |  |
| `p7-mcp` | SKIPPED | 64 ms | 269 ms |  |
| `p7-tnr` | PASS | 4s | 255 ms |  |
| `p7-akn` | UNVERIFIED | 3s | 239 ms |  |
| `p7-catala` | PASS | 33s | 188 ms |  |
| `p9-cost` | PASS | 540 ms | 46 ms |  |
| `p9-report` | PASS | 94 ms | 80 ms |  |
| `p9-explain` | SKIPPED | 12 ms | 83 ms |  |
| **total** | | **3m 28s** | **2s** | |

`dispatch` is the driver's own time before each stage started — asking the stage for its inputs, digesting and itemising them, and searching for a replayable receipt. It is spent on every stage, including the ones that then replay in milliseconds, and on an EXECUTED stage it is listed separately rather than folded in, because it is the harness's cost and not the stage's work.


**Attributed — what the agent sessions spent.** Read out of the harness's own JSONL transcripts, 22 of them, each named in `cost-ledger.json` with its sha256 so a second party can repeat the derivation. Nobody typed these numbers; the transcript is nonetheless an ordinary file, which is why they are attributed rather than attested.

| | in this run's window | across the whole session |
| --- | ---: | ---: |
| API requests | 0 | 2,204 |
| output tokens | 0 | 708,570 |
| of which reasoning | 0 | |
| input tokens | 0 | |
| cache writes | 0 | |
| cache reads | 0 | |
| tool calls | 0 | 2,369 |

The right-hand column is an upper bound, not a second measurement: it is everything the session did, including whatever else it was asked to do. The left column clips to this run's own window, from its first journal record to its last.

Both columns are attributions **by clock**, and a clock cannot tell work on this run apart from work that merely happened at the same time. So the left column misses what came before the driver was first invoked — reading the source, deciding what to encode — and includes anything else the session did between the first record and the last, which on a human-gated pipeline can be days. It understates at one end and overstates at the other; the honest reading is that the true figure lies between the two columns, nearer the left.

Model(s): `claude-fable-5-1 <synthetic> claude-sonnet-5 claude-opus-5`. Across the whole session — the right-hand column, not the left — 1,948 requests were made by subagents, spending 365,913 output tokens across 0 workflow fan-out(s). Those are measured from the subagents' own transcripts, which the session file does not contain at all: a ledger that read only the session file would report a fraction and look complete.

**Network, model-initiated.** In this run's window — the left-hand column above, not the right — 0 web search(es), 0 fetch(es) and 0 external-service call(s), taking 0 ms between them. Across the whole session: 0 web search(es).

That counts calls the MODEL made, by tool name. A stage that runs `curl` reaches the network inside a shell call and is invisible to it, so the pipeline's own retrievals are counted separately, by the stage that makes them:

> This run declared no `p1-ingest` stage, so there is no source-side figure. On the committed-encoding path the sources were fetched in an earlier run; on the deposit path `p1-ingest` validates the bundle that records them.

**Wall clock.** The run spans 3m 31s from its first journal record to its last. Of that, 3m 28s is attested stage execution, and at least 0 ms is measured tool-call time, giving a floor of 3m 28s during which something was demonstrably running. Both component figures stop where the attributed ones do; the span does not.

The gap between the span and that floor is mostly not idleness in the ordinary sense: this pipeline stops at a human gate and waits. The floor is a floor and not an estimate — it unions attested stage brackets with measured tool intervals, and counts nothing at all for the time a model spends reasoning between two tool calls, which is real work that leaves no interval to measure.

**No money.** Token counts are facts about this run; prices are facts about a contract and change without notice. A stale rate table would put a confident wrong figure in a report whose whole premise is that every number has a row behind it. A reader with a rate card can multiply.

The attributed figures stop at `p7-catala` — the last stage that had written a receipt when `p9-cost` read the journal. `p9-cost` runs before the reporting stages so that this section can exist, so it cannot count itself, `p9-report` or `p9-explain`. The per-stage table above is rendered after `run_end` and does see them, which is why the two totals differ by exactly the stages between them.

One further boundary: 1 of the transcripts read is the session that did the reading, so its own figures stop at the moment it measured itself. Two reads of a live transcript minutes apart differ by exactly the calls that did the reading.

> *claimed, not verified* (phase-script): The stage timings are ATTESTED — measured by the driver, and ledger.verify refuses any elapsed_ms more than a second longer than the bracket its own row sits in (the second of slack is for the whole-second clock fallback in lib/clock.sh). The token and tool figures are ATTRIBUTED: read from the harness's transcripts, which are named with their sha256 so the derivation can be repeated, but which are ordinary files. Figures stop at this stage; p9-report and p9-explain run after it. What each figure covers, and what it cannot, is stated in the report section that renders them, so it is written once.

---

## Every artifact this run put on disk

| stage | artifact | bytes (recorded) | sha256 (recorded) | state now |
| --- | --- | --- | --- | --- |
| `p0-preflight` | `probes.json` | 1970 | `sha256:a2daa18156196bb4…` | on disk |
| `p0-preflight` | `cli-surface.txt` | 81 | `sha256:e20fc97289bb520e…` | on disk |
| `p0-preflight` | `tripwire.json` | 519 | `sha256:aa1c12170035a408…` | on disk |
| `p3-check` | `p3-check.txt` | 1933 | `sha256:1241fac260717f94…` | on disk |
| `p6-tests` | `p6-assertions.txt` | 1863 | `sha256:a65af8cc8d707be8…` | on disk |
| `p6-tests` | `miles-card-domain.run.json` | 147 | `sha256:cbf8fdc28176d939…` | on disk |
| `p6-tests` | `classify.run.json` | 2923 | `sha256:dc0ff9eec2256a0f…` | on disk |
| `p6-tests` | `categorize.run.json` | 140 | `sha256:806b7c64e7728f8f…` | on disk |
| `p6-tests` | `dbs-yuu.run.json` | 33313 | `sha256:9907beefa4c3e75e…` | on disk |
| `p6-tests` | `dbs-womans-world.run.json` | 38008 | `sha256:30fe36c54695530d…` | on disk |
| `p6-tests` | `citi-rewards.run.json` | 40578 | `sha256:e03da3d01395e9d4…` | on disk |
| `p6-tests` | `hsbc-revolution.run.json` | 46527 | `sha256:07153c908c446b5a…` | on disk |
| `p6-tests` | `uob-ladys-solitaire.run.json` | 51194 | `sha256:7d0704edc1c2950b…` | on disk |
| `p6-tests` | `posb-passion.run.json` | 32672 | `sha256:a7f69673c7af8da7…` | on disk |
| `p6-tests` | `flat-cards.run.json` | 10461 | `sha256:73dbb511a5818b3a…` | on disk |
| `p6-tests` | `miles-card.run.json` | 2143 | `sha256:0f20f5e0c430a7d2…` | on disk |
| `p6-tests` | `miles-card-cases.run.json` | 27155 | `sha256:2f0761af9d7f55a0…` | on disk |
| `p6-tests` | `miles-card-disputed.run.json` | 30355 | `sha256:3f80680afa369abc…` | on disk |
| `p8-verify` | `verify-clean.verify.json` | 646 | `sha256:2dcbbef3bf9fb585…` | on disk |
| `p8-verify` | `verify-unsat.verify.json` | 717 | `sha256:e2b7fbd9031064b4…` | on disk |
| `p8-verify` | `verify-dead-branch.verify.json` | 749 | `sha256:74fcabdeca9b09c9…` | on disk |
| `p8-verify` | `verify-vacuous-guard.verify.json` | 753 | `sha256:7b78cee8ca7cb4c4…` | on disk |
| `p8-verify` | `verify-seam.verify.json` | 1428 | `sha256:320a00637f7b95f5…` | on disk |
| `p8-verify` | `miles-card-domain.verify.json` | 458 | `sha256:493c897c43bd0db3…` | on disk |
| `p8-verify` | `miles-card-domain.verify.txt` | 3331 | `sha256:5161ba60dac07b87…` | on disk |
| `p8-verify` | `classify.verify.json` | 1012 | `sha256:31fdf27704e5dbd6…` | on disk |
| `p8-verify` | `classify.verify.txt` | 3767 | `sha256:6974e31b2b2f6486…` | on disk |
| `p8-verify` | `categorize.verify.json` | 574 | `sha256:7bfa61d312e04861…` | on disk |
| `p8-verify` | `categorize.verify.txt` | 3428 | `sha256:7ea3c0fa086c2826…` | on disk |
| `p8-verify` | `dbs-yuu.verify.json` | 15452 | `sha256:a0a27fdc14b8f7dc…` | on disk |
| `p8-verify` | `dbs-yuu.verify.txt` | 16312 | `sha256:05a9d36d316eef59…` | on disk |
| `p8-verify` | `dbs-womans-world.verify.json` | 9596 | `sha256:d96cc0f25ac69031…` | on disk |
| `p8-verify` | `dbs-womans-world.verify.txt` | 11261 | `sha256:9a3ada5c70c57cde…` | on disk |
| `p8-verify` | `citi-rewards.verify.json` | 12462 | `sha256:c72e16b6dfa9bf11…` | on disk |
| `p8-verify` | `citi-rewards.verify.txt` | 13551 | `sha256:ce76f3e3ccbc1d2e…` | on disk |
| `p8-verify` | `hsbc-revolution.verify.json` | 10823 | `sha256:9ffb8d3a0ce78470…` | on disk |
| `p8-verify` | `hsbc-revolution.verify.txt` | 12376 | `sha256:2679bda9fef906bb…` | on disk |
| `p8-verify` | `uob-ladys-solitaire.verify.json` | 12526 | `sha256:351165cfb7a1159e…` | on disk |
| `p8-verify` | `uob-ladys-solitaire.verify.txt` | 13642 | `sha256:0f7e3c58e02fa1cf…` | on disk |
| `p8-verify` | `posb-passion.verify.json` | 11179 | `sha256:84dc1cf00eac2bf7…` | on disk |
| `p8-verify` | `posb-passion.verify.txt` | 12450 | `sha256:dac7c920be9f0f22…` | on disk |
| `p8-verify` | `flat-cards.verify.json` | 2567 | `sha256:e205231665bd8df2…` | on disk |
| `p8-verify` | `flat-cards.verify.txt` | 5134 | `sha256:7d85f9cf195abbca…` | on disk |
| `p8-verify` | `miles-card.verify.json` | 999 | `sha256:e7b09b97722b83c8…` | on disk |
| `p8-verify` | `miles-card.verify.txt` | 3793 | `sha256:06318e80007c5759…` | on disk |
| `p8-verify` | `miles-card-cases.verify.json` | 6949 | `sha256:32f38a4daff38ced…` | on disk |
| `p8-verify` | `miles-card-cases.verify.txt` | 9022 | `sha256:4ddbff2edfd5b608…` | on disk |
| `p8-verify` | `miles-card-disputed.verify.json` | 460 | `sha256:914dd6a8c24d977d…` | on disk |
| `p8-verify` | `miles-card-disputed.verify.txt` | 3333 | `sha256:7f668782a747cf50…` | on disk |
| `p8-verify` | `p8-verify.txt` | 1936 | `sha256:8638cc5532284a6b…` | on disk |
| `p7-mcp` | `sg-miles-card-deployable.zip` | 199588 | `sha256:16a941c3ce47f450…` | on disk |
| `p7-mcp` | `p7-mcp.txt` | 160 | `sha256:e1e704dedd8b3780…` | on disk |
| `p7-tnr` | `miles-card.nlg` | 1274 | `sha256:cd7a0cce397e7166…` | on disk |
| `p7-tnr` | `p7-tnr.txt` | 331 | `sha256:8c19ece9d8c0ee03…` | on disk |
| `p7-akn` | `sg-miles-card.akn.xml` | 206265 | `sha256:889b81e75a02d4e9…` | on disk |
| `p7-akn` | `p7-akn.txt` | 100 | `sha256:7c95ed862e53c56d…` | on disk |
| `p7-catala` | `dbsyuu.catala_en` | 63762 | `sha256:be5e421c1dcac77d…` | on disk |
| `p7-catala` | `dbswomansworld.catala_en` | 72410 | `sha256:581e4523a9595d2d…` | on disk |
| `p7-catala` | `citirewards.catala_en` | 96909 | `sha256:1a191f91a5627a67…` | on disk |
| `p7-catala` | `hsbcrevolution.catala_en` | 103934 | `sha256:99560bb8bf53bb7a…` | on disk |
| `p7-catala` | `uobladyssolitaire.catala_en` | 97108 | `sha256:7036bfcbc21db8af…` | on disk |
| `p7-catala` | `posbpassion.catala_en` | 102341 | `sha256:e579bb8ff622da5c…` | on disk |
| `p7-catala` | `flatcards.catala_en` | 35369 | `sha256:a75081e97ba4e291…` | on disk |
| `p7-catala` | `milescard.catala_en` | 103440 | `sha256:ba201eda785947be…` | on disk |
| `p7-catala` | `p7-catala.validate.txt` | 3888 | `sha256:64ffdd368bda23f4…` | on disk |
| `p7-catala` | `p7-catala.txt` | 195236 | `sha256:7b58b2a9a8691194…` | on disk |
| `p9-cost` | `cost-ledger.json` | 22838 | `sha256:d40bc815a916bf9f…` | on disk |
| `p9-cost` | `p9-cost.txt` | 0 | `sha256:e3b0c44298fc1c14…` | on disk |
| `p9-report` | `report.md` | 34075 | `sha256:f9dde3fcbd3c0d55…` | on disk |
| `p9-report` | `report.html` | 34640 | `sha256:bc3d38967a15bdc0…` | on disk |
| `p9-report` | `p9-report.txt` | 242 | `sha256:b3d1dfcbf00c93ca…` | on disk |

---

## How to re-derive this report without trusting it

```
etc/go/go.sh verify --run-id 2026-09-21-430aa01d-002 --gates
```

That re-reads `journal.ndjson`, re-hashes every artifact a receipt names, checks
that each granted gate was recorded before the first stage it gates began (by
record of either kind, so gated work run outside the driver is caught), and
recomputes the run verdict. It runs no build, calls no model, and makes no
network request. A second party can run it later against the same run directory
and does not have to believe anything this report says.

*Generated by `etc/go/report/render-report.mjs` from `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-09-21-430aa01d-002/journal.ndjson`. Nothing in this report was typed; every figure resolves from a journal row.*
