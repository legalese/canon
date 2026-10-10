# Community Disputes Resolution Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
1/9/2026", deposited at `../../registers/source-bundle/CDRA2015.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021"; the
consolidation annotates later amendments by Act 25 of 2021 (wef 1 April 2022) and
Act 43 of 2024 (wef 24 March 2025, and wef 1 September 2026 for ss 12A, 17, 17A,
26(1)(c), 29A and 31A to 31E).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It was chosen for its **everyday-life relevance**: it governs disputes between
neighbours over noise, smells, clutter, obstruction and the like, and sets up the
Community Disputes Resolution Tribunals that hear them. An automated count found 3
of the 527 deposited Singapore Acts citing it by its slug title. That count misses
citations by short or older titles, so it says nothing about how important the Act is.

This row takes what a resident on either side of a dispute meets: who counts as a
neighbour and what the tort requires (s 4); special directions, bonds, exclusion
orders, the penalties for breaching them, and landlords' termination rights (ss 6 to
11); the 36-month cap on mandatory treatment orders (s 12A); abatement orders,
appeal to the Minister, obstruction and mediation directions (ss 13L, 13N, 13R,
13W); composition (ss 13U, 34); and the tribunal's limit, time bar, representation
and appeal rules (ss 17, 26, 29). The s 19 rule against splitting claims and the
s 25 bar on costs are quoted in comments but not asserted.

Not encoded: the "just and equitable" weighing (ss 5(2), 9(4)), the hoarding order
(s 11A), the psychiatric assessment procedure in s 12A, the officers' appointment
and investigation powers (ss 13B to 13K, 13S, 13T), secrecy and regulations (ss 13X
to 13ZC), the Director-General's own applications (s 17A), transfers (ss 20, 21),
privacy orders (s 22), settlement registration (s 31A) and civil restraint orders
(ss 31B to 31E).

## What the Act turns out to say

### 1. An officer's abatement order carries heavier penalties than a court's direction

A court's special direction (s 7) or exclusion order (s 10) carries a fine of up to
$5,000, or 3 months, or both, plus up to $1,000 a day for a continuing offence,
"but not exceeding $10,000 in total". Breaching an abatement order issued by the
Director-General (s 13L(5)) carries up to $10,000 on a first conviction, and up to
$20,000 or 3 months or both on a later one. The daily $1,000 is stated with **no
total cap**. So 30 days of continued breach can cost up to $10,000 under s 7 but
up to $30,000 under s 13L(5). Imprisonment for breaching an abatement order is
available only on a second or later conviction. Asserted.

### 2. Damages cannot be pursued up the enforcement ladder

The ladder runs from a disobeyed order, to a special direction (s 6), to a bond
(s 6(3)), to exclusion from one's own home (s 9). But s 8 says "Section 6 does not
apply to an order of court made under section 5 which requires a contravening party
to pay damages." Injunctions, specific performance and apology orders can be taken
up the ladder; damages orders cannot. Asserted.

### 3. A person can be excluded from their own home, and a landlord can end the lease

If a special direction is breached without reasonable excuse, a court may exclude
the person "from his or her place of residence" where that is just and equitable
(s 9), and may do so more than once (s 9(5)). A landlord ordered to enter into a
bond may end the tenancy by written notice giving at least 14 days before
re-possession. This applies "despite anything in any other law or in any agreement",
and the landlord "is not liable" (s 11). Asserted.

### 4. Mediation can be compulsory, and walking out is an offence

An officer may direct neighbours, and their landlord, to mediation "with or without
the consent" of the people directed, and the direction "is final" (s 13M). Not
turning up is an offence. So is withdrawing before the mediator allows it. The
reasonable-excuse defence is for the accused to prove, and the maximum fine is
$1,500 (s 13R). Asserted.

### 5. The tribunal is small-claims in shape: $20,000, two years, no lawyers by default

The tribunal has no jurisdiction over a s 4 claim that exceeds $20,000 or is brought
more than 2 years after the cause of action accrued (s 17(3), (5)). A claimant may
abandon the excess, but then cannot recover more than the limit (s 17(4)). Each
party presents their own case. A lawyer may appear only if all parties agree **and**
the tribunal permits; the Director-General is the only exception (s 29(3)). Costs
other than disbursements are not awarded (s 25). An appeal to the High Court needs
the tribunal's own permission, and a refusal is final (s 26(2), (3)). The months
count of the 2-year bar is this encoding's simplification. Asserted, except costs.

### 6. "Neighbour" reaches 100 metres, but not the next room

A neighbour lawfully resides in the same building, or within 100 metres measured
boundary to boundary (s 4(4), (5)). People who occupy the same place of residence
are excluded: flatmates in different rooms, and the occupants of sub-divided units
in one apartment with the same registered address (Illustrations). Whether exactly
100 metres counts as "within" is not said. The encoding treats it as within, which
is an inference. Asserted.

### 7. Psychiatric treatment can be ordered in a civil neighbour dispute

From 1 September 2026, s 12A lets a court order a respondent to undergo psychiatric
treatment, possibly residing in a psychiatric institution. The total period is
capped at 36 months on the same basis, and an order may be made only if the formal
assessment report certifies all four matters in s 12A(15). Asserted (the cap and
the certification gate only).

### 8. Refusing an officer is no offence if the officer will not show identification

Obstructing or refusing a community relations officer carries up to $5,000 or 12
months (s 13N(1)). But refusing a request is not an offence if the officer fails to
declare his or her office or refuses to produce an identification card on demand
(s 13N(2)). Asserted.

### 9. A cross-reference to a subsection that is not in the deposit

s 17A(3)(b) applies "this Act (including section 17(3), (3A), (4) and (5))". The
deposited s 17 has subsections (1) to (5) and no (3A). Not asserted.

### 10. The fault words in s 4(1) are ambiguous

The tort covers interference caused "whether intentionally, recklessly or
negligently". The encoding reads this as requiring at least one of the three states
of mind. The words could also be read as making the state of mind irrelevant, which
would make the tort close to strict. Asserted on the first reading.

## What would need doing before this is worth anything

- The Community Disputes Resolution Rules and any regulations prescribing
  compoundable offences, s 12A matters or a substituted limit were not retrieved.
- The "just and equitable" factors, and what counts as "unreasonable" interference,
  are left as booleans. Tribunal decisions on them were not searched.
- The 2026 provisions (ss 12A, 17A, 31A to 31E) were read but mostly not encoded.
- The missing s 17(3A) should be checked against the official Act 43 of 2024.
