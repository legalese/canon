# Motor Vehicles (Third-Party Risks and Compensation) Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Observations below, not checked findings.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 January 2026 — so it carries the Platform Workers Act amendment (Act 30 of
2024, in force 1 January 2025) and the disqualification amendment (Act 2 of
2025, in force 1 January 2026).

**Checks:** `l4 run mv-cases.l4` — 34 assertions satisfied, 0 errors,
0 warnings.

## What is encoded

ss 2, 3, 4 and 9. That is the spine: it is unlawful to use a vehicle without
complying cover (s 3), s 4 says what "complying" means, and s 9 is what makes
the cover worth anything to the person actually injured — the insurer must pay
the third party's judgment *even though it could have avoided the policy against
its own insured*.

Not encoded: the settlement-agreement machinery in ss 5–8, and ss 10–24.

## Three things worth a second look

**1. The section headed "Duty of insurers to satisfy judgments" confers a
discretion for small judgments.** s 9(1) splits at the relevant amount:

- **(a)** where the sum "does not exceed the relevant amount", the insurer
  **may** pay it;
- **(b)** where it "exceeds the relevant amount", the insurer **must** pay.

So for a judgment at or below the relevant amount the Act creates no obligation
on the insurer at all. The third party has a judgment against the insured and,
on the face of s 9(1)(a), no statutory claim on the insurer. Everything the
section exists to do — surviving the insurer's right to avoid, reaching the
insurer directly — is in limb (b).

The relevant amount is **$5,000** unless the Minister prescribes another
(s 2, s 20). Whatever that figure was worth when the Act was passed in 1960, a
$5,000 ceiling in 2026 means limb (a) covers almost nothing: nearly every real
personal-injury judgment falls in (b). The practical effect may therefore be
nil. But the drafting still says "may" where the marginal note says "Duty", and
a reader relying on the note would get it wrong.

Asserted as the pair at exactly $5,000 and at $5,001 in `mv-cases.l4`
§ `9 — the relevant amount, and the four bars`. Note also that "does not exceed"
puts the relevant amount *itself* on the permissive side.

**2. s 9(6)(c) needs two things, and reads as though it needs one.** The bar
applies where the policy was cancelled before the event **and** one of three
things happened to the certificate — surrender or statutory declaration before
the event, the same within 14 days of cancellation taking effect, or the insurer
commencing proceedings for failure to surrender within that period. Cancellation
alone does not bar payment. The structure is easy to misread because the three
certificate limbs are long and the conjunction sits far above them. The pair on
`a judgment where the policy was cancelled but the certificate kept` is what
holds the two halves apart.

**3. The s 4(4) exclusions are each two-part.** An employee of the insured is
not outside the required cover merely by being an employee: the death or injury
must also arise "out of and in the course of" the employment. Same shape for the
platform-worker limb added in 2025. An encoding that read only the status would
wrongly exclude an employee injured as an ordinary road user on their own time.
Asserted as `an employee injured at work` against `an employee injured off
duty`.

## What would need doing before this is worth anything

- The relevant amount is modelled as a supplied fact rather than the literal
  5000, because s 20 lets the Minister change it by order in the Gazette. **No
  check was made for such an order.** If one exists, the figure in the cases is
  stale — but no rule depends on it, which is the point of carrying it as a fact.
- "Specified person" is encoded only in its paragraph (b) form, which is the
  limb s 9 uses. Paragraph (a), for s 6 settlement agreements, is not encoded
  because ss 5–8 are not.
- The Schedule of specified territories was not read.
- No case law was searched, and no rules made under s 24 were retrieved.
