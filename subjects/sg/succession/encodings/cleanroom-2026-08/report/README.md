# Reports — `cleanroom-2026-08`

One run, and two cost measurements that must not be added to each other.

| file                         | what it is                                                            |
| ---------------------------- | --------------------------------------------------------------------- |
| `go-run-report.md` / `.html` | the conversion report, rendered from the journal and nothing else     |
| `go-run-journal.ndjson`      | the hash-chained journal the report is rendered from                  |
| `go-run-cost-ledger.json`    | what the **pipeline run** cost — the ledger `p9-cost` built           |
| `cost-encoding-window.json`  | what the **encoding** cost — a second ledger over a hand-named window |
| `denovo-diff.md` / `.json`   | the §8 differential comparison against `../../legalese/`              |

## The run

`2026-08-26-3ab3039f-003`, over `legalese/l4-ide` tree `07e0a67d`. Verdict **COMPLETE**, which
is completeness of _accounting_ and not greenness: every declared stage has a receipt, no
receipt is broken, every non-PASS carries a reason, and every gate is signed or explicitly
waived. A run with every deposit absent would also be COMPLETE, over SKIPPED receipts.

**HG1 was WAIVED, not granted.** No signer is enrolled in the orchestrator's
`gate-allowed-signers`, which is the shipped state and deliberate — the orchestrator will not
invent an approver. The waiver text is in the report's Gates section, is recorded on the
journal, and binds to the deposit digest `sha256:3ab3039f…`: edit any of the ten files it covers
and the gate re-opens. What it waived is the one thing no script can do — a domain expert
reading the encoding against the four Acts, section by section.

Two stages are **DEGRADED** and both say why. `p8-verify` reported eight `unsat` findings, all
eight of them the abolition idiom described in `../NOTES.md`. `p7-dmn` refused to export a
module of bare `DECLARE`s, which is the §8.1 exhibit: a de novo encoding cannot yet ride the
committed corpus's projection suite.

## Re-deriving it without trusting it

From an `l4-ide` checkout at that tree, with the run directory:

```
etc/go/go.sh verify --run-id 2026-08-26-3ab3039f-003 --gates
```

It re-reads the journal, re-hashes every artifact each receipt names, checks that each gate was
recorded before the first stage it gates began, and recomputes the verdict. It runs no build,
calls no model, and makes no network request.

## Two cost ledgers, and why there are two

`p9-cost` clips to the run's own journal bracket — first record to last — and over that window
it reports **zero** model activity. That is correct and useless: the whole encoding happened
_before_ the driver was first invoked. The report says as much in its own words — the window
"misses what came before the driver was first invoked — reading the source, deciding what to
encode."

So `cost-encoding-window.json` is a second ledger over a window named by hand:
`2026-08-25T15:40:03Z` → `2026-08-26T01:27:00Z`, the four-Act run from the instruction that
started it to the end of the pipeline run.

|                   |                                   the encoding window |
| ----------------- | ----------------------------------------------------: |
| API requests      |                                                 4,930 |
| output tokens     |                          1,059,035 (83,027 reasoning) |
| cache reads       |                                           913,076,205 |
| network calls     | 1,142 in 55m 37s — 143 searches, 198 fetches, 801 MCP |
| workflow fan-outs |                                   6, across 84 agents |
| span              |            9h 47m, with an 8h 29m measured-busy floor |

## Two standings, never merged

**Attested** means the driver held the stopwatch: `go.sh verify` refuses any stage row claiming
more than a second beyond the interval between its own `stage_begin` and `stage_end`. The
per-stage timings in the report are attested; the whole pipeline run is 4m 10s.

**Attributed** means read out of the harness's JSONL transcripts. Nobody typed those numbers —
but a transcript is an ordinary file, so each of the 301 read is recorded with its sha256 and
byte count, and a second party can repeat the derivation or show that a file moved underneath
it. Both cost ledgers are attributed and say so in their own `standing` field.

**Averaging an attributed figure with an attested one collapses both to the weaker.** That is
the whole reason the split exists, and it is why the two ledgers here are separate files rather
than one total.

There is a third population, and it is separate again: the pipeline's **own** retrievals.
`source/fetch-sso.py` reports 14 HTTP requests over 7 documents, 2,153 ms, 3.66 MB. A `curl`
inside a shell call is invisible to a tool-name census of what the _model_ did, so those 14 are
never added to the 1,142.

## No money in the ledgers

Neither ledger here carries a dollar figure, and the report renderer emits none. Token counts
are facts about a run; prices are facts about a contract and change without notice, so a rate
table baked into a generated report goes stale silently — in a document whose whole premise is
that every number has a row behind it.

That is a rule about the _generated_ artifacts, not a prohibition on pricing. A reader with a
rate card can multiply, and the sibling `sg/child-support` deposit does exactly that in prose.
If you follow it, **date the rate card and say which one it was**: the multiplication is only
as good as the row it came from, and unlike the token counts it cannot be re-derived from the
transcripts later.
