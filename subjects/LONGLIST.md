# Longlist: bodies of law worth encoding next

Candidates for a subject directory under `subjects/` and, once encoded, for a sidecar in
`l4-ide/etc/go/subjects/` so the "⟨body of law⟩: go" pipeline can run them. A row here is a
**nomination with its reason**, not a commitment: it leaves this file when a subject
directory exists for it (and says where it went), or when it is struck with a reason.

Rows carry the date they were added and who nominated them, because the reason for a
nomination goes stale faster than the law does.

| subject | jurisdiction | why it is on the list | reference material | added |
| --- | --- | --- | --- | --- |
| **SARA** — the nine Internal Revenue Code sections of the Statutory Reasoning Assessment (§§ 1, 2, 63, 68, 151, 152, 3301, 3306, 7703) | US, federal | The one public benchmark that ships a **logic-programming reference encoding** beside the statute: Holzenberger, Blair-Stanek & Van Durme, *A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering* (NLLP @ KDD 2020, arXiv:2005.05257), hand-encoded in Prolog with a few hundred entailment and numerical cases. That makes it a differential target for the Blawx and Prolog legs (a reference answer set already exists) and a comparison point against Jason Morris's Claude-assisted Blawx encoding of it, mentioned at the Blawx v3 webinar of 2026-09-02. Note: the dataset's own encodings are the authors' interpretation; the go pipeline's de novo discipline still applies. | Paper + dataset: https://nlp.jhu.edu/law/ | 2026-09-02, Meng (nominated during the Blawx v3 webinar) |

## Not on this list, and why

- **Rock Paper Scissors Act** and **Beard Tax Act** (Blawx's running examples, Lexpedite/blawx
  v1.6.22 fixtures). Encoded in L4 on 2026-09-02 and run through `l4 blawx` both ways, but
  they are toy instruments that exist to exercise a backend, not law. They belong beside
  `alcohol.l4` as Blawx seeds in `l4-ide/jl4/examples/blawx/`, per the tools/law split in
  the README.
