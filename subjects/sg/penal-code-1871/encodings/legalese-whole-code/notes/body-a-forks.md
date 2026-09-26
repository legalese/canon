# body-a forks - Penal Code 1871, Chapter 16, ss 299-358

Every ambiguity met while encoding `pc-body-a-life.l4`, `pc-body-a-hurt.l4` and `pc-body-a-force.l4`: the readings, the one taken, why, and the text that licenses each.
Where I looked and found no fork, I say so at the end.

## F-1. Field names differ from the reference row's `Hurt Facts`

**Text.** The reference row's `hurt-321-323A.l4` names its leaves `cause hurt`, `not grievous` and `grievous`; PLAN §2 says a leaf is "the Code's own words for the element".
**Readings.** (a) keep the reference names so the app's existing s 323A card keeps working; (b) use the Code's words.
**Taken.** (b). s 319 is now its own ladder (`causes hurt`, four atoms including the Explanation's unconsciousness) and s 320 its own (`grievous hurt within section 320`, twelve atoms), so s 321 and s 323A draw a callee box where the reference drew a leaf.
The kept names are `intention of causing hurt` and `knowledge of being likely to cause hurt`.
**Consequence.** The catalogue's s 323A entry must be re-pointed at integration; its fixtures in the app will not type-check against the new record.

## F-2. The hurt aimed at, in ss 322, 323A, 334A: two positive leaves, never a leaf and its NOT

**Text.** s 322 "if the hurt which he intends to cause or knows himself to be likely to cause is grievous hurt"; s 323A "... is not grievous".
**Readings.** (a) one BOOLEAN and its negation; (b) two positive BOOLEANs.
**Taken.** (b). The charge generator fills an unknown leaf with FALSE (PLAN §3.4); under (a) an investigator who has said nothing about intent would see `NOT grievous-intended` TRUE and s 323A frame on a fact nobody supplied.
The cost: nothing stops both leaves being TRUE at once; a later pass could add a consistency assertion.

## F-3. "Except in the case provided for by section N" (ss 323, 324, 325, 326)

**Text.** s 323 "Whoever, except in the case provided for by section 323A or 334, voluntarily causes hurt"; likewise s 324 (334), s 325 (323A, 334A, 335), s 326 (335).
**Readings.** (a) an element: the offence is made out only when the excepted case is not; (b) a pointer telling the prosecutor which section to charge, not something the charge alleges.
**Taken.** (a), as `NOT (offence under s N f)` in the ladder, so exactly one of the overlapping sections frames and the refusal names the section to charge instead.
Under schema completion the unknown provocation leaves are FALSE, so the NOT is TRUE and s 323 frames - the safe direction, since provocation is the accused's to raise.
A real charge under s 323 does not recite "otherwise than on provocation", so the recital does not either; only the ladder carries it.
**Not excepted.** s 323 does not except s 324, and s 325 does not except s 326: a knife-hurt frames under both s 323 and s 324 (asserted). The aggravated section is the prosecutor's choice, not the Code's exclusion.

## F-4. "or with any combination of such punishments"

**Text.** ss 304(b), 308, 324, 354: "or with fine, or with caning, or with any combination of such punishments".
**Taken.** `or with both` TRUE, with `words` authoritative, following pc-general's G-12 (one flag, words verbatim). "Any combination" of three is wider than "both"; the flag cannot say so.

## F-5. s 328: the heading says "causing hurt", the enacting words do not

**Text.** Heading "Causing hurt by means of poison, etc., with intent to commit an offence"; body "Whoever administers ... with intent to cause hurt ..., or with intent to commit or to facilitate the commission of an offence, or knowing it to be likely that he will thereby cause hurt".
**Taken.** The body. No hurt need be caused (asserted: the drugged drink with no hurt frames). The charge's offence name is the heading, as CPC s 123(2) asks.

## F-6. The negligent limb and s 26F(2)

**Text.** ss 304A, 336, 337, 338: "(a) in the case of a rash act ...; (b) in the case of a negligent act"; s 26F(2) (as pc-general encodes it): negligence is also established by rashness, knowledge or intention.
**Readings.** (a) the limbs are exclusive - rash goes to (a), negligent to (b); (b) (b) is made out by a rash act too.
**Taken.** (b): `a negligent act` is `does the act negligently` OR `does the act rashly`, with s 26F(2) quoted inert in the ladder; asserted on the rash-driving fixture.
Not taken further: s 26E(3) (rashness established by intention or knowledge) is not folded into `a rash act`, because an intentional act that endangers life is not the case these sections are drafted for and the investigator answers `does the act rashly` directly. That is a choice a reviewer should check.

## F-7. The Exceptions to s 300, and every "positive-phrased proviso"

**Text.** s 300 "Except in the cases hereinafter excepted"; Exception 1's provisos are negative conditions ("that the provocation is not sought ...").
**Taken.** Each Exception is an exported ladder; murder is `commits culpable homicide` AND a limb AND NOT `an Exception to section 300 applies`.
The provisos are leaves phrased positively in the Code's own negative words (`the provocation is not sought or voluntarily provoked ...`), so an unknown proviso is FALSE and the Exception does not apply.
Consequence: with nothing said about the Exceptions, murder frames. That is the Code's allocation - the Exceptions are for the accused to bring himself within (PLAN §5's Evidence Act citation is unverified, G-15) - not a default chosen here. The same shape is used for the provocation provisos of ss 334-335 (s 335 Explanation) and ss 352, 355, 358 (s 352 Explanation), and for the s 339 Exception.

## F-8. s 354 needs a s 350 purpose, and the natural one is circular

**Text.** s 354 "Whoever assaults or uses criminal force to any person, intending to outrage ... the modesty of that person"; s 350 criminal force requires "in order to cause the committing of any offence, or intending ... or knowing it to be likely that ... he will illegally cause injury, fear or annoyance".
**Found by a test.** The lift fixture set the outrage-of-modesty intent but no s 350 purpose, and `offence under s 354(2)` failed. The expected value was right; the fixture was incomplete. It was completed with "in order to cause the committing of any offence" - the s 354 offence itself.
**For the charge generator.** An investigator who ticks "intending to outrage modesty" and not one of the three s 350 purposes will get a refusal naming "assaults ... or uses criminal force". That is correct law but a trap in the interview; the app should prompt for the s 350 purpose, or a later encoding could make the s 354 intent satisfy the "offence" purpose by rule. Not done here, because the Code does not say so in terms.

## F-9. s 301 is not re-encoded

It is a deeming rule that changes which description of culpable homicide attaches; it has no punishment and no charge of its own. The reference row's `culpable-homicide-301.l4` encodes it over its own `Killing` record. Deferred rather than ported for time; porting it onto `Homicide Facts` would let `commits murder` read the transferred description.

## F-10. "above 18 years of age" (s 300 Exception 5) in completed years

**Readings.** (a) completed years AT LEAST 18 (has passed the 18th birthday); (b) completed years > 18 (turned 19).
**Taken.** (a): a person aged 18 years and some months is above 18 years of age in ordinary usage. The only case (a) gets arguably wrong is the 18th birthday itself, which a whole-years helper cannot see. Contrast "below 14 years of age" and "below 18 years of age", which are unambiguous as `< N` over completed years.

**RULED 2026-09-26 (Meng): "yes 18 or older".** The reading taken above is the ruling; the shared helper `above 18 years of age` in `pc-general.l4` carries it.

## F-11. Overlapping punishing provisions both frame

- s 302(1) and s 302(2): where s 300(a) and (c) both hold (the knife-cut with intent to kill), both frame. The Code does not exclude (a) from (2); the choice of charge is the prosecution's.
- s 354(1) and (2), s 354A(1) and (2): (2) says "Whoever commits an offence under subsection (1) ...", so (1) is made out whenever (2) is. Both frame.
- ss 336, 337, 338 all frame on one act that endangered life and caused grievous hurt, since each reads its own result leaf. The Code grades them; it does not exclude.

## F-12. s 304(b)'s "without any intention"

**Text.** "(b) if the act is done with the knowledge that it is likely to cause death, but without any intention to cause death, or to cause such bodily injury as is likely to cause death".
**Taken.** NOT over the two intention leaves. With intent unknown (FALSE), s 304(b) frames rather than s 304(a) - the lesser limb, and the refusal of s 304(b) where intent IS shown points to s 304(a).

## F-13. Punishments that depend on a fact, and s 307(2)

- s 307(1) and s 308 ("and if hurt is caused to any person by such act ...") and s 312 ("and if the woman's pregnancy is of more than 16 weeks' duration") are one offence each, with two `Punishment` records chosen in the charge builder by the leaf, as PLAN §6 and the reference s 420(2) do.
- s 307(2) ("may, if hurt is caused, be punished with death") is a sentencing permission, not a new offence. It is encoded as its own `offence under s 307(2)` / `charge under s 307(2)` so the card can show the death-eligible case; its `Punishment` records death as `or with` (it is "may"). A reviewer may prefer it folded into s 307(1)'s punishment choice.
- s 326 "and shall also be liable to caning or if he is not sentenced to imprisonment for life, liable to fine" and ss 302(2), 305, 311, 313 conditional fines: the condition is not modelled; `words` carries it.
- s 332's "provided that in exceptional circumstances imprisonment need not be imposed": imprisonment is recorded as `shall be punished with`; the proviso lives only in `words`.

## F-14. s 356's theft is a leaf, and cannot become a call

**Text.** "in committing or attempting to commit theft of any property which that person is then wearing or carrying".
Theft (s 378) is property's. PLAN §1 lists property -> body-a (ss 382, 394, 397 read hurt) and not the reverse; adding body-a -> property would make a cycle. The leaf's @desc says so. A join, if wanted, belongs in the charge sheet that imports both.

## F-15. Rash Act Facts' hurt and death leaves are not calls into ss 319, 320, 299

ss 337, 338 and 304A read "causes hurt", "causes grievous hurt", "not amounting to culpable homicide" - all defined in this group - but over a different record. They are flat leaves whose @desc names the section. Nesting a `Hurt Facts` inside `Rash Act Facts` would let the card drill down; not done for time, and because the rash-act investigator is asking about a result, not about the accused's intention toward hurt, which is most of `Hurt Facts`.

## F-16. s 351 illus (c) has no expected value

"the gesture explained by the words **may** amount to an assault". Not asserted: a "may" is not an answer. The Explanation ("Mere words do not amount to an assault") is asserted instead.

## F-17. s 340 illus (b): threat as obstruction

A places armed men at the exits and tells Z they will fire. The obstruction is by threat, not physical barrier. Taken as `voluntarily obstructs that person` (the leaf's @desc says obstruction may be by threat), so illus (b) is illus (a) on the same atoms.

## F-18. s 300(b) illustration's second limb

"But if A, not knowing that Z is labouring under any disease, gives him such a blow as would not in the ordinary course of nature kill a person in a sound state of health, here A, although he may intend to cause bodily injury, is not guilty of murder". The illustration does not say whether it is culpable homicide; the fixture carries only an intention to cause bodily injury, so neither s 299 nor s 300 is made out, and only NOT murder is asserted.

## F-19. s 305(1)'s "minor or other person who lacks capacity" is one leaf

The two limbs of s 305(2) ("minor" = below 18; "person who lacks capacity" = four causes) are one leaf with the helper `below 18 years of age` for the age limb. Splitting them would let the ladder show which; not done for time.

## Where I looked and found no fork

s 319's Explanation (unconsciousness) widens the leaf set without ambiguity; s 320's list is closed ("only"); s 349's three ways are exhaustive by its proviso; ss 341, 342, 345-348 punish without qualification; s 353's three limbs mirror s 332's.
