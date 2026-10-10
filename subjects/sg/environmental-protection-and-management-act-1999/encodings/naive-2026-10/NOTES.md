# Environmental Protection and Management Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (the deposit says "Current
version as at 01 Oct 2026"), with amendments to Act 15 of 2026 (in force 1 July 2026)
shown.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes the duties and
offences an occupier, owner, trader or contractor meets: scheduled premises and the
First Schedule thresholds (s 6), the new owner's notice (s 9), dark smoke (s 11),
discharges into drains and land (s 15), toxic and hazardous discharges into inland
water (s 17), the hazardous substances licence (s 22), the principal contractor's
liability (s 35), and the penalty and composition arithmetic (ss 9, 15(5), 16, 17, 18,
25, 27, 28(4), 49, 67, 72). Not encoded: administration, the s 7 conditions and s 8
works permits beyond their penalty, air impurity standards (left to regulations),
the Director-General's notice powers, noise surveillance (s 28A), licences generally,
controlled works (Part 9A), greenhouse gases (Part 10A), enforcement powers, cost
recovery, and the Second Schedule list of hazardous substances.

## What the Act turns out to say

### 1. A second toxic discharge means prison: a minimum term, and the fine as well

s 17(1)(a): a first conviction for discharging a toxic or hazardous substance into
inland water carries a fine up to $50,000 **or** up to 12 months **or** both. On a
second or subsequent conviction the offender "be punished ... with both imprisonment
for a term of not less than one month and not more than 12 months and a fine not
exceeding $100,000". It is the only mandatory term in the provisions read. No
prosecution under s 17 may start without the Public Prosecutor's written consent
(s 17(6)). Asserted.

### 2. The principal contractor answers for pollution on site, and only due diligence gets them out

s 35(2): when s 14, 15 or 17 is contravened at a construction site, the principal
contractor is presumed to have had control, knowledge and to have permitted it. The
knowledge and permission presumptions are "not rebutted unless the defendant proves
that the defendant had exercised due diligence" (s 35(3)), and that requires "all
reasonable measures ... including all the measures prescribed" (s 35(4)). Taking
reasonable measures but missing one prescribed measure is not enough. The control
presumption is rebuttable by ordinary contrary proof. Asserted.

### 3. The occupier is presumed to be the discharger — unless the occupier is that principal contractor

s 15(2) and s 17(5)(d): matter discharged from premises is presumed, until the contrary
is proved, to have been discharged by the occupier, "other than a principal contractor
to which section 35 applies". The principal contractor is caught by s 35 instead.
Asserted.

### 4. Scheduled premises turn on hard thresholds, some inclusive and some not

First Schedule: concrete works need a batch capacity "greater than 0.5 cubic metre"; a
boiler of "2,300 kilograms or more per hour"; an incinerator or furnace burning "500
kilograms or more" of solids or "220 kilograms or more" of liquid an hour; storage of
"more than 100 tonnes" of toxic chemicals or "more than 1,000 tonnes" with a flash point
below 55°C. So exactly 100 tonnes of toxics is outside, and a 2,300 kg boiler is inside.
Occupying or using such premises without written permission is an offence (s 6).
Asserted.

### 5. Hazardous substances carry heavier default penalties than the rest of the Act

s 67 (the default for offences outside Part 7): $20,000, then $50,000 on a repeat
conviction, plus $1,000 / $2,000 a day for a continuing offence, and **no
imprisonment**. s 27 (the default inside Part 7): $50,000 **or** two years **or**
both, plus $2,000 a day. Using scheduled premises without permission or emitting dark
smoke cannot, on the text, lead to prison; dealing in hazardous substances without a
licence can. The fines and the two-year term are asserted; the absence of a prison
term under s 67 is encoded but not asserted.

### 6. Composition is capped at half the maximum fine, and never more than $15,000

s 72(1): "the lower of" half the prescribed maximum fine and $15,000 — so a $20,000
offence compounds for at most $10,000, a $50,000 offence for at most $15,000. Only
offences prescribed as compoundable qualify. Whether the daily continuing fine counts
toward "the maximum fine" is not said; the encoding leaves it out (an inference).
Asserted.

### 7. A noise stop-work order is fined by the day

s 28(4): ignoring a stop-work notice under s 28(3) carries "a fine not exceeding
$10,000 for every day during which the notice is not complied with" or 3 months or
both. Asserted.

### 8. A licence to deal in hazardous substances is personal

s 22(2): a licence "is not transferable" and authorises no individual "other than the
individual named in the licence". Holding someone else's licence is no defence.
Asserted.

## What would need doing before this is worth anything

- The Second Schedule (which substances are hazardous, and the exclusions) is scrambled
  across its two columns in the .txt deposit; it would have to be read from the PDF.
- "Dark smoke", the permitted periods of emission, effluent treatment and air impurity
  standards are all left to regulations, none of which was retrieved.
- First Schedule paragraph (a) lists fourteen kinds of works; only six are named in
  the encoding, the rest folded into one value. Paragraph (b) was read as applying the
  500 kg / 220 kg rates to both incinerators and furnaces.
- Part 9A (controlled works) and Part 10A (greenhouse gases) are substantial and
  unencoded.
- No case law or NEA guidance was searched.
