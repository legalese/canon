# Forks - exceptions group (Chapters 4 and 4A)

Each fork: the text, the readings, the one taken, and why.
Where I looked and found no fork, that is said at the end.

## E-1 - Which way a leaf faces (the charge generator's FALSE-fill)

**Text.** The Code states many conditions of an exception negatively or as denials: s 89's and s 92's provisos ("this exception shall not extend to (a) the intentional causing of death"), s 98(2) ("There is no right of private defence in cases in which there is reasonable opportunity to have recourse to the protection of a public authority"), s 104(2) ("continues till (a) the offender has effected his retreat"), s 106A ("There is no right of private defence against an act ... done ... by a public servant acting in good faith").

**Readings.**
(A) The leaf is the Code's words ("the intentional causing of death"), and the ladder puts NOT over it.
(B) The leaf is phrased so that TRUE favours the accused ("not the intentional causing of death, or the attempting to cause death"), and no exception ladder puts NOT over a leaf.

**Taken: B.** The charge generator completes a partial record with every unknown leaf FALSE (reference/charge-generator-README.md). Under (A), an unknown proviso would be filled FALSE, NOT would make it TRUE, and the exception would be shown as established on facts nobody supplied - the exact mirror of PLAN's FORK G-6. Under (B), an unknown leaf can only withhold an exception. That is also the law: Evidence Act 1893 s 107 (verified 2026-09-26 in the lawplain statutes corpus, EA1893 s 107) puts "the burden of proving the existence of circumstances bringing the case within any of the general exceptions in the Penal Code 1871" on the accused, "and the court is to presume the absence of such circumstances". So FALSE-fill IS s 107's presumption, provided every leaf faces the accused's way.

**Cost.** Some leaves are the Code's words with "not" prefixed, rather than the Code's words; each such leaf's `@desc` says NOT in capitals and says which way to answer. Where the Code's own words already face that way ("which is not intended to cause death", "did not of his own accord ... place himself"), they are used as they stand.

**Checked two ways.** A grep for `NOT` in the three modules finds it only in s 90 (a definition, see E-5) and s 86 (an unexported outcome). And the last section of the tests asserts, for every exported ladder, that the all-FALSE record gives FALSE (35 assertions).

**The PLAN citation.** notes/PLAN.md §5 cites Evidence Act s 107 and asks this encoder to verify it or drop it. Verified: the section exists, is headed "Burden of proving that case of accused comes within exceptions", and reads as quoted above.

## E-2 - s 78: does the good-faith proviso apply when the court DID have jurisdiction?

**Text.** "... is an offence, notwithstanding the court may have had no jurisdiction to pass the judgment or order, provided the person doing the act in good faith believes that the court had such jurisdiction."

**Readings.** (A) The proviso governs the whole section: the belief is always required. (B) The proviso qualifies only the "notwithstanding" clause: the belief is needed only where the court lacked jurisdiction.

**Taken: A**, the literal grammar: the proviso follows the main verb and is not set off to the "notwithstanding" clause. In practice the readings diverge only for a person who acted on an order of a court with jurisdiction while not believing it had jurisdiction, and s 76 (justified by law) would usually cover that person anyway.

## E-3 - s 81 Explanation: a condition, or a gloss?

**Text.** "Explanation.-It is a question of fact in such a case whether the harm to be prevented or avoided was of such a nature and so imminent as to justify or excuse the risk ..."

**Readings.** (A) A gloss on "in good faith for the purpose of preventing ... other harm". (B) A further condition of the exception.

**Taken: B.** All three Illustrations make it a condition in terms: "if it be found as a matter of fact that the danger which he intended to avoid was such as to excuse him" ((a)), "if it be found that the harm to be prevented was of such a nature and so imminent as to excuse A's act" ((b)), and the same in (c). Tested both ways on illus (a).

## E-4 - s 85(2): does "and the state of intoxication was caused without the knowledge or against the will" govern (a) as well as (b)?

**Text.** "(a) did not know what he was doing; or (b) did not know that such act or omission was wrong, and the state of intoxication was caused without the knowledge or against the will ..."

**Readings.** (A) It governs both limbs. (B) It governs (b) only.

**Taken: A.** In the source it is a full-width clause set out after both lettered limbs (and after the amendment note to (b)), not part of (b)'s indented text. Reading (B) would make self-induced intoxication a defence whenever the accused did not know what he was doing, which s 85(1) ("intoxication shall not constitute a defence ... Except as provided") and s 86(2) (intoxication otherwise goes only to the fault element) are drafted to prevent.

## E-5 - s 90: an exception, or a definition?

**Text.** "A consent is not such a consent as is intended by any section of this Code - (a) ...".

**Readings.** notes/PLAN.md §5 names every ladder in this group `exception under s N`, and says s 90 is "worded otherwise, so the name does not quote them" - implying `exception under s 90`. But s 90 does not except anything; it defines when a consent does not count, and it is read by offences ("without her consent") as much as by ss 87-89.

**Taken:** `consent within section 90`, following PLAN §2's own rule for "a definition section in your own chapters that other sections read". It is the one ladder in the group that puts NOT over leaves, which is right for a definition read by an offence: an unknown vitiating circumstance, filled FALSE, leaves the consent standing, so "without consent" is not made out and no charge is framed on facts nobody supplied. ss 87-89 carry consent as a flat leaf (PLAN §3.3), with s 90's vitiators in its `@desc`, and s 90's ladder is its drill-down.

**Reported to the ontology agent** as a naming disagreement between PLAN §5 and PLAN §2.

## E-6 - s 92: does "and has no guardian" govern both limbs?

**Text.** "... if the circumstances are such that it is impossible for that person to signify consent, or if that person is incapable of giving consent, and has no guardian or other person in lawful charge of him from whom it is possible to obtain consent in time ...".

**Readings.** (A) It governs only the second limb ("that person is incapable of giving consent, and has no guardian"). (B) It governs both.

**Taken: A.** The clause's implied subject is "that person" of the incapable limb, and illus (a) (the insensible rider, the impossible-to-signify limb) says nothing about a guardian, while illus (c) (the incapable child; "There is no time to apply to the child's guardian") is where the Code mentions one. First written as (B) and changed before the tests were final; no expected value depended on the change.

## E-7 - s 104: continuance where the act is more than one offence

**Text.** s 104(2)-(5) state a separate continuance for theft, robbery, criminal trespass or mischief, and house-breaking.

**Readings.** A robbery is also a theft (s 390(1)); house-breaking is also criminal trespass. (A) The right continues if it continues against ANY offence the act falls under. (B) Only the most specific offence's rule applies.

**Taken: A**, as the ladder's OR of four limbs, each pairing the offence with its own continuance. The Code gives no ordering among the subsections. Not tested at the boundary (no Illustration); listed for the reviewer.

## E-8 - s 106A Explanation 2's last clause

**Text.** "... unless A knows, or has reason to believe, that the person doing the act (B) is acting by such direction; or unless B states the authority under which B acts, or, if B has authority in writing, unless B produces such authority, if demanded."

**Readings.** (A) Where B has written authority and it is demanded, stating it is not enough: B must produce it. (B) Stating the authority always suffices; producing written authority is a further, alternative way.

**Taken: A**, which gives the "if B has authority in writing" clause work to do. Encoded as: A keeps the right if he did not know or have reason to believe, AND (B did not state his authority, OR B had written authority, it was demanded, and B did not produce it). Tested both ways.

## E-9 - s 87 "above 18 years of age", in completed years

**Text.** "to any person above 18 years of age".

**Readings.** On an age in completed years, a person of 18 completed years is older than 18 years except on the 18th birthday itself. (A) `years AT LEAST 18`. (B) `years > 18` (19 or more completed years). (C) Refuse at exactly 18.

**Taken: A.** Everyone with 18 completed years is above 18 years of age on every day but one; (B) would wrongly exclude them all. The remaining one-day edge (the birthday) cannot be represented on completed years at all; an encoding that needs it must take a date of birth. The helper is the only place this is decided (`above 18 years of age`), with a boundary test on each side.

**RULED 2026-09-26 (Meng): "yes 18 or older".** The reading taken above is the ruling; the shared helper `above 18 years of age` in `pc-general.l4` carries it.

## E-10 - s 87: the two limbs of consent

**Text.** "... by reason of any harm which it may cause, or be intended by the doer to cause, to any person above 18 years of age, who has given consent ... to suffer that harm; or by reason of any harm which it may be known by the doer to be likely to cause to any such person who has consented to take the risk of that harm."

**Taken.** Two limbs: consent to SUFFER the harm covers any harm caused or intended; consent to take the RISK covers only harm the doer knew to be likely (a leaf of its own). s 88 is not so split ("to suffer that harm, or to take the risk of that harm" for any harm) and is encoded without that leaf.

## E-11 - s 89 "by or by consent of the guardian"

The Illustration's father "has his child cut for the stone by a surgeon": the act is the surgeon's, done by the guardian's consent. One leaf covers both ("done by, or by the consent of, the guardian or other person having lawful charge"). No real fork; noted because proviso (d) (abetment) is also in play there, and the Illustration's "A is within the exception" is read as the father's abetment being within it too.

## E-12 - s 99's list is closed

**Text.** "by reason of the youth, the want of maturity of understanding, the unsoundness of mind, or the intoxication of the person doing that act, or by reason of any misconception".

**Taken.** The s 99 leaf names exactly those reasons. An act that is no offence for another reason (for example, one done by a person bound by law, s 76) does not give rise to the right; tested as "defending against an act that is no offence at all".

## E-13 - s 97(a) "any offence affecting the human body" vs s 101(1) "an offence against the human body or an attempt or a threat to commit the offence"

**Taken.** One leaf, "falls under the definition of an offence affecting the human body, or is an attempt or a threat to commit one", because s 101(1) says when the s 97(a) right STARTS, and it starts on an attempt or a threat. Treating "affecting" and "against" as the same class (Chapter 16's offences affecting the human body) is an assumption; the Code uses both phrases and defines neither.

## E-14 - ss 102-103: does a right that extends to death extend to lesser harm?

**Taken: yes.** s 102 says the right "extends ... to the voluntary causing of death" in the listed cases; s 103 says that otherwise it extends to "any harm other than death". The ladder is "harm other than death" OR a s 102 description, so a s 102 case covers every harm. Reading s 102 as covering death ONLY would make the right against a would-be killer narrower than against a slapper.

## E-15 - s 105(1)(d) "theft, mischief or house-breaking"

**Taken.** "house-breaking" here is read through the `the criminal trespass is house-breaking` leaf; theft and mischief through their own. The belief leaf ("the defender reasonably believes that death or grievous hurt will be the consequence, if such right of private defence is not exercised") is distinct from s 102(a)/(b)'s assault leaves, because it is about the danger from the property offence, not an assault.

## E-16 - The facts parameter is `f`, not `e`

notes/PLAN.md §2 says "the single input is always `GIVEN f IS A ...`"; §5 writes the exception ladders as `` `exception under s N` e ``. `f` was used throughout, because the charge generator's catalogue records `factsParam: 'f'`. Reported as a PLAN inconsistency.

## Where I looked and found nothing to fork

- ss 76, 77, 82, 83, 93, 95: each is one condition or a plain conjunction; the ladders read straight off the text.
- s 84(1)(b) with (2): "and" joins (2)(a) and (b), and the Illustration (knows it contrary to law, so not within (b)) confirms it.
- s 86(1): the exception ("if the person was of unsound mind by reason of intoxication") is s 85(3)'s limb exactly.
- s 94's "Except murder and offences against the State punishable with death": two leaves, both in the Code's own negative.
