
# G2 conversion report — sg-succession

|             |                                                                                  |
| ----------- | -------------------------------------------------------------------------------- |
| run id      | `2026-08-19-e364a474-001`                                                                     |
| milestone   | G2 — the de novo run.                                |
| subject     | sg-succession                                                                  |
| repo HEAD   | `fdf2e1b3e19a0808460918375d3209198a5517af` (clean)                                         |
| clock       | `2025-01-31T00:00:00Z`                                                              |
| `l4` binary | `/Users/mengwong/src/legalese/l4wt/sg-succession/dist-newstyle/build/aarch64-osx/ghc-9.10.3/jl4-0.1/x/l4/build/l4/l4`                                                              |
| journal     | `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-08-19-e364a474-001/journal.ndjson` — 25 records, chain verifies |
| verdict     | **COMPLETE**                                                              |

> COMPLETE means every declared stage has a receipt, no receipt is BROKEN, every non-PASS receipt carries a reason that appears below, and every gate is signed or explicitly waived. It is completeness of accounting, NOT greenness: legs below may report NOT-EXECUTABLE, DEGRADED or NOT-REGENERATED, and each says why.

---

## Gates

| gate | state | how |
| --- | --- | --- |
| HG1 | waived | **waived**: NOT REVIEWED. Registering the P1/P2/P4 deposits that were built and hand-validated but never given receipts. |

---

## What the source said

**PASS**

Oracle (`structural`): `node etc/go/lib/register-validate.mjs source-bundle /Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/source-bundle.json (+2 peer deposit(s))`

the validator models the bundle's semantics rather than its syntax: it audits the schema before using it and refuses any keyword it does not implement, it enforces 49 declared cross-field rules whose ids must match its implementations in both directions, and it re-hashes every captured document that names a local_path. It does NOT establish that the fetched text is the law, that the capture is current, or that the annotation inventory is complete — the schema records the last of those as a self-declared flag, which is exactly why P2's disposition join exists.

`deposit=/Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/source-bundle.json` · `peers_present=2` · `rules_checked=49` · `joins_skipped=1`

> *claimed, not verified* (phase-script): 1 cross-file join(s) could not run because a peer deposit is absent; the artifact reports each as 'skip' with its reason, never as a pass

> *claimed, not verified* (phase-script): whether the bundle is the RIGHT text — the correct point-in-time version, the whole of the subject, the amendment layers SPEC.md §4 P1 names — is unverified by this stage; the schema can only check that what was recorded is internally coherent and hashes as claimed

---

## What the external-modification sweep searched and surfaced

**PASS**

Oracle (`structural`): `node etc/go/lib/register-validate.mjs external-modifications /Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/external-modifications.json (+2 peer deposit(s))`

49 declared cross-field and cross-file rules ran over the register and its peers, including the searched-vs-found joins that make SPEC.md §4 P2's 'what was searched, not only what was found' checkable, the routing rules that force a binding modification to name where it landed in the encoding, and — when the P1 bundle is present — the completeness join over the bundle's annotation inventory. It does NOT establish that the sweep was thorough: no procedure enumerates the searches that should have been run.

`deposit=/Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/external-modifications.json` · `peers_present=2` · `rules_checked=49` · `joins_skipped=1` · `searches=3` · `entries=4` · `dispositions=3`

> *claimed, not verified* (phase-script): 1 cross-file join(s) could not run because a peer deposit is absent — most importantly 'annotation-inventory-disposed', which is the BNA C2 defect turned into an exit code and needs the P1 bundle. The artifact reports each as 'skip' with its reason, never as a pass

> *claimed, not verified* (phase-script): 3 search(es) and 4 finding(s) are recorded here; whether that sweep was WIDE ENOUGH is unfalsifiable by construction and is HG1's, and a register that searched nothing validates exactly as cleanly as one that searched everything

---

## What the encoding decided

**Encoding (de novo):** SKIPPED — the 'sg-succession' sidecar declares no denovo.modules, so this subject has nowhere to deposit a de novo encoding. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; the paths' existence is optional, because writing the L4 is agent work owned by the G2 section of .claude/skills/running-the-l4-pipeline/SKILL.md and by the writing-l4-rules skill.

**Ambiguity forks:** PASS

Oracle (`structural`): `node etc/go/lib/register-validate.mjs fork-register /Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/fork-register.json (+2 peer deposit(s))`

49 declared rules ran, and they model R4's ruled representation rather than the file's syntax: the 1:1 map between a materialised fork and an Interpretation field is enforced in both directions, the reading taken must be one of the register's own live readings, a non-live reading must explain itself, a live reading must cite the text that licenses it, and an observable divergence must name a witness. It does NOT establish COMPLETENESS — 7 fork(s) are recorded and nothing here says that is all of them.

`deposit=/Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/fork-register.json` · `peers_present=2` · `rules_checked=49` · `joins_skipped=1` · `forks=7` · `materialised=2` · `settled_by_authority=2` · `with_witnesses=6`

> *claimed, not verified* (phase-script): 1 cross-file join(s) could not run because a peer deposit is absent — including 'cross-refs-resolve', which is how a fork an authority has already settled proves it cites a real P2 entry rather than presenting as open. The artifact reports each as 'skip', never as a pass

> *claimed, not verified* (phase-script): fork-register completeness — that every ambiguity in the source was found — is unfalsifiable by construction and is carried by HG1 (SPEC.md §7.3). This stage's PASS means the 7 recorded forks are internally coherent and cross-reference resolvably, and nothing about the ones nobody noticed

**Adversarial gate (mechanisable half):** PASS

Oracle (`structural`): `node etc/go/lib/register-validate.mjs external-modifications /Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/external-modifications.json /Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/source-bundle.json /Users/mengwong/src/legalese/l4wt/sg-succession/jl4/examples/legal/sg-succession/denovo/fork-register.json`

49 declared rules ran across all three de novo deposits with every peer present, which is what makes SPEC.md §4 P5's third check — 'disposition of every entry in P2's external-modification register (consumed by the encoding, consumed by a fork, or explicitly deferred with a reason)' — an exit code: 'annotation-inventory-disposed' joins the disposition table against the bundle's declared-complete annotation inventory, 'fork-refs-resolve' and 'cross-refs-resolve' check the register/fork cross-references in both directions, and the routing rules force a binding modification to name where it landed. Two of P5's five checks are discharged elsewhere (p3-check), and two are not discharged at all — see the notes.

`deposits=3` · `rules_checked=49` · `joins_skipped=1`

> *claimed, not verified* (phase-script): 1 join(s) still reported 'skip' with all three deposits present. That should not happen — every cross-file rule's peer is on the command line — so read it as a defect in this stage's peer assembly rather than as coverage

> *claimed, not verified* (phase-script): CARRIED BY HG1 — fork-register completeness. No procedure establishes that every ambiguity in the source was found, so the register is checked for internal and cross-file consistency and never for exhaustiveness. SPEC.md §7.3; ORCHESTRATOR.md §5.2

> *claimed, not verified* (phase-script): CARRIED BY HG1 — isomorphism spot-checks against the source text. SPEC.md §4's P3 deliverable is 'a domain expert can review it against the regulation section by section', which has no checkable form; this stage does not attempt one

> *claimed, not verified* (phase-script): this PASS is NOT the P5 gate. SPEC.md §4's P5 condition is 'independent adversarial review is satisfied the encoding is as good as it can be' — a judgement, held by HG1. What passed here is the mechanisable third of its checklist

**What was checked about the committed encoding:** SKIPPED — the 'sg-succession' sidecar declares no module set for this milestone's origin (denovo: denovo.modules), so there is nothing to hold the P3 house rules against. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; writing the module is agent work.

---

## What each projection preserved and lost

| leg | status | oracle class | what it says |
| --- | --- | --- | --- |
| `p7-dmn` | SKIPPED | none | the 'sg-succession' sidecar declares no denovo.modules, so there is no de novo module to emit DMN from. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; writing the module is agent work. |

### `p7-dmn` — SKIPPED

the 'sg-succession' sidecar declares no denovo.modules, so there is no de novo module to emit DMN from. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; writing the module is agent work.

**Oracle:** none ran.


---

## Test results

**SKIPPED** — the 'sg-succession' sidecar declares no module set for this milestone's origin (denovo: denovo.modules), so there are no committed #ASSERT directives to run. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; writing the module is agent work.

---

## Every other stage that reported

The stages above are narrated under the heading they belong to. These are the rest — reporting stages, and anything added to the pipeline that has no heading of its own yet. They are here because the verdict gloss at the top of this report promises that every non-PASS receipt's reason appears below, and a stage with no site is how that promise quietly stops being true.

**`p8-verify`:** SKIPPED — the 'sg-succession' sidecar declares no module set for this milestone's origin (denovo: denovo.modules), so there is nothing to verify. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; writing the module is agent work.

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

**`p8-diff`:** SKIPPED — the 'sg-succession' sidecar declares no denovo.surface_map, so the §8 comparator has no pairing declaration to run over. Add it to /Users/mengwong/src/legalese/l4wt/sg-succession/etc/go/subjects/sg-succession/subject.json; writing the map (which decisions correspond, over which shared fact slots) is agent work owned by the skill's G2 section and DENOVO-DIFF-ORACLE.md.

---

## Every artifact this run put on disk

| stage | artifact | bytes (recorded) | sha256 (recorded) | state now |
| --- | --- | --- | --- | --- |
| `p1-ingest` | `p1-ingest-validate.txt` | 604 | `sha256:b67b0974924ea4cf…` | on disk |
| `p2-sweep` | `p2-sweep-validate.txt` | 604 | `sha256:21fc9bfa36e2adc8…` | on disk |
| `p4-forks` | `p4-forks-validate.txt` | 604 | `sha256:fe68c532cf68a17c…` | on disk |
| `p5-gate` | `p5-gate.txt` | 604 | `sha256:21fc9bfa36e2adc8…` | on disk |
| `p9-report` | `report.md` | 13339 | `sha256:6a5a9eb77d5d3b16…` | on disk |
| `p9-report` | `report.html` | 13700 | `sha256:998e3f41ced3c140…` | on disk |
| `p9-report` | `p9-report.txt` | 242 | `sha256:c25f62eb35185257…` | on disk |

---

## How to re-derive this report without trusting it

```
etc/go/go.sh verify --run-id 2026-08-19-e364a474-001 --gates
```

That re-reads `journal.ndjson`, re-hashes every artifact a receipt names, checks
that each granted gate was recorded before the first stage it gates began (by
record of either kind, so gated work run outside the driver is caught), and
recomputes the milestone verdict. It runs no build, calls no model, and makes no
network request. A second party can run it later against the same run directory
and does not have to believe anything this report says.

*Generated by `etc/go/report/render-report.mjs` from `/var/folders/jv/4t5pmlz5563gttw9cxqlx5k00000gp/T/l4-go/2026-08-19-e364a474-001/journal.ndjson`. Nothing in this report was typed; every figure resolves from a journal row.*
