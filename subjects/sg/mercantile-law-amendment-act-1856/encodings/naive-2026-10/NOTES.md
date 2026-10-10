# Mercantile Law Amendment Act 1856 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MLAA1856.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. No later amendment is annotated. The legislative history in the
deposit records the English Act (19 & 20 Vict., c. 97, commencement 29 July 1856),
its application in Singapore from 12 November 1993 by the Application of English Law
Act 1993, and the 1994 Revised Edition (Cap. 388).

**Checks:** one case file, 41 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0042** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to. No scenario has asked a sharper
question yet.

The Act has three sections. This row takes both operative ones, ss 1 and 2, and
leaves out s 3 (short title). What a "proper indemnity", a "security" and a "just
proportion" are is taken as given facts or amounts. Whether a guarantee must be in
writing at all is not encoded: s 1 assumes a written, signed promise and says nothing
about an oral one.

## What the Act turns out to say

### 1. A co-guarantor who pays everything can recover only the other's fair share

s 2 lets a paying surety stand in the creditor's place against "the principal debtor,
or any co-surety, co-contractor, or co-debtor", but the proviso caps recovery from a
co-surety, co-contractor or co-debtor at "the just proportion to which, as between
those parties themselves," that person "shall be justly liable". Against the principal
debtor the claim is for the full "advances made and loss sustained". A guarantor who
paid $100,000 and lost $5,000 more can claim $105,000 from the borrower but only the
co-guarantor's share (here $50,000) from the co-guarantor. Asserted.

### 2. Paying off the debt does not wipe out the securities

s 2 gives the payer an assignment of "every judgment, specialty, or other security" held
for the debt "whether ... deemed at law to have been satisfied by the payment" or not,
and the payment "shall not be pleadable in bar" of the payer's action. A judgment
satisfied by the payment is still assignable. A charge the creditor holds for a
different debt is not. Asserted.

### 3. s 1 removes one objection only

A written guarantee signed by the promisor (or someone "lawfully authorised") is not
invalid "by reason only that the consideration ... does not appear in writing". The
section does not cure a promise with no consideration at all, an unsigned one, an oral
one, or a promise to pay one's own debt, which is not a promise "to answer for the
debt, default, or miscarriage of another person". Asserted.

### 4. s 2 helps co-borrowers as well as guarantors

It applies to a person "being surety for the debt or duty of another, or being liable
with another for any debt or duty". A joint borrower who repays the whole loan takes
the creditor's place against the co-borrower, up to the co-borrower's just
proportion. Someone who pays another's debt without being liable for it is outside the
section. Asserted.

### 5. Using the creditor's name needs need and an indemnity

The payer may sue in the creditor's name only "if need be, and upon a proper
indemnity". Both conditions are required. Asserted.

## What would need doing before this is worth anything

- Partial payment is not addressed: the text speaks of a person who "shall pay such
  debt or perform such duty". Whether a part-payer gets anything is not encoded.
- Capping a claim against a co-obligor at the payer's own advances and loss is a
  reading of the words "in order to obtain ... indemnification for the advances made
  and loss sustained", not something the proviso states.
- Reading "co-surety, co-contractor, co-debtor" as relative to the payer is an
  inference; the Act does not define them.
- How the just proportion is worked out, and the formality rules for guarantees under
  other Singapore law, were not read. No case law was searched.
