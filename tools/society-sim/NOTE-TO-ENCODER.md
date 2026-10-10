# Note to the encoding session

From Michael, 10 October 2026. Read this before the next encoding.

**From now on, take your encoding priority from the requirement ledger**, not from `sg-candidates.json` or the tier list on its own. The ledger is one file, `subjects/sg/requirements.jsonl`, one JSON object per line, described in [`LEDGER.md`](LEDGER.md) and validated by `python tools/society-sim/check-ledger.py`, which also prints the open queue in the order you should work it.

## What is in it now

Eighteen entries, all at **priority 1**, written by hand from the cradle-to-grave scenario at `subjects/sg/scenarios/cradle-to-grave-simone/`. Each is a brief: the Act or instrument, the provision, a question that stands alone, the facts the simulation had, the answer it expected, and where the encoding attaches (enlarge an existing row's scope, resolve a fork, add a row, add a subject, or write an "as published" policy row). Priority 1 means it was raised by a life, and it skips the queue.

## What you should add

Your schedule of roughly 250 remaining Acts in three tiers goes into the same ledger as 250 lines, one per Act, with **priority 2, 3 or 4 by tier**. Use this shape, one line each, ids continuing from `REQ-0019` in order:

```json
{"id": "REQ-0019", "raised": {"on": "2026-10-11", "by": "encoder"}, "status": "open", "kind": "no-row", "instrument": {"type": "act", "title": "Feeding Stuffs Act 1965", "subject": "feeding-stuffs-act-1965"}, "question": "What does the Feeding Stuffs Act 1965 decide for a person or business it applies to? Scheduled naive encoding, tier 2; refine this question when a scenario asks one.", "trigger": {"date": "2026-10-11", "act": "scheduled naive encoding of the remaining Acts, tier 2"}, "expected": {"shape": "unknown"}, "attach_to": {"how": "new-row", "subject": "feeding-stuffs-act-1965"}, "count": 1, "first_seen": "2026-10-11", "last_seen": "2026-10-11", "priority": 2, "closes_when": {"text": "A row exists under the subject's encodings/ with an encoding.json, NOTES.md and passing cases."}}
```

The checker requires the `subject` slug to be a directory under `subjects/sg/`; every remaining Act already has one. Keep one object per line, never reorder or renumber, and run the checker before you commit. Generate the 250 lines with a script rather than by hand.

## How to work the queue

1. Run the checker. Take the first open entry. Priority 1 before 2 before 3 before 4; within a priority, the higher `count` first.
2. Set `status` to `claimed`, with `claimed_by` and `claimed_on`, and commit that change before you start, so a second session does not take the same entry.
3. For a priority-1 entry, read `question`, `facts` and `expected` first. The `expected.assertion` is the row's first test: add it as a case in the row's case file, in the scenario's own facts. `attach_to.how` tells you whether you are enlarging a row's scope, resolving a fork in its register, or adding a row or subject. Where the note says a citation is from memory, confirm it on SSO before encoding from it.
4. When the row or enlargement is committed, set `status` to `satisfied` and fill `resolution` with `on`, `subject`, `row` and `commit`. Until the simulation's replay exists, the closing check is: the row's cases pass, and the scenario's `check-status.py` would now classify that event's law as encoded. When replay exists, an entry is satisfied only when the replay named in `closes_when` no longer taints at that point.
5. If an entry cannot be done as stated (not law, no deposited source, or the instrument does not exist), set `status` to `declined` with `resolution.reason`. Do not delete it.
6. If, while encoding, you find the Act leaves the answer to a regulation, an order or a case, **raise a new entry** for it: `raised.by` is `encoder`, kind `supplied-fact`, `case-law` or `policy` as fits, priority 1 if a scenario needs it, otherwise 2. This is how the ledger learns about subsidiary legislation the Acts point at.

## Two conventions that differ from before

- **Scope is whatever the library holds.** A naive row's scope statement is the contract the simulation reads. Keep saying exactly what is in and out, as the rows already do; the ledger's `out-of-scope` kind depends on it.
- **The ledger change goes in the same commit as the row.** A row without its ledger line closed, or a line closed without its row, is a defect in the ledger.

## What not to do

Do not edit the scenario files under `subjects/sg/scenarios/`; they are the simulation's regression suite and are changed by the scenario's author. Do not change ids, delete entries, or re-prioritise another entry to move your own up. Do not write rules in anything but L4: the simulation calls the rows directly, and anything encoded elsewhere is invisible to it.
