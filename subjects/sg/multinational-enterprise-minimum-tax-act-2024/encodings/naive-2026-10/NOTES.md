# Multinational Enterprise (Minimum Tax) Act 2024 — naive encoding

**Method: naive.** Straight from the deposited text, nothing else. The
`writing-l4-rules` skill could not be loaded in this session, so the
conventions of the finished naive rows were followed instead. No pipeline, no
coverage table, no independent test pass, no human gate. NOT for public use.

**Edition:** informal consolidation, "version in force from 20/3/2025" (the page
footer of `../../registers/source-bundle/MEMTA2024.txt`, retrieved 1 October 2026).
The latest amendment annotated is Act 25 of 2025, with effect from 1 January 2025.
Section numbers follow the body. The arrangement of sections at the top of the
deposit is off by one. Several fractions are garbled in the .txt, and the
reading of each is stated at the rule.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers requirement **REQ-0077**: Tier 2 of the remaining Singapore Acts,
ordered by everyday-life relevance. The requirement asks what the Act decides for a
person or business it applies to. No scenario has asked a sharper question yet.

The Act runs to about 130 pages, and most of it computes GloBE income and covered
taxes (First Schedule). This row covers what a group meets first. That means
whether the Act reaches it (ss 2, 7, 8) and who is charged with MTT and DTT
(ss 12, 13, 28). It also covers the top-up arithmetic (ss 15 to 18, Second
Schedule), the de minimis exclusion (s 19), registration and the surcharge
(ss 31, 36), the return and payment deadlines (ss 40 to 45), and the offences
(ss 64, 66, 68, 69). The following are not encoded:

- the First Schedule;
- additional current top-up amounts (s 21);
- stateless entities, investment entities and joint ventures (ss 22 to 25);
- multi-parent groups (s 26);
- negative tax carried forward (s 17(4));
- safe harbours (s 20);
- currency (s 9);
- assessments, objections, appeals and recovery (Parts 6 and 7);
- everything left to regulations.

## What the Act turns out to say

### 1. A purely domestic group is outside the Act, however large

s 2(1) defines "MNE group" as a group with at least one entity or permanent
establishment "not located in the jurisdiction of the ultimate parent entity". s 8
applies the Act only to MNE groups. A Singapore group with EUR 800 million of
revenue in every year but no foreign entity therefore owes neither MTT nor DTT,
even though DTT taxes only Singapore entities (s 29). Asserted.

### 2. The EUR 750 million test looks backwards, two years out of four

s 8(1): the Act applies for a financial year beginning on or after 1 January 2025.
The test is that consolidated revenue "for at least 2 financial years out of the 4
financial years immediately before" reached the threshold. That threshold is
EUR 750 million scaled by months over 12 (s 8(2)), and equality counts. One big
year in four is not enough. *Inference:* the encoding scales each earlier year by
its own length, so a 6-month year is tested against EUR 375 million. The text says
only "the threshold for a financial year". Asserted.

### 3. A return is due even when no tax is, and the deadline is 18 months, then 15

ss 41(1)(a) and 43(1)(a) require "a return stating that fact" where nothing is
payable. The due date for returns and the GloBE information return is 18 months
after the end of the transition year and 15 months after every later year
(ss 40(4), 41(3), 43(4)). Payment follows within one month, "without demand", in
Singapore dollars (ss 42, 44). Asserted.

### 4. The top-up arithmetic: 15% minus the effective rate, on profits above a shrinking carve-out

The top-up tax percentage is the 15% minimum rate less the effective tax rate,
floored at nil (s 16(5)). The effective rate is deemed 15% where GloBE income is
nil or negative, and nil where taxes are negative against positive income
(s 17(2), (3)). The carve-out is a percentage of payroll plus a percentage of
tangible assets (s 18). It falls each year from 9.6% and 7.6% for 2025 to 5% from
2033 (Second Schedule). A jurisdiction's top-up amount is (H × I) + J − K
(s 16(4)), where K is a foreign qualified domestic top-up tax. When the top-up
amount is computed for DTT, "K is nil" (s 30(2)(b)). Asserted (K is a
parameter, and the asserted case sets it to the full amount).

### 5. Small jurisdictions can drop out, but only by election

s 19: if the three-year average revenue is below EUR 10 million and the average
GloBE income is below EUR 1 million, the top-up amounts are deemed nil, but only
"if ... the filing entity ... so elects". Asserted.

### 6. Penalties scale with fault: once, twice, three and four times the tax

An incorrect return carries a penalty equal to the tax understated. A negligent
one carries double and a fine up to $5,000. A wilful one with intent to evade
carries treble and up to $10,000 (s 68(1) to (3)). False books or fraud carry four
times the tax and up to $50,000 or 5 years (s 69). Failing to file for 2 years or
more carries double the assessed tax (s 64(2)). Repeat evaders face a mandatory
minimum of 6 months' imprisonment (ss 68(4), 69(2)). Failing to register costs a
surcharge of 10% of the MTT and DTT assessed (s 36(2)). Asserted.

## What would need doing before this is worth anything

- The First Schedule (GloBE income or loss, adjusted covered taxes, excluded
  entities), without which no real top-up amount can be computed.
- The Multinational Enterprise (Minimum Tax) Regulations, which the Act leans on
  throughout (currency, safe harbours, recalculations, adjustments). None were
  retrieved.
- s 19(2) and (3) (disregarded years and rescaling of short or long years), s 21,
  and the minority-owned and joint-venture rules.
- A check of the garbled formulae (ss 8(2), 15(2), 16(2), 17(1)) against the PDF.
- No IRAS guidance or case law was searched.
