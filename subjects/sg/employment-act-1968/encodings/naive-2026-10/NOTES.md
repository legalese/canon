# Employment Act 1968, Part 2 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
5 December 2025.

**Checks:** `l4 run ea-part2-cases.l4` — 52 assertions satisfied, 0 errors,
0 warnings.

## Read this before using it: the scope is a small fraction of the Act

The Employment Act has **16 Parts and about 275,000 characters**. This encodes
**Part 2 only**, ss 8–14. Part 2 decides how a job ends and how much notice is
owed, which is the part an employee is most likely to need in a hurry — but
Part 3 (payment of salary), Part 4 (rest days, hours of work and overtime),
Part 9 (maternity protection) and Part 10 (holiday, annual and sick leave) are
each at least as useful, and **none of them is encoded**. Nor are ss 15–19
within Part 2.

A system built on this must not answer "what are my rights under the Employment
Act?". It can answer "how much notice am I owed?" and "can I claim wrongful
dismissal?", and nothing else.

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
