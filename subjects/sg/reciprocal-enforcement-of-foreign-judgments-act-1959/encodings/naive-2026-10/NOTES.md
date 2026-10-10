# Reciprocal Enforcement of Foreign Judgments Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/REFJA1959.txt` (page furniture: "version in force
from 1/3/2023"). The cover says it incorporates amendments up to 1 December 2021;
later annotations shown are S 26/2022, Act 25 of 2021 (wef 1 April 2022) and the
repeal of Part 2 by Act 24 of 2019 (wef 1 March 2023). The arrangement of sections
at the top of the deposit is out of step with the body; the body's numbers are used.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**Requirement REQ-0045** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet. The Act is short, so this row takes nearly all of it: which
judgments it reaches (ss 2, 2A, 3), registration and the sum registered (s 4),
setting aside (ss 5, 6), the bar on suing instead (s 7), conclusive effect (s 11),
non-reciprocating countries (s 12) and certificates for Singapore judgments (s 13).
Not encoded: which countries and courts are gazetted under s 3 (no order was
retrieved), the Rules of Court and Family Justice Rules under s 8 (security for
costs, matters to be proved, the period to apply to set aside), interest rates, and
s 11(3).

## What the Act turns out to say

### 1. Punitive damages are cut down to compensation on registration

s 4(5): where a money judgment awards damages "in excess of compensation for the
actual loss or harm suffered", it "may only be registered for the amount of the
compensation" — but s 4(6) makes the court take into account how far the award
covers the costs of the foreign proceedings. A $300,000 award against $120,000 of
compensation registers for $120,000 plus the registration costs. Which comes first,
the cap or the deduction of part payments (s 4(9)), the text does not say; capping
first is an inference. Asserted.

### 2. Once a country is gazetted, registration is the only way in

s 7(1): no proceedings to recover a sum under a Part 1 judgment, "other than
proceedings by way of registration", are to be entertained in Singapore. The
creditor cannot simply sue on the foreign judgment as a debt. The only exception is
an order that operated before it was gazetted, for actions begun before
publication (s 7(2)). s 12 goes further for a country that treats Singapore
judgments substantially less favourably: no recovery proceedings at all, unless the
order directs otherwise. Asserted.

### 3. Registration must be sought within six years, and the bars are at the date of application

s 4(1): within 6 years of the judgment, or, where there was an appeal, after the
last appeal judgment (read here as six years from that judgment — an inference, as
(b) does not repeat the period). s 4(3): no registration if at the application date
the judgment is wholly satisfied, discharged or unenforceable in its own country.
A non-money judgment (an injunction, say) registers only if enforcement is "just
and convenient"; otherwise the court may register its monetary equivalent (s 4(4)).
Asserted.

### 4. Six grounds compel setting aside; the merits are not one of them

s 5(1)(a): the registration "shall be set aside" for (among others) lack of
jurisdiction, no timely notice to a defendant who did not appear, fraud, Singapore
public policy, or the applicant not holding the rights. An earlier conflicting
judgment, a defective notice of registration and a pending or intended appeal (s 6)
only allow it. Nothing in the Act lets the debtor reopen the merits. Asserted.

### 5. Appearing only to contest jurisdiction is not submission

s 5(3)(a)(i): voluntary appearance counts unless it was to protect seized property,
contest the jurisdiction or ask the court to decline it. A resident defendant who
stayed away is caught (iv) — unless the claim was brought in breach of an agreement
to settle the dispute elsewhere, which defeats (iv) and (v) but not submission or a
prior agreement to the forum (s 5(4)(b)). A foreign state with immunity that did not
submit is outside jurisdiction (s 5(4)(c)). Asserted.

### 6. A judgment can stay conclusive even after registration fails

s 11: a Part 1 judgment is conclusive between the parties on the same cause of
action, "whether or not it can be or is registered", unless set aside (or bound to
be) on a ground other than non-payment of money, satisfaction, or unenforceability
at origin. Setting aside for fraud ends it; setting aside because the judgment was
already paid does not. Setting aside for a pending appeal under s 6 is not among the
saved grounds, so on the text it ends conclusive effect too. Asserted.

### 7. A judgment for taxes or a fine is neither kind of judgment

s 2(1) excludes sums for taxes, similar charges, fines and penalties from both
"money judgment" and "non-money judgment". The Act does not say in terms that such a
judgment cannot be registered; whether it can is not encoded. The classification is
asserted.

### 8. Some setting-aside grounds expressly allow a second attempt

A defective or unserved notice (s 5(2)), a pending appeal or unenforceability at
origin (s 6(2)), and registration for the whole sum despite part payment (s 6(3),
where the court "shall" register the balance) leave the creditor free to register
again. For the other grounds the Act is silent. Asserted.

## What would need doing before this is worth anything

- The s 3 orders (which countries, which courts, which judgments) were not
  retrieved; without them the encoding cannot say whether any real judgment is
  within Part 1.
- The Rules of Court on registration (time to set aside, matters to be proved,
  security for costs) were not read.
- The interaction of s 4(5) and s 4(9), and the six-year period after an appeal,
  are inferences that need checking against case law.
- No case law was searched.
