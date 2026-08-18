
# G1 conversion report — sg-succession

|             |                                                                                  |
| ----------- | -------------------------------------------------------------------------------- |
| run id      | `2026-08-18-2b3f2400-002`                                                                     |
| milestone   | G1 — the replay run. The existing corpus is driven through every reachable projection; nothing is encoded from source.                                |
| subject     | sg-succession                                                                  |
| repo HEAD   | `afcef88f253d4076942883092ace7521e53bd3ad` (dirty)                                         |
| clock       | `2025-01-31T00:00:00Z`                                                              |
| `l4` binary | `/Users/mengwong/src/legalese/l4wt/sg-succession/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4`                                                              |
| journal     | `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-08-18-2b3f2400-002/journal.ndjson` — 19 records, chain verifies |
| verdict     | **COMPLETE**                                                              |

> COMPLETE means every declared stage has a receipt, no receipt is BROKEN, every non-PASS receipt carries a reason that appears below, and every gate is signed or explicitly waived. It is completeness of accounting, NOT greenness: legs below may report NOT-EXECUTABLE, DEGRADED or NOT-REGENERATED, and each says why.

---

## Gates

| gate | state | how |
| --- | --- | --- |
| HG1 | waived | **waived**: NOT REVIEWED. First run over a brand-new encoding of three Singapore Acts; no domain expert has read it against the statutes. The waiver lets the run PRODUCE the evidence a reviewer needs, not because that review has happened. Start at fork-register F6 (ISA s 6(b) half-blood ranking, knowingly not implemented) and F2 (legitimacy delegated to the fact supplier). |

---

## What the source said

**ABSENT.** SPEC.md §P1 requires the source bundle with provenance — the SEC entry point, the eCFR retrieval, and the FR citations for the adoption and each amendment. No stage in this run wrote it; `p1-ingest` is not declared at this milestone: the corpus is REPLAYED, not re-derived from source, so no ingest happened and none is claimed. (The stage itself no longer refuses — at `g2` it validates a deposited source bundle — but a bundle is not what this run read.)

What this run did read, and its exact content:

| file | sha256 |
| --- | --- |
| `jl4/examples/legal/sg-succession/sg-succession-domain.l4` | `sha256:983722aec9abca96329914b6127dd2f6c9b74fdfc005ae8a56ab1872b9633154` |
| `jl4/examples/legal/sg-succession/sg-wills.l4` | `sha256:326e74bab86a883edc908446abfa0a37e6fb9ac6397ed696d6ef77de313680d9` |
| `jl4/examples/legal/sg-succession/sg-isa.l4` | `sha256:67ca451d054459a9ebffe76bd592a3cb15b0e59e17721890f9866b199fab29d1` |
| `jl4/examples/legal/sg-succession/sg-paa.l4` | `sha256:032456f05b81913c222affc9ac8b77f2c91643619c44e8f7bf5c81288146180a` |
| `jl4/examples/legal/sg-succession/sg-succession.l4` | `sha256:a23fb518d0fd5db17a3db3ed917ff9d16cf60385b79eba0976ecd5ee0091ae25` |
| `jl4/examples/legal/sg-succession/sg-succession-cases.l4` | `sha256:fc292e05d2283559c7f23252b7a8862b426174d51bebd205b97e41f5ce49be2e` |

---

## What the external-modification sweep searched and surfaced

**ABSENT.** SPEC.md §P2 requires the external-modification register, and requires this report to state what was SEARCHED, not only what was found — "no modification found" is a checked claim, not a default. No stage in this run wrote it; `p2-sweep` is not declared at this milestone. Nothing was searched, so nothing may be reported as searched, and this report makes no claim that the encoding is current with respect to courts, C&DIs, no-action letters, or rules in flight. (At `g2` the stage validates a deposited register — but note that validating a register is not performing a sweep: no procedure enumerates the searches that should have run.)

---

## What the encoding decided

**ABSENT.** SPEC.md §P3/§P4 require what the encoding decided, including every ambiguity fork and every externally-settled resolution. No stage in this run wrote it; `p3-encode`, `p4-forks` and `p5-gate` are not declared at this milestone — they validate de novo deposits, and this run replayed the committed corpus — so this run made no encoding decisions and opened no forks. The encoding it exercised is the committed corpus.

**What was checked about the committed encoding:** PASS — 

Oracle (`structural`): `l4 check sg-succession-domain.l4 && l4 check sg-wills.l4 && l4 check sg-isa.l4 && l4 check sg-paa.l4 && l4 check sg-succession.l4 && l4 check sg-succession-cases.l4 && no ELSE IF chain && temporal closure NOT CHECKED (0 matched arms, floor 0 — see note)`

typechecking is the compiler's own verdict on the module; the two grep checks are the mechanisable half of P3's house rules, and the dated-arm floor stops the second one passing over an empty matched set (a 0 floor demotes that sub-check to NOT CHECKED on the receipt rather than passing it). Faithfulness to the source regulation is NOT covered and is carried by HG1.

> *claimed, not verified* (phase-script): temporal closure NOT CHECKED (does not affect status): 0 dated arms matched and the pinned floor for this origin (checks.min_dated_arms) is 0, so the @ref-per-dated-arm rule had nothing to hold — a vacuous pass refused, not a green earned; see the sidecar's NOTES.md for the population census

> *claimed, not verified* (phase-script): isomorphism against Wills Act 1838; Intestate Succession Act 1967; Probate and Administration Act 1934 (Singapore) is unverified by this stage and is HG1's subject

---

## What each projection preserved and lost

| leg | status | oracle class | what it says |
| --- | --- | --- | --- |
| `p7-lts` | NOT-BUILT | none | l4 state-graph exited 1; it exits 1 with 'No regulative rules found in module' when a module has none |
| `p7-akn` | UNVERIFIED (EXTRA) | none | an Akoma Ntoso 3.0 document was emitted and is well formed at the shallow level checked here (declaration, AKN namespace, one balanced root). It is UNVERIFIED because well-formedness is the only oracle available: this repo carries no AKN schema and no AKN checker, so nothing establishes that the document is schema-valid, let alone that it says what Wills Act 1838; Intestate Succession Act 1967; Probate and Administration Act 1934 (Singapore) says. etc/go/lib/verdict.mjs bars a wellformedness-class oracle from PASS for exactly this reason. |

### `p7-lts` — NOT-BUILT

l4 state-graph exited 1; it exits 1 with 'No regulative rules found in module' when a module has none

**Blocker.** No regulative rules found in module

**Oracle:** none ran.

### `p7-akn` — UNVERIFIED (EXTRA)

an Akoma Ntoso 3.0 document was emitted and is well formed at the shallow level checked here (declaration, AKN namespace, one balanced root). It is UNVERIFIED because well-formedness is the only oracle available: this repo carries no AKN schema and no AKN checker, so nothing establishes that the document is schema-valid, let alone that it says what Wills Act 1838; Intestate Succession Act 1967; Probate and Administration Act 1934 (Singapore) says. etc/go/lib/verdict.mjs bars a wellformedness-class oracle from PASS for exactly this reason.

**Oracle:** none ran.

`bytes=50886`

> *claimed, not verified* (phase-script): EXTRA leg. render --format akn is UNDOCUMENTED (its own command description lists only html|text|json|plan) and appears in no P7 projection table. Surfaced here because a demo arguing 'cooperate with the standards' should not be sitting on an unlisted LegalDocML output.


---

## Test results

**PASS**

Oracle (`execution`): `node etc/go/lib/assert-report.mjs sg-succession-domain.run.json sg-wills.run.json sg-isa.run.json sg-paa.run.json sg-succession.run.json sg-succession-cases.run.json `

the module's own #ASSERT directives were evaluated by the L4 evaluator and every result[] entry of kind 'assertion' is true with no entries of kind 'error'. The process exit code and the envelope's 'ok' field are BOTH ignored: measured, a failing #ASSERT yields ok:true and exit 0.

`assertions_total=131` · `module_origin=corpus`

> *claimed, not verified* (phase-script): these are the corpus's own committed assertions; no fork-discriminating tests exist at G1 because G1 does no encoding

---

## Every other stage that reported

The stages above are narrated under the heading they belong to. These are the rest — reporting stages, and anything added to the pipeline that has no heading of its own yet. They are here because the verdict gloss at the top of this report promises that every non-PASS receipt's reason appears below, and a stage with no site is how that promise quietly stops being true.

**`p8-verify`:** DEGRADED — the verifier ran over 6 corpus-origin module(s) and reported 1 propositional finding(s) across 79 analysed decision(s). Each finding names its decision, its site in the ladder, the atoms involved and what is wrong with it; see the .verify.txt artifacts. All 5 controls reproduced, so the checker was working when it said so — these are findings about the encoding, not about the harness.

`module_origin=corpus` · `sg-succession-domain.decisions=7` · `sg-succession-domain.analysed=2` · `sg-succession-domain.skipped=5` · `sg-succession-domain.nested_not_visited=0` · `sg-succession-domain.findings=0` · `sg-wills.decisions=70` · `sg-wills.analysed=21` · `sg-wills.skipped=49` · `sg-wills.nested_not_visited=2` · `sg-wills.findings=1` · `sg-isa.decisions=27` · `sg-isa.analysed=11` · `sg-isa.skipped=16` · `sg-isa.nested_not_visited=1` · `sg-isa.findings=0` · `sg-paa.decisions=142` · `sg-paa.analysed=44` · `sg-paa.skipped=98` · `sg-paa.nested_not_visited=99` · `sg-paa.findings=0` · `sg-succession.decisions=8` · `sg-succession.analysed=1` · `sg-succession.skipped=7` · `sg-succession.nested_not_visited=4` · `sg-succession.findings=0` · `sg-succession-cases.decisions=24` · `sg-succession-cases.analysed=0` · `sg-succession-cases.skipped=24` · `sg-succession-cases.nested_not_visited=0` · `sg-succession-cases.findings=0` · `controls_reproduced=5/5` · `decisions=278` · `analysed=79` · `skipped_non_boolean=199` · `nested_not_visited=106` · `findings=1` · `merged_atom_occurrences=1`

> *claimed, not verified* (phase-script): A clean run is a WEAK statement and the receipt refuses to imply otherwise. The analysis is propositional: every leaf (a projection, a comparison, an arithmetic test, a call to another DECIDE) is an opaque atom, so no numeric, interval, date or string contradiction is in range, and neither is anything that only appears once two named rules are unfolded against each other. Each DECIDE is read on its own. Findings are sound; silence is not a consistency proof. Full statement: l4 verify --help.

> *claimed, not verified* (phase-script): Rung 1 of 3. R5 (2026-08-02) ordered the P8 ladder as ROBDD first, the R4 fork-space agreement/divergence sweep second, an external model checker (TLA+/NuSMV/UPPAAL class) last. Rungs 2 and 3 are unbuilt: rung 2 needs the fork register P4 does not yet produce, rung 3 waits on the LTS semantics. 199 of 278 decisions are outside rung 1 entirely because they do not return BOOLEAN — they are counted, named in the artifact, and not reported as clean. A further 106 are outside it for a different reason: they are defined inside a WHERE clause, and neither this command nor the ladder's own entry point descends into one, so they are in NEITHER the analysed nor the skipped column. That is why the figure is on the receipt: 'analysed + skipped' does not total the corpus, and an exclusion nobody can size is an exclusion nobody believes.

**`p9-explain`:** SKIPPED — subject 'sg-succession' declares no 'explainer' section in subject.json, so it has no checked-in narrative to render. Declaring the directory is deliberate rather than discovered: a mistyped directory name would otherwise yield a fully-absent document with no error anywhere.

**`p9-report`:** PASS

Oracle (`structural`): `node etc/go/report/render-report.mjs $RUN --format md,html && every section SPEC.md §P9 requires is present`

the renderer reads journal.ndjson and nothing else, refuses a template containing a typed number, refuses an unresolved placeholder, and prints a chain-verification failure in the report itself; the section-presence check then confirms nothing §P9 requires was dropped

> *claimed, not verified* (phase-script): PASS here means the report accounts for everything the journal holds. It says nothing about whether the projections it describes are good.

> *claimed, not verified* (phase-script): this is the PRELIMINARY render, taken before this stage's own receipt and the run_end record exist. go.sh renders the final $RUN/report.md after run_end; it is derived rather than attested, and re-derivable by anyone with 'go.sh verify'.


---

## Where another system published its own representation of the same rule

**ABSENT.** SPEC.md §P9 requires a factual note of disagreement wherever another system has published its own representation of the same rule. No stage in this run wrote it; no stage in this milestone reads another system's representation. Making that comparison is R2's read-only probe, and any contact is HG2's subject.

---

## Triage

**ABSENT.** SPEC.md §8's triage table classifies each disagreement between the de novo encoding and the committed corpus as encoding error / genuine ambiguity / improvement over the hand corpus. No stage in this run wrote it; `p8-diff` — the stage that runs the diff oracle (`etc/go/lib/denovo-diff.mjs`) over the subject's declared surface map — has no receipt in this run. It is declared at milestone `g2`; a `g1` run replays one encoding and compares nothing.

---

## Every artifact this run put on disk

| stage | artifact | bytes (recorded) | sha256 (recorded) | state now |
| --- | --- | --- | --- | --- |
| `p0-preflight` | `probes.json` | 1742 | `sha256:a631abd51a44a1cc…` | on disk |
| `p0-preflight` | `cli-surface.txt` | 81 | `sha256:e20fc97289bb520e…` | on disk |
| `p0-preflight` | `tripwire.json` | 519 | `sha256:18cfd81f50506545…` | on disk |
| `p3-check` | `p3-check.txt` | 1330 | `sha256:794c24b0a3ebeebe…` | on disk |
| `p6-tests` | `p6-assertions.txt` | 885 | `sha256:f0b875430aa4a3ab…` | on disk |
| `p6-tests` | `sg-succession-domain.run.json` | 156 | `sha256:cf2ad27b2130853d…` | on disk |
| `p6-tests` | `sg-wills.run.json` | 9913 | `sha256:cd3e0dd46f148558…` | on disk |
| `p6-tests` | `sg-isa.run.json` | 142 | `sha256:9510077fe1e6d978…` | on disk |
| `p6-tests` | `sg-paa.run.json` | 13684 | `sha256:7af98eb66dcb1284…` | on disk |
| `p6-tests` | `sg-succession.run.json` | 149 | `sha256:827cde6f71d56756…` | on disk |
| `p6-tests` | `sg-succession-cases.run.json` | 10142 | `sha256:42ca86e0cc4baceb…` | on disk |
| `p8-verify` | `verify-clean.verify.json` | 649 | `sha256:d5ffffe086cc40ca…` | on disk |
| `p8-verify` | `verify-unsat.verify.json` | 720 | `sha256:8f32949572d71b19…` | on disk |
| `p8-verify` | `verify-dead-branch.verify.json` | 752 | `sha256:372a65d3c6ccda2c…` | on disk |
| `p8-verify` | `verify-vacuous-guard.verify.json` | 756 | `sha256:05045415b8d4df22…` | on disk |
| `p8-verify` | `verify-seam.verify.json` | 1431 | `sha256:139c94854caa3a27…` | on disk |
| `p8-verify` | `sg-succession-domain.verify.json` | 1360 | `sha256:e1ef357358cf5f11…` | on disk |
| `p8-verify` | `sg-succession-domain.verify.txt` | 3851 | `sha256:32fe5ffcfc23bcc4…` | on disk |
| `p8-verify` | `sg-wills.verify.json` | 10978 | `sha256:bc53b655b46ddb00…` | on disk |
| `p8-verify` | `sg-wills.verify.txt` | 12186 | `sha256:bff073646ee8757f…` | on disk |
| `p8-verify` | `sg-isa.verify.json` | 3910 | `sha256:96083a190819ba4a…` | on disk |
| `p8-verify` | `sg-isa.verify.txt` | 6068 | `sha256:84759bdda4c27540…` | on disk |
| `p8-verify` | `sg-paa.verify.json` | 20209 | `sha256:ed8efe16d1ba679c…` | on disk |
| `p8-verify` | `sg-paa.verify.txt` | 19894 | `sha256:b9343707916b68bf…` | on disk |
| `p8-verify` | `sg-succession.verify.json` | 1593 | `sha256:1aa873e83e807248…` | on disk |
| `p8-verify` | `sg-succession.verify.txt` | 4192 | `sha256:e5fa080b938c840b…` | on disk |
| `p8-verify` | `sg-succession-cases.verify.json` | 3748 | `sha256:f00f48e36d137e22…` | on disk |
| `p8-verify` | `sg-succession-cases.verify.txt` | 5910 | `sha256:62700b1b8b34a48f…` | on disk |
| `p8-verify` | `p8-verify.txt` | 1140 | `sha256:d696899442899a6d…` | on disk |
| `p7-lts` | `p7-lts.stderr` | 36 | `sha256:0d882bf9d3984abc…` | on disk |
| `p7-akn` | `sg-succession.akn.xml` | 50886 | `sha256:4281dc068d0e539c…` | on disk |
| `p7-akn` | `p7-akn.txt` | 99 | `sha256:4eb2c2d0efe987dd…` | on disk |
| `p9-report` | `report.md` | 16474 | `sha256:38fcd0d6f0adf4a9…` | on disk |
| `p9-report` | `report.html` | 16883 | `sha256:d0b87f418b046c84…` | on disk |
| `p9-report` | `p9-report.txt` | 242 | `sha256:3166c247a6f4f31a…` | on disk |

---

## How to re-derive this report without trusting it

```
etc/go/go.sh verify --run-id 2026-08-18-2b3f2400-002 --gates
```

That re-reads `journal.ndjson`, re-hashes every artifact a receipt names, checks
that each granted gate was recorded before the first stage it gates began (by
record of either kind, so gated work run outside the driver is caught), and
recomputes the milestone verdict. It runs no build, calls no model, and makes no
network request. A second party can run it later against the same run directory
and does not have to believe anything this report says.

*Generated by `etc/go/report/render-report.mjs` from `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-08-18-2b3f2400-002/journal.ndjson`. Nothing in this report was typed; every figure resolves from a journal row.*
