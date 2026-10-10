# Rapid Transit Systems Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2026 (in force 4 May 2026) shown. The deposit's arrangement of sections is out
of step with the body in Part 6; the body's numbering is followed (evidence of
identity is s 39, composition s 44).

**Checks:** one case file, 92 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**12 of the 527 Singapore Acts** deposited here cite it. Most of the Act is the
Land Transport Authority's machinery: land powers, licensing internals, special
administration. This row takes what a passenger, a cyclist, an operator or an
investor actually meets: operating without a licence (s 12), security screening
(s 23A), things left on railway premises (s 23B), endangering, damage and
compensation (ss 25 to 27), evidence of identity (s 39), the penalty table and
composition (s 44), and the controller thresholds for designated entities
(ss 21B, 21F, 21G, 21R). Not encoded: Part 2 (including the owner-initiated
acquisition in ss 7, 7A), ss 13 to 21, ss 21C to 21E and 21H to 21Q, inspectors'
powers beyond the s 23(3) penalty, Part 4A, appeals, arrest (s 40) and s 41.

## What the Act turns out to say

### 1. Selling down needs approval just as buying up does

s 21G(1)(b): a person must not, without the Authority's prior written approval,
"cease to be a 25% controller, 50% controller or 75% controller" of a designated
entity by a decrease. A fall from 30% to 10%, or from 55% to 30%, needs approval;
a move inside a band (30% to 45%, 80% to 100%) does not. Transactions entered
into before the effective designation date are excepted (s 21G(2)). Asserted.

### 2. The 5% notice catches only climbing into the 5% band

s 21F(1) applies when a person "becomes a 5% controller ... as a result of an
increase". Because the bands in s 21B do not overlap (5% to under 25%), someone
who jumps from 3% to 30% never becomes a 5% controller and owes no s 21F notice
(s 21G approval is needed instead), and someone who falls from 30% to 10% becomes
one by a decrease, which s 21F does not catch. The notice is due within 7 days;
the defences are unawareness plus notice within 14 days of becoming aware (s 21F(3)),
or an associate's unconcerted increase plus notice within 7 days of the
contravention (s 21F(4)). Every Part 3A offence carries $50,000 or 6 months, plus
$5,000 "for every day or part of a day" (s 21R). Asserted.

### 3. Who may frisk you on the MRT depends on who they are, not where they stand

s 23A(2): any police officer or "approved person" may ask a passenger or entrant
to walk through a detector, X-ray a bag, empty it, turn out pockets or remove a
coat or shoes. But a frisk search, or a hand-held scanner passed over the person,
may be asked for only by a police officer or a "senior approved person" (s 23A(3)):
uniformed auxiliary police, the operator's security officers and outsourced
enforcement officers, not the Authority's own officers or the operator's other
employees. Refusing a lawful request "without reasonable excuse" is an offence,
up to $1,000 (s 23A(6), (7)). Asserted.

### 4. An undeclared outsourced officer can still be obeyed at your peril

s 23A(8) makes refusal no offence where a plain-clothes police officer, or an
approved person, "fails to declare his or her office" — but for an outsourced
enforcement officer only if he or she ALSO "refuses to produce his or her
identification card on demand". A uniformed police officer need declare nothing.
Asserted.

### 5. Refusing the detector is an offence, but not a ground to be ordered out

s 23A(5) lets the officer order a person to leave immediately on refusing
screening or inspection of personal property or a bag, a hand-held scanner, or a
frisk. Walking through a screening detector and removing worn clothing are not in
that list, though refusing them is still an offence under s 23A(6) (and s 23A(1)
makes compliance a "condition of entry"). Treating "turn out pockets" as an
inspection of personal property is an inference. Asserted.

### 6. Damage: the fine is $200,000, and accidents still pay

s 26: wilfully removing, destroying or damaging the railway — up to $200,000 or 12
months, against $10,000 or 5 years for wilfully endangering safety (s 25). s 27:
compensation is payable for damage done "whether wilfully or otherwise", and the
criminal court may assess and order it. Asserted.

### 7. Composition is capped at the lower of half the fine and $5,000

s 44(1): for an offence "prescribed as a compoundable offence", the sum may not
exceed the lower of half the maximum fine and $5,000: $500 for refusing screening,
$250 for refusing identity, $5,000 for damage. Which offences are prescribed is
left to regulations (s 44(3)), not retrieved, so it is an input. Asserted.

### 8. Other points

s 23B: leaving a bicycle, PMD or any "article or thing" so as to obstruct the
public is an offence ($2,000) unless authorised by law or a "lawful and reasonable
use"; an approved person may move it at once if it is obstructing others, otherwise
only after telling the owner "(if known)" — that an unknown owner need not be told
is an inference. s 39: refusing or wilfully misstating identity to an officer who
reasonably believes an offence was committed — $500, with no reasonable-excuse
defence written in. s 12: only the Authority or a licensee may operate a rapid
transit system; $50,000 or 6 months, plus $5,000 a day after conviction.
Asserted.

## What would need doing before this is worth anything

- The regulations prescribing compoundable offences (s 44(3)) and the Part 3A
  regulations were not retrieved.
- Equity interest, associate and indirect controller (ss 21C, 21D) are not
  encoded; the controller rules take a single percentage, though s 21B treats
  equity and voting power as alternatives.
- Which entities are designated (s 21E gazette notifications) was not checked.
- The Act 5 of 2026 change (annotated at the end of s 23B) was not compared
  with the earlier text.
- No case law was searched.
