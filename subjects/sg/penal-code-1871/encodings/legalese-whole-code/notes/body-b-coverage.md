# body-b coverage - Penal Code 1871, Chapter 16, ss 359-377D

Group "body-b": Chapter 16 from the heading "Kidnapping, abduction, slavery and forced labour" to the end of Chapter 16.
Source: `inputs/PC1871.txt` lines 7956-10212.
Status as at the end of this session: 29 of 57 rows landed (26 encoded or partly encoded, 3 repealed), 28 deferred for time.
Run: `deposit/check.sh` over `pc-body-b-kidnapping.l4`, `pc-body-b-sexual.l4`, `pc-body-b-tests.l4` (with `pc-domain`, `pc-general`) prints 0 errors, 123 assertions satisfied, 0 failed; a positive control (one false `#ASSERT` appended to a copy) printed 1 error, 1 failed.

Modules: `deposit/pc-body-b-kidnapping.l4` (ss 359-374, plus the age helpers), `deposit/pc-body-b-sexual.l4` (ss 375-377D; imports the first), `deposit/pc-body-b-tests.l4`.
There is no `pc-body-b.l4`: the group is split into two parts as BRIEF.md permits.

Facts records: `Kidnapping Facts` (ss 359-368), `Slavery and Forced Labour Facts` (ss 370-374), `Sexual Penetration Facts` (ss 375, 376, 376A, 376AA, with s 377D), `Insult to Modesty Facts` (s 377BA); drill-down records `Exploitative Relationship Facts` (s 377CA) and `Misconception Facts` (s 377CB).

Illustrations not expressed as tests: none in the encoded sections except s 377C's (a private act in an open-concept shower), which belongs to s 377BB (deferred).

| s | heading | disposition | functions |
| --- | --- | --- | --- |
| 359 | Kidnapping | encoded (definition; no charge of its own - ss 363/363A punish) | `kidnaps`, `kidnaps or abducts` (pc-body-b-kidnapping.l4) |
| 360 | Kidnapping from Singapore | encoded (definition; punished by s 363) | `kidnaps from Singapore` |
| 361 | Kidnapping from lawful guardianship | encoded (definition, Explanation, Exception; punished by s 363) | `kidnaps from lawful guardianship`, `the section 361 Exception applies` |
| 362 | Abduction | encoded (definition; punished by s 363A) | `abducts` |
| 363 | Punishment for kidnapping | encoded | `offence under s 363`, `charge under s 363`, `punishment prescribed by s 363` |
| 363A | Punishment for abduction | encoded | `offence under s 363A`, `charge under s 363A`, `punishment prescribed by s 363A` |
| 364 | Kidnapping or abducting in order to murder | encoded; Illustrations (a), (b) are tests | `offence under s 364`, `charge under s 364`, `punishment prescribed by s 364` |
| 364A | (Repealed) | repealed (Act 19 of 2010); comment in place |  |
| 365 | Kidnapping or abducting with intent secretly and wrongfully to confine a person | encoded | `offence under s 365`, `charge under s 365`, `punishment prescribed by s 365` |
| 366 | Kidnapping or abducting a woman to compel her marriage, etc. | encoded | `offence under s 366`, `charge under s 366`, `punishment prescribed by s 366` |
| 367 | Kidnapping or abducting in order to subject a person to grievous hurt, slavery, etc. | encoded; "grievous hurt" is a leaf owed to body-a (s 320) | `offence under s 367`, `charge under s 367`, `punishment prescribed by s 367` |
| 368 | Wrongfully concealing or keeping in confinement a kidnapped person | encoded; no Punishment record - the section borrows ss 363-367 (FORK B-6) | `offence under s 368`, `charge under s 368`, `the punishment of section 368` |
| 369 | (Repealed) | repealed (Act 15 of 2019); comment in place |  |
| 370 | Buying or disposing of any person as a slave | encoded | `offence under s 370`, `charge under s 370`, `punishment prescribed by s 370` |
| 371 | Habitual dealing in slaves | encoded | `offence under s 371`, `charge under s 371`, `punishment prescribed by s 371` |
| 372 | Selling minor for purposes of prostitution, etc. | deferred - time (age helper `below 21 years of age` and the Explanation presumption are ready to use) |  |
| 373 | Buying minor for purposes of prostitution, etc. | deferred - time (as s 372) |  |
| 373A | Importing woman for purposes of prostitution, etc. | deferred - time |  |
| 374 | Unlawful compulsory labour | encoded | `offence under s 374`, `charge under s 374`, `punishment prescribed by s 374` |
| 375 | Rape | encoded: (1), (1A), (2), (3), (4), (5), (6) | `commits rape`, `commits rape within section 375(1)`, `commits rape within section 375(1A)`, `without consent within section 375(a)`, `below 14 within section 375(b)`, `aggravated within section 375(3)`, `offence under s 375(2)`, `offence under s 375(3)`, `charge under s 375(2)`, `charge under s 375(3)` (pc-body-b-sexual.l4) |
| 376 | Sexual assault involving penetration | encoded: (2)-(6); (1) deleted (Act 23 of 2021) | `commits sexual assault by penetration within section 376(2)`, `offence under s 376(3)`, `offence under s 376(4)`, `charge under s 376(3)`, `charge under s 376(4)` |
| 376A | Sexual penetration of minor below 16 years of age | encoded: (1), (1A), (2)(a)/(b), (3), (4); (1B) inert (avoidance of doubt) | `commits sexual penetration of a minor below 16 within section 376A(1)`, `excluded from section 376A by section 376A(1A)`, `offence under s 376A(2)`, `offence under s 376A(3)`, `charge under s 376A(2)`, `charge under s 376A(3)` |
| 376AA | Exploitative sexual penetration of minor of or above 16 but below 18 years of age | encoded: (1), (3); (2) inert (consent immaterial); with s 377D(2)-(3) | `commits exploitative sexual penetration of a minor within section 376AA(1)`, `offence under s 376AA(3)`, `charge under s 376AA(3)` |
| 376B | Commercial sex with minor below 18 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376C | Commercial sex with minor below 18 years of age outside Singapore | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376D | Tour outside Singapore for commercial sex with minor below 18 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376E | Sexual grooming of minor below 16 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376EA | Exploitative sexual grooming of minor of or above 16 but below 18 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376EB | Sexual communication with minor below 16 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376EC | Exploitative sexual communication with minor of or above 16 but below 18 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376ED | Sexual activity or image in presence of minor below 16 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376EE | Exploitative sexual activity or image in presence of minor of or above 16 but below 18 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376F | Procurement of sexual activity with person with mental disability | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376G | Incest | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 376H | Procurement of sexual activity by deception or false representation | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377 | Sexual penetration, etc., of a corpse | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377A | (Repealed) | repealed (Act 39 of 2022); comment in place |  |
| 377B | Sexual penetration with living animal | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BA | Word or gesture intended to insult modesty of any person | encoded | `offence under s 377BA`, `charge under s 377BA`, `punishment prescribed by s 377BA` |
| 377BB | Voyeurism | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BC | Distribution of voyeuristic image or recording | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BD | Possession of or gaining access to voyeuristic or intimate image or recording and production of intimate image or recording | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BE | Distributing or threatening to distribute intimate image or recording | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BF | Sexual exposure | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BG | Using or involving child in production of child abuse material | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BH | Producing child abuse material | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BI | Distributing or selling child abuse material | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BJ | Advertising or seeking child abuse material | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BK | Possession of or gaining access to child abuse material | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BL | Exploitation by abusive material of minor of or above 16 but below 18 years of age | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BM | Defences to offences relating to intimate image or recording and voyeurism | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BN | Defences to child abuse material offences | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377BO | Child abuse material offences outside or partially outside Singapore | deferred - time (the most-charged offences were encoded first, per BRIEF.md) |  |
| 377C | Interpretation of sections 375 to 377BO (sexual offences) | partly encoded - as leaf @descs only (vagina includes vulva; surgically constructed parts; sex identification; "sexual"); the definitions of child abuse material, distribute, image, material, private act feed the deferred sections; its Illustration (private act) is untested because s 377BB is deferred |  |
| 377CA | Meaning of exploitative relationship | encoded: (2)-(3) presumption as a drill-down; (1) is a judgement for the court on four factors, read by the ladders as one leaf | `presumed exploitative within section 377CA(2)` |
| 377CB | Consent given under misconception in sexual offences | encoded (drill-down for the consent leaf); Illustrations (a)-(d) are tests | `not a consent within section 377CB` |
| 377D | Mistake as to age in sexual offences | encoded in s 376AA only: (1) is why no other ladder has a mistake-as-to-age leaf; (2)-(3) and the Explanation | `defence of mistaken belief as to age within section 377D(2)` |
