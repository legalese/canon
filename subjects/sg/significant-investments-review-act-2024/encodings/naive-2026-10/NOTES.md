# Significant Investments Review Act 2024 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act No. 1 of 2024, informal consolidation, version in force from
28/3/2024, as deposited at `../../registers/source-bundle/SIRA2024.txt`. The deposit
annotates no amending Act or subsidiary legislation.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0079**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet.

The row takes what an investor, a designated entity and its officers meet: the
controller thresholds (s 16), notice by a Level A controller (s 18), prior approval
(s 19), the entity's duty to report (s 20), void transactions (s 21(1)), approval of
officers (s 27), the two-year look-back (s 32(1)-(3)), the Part 3 penalties (s 36) and
reconsideration before appeal (ss 38, 39). Not encoded: administration (Part 2), the
meanings of "equity interest" (s 14) and "associate" (s 15) — the encoding takes the
person's percentage, alone or with associates, as given — remedial directions
(ss 22-25), winding-up restrictions (s 26), removal of officers (s 28), special
administration (ss 29-31), the s 32 directions and their effect (ss 32(5)-(9), 33),
information and enforcement powers (ss 34, 35, Part 5) and the Reviewing Tribunal
(ss 40-45). Only the default percentages in s 16(2) are encoded; no regulations
prescribing others were retrieved.

## What the Act turns out to say

### 1. The look-back reaches entities that were never designated

s 32(1) applies to any entity incorporated in Singapore, carrying out "any activity"
in Singapore, or providing "any goods and services to any person in Singapore". If,
after any acquisition or disposal of equity or voting control, the entity "has acted
against the national security interests of Singapore within a period of 2 years after
the transaction", the Minister may publish a review notice within 2 years and 30 days
(s 32(3)) and then direct divestment (s 32(5)). A certificate from the Minister for
internal security is "conclusive evidence" of the act (s 32(9)). The encoding takes
2 years as 730 days; that is an inference. Asserted.

### 2. Fines are measured by the deal, not capped by a figure

s 36(1): for failing to notify (s 18(3)), acting without approval (s 19(10)), an
entity failing to report (s 20(2)) or breaching a validation-notice condition
(s 21(11)), the maximum fine is "the higher of" the transaction value and $500,000
for an individual, or $1 million for anyone else. For other Part 3 offences a
company faces the higher of 10% of annual turnover (from its latest audited accounts)
and $1 million. Individuals also face up to 3 years' imprisonment; continuing
offences add $50,000 or $100,000 a day. The value of a void transaction is taken "as
if the transaction were not void" (s 36(3)). Asserted.

### 3. Crossing 12%, 25% or 50% needs prior approval; 5% needs only notice

s 16(2) sets the defaults at 5%, 12%, 25%, 50% (and 50% and 75% for Levels Y and Z).
Becoming a Level A controller (5% to under 12%) needs only written notice within
7 days (s 18(1)); becoming a Level B, C or D controller needs the Minister's prior
written approval (s 19(1)(a)), and a transaction completed without it "is void"
(s 21(1)) unless validated. Because Level A is a band, someone who jumps from under
5% straight past 12% never becomes a Level A controller and owes no s 18 notice, but
does need s 19 approval. Asserted.

### 4. Going up past 75% needs approval too, on the words

s 19(1)(b) forbids a Level Y controller (50% to under 75%) to "cease to be a Level Y
controller" without approval. A holder going from 60% to 80% ceases to be a Level Y
controller even though it is increasing, and (a) is not engaged because it was
already a Level D controller. Read literally, every crossing of 75% or 50% in either
direction needs approval. Whether that is intended is not something the text says.
Asserted.

### 5. The controller levels overlap

Each level is satisfied by EITHER the equity limb OR the voting limb (s 16(1)), so a
person with 6% of the equity but 13% of the votes is on the words both a Level A and
a Level B controller. The duties in the encoding follow a single percentage; the
overlap is asserted only for the level definitions. Asserted.

### 6. Ignorance is a defence only with prompt self-reporting

s 18(4) and s 19(11): the accused must prove they were unaware and notified the
Minister within 14 days of becoming aware. s 18(5) and s 19(12): if an associate's
change caused the breach and there is no arrangement with that associate, notice
within 7 days of the contravention. For s 19 the accused must also have complied with
any remedial direction in time. Otherwise lack of intent is no defence (ss 18(6),
19(14)). Asserted.

### 7. Officers need approval; re-appointment on expiry does not

s 27(1): a CEO, director or board chair of a designated corporation may not be
appointed without the Minister's approval on the entity's application; s 27(5) lets
an approved individual be re-appointed "immediately upon the expiry" of the term
without fresh approval. Asserted.

### 8. Reconsideration first, within 14 days, and the courts are largely shut out

s 38(2)(b): reconsideration must be sought before the time stated in the decision,
no later than the 14th day. s 39(2): no appeal to a Reviewing Tribunal without it.
Decisions keep effect meanwhile (ss 38(7), 39(3)). s 46: decisions are final and may
be challenged in court only on compliance with procedural requirements. The encoding
counts "before the time" as "on or before the day" (a simplification). Asserted
(except s 46).

## What would need doing before this is worth anything

- The meanings of "equity interest" (s 14) and "associate" (s 15), which decide whose
  holdings are aggregated, are not encoded.
- The equity and voting limbs are collapsed into one percentage for the duties.
- No designation notices, regulations prescribing other percentages, or Guidelines on
  Fit and Proper Criteria were retrieved.
- No decided cases were searched.
