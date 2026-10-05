# Independent test report — Apportionment Act 1928

Expectations were decided from `../source/AA1928.txt` and `BRIEF.md` alone and written down in
`independent-expectations.md` before any `.l4` was opened. Tests: `tests-independent.l4`.
Run: `~/.local/bin/l4 run tests-independent.l4` from this directory (JL4_LIBRARY_PATH unset).

## Counts

| | |
|---|---|
| assertions | 37 |
| satisfied | 36 |
| failed (`assertion failed`) | 1 |
| parse / type / other errors | 0 |

## Failure

### F-1 — s 5(2) for rent on land whose payment has *determined*

- Assertion (line 100):
  `` #ASSERT `the route for recovering the apportioned part of` `dead rent due 30 Jun` EQUALS `by suit against the person entitled to the entire rent, not against the tenant or the land` ``
- Provision: s 5(2) — "Persons liable to pay rents reserved out of or charged on lands or
  tenements, and the same lands or tenements, shall not be resorted to for any such apportioned
  part forming part of an **entire or continuing** rent as aforesaid specifically, but the entire or
  continuing rent, including such apportioned part, shall be recovered and received by the person
  who, if the rent had not been apportionable ..., would have been entitled to the entire or
  continuing rent, and the apportioned part shall be recoverable from such person by the executors
  or other parties entitled under this Act to the same by suit."
- Expected (my reading R5): rent reserved out of or charged on land, in state "determined by
  re-entry, death or otherwise", goes the s 5(2) route. "Entire or continuing" is disjunctive:
  "continuing" matches s 4(a), "entire" matches the s 4(b) case where the *next entire portion*
  still falls to be paid (classically, the life tenant-landlord dies; the lease runs on and the
  remainderman receives the entire rent at the next gale day; the life tenant's executors sue the
  remainderman).
- Produced: `the same remedies as for the entire portion` (s 5(1)). The encoding's FORK F2
  restricts s 5(2) to `continuing` payments, reasoning that where the rent has determined no one
  receives a later entire rent.
- Assessment: **genuinely ambiguous, leaning encoding too narrow.** The encoding's single
  `state` field conflates two things: whether the *rent* (the lease) determined, and whether the
  *interest of the person entitled* determined (death of a life-tenant landlord). In the death
  case — expressly contemplated by s 4(b) ("determined by ... death") and s 5(1) ("persons whose
  interests determine with their own deaths") — there plainly is a later entire rent received by
  someone, and the word "entire" in s 5(2) only does work if s 5(2) covers that case. Where the
  lease itself ends by re-entry the encoding's reading is defensible. Suggest splitting the fact.

## Expectations I could not express against the encoding's names

- A2/A3/A5/A6/A8/A9/A11 (oral rent; payment in lieu of rent; salary; pension; bonus out of
  revenue; dividend not at fixed times) — the encoding takes the s 2 classification as an input
  (`kind`), so these definitional limbs are not decided by the encoding; tested only by the kind.
- D8 (no remedy before the s 4 date) — no rule joins s 5 remedies with the s 4 date; tested only
  via `is payable on`.
- Claimant `someone else` is an encoder addition, not tested.
- s 5(1) "allowing proportionate parts of all just allowances" — I wrote no expectation; all my
  fixtures use 0 allowances.
- Day count: the encoding's F1 (days = cut-off − start; period = end − start) agrees with my R1;
  all arithmetic tests passed. Cut-off outside the period refuses — not contradicted by the Act.


## Triage by the encoder (2026-10-05)

- **F-1 (s 5(2), determined rent on land): accepted, encoding changed.** On re-reading, "an entire or continuing rent" is disjunctive, and reading it as continuing rent only left "entire" with nothing to do. Fork F2 was reversed in `aa-act.l4` and `NOTES.md`. `aa-tests.l4`'s own assertion, which expected s 5(1) under the first reading, was changed with that reading and says so in a comment. This assertion now passes: 37 of 37.
- The untestable points are accepted as scope: the s 2 classification is an input (`kind`), and the s 5/s 4 join is a reading a caller makes from the two rules.
