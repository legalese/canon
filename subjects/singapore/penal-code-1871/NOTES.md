# Penal Code 1871 -- encoding notes

This subject's idiosyncrasies, in prose, for humans. No script reads this file.

---

## 1. What this subject is

An L4 encoding of **Penal Code 1871** (2020 Revised Edition, SSO current version as at 09 Sep 2026) built so an AI agent can screen a proposed act against the constitutive tests of the Code's offences and ask whether s 6 takes the act outside "offence" -- by a Chapter 4 general exception, or by the Chapter 4A right of private defence. Since 16 Sep 2026 it covers every live section of the Act.

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
chapter-1-preliminary.l4      s 1 short title, ss 2, 3, 4, 4A, 4B location facts, and the s 5 saving
chapter-2-definitions.l4      ss 6A-12, 17, 19-22A, 27-31A, 40-51 (the defined terms, and the ss 7-9, 49, 50 conventions)
chapter-2-explanations.l4     ss 23-26, 26A-26H (dishonestly, fraudulently, rashly, ...)
chapter-2-participation.l4    ss 32-38 (common intention, cooperation, attribution)
chapter-3-punishments.l4      ss 53, 54, 72, 73, 74, 74A-74E (the punishment vocabulary)
chapter-4-exceptions.l4       ss 6, 76-95 (the whole of Chapter 4)
chapter-4a-private-defence.l4 ss 96-106A (the whole of Chapter 4A), and s 6 combined
chapter-5-abetment.l4         ss 107-120 (the whole of Chapter 5, punishments included)
chapter-5a-conspiracy.l4      ss 120A, 120B
chapter-6-state.l4            ss 121-130A (the whole of Chapter 6)
chapter-6a-6b-piracy-and-genocide.l4  ss 130B-130E (Chapters 6A and 6B)
chapter-7-armed-forces.l4     ss 131-140B (the whole of Chapter 7)
chapter-8-unlawful-assembly.l4  ss 141-158 (the whole of Chapter 8)
chapter-9-public-servants.l4  ss 161-171 (the whole of Chapter 9)
chapter-10-contempts.l4       ss 172-190 (the whole of Chapter 10)
chapter-11-false-evidence.l4  ss 191-200 (false evidence)
chapter-11-public-justice.l4  ss 201-229 (offences against public justice)
chapter-12-government-stamps.l4  ss 255-263 (the live sections of Chapter 12)
chapter-14-public-tranquility.l4  ss 267A-268C, 290, 291 (affray, incitement, nuisance, hoaxes)
chapter-14-public-health-and-safety.l4  ss 269-289 (infection, food, drugs, ways, rash conduct)
chapter-14-obscenity.l4       ss 292-294 (obscene objects and acts)
chapter-15-race.l4            ss 298, 298A (the live sections of Chapter 15)
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
chapter-17-extortion-and-robbery.l4  ss 380-382, 383-389, 390-402
chapter-17-stolen-property.l4 ss 404, 407-409, 410-414
chapter-17-mischief-and-trespass.l4  ss 421-424, 425-440, 441-462
chapter-18-forgery.l4         ss 463, 464
chapter-18-forged-documents.l4  ss 466-477A (aggravated forgery, forged documents, false instruments, accounts)
chapter-18-currency.l4        ss 489A-489I (counterfeit and altered currency and bank notes)
chapter-21-22-speech.l4       ss 499, 501, 502, 503, 504, 505, 507
chapter-23-attempts.l4        s 511
punishment-provisions.l4      ss 302, 304, 311, 323, 325, 341, 342, 363, 363A, 379, 379A, 384, 392,
                              395, 406, 417, 419, 426, 447, 448, 458A, 465, 500, 512 (the standalone
                              punishment sections, as Chapter 3 Punishment values)
agent-compliance.l4           the screen and the Schedule-to-4B classifier
agent-cases.l4                scenario fixtures, machine-asserted
registers/source-bundle/      PC1871.txt / .pdf as retrieved 09 Sep 2026
registers/verification-register.md  the fidelity pass over the pre-existing rules
registers/coverage-register.md      which sections are modelled, and which are not
registers/verification-register-pass-2.md  the fidelity pass over the rules added 09 Sep
registers/verification-register-pass-3.md  the fidelity pass over the rules added 11 Sep
registers/verification-register-pass-4.md  the fidelity pass over the Chapter 16 rules
registers/verification-register-pass-5.md  the fidelity pass over the Chapter 17 rules
registers/verification-register-pass-6.md  the fidelity pass over the Chapter 18 rules
registers/verification-register-pass-7.md  the fidelity pass over the completion-pass rules
registers/verification-register-pass-8.md  the fidelity pass over the last seven sections
registers/missing-sections.md       every live section with no rule, named one by one (none since 16 Sep)
report/machine-evaluation.md  how the encoding was machine-checked, and against what
```

The Chapter 2 definition and participation modules are **freestanding**: they define terms
and attribution rules that the Code's own offence sections rely on, but no offence module
imports them, and `agent-compliance.l4` does not call them. They are directly callable by an
agent through their `@export` entry points. `chapter-2-explanations.l4` (dishonestly,
fraudulently) is imported by the offence modules that use those terms, and
`chapter-3-punishments.l4` is imported since 15 Sep by every module that computes a
punishment section. Wiring the definitions into the offence tests is the next piece of work,
not something this draft claims to have done.

## 2. What is deliberately not encoded

The Code lists 600 sections, of which 75 are repealed. This draft encodes **all 525 live
sections**. `registers/coverage-register.md` records which module carries each, chapter by
chapter and section by section; `registers/missing-sections.md` is kept, and is empty.

**Every live section has a rule.** Until 16 Sep 2026 seven did not -- ss 1, 7, 8, 9, 49, 50
and 79A, the short title, four drafting conventions, the definition of "section", and the
s 79A closure rule -- on the view that none states a factual test. That view was given up
on 16 Sep, and §3 records what each now decides; `coverage-register.md` §3 records how much
of it is substance, which for five of the seven is little. What remains deliberately absent
is not a section but a way of using one:

- **The s 499 exceptions** are a single caller-asserted flag `a section 499 exception applies`, not ten tests.
- **s 377BN(6)**, the marriage defence to the child abuse material offences, is **not encoded**. Its conditions turn on who is depicted in the material and who consented to what, which the `Sexual Image` record does not carry. `registers/verification-register-pass-4.md` records the gap rather than leaving it silent.
- **Punishment is not computed for any offence by the offence wrappers.** Since 15 Sep 2026 every standalone punishment section has a rule (`punishment-provisions.l4`, and the chapter modules for ss 109 to 120, 130E, 143, 147, 193, 267B and 290), each returning a Chapter 3 `Punishment` -- the ceiling, and where the Code fixes one the floor, that the section makes available. That reverses the policy under which the passes of 11 to 14 Sep left ss 302, 379, 465 and the rest out. What has not changed: no `the proposed act constitutes ...` wrapper returns a punishment, the screen carries none, the enhanced-penalty sections still take the base maximum as an argument, and nothing here is a sentence. An agent that wants the prescribed punishment for theft calls `the punishment for theft`; the screen will not volunteer it.
- **The internal punishment splits of offence sections** -- s 153's "if rioting is committed", s 173's "in the case of an individual", s 201's three gravity tiers, s 292(1A)'s "10 or more individuals" and their like -- are carried as facts on the record and not decided, as they were in Chapters 16 to 18. A section whose whole content is a punishment is computed; a punishment clause inside an offence section is not.
- **ss 32 to 38** are encoded as standalone attribution tests. They are not applied automatically to the offence wrappers: an agent that wants s 34 common-intention liability must call `the person is liable under section 34 as if he did the act alone` itself.
- **The defined terms** in `chapter-2-definitions.l4` (ss 11, 19, 21, 22, 29, 30, 40, 43, 44, 51 and the rest) are likewise callable but not spliced into the offence tests, which continue to take the underlying facts as booleans asserted by the caller. "Public servant" (s 21) is the clearest case: Chapters 9, 10 and 11 carry `is a public servant` as a fact on their own records, as the `Actor` record does, and neither is derived from s 21.
- **The ss 372 and 373 presumptions** are not encoded (pass 4); the s 286 presumption is (pass 7, §N27). The inconsistency is recorded there.
- **s 97(a)'s "offence affecting the human body"** is still caller-asserted, for the two-actor reason `verification-register-pass-4.md` §T3 gives.
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

### Added 12 Sep 2026 -- Chapter 17

- **s 390 gives robbery two separate tests, and the encoding keeps them separate.** "In all robbery there is either theft or extortion." s 390(2) makes theft robbery where harm or fear of instant harm is caused *for that end*; s 390(3) makes extortion robbery only where the offender is **present**, the fear is of **instant** harm, and delivery is **then and there**. Illustration (d) is the case that fails all three: a threat to kill a child held elsewhere by the offender's gang is extortion and is not robbery.
- **s 383 extortion turns on inducement, not on the legality of the threat.** "whether such harm is to be caused legally or illegally" -- so threatening to do something one is entitled to do is extortion if it dishonestly induces the delivery. Illustration (c), a threat to report a real offence, is extortion.
- **ss 385, 387 and 389 need no delivery.** They punish putting or attempting to put a person in fear *in order to* commit extortion, so they do not build on s 383. s 388 has a limb s 389 lacks -- fear of an accusation of having attempted to induce another to commit an offence -- and it is encoded on s 388 only.
- **s 391 gang-robbery does not require a completed robbery.** It reaches those who "commit **or attempt to commit**" a robbery, and counts those "present and aiding" towards the five. So the rule disjoins robbery with the attempt rather than conjoining robbery.
- **ss 394, 397 and 460 reach persons jointly concerned.** Each extends to "any other person jointly concerned", which is an alternative route into the section, not a further requirement on the person who did the act.
- **s 410's cessation clause is a negated conjunct.** Property "ceases to be stolen property" once a person legally entitled to it has possession. s 410(2) runs the other way and is disjoined: anything into or for which stolen property has been converted or exchanged is itself stolen property.
- **ss 411 to 414 are wider than s 410 and do not conjoin it.** Their knowledge element reaches "stolen property **or property obtained in whole or in part through an offence involving fraud or dishonesty**", so a person may be guilty under s 411 in respect of property that is not stolen property at all.
- **The reasonable-excuse defence is given to ss 411 and 412 only.** ss 413 and 414 have no such defence and the encoding does not extend it to them -- the same section-by-section discipline the Chapter 16 image defences needed.
- **s 410's Explanation removes a burden rather than adding an element.** The prosecution need not prove the elements of the offence that made the property stolen, so the underlying offence is a caller-asserted fact and is not computed from the theft, extortion or cheating rules.
- **s 439 requires no mischief.** It stands on its own conduct and intent -- intentionally running a vessel aground intending theft of what is in it -- and so does not build on s 425, unlike every other section in that group.
- **s 438 carries its own attempt.** "commits **or attempts to commit** by fire or any explosive substance such mischief as is described in section 437", so no separate s 511 analysis is needed for it.
- **s 453 requires no trespass.** Being found armed, disguised or equipped is complete in itself, which is why it is not built on s 441 or s 442.
- **s 442 closes the Chapter 4A dependency.** `registers/verification-register-pass-4.md` §T2 recorded that s 104(5) continues the right of private defence of property against house-breaking, which was defined nowhere in this encoding. It is s 442, and it is now here.

### Added 14 Sep 2026 -- Chapter 18

- **ss 466 to 469 are s 463 forgery plus one thing.** Each opens "whoever forges" or "whoever commits forgery", so each conjoins `constitutes forgery` (s 463 on s 464) with either a description of the document (ss 466, 467) or a purpose of the forger (ss 468, 469). The fault is s 464's, inherited, and is not re-tested.
- **s 470 is a designation and is caller-asserted.** Whether a document was made by forgery is a fact about the maker, who is usually not the accused. ss 471 and 474 turn on it, and so do ss 489B, 489C, 489H and 489I on their counterfeit or altered currency; none is computed from the maker's rule, for the reason s 410 gave in Chapter 17.
- **s 474 takes both the s 466 and the s 467 description as elements, disjoined.** The section applies only "if the document or electronic record is one of the descriptions mentioned in section 466" or "in section 467"; which of the two governs is punishment only. The two description facts are the ones ss 466 and 467 use, shared rather than re-declared.
- **s 474's "fraudulently or dishonestly" is inside the intention, not in `Fault`.** It qualifies the intended future use of the document, not the act of possessing it. s 471, by contrast, makes the *use* fraudulent or dishonest, and takes s 24 or s 25 from the `Fault` record. s 477A's "with intent to defraud" is not the s 25 term at all -- s 25 requires an intended advantage or detriment -- and stays inside each conduct fact.
- **s 477 has three routes to fault, and the third needs no s 24 or s 25.** "fraudulently or dishonestly, or with intent to cause damage or injury to the public or to any person" -- the first two come from `Fault`, the third is a fact on the record. Its conduct fact carries the attempts and the mischief limb, so no s 511 analysis is needed.
- **s 473C(2)'s disregard reaches the s 473C(4) machine case.** s 473C(1) is "subject to subsections (2) and (4)", but (2) is expressed "for the purpose of this section", and (4) is in the section. So the disregard -- an act the person has an enforceable duty to do, or an omission of an act he is not entitled to do -- is a negated conjunct over the whole disjunction, the six results and the machine case alike. s 473C(3)'s extension of "induce a person" to inducing a machine is written into the s 473B(b)(i) fact; s 473C(5)'s wider "loss" into the (a) fact.
- **s 473A and s 473B are not a pair.** s 473A is complete on knowledge that the equipment is designed or adapted for making a *false* instrument, with no further intent. s 473B drops that knowledge -- the equipment need only be for making *any* instrument -- and substitutes the two-part intent plus prejudice. A fixture that satisfies one fails the other.
- **ss 475 and 476 split on one fact and cannot both fire.** s 475 is the mark that authenticates a document described in s 467; s 476 is every other document or electronic record, encoded as the negation of that fact. ss 472 and 473 split the same way on which forgery the seal is for.
- **A coin is currency, but the encoding does not derive it.** s 489A(2)'s "currency" *includes* any coin which is legal tender; "coin" is metal stamped and issued by a government, legal tender or not. They are different sets, so both are caller-asserted. s 489F tests the coin fact; ss 489G to 489I test the currency fact; a caller with a legal-tender coin under the latter must assert the currency fact.
- **s 489H asks whether an *operation* was performed; s 489I whether an *offence* was committed.** The first is satisfied by an innocent alteration, the second is not. Two facts, not merged.
- **s 489E conjoins s 107 but not s 108**, as s 111 does: the section supplies the criminality of the thing abetted itself, so the abetment need not pass the capable-person test.

### Added 15 Sep 2026 -- Chapters 6 to 15, the rest of Chapter 5, and the punishment sections

- **The abetments inside Chapters 6 and 7 are facts, not the s 107 record.** ss 121, 121C, 125, 131 to 135 and 138 each name what is abetted and make the abetment a principal offence; they are encoded as one fact each, the way ss 111 and 489E were built on s 107 without s 108, but a step further -- the section supplies the whole of the criminality, so nothing of Chapter 5 is conjoined.
- **Chapter 7's s 140B is one rule.** Every Chapter 7 section but s 140 names "an officer or any serviceman in the Singapore Armed Forces or any visiting forces lawfully present in Singapore", and s 140B extends the Chapter to the police. `the person concerned is within Chapter 7` is that disjunction, conjoined by each section.
- **s 139 bites in the wrapper.** The saving says a person subject to service discipline law is not *punishable* under the Code, not that the act is no offence. The section tests ignore it; the Chapter 7 wrapper conjoins its negation.
- **s 154 is read as written**, with its three omissions -- no notice to the police, no prevention, no suppression -- conjoined. The distributive reading, on which any one omission suffices, is the alternative, and `verification-register-pass-7.md` §N23 records both.
- **s 149 builds on s 142, not s 141.** "Member" is defined, and constructive guilt for an offence committed in prosecution of the common object attaches to members in that sense.
- **s 151 is not narrowed by its Explanation.** The Explanation routes a s 141 case to s 145's punishment; it does not remove it from s 151's words. A s 145 case satisfies both.
- **"Harbour" is a rule three times over.** ss 130A, 140A and 216B define it identically for Chapter 6, Chapter 7 and ss 212, 216 and 216A; each is a rule disjoining the harbouring fact with the supply-of-shelter fact, so the definition reaches every limb that uses the word -- and does not reach s 157, which no definition names.
- **The ss 261 to 263 and ss 206 to 210 "fraudulently" is s 25.** Both groups take `the act is done fraudulently` from the `Fault` record, as ss 471 and 489F do. ss 261 to 263 disjoin it with "with intent to cause loss to the Government", which is a fact on the stamp record. s 477A's "with intent to defraud" remains the one place the word stays inside the fact.
- **s 255(2)'s stamp certificate reaches ss 255 to 262 and not s 263**, so the revenue stamp and the certificate are two facts, gathered by one rule for the eight sections and tested singly by the ninth.
- **s 286 is encoded as a route into s 285.** The presumption -- a cigarette dropped where a fire occurs within 60 minutes -- stands in for the contribution element until the contrary is proved, which is a negated conjunct. Pass 4 left the ss 372 and 373 presumptions out; §N27 of pass 7 records why this one is in and does not claim the two are consistent.
- **ss 284 to 289 share one ladder of consequences.** Each section disjoins the rungs it lists, so the shared facts do not widen any section: s 288 has two rungs, s 289 has "likely to cause grievous hurt", s 285 alone has property damage.
- **s 292(3) reaches s 293; the s 292 Exception does not.** The authorised-dealing deeming is conjoined, negated, wherever the s 292(2) object is used; the religious Exception only on ss 292, 292(1C) and 292B.
- **s 225A's fault is taken from its punishment paragraphs.** The offence clause has no fault word; paragraphs (a) and (b) punish the intentional and the negligent omission. An omission that is neither is outside both, so `intentionally or negligently omits` is conjoined as an element.
- **s 4A is now decided twice.** `chapter-1-preliminary.l4` still takes the Chapter 6 / Chapter 6B classification as a caller-asserted fact. `agent-compliance.l4` adds a second route from the encoded tests -- `a Chapter 6 offence is made out` or `constitutes genocide` -- and the reach rule disjoins them.
- **The Schedule to s 4B is complete but for item 15.** Items 1 and 2 (ss 268A to 268C) were the last specified offences the classifier could not compute; `the proposed act constitutes a hoax of a harmful thing` closes them.
- **The punishment sections are computed, and the policy is recorded in §2.** Three carry a test: s 302 on the s 300(a) fact already on the `Homicide` record, s 304 on the two s 299 intention facts, s 512 on whether the offence attempted carries death or life and whether express provision is made. s 116(2) and s 512(3), under which a minimum sentence does not bind the abettor or attempter, are one transformation, `with no minimum sentence`; s 458A's added caning is another; ss 119 and 120's fractions of the longest term, with the offence's own fine, a third.
- **s 379A(2), disqualification from driving, is not carried.** It is an order the court makes on conviction, not a punishment within s 53.

### Added 16 Sep 2026 -- the last seven sections

- **s 79A is decided the way s 5 is, and for the same reason.** Both are closure provisions that add no limb to any offence test, and until 16 Sep the first was decided and the second was not. The asymmetry is gone: `a mistake of law or ignorance of the law is a defence to the charge` is TRUE only where written law provides that it is, which is s 79A(1) read as the question an agent asks; and `the prosecution must prove the fault element notwithstanding the alleged mistake of law` is s 79A(2), TRUE where the alleged mistake may negate the fault element. Neither is a limb of `a general exception applies`, and neither feeds the wrappers: a TRUE from the first is another written law's defence, reported by the screen beside s 5, while the theft, or whatever the offence is, stays indicated. The fixtures `taking a knife in ignorance of the law` and `taking a knife under a mistake of law that written law excuses` are the two halves of that.
- **s 79A(2) is decided; ss 79(2) and 80(2) still are not.** All three are burden rules of the same shape. s 79A(2) is decided because it is the one thing the s 79A(1) FALSE needs said beside it, and because s 79A has no exception limb of its own to carry its coverage. ss 79(2) and 80(2) sit beside decided exceptions and add nothing to them. That is a reason, not a principle; `verification-register-pass-8.md` §N32 records it so a later pass can make the three consistent either way.
- **s 49 is an arithmetic rule, not a calendar.** `the period in calendar months of` years months is 12 × years + months, which is what Gregorian reckoning says a period stated in years and months amounts to, and is the conversion between the `Punishment` record's years and s 40(3)'s months. No date is carried anywhere in this subject, so no day is counted and no particular month's length is computed. A caller who needs the day on which a term ends is outside this encoding.
- **ss 8 and 10 are one rule.** Separately, each is a definition; together they decide something: "he" reaches a person of either sex, "man" and "woman" one each. s 375 -- rape by "any man" -- is the section that turns on it. `the word reaches a person of that sex` is total over `Sex` for the pronoun, which is exactly what s 8 provides and is why the rule is not vacuous.
- **s 7 is the within-Code half of s 6A.** s 6A already had a rule carrying the ss 22A to 26H explanations out to other written laws, with the s 24 and s 25 carve-outs. s 7 says that within the Code every explanation governs every use. The two are disjoined into `the Code explanation governs the expression as used`. The s 6A record's `the offence is in this Code` is read as "the use is a use in this Code", and one field was added to it for whether the expression is explained anywhere in the Code, since s 7 is not confined to ss 22A to 26H.
- **s 9 is two rules.** The singular reaching the plural and the plural reaching the singular are stated separately, each with "unless the contrary appears from the context" as a negated conjunct, so that "5 or more persons" in s 141 -- plural, context contrary -- does not reach one person, and "any person" in s 415 reaches several.
- **ss 1 and 50 are nominal, and are named as such.** s 1 is a string constant and an equality test on a citation; s 50 is the facts-record-and-predicate shape of ss 48 and 51. They are decided so that the count of 525 is a count of rules and not of `§§` headings, and nothing more is claimed for them.
- **The screen has a 115th field.** `a mistake of law is a defence s 79A` sits beside `another written law may still apply s 5`, and is computed from the `Exception Facts` record's three new s 79A facts. No existing fixture had to change but `blank exception facts`, which gained the three as FALSE.

## 4. Status

`draft`. No claim of fidelity. No HG1/HG2 grant.

Machine-checked: 45 modules, 0 type errors. `report/machine-evaluation.md` §14 is the run
of 16 Sep 2026, and it is not a clean bill: 108 of 108 assertions evaluated are
satisfied, including all 40 added on 16 Sep, but the 535
assertions of `agent-cases.l4` as it stood on 15 Sep **have not been evaluated on the
45-module tree** -- the `l4` CLI's evaluation cost grows with the import graph to the point
where a 42-module graph does not finish in an hour, and the 15 Sep pass cited a §14 for a
run it never recorded. §7.2 of that report records two blind spots in the earlier engine,
and §14.4 says what the fixtures are and are not evidence of until either the CLI or the
screen's import graph is changed.

Every encoded rule has been read back against the deposited source text, in eight passes:
`registers/verification-register.md` for the rules that existed before 09 Sep 2026 (twelve
defects, all fixed), `registers/verification-register-pass-2.md` for the rules added that day
(four defects, all fixed), `registers/verification-register-pass-3.md` for the eighteen
sections added on 11 Sep (no defect found; three drafting traps and two caller traps
recorded), `registers/verification-register-pass-4.md` for the 111 Chapter 16 sections
added the same day (no defect found; nine drafting traps and two structural limits recorded),
`registers/verification-register-pass-5.md` for the 52 Chapter 17 sections added on
12 Sep (no defect found; five drafting traps and one limit of the toolchain),
`registers/verification-register-pass-6.md` for the 25 Chapter 18 sections added on 14 Sep
(no defect found; five drafting traps and one observation on the toolchain), and
`registers/verification-register-pass-7.md` for the 204 sections added on 15 Sep (five
defects found in read-back and fixed before the machine check; nine drafting traps, one
policy change and one observation on the toolchain recorded), and
`registers/verification-register-pass-8.md` for the seven sections added on 16 Sep (no
defect found; one policy change and one drafting note recorded).
No pass is an adversarial review. Passes 3 to 8 read back rules written the same day, which
is a weaker check than passes 1 and 2 -- each says so on its own first page, and pass 7,
which read back 204 sections in one day, says so most loudly.
