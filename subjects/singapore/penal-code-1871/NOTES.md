# Penal Code 1871 -- encoding notes

This subject's idiosyncrasies, in prose, for humans. No script reads this file.

---

## 1. What this subject is

An L4 encoding of **Penal Code 1871** (2020 Revised Edition, SSO current version as at 09 Sep 2026) built so an AI agent can screen a proposed act against the constitutive tests of selected offences and ask whether s 6 takes the act outside "offence" -- by a Chapter 4 general exception, or by the Chapter 4A right of private defence.

The agent-facing entry points are in `agent-compliance.l4`:

| question | answered by |
| --- | --- |
| Which encoded offences are indicated on these facts? | `the offence screen of` |
| Is any encoded offence indicated? | `any screened offence is indicated` |
| Is the act justified, by a Chapter 4 exception or a Chapter 4A private defence? | `the act is taken outside offence by Chapter 4 or Chapter 4A` |
| Was it done in the exercise of the right of private defence? | `a private defence justification applies` |

Modules, in dependency order:

```
types.l4                      the nouns: records and enums, no rules
chapter-1-preliminary.l4      ss 2, 3, 4, 4A, 4B location facts, and the s 5 saving
chapter-2-definitions.l4      ss 6A-12, 17, 19-22A, 27-31A, 40-51 (the defined terms)
chapter-2-explanations.l4     ss 23-26, 26A-26H (dishonestly, fraudulently, rashly, ...)
chapter-2-participation.l4    ss 32-38 (common intention, cooperation, attribution)
chapter-3-punishments.l4      ss 53, 54, 72, 73, 74, 74A-74E (the punishment vocabulary)
chapter-4-exceptions.l4       ss 6, 76-95 (the whole of Chapter 4)
chapter-4a-private-defence.l4 ss 96-106A (the whole of Chapter 4A), and s 6 combined
chapter-5-abetment.l4         ss 107, 108, 108A, 108B, 111, 113, 114
chapter-5a-conspiracy.l4      ss 120A, 120B
chapter-16-life.l4            ss 299-301, 304A-304C, 305-308B, 310 (offences affecting life)
chapter-16-hurt.l4            ss 319-322, 323A, 324-338 (hurt and grievous hurt)
chapter-16-restraint-and-force.l4  ss 339-358 (restraint, confinement, force, assault)
chapter-16-unborn-and-infants.l4   ss 312-318 (miscarriage, unborn children, infants)
chapter-16-kidnapping.l4      ss 359-374 (kidnapping, abduction, slavery, forced labour)
chapter-16-sexual-general.l4  ss 377C-377D (what is sexual, exploitative, consented, mistaken)
chapter-16-sexual-penetration.l4   ss 375-377B (the penetration and minor offences)
chapter-16-sexual-images.l4   ss 377BA-377BO (voyeurism, images, abuse material)
chapter-17-cheating.l4        ss 415, 416, 416B, 418, 420, 420A
chapter-17-property.l4        ss 378, 403, 405
chapter-17-fraud.l4           ss 416A, 424A, 424B
chapter-18-forgery.l4         ss 463, 464
chapter-21-22-speech.l4       ss 499, 503, 504, 505
chapter-23-attempts.l4        s 511
agent-compliance.l4           the screen and the Schedule-to-4B classifier
agent-cases.l4                scenario fixtures, machine-asserted
registers/source-bundle/      PC1871.txt / .pdf as retrieved 09 Sep 2026
registers/verification-register.md  the fidelity pass over the pre-existing rules
registers/coverage-register.md      which sections are modelled, and which are not
registers/verification-register-pass-2.md  the fidelity pass over the rules added 09 Sep
registers/verification-register-pass-3.md  the fidelity pass over the rules added 11 Sep
registers/verification-register-pass-4.md  the fidelity pass over the Chapter 16 rules
registers/missing-sections.md       every live section with no rule, named one by one
report/machine-evaluation.md  how the encoding was machine-checked, and against what
```

The three Chapter 2 and Chapter 3 modules are **freestanding**: they define terms,
attribution rules and punishment records that the Code's own offence sections rely on, but
no offence module encoded here imports them yet, and `agent-compliance.l4` does not call
them. They are directly callable by an agent through their `@export` entry points. Wiring
them into the offence wrappers is the next piece of work, not something this draft claims
to have done.

## 2. What is deliberately not encoded

The Code lists 600 sections, of which 75 are repealed. This draft encodes **237 of the 525
live sections -- about 45%**. `registers/coverage-register.md` records which ones, chapter by
chapter and section by section; what follows is the policy behind those numbers.

The general parts are close to complete (Chapter 1: 6 of 7; Chapter 2: 49 of 54; Chapter 3:
10 of 10; Chapter 4: 20 of 21; **Chapter 4A: 12 of 12**; Chapter 5A: 2 of 2 -- and every gap
there is a section with no factual test to decide).

**Chapter 16 is complete in substance** -- 111 of its 120 live sections, all seven groups.
The nine not encoded are pure punishment sections, so every section of the chapter that
states a testable rule has one. It was opened because Chapter 4A had nothing to report a
private-defence justification against: "an offence affecting the human body" in s 97(a) is
Chapter 16's subject matter. The other offence chapters remain a deliberate thin slice: the
provisions an AI agent is most likely to walk into when checking its own output or a user's
requested act.

- **Not encoded:** Chapters 6 to 15 (State, armed forces, unlawful assembly, public servants, false evidence, public health, religion), one of Chapter 16's seven groups (below), most of Chapter 17 (extortion, robbery, stolen property, criminal trespass), currency offences, and the ten exceptions to s 499 as individual tests.
- **Chapter 16's nine punishment sections** -- ss 302, 304, 311, 323, 325, 341, 342, 363 and 363A -- are the only part of that chapter not encoded, and are excluded on the same ground as ss 109 to 120, that this subject does not compute sentence.
- **s 377BN(6)**, the marriage defence to the child abuse material offences, is **not encoded**. Its conditions turn on who is depicted in the material and who consented to what, which the `Sexual Image` record does not carry. `registers/verification-register-pass-4.md` records the gap rather than leaving it silent.
- **s 499 exceptions** are a single caller-asserted flag `a section 499 exception applies`.
- **Punishment** is not computed for any particular offence. `chapter-3-punishments.l4` encodes the Chapter 3 vocabulary -- what a `Punishment` is (s 53, s 54), how to pick the lower of two where it is doubtful which offence was committed (s 72), and the six enhanced-penalty sections that double a maximum (ss 73 to 74E). It does **not** attach a punishment to any offence section: no `the proposed act constitutes ...` wrapper returns one, and the doubling rules take the base maximum as a caller-supplied argument. The encoding still answers whether the constitutive test is met, not what sentence a court would pass.
- **ss 32 to 38** are encoded as standalone attribution tests. They are not applied automatically to the offence wrappers: an agent that wants s 34 common-intention liability must call `the person is liable under section 34 as if he did the act alone` itself.
- **The defined terms** in `chapter-2-definitions.l4` (ss 11, 19, 21, 22, 29, 30, 40, 43, 44, 51 and the rest) are likewise callable but not spliced into the offence tests, which continue to take the underlying facts as booleans asserted by the caller.
- **Chapter 5, ss 109, 110, 112 and 115 to 120** are not encoded. They are punishment and concealment provisions, consistent with this subject not computing sentence. The three substantive liability rules in that range -- ss 111, 113 and 114 -- are now encoded.
- **Computer Misuse Act 1993** is a different Act and is not in the source bundle.

## 3. Interpretive choices

- **s 415** "whether or not such deception was the sole or main inducement" is encoded by not treating that flag as a precondition.
- **s 415 Explanation 4 and 5** (a company can be deceived / induced even if no individual officer is personally deceived) are encoded as facts the caller may assert; they do not change the boolean test, which still requires `deceives a person` (s 11: "person" includes a company).
- **s 4B(1)(a)** is encoded as either relevant act in Singapore and another outside, or the reverse.
- **s 416A(3)** defence to the supply limb is encoded as: the supply limb fires unless both (purpose is not supply for an offence) and (no knowledge it will be so used).
- **s 424A / 424B** split on `is directly connected with a written or oral contract for the supply of goods or services`. Materiality is ignored (s 424A(2), s 424B(2)).
- **s 405** "intentionally suffers any other person to do so" is treated as sufficient without a separate dishonesty check on the sufferer limb, matching the disjunctive last clause of s 405.
- **s 6** is applied in every `the proposed act constitutes ...` wrapper, and since 11 Sep it is applied in full: the wrappers call `the act is taken outside offence by Chapter 4 or Chapter 4A`, so a Chapter 4A private-defence justification takes the act outside the offence exactly as a Chapter 4 exception does. `a general exception applies` is unchanged and still means Chapter 4 alone; the offence screen reports the two separately.
- **s 6A** carve-out is encoded as written: the ss 22A-26H explanations carry across to other written laws, but "dishonestly" (s 24) and "fraudulently" (s 25) do not, and any express definition in the other law displaces the Code explanation.
- **s 22 "property"** has no subsections; the four definitions are encoded as one record. "Movable property" is derived rather than asserted -- it is anything that is property under s 22 and is not immovable -- so money, things in action, intangibles and virtual currency all come out movable, which is what the definition of "movable property" ("property of every description, except immovable property") requires.
- **s 38** is permissive -- it removes an obstacle to charging participants differently rather than imposing a condition -- so it is encoded as the fact that the differing-offences outcome is open, not as a test that must be passed.
- **s 72** orders punishments as death > imprisonment for life > the longer maximum term. Fine, caning and forfeiture do not enter the ordering; where two punishments are equal on all three ranked limbs the first is not treated as the lower.
- **ss 73 to 74E** are encoded on the doubling trigger, the excluded-offence carve-outs and the statutory defence of each section. `the punishment after enhancement of` doubles the maximum imprisonment and the maximum fine **once**, however many of ss 73 to 74D are engaged, which is s 74E(1)(a). s 74E(1)(b) -- which of the engaged sections the court picks -- is not encoded, and does not matter while every section doubles by the same factor.
- **s 74E(2)** is satisfied structurally rather than by a rule. A prescribed minimum passes through `the punishment after enhancement of` unchanged, so no minimum sentence of imprisonment or caning is ever enhanced (s 74E(2)(a)); and the `Punishment` record carries no maximum number of strokes at all, only a minimum, so no maximum can be enhanced (s 74E(2)(b)).
- **s 81's Explanation** ("it is a question of fact whether the harm to be prevented was of such a nature and so imminent as to justify or excuse the risk") is encoded as a conjunct, not as commentary, on the view that without it the section does not excuse.
- **s 27** is given a first limb the section does not state -- `the person has the property physically`. s 27 is a deeming rule about possession through a spouse, clerk or servant; the encoding carries the ordinary case it builds on so the predicate is usable on its own.
- **s 84** remains encoded on the opening fact plus the s 84(1)(a)-(c) capacity limbs and the s 84(2) both-limbs requirement, as corrected in `registers/verification-register.md` (V1).

### Added 11 Sep 2026

- **Chapter 4A is encoded as two rights with a shared frame.** ss 97, 101, 104 give each right a subject matter and a window; ss 98 and 106A restrict both; ss 102, 103, 105 and 106 cap the harm. The caps are encoded as one test on the harm actually caused rather than as further elements of the right, because that is what ss 103 and 106 say: the right *does extend* to any harm other than death, and extends to death only on a s 102 or s 105 description.
- **s 99 is not a limb of s 96.** It supplies the "is an offence" element that ss 97, 101 and 104 each require, for the case where the act is no offence because of the doer's youth, immaturity, unsoundness of mind, intoxication or misconception. It is therefore encoded as an alternative inside those tests.
- **s 100 enlarges rather than restricts**, so it is a permission needed only where harm to an innocent person is actually risked. The body-right extent test reads: either no innocent person is harmed, or s 100 covers it.
- **s 106A is encoded on its double negative as written.** The bar bites only where the act does *not* cause the defender to reasonably believe that death or grievous hurt would result, so the first conjunct of each limb is a negation. Explanation 1 is a conjunct on the s 106A(1) limb; Explanation 2's two routes are disjoined on the s 106A(2) limb.
- **s 104(2) is encoded as three terminating events.** The right against theft continues *till* retreat, or assistance obtained, or recovery -- so each is a negated conjunct, not a requirement.
- **s 105(1) does not restate the s 104(1) belief.** The two are the same fact, and it is already required for the right to have started at all.
- **House-breaking is treated as within the s 104(1) list.** s 104(1) starts the property right against theft, robbery, mischief or criminal trespass; s 104(5) continues it against house-breaking, which s 104(1) does not name. House-breaking is an aggravated criminal trespass (ss 442 to 449), so it falls within the s 104(1) list — but none of those sections is encoded, so the containment is stated in the module rather than computed, and a caller asserting the house-breaking limb must assert the s 104(1) belief too.
- **The 6 ways in s 105(2) merge entry and leaving.** s 105(1)(b) distinguishes the wrongdoer who *enters* in one of the 6 ways from the one who, having been in the house, *leaves* in one of them. Each of the six facts is phrased "enters or leaves", which is what s 105(2) itself does in every one of its paragraphs.
- **s 3** is read as reaching acts wholly outside Singapore, matching the encoding of s 4. An act partly in and partly outside Singapore is the subject of s 4B, which has its own rule, and is not routed through s 3. Whether the person is liable by law to be tried here is a caller-asserted fact: no other written law is in the source bundle.
- **s 4A** takes the Chapter 6 / Chapter 6B classification as a caller-asserted fact, neither chapter being encoded. It is still decided, because without it the territorial screen reports no reach over a citizen's foreign conduct that the Code plainly reaches.
- **s 5 is decided, where s 79A is not.** Both are closure provisions that add no limb to any offence test. s 5 is given a rule anyway because it carries a consequence an agent needs: a FALSE from the screen is a statement about this Code alone, and where the conduct is or may be punishable under another written law, s 5 preserves that law untouched. `another written law is unaffected and may still apply` is that caution, made callable, and the screen reports it.
- **s 111 conjoins s 107 but not s 108.** The section fixes the abettor with the act actually done, not with the one he had in mind, so it requires abetment conduct but not that the thing abetted pass the s 108 capable-person test.
- **s 114 disjoins the s 108 abettor and the s 111 abettor**, because its opening words -- "who, if absent, would be liable to be punished as an abettor" -- reach both.
- **s 112 is not encoded.** It is a rule about cumulative punishment, and this subject does not compute sentence.

### Added 11 Sep 2026 -- Chapter 16

- **Murder is a conjunction with a subtraction.** s 300 makes culpable homicide murder on any of four limbs "except in the cases hereinafter excepted", so `constitutes murder` is s 299, plus a s 300 limb, minus all seven Exceptions. `constitutes culpable homicide not amounting to murder` is the complement, and is decided here because it is a classification and not a sentence.
- **s 299 Explanations 1 and 2 are routes to causation, not conjuncts.** Accelerating the death of a person already diseased is causing it, and so is inflicting an injury from which treatment might have saved the victim. Each supplies causation where it might be doubted, so they are disjoined with the plain "causes death by doing an act".
- **s 299 Explanation 3 is a limit and is encoded as one.** Causing the death of a child in the womb is excluded from homicide unless some part of the child had been brought forth.
- **s 300 Exception 2 is where Chapter 4A runs out.** If the right of private defence is not exceeded, s 96 makes the act no offence at all and no question of murder arises. Exception 2 governs the case where the right existed and was exceeded, and can only reduce murder to culpable homicide. The two are kept separate: the wrapper tests `a private defence justification applies`, the murder rule tests the Exception.
- **s 300 Exception 7's middle limb carries s 84(2)'s two-limb structure.** The impairment of the capacity to know the acts are wrong counts only if it extended to knowing both that they are wrong by the ordinary standards of reasonable and honest persons and wrong as contrary to law.
- **s 320 conjoins s 319.** "The following kinds of hurt only are designated as grievous" is a closed list of kinds of *hurt*, so grievous hurt requires hurt. Limb (aa) is the one that makes this worth saying: death is grievous hurt for Chapter 16 purposes.
- **s 322 does not require the intended kind and the caused kind to match**, because its Explanation says so expressly. `the hurt intended or known to be likely is grievous hurt` is one fact about gravity, not about which limb of s 320.
- **s 328 does not build on s 321.** It is complete on administering the substance with one of three fault states, whether or not hurt follows -- the only section in the hurt group that needs no hurt in fact. ss 335B and 336 are the same in that respect.
- **ss 335A(3) and 304C(5) gather their five exculpated cases into one caller-asserted fact.** Each defines the third party's "unlawful act" as one that would be an offence but for the actor being within s 82 or s 83, or entitled to rely on unsoundness of mind, intoxication or mistake of fact. Those are Chapter 4 tests already encoded, but applying them here would need the third party's own facts, which these records do not carry.
- **s 304C(3) is a defence to the second alternative only.** An accused whose own act caused the death cannot be heard to say he could not have protected the victim from himself, so the "could not have been expected to take any such step" fact is a negated conjunct inside the failure-to-protect branch, not on the whole section.
- **s 349's proviso is a requirement, not a gloss.** Force is used only if the motion was caused by the actor's own bodily power, by disposing a substance, or by inducing an animal. So the rule conjoins the two effects with the three ways.
- **s 351 needs no force and no contact.** An assault is complete on the apprehension. Its Explanation excludes only the case resting on words with no gesture or preparation at all.
- **The s 352 Explanation is encoded as three disqualifiers of the provocation**, shared by ss 352, 355 and 358, so that a disqualified provocation leaves the case in s 352 rather than s 358.
- **ss 347 and 348 do not share facts with ss 327 and 330**, though they are close neighbours. s 347 says "to do anything illegal or to give any information which may facilitate the commission of an offence"; s 327 says "to do anything which is illegal or which may facilitate the commission of an offence". The facts are kept separate so neither section is read through the other's words.
- **`an encoded hurt offence is made out` is deliberately not wired into s 97(a).** The private-defence right continues to take "an offence affecting the human body" as a caller-asserted fact. The facts that would have to be asserted are the assailant's, not the defender's, and the `Proposed Act` bundle carries one actor's facts only; and one of Chapter 16's seven groups is still unencoded, so a FALSE is not yet a statement that no such offence is in play. Wiring it in would make the right look computed when it is not.

### Added 11 Sep 2026 -- Chapter 16, second part

- **"Subject to the Termination of Pregnancy Act 1974" is a negated conjunct.** ss 312, 314 and 315 each open with it. That Act is not in this source bundle, so whether the act falls within it is caller-asserted, and it is encoded the same way as the Electronic Transactions Act 2010 in s 29B and the Organised Crime Act 2015 in s 308A -- the cross-referenced Act's own test is not re-derived here.
- **s 313 does not conjoin the 16-week duration.** s 312 punishes more heavily where the pregnancy is of more than 16 weeks, but s 313 applies "whether the woman's pregnancy is of more than 16 weeks' duration or not", so the duration is expressly immaterial to it.
- **s 314's Explanation removes a fault element rather than adding one.** It is not essential that the offender knew the act was likely to cause death, so nothing is conjoined for it.
- **s 315(2) is evidence, not an element.** Pregnancy of 28 weeks or more is *prima facie evidence* that the child was capable of being born alive. The fact is carried so a caller can assert it, and it is not conjoined.
- **s 316's culpable-homicide circumstance is carried, not computed.** It is a counterfactual about the offender's state of mind -- what would have been true had the act killed a person -- and no death of a person has occurred to test s 299 against.
- **s 318 needs no separate attempt analysis.** "intentionally conceals **or endeavours to conceal**" makes the offence complete on the attempt.
- **Abduction is not a kind of kidnapping.** s 359 says kidnapping is of two kinds and ss 360 and 361 define them; s 362 defines abduction separately. It needs no minority, no guardian and no crossing of the border. ss 364 to 367 open "kidnaps or abducts", so that disjunction is gathered once and each section adds its own purpose.
- **The Exception to s 361 is defeated by an immoral or unlawful purpose.** The section does not extend to a person who in good faith believes himself the father of an illegitimate child or entitled to its custody, *unless* the act is for an immoral or unlawful purpose -- so the good-faith belief is encoded as a protection that the purpose removes.
- **s 368 does not conjoin the kidnapping.** It attaches to a kidnapping or abduction committed by someone else; knowledge of it is the element. Its "punished in the same manner as if he had kidnapped" is a punishment direction, so only the conduct is decided.
- **The ss 372 and 373 presumptions are not encoded.** Each section presumes, until the contrary is proved, that one who disposes of or obtains a female below 21 to or from a prostitute or brothel-keeper did so for prostitution. Those are rebuttable presumptions of fact, not elements.

### Added 11 Sep 2026 -- Chapter 16, the sexual offences

- **s 377CB narrows s 90, it does not extend it.** "a consent ... is not a consent given by a person under a misconception of fact **only if** it is directly related to" the nature of the act, its purpose, or the identity of the actor. Under s 90 any misconception can vitiate; under s 377CB only these three can, and only where the actor knew or had reason to believe the consent followed from it. Illustration (d) -- the belief that the man was an influential movie director -- is the case the narrowing decides, and it is a valid consent. `the consent is not a consent within section 90` must therefore **not** be used for a sexual offence; the two rules are kept apart and the sexual offence sections use this one.
- **s 377D's default is that the defence is unavailable.** "a reasonable mistake as to the age of a person cannot be a defence to any charge for a sexual offence", subject to two subsections. So the rule decides when the defence *is* available, not when it is excluded: only where the 16-to-18 age band is a physical element, and then only absent a prior charge and absent a failure to take all reasonable steps. `a mistake as to age is a defence` is therefore conjoined, negated, to ss 376AA, 376EA, 376EC, 376EE and 377BL and to nothing else.
- **s 377CA(3) is a second, independent defeater of the presumption.** A person lawfully married to the minor is outside the s 377CA(2) presumption even where the relationship falls within one of its seven limbs. It is not an eighth relationship but a carve-out from all of them, so it is a separate negated conjunct alongside the rebuttal.
- **The below-16 / 16-to-18 pairs are the Act's own device and the encoding follows it.** ss 376A and 376AA, 376E and 376EA, 376EB and 376EC, 376ED and 376EE are four such pairs. The second of each attracts the s 377D defence and the exploitative-relationship element; the first attracts neither.
- **Consent is irrelevant to the age offences and the encoding says so by omission.** ss 376A(1B), 376AA(2) and 376G(5) each provide that the prosecution need not prove consent and that consent is no defence. The consent facts therefore appear nowhere in those rules.
- **ss 375 and 376 are not symmetrical between their limbs.** The s 375(5) good-faith belief in consent answers the non-consent limb only; the s 375(4) spouse carve-out answers the below-14 limb only. The two limbs are built separately and then disjoined, rather than sharing one set of conjuncts. s 376(5)(b) has its own asymmetry: the belief must extend both to consent and to the other person not being below 14.
- **ss 376F and 376H are offences where the other person DID consent.** What makes them offences is how the consent was procured -- by inducement, threat or deception on a person with a mental disability (s 376F), or fraudulently by a representation about a protective measure or disease risk (s 376H). s 376F treats a spouse differently: an inducement offered to a spouse is not enough, only a threat or deception.
- **ss 377 and 377B keep consent only on their causing limbs.** Neither a corpse nor an animal can consent, so the absence of consent appears only where the accused causes *another person* to do or undergo the act -- s 377(1)(e) to (h) and s 377B(3).
- **The image defences are section-specific and are not gathered.** s 377BM(1) answers s 377BD alone; s 377BM(2) answers ss 377BB, 377BC, 377BD and 377BE(1) but **not** s 377BE(2), the threat limb; s 377BN(1) answers s 377BK alone; s 377BN(2) to (4) answer ss 377BH to 377BK but **not** s 377BG. Each offence conjoins only the defences its own section names, and there is deliberately no single "a defence applies" predicate.
- **s 377BE(2) does not require the image to exist.** s 377BE(6) provides that the prosecution need not prove that the image mentioned in the threat exists, or that it is in fact intimate. The threat limb therefore conjoins neither.
- **s 377BB(6) stands outside the knowledge element.** Installing equipment or adapting a structure to enable a voyeurism offence is complete on the intention; it does not need the accused to know the victim does not consent, so it is disjoined outside that conjunction.
- **s 377BN(5) is encoded as nothing.** A mistaken belief that reasonable persons would not regard the material as offensive is expressly *not* a defence. The fact is carried so a caller can assert it, and it contributes to no rule -- which is the correct encoding of a provision that closes a defence off, and the same treatment s 79A gets.

## 4. Status

`draft`. No claim of fidelity. No HG1/HG2 grant.

Machine-checked: 26 modules, 0 type errors, 192 of 192 assertions satisfied
(`report/machine-evaluation.md`). §7.2 of that report records two blind spots in the
available engine which a future run should read it subject to.

Every encoded rule has now been read back against the deposited source text, in four passes:
`registers/verification-register.md` for the rules that existed before 09 Sep 2026 (twelve
defects, all fixed), `registers/verification-register-pass-2.md` for the rules added that day
(four defects, all fixed), `registers/verification-register-pass-3.md` for the eighteen
sections added on 11 Sep (no defect found; three drafting traps and two caller traps
recorded), and `registers/verification-register-pass-4.md` for the 111 Chapter 16 sections
added the same day (no defect found; nine drafting traps and two structural limits recorded).
No pass is an adversarial review, and none can reach the sections
`registers/coverage-register.md` records as absent. Passes 3 and 4 read back rules written
the same day, which is a weaker check than passes 1 and 2 -- each says so on its own first
page.

