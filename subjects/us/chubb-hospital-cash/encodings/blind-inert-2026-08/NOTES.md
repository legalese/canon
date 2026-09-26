# Notes — blind-inert-2026-08

**Status: `experimental`.** This is the first row in the corpus to carry that status rather than
`draft`, and the difference is deliberate. A `draft` row encodes real law and is unfinished. This row
encodes an instrument that **was never law at all**, and exists to support a measurement. Do not
promote it to `draft` by analogy with the rows beside it.

## 1. What this is, and what it is not

The subject is a **synthetic** supplemental hospitalization cash policy. The insurer
("CODEX INSURANCE LIMITED") is fictional. Nobody has ever been covered by it, no claim has ever been
made under it, and no court has ever construed it. It was written by researchers as a teaching and
benchmarking target and it is filed here because it is a body of contractual rules that has been
encoded — not because anyone is subject to it.

It is here to support a replication of **Kant et al. 2025** (arXiv:2502.17638), which measured how
accurately LLMs translate this policy into Prolog, scoring against a nine-item answer key the paper's
own authors wrote. We re-ran that with L4 as the target.

## 2. The source text has been modified, and the modification matters

The text encoded here is the variant printed at arXiv:2502.17638 Appendix A.1. Verified line by line
against the original at PMC10894687 on 2026-08-31, it differs in two ways:

| original (Goodenough & Carlson 2024, App. A) | as encoded here |
| --- | --- |
| **§2 BENEFITS** — 2.1 the operative grant ("If you have been confined in a hospital as a result of sickness or accidental Injury, we will pay you the Daily Hospital Income Benefit shown in §5"), 2.2 the 24-hour / 365-day / **United States** limits, 2.3 the claim requirement | **absent entirely** |
| §3 GENERAL EXCLUSIONS, items (a)–(e), age **≥ 75** | renumbered §2.1, items 1–5, age **≥ 80** |
| §4 GENERAL CONDITIONS | renumbered §3 |
| **§5 BENEFIT AND PREMIUM AMOUNTS** ($500/day, $2,000 premium) and **§6 SIGNATURE** | **absent** |

Two consequences a reader must know before trusting anything computed here:

**There is no insuring clause.** The removal of §2.1 leaves the document with no operative promise to
pay. Everything this encoding decides is therefore about *whether the policy is in effect and no
exclusion bites* — never about whether a benefit is actually owed, because the modified text never
says one is. The encoding names this rather than papering over it.

**Two cross-references dangle.** §1.2 ("the policy term described in Section 5 below") and §3.5.1
("The premium described in Section 5 below") both point at a section that is not in the document. In
the original they resolve. They are encoded as they stand, with the dangling reference recorded.

The age change is *not* a defect: Goodenough & Carlson explicitly describe the top permissible age as
one of the illustration's "moving parts that can be varied". Changing it is using the artifact as
designed. The excision of §2 is a different matter and is not flagged anywhere in the citing paper.

## 3. How this encoding was produced, and what "blind" means

Three encodings were written independently, by three agents in three house styles, **each shown only
the policy text** — not the nine benchmark questions, not the answer key, not each other's work. The
questions were mapped onto each encoding afterwards by a different agent, also blind to the key.

This row is the inert-style arm, ranked first of the three on isomorphism by the reviewing auditors.
Its sibling `blind-guarded-2026-08` is the third-ranked arm, deposited because the *comparison* is
the evidence.

**"Blind" is true of the rules, not of the whole file.** `chubb.l4` is the blind encoding
byte-for-byte through line 526; the remaining 237 lines are a benchmark-scenario section appended
afterwards *with the key in hand*, whose own header says so. No rule was changed — the nine answers
are the blind arm's, re-executed to confirm — but the file as committed is not itself a blind
artifact and should not be described as one.

## 4. What it answers, and where it disagrees with the published key

All three arms answer **No / Yes / Yes / Yes / No / No / Yes / No / Yes** to the paper's nine
queries: 8 of 9 agreement, with one unanimous disagreement.

**Q4 is the disagreement, and we think the key is contestable rather than the encoding wrong.** The
query asks about a hospitalization "due to a fall while traveling abroad" where wellness-visit
confirmation was given at month 8 — but **never says when the hospitalization occurred**, and clause
1.1 makes that the operative moment ("the policy being in effect *at the time of the
hospitalization*"), with 1.1(3) satisfied while the 1.3 condition "is still pending". Before month 7
the claim is good; after, it is not. The encodings applied the benchmark's own stated preamble — set
unreferenced facts favourably — and got "Yes". The counter-argument is grammatical (the pluperfect
sequences the confirmation before the hospitalization), which comes from the tense of the question
rather than from the policy.

**Q5 is worse and we did not disagree with it, which is itself worth recording.** Every arm answered
"No", matching the key — but reached it by *marshalling*, not by a rule: the fact record was given a
ground meaning "neither sickness nor accidental injury". Typed instead as an accidental injury, the
same encoding returns the opposite. So on Q5 the benchmark scores the fact-supply step, not the
encoding. An independent audit rated the published Q5 label **not defensible** on the modified text,
partly because the clause it depends on is the one that was deleted (§2).

## 5. What this row does NOT carry

- **No HG1.** The l4-ide pipeline run behind this encoding carries HG1 **WAIVED**, not granted. No
  domain expert has read it clause by clause against the source. That is precisely what HG1 asks for.
- **No `cases/`, `projections/`, `report/` or `gates/` directories.** The pipeline artifacts live in
  `legalese/l4-ide` and were not copied here.
- **No rule-version axis, no dated arms.** A synthetic instrument has no amendment history.
- **No DMN projection.** The exporter emits two classes of non-FEEL text that both KIE and Camunda
  refuse to load; see l4-ide's `p7-dmn` finding. Nothing DMN-shaped here would be trustworthy.

## 6. Goldens are a point-in-time record

The four goldens per module travel with the row, but **canon has no CI** and these modules are
outside l4-ide's corpus globs, so nothing here regenerates or re-checks them. They record what the
toolchain produced on 2026-08-31 and will silently rot as the language moves. The live copies are in
`legalese/l4-ide` at `jl4/examples/legal/chubb/`, where `jl4-test` does defend them.

**This row is a copy, not the only copy** — the same convention as `sg/succession`, whose `.l4` files
are byte-identical across both repositories. The l4-ide copy is what the `chubb` go.sh subject
declares as its corpus, so deleting it there would break that subject.

## 7. The choice-of-law contradiction in the source

Clause 3.3.1 elects **New York** law. Clause 3.2.1 requires arbitration under **the Arbitration Act
(Cap. 10)** — a *Singapore* statute — in a policy that also mandates payment in US currency. This is
a defect in the source document, faithfully preserved. It is why this row is filed under `us/` with
an `extent` field that explains itself rather than asserting a clean jurisdiction.
