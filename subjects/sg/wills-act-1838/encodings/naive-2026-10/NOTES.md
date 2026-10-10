# Wills Act 1838 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/WA1838.txt`. The deposit's footer reads "version in
force from 28/10/2022"; the latest amendment annotated in the body is Act 24 of 2022
(s 27(5)). Section numbers follow the body. The arrangement of sections at the top of
the deposit is one place out of step.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: nearly every adult who makes a will in
Singapore, and every family that finds one, meets these rules. An automated count found
none of the 527 deposited Singapore Acts citing it by its slug title. That count misses
Acts cited by short or older titles, so it says nothing about importance.

This row covers who may make a will (ss 4, 27), how it must be signed and witnessed
(ss 5, 6), gifts to witnesses (ss 9, 10), revocation by marriage and otherwise
(ss 13–15), alterations (s 16), revival (s 17), gifts to children who die before the
testator (s 26), and rectification (s 28). Not encoded: the definitions (s 2), what
property may be disposed of (s 3), powers of appointment (ss 5(3)(d), 5(4), 7, 21),
the choice-of-law details in s 5(3)–(8), creditor and executor witnesses (ss 11, 12),
and the construction rules in ss 18–25.

## What the Act turns out to say

### 1. Getting married cancels your will, unless the will names that marriage

s 13(1): "Every will made by a man or woman shall be revoked by his or her marriage".
The only general escape is s 13(2): a will made on or after 29 August 1938 and
"expressed to be made in contemplation of a marriage" survives "the marriage
contemplated". A will made in contemplation of one marriage is still revoked by a
different one. The rule covers "the first, second or subsequent marriage of a person
lawfully practising polygamy". Asserted.

### 2. Divorce does nothing to a will

s 14: no will is revoked "by any presumption of an intention on the ground of an
alteration in circumstances", and s 15 lists the only ways to revoke one. Divorce is
not among them. Treating divorce as "an alteration in circumstances" is an
**inference**: the Act never mentions divorce. On that reading (again an inference),
a former spouse named in a will still takes. Asserted.

### 3. A witness who is a beneficiary loses the gift, but the will stands

s 10(1): a gift to an attesting witness "or to whose wife or husband" is "utterly
null and void" as far as that person is concerned. s 9 keeps the will itself valid.
s 10(3) saves the gift if the will "is duly executed without his attestation", so two
other, disinterested witnesses rescue it, for testators dying after 29 May 1992
(s 10(4)). A direction to pay a debt is not caught. Asserted.

### 4. Under 21 cannot make a will, unless on active service

s 4: "No will made by any person under 21 years of age shall be valid." s 27 lets a
soldier "in actual military service" or a mariner "at sea" make one "even though under
21". Since Act 24 of 2022, "soldier" includes air force members and Digital and
Intelligence Service servicemen (s 27(5)). That such a testator also escapes the
formalities of s 6 is an **inference**: s 27 refers to the law "before the making of
this Act", which the deposit does not set out. Asserted.

### 5. Two witnesses together, but they need not watch each other sign

s 6(2): the signature must be made or acknowledged "in the presence of 2 or more
witnesses present at the same time", and the witnesses must subscribe "in the presence
of the testator". The text does not require them to sign in each other's presence, and
"no form of attestation shall be necessary". Someone else may sign for the testator, in
his presence and at his direction. Asserted.

### 6. Revocation needs intent, and revival needs formality

Tearing or burning revokes only "with the intention of revoking it", and only if done
by the testator or by someone "in his presence and by his direction" (s 15(d)). An
unwitnessed letter does not revoke. A revoked will comes back only by re-execution or a
duly executed codicil showing intent to revive (s 17(1)); revoking the later will does
not revive the earlier one. Asserted.

### 7. A gift to a child who dies first passes to the child's estate, not straight to the grandchildren

s 26: the gift does not lapse if the child leaves issue living at the testator's death,
but it takes effect "as if the death of that person had happened immediately after the
death of the testator". So it goes into the dead child's estate. The grandchildren are a
condition of the rule, not its beneficiaries. A contrary intention in the will, or an
interest that ends at the child's death, excludes the rule. Asserted.

### 8. Six months to fix a clerical error

s 28: a court may rectify a will that fails to carry out the testator's intentions
because of "a clerical error" or "a failure to understand the testator's instructions".
The application must be made within 6 months of the first grant unless the court gives
permission. Grants limited to settled land or trust property, grants that do not permit
distribution, and part-estate grants without a grant for the remainder do not start
the clock (s 28(4)). Personal representatives who distribute after the 6 months are
protected, though the property can still be recovered (s 28(3)). Asserted.

## What would need doing before this is worth anything

- No case law was retrieved: "actual military service", "in contemplation of a
  marriage", "apparent" in s 16, and the effect of s 27 all depend on it.
- The Intestate Succession Act 1967 and the Probate and Administration Act 1934, which
  s 13 and s 28 refer to, were not read.
- Whether other Acts (for example the Administration of Muslim Law Act 1966) change
  these rules for some testators was not examined; this deposit does not say.
- Months in s 28 are counted by the caller; no calendar arithmetic is done.
- A testator who died on 26 June 1992 itself falls between the words of s 5(9); this
  encoding applies s 5 to him, which is an inference.
