# Civil Law Act 1909 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit's arrangement
of sections is out of step with the body; the encoding follows the body.

**Checks:** one case file, 66 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**18 of the 527 Singapore Acts** deposited here cite it (s 5 by 6, s 20 by 4). It is a
miscellany. This row takes the provisions an ordinary person relies on: wagers,
litigation funding, contracts that must be in writing, contribution, death claims,
survivorship, contracts by 18-to-20-year-olds, and medical advice. Not encoded: law
and equity, s 4 insolvency rules, interest (s 12), choses in action, perpetuities and
accumulations, and the trust and estate sections.

## What the Act turns out to say

### 1. A former wife is a dependant; a former husband is not

s 20(8)(a): "the wife or husband or former wife of the deceased". A former husband
does not appear anywhere in the list. s 22(3) disregards a **widow's** remarriage or
her prospects of remarriage; nothing is said of a widower's. s 22(3A) lets a former
wife recover only to the extent of a subsisting maintenance order. Asserted.

### 2. A settler can recover contribution without admitting liability

s 15(4): someone who settles "in bona fide settlement or compromise" may recover
contribution "without regard to whether or not he himself is or ever was liable",
provided he would have been liable on the facts alleged. A settlement of a hopeless
claim recovers nothing. And s 15(3): a co-wrongdoer whose own liability has been
extinguished by limitation does not have to contribute. Asserted.

### 3. Bereavement damages are $15,000 split down a strict line

s 21: the spouse takes all of it; only if there is no spouse do the children share it;
then the parents; then the siblings. Three children get $5,000 each; a surviving
spouse shuts the children out entirely. The claim does not survive the claimant.
Asserted. **Simplified:** the step-parent class (s 21(2), for a deceased minor) is not
modelled.

### 4. An 18-year-old can sign a phone contract but not buy a flat

s 35: a contract by someone aged 18 to 20 has effect as if they were of full age,
**except** land dealings (other than a lease of up to 3 years), a lease over 3 years,
dealings with trust interests, and settling the young person's own claims. Asserted.

### 5. Medical advice: peer opinion is not enough

s 37 is a modified *Bolam*. Peer opinion must be logical, and it counts only if it
requires the patient to be told what a reasonable patient would need **and** what the
doctor knows or ought to know matters to **this** patient, even for "an idiosyncratic
reason". Withholding needs reasonable justification. Illustration (c): fear that the
patient would refuse treatment is not, by itself, a justification. Asserted.

### 6. Smaller things worth recording

- **s 5:** wagers are void, but bets with licensed or exempt operators are not, and
  neither are investment contracts made by way of business. Credit for gambling is
  never saved (s 5(3E)).
- **s 5B:** third-party funding is lawful only for a qualifying funder in prescribed
  proceedings. A funder that stops qualifying cannot enforce its rights, subject to
  relief.
- **s 6(d):** any disposition of an interest in land must be in signed writing. This is
  the rule that the Electronic Transactions Act First Schedule protects (see the
  electronic-transactions-act-2010 row).
- **s 30:** when the order of death is uncertain, the younger is deemed to have
  survived the elder.

## What would need doing before this is worth anything

- **No case law was searched.** Part performance and proprietary estoppel qualify s 6
  in practice, and s 37 codifies *Hii Chii Kok*; neither is reflected.
- The s 5B regulations (qualifying funders, prescribed proceedings) were not retrieved.
- s 21's step-parent class and the child-of-the-family route are not modelled.
