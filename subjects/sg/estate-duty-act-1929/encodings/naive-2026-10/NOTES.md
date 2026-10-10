# Estate Duty Act 1929 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2025 (in force 9 March 2025) shown.

**Checks:** one case file, 97 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes the
decisions an executor, or a practitioner closing an old estate, meets:
- which deaths the Act reaches and which rate schedule applies (ss 2A, 5)
- what property is within it (s 2 "property", s 11(2))
- lifetime gifts deemed to pass on death (s 7(1)(c))
- the house, other-property and CPF reliefs for deaths from 1 April 1984 (s 14(3)-(8))
- the Fourth and Fifth Schedule rates
- the funeral allowance (s 27(5))
- the six-month return, interest and the late-payment penalty (ss 35, 36, Sixth Schedule)
- the $50,000 share exception, intermeddling, small-sum waiver and false statements
  (ss 43(5), 44, 50, 54)

Not encoded: the other deemed-passing rules (s 7(1)(a), (b), (d)-(g), s 8),
companies (Part 3), aggregation and valuation (ss 23-26), foreign duty credits,
liability and apportionment (ss 29-34), the Commissioner's powers, certificates and
postponement (ss 37-42), appeals, informers, and every death before 1 April 1984
(First to Third Schedules and the remission schedules).

Dates are numbers of the form YYYYMMDD. That is an encoding convention, not the Act's.

**Warning about the source.** The Sixth Schedule (interest) is laid out in interleaved
columns in the `.txt` deposit. Periods and rates were matched by item number and order
of appearance. The First to Third Schedule tables are also visibly shifted (the 12½%
row and the final rates are out of line); they were not encoded.

## What the Act turns out to say

### 1. The Act is closed to every death from 15 February 2008, but it is still amended

s 2A: "This Act shall apply only in relation to persons dying before 15 February 2008."
The Fifth Schedule runs to that date and no later. Yet the deposit shows amendments
in 2019, 2021 and 2025 (s 4, appointment of the Commissioner, by Act 5 of 2025). A likely
reason (an inference, not stated) is s 34(1): no claim for estate duty "shall be barred by any lapse of time".
(s 34(2) lets the Minister remit duty still unpaid 25 years after a death; that is
not encoded.) Asserted for s 2A.

### 2. The house relief is $9 million, and the other-property relief does not top it up

For deaths from 28 February 1996, s 14(4) relieves the house up to the "amount
prescribed" ($9 million, s 14(8)) and $600,000 of "all other property". s 14(5): the
part of a house's value above $9 million "shall not qualify" for the $600,000 relief.
So a $10 million house and $1 million of other property leave $1.4 million chargeable,
duty $70,000 at 5%. Asserted.

### 3. CPF is relieved only above the threshold, so a CPF-heavy estate still pays

s 14(4)(c) relieves "the excess over $600,000, if any," of CPF balances. Reading CPF up
to $600,000 as "other property" within (b) (an inference, labelled in the module),
$400,000 of other property plus $1 million of CPF leaves $400,000 chargeable, duty
$20,000. Asserted.

### 4. A gift to a charity or the Government escapes even if the donor kept a benefit

s 7(1)(c) pulls back gifts not made 5 years before death (12 months for public or
charitable purposes) and gifts "whenever made" where the donor kept a benefit. But
proviso (ii) says "nothing in this paragraph" applies to gifts to the Government or an
institution of a public character, in consideration of marriage, normal expenditure,
or of $1,000 or less to a donee. So the exclusion beats the retained-benefit rule.
Asserted.

### 5. From 2002 a non-domiciled person pays only on immovable property in Singapore

The s 2 definition of "property" reaches movables abroad only for a person domiciled
in Singapore, and never immovables abroad. s 11(2) then frees all movable property of
a non-domiciled person dying on or after 1 January 2002. Asserted.

### 6. The penalty climbs a point a month and stops at 12%

s 36(2): 6% per year for the first complete month after the "relevant date" (the later
of 30 days after the notice of assessment and 6 months after death), then 1% more for
each further complete month, capped at 12%. Interest (Sixth Schedule) is 0% for the
first 6 months for deaths from 2005, then 6%, then 12% from 18 months. Asserted.

### 7. Intermeddling costs $1,000 and double duty; small CDP holdings are exempt

s 44(2): anyone who takes possession of or administers a dutiable estate without a
grant within 6 months forfeits $1,000 and is liable to "double the amount of duty
leviable". s 43(5) lets CDP or CPF Investment Account shares worth $50,000 or less be
dealt with without the estate duty schedule, and s 44(2) yields to it. Whether double
duty is in addition to the single duty is not said in s 44; the encoding gives twice
the duty and labels that reading. Asserted.

## What would need doing before this is worth anything

- The s 14 relief ignores the order in which debts (s 27(2), deducted "from the value
  of the property liable thereto") and the funeral allowance come off, and takes all
  CPF as qualifying; the contribution proviso in s 14(3)(c) and (4)(c) is not modelled.
- s 14(4)(c)'s proviso is garbled in the deposit (a second "(c)" before "shall qualify");
  it was read as one sentence.
- Bequests to public institutions (s 12), which also come out of the rate base, are not
  in the computation.
- Deaths before 1 April 1984, and the remission schedules, would need the First to
  Third and Seventh and Eighth Schedule tables re-read from the PDF.
- No case law or IRAS practice was consulted.
