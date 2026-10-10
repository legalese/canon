# Probate and Administration Act 1934 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the earlier naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The cover says it
incorporates amendments up to and including 1 December 2021; the body also shows
amendments by Act 18 of 2023 (in force 15 October 2024) to ss 4(2), 4(3), 22 and 39.

**Checks:** one case file, 51 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**7 of the 527 Singapore Acts** deposited here cite it. This row takes the rules with
decision content that a family member, creditor or practitioner meets in taking out
or resisting a grant: renunciation by citation (ss 4, 5), the number of personal
representatives (s 6), priority for letters with the will annexed (s 13(2)), infants
and persons lacking capacity (ss 21, 22), the oath (s 28), administration security
(s 29), caveats (s 33), the receiver offence (s 42), grants to the Public Trustee on
delay (s 55), the small-estate thresholds (ss 56(2), 62, 63, 64), the commission cap
(s 66) and the order in which a solvent estate's assets answer debts (s 57(4), Second
Schedule). The kinds of limited grant, revocation, vesting pending a grant, re-sealing
of foreign grants, consular administration, charges on property (s 58) and the
insolvency rules (First Schedule) are not encoded.

## What the Act turns out to say

### 1. A sole executor can take probate even where there is a minor or life interest

s 6(2) requires a trust corporation or at least 2 individuals where there is a
minority or a life interest, but it speaks only of **letters of administration**. A
grant of probate to one executor is not caught; s 6(1)'s cap of 4 grantees applies to
both. Asserted.

### 2. Security is for administrators, and the Public Trustee alone is excused

s 29(7) requires security "in the case of administrations whether with or without the
will annexed". No subsection requires it on probate (that probate needs none is an
inference from that silence). s 29(4) excuses the Public Trustee, but a trust company
is not excused from security, though s 28(2) excuses both from the oath. A Family
Court grantee gives security only if the grant is for an infant's benefit or the court
thinks fit (s 29(8)). Asserted.

### 3. The bond is sworn at the gross estate, less only mortgage debts

s 29(2): the bond is "in the amount at which the estate within the jurisdiction is
sworn, without deduction of any debts due by the deceased, other than debts secured by
mortgage", ordinarily with 2 sureties, which may ordinarily be dispensed with where the
administrator takes the whole estate after debts (s 29(5)). Asserted.

### 4. Silence after a citation is a renunciation

s 4(2): a person cited who fails to file a notice within the time permitted "shall be
deemed to have renounced". Filing a notice to contest and then not applying lets the
citor obtain an order with the same effect unless a grant follows in time (s 4(3)).
Renunciation bars a later application unless the court allows withdrawal for the
benefit of the estate (s 5). Asserted.

### 5. Three small-estate thresholds, and a heading that disagrees with its section

The Public Trustee may administer without any grant where property in Singapore is
not more than $50,000 gross, leaving out trust property and, for deaths on or after
17 September 2005, Dependants' Protection Insurance moneys (s 62). He may pay a
minor's maintenance from capital up to the whole of a holding of $25,000 or less, and
up to $25,000 of a holding between $25,000 and $50,000 (s 63). He need not advertise
before distributing where the estate "does not exceed $10,000" (s 64) — but the
section heading says "less than $10,000". At exactly $10,000 the operative words and
the heading disagree; the encoding follows the operative words. Funds in court of an
intestate with assets of $500 or less may go to a spouse, child, parent or sibling on a
declaration (s 56(2)); a grandchild is not in the list. Asserted.

### 6. Six months, then anyone fit — but the Public Trustee need not wait

s 55(1) lets letters go to the Public Trustee or another fit person after 6 months
with no application proceeded with, or where an administrator neglects security for a
month after the grant; s 55(2) says nothing prevents the Public Trustee applying
before 6 months. Asserted.

### 7. Priority, offences and caps

Letters with the will annexed go first to a residuary legatee, then the personal
representative of a deceased residuary legatee, then will beneficiaries who would take
on intestacy, then a legatee, then a creditor (s 13(2)). Removing, concealing or
withholding property from a s 39 receiver without lawful authority is an offence with a
maximum fine of $1,000 or 6 months (s 42). Commission is capped at 5% of assets
collected (s 66). No grant may be made over a caveat until the caveator has had the
opportunity to contest (s 33). A solvent estate's undisposed-of property answers debts
before the residuary gift, and specific gifts only after the pecuniary-legacy fund
(Second Schedule, which the will may vary). Asserted.

## What would need doing before this is worth anything

- The Family Justice Courts rules on probate (citations, caveats, security, the
  prescribed forms) were not retrieved; much of the procedure lives there.
- s 55(1)(d) and (e), the limited grants, and the First Schedule insolvency rules
  (which incorporate bankruptcy law) are not encoded.
- s 63 above $50,000 is encoded as giving no power (returns 0); that is an inference
  from the section's terms.
- The intestacy rules themselves (who is entitled to the estate) are in other law and
  are not here.
- No case law was searched.
