# Reports — `cleanroom-2026-08`

One run, and two cost measurements that must not be added to each other.

| file                         | what it is                                                              |
| ---------------------------- | ----------------------------------------------------------------------- |
| `go-run-report.md` / `.html` | the conversion report, rendered from the journal and nothing else       |
| `go-run-journal.ndjson`      | the hash-chained journal the report is rendered from                    |
| `go-run-cost-ledger.json`    | what the **pipeline run** cost — the ledger `p9-cost` built             |
| `cost-encoding-window.json`  | what the **encoding** cost — a second ledger over a hand-named window   |
| `denovo-diff.md` / `.json`   | the §8 differential comparison against `../../legalese/`                |
| `TRIAGE.md`                  | a PROPOSED reading of the five divergences — not a ruling, not evidence |

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

## Priced at list — a dated snapshot

Neither ledger carries a dollar figure and the report renderer emits none, because token counts
are facts about a run while prices are facts about a contract. So the multiplication is done
here, once, **dated**, and never folded back into the ledgers.

Rates are Anthropic's published list prices for `claude-opus-5`, read **26 August 2026** from
<https://platform.claude.com/docs/en/about-claude/pricing>: $5/MTok base input, $6.25/MTok
5-minute cache write, $10/MTok 1-hour cache write, $0.50/MTok cache hit, $25/MTok output, web
search $10 per 1,000, web fetch free beyond tokens.

| line                            |       tokens | rate          |        cost | share |
| ------------------------------- | -----------: | ------------- | ----------: | ----: |
| Cache reads (hits)              |  913,076,205 | $0.50 / MTok  | **$456.54** | 65.9% |
| Cache writes (1 h TTL)          |   20,845,520 | $10.00 / MTok | **$208.46** | 30.1% |
| Output — incl. 83,027 reasoning |    1,059,035 | $25.00 / MTok |  **$26.48** |  3.8% |
| Web search                      | 143 searches | $10 / 1,000   |       $1.43 |  0.2% |
| Fresh (uncached) input          |        9,860 | $5.00 / MTok  |       $0.05 |  0.0% |
| **Total**                       |              |               | **$692.95** |       |

That is **2.5¢ per committed line** of 27,515, **$0.36 per assertion** of 1,907, and about **$71
an hour** across the 9h47m span. The whole session — everything this context ever did, including
building and repairing the cost machinery — prices at **$1,554.81**.

**This is the one figure here that cannot be re-derived.** The tokens can be recomputed from the
transcripts at any time; the rate card cannot be recovered from anything once it changes. Treat
the dollars as a third standing — call it _quoted_ — weaker than attributed, and never merge it
into either ledger.

### Four things that move it

- **The 1-hour cache TTL.** At the 5-minute TTL ($6.25/MTok) the identical run prices at
  **$614.78**. Nothing about the work changes; only the row you multiply by.
- **The fan-outs are 85% of it** — $590.42 of $692.95 across six workflows and 84 agents. Their
  window figures are a strict subset of the window's line by line (87.5% of requests, 84.7% of
  cache reads, 69.6% of output tokens), so the costs nest. Per agent they range from $2.33 to
  $21.32, and the **51-agent** fan-out is the cheapest of the six per agent while the **5-agent**
  one is the dearest. Head count is close to useless as a cost estimator. Why is NOT established
  here: six fan-outs, each a different task, cannot separate context-carried from task length.
- **Never sum a transcript naively.** Measured on this window: 9,777 usage-bearing rows carry
  only 4,930 distinct requests, because one API response is written as several records that each
  repeat the same `usage`. A naive sum prices this run at **$1,433.02** against the true
  **$692.95** — **2.07x**, in the confident direction. The factor is not uniform, so no single
  fudge rescues it: output over-reports by 5.93x, cache writes 2.14x, cache reads 1.82x. (A note
  in `l4-ide` quotes 2.2x from a _different_ session; that is not this number.)
- **What is not in it.** No domain-expert review — HG1 was waived, and reading 27,515 lines
  against four Acts is the expensive part that has not happened. No human drafting time, no
  deployment.

### An intuition this pair of deposits retires

The obvious guess is that a shorter session is cheaper per unit of output, since cache reads
scale with how long a context has been alive. The two deposits under `sg/` say otherwise: the
`child-support` run priced at **3.5c/line** over 90 minutes, this one at **2.5c/line** over
9h47m. The long session was the cheaper one per line. Two runs of different subjects prove
nothing on their own — but they are enough to stop asserting the opposite, and the plausible
reason is that a cache paid for once amortises over everything after it.

### What the same work costs on a subscription

The figures above are what these tokens would cost **at API list**. The work was not bought that
way: it ran on a Claude Max 20x subscription, and the two prices are far apart.

**The 25% is a recollection, and it is the only unmeasured input on this page.** The operator's
estimate is that this work consumed about a quarter of one weekly quota. Nothing measures that —
Anthropic does not publish how subscription quota is metered, and no artifact in this deposit
records quota consumption — so it is recorded here as an impression, clearly marked, and every
figure derived from it inherits that standing.

At $200/month (the operator's own billed rate, not a figure read off a page) and four weeks to a
month, a weekly quota is $50 and a quarter of it is **$12.50**:

| basis                         |   cost | ratio to the $692.95 at list |
| ----------------------------- | -----: | ---------------------------: |
| 25% of a weekly Max 20x quota | $12.50 |                      **55×** |

Two independent things make the 25% look plausible rather than merely recalled. The run spanned
9h47m with an 8h29m measured-busy floor, against widely-reported (not published) Max 20x weekly
allowances in the range of a few tens of Opus hours. And that floor is a **union** — summed across
the 84 agents that ran concurrently, Bash alone accounts for 12h43m — so whatever the metering
unit, fan-out consumes more of it than wall clock suggests, and 25% may be an underestimate.

**Why this workload flatters the subscription so much.** 96% of the API bill is cache mechanics:
66% cache reads, 30% cache writes, and only 3.8% output. That is close to the most cache-read-heavy
shape a workload can have — a long-lived context re-reading a large worktree. A short,
output-heavy job would show a much smaller gap. Do not generalise 55x to "Claude work is 55x
cheaper on a subscription"; generalise it to "this shape of work is."

**Three things that would move it:**

- Claude Code weekly limits were running with a **50% boost through 31 August 2026**. A quarter of
  a temporarily enlarged quota is a larger share of an ordinary one.
- The metering unit is unpublished. If quota meters on something nearer compute-time than cached-token
  price, the ratio is an artifact of that mismatch and not a discount.
- The two prices buy different things. API list is uncapped, programmatic, no session window and no
  weekly cliff; a subscription is capacity-constrained and rate-limited. This is a real gap, not an
  arbitrage.

This is the second priced run in `subjects/sg/`. The first, `child-support`, did not record a
subscription comparison; if a third does, these three lines are the beginning of a series worth
plotting rather than three anecdotes.

### If you price a run yourself

Date the rate card and say which one it was. Unlike every other number in this directory, the
multiplication cannot be checked later against anything.
