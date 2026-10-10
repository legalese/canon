# Contributory Negligence and Personal Injuries Act 1953 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows. No pipeline, no coverage table, no independent test pass, no
human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CNPIA1953.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021". No later amendment is annotated in
the text; the last amending Act in the deposited legislative history is Act 45 of 1998
(Civil Law (Amendment) Act 1998, commencement 1 January 1999), followed by the 2002
Revised Edition.

**Checks:** one case file, 47 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore (Tier 1),
not by citation count. It decides what becomes of a damages claim when the injured
person was partly to blame: the pedestrian who stepped out without looking, the
worker who ignored a safety rule. The Act has five sections and every operative
one is encoded: the definitions (s 2), apportionment and its five qualifications
(s 3), the Maritime Conventions Act exclusion (s 4) and common employment (s 5).

Not encoded: how a court fixes the share of responsibility (the Act says only "just
and equitable"); the provisions this Act points to but which were not read (Civil Law
Act 1909 ss 10, 20, 21; Maritime Conventions Act 1911 s 1; Limitation Act 1959);
contribution between wrongdoers; case law.

## What the Act turns out to say

### 1. A liability cap is applied after the reduction, so partial fault can cost nothing

s 3(3): where a contract or written law limits liability, "the amount of damages
recoverable by the claimant under subsection (1) shall not exceed the maximum limit".
The amount recoverable under s 3(1) is the already-reduced figure. On that reading,
full damages of $200,000 reduced by 25% give $150,000, and a $100,000 cap then gives
$100,000: the same as a blameless claimant would get. The reduction only shows when
the reduced figure is under the cap. This order of operations is a reading of the
words, not stated in terms. Asserted.

### 2. Being partly to blame no longer defeats the claim, but nothing says how much it may be cut

s 3(1): the claim "shall not be defeated by reason of the fault of the person
suffering the damage", but damages are reduced "to such extent as the court thinks
just and equitable having regard to the claimant's share in the responsibility". The
Act sets no scale. The encoding treats a 100% reduction as outside s 3(1), since it
would defeat the claim by another name; that is an inference, not text. Asserted.

### 3. "Fault" covers carelessness that wrongs nobody but oneself

s 2: "fault" includes any act or omission that "would, apart from this Act, give rise
to the defence of contributory negligence". So the claimant's lapse in looking after
their own safety is "fault" although it is not a tort against anyone. A breach of
contract that is not also a tort is in neither limb of the definition (inference from
its silence on contract). Asserted.

### 4. Contractual defences, time bars and maritime claims sit outside the rescue

s 3(2): s 3(1) "shall not operate to defeat any defence arising under a contract".
s 3(6): a party at fault who escapes the other's claim by pleading the Limitation Act
1959 or another time limit cannot recover damages or contribution from that other
under s 3. s 4: claims under s 1 of the Maritime Conventions Act 1911 are outside the
Act altogether. Asserted.

### 5. The court must record what the claimant would have got if blameless

s 3(4): whenever damages are reduced, "the court shall find and record the total
damages which would have been recoverable if the claimant had not been at fault".
Asserted as a duty that arises whenever s 3 applies.

### 6. A death partly caused by the deceased cuts the family's claim too

s 3(5): if the estate's action would be reduced, actions for the dependants under
s 20 of the Civil Law Act 1909, or for any person under s 21, "shall be reduced to a
proportionate extent". The encoding reads "proportionate" as the same percentage
(inference). Asserted.

### 7. An employer cannot hide behind a fellow employee, by defence or by contract

s 5(1): it is no defence that the negligent employee was "in common employment" with
the injured one. s 5(2): a term of a contract of service or apprenticeship, or a
collateral agreement, is void so far as it excludes or limits the employer's
liability for personal injury caused by a fellow employee's negligence. s 5(3):
"personal injury" includes disease and any impairment of physical or mental
condition. A term limiting liability for property damage is outside s 5(2), and the
encoding treats an independent contractor's contract for services as outside it too
(inference; neither term is defined). Asserted.

## What would need doing before this is worth anything

- Civil Law Act 1909 ss 10, 20 and 21, the Maritime Conventions Act 1911 s 1 and the
  Limitation Act 1959 were not read, so s 3(5), s 4 and s 3(6) are encoded only as
  far as their own words go.
- The order of reduction and cap (finding 1), the bar on a 100% reduction (finding 2)
  and "proportionate extent" (finding 6) are readings that case law may settle
  differently; none was searched.
- No guidance on how courts actually fix the claimant's share was retrieved.
