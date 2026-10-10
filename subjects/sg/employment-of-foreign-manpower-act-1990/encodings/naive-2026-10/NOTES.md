# Employment of Foreign Manpower Act 1990 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/12/2025"), with amendments to Act 31 of 2023 (in force 1 December 2025) shown.

**Checks:** one case file, 118 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. This row takes what an
employer, a foreign worker or a construction principal contractor actually meets:
employing without a valid work pass and its penalties (s 5), the work-place occupier
offence (s 6A), terminating after revocation (s 9), self-employed foreigners (s 10),
when the levy stops (s 11), what a pass covers (s 12), kickbacks and phantom passes
(ss 22A, 22B, 23A), employer-borne costs and the Controller's financial penalties
(ss 9(3), 25, 25A), appeals (s 25G) and composition (s 27). Appointments, the
Controller's application and debarment powers (s 7), the register, custody and loss
of passes, inspection and arrest powers, prescribed-infringement procedure,
regulations, and the levy rates (set by order, not in the Act) are not encoded.

## What the Act turns out to say

### 1. The levy does not stop when the worker leaves

s 11(2): the levy "continues to be payable unless the work pass" has expired, been
suspended or revoked, or "been cancelled by the Controller on application by the
employer". The worker walking out is not on the list; only cancellation stops it, and
s 9(2) puts the cancellation application on the employer. Asserted.

### 2. Recovering the levy from the worker is not a kickback, but it is still penalised

s 22A(3) presumes any sum taken from a foreign worker to be consideration for the
employment, but carves out the charges the employer must bear under s 25(6) (levy,
pass fees, medical insurance and examinations, employer-required training,
repatriation "at any time"). Taking those from the worker is instead a prescribed
infringement under s 25(4): a financial penalty of up to $20,000, not a criminal
offence. A placement fee, a fee to keep the job or a security deposit falls squarely
in s 22A(1) (fine up to $30,000 or 2 years), and on conviction s 23A **requires** the
court to order repayment of an equal sum. An unexplained deduction is presumed a
kickback unless rebutted. Asserted.

### 3. A repeat company offender cannot be jailed; a repeat individual must be

s 5(6)(b): on a second conviction for employing without a valid pass, an individual
gets a fine of $10,000 to $30,000 **and** at least one month in prison; any other
offender gets a fine of $20,000 to $60,000 and no imprisonment. First convictions
carry a $5,000 minimum fine. Convictions at the same trial count as one (s 5(9)(b)).
Asserted.

### 4. Not knowing is no defence without checking the passport

s 5(4), (5): ignorance that the employee was a foreigner is a defence only with due
diligence, and there is no due diligence "unless the defendant had checked the
passport, document of identity or other travel document". s 6A(3) gives a
principal contractor three routes (keeping people out, checking the passport,
checking the original work pass). Reading the "or" as making them alternatives is an
inference. Asserted.

### 5. Phantom passes carry a presumptive six months, and caning at six convictions

s 22B(1): obtaining a pass for a business that does not exist, is not operating or
does not need the worker, and then not employing the worker, means "a presumptive
minimum term" of 6 months to 2 years. Charged with more than 5 and convicted of at
least 6 at one trial, caning follows (s 22B(2)), or a fine up to $10,000 in lieu
where the CPC bars caning. Asserted.

### 6. Honest mistakes and dishonest ones go down different roads

An employer who "inadvertently, or without intent to mislead or defraud," gives
inaccurate information faces a financial penalty up to $20,000 (s 25(3)); a statement
the person "knows, or ought reasonably to know" is false is an offence (s 22(1)(d)).
Composition is capped at the lower of half the maximum fine and $5,000 (s 27). An
appeal to the Appeal Board must be lodged within 14 days and suspends the
determination only if it is against a financial penalty or its amount (s 25G).
Asserted, except s 22(1)(d), which is quoted only.

## What would need doing before this is worth anything

- No regulations made under s 29 and no levy orders under s 11(1) were
  retrieved; the regulatory conditions, prescribed duties, and levy rates
  that give ss 11, 25(2) and 25A their content are all there.
- Whether the Minister has specified other "occupiers" under s 6A(7), or exempted
  anyone under s 4, was not checked.
- No case law on the s 22A(3) presumption or the s 22B presumptive minimum was
  searched.
