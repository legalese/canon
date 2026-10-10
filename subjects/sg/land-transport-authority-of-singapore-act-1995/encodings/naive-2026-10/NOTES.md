# Land Transport Authority of Singapore Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
23/9/2026", with amendments to Act 5 of 2026 and S 664/2026 (wef 23 September 2026)
shown.

**Checks:** one case file, 117 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. Most of the Act sets up
the Authority, its funds and its staff. This row takes the parts with decision
content for the public: compensation for railway, cross-border railway and
road-tunnel works (ss 19, 20, 22, 22A, 23, 25(3) and the Fourth Schedule),
outsourced enforcement officers (ss 11, 11A, 11B), the Authority's power to arrest
and the obstruction offence (s 39(1)(c), (6)), personal immunity (s 10), secrecy
(s 41) and the Authority's symbol (s 42). The constitution, functions, funds,
Compensation Board machinery, staff transfers and electronic service are not
encoded, and neither is the amount of any compensation.

## What the Act turns out to say

### 1. Losses from railway and road-tunnel works can only be claimed under the Act

s 19 bars any action "against the Authority or any other person" to stop works
authorised under the Rapid Transit Systems Act 1995, the Cross-Border Railways Act
2018 or the listed Street Works Act provisions, or to recover damages for loss,
disturbance or inconvenience they cause, "except pursuant to one of the rights to
compensation provided for in section 20". The bar protects "any other person" as
well as the Authority (that this reaches contractors is an inference; s 21 applies
the claims machinery to such persons). Asserted.

### 2. Some claim windows are only one year, and lapse is a bar

The Fourth Schedule periods run from 2 years (displacement under a possession
notice) to 6 years (structural damage, from the opening of the railway or tunnel
to the public), but damage from works on land, altering apparatus, and removal or
reinstatement of structures each have **one year**. Under s 22(1) a claim not served
in time is barred. The Compensation Board may extend, but never beyond **6 years from
when the right first arose** (s 22(5)). Asserted.

### 3. A mistake about the deadline itself does not count

s 22(4)(a) lets the Board extend for a "mistake of fact or mistake of any matter of
law (other than the relevant provision in the fourth column...)". A claimant who
misread the claim period has to rely on "any other reasonable cause" or on the
Authority not being materially affected by the delay (s 22(4)(b)). The encoding
treats the excluded mistake as not qualifying under (a), but leaves the other two
routes open; how a court would treat that combination is not decided. Asserted.

### 4. Business losses and changes in land value are not compensated

Fourth Schedule Part 2 para 3: no account is taken of loss from "interruption of or
interference with any trade or business", or of any increase or decrease in land
value attributable to the railway or road. Para 6 excludes the lost benefit of
advertising on a removed sign. A tenancy terminable on less than a month's notice,
or a mortgagee not in possession, has no "compensatable interest" (para 2). Asserted.

### 5. Silence and refused offers carry costs and deemed rejection

Unanswered requests for particulars deem the claim rejected after 28 days (s 23(4));
either side may go to the Compensation Board if the claim is not settled 4 months
after receipt (s 23(8)); a party who refuses an offer and does no better before the
Board pays both sides' later costs unless the Board finds special reasons (s 25(3)).
Asserted.

### 6. Outsourced enforcement officers can never arrest; LTA officers can

s 11A(3): the Chief Executive "cannot authorise" an outsourced enforcement officer
to arrest anyone, and the officer may act only in uniform, on production of the
card, within the written authorisation and as directed (s 11A(4)). An Authority
officer authorised in writing by the Chief Executive may arrest without warrant for
offences under the Fifth Schedule Acts (s 39(1)(c)). Impersonating an outsourced
officer is an offence ($2,500 or 6 months), with a defence, proved on a balance of
probabilities, for a licensed public entertainment (s 11B(3)). Asserted.

### 7. Obstruction carries the heaviest penalty of the five offences in the Act

s 39(6): obstructing, wilfully misstating, refusing information without lawful
excuse, or failing to comply with a lawful demand — $5,000 or 12 months. Secrecy
(s 41) is $2,000 or one year; the symbol offence (s 42) $2,000 or 6 months. Asserted.

## What would need doing before this is worth anything

- The Fourth Schedule Part 1 table is column-shifted in the `.txt` deposit; the
  periods were matched to items by order and wording, and should be checked
  against the PDF.
- The start event of each period (notice date, opening date, completion, removal)
  is not modelled; the encoding takes elapsed years as given.
- Reading s 23(4)'s "further period" as added to the 28 days, and s 22A's
  permitted loss as item 1(a), are inferences.
- The assessment bases in the second column, the Board's powers (ss 26-31) and the
  related possession provisions of the Rapid Transit Systems, Cross-Border Railways
  and Street Works Acts were not read.
- No decided cases or Compensation Board awards were searched.
