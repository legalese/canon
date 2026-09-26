# body-b forks - Penal Code 1871, Chapter 16, ss 359-377D

Every ambiguity met while encoding the sections marked `encoded` in `body-b-coverage.md`: the readings, the one taken, why, and the text that licenses each.
Where a fork was looked for and none found, the section is listed at the end.

## B-1. s 360 - "without the consent of that person, or of some person legally authorised to consent on behalf of that person"

- **Reading A (taken):** the conveying must be without the consent of BOTH - consent from either the person or an authorised person takes it out of the section. Encoded as two leaves joined by AND (`without the consent of that person` ... `without the consent of any person legally authorised to consent on behalf of that person`).
- **Reading B:** the consent that matters is the person's own, or (where the person cannot consent) the authorised person's - a disjunction by capacity.
- Why A: "without the consent of X, or of Y" negates a disjunction; the section contemplates the authorised person consenting "on behalf of" the person, which would be pointless if that consent did not count. The leaf's @desc tells the investigator to answer TRUE where there is no authorised person. Test: `conveyed with authorised consent`.

## B-2. s 361 Exception - in the ladder, as a negated leaf

- The Exception is part of s 361, not a General Exception (PLAN s 5), so it is in `kidnaps from lawful guardianship` as `NOT (the section 361 Exception applies f)`.
- The charge generator fills unknown leaves FALSE; a FALSE belief leaf means "exception not established", so an unknown never withdraws a charge. The burden reading (that the accused must bring himself within it) is the conventional one but the section does not say who proves the good-faith belief; recorded, not resolved.
- "unless such act is committed for an immoral or unlawful purpose" is a NOT on the purpose leaf inside the exception. Tests: `putative father`, `putative father, unlawful purpose`.

## B-3. s 364 Illustration (b) - "forcibly carries or entices B away from his home"

- "Forcibly carries" is abduction (s 362, "by force compels ... to go from any place").
- "Entices" is not abduction (no force, no deceit) and is kidnapping only from lawful guardianship (s 361), which needs B to be a minor below 16 or of unsound mind, taken out of a guardian's keeping.
- **Reading taken:** the Illustration presupposes B is such a person when it says "entices"; the test `s 364 illus (b), entices` supplies B as a minor below 16 in his mother's keeping. An enticing of a competent adult is not s 364 on this encoding. The Illustration's "from his home" is read as "out of the keeping of the lawful guardian".

## B-4. s 363A (and s 377BB(7), s 377BC(3)) - "or with any combination of such punishments"

- `Punishment` has one boolean, `or with both`. Three alternatives (imprisonment, fine, caning) "or any combination" is recorded as `or with both` = TRUE, with the section's words verbatim in `words`.
- A reader of the record who needs to distinguish "both of two" from "any combination of three" must read `words`. Proposed for the shared domain: rename or widen the field (`or any combination`).

## B-5. s 367 - "or knowing it to be likely that such person will be so subjected or disposed of"

- The knowledge limb is one leaf, covering all three harms (grievous hurt, slavery, non-consensual penile penetration of the anus or mouth), because "so subjected or disposed of" refers back to all of them.
- The charge names the harm from a STRING (`the harm intended`); which harm is not itself a toggleable leaf on the knowledge limb. A finer encoding would split the knowledge limb into three; not done because the section does not.

## B-6. s 368 - "shall be punished in the same manner as if he had kidnapped or abducted such person with the same intention ..."

- The punishment is whichever of ss 363-367 fits the concealer's own intention or knowledge. The encoding does not pick it: there is no `punishment prescribed by s 368` record, and `charge under s 368` carries the section's words (`the punishment of section 368`).
- To pick it, the s 368 facts would have to carry the concealer's intention and re-run ss 364-367's purpose limbs over it. Deferred; `pc-general`'s readers (`punishable with imprisonment` etc.) therefore cannot be applied to s 368.

## B-7. One facts record for ss 375, 376, 376A, 376AA

- PLAN s 2 suggests `Rape Facts`. **Taken:** one `Sexual Penetration Facts`, because s 376A(1A) excludes from s 376A any act that "would constitute an offence under" ss 375 and 376 - which can only be decided if s 376A reads their ladders over the same facts - and because the same act is routinely charged in the alternative. The catalogue's `factsType` for all eight penetration charges is therefore `Sexual Penetration Facts`.

## B-8. The `N` in `offence under s N` for sections that define and punish by subsection

- **Taken:** `N` is the punishing subsection: `375(2)`, `375(3)`, `376(3)`, `376(4)`, `376A(2)`, `376A(3)`, `376AA(3)`. That is what CPC s 123(4) and PLAN s 2 ask for, and the `Charge`'s closing words read "an offence punishable under section 375(2)".
- Singapore charges in practice often read "an offence under section 375(1)(a) and punishable under section 375(2)". The shared `frame the charge` has one section slot; this encoding does not change it. The defining limb is recited in the body (the consent and age clauses). Proposed for `pc-general`: a builder with a defining-section slot.
- s 376A(2) punishes by (a)/(b) on the exploitative-relationship fact. **Taken:** one `offence under s 376A(2)`, with the punishment words chosen by the leaf in the charge builder, as PLAN s 6 prescribes (the reference row does the same for s 420(2)).
- "Subject to subsection (3)" in s 375(2) (and "(4)" in s 376(3)) is read as displacing only the punishment: every rape is `offence under s 375(2)`; the aggravated ones are ALSO `offence under s 375(3)`. The alternative (s 375(2) = rape AND NOT aggravated) would make an unknown aggravating fact (filled FALSE) assert its absence.

## B-9. s 375(4), s 376(5)(a), s 376A(4) - "against his wife with her consent"

- The ladders use one consent leaf, `without the victim's consent`. The spouse exception is written as `NOT spouse OR without consent`, not as `NOT (spouse AND NOT without consent)` with a separate "with consent" leaf.
- Effect: where the victim is the spouse and consent is unknown, limb (b) is NOT made out - an unknown consent is never treated as the absence of consent. A spouse's non-consent must be supplied, and then limb (a) holds anyway.
- s 375(4) says "his wife"; the leaf is `the victim is the accused's spouse` (s 376(5)(a) and s 376A(4) say "spouse"). For s 375 the accused is a man; whether a husband of a man is within s 375(4) is not reached.

## B-10. s 376A(1A) - "would constitute an offence under"

- **Taken:** "would constitute an offence" means the offence is made out INCLUDING the sections' own answers (s 375(4), (5); s 376(5)). So where s 375(5)'s mistake defence is proved, s 375(1)(a) is not made out and s 376A is not excluded.
- **Alternative:** "would constitute" looks only at the physical and fault elements, ignoring defences, so an act excluded from s 375 by a defence is still excluded from s 376A. That reading leaves a gap (no offence at all), which is why it was not taken.
- "376(2) (if the victim B is of or above 14 years of age)" is encoded as `NOT the victim is below 14 years of age`. This is the one NOT on an age leaf; it is safe because s 376A itself requires one of the two below-16 bands to be TRUE.
- Consequence tested: a consensual penetration of a girl of 13 is both s 375(2) and s 376A(3) (`girl of 13 consenting`), because only "375(1)(b) READ WITH 375(3)" is excluded.

## B-11. s 376(5)(b) - "believed that B ... did consent to the penetration and B was not below 14 years of age"

- **Taken:** "and B was not below 14 years of age" is a fact about B, not part of the belief. The defence fails for a victim below 14 even if the accused believed otherwise (consistent with s 377D(1)). Test: `digital, girl of 12, mistake as to consent proved`.

## B-12. s 377D(2)-(3) - the defence's conditions as leaves

- (3)(b) "failed to take all reasonable steps to verify" is encoded as the POSITIVE leaf `took all reasonable steps to verify ...`, required TRUE. Under schema completion an unknown is FALSE, so the defence is never established by default and a charge is never refused on facts nobody supplied.
- (3)(a) "has previously been charged" is a leaf required FALSE: an unknown prior charge does not defeat a defence that the other leaves establish. Recorded, because the burden on (3)(a) is not stated.
- s 377D(2) applies "where the fact that a minor is of or above 16 ... but below 18 ... is a physical element of the offence". In the encoded sections that is s 376AA only. Sections 376EA, 376EC, 376EE, 377BL (deferred) will need the same drill-down.

## B-13. s 364 Illustration (a) - "intending or knowing it to be likely that Z may be sacrificed"

- The section says "in order that such person may be murdered"; the Illustration uses "intending or knowing it to be likely". **Taken:** the Illustration widens the leaf, and the leaf's @desc says so, rather than adding a separate knowledge limb the section does not have.

## B-14. ss 375(3)(a), 376(4)(a) - "voluntarily causes hurt to any person" / "puts ... in fear of death or hurt"

- One leaf each, cross-module: "voluntarily causes hurt" is s 321 (body-a). The fear limb is not a defined term and is a flat leaf. s 376(4)(a)(ii) says "to himself or any other person" where s 375(3)(a)(ii) says "to that person or any other person"; the same leaf serves both, since both cover fear of hurt to anyone.

## B-15. s 377CA(1) - a judgement, not a rule

- Whether a relationship is exploitative is "to be determined by the court in the circumstances of each case", having regard to four factors. The encoding does not decide it: the offence ladders read one leaf, and s 377CA(2)-(3)'s presumption is the drill-down. The presumption's rebuttal ("until the contrary is proved") is a leaf. Whether "lawfully married" in (3) displaces only the presumption, or also the court's (1) determination, is not reached: (3) says "the presumption ... does not apply", which is all that is encoded.

## B-16. s 377BA - the grouping of the alternatives

- "utters any word, makes any sound or gesture, or exhibits any object, intending that such word or sound will be heard, or that such gesture or object will be seen by such person, or intrudes upon the privacy of such person".
- **Taken:** the "intending that ... heard/seen" clause qualifies the first four acts only; intrusion upon privacy stands alone. The alternative - that intrusion also requires an intention to be seen or heard - makes no sense of the words.
- The investigator is not asked to match word with heard and gesture with seen; one leaf covers "heard or seen" as the section's own clause does.

## B-17. ss 370-374 - names of offences

- "unlawfully" in s 374 is s 43's word (`illegal within section 43`, pc-general); it rides in the leaf `unlawfully compels the person to labour`, with the Chapter 2 ladder as the drill-down.

## Where no fork was found

ss 359, 362, 363, 365, 366 (beyond B-1/B-3 above), 370, 371, 374, 376AA(1), 377CB (its four Illustrations settle the only question it raises: identity vs attributes).
