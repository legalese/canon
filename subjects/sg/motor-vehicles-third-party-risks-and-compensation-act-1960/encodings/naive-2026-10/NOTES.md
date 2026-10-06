# Motor Vehicles (Third-Party Risks and Compensation) Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Observations below, not checked findings.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 January 2026 — so it carries the Platform Workers Act amendment (Act 30 of
2024, in force 1 January 2025) and the disqualification amendment (Act 2 of
2025, in force 1 January 2026).

**Checks:** `l4 run mv-cases.l4` and `l4 run mv-third-parties-cases.l4` — 82
assertions satisfied, 0 errors, 0 warnings.

## What is encoded

**ss 2 to 16.** `mv-act.l4` is the spine: it is unlawful to use a vehicle
without complying cover (s 3), s 4 says what "complying" means, and s 9 is what
makes the cover worth anything to the person actually injured.
`mv-third-parties.l4` is everything that stops the cover failing them.

Not encoded: s 6's settlement-payment machinery beyond the routing rule, and
ss 17–24.

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


---

# Added with sections 5 to 16

## The architecture, once the whole Act is in view

Every section in this half removes one way the insurance could be defeated. Read
together they say something the individual sections do not: **the cover is for
the victim, not for the driver.**

- **s 5** — an agreement with the passenger cannot restrict the liability, and
  it is caught "**whether intended to be legally binding or not**". A mere
  understanding between driver and passenger is struck down on the same terms as
  a contract. s 5(2) then excludes *volenti* outright: willingly accepting the
  risk of the driver's negligence never negatives the liability.
- **s 7** — a condition in the policy is of no effect, but **only if it bites on
  something done or omitted *after* the accident**. A condition about
  pre-accident conduct stands however severe. The timing is the whole of it.
- **s 8** — restrictions on the policy's scope are of no effect, by reference to
  a **closed list of eight** grounds. A restriction on anything else survives.
- **ss 10–13** — the insured's bankruptcy or winding up transfers their rights
  against the insurer directly to the third party, so the proceeds never enter
  the estate and the other creditors never see them. s 12 then stops the insurer
  and the insured dealing them away.
- **s 14** — no settlement is valid unless the third party is a party to it, and
  it reaches a claim that "**might** be made", so the insurer cannot buy off the
  insured before the victim has sued.

And then the counterweight, in **s 7(2)** and **s 8(3)**: the insurer pays the
third party and **recovers from its own insured**. The driver does not escape;
the victim is simply not made to bear the driver's breach.

## Two observations

**1. s 11's second limb is doing load-bearing work.** The duty is to say whether
you were insured **"or would have been so insured if the insurer had not avoided
or cancelled the policy"**, and to give the certificate particulars either way.
Without it, the s 9 route — which survives avoidance — could never be found by
a claimant, because the only person who knows the policy existed is the one with
an interest in not mentioning it. Asserted on the driver whose policy has been
avoided.

**2. The driver's paperwork decides whether the victim is paid.** s 15(1)
requires the certificate to be surrendered within **7 days** of a cancellation
taking effect. s 9(6)(c), encoded in the other module, makes that surrender one
of the three things that **bars** the third party's recovery from the insurer.

So a third party's claim can fail because someone else returned a piece of paper
on time. The victim has no way of knowing, no way of influencing it, and no
remedy against the insurer if it happened. The penalty for *not* surrendering is
a fine not exceeding $500. Whether that is the intended trade is not something
the text settles, but the two provisions should be read together and are three
sections apart.

## What would still need doing

- s 6's settlement machinery, which has its own Public Trustee approval route and
  costs-determination preconditions.
- ss 17–24, including s 21's power to amend the sums.
- The Schedule of specified territories.
- No case law was searched, and no human gate has been sought.
