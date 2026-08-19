# Reports

**Two reports, because "go" is not one run.** Each is an account of a single
*run*, and no single run exercises every stage of the pipeline:

| file | milestone | what it accounts for |
| ---- | --------- | -------------------- |
| `g1-replay-report.md` | G1 — the **replay** run | the committed corpus driven through every reachable projection: the house-style check, the 178 assertions, `l4 verify`, the MCP deployment, Akoma Ntoso |
| `g2-deposits-report.md` | G2 — the **de novo** run | the three deposits and the cross-file gate: the source bundle (P1), the external-modification sweep (P2), the fork register (P4), and P5's joins over all three |

Each has its hash-chained journal beside it; the report is rendered from the
journal and nothing else.

## Read them together, and mind the seam

Neither report is the whole account, and each will tell you so about the other's
half. The G1 report marks §P1 and §P2 **ABSENT** — correctly, because
`p1-ingest` and `p2-sweep` are not declared at G1, so that run neither performed
nor claimed an ingest. The G2 report marks `p3-check`, `p6-tests`, `p8-verify`
and `p8-diff` **SKIPPED** — correctly, because this subject declares no
`denovo.modules`.

**Why no `denovo.modules`:** SPEC.md §8's acceptance diff compares a de novo
encoding against a *previously committed* one. There is no prior Singapore
succession encoding, so there is nothing to diff, and a de novo module that IS
the corpus would make the comparison an identity (which the resolver refuses).
This is the first subject where "de novo" and "corpus" are the same encoding.

## A known limitation of this directory

A **subject-level** report — one document folding the latest evidence per stage
across runs, and marking any stage whose evidence predates the current corpus
digest as stale — does not exist yet. Until it does, the two files here are the
complete account, and reading only one of them will understate what was done.

The fold is not a simple union: a receipt binds to the corpus digest it ran
over, so evidence from two runs is only jointly meaningful when both ran over
the same corpus. Both reports here did — digest `951d08d8…` for G1 and the
deposit set for G2 — but nothing in this directory *checks* that, which is
exactly what a subject-level renderer would have to do.
