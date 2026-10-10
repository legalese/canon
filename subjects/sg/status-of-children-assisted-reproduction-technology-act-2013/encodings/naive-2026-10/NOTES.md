# Status of Children (Assisted Reproduction Technology) Act 2013 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
deposited as the informal consolidation in force from 15/10/2024. The latest
amendment annotated is Act 25 of 2021, in force 15/10/2024 (s 10(2), (3)).

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its everyday relevance: it decides who a child's legal mother and father
are after IVF, donor eggs or sperm, artificial insemination, or a clinic mix-up. The
Act is short, so this row takes nearly all of it: where it applies (s 3), written
consent (s 4), donors and the gestational mother (ss 5, 6), the husband and the
later-married partner (s 7), the court's power over an unmarried partner (s 8),
mix-ups (s 9), who may apply (s 10), legitimacy (s 11) and children born before
1 October 2014 (s 15). Not encoded: void marriages (s 2(2)), the welfare factors in
s 10(7) (listed in comments, not weighed), ancillary orders (s 10(8)), when a court
order takes effect (s 10(9)), and the rule-making powers (ss 13, 14). Dates are
abstract day numbers.

## What the Act turns out to say

### 1. A man who marries the mother after the procedure gets nothing under this Act unless he was already her partner or his sperm was used

s 7(1) covers a husband "at any time thereafter" only where the child was brought
about with his sperm. ss 7(2)–(6) cover a man who was her husband or de facto partner
**at the time of the procedure**. s 8 covers only a partner she was "not married to
... at any time after the fertilisation procedure". So a stepfather who met and
married the mother after a donor-sperm conception, and who has raised the child as
his own, is not the father under s 7 and cannot ask for a s 8 declaration. Asserted.

### 2. A known sperm donor becomes the father by marrying the mother

s 5 says the man whose sperm was used is not the father "except as determined under
this Act". s 7(1)(a) then makes a husband whose sperm was used the father if she
"was married at any time thereafter", from the later of the birth and the marriage.
A donor who later marries the mother is the father from the wedding day. Asserted.

### 3. When two men qualify on the same day, s 7(7) does not say who wins

s 7(7) picks "only the man who is to be treated as the father of the child earlier in
time". A husband at the procedure who consented to donor sperm is father from the
birth; a partner whose sperm was used and whom she married before the birth is also
father from the birth (s 7(4), the later of birth and marriage). The section gives no
rule for a tie, and this encoding returns one. Asserted.

### 4. Consent counts only if it is written, and silence is fatal to a husband's denial only by inference

s 4(a): consent is "deemed not to have validly given" unless in writing, wherever the
procedure was done. s 7(2) makes a husband the father "unless it is proved that he
did not consent". This encoding reads those together (an inference) so that a husband
who gave no written consent is not the father under s 7(2) — but becomes father under
s 7(3) from the day he accepts the child through a course of conduct. Asserted.

### 5. The carrying woman is the mother, even after a mix-up, unless a court acts within two years

s 6 makes the woman who carried the child the mother; s 5 excludes an egg donor. s 9(2)
decides a mix-up "as if" it had not happened, and s 9(3), (4) let the court declare
another person the parent only on an application made "within 2 years after" the
applicant discovered it. s 15(3) imposes the same two-year bar on children born before
1 October 2014, but only for mix-up cases (an inference about the rest). Asserted.

### 6. An unmarried partner is never the father without a court order

s 8(5): a de facto partner "is not to be treated as the father of a child unless the
court so declares", and s 8 applies only if no man is father under s 7, s 9 does not
apply and no earlier s 8 order exists. A partner who became her partner only after the
procedure qualifies only if his sperm was used. Asserted.

## What would need doing before this is worth anything

- The welfare factors in s 10(7) and the court's discretion in ss 8, 9(3) and 15 are
  not modelled; the encoding says only when the court *may* act.
- The two-year limits are counted in whole months, with 24 treated as within; the
  exact boundary is untested.
- The reading of "proved that he did not consent" as "no written consent" needs a
  lawyer's check, as does the s 7(7) tie.
- No case law, regulations or Family Justice Rules were searched.
