# Singapore Armed Forces Act 1972 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 9
of 2026 (in force 1 May 2026) shown. The arrangement of sections at the top of the
`.txt` deposit is one number out of step with the body; the body's numbers are used.
The First Schedule table is column-shifted in the deposit; its section numbers were
matched to items by order of appearance.

**Checks:** one case file, 99 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**18 of the 527 Singapore Acts** deposited here cite it. It is a 200-section code of
military discipline, so this row takes what a serviceman, a national serviceman or a
defence lawyer meets first: who is subject to military law (s 3); absence without
leave, desertion and failing to report them (ss 22-24) and the maxima for a handful of
common offences; which offences a disciplinary officer may try summarily (ss 4, 61,
First Schedule); the right to elect a court martial (s 77); time limits (ss 78, 111);
composition (s 79A); trial twice (s 108); homicide (s 112(2)); and assignment of
military pay and pensions (s 196). Organisation, the punishment powers of each grade
of disciplinary officer, court-martial procedure, appeals, arrest, bail, boards of
inquiry, pay deductions and the emergency and aid-to-civil-authority powers are not
encoded. No regulation was read.

## What the Act turns out to say

### 1. Absence without leave never goes stale; desertion can

s 111(1) bars any trial not started within 3 years after the latest of several dates,
but s 111(2) disapplies the whole section for "misconduct in action, assisting the
enemy, mutiny, absence without leave or desertion". s 111(4) then puts desertion back
under a bar: a serviceman with "not less than 3 years" of continuous exemplary service
must not be tried for desertion (other than on active service) committed more than 3
years before the trial. No such relief is written for absence without leave, the
lesser offence. So a 10-year-old AWOL charge may go to a court martial, while an
exemplary serviceman's 4-year-old desertion may not. Asserted.

### 2. A disciplinary officer cannot touch desertion or drugs

s 4 and s 61(1): a charge for an offence "not specified in the First Schedule must not
be dealt with summarily". The Schedule lists absence without leave, failure to report
deserters and absentees, disobedience of general orders, conduct to the prejudice of
good order, malingering and intoxication, but not desertion (s 23), drugs (s 34),
mutiny or misconduct in action. Those go to a subordinate military court. Asserted.

### 3. Summary trial has a short clock: 6 months, or 3 years for NSmen and leavers

s 78(1): no trial by a disciplinary officer after 6 months from the offence, unless
the person was released or discharged within 6 months after it, or was an
operationally ready national serviceman at the time; then 3 years. The Armed Forces
Council (or someone it authorises) may by written order direct a trial out of time
(s 78(2)), but never past a s 111 limit (s 78(3)). Asserted.

### 4. Who is subject to military law turns on orders, not on turning up

s 3(b) and (f): an operationally ready national serviceman, and a volunteer, is
subject from the time of being ordered to report "whether they have complied with such
order or not". Civilians in or accompanying the SAF are subject only "when engaged on
active service". Regulars and full-time NSmen are subject from the time their
liability to report arises until lawfully discharged or released. Asserted.

### 5. Mutiny in the face of the enemy, or with violence, carries a mandatory death sentence

s 15(1): "if the offence is committed in the face of the enemy or involves the use of
violence he or she shall be punished with death". Otherwise mutiny is 10 years. s 11
misconduct in action is "death or any less punishment". Asserted (mutiny only).

### 6. A disciplinary officer's verdict does not bar a civil court; a court martial's does

s 108(1): after a subordinate military court, no second trial by any court or officer
"for any offence based on the same facts". s 108(2): after a disciplinary officer, no
second military trial, "but the person may be tried ... by a civil court", which must
have regard to military punishment already undergone. s 108(3): a civil court's
verdict bars both military forums. Asserted.

### 7. Smaller points

- s 22(2) gives AWOL a defence of "circumstances over which he or she had no control",
  on the accused to prove; s 23 (desertion) has none written. Asserted.
- s 24 is broken by failing **either** to report without delay **or** to take steps to
  apprehend: doing one is not enough. Asserted.
- s 77: before convicting summarily, a disciplinary officer satisfied of guilt must
  offer a court martial, unless only a reprimand or minor punishment is proper. Asserted.
- s 79A: composition is capped at the lower of half the relevant maximum fine and
  $5,000, and not by someone in the accused's chain of command. Asserted.
- s 112(2): a court martial may try murder or culpable homicide only if the victim was
  subject to military law or the offence was on active service. Asserted.
- s 196: an assignment of military pay or pension is void unless made under
  regulations for the family's benefit or authorised by written law. Asserted.

## What would need doing before this is worth anything

- The disciplinary officers' punishment powers (ss 68-70B) and the scale of
  punishments (s 118) are where most outcomes are decided; none is encoded.
- s 111(1)(b)-(f) are collapsed into one input ("months since the latest date"); the
  related-civil-offence machinery is not modelled.
- "Exactly 36 months" is treated as within 3 years; that is an inference about the
  measure of time, not something the text states.
- The First Schedule was read from a column-shifted table and should be checked
  against the PDF.
- The s 3(b) triggers for national servicemen (in uniform, mobilised, called out in
  aid of the civil power) are collapsed into one flag.
- No regulations, General Orders or military court decisions were read.
