# Education Endowment and Savings Schemes Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from 1 January 2022).

**Checks:** one case file, 27 assertions satisfied, 0 errors, 0 warnings. The first cases are
requirement REQ-0014's own.

## Why this Act, and why scoped

Requirement **REQ-0014** in `subjects/sg/requirements.jsonl`, raised by the
`cradle-to-grave-simone` scenario (event e030), asked two things. Can a 19-year-old's
Post-Secondary Education Account pay her university fees? And who authorises the
withdrawal? The child-support row credits money into this account at 17 without defining
it. This row takes the PSE Scheme only (Parts 3A and 3B). Edusave is not encoded.

## What the Act turns out to say

### 1. Yes, for approved fees, but under 21 it is the parent who withdraws

Under s 22(2), "a parent of a member ... below 21 years of age, or a member ... who has
attained 21 years of age" is entitled to withdraw. The withdrawal must be:
- for the fees and charges of an approved course at an approved institution, attended by the
  member *or a sibling*; or
- for another prescribed purpose.

Under s 22(5), "approved" means approved by the Minister. Under ss 22(1) and 25(1), the
withdrawal is made "with the authority of the PSE Scheme Administrator".

REQ-0014's expected answer says the account holder authorises, or a parent while she is under
21. **The text differs in two ways:**
- At 19, the person *entitled* to withdraw is her parent, not she herself.
- The person who *authorises* is the PSE Scheme Administrator.

Both points are asserted. The money may also pay for a sibling's course, which the
expectation did not mention.

### 2. Other ways out of the account

- **s 22(3):** the whole sum may be withdrawn if the Minister thinks it just and equitable. The
  application is by the member, or by a parent if the member is under 21. The account then
  closes.
- **s 23:** a donation to a prescribed education charity, made by the same people.
- **s 24(1):** from 21, the member may move the whole sum to their CPF ordinary account.
- **s 24(4):** after the prescribed "relevant age", if nobody acts within the period the
  Administrator specifies (at most 12 months), the Administrator *must* make the transfer.
  Under s 24(4A) the sum then counts as a CPF cash grant.

### 3. Creditors cannot reach it

Under s 26(1), PSE moneys "belong to the member" and cannot be assigned or attached for debts.

## Smaller things worth recording

- Membership (s 20) requires citizenship plus "any other prescribed requirements"; the
  latter is an input.
- Ages are completed years. The Act says "attained 21 years of age" but has no rule of its own
  on when an age is attained; see REQ-0263.

## What would need doing before this is worth anything

- The regulations under s 35 were not retrieved. They hold the prescribed purposes,
  the membership requirements, the relevant age for s 24, and the contribution caps.
- Which courses and institutions the Minister has approved is an input.
- No case law was searched.
