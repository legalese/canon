# Accounting Standards Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 17
of 2026 (in force 1 July 2026) shown.

**Checks:** one case file, 61 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. It is an institutional Act:
it has no offences and no penalties, and the accounting standards themselves are not
in it. This row takes the provisions with decision content: who the Accounting
Standards Committee's standards may reach (s 8(1)), when a standard has force (ss 9(3),
10(2)), the Committee's size, appointment, resignation, quorum, presiding member and
delegation (ss 4, 5, 7), the definition of "statutory body" (s 2), and which statutory
bodies must follow the Accountant-General's standards (ss 11(4), 12 and the Schedule).
Not encoded: the objects in s 9(1)-(2) beyond their effect on validity, the evidence
rules in s 10(3), the Accountant-General's choice of text (s 11(2)-(3)), terms of
office and revocation of appointments, the transitional carry-over of Accounting
Standards Council standards (s 8(4)-(5)), and ss 13-14.

## What the Act turns out to say

### 1. A standard made carelessly is valid, but a standard not announced has no force

s 9(3): "A failure to comply with this Part in relation to the making or formulation
of an accounting standard does not affect the validity of the standard". So a standard
made without regard to the s 9 objects still stands. But s 10(2): no standard,
amendment or revocation "has any force or effect" until the s 10(1) notice is
published. A revocation likewise takes effect only on notice. s 10 is itself in Part 3,
so the two provisions overlap where the notice is defective; this encoding follows
s 10(2) and does not resolve the overlap. Asserted.

### 2. Statutory bodies are bound only if listed, and only by standards notified to them

s 12 binds "every statutory body specified in the Schedule", and only to standards
"established under this Part and notified in writing to the statutory body by the
Accountant-General". Meeting the s 2 definition of "statutory body" (public Act,
public function, accounts presented to Parliament) is not enough on its own. The
Monetary Authority of Singapore is not in the deposited Schedule. A standard applies to
"any periods specified in the standard" (s 11(4)). Asserted.

### 3. The Committee's standards reach four kinds of entity, listed by name

s 8(1): companies, registered co-operative societies, registered societies, and
registered charities and institutions of a public character. Nothing else is named.
That an LLP or a sole proprietorship falls outside is a reading of the list, not a
statement in the text. Asserted.

### 4. A Committee of 11 to 16, quorum one half

s 4(2): a Chairperson and "at least 10 but not more than 15 other members". s 5(2):
"one half of the number of its members constitutes a quorum"; with an odd number this
encoding requires the next whole member above half (6 of 11), an inference. If the
Chairperson is absent the temporary Chairperson presides, and otherwise a member
elected by those present (s 5(3)). Asserted.

### 5. Everything can be delegated except delegation

s 7(4): the Committee may delegate to a member or a sub-committee "any of the functions
or powers of the Committee under this Act, except the power of delegation conferred by
this section", and keeps the power itself (s 7(6)). A sub-committee may include
outsiders, but its chairperson must be a Committee member (s 7(2), (3)). Asserted.

### 6. Resignation needs a month's written notice

s 4(8): "at least one month's notice in writing to the Authority". Asserted.

## What would need doing before this is worth anything

- The deposit shows "[Deleted by Act 36 of 2022 wef 01/04/2023]" notes after para (b)
  of "accounting standard" and after the definition of "company"; what was deleted is
  not shown, and the definition of "company" (including foreign companies for their
  Singapore operations) was not encoded.
- Schedule items 5 and 63 are deleted; their former occupants are not named in the
  deposit. Only a sample of eight bodies is encoded, two of them as not listed.
- No accounting standard, Accountant-General notification, or rules under s 14 were
  retrieved.
