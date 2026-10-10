# Insolvency, Restructuring and Dissolution Act 2018 — naive encoding

**Method: naive.** Straight from the deposited text, following the
`writing-l4-rules` conventions of the example rows (the skill itself was not
loadable in this session). No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
30/9/2026, as deposited at `../../registers/source-bundle/IRDA2018.txt`. The
revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated is Act 8 of 2026 wef 29/05/2026. The arrangement of sections
at the top of the deposit is one number out of step in Part 20 (it lists
"Obtaining credit ..." as s 411; the body numbers it s 412). The body is followed.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings. A
deliberately wrong copy of one assertion was run and reported as failing, to
confirm the runner sees failures.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it is the law under which an
individual with unpaid debts can be made bankrupt, and it says what bankruptcy then
does to them. The Act runs to several hundred pages and most of it concerns
companies. This row takes personal bankruptcy as an individual meets it: who can be
made bankrupt and on what debt (ss 310 to 316), the mandatory referral to a debt
repayment scheme (ss 316(9), 318(3), 290, 291), what the Official Assignee takes
(s 329), gifts and preferences that can be unwound (ss 361 to 363), discharge by
the Official Assignee (ss 395, 396), what discharge does not release (s 397), the
bankrupt's disqualifications and disabilities (ss 400, 401), and two offences
(ss 412, 413, with s 404 and s 417).

Not encoded: corporate insolvency, judicial management, schemes and winding up
(Parts 4 to 12), cross-border insolvency, insolvency practitioners, voluntary
arrangements (Part 14), the running of a debt repayment scheme once it starts,
proof of debts and priority (ss 345 to 356), the monthly and target contribution
(s 339 lists factors but gives no formula), annulment and discharge by the Court
(ss 392 to 394), and the other Part 20 offences.

## What the Act turns out to say

### 1. Not knowing you are bankrupt excuses a $1,000 loan but not a $10,000 deposit

s 412(1) makes it an offence for an undischarged bankrupt, without saying so, to
obtain credit of at least $1,000, give a guarantee of at least $1,000, or (from
22 May 2026, per the annotation) take an advance payment of at least $10,000 for
goods or services. s 404(2) lets a bankrupt escape by proving he or she "did not
know or have any reason to believe" in the bankruptcy, but only for "412(1)(a),
(b) or (c)". Paragraph (d), the advance payment, is not listed. The general
no-intent-to-defraud defence in s 404(1) still covers all of s 412. Asserted.

### 2. A small debtor must be offered a repayment scheme before bankruptcy

Where a bankruptcy order "may be made", s 316(9) (and s 318(3) for a debtor's own
application) says the Court "must, instead of making the order, adjourn" for six
months and refer the debtor for a debt repayment scheme, if the debts are within a
"prescribed amount" and the debtor has had no bankruptcy, voluntary arrangement or
scheme in five years and is not a sole proprietor or partner. The prescribed amount
is not in the Act and was not retrieved, so it enters as a yes/no fact. A plan may
run at most five years (ss 290(1)(b), 291(7)). Asserted.

### 3. Discharge clocks stop while you are abroad without permission

A first-time bankrupt may be discharged by the Official Assignee after 3 years if
the target contribution is paid (or excused) and creditors at the "relevant
threshold" do not object, after 5 years if paid regardless of objection, or after
7 years in any case; a repeat bankrupt waits 5, 7 or 9 years (s 395(2)). Time spent
outside Singapore without the Official Assignee's permission "must be disregarded"
(s 395(5)). The section says the Official Assignee "must not" discharge "unless"
these hold and otherwise acts "in his or her discretion", so these are conditions,
not an entitlement; the encoding reads them as "may discharge". Asserted.

### 4. The objection threshold is lopsided

s 395(6): the relevant threshold of creditors is "not less than half in number or
more than one-fourth in value". Exactly half by number suffices; exactly a quarter
by value does not. On an objection the Court may bar discharge for up to 2 years,
but ordinarily not beyond 9 years after the administration date (11 for a repeat
bankruptcy) (s 396(11), (13)). Asserted.

### 5. Discharge leaves Government debts, MediShield Life premiums, fines and fraud debts

s 397(2) and (3): debts due to the Government, revenue-offence liabilities and
MediShield Life or CareShield Life premiums survive unless the Minister certifies
otherwise. s 397(5): fraud debts and fines are not released at all. s 397(6):
personal-injury damages, Women's Charter family orders and confiscation orders are
released only so far as the Court directs. Asserted.

### 6. The $15,000 floor, the 21-day demand, and what the Official Assignee leaves

A bankruptcy application needs debts of at least $15,000, liquidated and payable
immediately (s 311(1)). Failure to meet a statutory demand for 21 days raises a
presumption of inability to pay (s 312(a)); a creditor may apply sooner if the
debtor's property is at serious risk, but no order can be made until 21 days have
passed (ss 314, 316(2)). The annual bonus or AWS, the salary left after the monthly
contribution, tools and vehicles needed for work, and necessary household goods
stay with the bankrupt (s 329(2)). Asserted.

### 7. Gifts reach back three years; preferences one or two

A transaction at an undervalue can be unwound if made within 3 years before the
application; a preference to an associate within 2 years, any other within 1
(s 363(1)), and only if the individual was insolvent or became so as a result
(s 363(2)); insolvency is presumed for an undervalue with an associate (s 363(3)).
Asserted.

### 8. A bankrupt may sue for personal injury or divorce, but must travel only with permission

Without the Official Assignee's sanction a bankrupt cannot bring or defend any
action other than a personal-injury claim or a matrimonial proceeding (s 401(1)(a)),
and must not leave Singapore without prior permission (s 401(1)(b)); either breach
carries $10,000 or 2 years. A bankrupt cannot act as an executor or trustee without
the Court's permission (s 400). Asserted.

## What would need doing before this is worth anything

- Retrieve the subsidiary legislation made under the Act (none was retrieved) for
  the debt repayment scheme "prescribed amount" and any "higher amount" prescribed
  under s 412.
- The s 312(d) and s 363 variants for failed debt repayment schemes are not
  modelled.
- The monthly and target contribution (s 339) needs the regulations or Official
  Assignee practice to compute anything.
- No case law was searched; the meaning of "unable to pay", "associate" (s 364)
  and "extenuating circumstances" is taken at face value.
