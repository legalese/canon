# National Servicemen (Employment) Act 1970 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which by its own account incorporates all
amendments up to and including 1 December 2021 and came into operation on
31 December 2021. Its Legislative History lists only Act 28 of 1970 and the 1970
and 1985 Revised Editions: no amending Act is annotated.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it is
the Act about jobs for men who have completed full-time national service, and
about the employers who hire them. It is short, so this row takes nearly all of
it: the register (ss 2, 4), the Minister's order to hire only from the register
and its exceptions (s 5), consent and appeal (s 6), the duty to report a new job
(s 7), entry, information and summons powers and their offences (ss 8, 9), and
corporate officers (s 10). Not encoded: appointments (s 3), the form of the
register (s 4(2)), varying or revoking an order (s 5(6)), the Appeals Board's
composition (s 6(3)) and the rule-making power (s 11).

## What the Act turns out to say

### 1. The Act does nothing on its own; everything turns on an order the deposit does not contain

The duty to hire only registered persons exists only where the Minister has made
an order "published in the Gazette" under s 5(1), and only for the employers and
employees the order names (s 5(3)). The deposit contains no such order, and
nothing in it says whether one is in force. With no order, no hiring contravenes
the Act. Asserted.

### 2. A serviceman who fails to report his new job loses his place on the register, and nothing more

s 7(1): a registered person must notify the Director in writing "within 7 days"
of securing employment. s 7(2): failure means he "shall have his name deleted from
the register". The deletion is mandatory, but there is no fine and no offence.
Asserted (day 7 keeps the name; day 8 or no written notice loses it).

### 3. The employer's fine grows by the day, but the employee's contract survives

s 5(4): up to $2,000, plus up to $50 "for every day" each employee is wrongly
employed; no imprisonment. So 30 employee-days gives a maximum of $3,500, and 90
gives $6,500. s 5(5): the employee is not, "by reason only of that contravention",
employed under an illegal contract. Asserted.

### 4. Old duties to hire are protected, frozen at 2 January 1971

s 5(2): no order applies where the employer would have had a duty to take the
person on by written law or "by virtue of any agreement made before 2 January
1971" — the Act's commencement date. Agreements made later get no such
protection. Asserted.

### 5. A 14-day appeal, and then no court

s 6(2): a refused employer may appeal to the Appeals Board "within 14 days of the
refusal"; s 6(4): the Board's decision "shall not be called in question in any
court". How the 14 days are counted is not stated; the encoding counts calendar
days after the refusal (an inference). Asserted.

### 6. The summons offence is only about turning up

s 9(1) requires a summoned person to attend and "answer truthfully", but s 9(2)
punishes only one who "neglects to attend" ($500 or 3 months). A knowingly false
statement is caught instead by s 8(2)(c), with obstruction and non-production
($1,000 or 6 months). Homes used solely as dwellings cannot be entered (s 8(1)(a)).
Asserted.

### 7. The deposit's table of contents is off by one

The Arrangement of Sections pairs each heading with the next section's number
(for example "2. Short title"). The body is consistent, and this encoding follows
the body. Not asserted.

## What would need doing before this is worth anything

- Find out whether any order under s 5(1), or any rules under s 11, have been made
  and are in force; none was retrieved. Without them the encoding has nothing to
  bite on.
- "Registered person" may be conditioned by rules under s 11(a) (conditions of and
  disqualifications from retention on the register); the encoding treats
  completion of full-time national service as sufficient.
- No case law or practice on the Act was searched.
