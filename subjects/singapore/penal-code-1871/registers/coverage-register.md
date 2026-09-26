# Penal Code 1871 — coverage register

**Run date:** 2026-09-16 (the closing pass; first run 2026-09-09)
**Question answered:** which sections of the Act are modelled, and which are not.
**Method:** every `@ref` citation in the 45 `.l4` modules was parsed for section
numbers and matched against the Act's own arrangement of sections, as it appears in
`registers/source-bundle/PC1871.txt` (SSO current version as at 09 Sep 2026). Multi-section
citations (`ss 45, 46, 47, 48`) and ranges (`ss 76 to 95`) are expanded; subsection numbers
in parentheses are stripped so that `s 120A(4) and (5)` does not read as sections 4 and 5.

This register is mechanical. It records that a section **is cited by the encoding**, not that
the rule is a correct or complete reading of it. Fidelity is a separate question, answered by
the eight verification registers, `registers/verification-register.md` and
`registers/verification-register-pass-2.md` to `-pass-8.md`.

One limit of the method is worth stating, because the fidelity pass found it: a citation may
sit on a `DECLARE` rather than on a rule, in which case this register counts the section as
covered although nothing decides it. That was true of ss 45 and 46 when this register was
first generated (defect W4 in pass 2). Both now have rules, so the count below stands -- but
a future reader should treat any single-citation section as worth checking rather than as
proven. Until this run one section was excluded from the count by hand: s 79A falls inside
the range citation `ss 6 and 76 to 95` on the Chapter 4 gathering rule, and no rule decided
it. Since 16 Sep 2026 two rules do, each with its own `@ref`, so the hand exclusion is gone
and the count is what the citations say.

---

## 1. Headline

| | sections |
| --- | ---: |
| listed in the Act's arrangement of sections | 600 |
| repealed — nothing to encode | 75 |
| **live** | **525** |
| **encoded** | **525** |
| **live but not encoded** | **0** |

**Every live section of the Code has a rule.** The seven that §3 listed as deliberate until
15 Sep -- the short title, four drafting conventions, the definition of "section", and the
s 79A closure rule -- were encoded on 16 Sep 2026. §3 now records what each of them decides,
and how much of that is substance: s 79A and s 49 carry rules an agent will call; ss 7, 8, 9
and 50 are decided in the shape the other defined terms take; s 1 is a name made callable.

Six passes brought the count here. The first, on 11 Sep, added 18 -- the whole of Chapter 4A
(ss 96 to 106A), ss 111, 113 and 114 of Chapter 5, and ss 3, 4A and 5 of Chapter 1 -- which
were the three gaps §6 of this register called more than scope choices. The second opened
**Chapter 16**, the offences affecting the human body, and completed its substantive sections.
The third, on 12 Sep, did the same for **Chapter 17**, the offences against property; the
fourth, on 14 Sep, for **Chapter 18**. The fifth, on 15 Sep, encoded **everything else**: the
eleven chapters that had nothing (6, 6A, 6B, 7, 8, 9, 10, 11, 12, 14, 15), the nine remaining
sections of Chapter 5, ss 501, 502 and 507, and -- reversing the policy under which the
earlier passes had left them out -- the 24 standalone punishment sections, now encoded as
prescribed `Punishment` values in the Chapter 3 vocabulary (`punishment-provisions.l4`, and
the punishment rules in each new chapter module). The sixth, on 16 Sep, encoded the seven
sections the fifth had left.

There is no Chapter 19; Chapters 13 and 20 are wholly repealed.

## 2. By chapter

| chapter | ss | repealed | live | encoded | not encoded |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Chapter 1** — PRELIMINARY | 7 | 0 | 7 | 7 | 0 |
| **Chapter 2** — GENERAL EXPLANATIONS | 56 | 2 | 54 | 54 | 0 |
| **Chapter 3** — Punishments | 13 | 3 | 10 | 10 | 0 |
| **Chapter 4** — General Exceptions | 21 | 0 | 21 | 21 | 0 |
| **Chapter 4A** — Right of private defence | 12 | 0 | 12 | 12 | 0 |
| **Chapter 5** — Abetment | 16 | 0 | 16 | 16 | 0 |
| **Chapter 5A** — Criminal Conspiracy | 2 | 0 | 2 | 2 | 0 |
| **Chapter 6** — Offences against the State | 15 | 0 | 15 | 15 | 0 |
| **Chapter 6A** — Piracy | 2 | 0 | 2 | 2 | 0 |
| **Chapter 6B** — Genocide | 2 | 0 | 2 | 2 | 0 |
| **Chapter 7** — Offences relating to the armed forces | 12 | 0 | 12 | 12 | 0 |
| **Chapter 8** — Offences relating to unlawful assembly | 21 | 3 | 18 | 18 | 0 |
| **Chapter 9** — Offences by or relating to public servants | 11 | 0 | 11 | 11 | 0 |
| **Chapter 10** — Contempts of the lawful authority of public servants | 19 | 0 | 19 | 19 | 0 |
| **Chapter 11** — False evidence and offences against public justice | 46 | 3 | 43 | 43 | 0 |
| **Chapter 12** — Offences relating to government stamps | 35 | 26 | 9 | 9 | 0 |
| **Chapter 13** — *(wholly repealed)* | 4 | 4 | 0 | 0 | 0 |
| **Chapter 14** — Offences affecting the public tranquility, public health, safety, convenience, decency and morals | 35 | 0 | 35 | 35 | 0 |
| **Chapter 15** — Offences relating to race | 5 | 3 | 2 | 2 | 0 |
| **Chapter 16** — Offences affecting the human body | 126 | 6 | 120 | 120 | 0 |
| **Chapter 17** — Offences against property | 93 | 17 | 76 | 76 | 0 |
| **Chapter 18** — Offences relating to documents or electronic records, false instruments, and to currency and bank notes | 28 | 0 | 28 | 28 | 0 |
| **Chapter 20** — *(wholly repealed)* | 5 | 5 | 0 | 0 | 0 |
| **Chapter 21** — Defamation | 4 | 0 | 4 | 4 | 0 |
| **Chapter 22** — Criminal intimidation, insult and annoyance | 8 | 3 | 5 | 5 | 0 |
| **Chapter 23** — Attempts to commit offences | 2 | 0 | 2 | 2 | 0 |
| **total** | **600** | **75** | **525** | **525** | **0** |

## 3. The seven sections encoded last, and what each decides

From 09 to 15 Sep 2026 this section listed these seven as deliberately not encoded, on the
view that each states no factual test. On 16 Sep each was given a rule. The view was not
wrong about the sections' weight -- none adds a limb to any offence test -- but it was
wrong about two of them having nothing to decide, and once s 79A and s 49 had rules the
other five were cheap to give the shape every other defined term already has. The table
records what each rule decides, and how much of it is substance, so that a reader does not
mistake the count of 525 for 525 sections of equal weight.

| s | what is decided | weight |
| --- | --- | --- |
| 1 | `the short title of this Act` is the string "Penal Code 1871"; `the citation names this Act by its short title` compares a citation with it. | nominal — a name made callable |
| 7 | `the expression is used in conformity with its explanation`: an expression explained in any part of the Code, used in the Code. Disjoined with the s 6A rule into `the Code explanation governs the expression as used`, so the pair now covers a use inside the Code and a use in another written law. | light — the within-Code half of a pair whose other half already had a rule |
| 8 | With s 10: `the word reaches a person of that sex`. "He" reaches either sex; "man" and "woman" reach one each. | light — but it is the rule that separates s 375's "any man" from every "whoever ... he" |
| 9 | `the word reaches the plural number` and `the word reaches the singular number`, each with the contrary-context carve-out as a negated conjunct. | light |
| 49 | `the period in calendar months of` years months = 12 × years + months, the one arithmetic consequence of Gregorian reckoning. The `Punishment` record carries terms in years and s 40(3) asks for months, so this is the conversion between them. Counts no days: the encoding carries no date. | substantive |
| 50 | `is a section within section 50`: a portion of a Chapter distinguished by a prefixed numeral. The facts-record-and-predicate shape of ss 48 and 51. | nominal |
| 79A | s 79A(1): `a mistake of law or ignorance of the law is a defence to the charge` — only where written law provides that it is. s 79A(2): `the prosecution must prove the fault element notwithstanding the alleged mistake of law` — where the alleged mistake may negate the fault element. Neither is a limb of `a general exception applies`; the first is reported by the screen beside s 5. | substantive — the FALSE an agent asking about ignorance of the law needs |

s 79A is now decided the way s 5 is, and for the same reason -- `NOTES.md` §3 records both.
ss 79(2) and 80(2), the burden rules that sit beside decided exceptions, are still not
decided; `verification-register-pass-8.md` §N32 records why s 79A(2) is and they are not.

## 4. Every chapter, section by section

The module named is the one that carries the section's rule. Where two are named, the
second builds on the first (ss 2 to 4B are decided in `chapter-1-preliminary.l4` and
gathered in `agent-compliance.l4`; the s 375 to 376ED sexual offences take their consent
and exploitation tests from `chapter-16-sexual-general.l4`).

### Chapter 1 — PRELIMINARY

7 of 7 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 1 | Short title | `chapter-1-preliminary.l4` |
| 2 | Punishment of offences committed within Singapore | `chapter-1-preliminary.l4` |
| 3 | Punishment of offences committed beyond, but which by law may be tried within Singapore | `chapter-1-preliminary.l4` |
| 4 | Jurisdiction over public servants for offences committed outside Singapore | `chapter-1-preliminary.l4` |
| 4A | Offences against State and genocide committed outside Singapore by citizen or permanent resident | `chapter-1-preliminary.l4` |
| 4B | Punishment of specified offences with elements occurring in Singapore but others occurring outside Singapore | `chapter-1-preliminary.l4` |
| 5 | Certain laws not to be affected by this Code | `chapter-1-preliminary.l4` |

### Chapter 2 — GENERAL EXPLANATIONS

54 of 54 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 6 | Definitions in this Code to be understood subject to exceptions | `chapter-4-exceptions.l4`, `chapter-4a-private-defence.l4` |
| 6A | Definitions to apply to this Code and other written law | `chapter-2-definitions.l4` |
| 7 | Expression once explained is used in the same sense throughout this Code | `chapter-2-definitions.l4` |
| 8 | "Gender" | `chapter-2-definitions.l4` |
| 9 | "Number" | `chapter-2-definitions.l4` |
| 10 | "Man" and "woman" | `chapter-2-definitions.l4` |
| 11 | "Person" | `chapter-2-definitions.l4` |
| 12 | "Public" [There are no sections 13 to 16.] | `chapter-2-definitions.l4` |
| 17 | "Government" [There is no section 18.] | `chapter-2-definitions.l4` |
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
| 34 | Each of several persons liable for an act done by all, in like manner as if done by him alone | `chapter-2-participation.l4` |
| 35 | When such an act is criminal by reason of its being done with a criminal knowledge or intention | `chapter-2-participation.l4` |
| 36 | Effect caused partly by act and partly by omission | `chapter-2-participation.l4` |
| 37 | Cooperation by doing one of several acts constituting an offence | `chapter-2-participation.l4` |
| 38 | Several persons engaged in the commission of a criminal act may be guilty of different offences | `chapter-2-participation.l4` |
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
| 49 | "Year" and "month" | `chapter-2-definitions.l4` |
| 50 | "Section" | `chapter-2-definitions.l4` |
| 51 | "Oath" | `chapter-2-definitions.l4` |

Repealed, nothing to encode: s 39, s 52.

### Chapter 3 — Punishments

10 of 10 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 53 | Punishments | `chapter-3-punishments.l4` |
| 54 | Imprisonment for life | `chapter-3-punishments.l4` |
| 72 | Punishment of a person found guilty of one of several offences, the judgment stating that it is doubtful of which | `chapter-3-punishments.l4` |
| 73 | Enhanced penalties for offences against domestic workers | `chapter-3-punishments.l4` |
| 74 | Enhanced penalties for racially or religiously aggravated offences | `chapter-3-punishments.l4` |
| 74A | Enhanced penalties for offences against vulnerable persons | `chapter-3-punishments.l4` |
| 74B | Enhanced penalties for offences against person below 14 years of age | `chapter-3-punishments.l4` |
| 74C | Enhanced penalties for offences against victims in intimate relationships | `chapter-3-punishments.l4` |
| 74D | Enhanced penalties for offences against victims in close relationships | `chapter-3-punishments.l4` |
| 74E | Application of enhanced penalties | `chapter-3-punishments.l4` |

Repealed, nothing to encode: s 57, s 71, s 75.

### Chapter 4 — General Exceptions

21 of 21 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 76 | Act done by person bound, or justified by law | `chapter-4-exceptions.l4` |
| 77 | Act of judge when acting judicially | `chapter-4-exceptions.l4` |
| 78 | Act done pursuant to the judgment or order of a court of justice | `chapter-4-exceptions.l4` |
| 79 | Act done by person by mistake of fact believing himself bound or justified by law | `chapter-4-exceptions.l4` |
| 79A | Mistake of law or ignorance of law not defence | `chapter-4-exceptions.l4`, `agent-compliance.l4` |
| 80 | Accident in the doing of a lawful act | `chapter-4-exceptions.l4` |
| 81 | Act likely to cause harm but done to prevent other harm | `chapter-4-exceptions.l4` |
| 82 | Act of a child below 10 years of age | `chapter-4-exceptions.l4` |
| 83 | Act of a child of or above 10 and below 12 years of age, who has not sufficient maturity of understanding | `chapter-4-exceptions.l4` |
| 84 | Act of person of unsound mind | `chapter-4-exceptions.l4` |
| 85 | Intoxication when a defence | `chapter-4-exceptions.l4` |
| 86 | Effect of defence of intoxication when established | `chapter-4-exceptions.l4` |
| 87 | Act not intended and not known to be likely to cause death or grievous hurt, done by consent | `chapter-4-exceptions.l4` |
| 88 | Act not intended to cause death done by consent in good faith for the benefit of a person | `chapter-4-exceptions.l4` |
| 89 | Act done in good faith for the benefit of a child or person of unsound mind, by or by consent of guardian | `chapter-4-exceptions.l4` |
| 90 | Consent given under fear or misconception, by person of unsound mind, etc., and by child | `chapter-4-exceptions.l4` |
| 91 | Acts which are offences independently of harm caused to the person consenting, are not within the exceptions in sections 87, 88 and 89 | `chapter-4-exceptions.l4` |
| 92 | Act done in good faith for the benefit of a person without consent | `chapter-4-exceptions.l4` |
| 93 | Communication made in good faith | `chapter-4-exceptions.l4` |
| 94 | Act to which a person is compelled by threats | `chapter-4-exceptions.l4` |
| 95 | Act causing slight harm | `chapter-4-exceptions.l4` |

### Chapter 4A — Right of private defence

12 of 12 live sections encoded.

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

### Chapter 5 — Abetment

16 of 16 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 107 | Abetment of the doing of a thing | `chapter-5-abetment.l4` |
| 108 | Abettor | `chapter-5-abetment.l4` |
| 108A | Abetment in Singapore of an offence outside Singapore | `chapter-5-abetment.l4` |
| 108B | Abetment outside Singapore of an offence in Singapore | `chapter-5-abetment.l4` |
| 109 | Punishment of abetment if the act abetted is committed in consequence, and where no express provision is made for its punishment | `chapter-5-abetment.l4` |
| 110 | Punishment of abetment if the person abetted does the act with a different intention from that of the abettor | `chapter-5-abetment.l4` |
| 111 | Liability of abettor when one act is abetted and a different act is done | `chapter-5-abetment.l4` |
| 112 | Abettor, when liable to cumulative punishment for act abetted and for act done | `chapter-5-abetment.l4` |
| 113 | Liability of abettor for an offence caused by the act abetted different from that intended by the abettor | `chapter-5-abetment.l4` |
| 114 | Abettor present when offence committed | `chapter-5-abetment.l4` |
| 115 | Abetment of offence punishable with death or imprisonment for life | `chapter-5-abetment.l4` |
| 116 | Abetment of offence punishable with imprisonment | `chapter-5-abetment.l4` |
| 117 | Abetting the commission of an offence by the public or by more than 10 persons | `chapter-5-abetment.l4` |
| 118 | Concealing a design to commit an offence punishable with death or imprisonment for life | `chapter-5-abetment.l4` |
| 119 | A public servant concealing a design to commit an offence which it is his duty to prevent | `chapter-5-abetment.l4` |
| 120 | Concealing a design to commit an offence punishable with imprisonment | `chapter-5-abetment.l4` |

### Chapter 5A — Criminal Conspiracy

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 120A | Definition of criminal conspiracy | `chapter-5a-conspiracy.l4` |
| 120B | Punishment of criminal conspiracy | `chapter-5a-conspiracy.l4` |

### Chapter 6 — Offences against the State

15 of 15 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 121 | Waging or attempting to wage war or abetting the waging of war against the Government | `chapter-6-state.l4` |
| 121A | Offences against the President’s person | `chapter-6-state.l4` |
| 121B | Offences against authority | `chapter-6-state.l4` |
| 121C | Abetting offences under section 121A or 121B | `chapter-6-state.l4` |
| 121D | Intentional omission to give information of offences against section 121, 121A, 121B or 121C by a person bound to inform | `chapter-6-state.l4` |
| 122 | Collecting arms, etc., with the intention of waging war against the Government | `chapter-6-state.l4` |
| 123 | Concealing with intent to facilitate a design to wage war | `chapter-6-state.l4` |
| 124 | Assaulting President, etc., with intent to compel or restrain the exercise of any lawful power | `chapter-6-state.l4` |
| 125 | Waging war against any power in alliance or at peace with Singapore | `chapter-6-state.l4` |
| 126 | Committing depredation on the territories of any power in alliance or at peace with Singapore | `chapter-6-state.l4` |
| 127 | Receiving property taken by war or depredation mentioned in sections 125 and 126 | `chapter-6-state.l4` |
| 128 | Public servant voluntarily allowing prisoner of State or war in his custody to escape | `chapter-6-state.l4` |
| 129 | Public servant negligently suffering prisoner of State or war in his custody to escape | `chapter-6-state.l4` |
| 130 | Aiding escape of, rescuing, or harbouring such prisoner | `chapter-6-state.l4` |
| 130A | "Harbour" | `chapter-6-state.l4` |

### Chapter 6A — Piracy

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 130B | Piracy by law of nations. Cf. 12 and 13 Victoria c. 96 (Admiralty Offences (Colonial) Act 1849) | `chapter-6a-6b-piracy-and-genocide.l4` |
| 130C | Piratical acts | `chapter-6a-6b-piracy-and-genocide.l4` |

### Chapter 6B — Genocide

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 130D | Genocide | `chapter-6a-6b-piracy-and-genocide.l4` |
| 130E | Punishment for genocide | `chapter-6a-6b-piracy-and-genocide.l4` |

### Chapter 7 — Offences relating to the armed forces

12 of 12 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 131 | Abetting mutiny, or attempting to seduce an officer or a serviceman from his duty | `chapter-7-armed-forces.l4` |
| 132 | Abetment of mutiny, if mutiny is committed in consequence thereof | `chapter-7-armed-forces.l4` |
| 133 | Abetment of an assault by an officer or a serviceman on his superior officer, when in the execution of his office | `chapter-7-armed-forces.l4` |
| 134 | Abetment of such assault, if the assault is committed | `chapter-7-armed-forces.l4` |
| 135 | Abetment of the desertion of an officer or a serviceman | `chapter-7-armed-forces.l4` |
| 136 | Harbouring a deserter | `chapter-7-armed-forces.l4` |
| 137 | Deserter concealed on board merchant vessel through negligence of master | `chapter-7-armed-forces.l4` |
| 138 | Abetment of act of insubordination by an officer or a serviceman | `chapter-7-armed-forces.l4` |
| 139 | Saving | `chapter-7-armed-forces.l4` |
| 140 | Wearing the dress of a serviceman | `chapter-7-armed-forces.l4` |
| 140A | "Harbour" | `chapter-7-armed-forces.l4` |
| 140B | Application of Chapter 7 to Singapore Police Force | `chapter-7-armed-forces.l4` |

### Chapter 8 — Offences relating to unlawful assembly

18 of 18 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 141 | Unlawful assembly | `chapter-8-unlawful-assembly.l4` |
| 142 | Being a member of an unlawful assembly | `chapter-8-unlawful-assembly.l4` |
| 143 | Punishment | `chapter-8-unlawful-assembly.l4` |
| 144 | Joining an unlawful assembly armed with any deadly weapon | `chapter-8-unlawful-assembly.l4` |
| 145 | Joining or continuing in an unlawful assembly, knowing that it has been commanded to disperse | `chapter-8-unlawful-assembly.l4` |
| 146 | Force used by one member in prosecution of common object | `chapter-8-unlawful-assembly.l4` |
| 147 | Punishment for rioting | `chapter-8-unlawful-assembly.l4` |
| 148 | Rioting, armed with a deadly weapon | `chapter-8-unlawful-assembly.l4` |
| 149 | Every member of an unlawful assembly to be deemed guilty of any offence committed in prosecution of common object | `chapter-8-unlawful-assembly.l4` |
| 150 | Hiring, or conniving at hiring, of persons to join an unlawful assembly | `chapter-8-unlawful-assembly.l4` |
| 151 | Knowingly joining or continuing in any assembly of 5 or more persons after it has been commanded to disperse | `chapter-8-unlawful-assembly.l4` |
| 152 | Assaulting or obstructing public servant when suppressing riot, etc. | `chapter-8-unlawful-assembly.l4` |
| 153 | Intentionally or rashly giving provocation, with intent to cause riot | `chapter-8-unlawful-assembly.l4` |
| 154 | Owner or occupier of land on which an unlawful assembly is held | `chapter-8-unlawful-assembly.l4` |
| 155 | Liability of person for whose benefit a riot is committed | `chapter-8-unlawful-assembly.l4` |
| 156 | Liability of agent of owner or occupier for whose benefit a riot is committed | `chapter-8-unlawful-assembly.l4` |
| 157 | Harbouring persons hired for an unlawful assembly | `chapter-8-unlawful-assembly.l4` |
| 158 | Being hired to take part in an unlawful assembly or riot | `chapter-8-unlawful-assembly.l4` |

Repealed, nothing to encode: s 151A, s 159, s 160.

### Chapter 9 — Offences by or relating to public servants

11 of 11 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 161 | Public servant taking a gratification, other than legal remuneration, in respect of an official act | `chapter-9-public-servants.l4` |
| 162 | Taking a gratification in order, by corrupt or illegal means, to influence a public servant | `chapter-9-public-servants.l4` |
| 163 | Taking a gratification, for the exercise of personal influence with a public servant | `chapter-9-public-servants.l4` |
| 164 | Punishment for abetment by public servant of the offences above defined | `chapter-9-public-servants.l4` |
| 165 | Public servant obtaining any valuable thing, without consideration, from person concerned in any proceeding or business transacted by such public servant | `chapter-9-public-servants.l4` |
| 166 | Public servant disobeying a direction of the law, with intent to cause injury to any person | `chapter-9-public-servants.l4` |
| 167 | Public servant framing an incorrect document or electronic record with intent to cause injury | `chapter-9-public-servants.l4` |
| 168 | Public servant unlawfully engaging in trade | `chapter-9-public-servants.l4` |
| 169 | Public servant unlawfully buying or bidding for property | `chapter-9-public-servants.l4` |
| 170 | Personating a public servant | `chapter-9-public-servants.l4` |
| 171 | Wearing garb or carrying token used by public servant, with fraudulent intent | `chapter-9-public-servants.l4` |

### Chapter 10 — Contempts of the lawful authority of public servants

19 of 19 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 172 | Absconding to avoid arrest on warrant or service of summons, etc., proceeding from a public servant | `chapter-10-contempts.l4` |
| 173 | Preventing service of summons, etc., or preventing publication thereof | `chapter-10-contempts.l4` |
| 174 | Failure to attend in obedience to order from public servant | `chapter-10-contempts.l4` |
| 175 | Omission to produce document or electronic record to public servant by person legally bound to produce such document or electronic record | `chapter-10-contempts.l4` |
| 176 | Omission to give notice or information to public servant by person legally bound to give such notice or information | `chapter-10-contempts.l4` |
| 177 | Furnishing false information | `chapter-10-contempts.l4` |
| 178 | Refusing oath when duly required to take oath by a public servant | `chapter-10-contempts.l4` |
| 179 | Refusing to answer public servant authorised to question | `chapter-10-contempts.l4` |
| 180 | Refusing to sign statement | `chapter-10-contempts.l4` |
| 181 | False statement on oath to public servant or person authorised to administer an oath | `chapter-10-contempts.l4` |
| 182 | False information, with intent to cause a public servant to use his lawful power to the injury of another person | `chapter-10-contempts.l4` |
| 183 | Resistance to taking of property by lawful authority of public servant | `chapter-10-contempts.l4` |
| 184 | Obstructing sale of property offered for sale by authority of public servant | `chapter-10-contempts.l4` |
| 185 | Illegal purchase or bid for property offered for sale by authority of public servant | `chapter-10-contempts.l4` |
| 186 | Obstructing public servant in discharge of his public functions | `chapter-10-contempts.l4` |
| 187 | Omission to assist public servant when bound by law to give assistance | `chapter-10-contempts.l4` |
| 188 | Disobedience to order duly promulgated by public servant | `chapter-10-contempts.l4` |
| 189 | Threat of injury to a public servant | `chapter-10-contempts.l4` |
| 190 | Threat of injury to induce any person to refrain from applying for protection to a public servant | `chapter-10-contempts.l4` |

### Chapter 11 — False evidence and offences against public justice

43 of 43 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 191 | Giving false evidence | `chapter-11-false-evidence.l4` |
| 192 | Fabricating false evidence | `chapter-11-false-evidence.l4` |
| 193 | Punishment for false evidence | `chapter-11-false-evidence.l4` |
| 194 | Giving or fabricating false evidence with intent to procure conviction of a capital offence | `chapter-11-false-evidence.l4` |
| 195 | Giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment | `chapter-11-false-evidence.l4` |
| 196 | Using evidence known to be false | `chapter-11-false-evidence.l4` |
| 197 | Issuing or signing a false certificate | `chapter-11-false-evidence.l4` |
| 198 | Using as a true certificate one known to be false in a material point | `chapter-11-false-evidence.l4` |
| 199 | False statement made in any declaration which is by law receivable as evidence | `chapter-11-false-evidence.l4` |
| 200 | Using as true any such declaration known to be false | `chapter-11-false-evidence.l4` |
| 201 | Causing disappearance of evidence of an offence committed, or giving false information touching it, to screen the offender | `chapter-11-public-justice.l4` |
| 202 | Intentional omission to give information of an offence, by person bound to inform | `chapter-11-public-justice.l4` |
| 203 | Giving false information respecting an offence committed | `chapter-11-public-justice.l4` |
| 204 | Destruction of document or electronic record to prevent its production as evidence | `chapter-11-public-justice.l4` |
| 204A | Obstructing, preventing, perverting or defeating course of justice | `chapter-11-public-justice.l4` |
| 204B | Bribery of witnesses | `chapter-11-public-justice.l4` |
| 205 | False personation for the purpose of any act or proceeding in a suit | `chapter-11-public-justice.l4` |
| 206 | Fraudulent removal or concealment of property to prevent its seizure as a forfeiture, in execution of a decree or under or pursuant to an enforcement order | `chapter-11-public-justice.l4` |
| 207 | Fraudulent claim to property to prevent its seizure as a forfeiture, in execution of a decree or under or pursuant to an enforcement order | `chapter-11-public-justice.l4` |
| 208 | Fraudulently suffering a decree for a sum not due | `chapter-11-public-justice.l4` |
| 210 | Fraudulently obtaining a decree for a sum not due | `chapter-11-public-justice.l4` |
| 211 | False charge of offence made with intent to injure | `chapter-11-public-justice.l4` |
| 212 | Harbouring an offender | `chapter-11-public-justice.l4` |
| 213 | Taking gifts, etc., to screen an offender from punishment | `chapter-11-public-justice.l4` |
| 214 | Offering gift or restoration of property in consideration of screening offender | `chapter-11-public-justice.l4` |
| 215 | Taking gift to help to recover stolen property, etc. | `chapter-11-public-justice.l4` |
| 216 | Harbouring an offender who has escaped from custody, or whose apprehension has been ordered | `chapter-11-public-justice.l4` |
| 216A | Harbouring robbers or gang-robbers, etc. | `chapter-11-public-justice.l4` |
| 216B | "Harbour" | `chapter-11-public-justice.l4` |
| 217 | Public servant disobeying a direction of law with intent to save person from punishment or property from forfeiture | `chapter-11-public-justice.l4` |
| 218 | Public servant framing an incorrect record or writing with intent to save person from punishment, or property from forfeiture | `chapter-11-public-justice.l4` |
| 219 | Public servant in a judicial proceeding making an order, etc., which he knows to be contrary to law | `chapter-11-public-justice.l4` |
| 220 | Commitment for trial or confinement by person having authority who knows he is acting contrary to law | `chapter-11-public-justice.l4` |
| 221 | Intentional omission to apprehend on the part of a public servant bound by law to apprehend | `chapter-11-public-justice.l4` |
| 222 | Intentional omission to apprehend on the part of a public servant bound by law to apprehend person under sentence of a court of justice | `chapter-11-public-justice.l4` |
| 223 | Escape from confinement negligently suffered by a public servant | `chapter-11-public-justice.l4` |
| 224 | Resistance or obstruction by a person to his lawful apprehension | `chapter-11-public-justice.l4` |
| 225 | Resistance or obstruction to the lawful apprehension of another person | `chapter-11-public-justice.l4` |
| 225A | Public servant omitting to apprehend or suffering other persons to escape in cases not already provided for | `chapter-11-public-justice.l4` |
| 225B | Resistance or obstruction to lawful apprehension, or escape, or rescue, in cases not otherwise provided for | `chapter-11-public-justice.l4` |
| 225C | Offences against laws of Singapore where no special punishment is provided | `chapter-11-public-justice.l4` |
| 228 | Intentional insult or interruption to a public servant sitting in any stage of a judicial proceeding or mediation or other alternative dispute resolution process | `chapter-11-public-justice.l4` |
| 229 | Personation of an assessor | `chapter-11-public-justice.l4` |

Repealed, nothing to encode: s 209, s 226, s 227.

### Chapter 12 — Offences relating to government stamps

9 of 9 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 255 | Counterfeiting a Government stamp | `chapter-12-government-stamps.l4` |
| 256 | Having possession of an instrument or material for the purpose of counterfeiting a Government stamp | `chapter-12-government-stamps.l4` |
| 257 | Making or selling an instrument for the purpose of counterfeiting a Government stamp | `chapter-12-government-stamps.l4` |
| 258 | Sale of counterfeit Government stamp | `chapter-12-government-stamps.l4` |
| 259 | Having possession of a counterfeit Government stamp | `chapter-12-government-stamps.l4` |
| 260 | Using as genuine a Government stamp known to be counterfeit | `chapter-12-government-stamps.l4` |
| 261 | Effacing any writing from a substance bearing a Government stamp, or removing from a document a stamp used for it, with intent to cause loss to Government | `chapter-12-government-stamps.l4` |
| 262 | Using a Government stamp known to have been before used | `chapter-12-government-stamps.l4` |
| 263 | Erasure of mark denoting that stamp has been used | `chapter-12-government-stamps.l4` |

Repealed, nothing to encode: s 230, s 231, s 232, s 233, s 234, s 235, s 236, s 237, s 238, s 239, s 240, s 241, s 241A, s 242, s 243, s 243A, s 246, s 247, s 248, s 249, s 250, s 251, s 252, s 253, s 254, s 254A.

### Chapter 13 — *(wholly repealed)*

All 4 sections repealed. Nothing to encode.

### Chapter 14 — Offences affecting the public tranquility, public health, safety, convenience, decency and morals

35 of 35 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 267A | Affray | `chapter-14-public-tranquility.l4` |
| 267B | Punishment for committing affray | `chapter-14-public-tranquility.l4` |
| 267C | Uttering words, making document, etc., containing incitement to violence, etc. | `chapter-14-public-tranquility.l4` |
| 268 | Public nuisance | `chapter-14-public-tranquility.l4` |
| 268A | Communicating false information of harmful thing | `chapter-14-public-tranquility.l4` |
| 268B | Placing or sending thing with intent to cause fear of harm | `chapter-14-public-tranquility.l4` |
| 268C | Placing or sending thing causing fear of harm | `chapter-14-public-tranquility.l4` |
| 269 | Negligent act likely to spread infection of any disease dangerous to life | `chapter-14-public-health-and-safety.l4` |
| 270 | Intentional or rash act likely to spread infection of any disease dangerous to life | `chapter-14-public-health-and-safety.l4` |
| 271 | Disobedience to a quarantine rule | `chapter-14-public-health-and-safety.l4` |
| 272 | Adulteration of food or drink which is intended for sale | `chapter-14-public-health-and-safety.l4` |
| 273 | Sale of noxious food or drink | `chapter-14-public-health-and-safety.l4` |
| 274 | Adulteration of drugs | `chapter-14-public-health-and-safety.l4` |
| 275 | Sale of adulterated drugs | `chapter-14-public-health-and-safety.l4` |
| 276 | Sale of any drug as a different drug or preparation | `chapter-14-public-health-and-safety.l4` |
| 277 | Fouling the water of a public spring or reservoir | `chapter-14-public-health-and-safety.l4` |
| 278 | Making atmosphere noxious to health | `chapter-14-public-health-and-safety.l4` |
| 279 | Rash driving or riding on a public way | `chapter-14-public-health-and-safety.l4` |
| 280 | Rash navigation of a vessel | `chapter-14-public-health-and-safety.l4` |
| 281 | Exhibition of a false light, mark or buoy | `chapter-14-public-health-and-safety.l4` |
| 282 | Conveying person by water for hire in a vessel overloaded or unsafe | `chapter-14-public-health-and-safety.l4` |
| 283 | Danger or obstruction in a public way or navigation | `chapter-14-public-health-and-safety.l4` |
| 284 | Rash or negligent conduct with respect to dangerous or harmful substance | `chapter-14-public-health-and-safety.l4` |
| 285 | Causing or contributing to risk of dangerous fire | `chapter-14-public-health-and-safety.l4` |
| 286 | Presumption of cause of fire | `chapter-14-public-health-and-safety.l4` |
| 287 | Rash or negligent conduct with respect to any machinery in possession or under charge of offender | `chapter-14-public-health-and-safety.l4` |
| 288 | Negligence in pulling down or repairing buildings | `chapter-14-public-health-and-safety.l4` |
| 289 | Negligence with respect to any animal | `chapter-14-public-health-and-safety.l4` |
| 290 | Punishment for public nuisance | `chapter-14-public-tranquility.l4` |
| 291 | Continuance of nuisance after injunction to discontinue | `chapter-14-public-tranquility.l4` |
| 292 | Sale of obscene objects, etc. | `chapter-14-obscenity.l4` |
| 292A | Possession, distribution, etc., of child sex-doll | `chapter-14-obscenity.l4` |
| 292B | Obscene object on online location | `chapter-14-obscenity.l4` |
| 293 | Sale, etc., of obscene objects to young person | `chapter-14-obscenity.l4` |
| 294 | Obscene acts | `chapter-14-obscenity.l4` |

### Chapter 15 — Offences relating to race

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 298 | Uttering words, etc., with deliberate intent to wound the racial feelings of any person | `chapter-15-race.l4` |
| 298A | Promoting enmity between different groups on grounds of race and doing acts prejudicial to maintenance of harmony | `chapter-15-race.l4` |

Repealed, nothing to encode: s 295, s 296, s 297.

### Chapter 16 — Offences affecting the human body

120 of 120 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 299 | Culpable homicide | `chapter-16-life.l4` |
| 300 | Murder | `chapter-16-life.l4` |
| 301 | Culpable homicide by causing the death of a person other than the person whose death was intended | `chapter-16-life.l4` |
| 302 | Punishment for murder [There is no section 303.] | `punishment-provisions.l4` |
| 304 | Punishment for culpable homicide not amounting to murder | `punishment-provisions.l4` |
| 304A | Causing death by rash or negligent act | `chapter-16-life.l4` |
| 304B | Causing death of child below 14 years of age, domestic worker or vulnerable person by sustained abuse | `chapter-16-life.l4` |
| 304C | Causing or allowing death of child below 14 years of age, domestic worker or vulnerable person in same household | `chapter-16-life.l4` |
| 305 | Abetment of suicide or attempted suicide of minor or person who lacks mental capacity | `chapter-16-life.l4` |
| 306 | Abetment of suicide or attempted suicide | `chapter-16-life.l4` |
| 307 | Attempt to murder | `chapter-16-life.l4` |
| 308 | Attempt to commit culpable homicide | `chapter-16-life.l4` |
| 308A | Causing death in furtherance of group’s object | `chapter-16-life.l4` |
| 308B | Concealment, desecration or disposal of corpse that impedes discovery, identification, criminal investigations or prosecutions | `chapter-16-life.l4` |
| 310 | Infanticide | `chapter-16-life.l4` |
| 311 | Punishment for infanticide | `punishment-provisions.l4` |
| 312 | Causing miscarriage | `chapter-16-unborn-and-infants.l4` |
| 313 | Causing miscarriage without woman’s consent | `chapter-16-unborn-and-infants.l4` |
| 314 | Death caused by act done with intent to cause miscarriage | `chapter-16-unborn-and-infants.l4` |
| 315 | Child destruction before, at or immediately after birth | `chapter-16-unborn-and-infants.l4` |
| 316 | Causing death of a quick unborn child by an act amounting to culpable homicide | `chapter-16-unborn-and-infants.l4` |
| 317 | Exposure and abandonment of a child below 12 years of age by parent or person having care of it | `chapter-16-unborn-and-infants.l4` |
| 318 | Concealment of birth by secret disposal of dead body | `chapter-16-unborn-and-infants.l4` |
| 319 | Hurt | `chapter-16-hurt.l4` |
| 320 | Grievous hurt   Current version as at 09 Sep 2026  PDF created date on: 09 Sep 2026 | `chapter-16-hurt.l4` |
| 321 | Voluntarily causing hurt | `chapter-16-hurt.l4` |
| 322 | Voluntarily causing grievous hurt | `chapter-16-hurt.l4` |
| 323 | Punishment for voluntarily causing hurt | `punishment-provisions.l4` |
| 323A | Punishment for voluntarily causing hurt which causes grievous hurt | `chapter-16-hurt.l4` |
| 324 | Voluntarily causing hurt by dangerous weapons or means | `chapter-16-hurt.l4` |
| 325 | Punishment for voluntarily causing grievous hurt | `punishment-provisions.l4` |
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
| 338 | Causing grievous hurt by an act which endangers life or the personal safety of others Wrongful restraint and wrongful confinement | `chapter-16-hurt.l4` |
| 339 | Wrongful restraint | `chapter-16-restraint-and-force.l4` |
| 340 | Wrongful confinement | `chapter-16-restraint-and-force.l4` |
| 341 | Punishment for wrongful restraint | `punishment-provisions.l4` |
| 342 | Punishment for wrongful confinement | `punishment-provisions.l4` |
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
| 363 | Punishment for kidnapping | `punishment-provisions.l4` |
| 363A | Punishment for abduction | `punishment-provisions.l4` |
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
| 375 | Rape | `chapter-16-sexual-general.l4`, `chapter-16-sexual-penetration.l4` |
| 376 | Sexual assault involving penetration | `chapter-16-sexual-general.l4`, `chapter-16-sexual-penetration.l4` |
| 376A | Sexual penetration of minor below 16 years of age | `chapter-16-sexual-general.l4`, `chapter-16-sexual-penetration.l4` |
| 376AA | Exploitative sexual penetration of minor of or above 16 but below 18 years of age | `chapter-16-sexual-penetration.l4` |
| 376B | Commercial sex with minor below 18 years of age | `chapter-16-sexual-general.l4`, `chapter-16-sexual-penetration.l4` |
| 376C | Commercial sex with minor below 18 years of age outside Singapore | `chapter-16-sexual-penetration.l4` |
| 376D | Tour outside Singapore for commercial sex with minor below | `chapter-16-sexual-penetration.l4` |
| 376E | Sexual grooming of minor below 16 years of age | `chapter-16-sexual-penetration.l4` |
| 376EA | Exploitative sexual grooming of minor of or above 16 but below 18 years of age | `chapter-16-sexual-penetration.l4` |
| 376EB | Sexual communication with minor below 16 years of age | `chapter-16-sexual-general.l4`, `chapter-16-sexual-penetration.l4` |
| 376EC | Exploitative sexual communication with minor of or above | `chapter-16-sexual-penetration.l4` |
| 376ED | Sexual activity or image in presence of minor below 16 years of age | `chapter-16-sexual-general.l4`, `chapter-16-sexual-penetration.l4` |
| 376EE | Exploitative sexual activity or image in presence of minor of or above 16 but below 18 years of age | `chapter-16-sexual-penetration.l4` |
| 376F | Procurement of sexual activity with person with mental disability | `chapter-16-sexual-penetration.l4` |
| 376G | Incest | `chapter-16-sexual-penetration.l4` |
| 376H | Procurement of sexual activity by deception or false representation | `chapter-16-sexual-penetration.l4` |
| 377 | Sexual penetration, etc., of a corpse | `chapter-16-sexual-penetration.l4` |
| 377B | Sexual penetration with living animal | `chapter-16-sexual-penetration.l4` |
| 377BA | Word or gesture intended to insult modesty of any person | `chapter-16-sexual-images.l4` |
| 377BB | Voyeurism | `chapter-16-sexual-images.l4` |
| 377BC | Distribution of voyeuristic image or recording | `chapter-16-sexual-images.l4` |
| 377BD | Possession of or gaining access to voyeuristic or intimate image or recording and production of intimate image or recording | `chapter-16-sexual-images.l4` |
| 377BE | Distributing or threatening to distribute intimate image or recording | `chapter-16-sexual-images.l4` |
| 377BF | Sexual exposure | `chapter-16-sexual-images.l4` |
| 377BG | Using or involving child in production of child abuse material | `chapter-16-sexual-images.l4` |
| 377BH | Producing child abuse material | `chapter-16-sexual-images.l4` |
| 377BI | Distributing or selling child abuse material | `chapter-16-sexual-images.l4` |
| 377BJ | Advertising or seeking child abuse material | `chapter-16-sexual-images.l4` |
| 377BK | Possession of or gaining access to child abuse material | `chapter-16-sexual-images.l4` |
| 377BL | Exploitation by abusive material of minor of or above 16 but below 18 years of age | `chapter-16-sexual-images.l4` |
| 377BM | Defences to offences relating to intimate image or recording and voyeurism | `chapter-16-sexual-images.l4` |
| 377BN | Defences to child abuse material offences | `chapter-16-sexual-images.l4` |
| 377BO | Child abuse material offences outside or partially outside Singapore | `chapter-16-sexual-images.l4` |
| 377C | Interpretation of sections 375 to 377BO (sexual offences) | `chapter-16-sexual-general.l4` |
| 377CA | Meaning of exploitative relationship | `chapter-16-sexual-general.l4` |
| 377CB | Consent given under misconception in sexual offences | `chapter-16-sexual-general.l4` |
| 377D | Mistake as to age in sexual offences | `chapter-16-sexual-general.l4` |

Repealed, nothing to encode: s 309, s 343, s 344, s 364A, s 369, s 377A.

### Chapter 17 — Offences against property

76 of 76 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 378 | Theft | `chapter-17-property.l4` |
| 379 | Punishment for theft | `punishment-provisions.l4` |
| 379A | Punishment for theft of a motor vehicle | `punishment-provisions.l4` |
| 380 | Theft in dwelling house, etc. | `chapter-17-extortion-and-robbery.l4` |
| 381 | Theft by clerk or servant of property in possession of master | `chapter-17-extortion-and-robbery.l4` |
| 382 | Theft after preparation made for causing death or hurt in order to commit theft | `chapter-17-extortion-and-robbery.l4` |
| 383 | Extortion     Current version as at 09 Sep 2026  PDF created date on: 09 Sep 2026 | `chapter-17-extortion-and-robbery.l4` |
| 384 | Punishment for extortion | `punishment-provisions.l4` |
| 385 | Putting person in fear of harm in order to commit extortion | `chapter-17-extortion-and-robbery.l4` |
| 386 | Extortion by putting a person in fear of death or grievous hurt | `chapter-17-extortion-and-robbery.l4` |
| 387 | Putting person in fear of death or of grievous hurt in order to commit extortion | `chapter-17-extortion-and-robbery.l4` |
| 388 | Extortion by threat of accusation of an offence punishable with death, or imprisonment, etc. | `chapter-17-extortion-and-robbery.l4` |
| 389 | Putting person in fear of accusation of offence, in order to commit extortion | `chapter-17-extortion-and-robbery.l4` |
| 390 | Robbery | `chapter-17-extortion-and-robbery.l4` |
| 391 | Gang-robbery | `chapter-17-extortion-and-robbery.l4` |
| 392 | Punishment for robbery | `punishment-provisions.l4` |
| 393 | Attempt to commit robbery | `chapter-17-extortion-and-robbery.l4` |
| 394 | Voluntarily causing hurt in committing robbery | `chapter-17-extortion-and-robbery.l4` |
| 395 | Punishment for gang-robbery | `punishment-provisions.l4` |
| 396 | Gang-robbery with murder | `chapter-17-extortion-and-robbery.l4` |
| 397 | Robbery when armed or with attempt to cause death or grievous hurt | `chapter-17-extortion-and-robbery.l4` |
| 399 | Making preparation to commit gang-robbery | `chapter-17-extortion-and-robbery.l4` |
| 400 | Punishment for belonging to gang-robbers | `chapter-17-extortion-and-robbery.l4` |
| 401 | Punishment for belonging to gang of thieves | `chapter-17-extortion-and-robbery.l4` |
| 402 | Assembling for purpose of committing gang-robbery Criminal misappropriation of property | `chapter-17-extortion-and-robbery.l4` |
| 403 | Dishonest misappropriation of property | `chapter-17-property.l4` |
| 404 | Dishonest misappropriation of property possessed by a deceased person at the time of his death Criminal breach of trust | `chapter-17-stolen-property.l4` |
| 405 | Criminal breach of trust | `chapter-17-property.l4` |
| 406 | Punishment of criminal breach of trust | `punishment-provisions.l4` |
| 407 | Criminal breach of trust of property entrusted for purposes of transportation or storage | `chapter-17-stolen-property.l4` |
| 408 | Criminal breach of trust by employees | `chapter-17-stolen-property.l4` |
| 409 | Criminal breach of trust by public servant, or by banker, merchant, agent, director, officer, partner, key executive or fiduciary Receiving stolen property | `chapter-17-stolen-property.l4` |
| 410 | Stolen property | `chapter-17-stolen-property.l4` |
| 411 | Receiving stolen property | `chapter-17-stolen-property.l4` |
| 412 | Receiving property stolen in the commission of a gang-robbery | `chapter-17-stolen-property.l4` |
| 413 | Habitually dealing in stolen property | `chapter-17-stolen-property.l4` |
| 414 | Assisting in concealment or disposal of stolen property Cheating | `chapter-17-stolen-property.l4` |
| 415 | Cheating | `chapter-17-cheating.l4` |
| 416 | Cheating by personation | `chapter-17-cheating.l4` |
| 416A | Illegally obtained personal information | `chapter-17-fraud.l4` |
| 416B | Cheating by remote communication | `chapter-17-cheating.l4` |
| 417 | Punishment for cheating | `punishment-provisions.l4` |
| 418 | Cheating with knowledge that wrongful loss may be thereby caused to a person whose interest the offender is bound to protect | `chapter-17-cheating.l4` |
| 419 | Punishment for cheating by personation | `punishment-provisions.l4` |
| 420 | Cheating and dishonestly inducing a delivery of property | `chapter-17-cheating.l4` |
| 420A | Obtaining services dishonestly or fraudulently Fraudulent deeds and dispositions of property | `chapter-17-cheating.l4` |
| 421 | Dishonest or fraudulent removal or concealment of property to prevent distribution among creditors | `chapter-17-mischief-and-trespass.l4` |
| 422 | Dishonestly or fraudulently preventing a debt or demand due to the offender from being made available for his creditors | `chapter-17-mischief-and-trespass.l4` |
| 423 | Dishonest or fraudulent execution of deed of transfer containing a false statement of consideration | `chapter-17-mischief-and-trespass.l4` |
| 424 | Dishonest or fraudulent removal or concealment of property or release of claim | `chapter-17-mischief-and-trespass.l4` |
| 424A | Fraud by false representation, non-disclosure or abuse of position not connected with contracts for goods or services | `chapter-17-fraud.l4` |
| 424B | Fraud by false representation, non-disclosure or abuse of position | `chapter-17-fraud.l4` |
| 425 | Mischief | `chapter-17-mischief-and-trespass.l4` |
| 426 | Punishment for committing mischief | `punishment-provisions.l4` |
| 427 | Punishment for committing mischief causing disruption to key service, etc. | `chapter-17-mischief-and-trespass.l4` |
| 428 | Mischief by killing or maiming any animal | `chapter-17-mischief-and-trespass.l4` |
| 435 | Mischief by fire or explosive substance with intent to cause damage | `chapter-17-mischief-and-trespass.l4` |
| 436 | Mischief by fire or explosive substance with intent to destroy a house, etc. | `chapter-17-mischief-and-trespass.l4` |
| 437 | Mischief with intent to destroy or make unsafe a decked vessel or a vessel of 20 tons burden | `chapter-17-mischief-and-trespass.l4` |
| 438 | Punishment for the mischief described in section 437 when committed by fire or any explosive substance | `chapter-17-mischief-and-trespass.l4` |
| 439 | Punishment for intentionally running vessel aground or ashore with intent to commit theft, etc. | `chapter-17-mischief-and-trespass.l4` |
| 440 | Mischief committed after preparation made for causing death or hurt Criminal trespass | `chapter-17-mischief-and-trespass.l4` |
| 441 | Criminal trespass | `chapter-17-mischief-and-trespass.l4` |
| 442 | House-breaking | `chapter-17-mischief-and-trespass.l4` |
| 447 | Punishment for criminal trespass | `punishment-provisions.l4` |
| 448 | Punishment for house-breaking | `punishment-provisions.l4` |
| 449 | House-breaking in order to commit an offence punishable with death | `chapter-17-mischief-and-trespass.l4` |
| 450 | House-breaking in order to commit an offence punishable with imprisonment for life | `chapter-17-mischief-and-trespass.l4` |
| 451 | House-breaking in order to commit an offence punishable with imprisonment | `chapter-17-mischief-and-trespass.l4` |
| 452 | House-breaking after preparation made for causing hurt, etc. | `chapter-17-mischief-and-trespass.l4` |
| 453 | Possession of house-breaking implements or offensive weapons | `chapter-17-mischief-and-trespass.l4` |
| 458A | Punishment for subsequent offence under section 449, 450, 451 or 452 | `punishment-provisions.l4` |
| 459 | Grievous hurt caused while committing house-breaking | `chapter-17-mischief-and-trespass.l4` |
| 460 | House-breaking when death or grievous hurt caused | `chapter-17-mischief-and-trespass.l4` |
| 461 | Dishonestly breaking open any closed receptacle containing or supposed to contain property | `chapter-17-mischief-and-trespass.l4` |
| 462 | Punishment for same offence when committed by person entrusted with custody | `chapter-17-mischief-and-trespass.l4` |

Repealed, nothing to encode: s 429, s 430, s 430A, s 431, s 431A, s 432, s 433, s 434, s 443, s 444, s 445, s 446, s 454, s 455, s 456, s 457, s 458.

### Chapter 18 — Offences relating to documents or electronic records, false instruments, and to currency and bank notes

28 of 28 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 463 | Forgery | `chapter-18-forgery.l4` |
| 464 | Making a false document or false electronic record | `chapter-18-forgery.l4` |
| 465 | Punishment for forgery | `punishment-provisions.l4` |
| 466 | Forgery of a record of a court of justice, or a public register of births, etc. | `chapter-18-forged-documents.l4` |
| 467 | Forgery of a valuable security or will | `chapter-18-forged-documents.l4` |
| 468 | Forgery for the purpose of cheating | `chapter-18-forged-documents.l4` |
| 469 | Forgery for the purpose of harming the reputation of any person | `chapter-18-forged-documents.l4` |
| 470 | "A forged document" or "a forged electronic record" | `chapter-18-forged-documents.l4` |
| 471 | Using as genuine a forged document or forged electronic record | `chapter-18-forged-documents.l4` |
| 472 | Making or possessing a counterfeit seal, plate, etc., with intent to commit a forgery punishable under section 467 | `chapter-18-forged-documents.l4` |
| 473 | Making or possessing a counterfeit seal, plate, etc., with intent to commit a forgery punishable otherwise | `chapter-18-forged-documents.l4` |
| 473A | Making or possessing equipment for making a false instrument | `chapter-18-forged-documents.l4` |
| 473B | Making or possessing equipment for making a false instrument with intent to induce prejudice | `chapter-18-forged-documents.l4` |
| 473C | Meaning of "prejudice" and "induce" | `chapter-18-forged-documents.l4` |
| 474 | Having possession of certain document or electronic record known to be forged, with intent to use it as genuine | `chapter-18-forged-documents.l4` |
| 475 | Counterfeiting a device or mark used for authenticating documents described in section 467, or possessing counterfeit marked material | `chapter-18-forged-documents.l4` |
| 476 | Counterfeiting a device or mark used for authenticating documents or electronic records other than those described in section 467, or possessing counterfeit marked material | `chapter-18-forged-documents.l4` |
| 477 | Fraudulent cancellation, destruction, etc., of a will | `chapter-18-forged-documents.l4` |
| 477A | Falsification of accounts | `chapter-18-forged-documents.l4` |
| 489A | Forging or counterfeiting currency or bank notes | `chapter-18-currency.l4` |
| 489B | Using as genuine forged or counterfeit currency or bank notes | `chapter-18-currency.l4` |
| 489C | Possession of forged or counterfeit currency or bank notes | `chapter-18-currency.l4` |
| 489D | Making or possessing instruments or materials for forging or counterfeiting currency or bank notes | `chapter-18-currency.l4` |
| 489E | Abetting in Singapore counterfeiting of currency out of Singapore | `chapter-18-currency.l4` |
| 489F | Fraudulently or dishonestly diminishing weight or altering composition of any coin | `chapter-18-currency.l4` |
| 489G | Altering appearance of currency with intent that it shall pass as currency of different description | `chapter-18-currency.l4` |
| 489H | Delivery to another of altered currency | `chapter-18-currency.l4` |
| 489I | Possession of altered currency | `chapter-18-currency.l4` |

### Chapter 20 — *(wholly repealed)*

All 5 sections repealed. Nothing to encode.

### Chapter 21 — Defamation

4 of 4 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 499 | Defamation     Current version as at 09 Sep 2026  PDF created date on: 09 Sep 2026 | `chapter-21-22-speech.l4` |
| 500 | Punishment for defamation | `punishment-provisions.l4` |
| 501 | Printing or engraving matter known to be defamatory | `chapter-21-22-speech.l4` |
| 502 | Sale of printed or engraved substance containing defamatory matter | `chapter-21-22-speech.l4` |

### Chapter 22 — Criminal intimidation, insult and annoyance

5 of 5 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 503 | Criminal intimidation | `chapter-21-22-speech.l4` |
| 504 | Intentional insult with intent to provoke a breach of the peace | `chapter-21-22-speech.l4` |
| 505 | Statements conducing to public mischief | `chapter-21-22-speech.l4` |
| 506 | Punishment for criminal intimidation | `chapter-21-22-speech.l4` |
| 507 | Criminal intimidation by an anonymous communication | `chapter-21-22-speech.l4` |

Repealed, nothing to encode: s 508, s 509, s 510.

### Chapter 23 — Attempts to commit offences

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 511 | Attempt to commit offence | `chapter-23-attempts.l4` |
| 512 | Punishment for attempting to commit offences | `punishment-provisions.l4` |

## 5. Chapters with nothing encoded

None. Every chapter with a live section has every one of them encoded. Until 15 Sep 2026
this section listed eleven chapters and 168 live sections, and until 16 Sep seven sections
stood outside the count; the history is in the git log and in `missing-sections.md` §1.

## 6. The gaps that were more than scope choices — and what closing the rest changed

**6.1 to 6.3, closed 11 Sep 2026.** Chapter 4A, the right of private defence, was the one
absence that distorted the screen's answers: with twenty Chapter 4 exceptions and no
private-defence rule, an act a court would hold justified under s 96 still came back as an
indicated offence. All twelve sections were encoded and wired into every offence wrapper
through `the act is taken outside offence by Chapter 4 or Chapter 4A`. ss 111, 113 and 114
of Chapter 5 -- the abettor's liability for a different act, a different effect, and when
present -- were encoded with their Illustrations as assertions. ss 3, 4A and 5 of Chapter 1
widened the territorial screen to the Code's actual reach.

**6.4 Two things the completion pass closed that the earlier registers had flagged.**

- **s 4A** took the Chapter 6 / Chapter 6B classification as a caller-asserted fact, neither
  chapter being encoded. Both now are, and `agent-compliance.l4` decides
  `the act is deemed committed in Singapore under section 4A on the encoded tests` from
  `a Chapter 6 offence is made out` and `constitutes genocide`, alongside the asserted route.
- **Items 1 and 2 of the Schedule to s 4B** -- ss 268A to 268C, the hoax offences -- were the
  only specified offences the s 4B classifier could not compute. They are in
  `chapter-14-public-tranquility.l4`, and the classifier now reaches every item but the
  open-ended item 15.

**6.5 What the completion pass did not change.** `there is a section 97(a) right to defend
the body` still takes "an offence affecting the human body" as a caller-asserted fact rather
than computing it from the hurt rules, for the reason `verification-register-pass-4.md` §T3
gives: the offence is the assailant's, and the `Proposed Act` bundle carries one actor's
facts. Every section is encoded; that structural limit is not a section.

**6.6 What the closing pass changed.** s 79A had been the one section a range citation
swallowed without a rule, and the one closure provision left undecided where s 5 was decided.
It now has two rules and a screen field, and the hand exclusion in the method note above is
gone. s 49 gives the encoding its first unit conversion between the years of the `Punishment`
record and the months of s 40(3). The other five add nothing an offence test calls.

## 7. How to regenerate this register

Parse every line beginning `@ref` in `*.l4` for section numbers, expanding `ss X, Y, Z` lists
and `ss X to Y` ranges and stripping parenthesised subsections; parse the arrangement of
sections from the head of `registers/source-bundle/PC1871.txt`; match. Roughly 100 lines of
script. It is not committed here for the same reason the machine checker is not: this
repository holds law, and tooling belongs in `l4-ide`. `missing-sections.md` §4 records the
three parsing traps that each silently changed the counts when missing.

A section acquiring or losing an `@ref` changes these counts, so re-run this whenever modules
are added or citations edited. Counts here are current as at the closing pass of
16 Sep 2026, and were reproduced on that day by a fresh 60-line parse of the body of the
Act rather than of its arrangement of sections -- the two agree on 600, 75 and 525.
