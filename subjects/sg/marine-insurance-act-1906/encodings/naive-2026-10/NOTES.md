# Marine Insurance Act 1906 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions
of the `writing-l4-rules` skill as the finished naive rows use them (the skill
itself was not loadable in this session). No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MIA1906.txt`. The deposit says it "incorporates
all amendments up to and including 1 December 2021 and comes into operation on
31 December 2021"; the retrieval record gives it as current at 1 October 2026.
No amending Act is annotated in the body. The Legislative History records the
English Act 6 Edw. VII, c. 41 (commenced 1 January 1907), declared by the
Application of English Law Act 1993 to apply in Singapore from 12 November 1993,
and revised as Chapter 387 in 1994. The arrangement of sections at the top of
the deposit is out of step with the body from s 22 on; the body's numbers are
used throughout.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0039**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business
it applies to; no scenario has asked a sharper question yet. That person is
whoever buys marine cover (shipowner, cargo owner, trader) and their insurer.

This row takes the points at which a marine claim is won or lost: gaming
policies and insurable interest (ss 4, 6), disclosure (ss 17, 18), warranties
and seaworthiness (ss 33, 34, 39), deviation and delay (ss 46, 48, 49), included
and excluded losses (s 55), total loss and abandonment (ss 57, 60 to 62), the
measure of indemnity (ss 67 to 69, 71, 81) and return of premium (s 84).

Not encoded: definitions (ss 1 to 3), the minor insurable interests (ss 7 to 15),
insurable value (s 16), misrepresentation (s 20), the form of the policy and the
Schedule's rules of construction, double insurance and contribution (ss 32, 80),
the special warranties (ss 35 to 38, 40, 41), commencement of risk and change of
voyage (ss 42 to 45, 47), assignment, brokers, general average and salvage,
freight and liability measures, subrogation and mutual insurance. Almost every
rule gives way to the policy's own terms (s 87); the encoding assumes a silent
policy.

## What the Act turns out to say

### 1. A breach of warranty discharges the insurer even if it did not matter and was put right

s 33(3): a warranty "must be exactly complied with, whether it be material to the
risk or not", and on breach the insurer is discharged from the date of breach.
s 34(2): the assured "cannot avail himself of the defence that the breach has been
remedied ... before loss". Only a change of circumstances, a later law making
compliance unlawful, or the insurer's waiver excuses it (s 34(1), (3)). A loss
that came before the breach is still covered. Asserted.

### 2. On a voyage policy an unseaworthy ship loses the cover; on a time policy only if the owner knew and it caused the loss

s 39(1) implies a warranty of seaworthiness at the start of a voyage policy, so
by finding 1 the insurer is discharged whatever caused the loss. s 39(5): a time
policy carries no such warranty; the insurer escapes only a loss "attributable to
unseaworthiness" where the ship was sent to sea unseaworthy "with the privity of
the assured". Asserted.

### 3. The assured must volunteer every material fact, but the exceptions fall away once the insurer asks

s 18(1) puts the duty on the assured, who is deemed to know what "ought to be
known by him", and gives the insurer the right to avoid. The exceptions in s 18(3)
(what lessens the risk, what the insurer knows or is presumed to know, what it
waives) apply only "in the absence of inquiry": a widely reported war need not be
mentioned, unless the insurer asks about it. Asserted.

### 4. A deviation discharges the insurer even if the ship returns to her route; saving life excuses it, chasing salvage does not

s 46(1): deviation without lawful excuse discharges the insurer "and it is
immaterial that the ship may have regained her route"; (3) an intention to deviate
alone does not. s 49(1)(e) excuses saving life or aiding a ship in distress
"where human life may be in danger"; aid to a ship with no lives at risk is not
listed (an inference from the list, not a stated exclusion). Barratry excuses only
"if barratry be one of the perils insured against". Asserted.

### 5. A constructive total loss is paid as total only if notice of abandonment is given

s 62(1): without notice "the loss can only be treated as a partial loss", unless
notice is unnecessary (no possible benefit to the insurer, (7)) or waived (8). An
actual total loss needs no notice (s 57(2)). For a damaged ship the test is repair
cost against repaired value, counting future salvage (s 60(2)(b)). Asserted.

### 6. Delay, wear and tear, inherent vice and vermin are excluded unless the policy says otherwise; crew negligence is not

s 55(2): the insurer is liable for a peril-caused loss even though it "would not
have happened but for the misconduct or negligence of the master or crew", is
never liable for the assured's wilful misconduct, and is not liable for delay
"although the delay be caused by a peril insured against". Asserted.

### 7. Under-insured, the assured carries the gap

s 81: an assured insured below the insurable value "is deemed to be his own
insurer in respect of the uninsured balance"; s 67(2) gives each insurer its
subscription's proportion. On a damaged-goods loss of 200,000 under an unvalued
800,000 policy for 600,000, the insurer pays 150,000. The s 68, 69 and 71(c)
measures are encoded alongside. Asserted.

### 8. Premium comes back when the risk never ran, but not after fraud or once an indivisible risk attached

s 84(3): returnable where the subject-matter was never imperilled, or there was no
insurable interest throughout; not where the policy was avoided for the
assured's fraud, nor where an unapportionable risk "has once attached". A "lost or
not lost" policy on goods already safely arrived returns nothing unless the
insurer knew. Asserted.

## What would need doing before this is worth anything

- No Singapore case law was searched; the 1906 text is read as printed, and how
  Singapore courts apply ss 18, 33 and 39 today was not checked.
- The encoding assumes a policy silent on every point; real policies
  may displace much of it, and none was read.
- The excluded sections above, especially s 20 (misrepresentation), double
  insurance and general average, are what a practitioner would ask about next.
