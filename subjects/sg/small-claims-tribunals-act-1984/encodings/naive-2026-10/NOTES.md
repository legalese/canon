# Small Claims Tribunals Act 1984 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, with the Act 12 of 2020 Schedule amendments
in force from 1 October 2025.

**Checks:** `l4 run scta-cases.l4` — 116 assertions satisfied, 0 errors,
0 warnings.

## Scope

- **ss 2, 5 to 10 and the Schedule** — what the tribunal can hear, the two money
  limits, the two-year bar, the one-forum rules, transfer, division,
  abandonment of the excess, and an out-of-limit counterclaim.
- **ss 34, 35, 36, 38, 40, 41, 42 and 46** — the eight orders and the cap,
  the slip rule, withdrawal, enforcement, appeal, finality, setting aside, stay,
  and the election to litigate elsewhere.

Not encoded: ss 3, 4, 13 and 14 (which constitute the tribunals and the
Registry), ss 11, 12 and 15 to 33 (procedure, the Registrar's consultation
powers, referral to a Community Mediation Centre, service, parties,
representation, evidence, failure to appear, adjournment), ss 43 to 45, and s 47.

**Unlike the `employment-claims-act-2016` row, the money limits here are in the
Act.** s 2(1) fixes the prescribed limit at **$20,000** and the prescribed
extended limit at **$30,000**, each "or such other sum as the Minister may,
after consultation with the Chief Justice, prescribe by order in the Gazette".
No such order was retrieved, so they are carried as parameters and the Act's own
figures are supplied in the cases. No rules under s 47 were retrieved, and the
Act leaves the manner and procedure of appeals entirely to them — so this row
cannot say how long a party has to appeal under s 38.

## What the Act turns out to say

### 1. Two years, and the cheap forum is the one with the short clock

s 5(3)(b) takes the tribunal's jurisdiction away "after the expiry of 2 years
after the date on which the cause of action accrued". The general limitation
period for a claim in contract or tort is six years.

So a $3,000 claim for undelivered goods is squarely within the tribunal at two
years and squarely outside it at three — and squarely inside the Magistrate's
Court at both. Asserted at exactly two years (in) and three (out).

**s 46 does not help.** It preserves an election — "Nothing in this Act is to be
construed as precluding a person from lodging a claim **that is within the
jurisdiction of a tribunal** in any other court if that person elects to
institute proceedings in that other court" — and that election is confined to
claims the tribunal *could* hear. The claimant with a stale claim gets to the
ordinary courts because the general law lets them, not because of s 46. Asserted
both ways.

### 2. A dented car is not a small claim

s 5(2)(a) removes from the tribunal any claim "in respect of damage caused to any
property **by an accident arising out of or in connection with the use of a motor
vehicle**".

Schedule para 1(b) puts "a claim in tort relating to damage caused to any
property" squarely inside the tribunal. s 5(2)(a) then takes out the commonest
version of it. A $2,000 claim for a scraped car goes to the Magistrate's Court;
an identical $2,000 claim for a wall a contractor put a hole in stays here.
Asserted as that pair.

### 3. The value of a contract claim is not always the sum you ask for

s 2(2) says the value of a claim relating to a contract means:

| nature of the claim | value |
|---|---|
| (a) rescission of the contract | **the value of the contract** |
| (b) recovery of a progress payment due under it | **the value of the contract** |
| (c) anything else | the quantum of the claim |

Consider a customer who paid a $4,000 deposit under a $90,000 renovation
contract and wants out.

- Pleaded as **rescission**, the value is **$90,000** — above the extended limit,
  so no memorandum under s 5(4) can reach it.
- Pleaded as a **debt for the $4,000**, the value is **$4,000** and the tribunal
  has jurisdiction.

Both asserted, along with the arithmetic that produces each figure.

And **there is nothing to abandon under s 9**. s 9(1) lets the claimant abandon
"the excess" where "the value of a claim exceeds the prescribed limit". On a
rescission claim what exceeds the limit is the value of the *contract*; reducing
the sum sought does not reduce it. So a claim to rescind a large contract is
outside the tribunal absolutely, not merely capped. Asserted as
`NOT abandoning the sum sought would bring the value within the limit`.

### 4. The two ways past the limit are not equivalent

| | needs the respondent | reaches | costs the claimant |
|---|---|---|---|
| **s 5(4) memorandum** | **yes** — "a memorandum signed by them" | only $20,000–$30,000 | nothing |
| **s 9(1) abandonment** | no | any amount | the excess |

A respondent facing a $25,000 claim who would rather be sued in the Magistrate's
Court simply declines to sign. The claimant's only route is then to give up
$5,000. Asserted: the $25,000 claim is in with a memorandum, out without one, and
in again with $5,000 abandoned.

A $40,000 claim is above the extended limit, so s 5(4) could not reach it even
with the respondent's signature — abandonment is the only route, at a cost of
$20,000. Asserted.

And **s 35(2) keeps the ceiling at the prescribed limit after an abandonment**,
because the extended limit applies only "in the case where section 5(4)
applies". Asserted: the ceiling is $30,000 on the memorandum route and $20,000
on the abandonment route.

### 5. Section 6(1) has a gap, and the Employment Claims Act 2016 does not

s 6(1): "Where a claim has been lodged with a tribunal, no proceedings relating
to that claim may be brought before any other court **except** — (a) where the
proceedings before that court were commenced before the claim was lodged; or
(b) where the claim before the tribunal has been **withdrawn or abandoned**."

s 5(5) requires the tribunal, where it is of the opinion that a claim is beyond
its jurisdiction, to **discontinue** the proceedings.

A tribunal-ordered discontinuance is neither a withdrawal nor an abandonment. So
on the words of the Act, a claimant who lodges in the wrong forum and lets the
tribunal say so is barred by s 6(1) from bringing the claim anywhere else — and
s 46 does not rescue them, because s 46 is confined to a claim that *is* within
the tribunal's jurisdiction.

Asserted: `section 6(1) bars proceedings in another court` on the
discontinuance fixture, and `NOT the claimant can still take the claim to
another court`.

**Two cures, and both have to happen before the discontinuance:**

- **s 34** — "A claimant may **at any time** withdraw the claimant's claim
  whether or not a tribunal has heard the claim." Unqualified. A claimant who
  sees the tribunal heading for s 5(5) should withdraw instead. Asserted.
- **s 7** — "**Despite section 5**, a tribunal may, at any time if it is of the
  opinion that a claim ought to be dealt with by any other court, **transfer**
  the proceedings to that court." The words "despite section 5" mean the power
  survives the absence of jurisdiction, so s 7 is the tribunal's alternative to
  discontinuing, and the only one of the two that leaves the claimant with a
  claim. Asserted.

Worth noting beside this row's sibling: the **Employment Claims Act 2016**,
drafted thirty-two years later, has the same structure in its s 16(2) and lists
all three outcomes — "withdrawn, **discontinued** or **dismissed for lack of
jurisdiction**". This Act lists two. Whether that is a drafting improvement
noticed in 2016 or a difference with a reason is not something the deposited text
answers.

### 6. Section 10(4) is the widest jurisdictional provision in the Act

s 10(1) lets any party apply to move an out-of-limit counterclaim to the
appropriate court. s 10(4): "Where **no application is made** under subsection
(1) or where on such an application it is ordered that the whole proceedings be
heard before a tribunal, **the tribunal has jurisdiction to hear the proceedings
despite any other provisions of this Act**."

"Despite any other provisions of this Act" — so despite the prescribed limit,
despite the extended limit, and on the words despite the two-year bar. A
respondent with a $200,000 counterclaim who says nothing hands the tribunal
jurisdiction over the whole of it. Asserted.

What the Act does not say is what the tribunal may then *order*. s 35(2) caps "a
money order or work order" at the prescribed or extended limit and says nothing
about a counterclaim within s 10(4). The relationship between the two is
unresolved on the face of the Act.

### 7. The Small Claims Tribunal can evict a residential tenant, and the cap does not apply

s 35(1)(g): "where the claim is for **unpaid rent** for any premises under a
contract specified in paragraph 1(c) of the Schedule, an order for the **delivery
of vacant possession** of the premises".

Schedule para 1(c) is "a claim relating to a contract for the lease of
residential premises that does not exceed 2 years". So within that limb, and on
a claim for unpaid rent and nothing else, a tribunal designed for consumer
disputes can order a tenant out. Asserted, including that the order is not
available on a claim for some other breach of the lease, nor on a goods claim.

**s 35(2) does not reach it.** The cap applies to "the total value of a **money
order or work order**" — and s 35(4) defines "money order" as an order under
s 35(1)(a). A possession order has no total value in that sense, and nothing in
the Act values the premises or caps the order by reference to them. So the tenant
of a property worth any amount may be ordered out on a rent claim of $500.
Asserted, as is the fact that the cap does not reach the costs order under
s 35(1)(f) or the ancillary order under s 35(1)(h) either.

Also worth recording: a three-year residential lease is outside Schedule para
1(c) and therefore outside the tribunal altogether — the tenant on the longer
lease is better protected than the tenant on the shorter one, because the
landlord has to go to court. Asserted.

### 8. Two thirds of the Schedule is there for institutions to collect

Of the nine specified claims in Schedule para 1, three are the ones an individual
brings — (a) goods and services contracts, (b) property damage in tort, (c) a
short residential lease. The other six are all claims **by** a body **for the
recovery** of money from an individual: an owner developer, a management
corporation, the Housing and Development Board, the Council of the Singapore
Business Federation, and a Town Council twice over.

Asserted limb by limb. It is not a defect; it is what the Act is for, and it is
worth knowing before describing this tribunal as a consumer forum.

### 9. The reading question in section 5

s 5(3) opens "**Except where this Act expressly provides otherwise**" and then
states two bars: the value bar in (a) and the two-year bar in (b).

s 5(4) is a freestanding conferral — "a tribunal **has** jurisdiction to hear and
determine any claim the value of which exceeds the prescribed limit but does not
exceed the prescribed extended limit, if the parties so agree" — and it is
expressed to be "**Subject to subsections (1) and (2)**". Not to subsection (3).

Read literally, s 5(4) expressly provides otherwise and is not subject to the
two-year bar. A $25,000 claim three years old would be heard on a memorandum,
while a $15,000 claim of the same age could not be heard on any terms.

**The conservative reading is the more likely one.** s 5(3)(b) is naturally a
freestanding time bar; s 5(4) is about value and nothing else; the omission of
subsection (3) from s 5(4)'s opening words is loose drafting rather than design.
Nothing in the Act suggests Parliament meant parties to be able to contract out
of a limitation period by raising the amount in dispute, and the literal reading
produces the absurdity that the larger claim is heard and the smaller is not.

So `the tribunal has jurisdiction` in `scta-jurisdiction.l4` **takes the
conservative reading**, because an encoding anyone might rely on should not hand
a claimant the generous one. The literal reading is encoded beside it as
`the tribunal has jurisdiction on the literal reading of section 5(4)`, and
`the two readings of section 5 disagree about this claim` is asserted true on the
one fixture where they part and false on four where they do not.

The same words recur in s 10(4) — "despite any other provisions of this Act" —
where the drafting is unambiguous and points the other way, which is some
evidence that s 5(4)'s narrower formula was chosen rather than slipped into.

### 10. Smaller things worth recording

**Service in Singapore is a condition of jurisdiction.** s 5(1)(b) makes it part
of the jurisdictional test, not a step of procedure. A respondent who cannot be
served here is beyond the tribunal whatever the claim is worth. Asserted.

**There is no appeal on the facts.** s 38(1) allows only a question of law or a
want of jurisdiction; s 40 makes the order "final and binding … and, except as
provided in section 38, no appeal lies". A claimant who says the tribunal
believed the wrong witness has no remedy under this Act. Asserted, including
`NOT the party has some way of challenging the order` on those facts.

**s 41 is a remedy for not having been there, not for having lost.** It reaches
orders made on a failure to appear and certain Registrar's orders, on the
application of "a person aggrieved", within one month "or such further period as
the tribunal may allow". Asserted at one month, at three months, and at three
months with an extension.

**The slip rule is shorter and cannot be stretched.** s 35(3) gives fourteen
days to correct a clerical mistake, an accidental slip, a material
miscalculation or a defect of form — with no extension power, where s 41(2) has
one. Asserted at day 10, day 14 and day 20, and `NOT the fourteen days in
section 35(3) may be extended`.

**Three courts can stay enforcement and none of them need.** s 42(1): an appeal
"does not operate as a stay … unless the tribunal, a District Court or the
General Division of the High Court orders otherwise". Asserted both ways.

**Enforcement is a District Court's.** s 36 makes an order under s 35(1)
enforceable "in the same manner as a judgment or an order made by a District
Court", so the machinery belongs to a court the claimant never went to.

**The work order is what this tribunal has that a money court does not.**
s 35(1)(b), with the money-in-default backing in s 35(1)(c), lets the tribunal
require the trader to come back and fix the thing. s 2(1) defines it widely
enough to include replacing the goods.

**s 8 leaves room.** A claim must not be divided "**for the sole purpose** of
bringing the sum claimed in each of such proceedings within the jurisdiction of a
tribunal", so a division for another genuine reason is not forbidden by that
section. Asserted on all three combinations.

## What would need doing before this is worth anything

- **Check for an order under s 2(1)** varying either limit. The Act's own $20,000
  and $30,000 are encoded, and an order in the Gazette would displace them
  silently.
- **Retrieve the rules under s 47.** Without them this row cannot say how long a
  party has to appeal under s 38 — the Act leaves "the manner and the conditions
  under which appeals may be brought" entirely to rules.
- **No case law was searched.** The reading question in finding 9, the s 6(1) gap
  in finding 5, and the uncapped possession order in finding 7 are all readings
  of the words. The s 38 appellate jurisdiction exists and will have produced
  authority.
- The procedure — ss 15 to 33 — is not encoded at all, and for a litigant in
  person it is most of what matters: how to lodge, who may appear, what happens
  if the other side does not turn up, when the Registrar can decide the case
  without a hearing. None of that is in this row.
- The onward references are not followed: Community Disputes Resolution Act 2015
  s 4; Building (Strata Management) Act 2004 ss 22(1) and 40(6); Housing and
  Development Act 1959 s 83; Singapore Business Federation Act 2001 s 12(4);
  Town Councils Act 1988 ss 36 and 73; Payment Services Act 2019.
