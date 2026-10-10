# Extradition Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments annotated
to Act 15 of 2026 (in force 1 July 2026) shown. Nearly every provision encoded here
was substituted by Act 17 of 2022 (wef 1 July 2022) or Act 31 of 2022 (wef 1 November
2022), although the cover page still says the edition incorporates amendments only
"up to and including 1 December 2021".

**Checks:** one case file, 78 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. This row takes the questions a
fugitive's counsel meets first: is the offence an "extradition offence" (s 2), does a
bar to surrender apply (ss 8, 9, 28), must or may the Minister refuse (ss 8(8), 10,
29), and what clocks run (ss 15A, 17, 18, 19, 22), plus the Malaysian route's offence
threshold, discretion and discharge clock (ss 32(2), 36, 38). How the Act comes to
apply to a State (ss 3-6, 40, 41), warrants, search, bail and property (ss 11-15, 20),
extradition to Singapore (ss 23-26), evidence (ss 42-46) and simultaneous requests
(s 49) are not encoded. The First Schedule's excluded offences turn on definitions in
the Mutual Assistance in Criminal Matters Act 2000 and are taken as a given fact.

## What the Act turns out to say

### 1. The same facts bar surrender to a foreign State but only permit refusal to a Commonwealth territory

A conviction in absence (without deliberate absconding or an assured retrial) and a
prosecution that is time-barred abroad are bars for a **foreign State**: s 8(5), (6)
say the person "is not liable to be surrendered". s 9, for a **declared Commonwealth
territory**, has neither. The same facts appear only in s 29, where the Minister "may
decline" (in absence; immunity "because of any reason, including lapse of time or
amnesty"). So an in-absence conviction from a Commonwealth territory leaves the person
liable to surrender, subject to ministerial discretion. Asserted.

### 2. Murder can be political when a foreign State asks, but not when a Commonwealth territory does

s 28(1) declares murder and offences against heads of state, heads of government and
ministers "are not offences of a political character" -- but only "For the purposes of
section 9(1)", the Commonwealth-territory bar. s 8(1), for foreign States, has no such
list, so the political-offence bar can still apply to the same conduct. Asserted.

### 3. Two years both ways, and tax offences count

An "extradition offence" on a request from abroad needs a maximum of at least 2 years'
imprisonment under the requesting law **and** under Singapore law for the equivalent
conduct, which must not be an excluded offence (s 2(1)). s 2(3) says an offence is not
kept out "merely because it is an offence of a purely fiscal character". The Malaysian
route (Part 6) uses a different word and test: "offence" means an arrestable offence or
one punishable with 6 months or more under the law of Malaysia (s 32(2)). Whether a
Singapore-equivalence test also applies to Malaysia is not stated in Part 6; this
encoding infers it does not. Asserted (the Part 6 inference is labelled as such in the
module).

### 4. Unjust or oppressive: the Minister must refuse; for Malaysia the Magistrate may

s 10(2): if surrender would be "unjust, oppressive or too severe a punishment" because
of triviality, bad faith, the passage of time or any other sufficient cause, the
Minister "must not" proceed. s 36, on the Malaysian route, takes the same finding and
says the Magistrate "may" release, defer or make another order. s 10(1) (persecution on
grounds of race, religion, sex, ethnic origin, nationality or political opinions) is
also mandatory. Asserted.

### 5. A short remaining sentence is a discretion, and only for foreign States

s 8(8): when a foreign State seeks surrender to enforce a sentence, the Minister may
refuse if the remainder is shorter than the treaty's minimal period, or under 6 months
where no treaty period is specified. Nothing equivalent appears in s 9. Asserted.

### 6. The clocks

Remand of at most 7 days at a time (s 15A(2)); review notice within 15 days of the
Magistrate's order (s 17(4)); no surrender until after 15 days from committal unless
the prisoner waives review (s 19); a reference to the Court of Appeal within 15 days,
with the Attorney-General needing no permission (s 18); and release on application if
still in custody 2 months after the latest of committal, review and reference (s 22)
-- one month on the Malaysian route (s 38) -- unless reasonable cause for the delay is
shown. "After the expiry of the period of 15 days" in s 19 is read as from day 16;
that is an interpretive choice. Asserted.

## What would need doing before this is worth anything

- The First Schedule (excluded offences) was not encoded; it depends on the Mutual
  Assistance in Criminal Matters Act 2000 definitions and a long table, which was not
  checked for column shifts.
- The "or any more severe punishment" limb of s 2(1) (eg death) is not modelled; it
  must be given as a long maximum term.
- The Gazette notifications and declarations that decide whether the Act applies to a
  given State or territory (ss 3-6), and any treaty limitations, were not retrieved.
- s 28(2) (the Minister may restrict the s 28 list by order) and s 41(2) (Convention
  offences deemed not political) are not modelled.
- No extradition case law was searched.
