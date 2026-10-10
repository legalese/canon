# Debtors Act 1934 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 April 2022), deposited as `DeA1934.txt`. The revised edition incorporates
amendments up to 1 December 2021; the latest amendment annotated is Act 25 of 2021,
in force 1 April 2022.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0033** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet. The Act
has 27 sections, so most of it is here: arrest and committal of judgment debtors
(ss 3, 6, 8, 9, 12, 22, 24(7)-(9)), the defaulting trustee (s 10), arrest and
attachment before judgment (ss 13, 15, 17, 20), compensation (s 21), fraud debts and
compositions (s 26) and the fraudulent-debtor offence (s 27). Left out: the manner of
examination (s 4), interim protection orders (s 5), rule-making (s 7), discharge and
variation (ss 11, 16, 24(10), 25), sureties (s 14), release and sale of seized property
(ss 18, 19), the judgment debtor summons procedure (s 24(1)-(6), (11)), and every rule
of court the Act defers to.

## What the Act turns out to say

### 1. You cannot be jailed for a debt you never had the means to pay

s 6(4) and s 24(9): a debtor "shall not be committed to prison ... unless it appears
that he has ... had sufficient means" to pay since the judgment or order. A debtor who
defaulted, was personally served and showed no cause still cannot be committed if he
never had the means. Asserted.

### 2. Prison does not pay the debt, and the creditor's costs are added to it

s 12: no imprisonment "shall operate to satisfy or extinguish any debt" or stop
enforcement against property. s 9: the costs of arrest and imprisonment are added to the
judgment debt unless the court orders otherwise. A debtor who serves six weeks owes the
same as before, plus the creditor's expenses. Asserted.

### 3. Arrest before judgment is only for people who live or trade here

s 13(1) applies only to "a defendant who carries on business or ordinarily resides
within the jurisdiction", and never in an action for possession of immovable property.
A visitor with no business or home here, about to leave, cannot be arrested under s 13,
however strong the claim (attachment of property under s 17 has no such limit).
Paying the sum specified in the order to the officer prevents the arrest. Asserted.

### 4. Three different ceilings: 6 weeks, 6 months, 1 year

Civil committal of a judgment debtor (ss 6(1), 6(3), 24(8)) and detention for want of
security (s 15(2)) are capped at 6 weeks. A trustee who fails to pay money into court
faces up to 6 months (s 10), unless he "acted innocently", and must be released on
payment; s 22 keeps s 10 out of the District Courts. The fraud offence in s 27 carries
up to one year, a fine (no maximum stated), or both. Asserted.

### 5. A wrongly arrested defendant gets at most $500 under the Act

s 21(1): compensation for an arrest or attachment applied for on insufficient grounds is
"not exceeding $500", and taking it "shall bar any action for damages"; the defendant may
sue for damages instead. Asserted
(the cap; the bar on suing is encoded but not asserted).

### 6. Hiding property is a crime only within 2 months before, or after, an unpaid judgment

s 27(c) catches concealing or removing property with intent to defraud creditors "since
or within 2 months before" an unsatisfied judgment. Concealment three months before the
judgment, or concealment where the judgment was later paid, falls outside (c), though
(a) false-pretence credit and (b) fraudulent gifts or transfers have no time limit.
Asserted.

### 7. Attaching property before judgment does not make the claimant secured

s 17(1) lets the Sheriff seize property before trial where the defendant has vanished
abroad, cannot be served, or is hiding assets, but the order "shall not constitute the
claimant a secured creditor" in the defendant's bankruptcy. Property in official
Government or armed-forces custody needs the Attorney-General's written consent (s 17(2)).
s 20 gives priority to a creditor whose judgment came within one year before the seizure
and who had an enforcement order first; "one year" is read as 12 months (an inference).
Asserted, except the bankruptcy point, which is quoted only.

### 8. Fraud debts survive a composition

s 26: a debtor who compounds with creditors remains liable for any debt incurred,
increased, or forborne by fraud, unless the defrauded creditor assented otherwise than by
proving and taking dividends. Asserted.

## What would need doing before this is worth anything

- The rules of court the Act defers to (examination, deposits, notices to show cause) were
  not read; most of the procedure the Act describes lives there.
- No case law on "sufficient means", "probable reason" or s 13 was searched.
- The relation to bankruptcy law (s 17(1) mentions adjudication) was not traced.
- The court's discretion ("may") is encoded as permission only; nothing models how it is
  exercised.
