# Employment Claims Act 2016 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 April 2022.

**Checks:** `l4 run eca-cases.l4` — 134 assertions satisfied, 0 errors,
0 warnings.

## Why this Act and not another

The `employment-act-1968` row in this repository encodes Parts 2 to 12 of the
Employment Act and routes the s 14(2) wrongful dismissal claim onward — and
then stops, because the Employment Act does not say where the claim goes. This
is where it goes. The same is true of the Child Development Co-Savings Act 2001
leave entitlements, the Retirement and Re-employment Act 1993 re-employment
disputes, and every money claim in the Employment Act's Parts 3, 4 and 10.

So the limitation periods in s 3(2) of **this** Act are the limitation periods
for those claims, and the jurisdictional conditions in s 12 are what decides
whether they can be brought at all. Nothing in the Employment Act says so.

## Scope

- **Part 2 in full** — ss 2 to 7: the mediation gateway, the seven time limits in
  s 3(2), the listing requirements in s 3(3), the Commissioner's power to refuse,
  the claim referral certificate in s 6, and settlement in s 7.
- **Part 3, Divisions 2 to 4** — ss 12 to 16, 21, 22, 23, 24, 27 and 28.

Not encoded: Part 3 Division 1 (ss 8 to 11, which constitute the tribunals and
make appointments), the procedural detail in ss 17 to 20, and ss 29 to 35.

### The single biggest limitation on this row

**No regulations and no Rules of Court were retrieved.** The Act leaves to them:

| left to regulations | provision |
|---|---|
| which employees may use the tribunal | s 12(2)(a), (b), s 12(8)(a) |
| which employers may | s 12(2)(c), s 12(8)(b) |
| **the claim limits** | s 12(7), s 12(8)(e) |
| the period for lodging after a certificate issues | s 12(6), s 12(8)(d) |
| the mediation fee | s 3(3)(d), s 3(6)(d) |
| the manner of submitting a request | s 3(2), s 3(6)(a) |

Every one of those is carried as a supplied fact or a parameter. The claim limits
are exercised in `eca-cases.l4` using **explicitly invented figures** of $20,000
and $20,000, labelled as invented in the file. The figures commonly cited for the
real limits are deliberately **not** encoded, because they are in regulations
that were not read and a figure in a repository of law is taken as the law.

## What the Act turns out to say

### 1. There are three limitation periods, not one, and the second is easy to miss

s 3(2) sets a period for submitting the mediation request, with seven limbs. The
shortest — **one month from the date of dismissal** — governs the central
wrongful dismissal claim under Employment Act s 14(2). Asserted at three weeks
and at six weeks.

But s 3(3)(a)(ii) imposes a **separate** requirement, on every limb: the dispute
may be listed only if "the material facts giving rise to the dispute occurred
**not earlier than one year before** the date on which that request is
submitted". It runs from the facts, not from the end of the employment.

So consider an employee with three years' service, owed an allowance that fell
due eighteen months ago, who resigns and submits a request two months later:

| | |
|---|---|
| s 3(2)(f) — six months from the last day of employment | **satisfied** |
| s 3(3)(a)(ii) — facts under a year old | **not satisfied** |
| may the dispute be listed? | **no** |

Both asserted. The practical effect is that the six-month window in s 3(2)(f) is
a one-year-from-the-facts window in disguise, and the employee who waited to
leave before complaining has lost the older part of the claim.

And a third period: **s 12(6)** requires the claim to be lodged "within the
prescribed period after the date of issue of the claim referral certificate".
That period is not stated in the Act.

### 2. The claimant who misses the mediation can lose everything; the respondent who misses it cannot

s 6(2) makes the certificate **mandatory** on any of three grounds, the first
being that "the respondent is given reasonable notice of, but does not attend,
the mediation". So a respondent who ignores the process hands the claimant the
document they need.

s 6(3) says that where the claimant "without reasonable excuse, fails to attend
any mediation session", the mediator **may** discontinue the mediation and
"refuse to issue to the claimant a claim referral certificate".

s 12(5) then requires a certificate "in respect of **every** specified employment
dispute for which the claim is lodged".

Read with the one-month limit in s 3(2)(d), a claimant who misses the mediation
session on a wrongful dismissal claim and is refused a certificate has in
practice lost the claim: the month from dismissal will have gone, and there is no
extension power in the Act. Both halves asserted.

The power is discretionary, so the same absence need not be fatal — also
asserted, on a fixture where the certificate issued anyway.

### 3. The order in which you choose your forum decides whether you have a claim at all

This is the sharpest thing in the Act, and it is in four subsections that read
almost identically.

**s 16(5)** — representations to the Minister under Industrial Relations Act
s 35(3) bar a wrongful dismissal claim, **if** (a) they were made and (b) either
(i) the employee does not withdraw them, or (ii) the Minister decides on them.

**s 16(6)** — where the employee **has lodged** the claim and then makes those
representations, "the claim is **deemed to be discontinued** … with effect from
the date on which the employee makes those representations."

s 16(3) and s 16(4) do the same for claims about First Schedule item 17 and
Second Schedule items 13 and 15, and s 16(3) additionally catches
representations under Retirement and Re-employment Act s 8(1).

**The two orders are not the same.**

| order | outcome |
|---|---|
| representations, then withdrawn before a Minister's decision, then lodge | **live claim** — limb (b) fails both ways |
| representations, Minister decides, then withdraw, then lodge | barred — limb (b)(ii) |
| **lodge, then representations** | **deemed discontinued** |
| **lodge, then representations, then withdraw them** | **still discontinued** — nothing revives it |

All four asserted, and the first and last asserted side by side, because the
conduct is identical and only the sequence differs.

s 16(5)'s bar is conditional and curable. s 16(6)'s deeming is neither: it has no
withdrawal condition and no revival provision. Read with the one-month limit in
s 3(2)(d), the second order is in practice terminal — by the time the employee
has lodged, gone to the Minister and changed their mind, the month is long gone.

### 4. The excess over the claim limit is abandoned everywhere, not just here

s 15(1) lets a claimant whose total exceeds the limit "abandon the excess
amount", and s 15(2) then deems s 12(7) satisfied and gives the tribunal
jurisdiction. s 15(3): "Where the claimant has abandoned the excess amount, the
claimant **cannot recover that amount in a tribunal or any other court**."

So there is no route by which a claimant takes the limit here and the balance in
the District Court. s 15(3) shuts that direction; s 16(2) shuts the reverse while
the tribunal claim is live; and s 16(1)(a) shuts it permanently once another
court has "heard and determined" the claim. The price of the tribunal's speed and
informality is the excess, paid once and for good. Asserted.

A detail that cuts the other way: **s 12(7) counts the two caps separately** —
one for contractual and statutory disputes together, one for wrongful dismissal
disputes. A claimant can be inside one and outside the other, and abandon down
only the second. Asserted on a mixed claim.

And **s 7(1)(b) and (c) apply the same limits to a negotiated settlement**, with
no counterpart to s 15. Parties who agree a figure above the limit cannot record
it in a settlement agreement under Part 2 at all. Asserted, together with
`NOT a party at a mediation may abandon an excess over the claim limit`.

### 5. The tribunal is an employees' forum, and the Act says so

s 12(2)(c) lets a prescribed **employer** bring a claim against an employee only
about "item 17 of the First Schedule or item 14 or 16 of the Second Schedule", or
another Schedule matter prescribed for the purpose. Those three are: salary in
lieu of notice, the Employment Act s 11(1) payment, and the Employment Act s 16
payment — all of them money an employee owes for leaving without notice or
breaking the contract.

Everything else in the two Schedules — all eighteen First Schedule items and the
Second Schedule's thirty-odd — is available to an employee and not to an
employer. Asserted item by item for the three that are named and for one that is
not.

### 6. Section 27(2)(b) rewards an employer for saying nothing

s 27(2) puts the burden on the employer in four situations. Three of them
(summary dismissal met with a s 14(2) claim; the two maternity cases) turn on
what the employee did.

Limb (b) is different: it applies "where an employee is dismissed **with notice**
by an employer, and the notice of dismissal **is or purports to be given on the
ground that there has been poor performance or misconduct**".

The trigger is the employer's own statement. An employer who gives contractual
notice and writes "for poor performance" takes on the burden of proving poor
performance. An employer who gives the same notice and states no reason at all
does not come within the limb. Asserted as that pair.

### 7. Smaller things worth recording

**A dispute has to be about money.** Both Schedule definitions in s 2(1) are
confined to "a dispute, relating to a payment of an amount of money". A demotion,
a transfer, a refused reference, a shift roster — none is a specified employment
dispute, however squarely it arises out of employment. Asserted.

**Reinstatement is the Act's only non-money remedy and it belongs to one kind of
dispute.** s 12(3)(b) allows it only "in a case where the claim is lodged in
respect of a wrongful dismissal dispute". Asserted, including the failure case
where reinstatement is sought on a contractual claim.

**Jurisdiction does not depend on when the dispute arose.** s 12(1) ends
"regardless whether the dispute giving rise to the claim arose before, on or
after 1 April 2017". Every time limit in the Act is in s 3(2), s 3(3)(a)(ii) and
s 12(6), and none of them is in s 12(1). Asserted as
`NOT jurisdiction depends on whether the dispute arose before 1 April 2017`.

**s 3(4) is a power, not a duty.** The Commissioner "may refuse to accept" a
non-compliant request. A ground to refuse is not a refusal, and the encoding
reports the ground and stops there. s 3(4)(a)(ii) also brings the claim limit
forward into the gateway, so a request can be refused before anyone reaches the
tribunal — which is where s 15 would have cured it. Asserted.

**s 3(5) is a duty, not a power.** "Upon accepting the mediation request, the
Commissioner **must** … refer every specified employment dispute listed in that
request for mediation."

**s 21(2) is the practical answer to the records problem** in a small wage claim:
the tribunal "may draw any inferences that the tribunal thinks fit from a party's
failure to comply with any obligation … under any written law specified in the
Fourth Schedule, including … that any evidence that is not available on account
of that failure would, if produced, have been unfavourable to that party". It is
a power and not a presumption — asserted as
`NOT section 21(2) creates a presumption against the party` — and it is tied to
the Fourth Schedule's list of written laws rather than to record-keeping
generally.

**s 21(8) and s 23(1) sit oddly together.** The tribunal "need not keep a record
of the evidence given in any proceedings", and the only appeal is on a question
of law or jurisdiction. Asserted.

**There is no appeal on the facts, and the gate to the appeal that exists is
itself unappealable.** s 23(2): an appeal lies "only if permission to appeal is
given by a District Court". s 23(4)(a): that order "is final and is not subject
to any appeal". A party who says the tribunal found the facts wrongly has nowhere
to go; a party who says it got the law wrong must first persuade a District
Court, whose refusal ends the matter. Asserted.

**s 24(1): the order is enforceable while the appeal runs** unless a court orders
a stay. Asserted both ways.

**s 14 leaves room.** "A claim cannot be divided and pursued in separate
proceedings … **if the only reason** for doing so is to bring the total within
the jurisdiction of a tribunal." A division for another genuine reason is not
forbidden by this section.

**s 28 severs rather than voiding wholesale** — "void **to the extent that** it
purports" — and reaches an arbitration clause, a settlement barring future
claims, and a foreign-forum term alike, whenever the agreement was made.
Asserted on all three plus a control.

## What would need doing before this is worth anything

- **Retrieve the Employment Claims Regulations and the Rules of Court.** Without
  them this row cannot answer the two questions a claimant asks first: *can I use
  this tribunal* and *how much can I claim*. The invented figures in the cases
  file must not be read as anything else.
- **No case law was searched.** The order trap in finding 3 and the double
  limitation period in finding 1 are readings of the words. Both are the kind of
  point on which there may be a High Court decision on appeal under s 23.
- The Fourth Schedule (the written laws whose breach feeds the s 21(2) inference)
  and the detail of the First and Second Schedules are carried as flags rather
  than enumerated. Nothing in the encoding checks which Schedule item a
  particular claim is about, except for the five items that other sections name.
- The onward references are not followed: Employment Act ss 11, 14, 16, 65, 84,
  115 and 119; Industrial Relations Act ss 30H and 35; Retirement and
  Re-employment Act ss 8, 8A and 8B. Where this Act defers to a period "determined
  under" one of those provisions, the encoding takes compliance as a supplied
  fact. The `sg/employment-act-1968` row covers some of the Employment Act side
  and does not cover ss 65, 115 or 119.
