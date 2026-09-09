# Penal Code 1871 — coverage register

**Run date:** 2026-09-09
**Question answered:** which sections of the Act are modelled, and which are not.
**Method:** every `@ref` citation in the seventeen `.l4` modules was parsed for section
numbers and matched against the Act's own arrangement of sections, as it appears in
`registers/source-bundle/PC1871.txt` (SSO current version as at 09 Sep 2026). Multi-section
citations (`ss 45, 46, 47, 48`) and ranges (`ss 76 to 95`) are expanded; subsection numbers
in parentheses are stripped so that `s 120A(4) and (5)` does not read as sections 4 and 5.

This register is mechanical. It records that a section **has a rule carrying its citation**,
not that the rule is a correct or complete reading of it. Fidelity is a separate question,
answered in part by `registers/verification-register.md`.

---

## 1. Headline

| | sections |
| --- | ---: |
| listed in the Act's arrangement of sections | 600 |
| repealed — nothing to encode | 75 |
| **live** | **525** |
| **encoded** | **108** |
| **live but not encoded** | **417** |

**About 21% of the live sections.** There is no Chapter 19; Chapters 13 and 20 are wholly
repealed.

The distribution is the point. The Code's **general parts are close to complete**, and its
**offence chapters are a deliberate thin slice** — the provisions an AI agent is most likely
to walk into when checking its own output or a user's requested act. `NOTES.md` §2 states the
policy; this register states its consequences section by section.

## 2. By chapter

| chapter | ss | repealed | live | encoded | not encoded |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Chapter 1** — PRELIMINARY | 7 | 0 | 7 | 3 | 4 |
| **Chapter 2** — GENERAL EXPLANATIONS | 56 | 2 | 54 | 49 | 5 |
| **Chapter 3** — Punishments | 13 | 3 | 10 | 10 | 0 |
| **Chapter 4** — General Exceptions | 21 | 0 | 21 | 20 | 1 |
| **Chapter 4A** — Right of private defence | 12 | 0 | 12 | 0 | 12 |
| **Chapter 5** — Abetment | 16 | 0 | 16 | 4 | 12 |
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
| **Chapter 16** — Offences affecting the human body | 126 | 6 | 120 | 0 | 120 |
| **Chapter 17** — Offences against property | 93 | 17 | 76 | 12 | 64 |
| **Chapter 18** — Offences relating to documents, electronic records and marks | 28 | 0 | 28 | 2 | 26 |
| **Chapter 20** — *(wholly repealed)* | 5 | 5 | 0 | 0 | 0 |
| **Chapter 21** — Defamation | 4 | 0 | 4 | 1 | 3 |
| **Chapter 22** — Criminal intimidation, insult and annoyance | 8 | 3 | 5 | 4 | 1 |
| **Chapter 23** — Attempts to commit offences | 2 | 0 | 2 | 1 | 1 |
| **total** | **600** | **75** | **525** | **108** | **417** |

## 3. The general parts

Four chapters decide whether an offence test is reached at all, and these are the ones the
encoding treats as load-bearing:

| chapter | live | encoded |
| --- | ---: | ---: |
| Chapter 2 — General explanations | 54 | 49 |
| Chapter 3 — Punishments | 10 | 10 |
| Chapter 4 — General exceptions | 21 | 20 |
| Chapter 5A — Criminal conspiracy | 2 | 2 |

**The six apparent gaps there are deliberate, and each is documented in the module itself
under its own `§§` heading.** They are sections with no factual test to decide:

| s | why nothing is decided |
| --- | --- |
| 7 | Rule of construction addressed to the reader: an expression explained in one part is used in the same sense throughout. Honoured by the encoding's own discipline — one definition module per term, imported rather than restated. |
| 8 | "He" and its derivatives are used of any person. A drafting convention; this encoding writes gender-neutrally throughout. |
| 9 | Singular includes plural and plural singular unless the contrary appears. A drafting convention. |
| 49 | A year or month is reckoned by the Gregorian calendar. Every period in this encoding is Gregorian by construction. |
| 50 | "Section" denotes a numbered portion of a Chapter. |
| 79A | A **closure** rule, not an exception: mistake or ignorance of law is never a defence unless another written law so provides. It therefore contributes no limb to `a general exception applies`, which is the correct encoding of it. |

So Chapters 2, 3, 4 and 5A are complete in substance: every section that states a testable
rule has one.

## 4. Chapters partially encoded, section by section


### Chapter 1 — PRELIMINARY

3 of 7 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 2 | Punishment of offences committed within Singapore | `agent-compliance.l4` |
| 4 | Jurisdiction over public servants for offences committed outside | `agent-compliance.l4` |
| 4B | Punishment of specified offences with elements occurring in | `agent-compliance.l4` |

**Not encoded:** s 1, s 3, s 4A, s 5.

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

### Chapter 5 — Abetment

4 of 16 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 107 | Abetment of the doing of a thing | `chapter-5-abetment.l4` |
| 108 | Abettor | `chapter-5-abetment.l4` |
| 108A | Abetment in Singapore of an offence outside Singapore | `chapter-5-abetment.l4` |
| 108B | Abetment outside Singapore of an offence in Singapore | `chapter-5-abetment.l4` |

**Not encoded:** s 109, s 110, s 111, s 112, s 113, s 114, s 115, s 116, s 117, s 118, s 119, s 120.

### Chapter 5A — Criminal Conspiracy

2 of 2 live sections encoded.

| s | title | module |
| --- | --- | --- |
| 120A | Definition of criminal conspiracy | `chapter-5a-conspiracy.l4` |
| 120B | Punishment of criminal conspiracy | `chapter-5a-conspiracy.l4` |

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
| **Chapter 4A** — Right of private defence | 12 | ss 96–106A |
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
| **Chapter 16** — Offences affecting the human body | 120 | ss 299–377D |

**300 live sections, none of them modelled** — 57% of the live Code. Chapters 13 and 20 are
omitted from this table: both are wholly repealed and contribute no live section.

## 6. The three gaps that are more than scope choices

Most of §5 is honest scoping: an agent has no occasion to ask whether its output is piracy or
an offence relating to government stamps. Three absences are different, because a caller
could reasonably expect them to be there and be misled by their silence.

**6.1 Chapter 4A — the right of private defence (ss 96 to 106A).** This is the one that
distorts the screen's answers. The encoding models twenty Chapter 4 general exceptions and
**zero** private-defence rules, so `a general exception applies` cannot report a
private-defence justification. An act a court would hold justified under s 96 still comes back
from the screen as an indicated offence. The screen is therefore **over-inclusive on offences
and under-inclusive on defences**: a FALSE from `any screened offence is indicated` is more
trustworthy than a TRUE.

**6.2 Chapter 5, ss 109 to 120 — the rest of abetment.** ss 109, 110, 112, 115 to 120 are
punishment and concealment provisions, consistent with this subject not computing sentence.
But **ss 111, 113 and 114 are substantive liability rules** — the abettor's liability when a
*different* act from the one abetted results, when the act abetted causes a different effect,
and when the abettor is present at the commission. An agent reasoning about abetment from
ss 107 and 108 alone will not reach them.

**6.3 Chapter 1, ss 3, 4A and 5.** Further extraterritorial reach beyond the ss 2, 4 and 4B
that are encoded, including offences against the State and genocide committed outside
Singapore (s 4A) and the saving for other laws (s 5). The territorial screen is narrower than
the Code's actual reach.

## 7. How to regenerate this register

Parse every line beginning `@ref` in `*.l4` for section numbers, expanding `ss X, Y, Z` lists
and `ss X to Y` ranges and stripping parenthesised subsections; parse the arrangement of
sections from the head of `registers/source-bundle/PC1871.txt`; match. Roughly 40 lines of
script. It is not committed here for the same reason the machine checker is not: this
repository holds law, and tooling belongs in `l4-ide`.

A section acquiring or losing an `@ref` changes these counts, so re-run this whenever modules
are added or citations edited.
