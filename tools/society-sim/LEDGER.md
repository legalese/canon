# The requirement ledger

One file, across every Act: the questions the simulated Singapore asked that the encoding library could not answer. The simulation writes to it when adjudication runs out of law, proceeds on a declared assumption, and taints the trace. The encoding agent (for now, a person) reads from the top of it. An entry is closed when the run that raised it replays without tainting at that point.

- The ledger: [`subjects/sg/requirements.jsonl`](../../subjects/sg/requirements.jsonl), one JSON object per line, append-only except for status changes.
- The schema: [`ledger.schema.json`](ledger.schema.json), JSON Schema 2020-12.
- The checker: `python tools/society-sim/check-ledger.py` validates every line, checks ids are unique and subjects exist, and prints the open queue ranked.

The ledger is one file rather than one per subject because the encoding agent ranks across Acts, and because a single requirement often names more than one subject (two rows that disagree, or a regulation under one Act that another Act's row needs). Each subject's `NOTES.md` may point at its entries by id; the ledger does not point back.

## What an entry is

An entry is a **brief**, not a complaint. It must carry enough for an encoder who has never seen the simulation to do the work and to know when it is done:

| field | what it holds |
| --- | --- |
| `id` | `REQ-` and four or more digits, assigned in order, never reused |
| `raised` | the date the entry was first written, and `by`: `hand`, `encoder` (raised while encoding something else), `replay`, `simulation` or `lqa` |
| `status` | `open` → `claimed` → `satisfied`, or `declined` or `superseded`; see lifecycle |
| `kind` | which way the law ran out; one of the nine kinds below |
| `instrument` | the thing that needs encoding: its type, title, citation if known, the subject slug if one exists, and the provision |
| `question` | the question the simulation asked, written so that it makes sense **read on its own** with no other context |
| `trigger` | the event that raised it: the scenario event id if any, the date, the actor, the act, and the subjects the act engaged |
| `facts` | the record the adjudicator built and could not evaluate; what an encoder needs to write the first test |
| `expected` | the shape of the answer (`boolean`, `money`, `date`, `duration`, `status`, `enum`, `text`) and, where the raiser knows it, the assertion the scenario would make. This is the row's first test, inherited |
| `assumption` | what the simulation assumed in order to proceed, and the trace ids it tainted |
| `attach_to` | where the encoding goes: scope enlargement of an existing row, a fork in an existing row's register, a new row on an existing subject, a new subject, or an "as published" policy row |
| `count`, `first_seen`, `last_seen` | how often the same requirement has recurred; the simulation increments rather than duplicating |
| `priority` | an integer, lower is sooner. **1**: raised by a scenario, a replay or the simulation; these skip the queue. **2, 3, 4**: the three scheduled tiers of remaining Acts. The checker ranks ascending, then by count descending |
| `closes_when` | the closing condition, normally the seed and event at which the raising run must replay untainted |
| `resolution` | filled on close: the subject, row and commit that satisfied it, or the reason it was declined, or the id it was merged into |

## The nine kinds

| `kind` | meaning | usual `attach_to` |
| --- | --- | --- |
| `no-subject` | no directory under `subjects/` for the instrument at all | `new-subject` |
| `no-row` | the subject exists with a deposited source and no encoding row | `new-row` |
| `out-of-scope` | a row exists and its scope statement excludes the provision asked about | `scope` (enlarge the row) |
| `named-refusal` | the row refuses through a named `ASSUME` or `REFUSE`; the encoding is working as designed and the refusal names what is missing | `scope`, or `new-row` for the thing named |
| `supplied-fact` | the row answers, but only once given a figure that is really prescribed by subsidiary legislation (a rate, a cap, a sum, a threshold) | `new-row` for the instrument, under the parent Act's subject |
| `policy` | no legislative instrument exists; the answer is an administrative scheme as published | `policy-row` (an "as published" row in the manner of `sg/child-support`) |
| `case-law` | only a decision, or a common-law doctrine, settles the point | `fork` where the point is an interpretive choice in an existing row; `new-subject` for a doctrine with no statute |
| `cross-row` | two rows reach different answers to the same question | the fork register of each row; `resolution` records which reading was taken |
| `rule-version` | the question is dated before (or after) the version of the law the row states | `scope` (a dated arm) |

An entry whose kind cannot be settled is written as `unclassified` and is the first thing a human looks at.

## Lifecycle

```
open ──claim──▶ claimed ──row lands, replay clean──▶ satisfied
  │                 │
  │                 └──cannot be done as stated──▶ declined (reason)
  └──same requirement already open──▶ superseded (merged_into)
```

- **open**: written by the simulation or by hand. The simulation never writes a duplicate: if an open entry has the same `instrument` and `kind`, it increments `count` and moves `last_seen`.
- **claimed**: an encoder has taken it; `claimed_by` and `claimed_on` are set. The encoding agent works from the top of the ranked open queue.
- **satisfied**: the row (or scope enlargement, or fork resolution) is committed, and the run named in `closes_when` has been replayed and no longer taints at that trace. `resolution` names the commit. Satisfying an entry is a check, not an opinion.
- **declined**: the thing asked for is not law, cannot be encoded as stated, or is out of the library's remit. The reason stays on the entry; the simulation keeps tainting at that point, and the counter keeps counting, which is the honest state.
- **superseded**: merged into another entry; `merged_into` names it.

A satisfied entry is never deleted. The ledger is also the history of how the library grew and why.

## What the simulation must do when it writes an entry

1. Stop evaluating that question for that act, record the assumption it will proceed on, and mark the trace tainted. Taint propagates to every consequence derived from the assumed one.
2. Look for an open entry with the same `instrument` and `kind`; increment it if found, else append.
3. Carry on. The population does not wait for the law to be written.

LQA mode reads the same traces afterwards and writes its own incidents elsewhere. It does not write to this ledger, except to raise a `cross-row` or `named-refusal` entry it finds while reading.

## Seed entries

The first entries were written by hand from Simone's life (`subjects/sg/scenarios/cradle-to-grave-simone/GAPS.md`), one or two per kind, so that the shape of a good brief is on the record before the simulation writes any. Their `raised.by` is `hand` and their `closes_when` names the scenario event rather than a seed; when the replay exists, the entries should be re-raised by it and these superseded.
