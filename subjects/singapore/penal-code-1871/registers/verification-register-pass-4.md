# Penal Code 1871 — verification register, pass 4

**Run date:** 2026-09-11
**Scope:** the 74 Chapter 16 sections added on 11 Sep 2026 — the offences affecting life
(ss 299 to 310), causing miscarriage and injuries to unborn children (ss 312 to 318), hurt
(ss 319 to 338), wrongful restraint, wrongful confinement, criminal force and assault
(ss 339 to 358), and kidnapping, abduction, slavery and forced labour (ss 359 to 374). Six of
the Chapter's seven groups; only the sexual offences (ss 375 to 377D) are outstanding.
**Method:** every rule read back against the deposited source text in
`registers/source-bundle/PC1871.txt`, clause by clause, after it was written and
machine-checked. Same method as passes 1 to 3. Not an adversarial review.

**Result: no defect found in read-back. 6 traps in the Act's drafting recorded; 1 structural
limit of this subject recorded.**

---

## 1. What this pass covers, and the limit of it

The same limit as pass 3, and it bears repeating because this pass is six times the size:
these rules were read back on the day they were written, so **a misreading shared by the
rule and the read-back is invisible here**. No count below is evidence against that.

What partly compensates is that Chapter 16 is unusually rich in Illustrations, and they are
worked examples with stated outcomes rather than commentary. Every Illustration that states
an outcome was turned into an assertion in `agent-cases.l4` rather than into prose here, so
the engine checks the reading and a later reader can re-run it. The ones that carry the most
weight:

| Illustration | what it tests | fixture |
| --- | --- | --- |
| s 299 Expl 3 | the child in the womb is not homicide; the child partly brought forth may be | `a death in the womb`, `a death of a child partly brought forth` |
| s 300 Exc 1 Ill (c) | provocation by a lawful arrest does not reduce murder | `a killing on provocation given by a lawful arrest` |
| s 300 Exc 5 Ill | the survivor of a suicide pact commits culpable homicide, not murder | `a suicide pact death by consent` |
| s 316 Ill | an act that would be culpable homicide, killing the unborn child instead | `a quick unborn child killed` |
| s 322 Ill | grievous hurt of one kind intended, of another caused, is still s 322 | `a blow intended to disfigure that breaks a bone` |
| s 323A Ill | minor hurt intended, grievous hurt caused, is not s 322 | `a punch that unexpectedly paralyses` |
| s 330 Ill (a) | torture to extract a confession | `torture to extract a confession` |
| s 339 Exc | the private way believed in good faith to be obstructible | `blocking a private way in good faith` |
| s 340 Ill (a) | restraint within circumscribing limits is confinement | `locking a person in a room` |
| s 350 Ill (d) | a push in the street, without consent, intending annoyance | `pushing someone in the street` |
| s 351 Ill (a) and Expl | a shaken fist is assault; words alone are not | `shaking a fist`, `a threat in words alone` |
| s 361 Exc | the father in good faith, and the same belief defeated by an unlawful purpose | `a father taking his own child in good faith`, `... for an unlawful purpose` |

## 2. Six traps in the drafting

Each is recorded in the module as well as here.

### N4 — s 300's Exceptions subtract, they do not add

s 300 opens "Except in the cases hereinafter excepted culpable homicide is murder". Read as a
list of ways to be guilty, the seven Exceptions would each *make* a killing murder. They do
the opposite: each returns the case to culpable homicide not amounting to murder. So
`constitutes murder` conjoins s 299 and a s 300 limb with the **negation** of the Exception
aggregate, and the two provocation fixtures — one within Exception 1, one caught by its
proviso (b) — are the regression test.

### N5 — s 299 Explanations 1 and 2 supply causation, so they disjoin

Both Explanations deem a death to have been caused where causation might otherwise be
denied: accelerating the death of a person already diseased, and inflicting an injury from
which proper treatment might have saved the victim. Conjoined, they would have made every
culpable homicide require a diseased victim and inadequate treatment. They are disjoined with
the plain "causes death by doing an act".

Explanation 3 runs the other way and is a conjunct: it *excludes* the child in the womb,
unless some part of the child has been brought forth.

### N6 — s 320 needs s 319, and s 349's proviso is a requirement

Two places where a section that reads like a bare list is not one.

s 320 says "The following kinds of hurt **only** are designated as grievous". It is a closed
list of kinds of *hurt*, so grievous hurt requires s 319 hurt as well as one of the ten
limbs. Limb (aa) is why this matters: death is grievous hurt for Chapter 16 purposes, and a
rule that did not conjoin s 319 would report grievous hurt from the death fact alone.

s 349 defines force, then adds "Provided that the person causing the motion … causes that
motion … in one of the following 3 ways". The proviso is a requirement, not a gloss: force is
used only if the motion was caused by the actor's own bodily power, by disposing a substance,
or by inducing an animal. The rule conjoins the two effects with the three ways.

### N7 — s 304C(3) defends only one of the two alternatives

s 304C(1)(d) is a true alternative: either the accused's own act caused the death, or he was
aware of the risk, failed to protect, and the act occurred in circumstances he foresaw.
s 304C(3) provides that he is not guilty if he could not have been expected to take any such
step. Applied to the whole section, that would exculpate an accused whose own act caused the
death on the ground that he could not have protected the victim from himself. It is encoded
as a negated conjunct inside the failure-to-protect branch only.

### N8 — three openings that look like elements and are not

Three provisions in the second part of this pass each read like a further element and are
something else.

**s 315(2)** — "evidence that a woman had at any material time been pregnant for a period of
28 weeks or more shall be **prima facie evidence** that she was at that time pregnant of a
child capable of being born alive". That tells a court what may be presumed, not what must be
proved. Conjoined, it would have made child destruction impossible to establish before 28
weeks, which is the opposite of what the subsection does. The fact is carried, unconjoined.

**ss 372 and 373** each carry a presumption in the same shape — that one who disposes of, or
obtains possession of, a female below 21 to or from a prostitute or brothel-keeper is
presumed until the contrary is proved to have done so for prostitution. Rebuttable
presumptions of fact, not elements; not encoded.

**s 314's Explanation** — "It is not essential to this offence that the offender should know
that the act is likely to cause death." It *removes* a fault element. Nothing is conjoined
for it; the section is complete on the intent to cause miscarriage plus the death.

### N9 — the section 361 Exception is defeated, not merely qualified

s 361 "does not extend to the act of any person who in good faith believes himself to be the
father of an illegitimate child or who in good faith believes himself to be entitled to the
lawful custody of such child, **unless** such act is committed for an immoral or unlawful
purpose."

The "unless" restores the section. Encoded as a bare good-faith carve-out, a father who took
his child for an unlawful purpose would escape. The Exception is therefore encoded as a
protection that the immoral-or-unlawful purpose removes, and both cases are asserted.

## 3. A structural limit, recorded rather than fixed

### T3 — "an offence affecting the human body" is still asserted, not computed

s 97(a) gives a right of private defence of the body "against any offence affecting the human
body". Chapter 16 is the chapter of those offences, and this pass encodes 74 of them. It is
therefore tempting to wire `an encoded hurt offence is made out` into
`there is a section 97(a) right to defend the body` and have the right computed.

It is not wired in, for two reasons.

**The facts belong to the wrong person.** The offence affecting the human body is the
*assailant's*, and the `Proposed Act` bundle carries one actor's facts. Feeding the defender's
own `Bodily Harm` record into the s 97(a) test would ask whether the defender committed an
offence, which is the opposite question.

**The chapter is not complete.** One of Chapter 16's seven groups is still absent -- the
sexual offences -- so a FALSE from the hurt predicate is not a statement that no offence
affecting the human body is in play. Wiring it in would make the private-defence right look computed when it is not — which
is the failure mode `coverage-register.md` §6.1 was written about.

`an encoded hurt offence is made out` is exported so a caller who *does* hold the assailant's
facts can use it. Closing this properly needs a two-actor bundle, which is a change to the
shape of the subject and not a defect in these rules.

## 4. Clause-by-clause read-back

"As written" means the rule's limbs correspond one to one with the provision's, in the same
polarity.

### Offences affecting life

| s | provision | reading |
| --- | --- | --- |
| 299 | culpable homicide | Three fault limbs disjoined, conjoined with causation. Expl 1 and 2 disjoin into causation (N5); Expl 3 is a negated conjunct. |
| 300(a)–(d) | when culpable homicide is murder | All four limbs present, disjoined, each as written. |
| 300 Exc 1 | grave and sudden provocation | The deprivation fact and Explanation 1's ordinary-person test are conjuncts; the three provisos are negated conjuncts. Explanation 2 (words, gestures or conduct) widens what may be asserted and adds no limb. |
| 300 Exc 2 | exceeding private defence | All three conjuncts as written. The Explanation's definition of "premeditation" is carried as one fact. |
| 300 Exc 3 | public servant exceeding his powers | As written, three conjuncts. |
| 300 Exc 4 | sudden fight | Two conjuncts plus the negated proviso. Its four Explanations bear on what may be asserted — which party struck first is immaterial, a "fight" includes unlanded and single blows, a "quarrel" needs no words — and add no limb. |
| 300 Exc 5 | consent of a person above 18 | As written. |
| 300 Exc 6 | woman, child below 12 months | Both conjuncts as written. Shares the balance-of-mind fact with s 310. |
| 300 Exc 7 | abnormality of mind | Three impairment limbs disjoined; the middle one carries the two-limb wrongness test the Exception attaches to it, as s 84(2) does for s 84(1)(b). |
| 301(1) | death of a person other than the one intended | Reports that the transfer is engaged; what it transfers into is decided by `constitutes murder` on the same facts. |
| 304A | rash or negligent act | As written, conjoined with the negation of culpable homicide, which the section states in terms. |
| 304B | sustained abuse | Relevant person, victim status, causation, and the s 304B(2) definition of sustained abuse as 2+ occasions or one protracted occasion. |
| 304C(1) | causing or allowing a household death | Four conjuncts plus the (d) alternative. s 304C(2) is a rule about proof and adds no limb; s 304C(3) is N7. |
| 305, 306 | abetment of suicide | s 306 is the base; s 305 adds the victim's status and the abettor's knowledge. s 305(1)(a)–(c) differ only in punishment; the distinguishing facts are carried, no term computed. |
| 307, 308 | attempt to murder, attempt to commit culpable homicide | Both complete without a death, as the Illustrations require. Hurt raises the punishment only; the fact is carried. |
| 308A(1) | death in furtherance of a group's object | (a) and (c) conjoined, (b)(i) and (b)(ii) disjoined. "Group" comes from the Organised Crime Act 2015, not in the source bundle, so membership is asserted. |
| 308B(1) | concealment or disposal of a corpse | Conduct conjoined with the disjunction of the two impediments. |
| 310 | infanticide | As written. Shares the balance-of-mind fact with Exc 6 but not the conduct fact — "voluntarily causes" there, "by any intentional act or omission" here. |

### Unborn children and infants

| s | provision | reading |
| --- | --- | --- |
| 312 | causing miscarriage | Conduct disjoined with the Explanation's self-induced case, conjoined with the negation of the Termination of Pregnancy Act 1974 carve-out. The 16-week duration is punishment only. |
| 313 | without the woman's consent | s 312 plus the absence of consent. The duration is expressly immaterial to this section and is not conjoined. |
| 314 | death caused by an act done with intent to cause miscarriage | As written. Its Explanation removes a fault element (N8). |
| 315(1) | child destruction | Intent, the two causing limbs disjoined, and the section's own saving for the mother's life as a negated conjunct. s 315(2) is evidence, not an element (N8). |
| 316 | death of a quick unborn child | Both conjuncts as written. The culpable-homicide circumstance is carried rather than computed — no death of a *person* has occurred to test s 299 against. |
| 317 | exposure and abandonment | Three conjuncts as written. Its Explanation preserves a murder or culpable homicide charge and adds no limb. |
| 318 | concealment of a birth | Both conjuncts. "or endeavours to conceal" makes the offence complete on the attempt. |

### Kidnapping, abduction, slavery and forced labour

| s | provision | reading |
| --- | --- | --- |
| 359 | kidnapping is of 2 kinds | No test of its own; `the person kidnaps` is the disjunction of ss 360 and 361. |
| 360 | kidnapping from Singapore | Both conjuncts as written. |
| 361 | kidnapping from lawful guardianship | Two conjuncts plus the negated Exception (N9). Its Explanation widens "lawful guardian" and adds no limb. |
| 362 | abduction | As written. Not a kind of kidnapping: no minority, no guardian, no border. |
| 364–367 | kidnapping or abducting for a purpose | Common "kidnaps or abducts" opening gathered once; each section adds its own purpose or knowledge. s 366 additionally requires the person to be a woman. |
| 368 | concealing or confining a kidnapped person | Does **not** conjoin the kidnapping — it attaches to one committed by another, and knowledge of it is the element. Its "punished in the same manner as if he had kidnapped" is a punishment direction. |
| 370, 371 | slavery | s 370's two limbs disjoined; only the second carries "against his will". s 371 differs from s 370 only by "habitually". |
| 372, 373 | selling and buying a minor for prostitution | The sale and purchase sides of one transaction, sharing the age element and the purpose-or-knowledge disjunction. Their presumptions are not encoded (N8). |
| 373A | importing a woman for prostitution | Three limbs disjoined. No age element. |
| 374 | unlawful compulsory labour | As written. |

### Hurt

| s | provision | reading |
| --- | --- | --- |
| 319 | hurt | Four disjuncts — the three in the section plus the Explanation's unconsciousness. |
| 320 | grievous hurt | Closed list of ten, conjoined with s 319 (N6). |
| 321 | voluntarily causing hurt | Fault disjunction conjoined with hurt in fact. |
| 322 | voluntarily causing grievous hurt | s 321, plus gravity of the hurt intended, plus grievous hurt caused. The Explanation's second half is why the kinds need not match. |
| 323A | hurt intended, grievous hurt caused | s 321, the negation of the gravity fact, and grievous hurt caused. |
| 324, 326 | dangerous weapons or means | Identical seven-item list in both, shared. The "except in the case provided for by s 334/335" openings allocate punishment and are not elements. |
| 327, 329 | extorting property, constraining to an illegal act | Shared two-purpose disjunction. |
| 328 | poison with intent | Administering conjoined with a three-way fault disjunction. No hurt in fact required — the only such section in the group besides ss 335B and 336. |
| 330, 331 | extorting a confession, compelling restoration | Shared two-purpose disjunction. |
| 332, 333 | deterring a public servant | Shared three-limb disjunction. The s 332 proviso on imprisonment is a sentencing direction and is not encoded. |
| 334, 334A, 335 | provocation | Each is the underlying offence plus the provocation limbs. Note s 335's confinement limb is about grievous hurt where ss 334 and 334A are about hurt. The Explanation subjects all three to Exc 1 to s 300; those provisos live in the life module and are not restated. |
| 335A(1),(2) | allowing neglect or abuse | Common paragraphs conjoined; (c) differs by victim type and is the disjunction. s 335A(3) is one asserted fact; s 335A(4) widens what a court may consider and adds no limb. |
| 335B, 336, 337, 338 | endangering life or personal safety | s 335B on knowledge or belief; ss 336 to 338 on the shared rash-or-negligent disjunction, with hurt and grievous hurt added for ss 337 and 338. |

### Restraint, force and assault

| s | provision | reading |
| --- | --- | --- |
| 339 | wrongful restraint | Conduct conjoined with the negation of the section's own private-way Exception. |
| 340 | wrongful confinement | s 339 conjoined with the circumscribing-limits fact. |
| 345–348 | aggravated confinement | Each is s 340 plus its own circumstance or purpose. ss 347 and 348 do not share facts with ss 327 and 330 — the wording differs. |
| 349 | force | Two effects disjoined, conjoined with the three ways of the proviso (N6). No fault element. |
| 350 | criminal force | s 349, intentional use, absence of consent, and a three-way purpose disjunction. |
| 351 | assault | Gesture or preparation, the apprehension fault, and the negation of the words-alone case. Needs no force and no contact. |
| 352, 358 | provocation | Complementary. The s 352 Explanation's three cases are encoded as disqualifiers of the provocation, shared with s 355 which adopts the same Explanation. |
| 353 | deterring a public servant | Three limbs as written. Unlike ss 332 and 333, s 353 does not extend the deterrence limb to "any other public servant" — encoded as it stands. |
| 354, 354A | outraging modesty | s 354(1) as written; s 354(2)'s age fact is punishment and is carried, not an element. s 354A(1) does not require the s 354 offence to be committed, only the purpose; s 354A(2)'s lift and age facts are punishment. |
| 355, 356, 357 | dishonour, theft from the person, attempted confinement | Each is the common assault-or-criminal-force opening plus its own circumstance. s 357 needs only the attempt at confinement, not a completed s 340. |

## 5. Machine check

23 modules, **0 type errors, 154 of 154 assertions satisfied** — 88 pre-existing and 66 added
by this pass. `report/machine-evaluation.md` §7.2 records two blind spots in the available
engine that the run does not cover; the fixture-completeness check described there was run on
every fixture in this pass and passes.

A third trap, in the coverage tooling rather than the engine, surfaced during this pass and is
recorded in `missing-sections.md` §4: a citation of the form `s 300 Exception 1` reads as
section 1 unless "Exception N" is stripped, exactly as "Explanation N" must be. It inflated
Chapter 1 and Chapter 2 by one section each before it was caught.
