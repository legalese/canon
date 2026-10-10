# Sale of Commercial Properties Act 1979 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation
31 December 2021), informal consolidation "version in force from 1/7/2025", as
deposited at `../../registers/source-bundle/SCPA1979.txt`. The latest amendment
annotated is Act 15 of 2025, with effect from 1 July 2025. The arrangement of
sections at the top of the deposit is one line out of step with the body; the
encoding follows the body's numbers.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0031** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The Act is short, so nearly all of it is taken: when it applies (s 11), what is a
sale (s 3(2), (3)), the ban on selling before plans are approved (s 3(1)), the option
form (s 4), anonymous money (s 5A(1)), substantial shareholders and responsible
positions (ss 5D, 5E), the Controller's s 8 directions and the purchaser's
liquidated damages, officers' liability (s 9), composition (s 9A) and every penalty.
Not encoded: the content of the due diligence, record-keeping and programme duties
(ss 5A(2) to (4), 5B, 5C) beyond their penalties, the s 7A production powers beyond
s 7A(4), the s 10 rule-making power beyond the s 10(3) cap, and s 12. The rules made
under s 10 (option form, agreement terms, deposits, instalments, compoundable
offences) were not retrieved, and they are where most of a buyer's protection lives.

## What the Act turns out to say

### 1. A building of four units or fewer is outside the Act altogether

s 11(1)(a): the Act "does not apply" to a sale in a building that contains, or will
contain, "not more than 4 separate units". So a five-unit block is covered and a
four-unit block is not. s 11(1)(b) also takes out a unit once the certificate of
statutory completion **and** (where applicable) the subsidiary strata title have both
issued, so a completed unit still awaiting its strata title is inside the Act.
Asserted.

### 2. The ban on selling off-plan without approved plans binds "a person", not just a developer

s 3(1): "A person must not sell any commercial property unless the plans ... have been
approved by the Building Authority." Nothing confines it to developers. s 3 carries no
penalty of its own; s 6 punishes failure to comply with "any of the provisions" with
$10,000 or one year or both. That s 6 is the penalty for s 3 is an inference. Asserted.

### 3. A lease of up to 7 years is not a sale, unless it carries an option to renew or buy

s 3(3): a lease "for a term of years not exceeding 7 years without the option of
renewal or purchase" is not a sale. An 8-year lease, or a 3-year lease with an option
to purchase, is caught. Asserted.

### 4. A fraud conviction bars a director for 5 years from release; a money laundering conviction bars for ever

s 5E(2): the fraud-or-dishonesty disqualification ends 5 years from the conviction or,
if imprisoned, from release, "whichever date is later". The money laundering
disqualification (s 5E(1)(a)) and the bankruptcy one (s 5E(1)(c)) have no time limit.
Yet s 5D, which bars **substantial shareholders**, reaches only money laundering
convicts (and entities with one in a responsible position): a fraudster or bankrupt
barred from the board may still hold a substantial stake. Dates are modelled as whole
years. Asserted.

### 5. The sharpest penalties are for money laundering failures, and the longest prison term is for the disqualified director

Every s 5A to 5D duty, s 5E(1)(a) and s 7A(4) carry a fine up to $100,000 but no
imprisonment. Holding a responsible position after a fraud conviction or while
bankrupt carries $50,000 **or 3 years** (s 5E(5)), the only prison term above one year
in the Act. Disobeying a Controller's direction adds up to $1,000 a day after
conviction (ss 7(2), 8(2)). s 9A lets the Controller compound a prescribed offence
for at most half the maximum fine. Asserted.

### 6. The Controller's directions do not take away the buyer's liquidated damages

s 8(3): exercising the s 8 power "does not prejudice the right of the purchaser to
claim liquidated damages" for late completion. s 8(5) reaches property sold before the
Act began on 20 July 1979, and s 8(4) gives "developer" a wider meaning for s 8 than
s 2 does. Asserted (s 8(3) only).

## What would need doing before this is worth anything

- The Sale of Commercial Properties Rules (option form, agreement terms, deposit and
  instalment limits, compoundable offences) were not retrieved, so nothing here says
  what a buyer pays or when.
- A Minister's exemption under s 11(2) is treated as total; real exemptions may be
  partial or conditional.
- The "position analogous to" limbs of s 5E(3) are not modelled.
- No case law was searched.
