# Independent test report — Notaries Public Act 1959

Expectations were decided from `../source/NPA1959.txt`, `PROVENANCE.md` and `BRIEF.md` alone and
written down in `independent-expectations.md` before any `.l4` was opened. Tests:
`tests-independent.l4`. Run: `~/.local/bin/l4 run tests-independent.l4` from this directory
(JL4_LIBRARY_PATH unset).

## Counts

| | |
|---|---|
| assertions | 59 |
| satisfied | 59 |
| failed (`assertion failed`) | 0 |
| parse / type / other errors | 0 |

Covered: s 3(1)-(3) (fit and proper; 12 vs 13 months; practising + 7 years exactly vs 6.99;
past practice without current practice; Council consultation); s 3(5) (absence of exactly one
calendar month vs one month and a day; a practising A&S of 2 years may be temporarily appointed;
a non-practising lawyer may not); s 3(6) (12-month cap, 13-month period, lapse on the absent
notary's return and death); s 2 (revoked under s 5; revoked under s 6; before/after revocation);
s 4(2)/(3) every limb (i), (ii), (iii), use within Singapore outside (i)-(ii), and the refusal
where the answer turns on English powers / prescribed powers; s 5 each of (a), (b), (c) alone,
all, none; s 6 with and without request; s 7 (non-notary, notary within powers, notary beyond
s 4, no exercise, valid temporary notary, lapsed temporary notary, the $10,000 ceiling both
sides, District Judge); s 8(1) consultation and s 8(2) commencement; and the 1 June 2007 gate
(31 May 2007 refuses, 1 June 2007 answers) on s 2, s 3(5) and s 7.

## Failures

None.

## Expectations I could not express against the encoding's names

- **s 3(3) for temporary appointments (my R5).** "The Senate shall not make any appointment under
  this section without consulting the Council" covers s 3(5) appointments too. The rule
  `the Senate may temporarily appoint … for an absence from … to …` takes no consultation input,
  so it answers TRUE without any consultation. I could not assert the "not consulted → may not"
  case. This looks like a gap in the encoding (the `Appointment` record carries
  `Council of the Law Society consulted`, but no rule reads it).
- **s 3(4) for temporary appointments** — likewise not represented; inert discretion anyway.
- **Date gate on s 3(1).** `the s 3(1) decision on … for … months …` takes no date, so A10/A11
  (refuse before 1 June 2007) could only be tested on s 2, s 3(5) and s 7.
- **s 4(1) England powers / s 4(3)(c) prescribed powers** — no named input; tested only via the
  `another purpose`, neither-within-nor-outside refusal.
- **s 7 "within Singapore"** — modelled as the input `exercised a notarial function within
  Singapore`; exercise outside Singapore tested as FALSE on that input.
- **s 3(7) Gazette publication** — carried as an input field that no rule reads; nothing to
  assert. Exact 12-month boundary day (F2: ends the day before the anniversary) was not asserted;
  my expectation did not fix that day.
- Note: the s 5 rule joins (a) and (b) with the asyndetic `..`; my tests confirm it behaves as OR
  ((a) alone, (b) alone and (c) alone each require revocation).


## Triage by the encoder (2026-10-05)

- **s 3(3) and temporary appointments: accepted, encoding changed.** `the Senate may temporarily appoint` now takes `the Council consulted` and is false without it. `npa-tests.l4` gained the case, and the calls in `tests-independent.l4` gained the new argument (`TRUE`) with no expected value changed. Now 59 of 59.
- The s 3(1) decision takes no date, so the 2007 gate does not reach it. It answers what the current text requires; a decision made before 1 June 2007 should not be put to it, and `NOTES.md` says so.
- Gazette publication (s 3(7)) is recorded on an appointment but read by no rule, because the Act attaches no consequence to its absence.
