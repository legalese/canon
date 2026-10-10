# Government Proceedings Act 1956 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 8
of 2026 (wef 29 May 2026, s 7) and Act 25 of 2021 (wef 1 April 2022) shown.

**Checks:** one case file, 85 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**11 of the 527 Singapore Acts** deposited here cite it. This row takes what a
claimant against the Government, or a debtor of it, meets: which claims lie
(ss 4 to 7, 12, 14), who may sue over public nuisances and public trusts (ss 8, 9),
the priority of Government debts (s 10), whom to name as defendant (s 19), transfer
to the High Court (s 25), what relief a court may give (s 27), when to ask for a
certificate of the order (s 31) and proceedings in rem (s 35). Procedure, service,
costs, interest, enforcement by the Government, attachment, discovery, Rules of
Court and the savings in s 38 are not encoded.

## What the Act turns out to say

### 1. Anything done "in exercise of the public duties" is immune, except in contract and in works

s 7(1) says, "Notwithstanding any other provisions of this Act", that no proceedings
other than for breach of contract lie for anything done, omitted or refused "in
exercise of the public duties of the Government". s 7(3) carves back suits for
negligence or trespass in executing construction or maintenance works. So a
negligent public-duty decision is barred, but negligence in road works is not.
Act 8 of 2026 (wef 29 May 2026) widened the inclusive list in s 7(2) to flood
prevention, waterways and "coastal management". The list is inclusive, so the
encoding takes "public duty" as a fact found, and separately says which activities
s 7(2) names. Asserted.

### 2. No injunction, specific performance or recovery of land against the Government

s 27(1): where private parties could get an injunction or specific performance, the
court "shall not" grant one against the Government and may instead declare the
parties' rights; likewise no order for recovery of land or delivery of property,
only a declaration of entitlement. s 27(2) stops the same relief being obtained by
suing an officer instead. Asserted.

### 3. A judgment against the Government is paid on a certificate, never by execution

s 31(1): the successful party may apply for a certificate after 21 days from the
order, or after costs are assessed if that is later; s 31(3) the Government "shall
pay" it; s 31(4) no enforcement order or attachment issues against the Government.
The encoding reads "after the expiration of 21 days" as 22 or more days after the
order; that day count is an inference. Asserted.

### 4. Forces members injured on duty cannot sue in tort, and "forces" includes the police

s 14(1), (5): no tort liability, for the member or the Government, for death or
personal injury to another member who was on duty, on forces property, or
travelling to or from duty, if the Finance Minister certifies the harm attributable
to service. "Forces" includes the Singapore Police Force and its volunteer,
auxiliary and special police. The proviso, for acts unconnected with duty, names
only the member; read literally the Government stays exempt. That reading is
an inference from the words, encoded and asserted.

### 5. Government debts rank ahead of later debts, but not registered mortgages

s 10: a debt to the Government has preference over debts "subsequent to" its
accrual date, except a registered mortgage or charge of immovable property. A debt
incurred the same day is not "subsequent" and is not postponed. Asserted.

### 6. Tort liability is vicarious and narrowly gated

s 5 makes the Government liable as a private principal for its agent; s 6 adds
that the officer must have been personally liable, not acting judicially, and paid
wholly from Government revenues or a certified fund. IP infringement lies only if
committed with the Government's authority after 25 February 1965 (s 12).
Asserted.

### 7. Public nuisance and public trusts are the Attorney-General's, or two people's with consent

ss 8, 9: the Attorney-General, or two or more persons with the AG's written consent
(for trusts, persons with an interest in the trust), may sue; for a public nuisance
no special damage is needed. One person alone cannot. Asserted.

## What would need doing before this is worth anything

- The gazetted list of authorised departments (s 19(1)) and the Rules of Court
  under s 37 were not retrieved; s 37(2) requires rules on default judgment, summary
  judgment and set-off against the Government, none encoded.
- "Public duties", "personally liable" and "reasonable belief" (s 35) are facts
  taken as inputs; no case law was searched.
- The 21-day count in s 31 and the reading of the s 14(1) proviso are inferences.
