# Longlist: bodies of law worth encoding next

Candidates for a subject directory under `subjects/` and, once encoded, for a sidecar in
`l4-ide/etc/go/subjects/` so the "⟨body of law⟩: go" pipeline can run them. A row here is a
**nomination with its reason**, not a commitment: it leaves this file when a subject
directory exists for it (and says where it went), or when it is struck with a reason.

Rows carry the date they were added and who nominated them, because the reason for a
nomination goes stale faster than the law does.

| subject | jurisdiction | why it is on the list | reference material | added |
| --- | --- | --- | --- | --- |
| **SARA** — the nine Internal Revenue Code sections of the Statutory Reasoning Assessment (§§ 1, 2, 63, 68, 151, 152, 3301, 3306, 7703) | US, federal | The one public benchmark that ships a **logic-programming reference encoding** beside the statute: Holzenberger, Blair-Stanek & Van Durme, *A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering* (NLLP @ KDD 2020, arXiv:2005.05257), hand-encoded in Prolog with a few hundred entailment and numerical cases. That makes it a differential target for the Blawx and Prolog legs (a reference answer set already exists) and a comparison point against Jason Morris's Claude-assisted Blawx encoding of it, mentioned at the Blawx v3 webinar of 2026-09-02. Note: the dataset's own encodings are the authors' interpretation; the go pipeline's de novo discipline still applies. **The sharper reason (Matti Schneider, at the same webinar):** an encoding validated only by tests derived from the encoder's own reading of the statute can pass an unbounded number of tests and still be a misreading, because tests and encoding descend from one act of reading. SARA's cases are an **external** reference — written and answered independently of any encoding — which is the kind of validation our oracle-outside-the-artifact discipline (transpiler-level) cannot supply. That makes SARA the first subject on this list whose acceptance test is not something we could have generated ourselves. **Double-duty ruling (2026-09-03, session papers-kant):** SARA was absorbed into LegalBench (Guha et al. 2023, arXiv:2308.11462) as its SARA entailment/numeric tasks, so when the go pipeline runs SARA, also score and report in LegalBench task terms — external comparability against published per-task LLM numbers for free. The SARA run then decides whether LegalBench's other rule-application tasks earn a row of their own (see the strike note below). | Paper + dataset: https://nlp.jhu.edu/law/ | 2026-09-02, Meng (nominated during the Blawx v3 webinar) |

## Not on this list, and why

- **LegalBench wholesale** (Guha et al. 2023, arXiv:2308.11462 — 162 expert-built tasks over
  six types of legal reasoning). Considered and declined 2026-09-03 (session papers-kant): the
  great majority of its tasks are legal *reading* — classification, issue-spotting, rhetorical
  understanding — with no underlying rule to encode, so attempting it wholesale would measure
  the model, not the pipeline, and land us as one more row on an LLM leaderboard. Its
  **rule-application slice** (the SARA tasks, diversity jurisdiction, and kin — a crisp rule
  applied across hundreds of instances with published golds) *is* go-pipeline shaped and would
  fix the nine-item small-n weakness the Chubb replication reports, but it stays off the list
  until the SARA double-duty run (see SARA's row) reports back. Any slice adopted later owes a
  per-task gold audit first (dual-key discipline — feasible for three to six tasks, hopeless
  for 162) and carries maximal recall-contamination risk, the data being fully public since
  2023: frame any result as encoding fidelity at scale, never as novel capability.
- **Rock Paper Scissors Act** and **Beard Tax Act** (Blawx's running examples, Lexpedite/blawx
  v1.6.22 fixtures). Encoded in L4 on 2026-09-02 and run through `l4 blawx` both ways, but
  they are toy instruments that exist to exercise a backend, not law. They belong beside
  `alcohol.l4` as Blawx seeds in `l4-ide/jl4/examples/blawx/`, per the tools/law split in
  the README.
