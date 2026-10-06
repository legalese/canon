# Employment Act 1968, Part 2 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
5 December 2025.

**Checks:** `l4 run ea-part2-cases.l4` — 52 assertions satisfied, 0 errors,
0 warnings.

## Scope

Parts **2, 3, 4, 5, 6, 6A, 7, 8, 9, 10 and 12** — every operative Part except
Part 1 (preliminary), Part 11 (repealed) and Parts 13–16 (inspection, general
and final provisions).

**246 assertions**, 0 errors, 0 warnings.

Two limits to hold in mind:

- **Part 9 is the current law only.** s 76 carries three qualifying rules side
  by side — for confinements before 1 May 2013, between then and 22 August 2015,
  and after. Only the last is encoded. A confinement before 22 August 2015 is
  outside this encoding entirely and the rules for it differ.
- **Everything prescribed is a supplied fact.** Record retention periods, pay
  slip timing, the Fifth Schedule reckoning, the s 95A minimum period of
  service. The regulations were not retrieved.

Not encoded within the Parts covered: s 19, s 34, s 39, ss 41–41A, ss 47–53,
s 66, ss 70–75, ss 84–87A (including childcare leave), s 90, ss 97–101.

## Four observations

**1. The employee's entitlement to the statutory minimum notice is nowhere
stated in one place.** It emerges from three subsections read in order:

1. s 10(2) — the contract's notice period governs;
2. s 8 — but a term less favourable to the employee than the Act is "illegal and
   void to the extent that it is so less favourable";
3. s 10(2) again — and once the term is void there is no provision in the
   contract, so the subsection's own words, "in the absence of such provision",
   send the question to s 10(3).

So a contract saying "one day's notice" gives a ten-year employee 28 days. That
is almost certainly the intended result, and it is reached by a route that no
single provision describes. Asserted as the chain on `a mean contract of 1 day`
against `ten years in`.

The same one-day term is **perfectly lawful** for a new starter, because their
statutory minimum is also one day. Nothing about the term changes; what changes
is the service it is measured against. That pair is in the cases too.

**2. s 10(3) states its three thresholds in two different units.** The bands are
"less than 26 weeks", "26 weeks or more but less than 2 years", "2 years or more
but less than 5 years", and "5 years or more". Weeks and years, with no
conversion given. A system that reduced service to a single number would have to
decide how many days are in two years, which differs across leap years and which
the Act does not answer.

This encoding therefore does **not** compute the bands: it asks the three
questions the Act asks ("employed for 26 weeks or more", "for 2 years or more",
"for 5 years or more") and leaves them as facts. That is as precise as the Act
and no more, which is the right place to stop — but it means the encoding cannot
take a start date and tell you your band. Doing that would require a convention
the legislature has not supplied.

**3. s 13 treats the two parties very differently.** The employer is deemed to
have broken the contract on **one** element: failure to pay salary in accordance
with Part 3. The employee is deemed to have broken it on **three**: absence of
more than two days, continuously, without prior leave, *and* either no
reasonable excuse *or* no attempt to tell the employer.

The "or" in that last pair does real work. An employee with a genuinely
reasonable excuse who does not mention it is **still deemed to have broken the
contract** — limb (b) is made out on its own. Asserted as
`an absence of 10 FALSE TRUE FALSE`: reasonable excuse, never communicated,
deemed in breach.

**4. Worse treatment unlocks the wrongful-dismissal remedy sooner.** Under
s 14(2A), a manager or executive dismissed **with** notice (or without notice
but paid salary in lieu) is a "relevant employee" only after **6 months'**
service. A manager dismissed **without notice and without salary in lieu** —
the harsher treatment — is a relevant employee under limb (b) with **no service
qualification at all**.

So the manager sacked on the spot in week one may bring a claim, and the one
given proper notice in week one may not. There is a coherent policy reading
(summary dismissal with nothing in hand is the case that most needs a remedy),
but the drafting produces it as a side effect of two limbs rather than stating
it. Asserted as the pair in § `14(2A)`.

## The s 14(2A) point, completed

Limb (c) of s 14(2A) is the whole of its own text: "an employee not employed in
a managerial or an executive position." No service qualification, no condition
about notice. It is now encoded, and it sharpens observation 4 rather than
softening it:

- a **non-managerial** employee is a relevant employee from the first day,
  however they were dismissed;
- a **manager or executive** dismissed *with* notice must have served 6 months;
- a **manager or executive** dismissed *without* notice and *without* salary in
  lieu is a relevant employee from the first day, like the non-manager.

So the 6-month threshold applies to exactly one group — managers and executives
who were dismissed in the proper manner. Asserted as a pair on the same facts,
one a manager and one not.

## What would need doing before this is worth anything

- ss 15–19 of Part 2.
- Parts 3, 4, 9 and 10, which is where most of the Act's value to an employee is.
- The Employment Claims Act 2016, which s 14(2) routes the remedy through.
- No case law was searched.


---

# Added with Parts 3 to 12

## A harness trap worth recording

**`MODULO` does not return a fractional part on this toolchain.** `3.5 MODULO 1`
evaluates to **3.5**, not 0.5. A floor written as `n MINUS (n MODULO 1)` is
therefore the identity function, and a round-half-up built on it silently
returns its input — which is exactly what the first version of the s 88A(2)
proportioning did. It type-checked, ran clean, and gave wrong answers; only the
assertions caught it.

On integers `MODULO` behaves: `42 MODULO 12` is 6. The rule was rebuilt to stay
in integer arithmetic throughout — the entitlement in days and the months in the
year are both whole numbers, so the division is a numerator over 12 and the
rounding comes off the remainder. See `the proportion rounded half up` in
`ea-part10-leave.l4`.

## Observations, Part by Part

**s 16 yields to the contract in either direction.** "Subject to anything in the
contract of service to the contrary" — unlike s 8, which strikes down only terms
*less favourable* to the employee. So the measure of damages for breach can be
contracted below the statutory default.

**s 29's three requirements come apart.** A deduction for damage or loss is
capped at the actual loss, capped again at a quarter of a month's wages, and
forbidden until the employee has had an opportunity to show cause. The
Commissioner may lift the *second* ceiling only. Not the first, and not the
procedural one.

**Three heads escape the s 32 overall cap** — absence, recovery of advances and
loans, and cooperative society payments. An employee repaying a loan can be
deducted more than half their salary and s 32 has nothing to say; what limits it
is s 31(5)'s quarter per instalment. Note also the asymmetry inside s 31: the
12-month ceiling applies to *advances* only, and s 31(4) gives loans no period
limit at all.

**s 38(8)'s absolute 12-hour ceiling is excepted by s 38(2)(a) to (e) but not by
(f).** The economic and essential-services ground raises the s 38(1) limits and
leaves the 12-hour one standing.

**ss 45 and 46 are expressed negatively**, and so is s 76(2B). None of them
creates an entitlement; each bars one below a threshold. The Act nowhere says
what a retrenchment benefit *is* or how much it is.

**s 35 and s 33(1) are word for word identical** — same two paragraphs, same
$4,500 and $2,600, same exclusions, same substitution power — governing two
entirely different questions: who has a rest day and a right to overtime, and
who gets priority for unpaid salary in an insolvency. They are not
cross-referenced. The encoding uses one rule for both, so the duplication is
visible rather than mirrored; if an amendment moved one figure and not the
other, this encoding would give one answer where the Act gave two.

**s 54 voids the whole contract of service**, not merely the offending term.
Compare s 8, which voids a term "to the extent that it is so less favourable".
An employer who writes part of the salary as payable in goods destroys the
contract, not just that clause — on the face of it, including every term
protecting the workman.

**The maternity benefit period is shorter than the maternity absence.** Under
s 76(1)(a) and (b) the absence is 12 weeks; under s 76(1A) the paid benefit
period is 8 weeks in every case. Four weeks of the statutory absence are unpaid.

**s 76(3) pays a day worked inside the benefit period twice over** — the gross
rate for that day, *plus* either another day's pay or a day's absence at the end.

**s 95(3) and s 96(4) deem a failure regardless of knowledge.** An incomplete or
inaccurate employee record or pay slip is a breach "whether or not the employer
knew". Asserted as a pair on the knowledge fact, where the answer does not move.

**Part 7 is one sentence, and its effect is exclusion.** The Act does not apply
to a domestic worker at all unless the Minister has applied it by notification.
Nothing in the encoding can decide whether such a notification exists.

**s 69 bars a young person only from undertakings the Minister has named.**
Industrial work as such is not forbidden to a 15-year-old; a declaration is
needed. Contrast s 68, where the prohibition on employing a child is general and
the exceptions are narrow.

## What would still need doing

- Parts 13–16, and Part 1.
- ss 84, 84A and 87A — dismissal before confinement, and childcare leave. s 87A
  is the one an employee is most likely to ask about of those left out.
- The historical limbs of s 76 and ss 84–84A, if anything before 22 August 2015
  matters.
- The regulations, which carry every prescribed period and the Fifth Schedule.
- The Employment Claims Act 2016, which s 14(2) routes the remedy through.
- No case law was searched, and no human gate has been sought.
