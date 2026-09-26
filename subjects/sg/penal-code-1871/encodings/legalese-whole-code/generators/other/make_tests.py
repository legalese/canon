exec(open('gen_tests.py').read())
K='Kidnapping Facts'; SL='Slavery and Forced Labour Facts'; SP='Sexual Penetration Facts'; IM='Insult to Modesty Facts'; ER='Exploitative Relationship Facts'; MC='Misconception Facts'
out=[]
P=out.append
P('''-- Tests for group body-b: Penal Code 1871, Chapter 16, ss 359-377D.
--
-- Expected values come FROM THE SOURCE: the Code's own Illustrations first
-- (cited on the line above each), then boundary cases for every age
-- threshold on the NUMBER helpers, then one route through each limb.
-- The fixtures are generated (every field listed; FALSE / "" unless the case
-- says otherwise), so that each fixture reads as the facts of its case.
-- A failing assertion is a finding: none has been edited to match the code.

IMPORT prelude
IMPORT `pc-domain`
IMPORT `pc-general`
IMPORT `pc-body-b-kidnapping`
IMPORT `pc-body-b-sexual`

§ `body-b tests`

`the particulars` MEANS Particulars WITH
    accused            IS "Tan Ah Kow"
    date               IS "the 1st day of March 2025"
    time               IS "9.30 pm"
    place              IS "Block 123 Ang Mo Kio Avenue 3"
    `co-accused`       IS ""
    `common intention` IS FALSE

`the victim` MEANS Person WITH
    name           IS "Lim Mei Ling"
    `described as` IS ""
    pronoun        IS she
    kind           IS `a human being`

`Z` MEANS Person WITH
    name           IS "Z"
    `described as` IS ""
    pronoun        IS he
    kind           IS `a human being`

§§ `The age thresholds (PLAN s 3.5): both sides of every line`

#ASSERT `below 14 years of age` 13
#ASSERT NOT `below 14 years of age` 14
#ASSERT `below 16 years of age` 15
#ASSERT NOT `below 16 years of age` 16
#ASSERT NOT `of or above 14 years of age but below 16 years of age` 13
#ASSERT `of or above 14 years of age but below 16 years of age` 14
#ASSERT `of or above 14 years of age but below 16 years of age` 15
#ASSERT NOT `of or above 14 years of age but below 16 years of age` 16
#ASSERT NOT `of or above 16 years of age but below 18 years of age` 15
#ASSERT `of or above 16 years of age but below 18 years of age` 16
#ASSERT `of or above 16 years of age but below 18 years of age` 17
#ASSERT NOT `of or above 16 years of age but below 18 years of age` 18
#ASSERT `below 21 years of age` 20
#ASSERT NOT `below 21 years of age` 21

§§ `ss 359-368 - kidnapping and abduction`
''')
conv={'conveys the person beyond':True,'without the consent of that person':True,'legally authorised':True}
# s 364 illus (a)
P('-- s 364 illus (a): A kidnaps Z from Singapore, intending or knowing it to be likely that Z may be sacrificed to an idol.')
P(fixture('s 364 illus (a)',K,{**conv,'victim':'`Z`','where the person was conveyed':'Batam, Indonesia','in order that the person may be murdered':True}))
P('''-- s 364 illus (a): "A has committed the offence defined in this section."
#ASSERT `offence under s 364` `s 364 illus (a)`
#ASSERT `kidnaps from Singapore` `s 364 illus (a)`
#ASSERT (`charge under s 364` `s 364 illus (a)`)'s `made out`
-- every s 364 kidnapping is also a kidnapping punishable under s 363
#ASSERT `offence under s 363` `s 364 illus (a)`
#ASSERT NOT `offence under s 363A` `s 364 illus (a)`
''')
P('-- s 364 illus (b): A forcibly carries B away from his home in order that B may be murdered.')
P(fixture('s 364 illus (b), forcibly',K,{'victim':'`Z`','by force compels':True,'to go from any place':True,'the place from which':"his home at Block 5 Jalan Bukit Merah",'in order that the person may be murdered':True}))
P('-- s 364 illus (b): A entices B away from his home in order that B may be murdered (B taken here as a minor below 16 in his guardian\'s keeping - FORK B-3).')
P(fixture('s 364 illus (b), entices',K,{'victim':'`Z`','entices':True,'the person is a minor below 16 years of age':True,'out of the keeping of the lawful guardian':True,'without the consent of such guardian':True,'the lawful guardian':'one Tan Bee Hoon, his mother','in order that the person may be murdered':True}))
P('''-- s 364 illus (b): "A has committed the offence defined in this section."
#ASSERT `offence under s 364` `s 364 illus (b), forcibly`
#ASSERT abducts `s 364 illus (b), forcibly`
#ASSERT `offence under s 363A` `s 364 illus (b), forcibly`
#ASSERT NOT `offence under s 363` `s 364 illus (b), forcibly`
#ASSERT `offence under s 364` `s 364 illus (b), entices`
#ASSERT `kidnaps from lawful guardianship` `s 364 illus (b), entices`
''')
P('-- s 361: a child below 16 taken out of her mother\'s keeping without the mother\'s consent.')
P(fixture('child taken from her mother',K,{'takes':True,'the person is a minor below 16 years of age':True,'out of the keeping of the lawful guardian':True,'without the consent of such guardian':True,'the lawful guardian':'one Tan Bee Hoon, her mother'}))
P('''#ASSERT `offence under s 363` `child taken from her mother`
#ASSERT (`charge under s 363` `child taken from her mother`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did kidnap one Lim Mei Ling from lawful guardianship, to wit, by taking the said Lim Mei Ling, a minor below 16 years of age, out of the keeping of one Tan Bee Hoon, her mother, the lawful guardian of the said Lim Mei Ling, without the consent of such guardian, and you have thereby committed an offence punishable under section 363 of the Penal Code 1871."
#ASSERT (`charge under s 363` `child taken from her mother`)'s punishment EQUALS "imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning"
-- not abduction: no force, no deceit
#ASSERT NOT `offence under s 363A` `child taken from her mother`
''')
P('-- s 361 Exception: the taker in good faith believes himself to be the father of the (illegitimate) child.')
P(fixture('putative father',K,{'takes':True,'the person is a minor below 16 years of age':True,'out of the keeping of the lawful guardian':True,'without the consent of such guardian':True,'the father of an illegitimate child':True}))
P('-- s 361 Exception, proviso: ... unless such act is committed for an immoral or unlawful purpose.')
P(fixture('putative father, unlawful purpose',K,{'takes':True,'the person is a minor below 16 years of age':True,'out of the keeping of the lawful guardian':True,'without the consent of such guardian':True,'the father of an illegitimate child':True,'immoral or unlawful purpose':True}))
P('''#ASSERT `the section 361 Exception applies` `putative father`
#ASSERT NOT `offence under s 363` `putative father`
#ASSERT (`charge under s 363` `putative father`)'s refusal EQUALS "A charge under section 363 would assert that the facts fulfil every legal condition of kidnapping (CPC s 123(5)). On the facts given they do not: the act is not within the Exception to section 361; the elements of section 360 or section 361 taken together."
#ASSERT NOT `the section 361 Exception applies` `putative father, unlawful purpose`
#ASSERT `offence under s 363` `putative father, unlawful purpose`
''')
P('-- s 361: a person of 16 is not "a minor below 16 years of age"; with no unsoundness of mind there is no kidnapping from lawful guardianship.')
P(fixture('sixteen-year-old taken',K,{'takes':True,'the person is a minor below 16 years of age':'(`below 16 years of age` 16)','out of the keeping of the lawful guardian':True,'without the consent of such guardian':True}))
P('''#ASSERT NOT `offence under s 363` `sixteen-year-old taken`
''')
P('-- s 360: conveyed out of Singapore with the consent of a person legally authorised to consent on the person\'s behalf.')
P(fixture('conveyed with authorised consent',K,{'conveys the person beyond':True,'without the consent of that person':True}))
P('''#ASSERT NOT `kidnaps from Singapore` `conveyed with authorised consent`
''')
P('-- s 362: abduction by deceitful means.')
P(fixture('lured by deceit',K,{'by any deceitful means induces':True,'to go from any place':True,'the place from which':'the void deck of Block 123 Ang Mo Kio Avenue 3','the deceitful means':'by falsely telling her that her mother had been taken to hospital'}))
P('''#ASSERT `offence under s 363A` `lured by deceit`
#ASSERT (`charge under s 363A` `lured by deceit`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did abduct one Lim Mei Ling, to wit, by deceitful means, to wit, by falsely telling her that her mother had been taken to hospital, inducing her to go from the void deck of Block 123 Ang Mo Kio Avenue 3, and you have thereby committed an offence punishable under section 363A of the Penal Code 1871."
''')
P('-- s 362: force used, but the person did not go from any place: no abduction, and the refusal says so.')
P(fixture('force but no going',K,{'by force compels':True}))
P('''#ASSERT NOT `offence under s 363A` `force but no going`
#ASSERT (`charge under s 363A` `force but no going`)'s refusal EQUALS "A charge under section 363A would assert that the facts fulfil every legal condition of abduction (CPC s 123(5)). On the facts given they do not: any person to go from any place; the elements of section 362 taken together."
''')
P('-- ss 365, 366, 367: the aggravated purposes, over a forcible abduction.')
ab={'by force compels':True,'to go from any place':True,'the place from which':'Changi Village'}
P(fixture('abducted to be confined',K,{**ab,'secretly and wrongfully confined':True}))
P(fixture('woman abducted to be married',K,{**ab,'the person is a woman':True,'with intent that she may be compelled to marry':True}))
P(fixture('man abducted to be married',K,{**ab,'with intent that she may be compelled to marry':True}))
P(fixture('abducted to be enslaved',K,{**ab,'to slavery':True,'the harm intended':'slavery'}))
P(fixture('abducted, no purpose',K,{**ab}))
P('''#ASSERT `offence under s 365` `abducted to be confined`
#ASSERT NOT `offence under s 366` `abducted to be confined`
#ASSERT `offence under s 366` `woman abducted to be married`
-- s 366 reads "any woman": the same facts against a man are not s 366
#ASSERT NOT `offence under s 366` `man abducted to be married`
#ASSERT `offence under s 367` `abducted to be enslaved`
#ASSERT (`charge under s 367` `abducted to be enslaved`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did abduct one Lim Mei Ling, to wit, by force compelling her to go from Changi Village, in order that the said Lim Mei Ling may be subjected to slavery, and you have thereby committed an offence punishable under section 367 of the Penal Code 1871."
#ASSERT NOT `offence under s 364` `abducted, no purpose`
#ASSERT NOT `offence under s 365` `abducted, no purpose`
#ASSERT NOT `offence under s 367` `abducted, no purpose`
#ASSERT `offence under s 363A` `abducted, no purpose`
''')
P('-- s 368: knowing she had been abducted, the accused kept her in confinement.')
P(fixture('kept the abducted woman',K,{'knowing that the person has been kidnapped':True,'wrongfully keeps such person in confinement':True}))
P(fixture('kept her, not knowing',K,{'wrongfully keeps such person in confinement':True}))
P('''#ASSERT `offence under s 368` `kept the abducted woman`
#ASSERT NOT `offence under s 368` `kept her, not knowing`
#ASSERT (`charge under s 368` `kept her, not knowing`)'s refusal EQUALS "A charge under section 368 would assert that the facts fulfil every legal condition of wrongfully concealing or keeping in confinement a kidnapped person (CPC s 123(5)). On the facts given they do not: knowing that any person has been kidnapped or has been abducted."

-- punishments as data
#ASSERT `punishable with death or imprisonment for life` `punishment prescribed by s 364`
#ASSERT NOT `punishable with death or imprisonment for life` `punishment prescribed by s 363`
#ASSERT `punishable with imprisonment for` 120 `months or upwards within section 41` `punishment prescribed by s 363`
#ASSERT NOT `punishable with imprisonment for` 121 `months or upwards within section 41` `punishment prescribed by s 363`

§§ `ss 370-374 - slavery and forced labour`
''')
P(fixture('sold as a slave',SL,{'imports, exports, removes, buys, sells or disposes':True,'the dealing':'sell one Lim Mei Ling as a slave to one Ong Beng Huat'}))
P(fixture('domestic worker compelled',SL,{'unlawfully compels the person to labour':True,'against the will of that person':True,'the labour':'by confining her to the flat and making her work without rest days'}))
P(fixture('willing worker',SL,{'unlawfully compels the person to labour':True}))
P('''#ASSERT `offence under s 370` `sold as a slave`
#ASSERT NOT `offence under s 371` `sold as a slave`
#ASSERT `offence under s 374` `domestic worker compelled`
#ASSERT (`charge under s 374` `domestic worker compelled`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did unlawfully compel one Lim Mei Ling to labour against her will, to wit, by confining her to the flat and making her work without rest days, and you have thereby committed an offence punishable under section 374 of the Penal Code 1871."
#ASSERT NOT `offence under s 374` `willing worker`
#ASSERT `punishable with death or imprisonment for life` `punishment prescribed by s 371`

§§ `ss 375-376AA - sexual penetration`
''')
base={'the accused is a man':True,'the victim is a woman':True,"penetrates the vagina of the victim with the accused's penis":True,'the act of penetration':'penetrate the vagina of one Lim Mei Ling with your penis'}
P('-- s 375(1)(a): penile penetration of an adult woman without her consent.')
P(fixture('rape of an adult',SP,{**base,"without the victim's consent":True}))
P('''#ASSERT `commits rape within section 375(1)` `rape of an adult`
#ASSERT `offence under s 375(2)` `rape of an adult`
#ASSERT NOT `offence under s 375(3)` `rape of an adult`
#ASSERT (`charge under s 375(2)` `rape of an adult`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did penetrate the vagina of one Lim Mei Ling with your penis, without her consent, and you have thereby committed an offence punishable under section 375(2) of the Penal Code 1871."
-- s 376A(1A): an act that would constitute s 375(1)(a) is not s 376A (and she is an adult anyway)
#ASSERT NOT `offence under s 376A(2)` `rape of an adult`
#ASSERT NOT `offence under s 376A(3)` `rape of an adult`
''')
P('-- s 375(5): he proves a mistake of fact in good faith that she consented.')
P(fixture('rape, mistake as to consent proved',SP,{**base,"without the victim's consent":True,'believed that the act was done with consent':True}))
P('''#ASSERT NOT `offence under s 375(2)` `rape, mistake as to consent proved`
''')
P('-- s 375(1)(b): she is 13 and consents; he is not her husband.')
P(fixture('girl of 13 consenting',SP,{**base,'the victim is below 14 years of age':'(`below 14 years of age` 13)'}))
P('''#ASSERT `offence under s 375(2)` `girl of 13 consenting`
#ASSERT NOT `offence under s 375(3)` `girl of 13 consenting`
-- s 376A(1A) excludes only 375(1)(b) READ WITH 375(3); unaggravated 375(1)(b) is not excluded, so s 376A(3) is also made out
#ASSERT NOT `excluded from section 376A by section 376A(1A)` `girl of 13 consenting`
#ASSERT `offence under s 376A(3)` `girl of 13 consenting`
''')
P('-- s 375(4) and s 376A(4): she is 13, his wife, and consents.')
P(fixture('wife of 13 consenting',SP,{**base,'the victim is below 14 years of age':True,"the victim is the accused's spouse":True}))
P('''#ASSERT NOT `offence under s 375(2)` `wife of 13 consenting`
#ASSERT NOT `offence under s 376A(3)` `wife of 13 consenting`
''')
P('-- s 375(3)(b): she is 13 and does not consent.')
P(fixture('girl of 13 not consenting',SP,{**base,'the victim is below 14 years of age':True,"without the victim's consent":True}))
P('''#ASSERT `offence under s 375(3)` `girl of 13 not consenting`
#ASSERT (`charge under s 375(3)` `girl of 13 not consenting`)'s punishment EQUALS "imprisonment for a term of not less than 8 years and not more than 20 years and shall also be punished with caning of not less than 12 strokes"
#ASSERT `fixed by law or carries a minimum sentence` `punishment prescribed by s 375(3)`
#ASSERT NOT `fixed by law or carries a minimum sentence` `punishment prescribed by s 375(2)`
-- s 376A(1A): 375(1)(a) is made out, so s 376A does not apply
#ASSERT NOT `offence under s 376A(3)` `girl of 13 not consenting`
''')
P('-- s 375(6): as above, but he proves he believed in good faith that she consented: not punishable under (3)(b); (1)(b) still stands.')
P(fixture('girl of 13, mistake as to consent proved',SP,{**base,'the victim is below 14 years of age':True,"without the victim's consent":True,'believed that the act was done with consent':True,'against a person below 14 years of age was done with consent':True}))
P('''#ASSERT NOT `offence under s 375(3)` `girl of 13, mistake as to consent proved`
#ASSERT `offence under s 375(2)` `girl of 13, mistake as to consent proved`
''')
P('-- s 375(3)(a): hurt caused to facilitate the rape of an adult.')
P(fixture('rape with hurt',SP,{**base,"without the victim's consent":True,'voluntarily causes hurt to any person':True}))
P('''#ASSERT `offence under s 375(3)` `rape with hurt`
#ASSERT (`charge under s 375(3)` `rape with hurt`)'s `made out`
''')
P('-- s 375(1A): penile penetration of the mouth of a man, without consent.')
P(fixture('oral penetration of a man',SP,{'the accused is a man':True,"penetrates the anus or mouth of the victim with the accused's penis":True,"without the victim's consent":True}))
P('''#ASSERT `commits rape within section 375(1A)` `oral penetration of a man`
#ASSERT `offence under s 375(2)` `oral penetration of a man`
''')
P('-- s 375(1): a woman accused is not "any man".')
P(fixture('woman accused, penile element absent',SP,{'the victim is a woman':True,"without the victim's consent":True}))
P('''#ASSERT NOT `offence under s 375(2)` `woman accused, penile element absent`
#ASSERT (`charge under s 375(2)` `woman accused, penile element absent`)'s refusal EQUALS "A charge under section 375(2) would assert that the facts fulfil every legal condition of rape (CPC s 123(5)). On the facts given they do not: any man; penetrates the vagina of a woman, or the anus or mouth of another person, with his penis; the elements of section 375(1) or (1A) taken together."
''')
dig={"sexually penetrates the vagina or anus":True,'the act of penetration':'penetrate the vagina of one Lim Mei Ling with your finger'}
P('-- s 376(2)(a): digital penetration of an adult without consent.')
P(fixture('digital penetration of an adult',SP,{**dig,"without the victim's consent":True}))
P('''#ASSERT `offence under s 376(3)` `digital penetration of an adult`
#ASSERT NOT `offence under s 376(4)` `digital penetration of an adult`
#ASSERT NOT `offence under s 375(2)` `digital penetration of an adult`
''')
P('-- s 376(5)(b): he proves he believed she consented, and she was not below 14.')
P(fixture('digital, mistake as to consent proved',SP,{**dig,"without the victim's consent":True,'believed that the act was done with consent':True}))
P(fixture('digital, girl of 12, mistake as to consent proved',SP,{**dig,"without the victim's consent":True,'believed that the act was done with consent':True,'the victim is below 14 years of age':'(`below 14 years of age` 12)'}))
P('''#ASSERT NOT `offence under s 376(3)` `digital, mistake as to consent proved`
-- s 376(5)(b) needs "B was not below 14 years of age"
#ASSERT `offence under s 376(3)` `digital, girl of 12, mistake as to consent proved`
''')
P('-- s 376A(2): she is 15 and consents to digital penetration; no exploitative relationship.')
P(fixture('girl of 15 consenting, digital',SP,{**dig,'the victim is of or above 14 years of age but below 16':'(`of or above 14 years of age but below 16 years of age` 15)'}))
P(fixture('girl of 15 consenting, digital, by her teacher',SP,{**dig,'the victim is of or above 14 years of age but below 16':True,'exploitative of the victim':True}))
P(fixture('girl of 15 not consenting, digital',SP,{**dig,'the victim is of or above 14 years of age but below 16':True,"without the victim's consent":True}))
P('''#ASSERT NOT `offence under s 376(3)` `girl of 15 consenting, digital`
#ASSERT `offence under s 376A(2)` `girl of 15 consenting, digital`
#ASSERT NOT `offence under s 376A(3)` `girl of 15 consenting, digital`
#ASSERT (`charge under s 376A(2)` `girl of 15 consenting, digital`)'s punishment EQUALS "imprisonment for a term which may extend to 10 years, or with fine, or with both"
#ASSERT (`charge under s 376A(2)` `girl of 15 consenting, digital, by her teacher`)'s punishment EQUALS "imprisonment for a term which may extend to 20 years, and shall also be liable to fine or to caning"
#ASSERT (`charge under s 376A(2)` `girl of 15 consenting, digital`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did penetrate the vagina of one Lim Mei Ling with your finger, the said Lim Mei Ling then being of or above 14 years of age but below 16 years of age, and you have thereby committed an offence punishable under section 376A(2) of the Penal Code 1871."
-- s 376A(1A): 376(2) with B of or above 14 is excluded from s 376A
#ASSERT `offence under s 376(3)` `girl of 15 not consenting, digital`
#ASSERT NOT `offence under s 376A(2)` `girl of 15 not consenting, digital`
''')
P('-- s 376A: she is 16 - outside the section.')
P(fixture('girl of 16 consenting, digital',SP,{**dig,'the victim is of or above 16 years of age but below 18':'(`of or above 16 years of age but below 18 years of age` 16)'}))
P('''#ASSERT NOT `offence under s 376A(2)` `girl of 16 consenting, digital`
#ASSERT NOT `offence under s 376A(3)` `girl of 16 consenting, digital`
-- no exploitative relationship: not s 376AA either
#ASSERT NOT `offence under s 376AA(3)` `girl of 16 consenting, digital`
''')
ex={**base,'the victim is of or above 16 years of age but below 18':'(`of or above 16 years of age but below 18 years of age` 17)','exploitative of the victim':True}
P('-- s 376AA: she is 17; he is her stepfather (s 377CA(2)(a)); she consents (s 376AA(2)(b): no defence).')
P(fixture('stepdaughter of 17',SP,ex))
P('-- s 377D(2)-(3): he reasonably believed she was 18, and took all reasonable steps to verify it.')
P(fixture('stepdaughter of 17, verified belief',SP,{**ex,'reasonably and mistakenly believed':True,'took all reasonable steps':True}))
P('-- s 377D(3)(b): the same belief, but he failed to take all reasonable steps.')
P(fixture('stepdaughter of 17, unverified belief',SP,{**ex,'reasonably and mistakenly believed':True}))
P('-- s 377D(3)(a): the same belief and steps, but he had previously been charged with a listed offence.')
P(fixture('stepdaughter of 17, previously charged',SP,{**ex,'reasonably and mistakenly believed':True,'took all reasonable steps':True,'has previously been charged':True}))
P('''#ASSERT `offence under s 376AA(3)` `stepdaughter of 17`
#ASSERT NOT `offence under s 375(2)` `stepdaughter of 17`
#ASSERT NOT `offence under s 376AA(3)` `stepdaughter of 17, verified belief`
#ASSERT `offence under s 376AA(3)` `stepdaughter of 17, unverified belief`
#ASSERT `offence under s 376AA(3)` `stepdaughter of 17, previously charged`
#ASSERT (`charge under s 376AA(3)` `stepdaughter of 17, verified belief`)'s refusal EQUALS "A charge under section 376AA(3) would assert that the facts fulfil every legal condition of exploitative sexual penetration of minor of or above 16 but below 18 years of age (CPC s 123(5)). On the facts given they do not: no defence of reasonable mistaken belief that B was of or above 18 years of age (section 377D(2)); the elements of section 376AA(1) taken together."

§§ `s 377CA - the presumption of an exploitative relationship`
''')
P(fixture('stepfather',ER,{'parent, step-parent':True}))
P(fixture('stepfather, married to the minor',ER,{'parent, step-parent':True,'lawfully married':True}))
P(fixture('stepfather, contrary proved',ER,{'parent, step-parent':True,'the contrary is proved':True}))
P(fixture('neighbour',ER,{}))
P('''#ASSERT `presumed exploitative within section 377CA(2)` `stepfather`
#ASSERT NOT `presumed exploitative within section 377CA(2)` `stepfather, married to the minor`
#ASSERT NOT `presumed exploitative within section 377CA(2)` `stepfather, contrary proved`
#ASSERT NOT `presumed exploitative within section 377CA(2)` `neighbour`

§§ `s 377CB - consent given under misconception`
''')
P('-- s 377CB illus (a): she believes it is a procedure to extract an evil spirit - misconception as to the sexual nature of the act.')
P(fixture('s 377CB illus (a)',MC,{'consented under a misconception':True,'not of a sexual nature':True,'knows or has reason to believe':True}))
P('-- s 377CB illus (b): she believes it is treatment for a chronic disease - misconception as to the purpose.')
P(fixture('s 377CB illus (b)',MC,{'consented under a misconception':True,'not for a sexual purpose':True,'knows or has reason to believe':True}))
P('-- s 377CB illus (c): she believes the imposter is her husband - misconception as to identity.')
P(fixture('s 377CB illus (c)',MC,{'consented under a misconception':True,'as to the identity':True,'knows or has reason to believe':True}))
P('-- s 377CB illus (d): she believes he is an influential movie director - a misconception as to attributes, not identity.')
P(fixture('s 377CB illus (d)',MC,{'consented under a misconception':True,'knows or has reason to believe':True}))
P('''-- s 377CB illus (a): "B's apparent consent is therefore not a valid consent."
#ASSERT `not a consent within section 377CB` `s 377CB illus (a)`
-- s 377CB illus (b): "B's apparent consent is therefore not a valid consent."
#ASSERT `not a consent within section 377CB` `s 377CB illus (b)`
-- s 377CB illus (c): "... is therefore not a valid consent."
#ASSERT `not a consent within section 377CB` `s 377CB illus (c)`
-- s 377CB illus (d): "B's consent is therefore a valid consent."
#ASSERT NOT `not a consent within section 377CB` `s 377CB illus (d)`

§§ `s 377BA - word or gesture intended to insult modesty`
''')
P(fixture('lewd gesture',IM,{'intending to insult the modesty':True,'makes any gesture':True,'intending that such word or sound will be heard':True,'what was said, done or exhibited':'by making an obscene gesture with your hand at her'}))
P(fixture('muttered, not meant to be heard',IM,{'intending to insult the modesty':True,'utters any word':True}))
P(fixture('peeping into the bathroom',IM,{'intending to insult the modesty':True,'intrudes upon the privacy':True,'what was said, done or exhibited':'by peeping at her through the ventilation window of her bathroom'}))
P('''#ASSERT `offence under s 377BA` `lewd gesture`
#ASSERT (`charge under s 377BA` `lewd gesture`)'s text EQUALS "You, Tan Ah Kow, are charged that you, on or about the 1st day of March 2025, at about 9.30 pm, at Block 123 Ang Mo Kio Avenue 3, Singapore, did, intending to insult the modesty of one Lim Mei Ling, utter words, make sounds or gestures, or exhibit an object, intending that they be heard or seen by the said Lim Mei Ling, to wit, by making an obscene gesture with your hand at her, and you have thereby committed an offence punishable under section 377BA of the Penal Code 1871."
#ASSERT NOT `offence under s 377BA` `muttered, not meant to be heard`
#ASSERT `offence under s 377BA` `peeping into the bathroom`
''')
open('/Users/mengwong/src/legalese/pc-encode/deposit/pc-body-b-tests.l4','w').write('\n'.join(out))
print('written')
