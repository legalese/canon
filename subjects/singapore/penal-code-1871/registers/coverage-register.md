# Penal Code 1871 — coverage register

**Run date:** 2026-09-11 (Chapter 16 pass; first run 2026-09-09)
**Question answered:** which sections of the Act are modelled, and which are not.
**Method:** every `@ref` citation in the seventeen `.l4` modules was parsed for section
numbers and matched against the Act's own arrangement of sections, as it appears in
`registers/source-bundle/PC1871.txt` (SSO current version as at 09 Sep 2026). Multi-section
citations (`ss 45, 46, 47, 48`) and ranges (`ss 76 to 95`) are expanded; subsection numbers
in parentheses are stripped so that `s 120A(4) and (5)` does not read as sections 4 and 5.

This register is mechanical. It records that a section **is cited by the encoding**, not that
the rule is a correct or complete reading of it. Fidelity is a separate question, answered by
`registers/verification-register.md` and `registers/verification-register-pass-2.md`.

One limit of the method is worth stating, because the fidelity pass found it: a citation may
sit on a `DECLARE` rather than on a rule, in which case this register counts the section as
covered although nothing decides it. That was true of ss 45 and 46 when this register was
first generated (defect W4 in pass 2). Both now have rules, so the count below stands -- but
a future reader should treat any single-citation section as worth checking rather than as
proven.

---

## 1. Headline

| | sections |
| --- | ---: |
| listed in the Act's arrangement of sections | 600 |
| repealed — nothing to encode | 75 |
| **live** | **525** |
| **encoded** | **200** |
| **live but not encoded** | **325** |

**About 38% of the live sections.** Two passes on 11 Sep. The first added 18 — the whole of
Chapter 4A (ss 96 to 106A), ss 111, 113 and 114 of Chapter 5, and ss 3, 4A and 5 of
Chapter 1 — which were the three gaps §6 of this register called more than scope choices.
The second opened **Chapter 16**, the offences affecting the human body, and added 74: six of
its seven groups — life, hurt, restraint, force and assault, unborn children and infants, and
kidnapping, abduction, slavery and forced labour. Only the sexual offences (ss 375 to 377D)
remain, with the nine pure punishment sections the policy excludes.

There is no Chapter 19; Chapters 13 and 20 are wholly repealed.

The distribution is the point. The Code's **general parts are close to complete**, and its
**offence chapters are a deliberate thin slice** — the provisions an AI agent is most likely
to walk into when checking its own output or a user's requested act. `NOTES.md` §2 states the
policy; this register states its consequences section by section.

## 2. By chapter

| chapter | ss | repealed | live | encoded | not encoded |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Chapter 1** — PRELIMINARY | 7 | 0 | 7 | 6 | 1 |
| **Chapter 2** — GENERAL EXPLANATIONS | 56 | 2 | 54 | 49 | 5 |
| **Chapter 3** — Punishments | 13 | 3 | 10 | 10 | 0 |
| **Chapter 4** — General Exceptions | 21 | 0 | 21 | 20 | 1 |
| **Chapter 4A** — Right of private defence | 12 | 0 | 12 | 12 | 0 |
| **Chapter 5** — Abetment | 16 | 0 | 16 | 7 | 9 |
| **Chapter 5A** — Criminal Conspiracy | 2 | 0 | 2 | 2 | 0 |
| **Chapter 6** — Offences against the State | 15 | 0 | 15 | 0 | 15 |
| **Chapter 6A** — Piracy | 2 | 0 | 2 | 0 | 2 |
| **Chapter 6B** — Genocide | 2 | 0 | 2 | 0 | 2 |
| **Chapter 7** — Offences relating to the armed forces | 12 | 0 | 12 | 0 | 12 |
| **Chapter 8** — Offences relating to unlawful assembly | 21 | 3 | 18 | 0 | 18 |
| **Chapter 9** — Offences by or relating to public servants | 11 | 0 | 11 | 0 | 11 |
| **Chapter 10** — Contempts of the lawful authority of public servants | 19 | 0 | 19 | 0 | 19 |
| **Chapter 11** — False evidence and offences against public justice | 46 | 3 | 43 | 0 | 43 |
| **Chapter 12** — Offences relating to government stamps | 35 | 26 | 9 | 0 | 9 |
| **Chapter 13** — *(wholly repealed)* | 4 | 4 | 0 | 0 | 0 |
| **Chapter 14** — Offences affecting public tranquility, health, safety and decency | 35 | 0 | 35 | 0 | 35 |
| **Chapter 15** — Offences relating to race | 5 | 3 | 2 | 0 | 2 |
| **Chapter 16** — Offences affecting the human body | 126 | 6 | 120 | 74 | 46 |
| **Chapter 17** — Offences against property | 93 | 17 | 76 | 12 | 64 |
| **Chapter 18** — Offences relating to documents, electronic records and marks | 28 | 0 | 28 | 2 | 26 |
| **Chapter 20** — *(wholly repealed)* | 5 | 5 | 0 | 0 | 0 |
| **Chapter 21** — Defamation | 4 | 0 | 4 | 1 | 3 |
| **Chapter 22** — Criminal intimidation, insult and annoyance | 8 | 3 | 5 | 4 | 1 |
| **Chapter 23** — Attempts to commit offences | 2 | 0 | 2 | 1 | 1 |
| **total** | **600** | **75** | **525** | **200** | **325** |

## 3. The general parts

Six chapters decide whether an offence test is reached at all, and these are the ones the
encoding treats as load-bearing:

| chapter | live | encoded |
| --- | ---: | ---: |
| Chapter 1 — Preliminary | 7 | 6 |
| Chapter 2 — General explanations | 54 | 49 |
| Chapter 3 — Punishments | 10 | 10 |
| Chapter 4 — General exceptions | 21 | 20 |
| Chapter 4A — Right of private defence | 12 | 12 |
| Chapter 5A — Criminal conspiracy | 2 | 2 |

**The seven apparent gaps there are deliberate, and each is documented in the module itself
under its own `§§` heading.** They are sections with no factual test to decide:

| s | why nothing is decided |
| --- | --- |
| 1 | "This Act is the Penal Code 1871." A short title states no test. |
| 7 | Rule of construction addressed to the reader: an expression explained in one part is used in the same sense throughout. Honoured by the encoding's own discipline — one definition module per term, imported rather than restated. |
| 8 | "He" and its derivatives are used of any person. A drafting convention; this encoding writes gender-neutrally throughout. |
| 9 | Singular includes plural and plural singular unless the contrary appears. A drafting convention. |
| 49 | A year or month is reckoned by the Gregorian calendar. Every period in this encoding is Gregorian by construction. |
| 50 | "Section" denotes a numbered portion of a Chapter. |
| 79A | A **closure** rule, not an exception: mistake or ignorance of law is never a defence unless another written law so provides. It therefore contributes no limb to `a general exception applies`, which is the correct encoding of it. |

So Chapters 1, 2, 3, 4, 4A and 5A are complete in substance: every section that states a
testable rule has one. Note that s 5, the other Chapter 1 closure provision, **is** decided,
where s 79A is not — `NOTES.md` §3 gives the reason.

## 4. Chapters partially encoded, section by section


### Chapter 1 — PRELIMINARY

6 of 7 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 2 | Punishment of offences committed within Singapore | `chapter-1-preliminary.l4` |
| 3 | Punishment of offences committed beyond, but which by law may be tried within Singapore | `chapter-1-preliminary.l4` |
| 4 | Jurisdiction over public servants for offences committed outside Singapore | `chapter-1-preliminary.l4` |
| 4A | Offences against State and genocide committed outside Singapore by citizen or permanent resident | `chapter-1-preliminary.l4` |
| 4B | Punishment of specified offences with elements occurring in Singapore but others occurring outside Singapore | `chapter-1-preliminary.l4` |
| 5 | Certain laws not to be affected by this Code | `chapter-1-preliminary.l4` |

**Not encoded:** s 1 (short title — no test to decide).

### Chapter 2 — GENERAL EXPLANATIONS

49 of 54 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 6 | Definitions in this Code to be understood subject to exceptions | `chapter-4-exceptions.l4` |
| 6A | Definitions to apply to this Code and other written law | `chapter-2-definitions.l4` |
| 10 | "Man" and "woman" | `chapter-2-definitions.l4` |
| 11 | "Person" | `chapter-2-definitions.l4` |
| 12 | "Public" | `chapter-2-definitions.l4` |
| 17 | "Government" | `chapter-2-definitions.l4` |
| 19 | "Judge" | `chapter-2-definitions.l4` |
| 20 | "Court of justice" | `chapter-2-definitions.l4` |
| 21 | "Public servant" | `chapter-2-definitions.l4` |
| 22 | "Property" | `chapter-2-definitions.l4` |
| 22A | "Fault element" and "physical element" | `chapter-2-definitions.l4` |
| 23 | "Wrongful gain" and "wrongful loss" | `chapter-2-explanations.l4` |
| 24 | "Dishonestly" | `chapter-2-explanations.l4` |
| 25 | "Fraudulently" | `chapter-2-explanations.l4` |
| 26 | "Reason to believe" | `chapter-2-explanations.l4` |
| 26A | "Voluntarily" | `chapter-2-explanations.l4` |
| 26B | "Good faith" | `chapter-2-explanations.l4` |
| 26C | "Intentionally" | `chapter-2-explanations.l4` |
| 26D | "Knowingly" | `chapter-2-explanations.l4` |
| 26E | "Rashly" | `chapter-2-explanations.l4` |
| 26F | "Negligently" | `chapter-2-explanations.l4` |
| 26G | "Transferred fault" | `chapter-2-explanations.l4` |
| 26H | "Strict liability" | `chapter-2-explanations.l4` |
| 27 | Property in possession of spouse, clerk or servant | `chapter-2-definitions.l4` |
| 28 | "Counterfeit" | `chapter-2-definitions.l4` |
| 29 | "Document" | `chapter-2-definitions.l4` |
| 29A | "Writing" | `chapter-2-definitions.l4` |
| 29B | "Electronic record" | `chapter-2-definitions.l4` |
| 30 | "Valuable security" | `chapter-2-definitions.l4` |
| 31 | "A will" | `chapter-2-definitions.l4` |
| 31A | "Die" and "instrument" | `chapter-2-definitions.l4` |
| 32 | Words referring to acts include illegal omissions | `chapter-2-participation.l4` |
| 33 | "Act" and "omission" | `chapter-2-participation.l4` |
| 34 | Each of several persons liable for an act done by all, in like manner | `chapter-2-participation.l4` |
| 35 | When such an act is criminal by reason of its being done with a | `chapter-2-participation.l4` |
| 36 | Effect caused partly by act and partly by omission | `chapter-2-participation.l4` |
| 37 | Cooperation by doing one of several acts constituting an offence | `chapter-2-participation.l4` |
| 38 | Several persons engaged in the commission of a criminal act may | `chapter-2-participation.l4` |
| 40 | "Offence" | `chapter-2-definitions.l4` |
| 41 | Offence with specified term of imprisonment | `chapter-2-definitions.l4` |
| 42 | "Obscene" | `chapter-2-definitions.l4` |
| 43 | "Illegal", "unlawful" and "legally bound to do" | `chapter-2-definitions.l4` |
| 44 | "Injury" | `chapter-2-definitions.l4` |
| 44A | "Bodily injury" | `chapter-2-definitions.l4` |
| 45 | "Life" | `chapter-2-definitions.l4` |
| 46 | "Death" | `chapter-2-definitions.l4` |
| 47 | "Animal" | `chapter-2-definitions.l4` |
| 48 | "Vessel" | `chapter-2-definitions.l4` |
| 51 | "Oath" | `chapter-2-definitions.l4` |

**Not encoded:** s 7, s 8, s 9, s 49, s 50.

Repealed, nothing to encode: s 39, s 52.

### Chapter 3 — Punishments

10 of 10 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 53 | Punishments | `chapter-3-punishments.l4` |
| 54 | Imprisonment for life | `chapter-3-punishments.l4` |
| 72 | Punishment of a person found guilty of one of several offences, the | `chapter-3-punishments.l4` |
| 73 | Enhanced penalties for offences against domestic workers | `chapter-3-punishments.l4` |
| 74 | Enhanced penalties for racially or religiously aggravated offences | `chapter-3-punishments.l4` |
| 74A | Enhanced penalties for offences against vulnerable persons | `chapter-3-punishments.l4` |
| 74B | Enhanced penalties for offences against person below 14 years of | `chapter-3-punishments.l4` |
| 74C | Enhanced penalties for offences against victims in intimate | `chapter-3-punishments.l4` |
| 74D | Enhanced penalties for offences against victims in close | `chapter-3-punishments.l4` |
| 74E | Application of enhanced penalties | `chapter-3-punishments.l4` |

Repealed, nothing to encode: s 57, s 71, s 75.

### Chapter 4 — General Exceptions

20 of 21 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 76 | Act done by person bound, or justified by law | `chapter-4-exceptions.l4` |
| 77 | Act of judge when acting judicially | `chapter-4-exceptions.l4` |
| 78 | Act done pursuant to the judgment or order of a court of justice | `chapter-4-exceptions.l4` |
| 79 | Act done by person by mistake of fact believing himself bound or | `chapter-4-exceptions.l4` |
| 80 | Accident in the doing of a lawful act | `chapter-4-exceptions.l4` |
| 81 | Act likely to cause harm but done to prevent other harm | `chapter-4-exceptions.l4` |
| 82 | Act of a child below 10 years of age | `chapter-4-exceptions.l4` |
| 83 | Act of a child of or above 10 and below 12 years of age, who has | `chapter-4-exceptions.l4` |
| 84 | Act of person of unsound mind | `chapter-4-exceptions.l4` |
| 85 | Intoxication when a defence | `chapter-4-exceptions.l4` |
| 86 | Effect of defence of intoxication when established | `chapter-4-exceptions.l4` |
| 87 | Act not intended and not known to be likely to cause death or | `chapter-4-exceptions.l4` |
| 88 | Act not intended to cause death done by consent in good faith for | `chapter-4-exceptions.l4` |
| 89 | Act done in good faith for the benefit of a child or person of | `chapter-4-exceptions.l4` |
| 90 | Consent given under fear or misconception, by person of unsound | `chapter-4-exceptions.l4` |
| 91 | Acts which are offences independently of harm caused to the | `chapter-4-exceptions.l4` |
| 92 | Act done in good faith for the benefit of a person without consent | `chapter-4-exceptions.l4` |
| 93 | Communication made in good faith | `chapter-4-exceptions.l4` |
| 94 | Act to which a person is compelled by threats | `chapter-4-exceptions.l4` |
| 95 | Act causing slight harm | `chapter-4-exceptions.l4` |

**Not encoded:** s 79A.

### Chapter 4A — Right of private defence

12 of 12 live sections encoded — the whole Chapter.

| s | title | module |
| --- | --- | --- |
| 96 | Nothing done in private defence is an offence | `chapter-4a-private-defence.l4` |
| 97 | Right of private defence of the body and of property | `chapter-4a-private-defence.l4` |
| 98 | Extent to which right may be exercised | `chapter-4a-private-defence.l4` |
| 99 | Right of private defence against act of person of unsound mind, etc. | `chapter-4a-private-defence.l4` |
| 100 | Right of private defence against deadly assault when there is risk of harm to innocent person | `chapter-4a-private-defence.l4` |
| 101 | Start and continuance of right of private defence of body | `chapter-4a-private-defence.l4` |
| 102 | When right of private defence of body extends to causing death | `chapter-4a-private-defence.l4` |
| 103 | When such right extends to causing any harm other than death | `chapter-4a-private-defence.l4` |
| 104 | Commencement and continuance of right of private defence of property | `chapter-4a-private-defence.l4` |
| 105 | When right of private defence of property extends to causing death | `chapter-4a-private-defence.l4` |
| 106 | When such right extends to causing any harm other than death | `chapter-4a-private-defence.l4` |
| 106A | Acts against which there is no right of private defence | `chapter-4a-private-defence.l4` |

**Nothing not encoded.** The Chapter's own structure is recorded in `NOTES.md` §3 and in the
module header.

### Chapter 5 — Abetment

7 of 16 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 107 | Abetment of the doing of a thing | `chapter-5-abetment.l4` |
| 108 | Abettor | `chapter-5-abetment.l4` |
| 108A | Abetment in Singapore of an offence outside Singapore | `chapter-5-abetment.l4` |
| 108B | Abetment outside Singapore of an offence in Singapore | `chapter-5-abetment.l4` |
| 111 | Liability of abettor when one act is abetted and a different act is done | `chapter-5-abetment.l4` |
| 113 | Liability of abettor for an offence caused by the act abetted different from that intended by the abettor | `chapter-5-abetment.l4` |
| 114 | Abettor present when offence committed | `chapter-5-abetment.l4` |

**Not encoded:** s 109, s 110, s 112, s 115, s 116, s 117, s 118, s 119, s 120 — all of them
punishment or concealment provisions, consistent with this subject not computing sentence.

### Chapter 5A — Criminal Conspiracy

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 120A | Definition of criminal conspiracy | `chapter-5a-conspiracy.l4` |
| 120B | Punishment of criminal conspiracy | `chapter-5a-conspiracy.l4` |

### Chapter 16 — Offences affecting the human body

74 of 120 live sections encoded; 6 repealed and excluded.

| s | title | module |
| --- | --- | --- |
| 299 | Culpable homicide | `chapter-16-life.l4` |
| 300 | Murder | `chapter-16-life.l4` |
| 301 | Culpable homicide by causing the death of a person other than the person whose death was intended | `chapter-16-life.l4` |
| 304A | Causing death by rash or negligent act | `chapter-16-life.l4` |
| 304B | Causing death of child below 14 years of age, domestic worker or vulnerable person by sustained abuse | `chapter-16-life.l4` |
| 304C | Causing or allowing death of child below 14 years of age, domestic worker or vulnerable person in same household | `chapter-16-life.l4` |
| 305 | Abetment of suicide or attempted suicide of minor or person who lacks mental capacity | `chapter-16-life.l4` |
| 306 | Abetment of suicide or attempted suicide | `chapter-16-life.l4` |
| 307 | Attempt to murder | `chapter-16-life.l4` |
| 308 | Attempt to commit culpable homicide | `chapter-16-life.l4` |
| 308A | Causing death in furtherance of group's object | `chapter-16-life.l4` |
| 308B | Concealment, desecration or disposal of corpse that impedes discovery, identification, criminal investigations or prosecutions | `chapter-16-life.l4` |
| 310 | Infanticide | `chapter-16-life.l4` |
| 312 | Causing miscarriage | `chapter-16-unborn-and-infants.l4` |
| 313 | Causing miscarriage without woman's consent | `chapter-16-unborn-and-infants.l4` |
| 314 | Death caused by act done with intent to cause miscarriage | `chapter-16-unborn-and-infants.l4` |
| 315 | Child destruction before, at or immediately after birth | `chapter-16-unborn-and-infants.l4` |
| 316 | Causing death of a quick unborn child by an act amounting to culpable homicide | `chapter-16-unborn-and-infants.l4` |
| 317 | Exposure and abandonment of a child below 12 years of age by parent or person having care of it | `chapter-16-unborn-and-infants.l4` |
| 318 | Concealment of birth by secret disposal of dead body | `chapter-16-unborn-and-infants.l4` |
| 319 | Hurt | `chapter-16-hurt.l4` |
| 320 | Grievous hurt | `chapter-16-hurt.l4` |
| 321 | Voluntarily causing hurt | `chapter-16-hurt.l4` |
| 322 | Voluntarily causing grievous hurt | `chapter-16-hurt.l4` |
| 323A | Punishment for voluntarily causing hurt which causes grievous hurt | `chapter-16-hurt.l4` |
| 324 | Voluntarily causing hurt by dangerous weapons or means | `chapter-16-hurt.l4` |
| 326 | Voluntarily causing grievous hurt by dangerous weapons or means | `chapter-16-hurt.l4` |
| 327 | Voluntarily causing hurt to extort property or to constrain to an illegal act | `chapter-16-hurt.l4` |
| 328 | Causing hurt by means of poison, etc., with intent to commit an offence | `chapter-16-hurt.l4` |
| 329 | Voluntarily causing grievous hurt to extort property, or to constrain to an illegal act | `chapter-16-hurt.l4` |
| 330 | Voluntarily causing hurt to extort confession or to compel restoration of property | `chapter-16-hurt.l4` |
| 331 | Voluntarily causing grievous hurt to extort confession or to compel restoration of property | `chapter-16-hurt.l4` |
| 332 | Voluntarily causing hurt to deter public servant from his duty | `chapter-16-hurt.l4` |
| 333 | Voluntarily causing grievous hurt to deter public servant from his duty | `chapter-16-hurt.l4` |
| 334 | Voluntarily causing hurt on provocation | `chapter-16-hurt.l4` |
| 334A | Punishment for voluntarily causing hurt on provocation which causes grievous hurt | `chapter-16-hurt.l4` |
| 335 | Causing grievous hurt on provocation | `chapter-16-hurt.l4` |
| 335A | Allowing neglect, physical or sexual abuse of domestic worker or vulnerable person | `chapter-16-hurt.l4` |
| 335B | Punishment for act which endangers life or personal safety of others with knowledge or belief that it is likely to cause death | `chapter-16-hurt.l4` |
| 336 | Punishment for act which endangers life or the personal safety of others | `chapter-16-hurt.l4` |
| 337 | Causing hurt by an act which endangers life or the personal safety of others | `chapter-16-hurt.l4` |
| 338 | Causing grievous hurt by an act which endangers life or the personal safety of others | `chapter-16-hurt.l4` |
| 339 | Wrongful restraint | `chapter-16-restraint-and-force.l4` |
| 340 | Wrongful confinement | `chapter-16-restraint-and-force.l4` |
| 345 | Wrongful confinement of person for whose liberation a writ has been issued | `chapter-16-restraint-and-force.l4` |
| 346 | Wrongful confinement in secret | `chapter-16-restraint-and-force.l4` |
| 347 | Wrongful confinement for the purpose of extorting property or constraining to an illegal act | `chapter-16-restraint-and-force.l4` |
| 348 | Wrongful confinement for the purpose of extorting confession or of compelling restoration of property | `chapter-16-restraint-and-force.l4` |
| 349 | Force | `chapter-16-restraint-and-force.l4` |
| 350 | Criminal force | `chapter-16-restraint-and-force.l4` |
| 351 | Assault | `chapter-16-restraint-and-force.l4` |
| 352 | Punishment for using criminal force otherwise than on grave and sudden provocation | `chapter-16-restraint-and-force.l4` |
| 353 | Using criminal force to deter a public servant from discharge of his duty | `chapter-16-restraint-and-force.l4` |
| 354 | Assault or use of criminal force to a person with intent to outrage modesty | `chapter-16-restraint-and-force.l4` |
| 354A | Outraging modesty in certain circumstances | `chapter-16-restraint-and-force.l4` |
| 355 | Assault or criminal force with intent to dishonour otherwise than on grave and sudden provocation | `chapter-16-restraint-and-force.l4` |
| 356 | Assault or criminal force in committing or attempting to commit theft of property carried by a person | `chapter-16-restraint-and-force.l4` |
| 357 | Assault or criminal force in attempting wrongfully to confine a person | `chapter-16-restraint-and-force.l4` |
| 358 | Assaulting or using criminal force on grave and sudden provocation | `chapter-16-restraint-and-force.l4` |
| 359 | Kidnapping | `chapter-16-kidnapping.l4` |
| 360 | Kidnapping from Singapore | `chapter-16-kidnapping.l4` |
| 361 | Kidnapping from lawful guardianship | `chapter-16-kidnapping.l4` |
| 362 | Abduction | `chapter-16-kidnapping.l4` |
| 364 | Kidnapping or abducting in order to murder | `chapter-16-kidnapping.l4` |
| 365 | Kidnapping or abducting with intent secretly and wrongfully to confine a person | `chapter-16-kidnapping.l4` |
| 366 | Kidnapping or abducting a woman to compel her marriage, etc. | `chapter-16-kidnapping.l4` |
| 367 | Kidnapping or abducting in order to subject a person to grievous hurt, slavery, etc. | `chapter-16-kidnapping.l4` |
| 368 | Wrongfully concealing or keeping in confinement a kidnapped person | `chapter-16-kidnapping.l4` |
| 370 | Buying or disposing of any person as a slave | `chapter-16-kidnapping.l4` |
| 371 | Habitual dealing in slaves | `chapter-16-kidnapping.l4` |
| 372 | Selling minor for purposes of prostitution, etc. | `chapter-16-kidnapping.l4` |
| 373 | Buying minor for purposes of prostitution, etc. | `chapter-16-kidnapping.l4` |
| 373A | Importing woman for purposes of prostitution, etc. | `chapter-16-kidnapping.l4` |
| 374 | Unlawful compulsory labour | `chapter-16-kidnapping.l4` |

**Not encoded:** s 302, s 304, s 311, s 323, s 325, s 341, s 342, s 363, s 363A, s 375, s 376, s 376A, s 376AA, s 376B, s 376C, s 376D, s 376E, s 376EA, s 376EB, s 376EC, s 376ED, s 376EE, s 376F, s 376G, s 376H, s 377, s 377B, s 377BA, s 377BB, s 377BC, s 377BD, s 377BE, s 377BF, s 377BG, s 377BH, s 377BI, s 377BJ, s 377BK, s 377BL, s 377BM, s 377BN, s 377BO, s 377C, s 377CA, s 377CB, s 377D.

Nine of those are pure punishment sections — ss 302, 304, 311, 323, 325, 341, 342, 363
and 363A — which this subject does not encode because it does not compute sentence. The
remaining 37 are the Chapter's last group, the sexual offences (ss 375 to 377D), which
includes its own interpretation section (s 377C) and three provisions that govern the
whole group (ss 377CA, 377CB and 377D).

### Chapter 17 — Offences against property

12 of 76 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 378 | Theft | `chapter-17-property.l4` |
| 403 | Dishonest misappropriation of property | `chapter-17-property.l4` |
| 405 | Criminal breach of trust | `chapter-17-property.l4` |
| 415 | Cheating | `chapter-17-cheating.l4` |
| 416 | Cheating by personation | `chapter-17-cheating.l4` |
| 416A | Illegally obtained personal information | `chapter-17-fraud.l4` |
| 416B | Cheating by remote communication | `chapter-17-cheating.l4` |
| 418 | Cheating with knowledge that wrongful loss may be thereby | `chapter-17-cheating.l4` |
| 420 | Cheating and dishonestly inducing a delivery of property | `chapter-17-cheating.l4` |
| 420A | Obtaining services dishonestly or fraudulently | `chapter-17-cheating.l4` |
| 424A | Fraud by false representation, non-disclosure or abuse of | `chapter-17-fraud.l4` |
| 424B | Fraud by false representation, non-disclosure or abuse of | `chapter-17-fraud.l4` |

**Not encoded:** s 379, s 379A, s 380, s 381, s 382, s 383, s 384, s 385, s 386, s 387, s 388, s 389, s 390, s 391, s 392, s 393, s 394, s 395, s 396, s 397, s 399, s 400, s 401, s 402, s 404, s 406, s 407, s 408, s 409, s 410, s 411, s 412, s 413, s 414, s 417, s 419, s 421, s 422, s 423, s 424, s 425, s 426, s 427, s 428, s 435, s 436, s 437, s 438, s 439, s 440, s 441, s 442, s 447, s 448, s 449, s 450, s 451, s 452, s 453, s 458A, s 459, s 460, s 461, s 462.

Repealed, nothing to encode: s 429, s 430, s 430A, s 431, s 431A, s 432, s 433, s 434, s 443, s 444, s 445, s 446, s 454, s 455, s 456, s 457, s 458.

### Chapter 18 — Offences relating to documents, electronic records and marks

2 of 28 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 463 | Forgery | `chapter-18-forgery.l4` |
| 464 | Making a false document or false electronic record | `chapter-18-forgery.l4` |

**Not encoded:** s 465, s 466, s 467, s 468, s 469, s 470, s 471, s 472, s 473, s 473A, s 473B, s 473C, s 474, s 475, s 476, s 477, s 477A, s 489A, s 489B, s 489C, s 489D, s 489E, s 489F, s 489G, s 489H, s 489I.

### Chapter 21 — Defamation

1 of 4 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 499 | Defamation | `chapter-21-22-speech.l4` |

**Not encoded:** s 500, s 501, s 502.

### Chapter 22 — Criminal intimidation, insult and annoyance

4 of 5 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 503 | Criminal intimidation | `chapter-21-22-speech.l4` |
| 504 | Intentional insult with intent to provoke a breach of the peace | `chapter-21-22-speech.l4` |
| 505 | Statements conducing to public mischief | `chapter-21-22-speech.l4` |
| 506 | Punishment for criminal intimidation | `chapter-21-22-speech.l4` |

**Not encoded:** s 507.

Repealed, nothing to encode: s 508, s 509, s 510.

### Chapter 23 — Attempts to commit offences

1 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 511 | Attempt to commit offence | `chapter-23-attempts.l4` |

**Not encoded:** s 512.

## 5. Chapters with nothing encoded

| chapter | live sections | range |
| --- | ---: | --- |
| **Chapter 6** — Offences against the State | 15 | ss 121–130A |
| **Chapter 6A** — Piracy | 2 | ss 130B–130C |
| **Chapter 6B** — Genocide | 2 | ss 130D–130E |
| **Chapter 7** — Offences relating to the armed forces | 12 | ss 131–140B |
| **Chapter 8** — Offences relating to unlawful assembly | 18 | ss 141–160 |
| **Chapter 9** — Offences by or relating to public servants | 11 | ss 161–171 |
| **Chapter 10** — Contempts of the lawful authority of public servants | 19 | ss 172–190 |
| **Chapter 11** — False evidence and offences against public justice | 43 | ss 191–229 |
| **Chapter 12** — Offences relating to government stamps | 9 | ss 230–263 |
| **Chapter 14** — Offences affecting public tranquility, health, safety and decency | 35 | ss 267A–294 |
| **Chapter 15** — Offences relating to race | 2 | ss 295–298A |

**168 live sections, none of them modelled** — 32% of the live Code. Chapters 13 and 20 are
omitted from this table: both are wholly repealed and contribute no live section.

This table gives ranges. `missing-sections.md` names each of these 168 sections individually,
with the Act's own marginal heading, alongside the 157 missing from the partially encoded
chapters above.

## 6. The three gaps that were more than scope choices — closed 11 Sep 2026

Most of §5 is honest scoping: an agent has no occasion to ask whether its output is piracy or
an offence relating to government stamps. Three absences were different, because a caller
could reasonably expect them to be there and be misled by their silence. All three are now
encoded. What follows is what each one was, and what closing it changed.

**6.1 Chapter 4A — the right of private defence (ss 96 to 106A).** This was the one that
distorted the screen's answers. The encoding modelled twenty Chapter 4 general exceptions and
**zero** private-defence rules, so `a general exception applies` could not report a
private-defence justification, and an act a court would hold justified under s 96 still came
back from the screen as an indicated offence.

All twelve sections are now encoded in `chapter-4a-private-defence.l4`, and — this is the
part that mattered — they are **wired into the offence wrappers**. s 6 subjects every offence
definition to the Chapter entitled "Right of Private Defence" as well as to the General
Exceptions, so all nineteen `the proposed act constitutes ...` wrappers now call
`the act is taken outside offence by Chapter 4 or Chapter 4A` in place of
`a general exception applies`. The screen reports the two routes in separate fields, so a
caller can still tell which one fired.

The asymmetry §6.1 used to warn about — over-inclusive on offences, under-inclusive on
defences, so a FALSE was more trustworthy than a TRUE — is narrowed but not gone. It now
rests on the remaining unencoded defences and on the 325 unencoded sections, not on a whole
missing Chapter.

**6.2 Chapter 5, ss 111, 113 and 114.** ss 109, 110, 112, 115 to 120 are punishment and
concealment provisions, consistent with this subject not computing sentence, and stay
unencoded. But ss 111, 113 and 114 are substantive liability rules — the abettor's liability
when a *different act* from the one abetted results (s 111), when the act abetted causes a
*different effect* (s 113), and when the abettor is *present* at the commission (s 114). An
agent reasoning about abetment from ss 107 and 108 alone could not reach them. All three are
now encoded, each with its Illustrations carried into `agent-cases.l4` as assertions.

**6.3 Chapter 1, ss 3, 4A and 5.** The territorial screen was narrower than the Code's actual
reach. ss 3 and 4A now feed `Singapore has territorial reach over the proposed act` alongside
ss 2, 4 and 4B. s 5 is decided too, though it adds no limb to any offence test: it is the
reason a FALSE from the screen is not a clearance, and the screen now says so in its own
field. `NOTES.md` §3 explains why s 5 is decided where s 79A is not.

### What is still missing, and still matters

**Updated later the same day.** The absence named here was Chapter 16, and it is now half
closed: 74 of its 120 live sections are encoded — six of its seven groups — so the screen
reports murder, culpable homicide, hurt, grievous hurt, wrongful restraint, wrongful
confinement, assault, criminal force, outraging modesty, causing miscarriage, child
destruction, abandonment of a child, kidnapping, abduction, slavery and forced labour, each
subject to s 6. One group remains: the sexual offences (ss 375 to 377D), 37 live sections.

One thing the Chapter 16 pass did **not** do, and it is recorded in
`verification-register-pass-4.md` §T3: `there is a section 97(a) right to defend the body`
still takes "an offence affecting the human body" as a caller-asserted fact rather than
computing it from the new hurt rules. The offence in question is the *assailant's*, and the
`Proposed Act` bundle carries one actor's facts; and with three groups still absent, a FALSE
from the hurt predicate would not mean no such offence was in play. Closing that needs a
two-actor bundle, which is a change to the shape of the subject.

`missing-sections.md` names all 325 sections that remain.

## 7. How to regenerate this register

Parse every line beginning `@ref` in `*.l4` for section numbers, expanding `ss X, Y, Z` lists
and `ss X to Y` ranges and stripping parenthesised subsections; parse the arrangement of
sections from the head of `registers/source-bundle/PC1871.txt`; match. Roughly 40 lines of
script. It is not committed here for the same reason the machine checker is not: this
repository holds law, and tooling belongs in `l4-ide`.

A section acquiring or losing an `@ref` changes these counts, so re-run this whenever modules
are added or citations edited. Counts here are current as at the pass-2 fixes.
