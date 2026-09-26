"""pc-justice-order-tests.l4 - expected values from the Code's Illustrations and the words of each section."""
from lib import FACTS
from build import Tests

DEP = "/Users/mengwong/src/legalese/pc-encode/deposit/"
OPEN = "You, Tan Ah Kow, are charged that you, on or about the 1st day of June 2026, at about 10.00 am, at the State Courts, 1 Havelock Square, Singapore, "


def close(sec):
    return f", and you have thereby committed an offence punishable under section {sec} of the Penal Code 1871."


def build():
    t = Tests(DEP + "pc-justice-order-tests.l4", """-- Tests for pc-justice-order.l4 and pc-justice-order-public.l4 - Penal Code 1871
-- Chapters 11-15 (ss 191-298A).
--
-- Expected values come FROM THE SOURCE: each Illustration is cited on the line
-- above its assertion as `-- s N illus (x)`; boundary cases test the words of
-- the threshold they cite. Charge texts are the CPC 2010 s 123-126 form the
-- reference row uses, with the section's own words as the recital. A failing
-- assertion is a finding, not a typo: never edit an expected value to match.
--
-- Fixtures are full record literals (L4 has no record update); every leaf a
-- fixture does not mention is FALSE, as the charge generator's schema
-- completion would make it.""",
              ["IMPORT prelude", "IMPORT `pc-domain`", "IMPORT `pc-general`", "IMPORT `pc-justice-order`", "IMPORT `pc-justice-order-public`"])
    t.add('''
        § `Chapters 11-15 - tests`

        `the particulars` MEANS Particulars WITH
            accused            IS "Tan Ah Kow"
            date               IS "the 1st day of June 2026"
            time               IS "10.00 am"
            place              IS "the State Courts, 1 Havelock Square"
            `co-accused`       IS ""
            `common intention` IS FALSE
        ''')
    fx = lambda fam, name, true, strings=None, comment=None: t.fixture(FACTS[fam], name, true, strings, comment)

    # ------------------------------------------------------------ false evidence
    t.add("§§ `ss 191-195 - false evidence`")
    oath = ["legally bound by an oath to state the truth", "makes a statement", "the statement is false"]
    fx("False Evidence Facts", "s 191 illus (a)", oath + ["he knows or believes the statement to be false", "gives it intentionally", "in any stage of a judicial proceeding"],
       {"the statement": "that you heard Z admit the justice of B's claim"},
       "s 191 illus (a): A, on a trial, falsely swears that he heard Z admit the justice of B's claim.")
    t.add('''
        -- s 191 illus (a): "A has given false evidence."
        #ASSERT `gives false evidence` `s 191 illus (a)`
        -- ... given on a trial, intentionally: s 193, first limb
        #ASSERT `offence under s 193` `s 191 illus (a)`
        #ASSERT `the false evidence is in a stage of a judicial proceeding` `s 191 illus (a)`
        #ASSERT (`charge under s 193` `s 191 illus (a)`)'s punishment EQUALS "imprisonment for a term which may extend to 7 years, and shall also be liable to fine"
        #ASSERT (`charge under s 193` `s 191 illus (a)`)'s text EQUALS "''' + OPEN + '''did intentionally give false evidence in a stage of a judicial proceeding, to wit, by stating that you heard Z admit the justice of B's claim, which statement you knew or believed to be false or did not believe to be true''' + close("193") + '''"
        ''')
    fx("False Evidence Facts", "s 191 illus (b)", oath + ["he knows or believes the statement to be false"],
       comment="s 191 illus (b): bound by oath, A states he believes a signature is Z's when he does not believe it (Explanation 2).")
    t.add('''
        -- s 191 illus (b): "A states that which he knows to be false, and therefore gives false evidence."
        #ASSERT `gives false evidence` `s 191 illus (b)`
        ''')
    fx("False Evidence Facts", "s 191 illus (c)", ["legally bound by an oath to state the truth", "makes a statement"],
       comment="s 191 illus (c): A in good faith believes the signature is Z's; his statement of belief is true as to his belief, so it is not false.")
    t.add('''
        -- s 191 illus (c): "A has not given false evidence."
        #ASSERT NOT `gives false evidence` `s 191 illus (c)`
        #ASSERT NOT `offence under s 193` `s 191 illus (c)`
        ''')
    fx("False Evidence Facts", "s 191 illus (d)", oath + ["he does not believe the statement to be true"],
       comment="s 191 illus (d): bound by oath, A states he knows Z was at a place, knowing nothing of it.")
    t.add('''
        -- s 191 illus (d): "A gives false evidence"
        #ASSERT `gives false evidence` `s 191 illus (d)`
        ''')
    fx("False Evidence Facts", "s 191 illus (e)", oath + ["he does not believe the statement to be true"],
       comment="s 191 illus (e): an interpreter bound by oath certifies as true a translation he does not believe true.")
    t.add('''
        -- s 191 illus (e): "A has given false evidence."
        #ASSERT `gives false evidence` `s 191 illus (e)`
        ''')
    fab = ["intending that it may appear in evidence in a judicial proceeding",
           "intending that it may cause a person forming an opinion upon the evidence to entertain an erroneous opinion touching a point material to the result"]
    fx("False Evidence Facts", "s 192 illus (a)", ["causes any circumstance to exist"] + fab, {"the fabrication": "by putting jewels into a box belonging to Z"},
       "s 192 illus (a): A puts jewels into Z's box intending that Z be convicted of theft.")
    fx("False Evidence Facts", "s 192 illus (b)", ["makes any false entry in any book or record or electronic record"] + fab + ["for the purpose of being used in any stage of a judicial proceeding"],
       comment="s 192 illus (b): A makes a false entry in his shop-book to use as corroborative evidence in a court.")
    fx("False Evidence Facts", "s 192 illus (c)", ["makes any document or electronic record containing a false statement"] + fab,
       comment="s 192 illus (c): A forges a letter in Z's hand to an accomplice and puts it where the police will search.")
    t.add('''
        -- s 192 illus (a), (b), (c): "A has fabricated false evidence."
        #ASSERT `fabricates false evidence` `s 192 illus (a)`
        #ASSERT `fabricates false evidence` `s 192 illus (b)`
        #ASSERT `fabricates false evidence` `s 192 illus (c)`
        #ASSERT `offence under s 193` `s 192 illus (a)`
        -- (a) says only "may appear in evidence", not "for the purpose of being used in a stage of a judicial proceeding": the second limb of s 193
        #ASSERT (`charge under s 193` `s 192 illus (a)`)'s punishment EQUALS "imprisonment for a term which may extend to 3 years, and shall also be liable to fine"
        #ASSERT (`charge under s 193` `s 192 illus (a)`)'s text EQUALS "''' + OPEN + '''did fabricate false evidence, to wit, by putting jewels into a box belonging to Z''' + close("193") + '''"
        -- (b) is "for the purpose of using it as corroborative evidence in a court of justice": the first limb
        #ASSERT (`charge under s 193` `s 192 illus (b)`)'s punishment EQUALS "imprisonment for a term which may extend to 7 years, and shall also be liable to fine"
        ''')
    fx("False Evidence Facts", "s 193 Explanation 2 illus", oath + ["he knows or believes the statement to be false", "gives it intentionally", "in any stage of a judicial proceeding"],
       comment="s 193 Explanation 2 illustration: in a Magistrate's inquiry into committal for trial, A makes on oath a statement he knows to be false.")
    fx("False Evidence Facts", "s 193 Explanation 3 illus", oath + ["he knows or believes the statement to be false", "gives it intentionally", "in any stage of a judicial proceeding"],
       comment="s 193 Explanation 3 illustration: before an officer deputed by a court to ascertain boundaries on the spot, A makes on oath a statement he knows to be false.")
    t.add('''
        -- s 193 Explanations 2 and 3 illustrations: "As this inquiry is a stage of a judicial proceeding, A has given false evidence."
        #ASSERT `offence under s 193` `s 193 Explanation 2 illus`
        #ASSERT `the false evidence is in a stage of a judicial proceeding` `s 193 Explanation 2 illus`
        #ASSERT `offence under s 193` `s 193 Explanation 3 illus`
        #ASSERT `the false evidence is in a stage of a judicial proceeding` `s 193 Explanation 3 illus`
        ''')
    fx("False Evidence Facts", "false evidence given without intention", oath + ["he knows or believes the statement to be false"],
       comment="Refusal: false evidence given, but not intentionally, and nothing fabricated.")
    t.add('''
        #ASSERT `gives false evidence` `false evidence given without intention`
        #ASSERT NOT `offence under s 193` `false evidence given without intention`
        #ASSERT (`charge under s 193` `false evidence given without intention`)'s text EQUALS ""
        #ASSERT (`charge under s 193` `false evidence given without intention`)'s refusal EQUALS "A charge under section 193 would assert that the facts fulfil every legal condition of giving or fabricating false evidence (CPC s 123(5)). On the facts given they do not: intentionally (section 193)."
        ''')
    fx("False Evidence Facts", "s 195 illus", oath + ["he knows or believes the statement to be false",
                                                     "intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for a term of 7 years or upwards"],
       {"the offence intended": "gang-robbery"},
       "s 195 illus: A gives false evidence before a court intending Z to be convicted of gang-robbery.")
    t.add('''
        -- s 395 (pc-property's): gang-robbery, as the s 195 illustration states it.
        @ref Penal Code 1871 s 395 (quoted for the s 195 illustration; pc-property owns it)
        `gang-robbery punishment, for the s 195 illustration` MEANS Punishment WITH
            section                  IS "395"
            words                    IS "imprisonment for a term of not less than 5 years and not more than 20 years and shall also be punished with caning with not less than 12 strokes"
            death                    IS `not prescribed`
            `imprisonment for life`  IS `not prescribed`
            imprisonment             IS `shall be punished with`
            `maximum term in months` IS JUST 240
            `minimum term in months` IS JUST 60
            `forfeiture of property` IS `not prescribed`
            fine                     IS `not prescribed`
            `maximum fine`           IS NOTHING
            `minimum fine`           IS NOTHING
            caning                   IS `shall be punished with`
            `minimum strokes`        IS JUST 12
            `maximum strokes`        IS NOTHING
            `or with both`           IS FALSE

        -- s 195 illus: A gives false evidence intending Z's conviction of gang-robbery
        #ASSERT `offence under s 195(1)` `s 195 illus`
        #ASSERT NOT `offence under s 195(2)` `s 195 illus`
        -- "A, therefore, is liable to such imprisonment, but is not liable to caning."
        #ASSERT (`punishment prescribed by s 195(1) for` `gang-robbery punishment, for the s 195 illustration`)'s imprisonment EQUALS `shall be punished with`
        #ASSERT (`punishment prescribed by s 195(1) for` `gang-robbery punishment, for the s 195 illustration`)'s `minimum term in months` EQUALS JUST 60
        #ASSERT (`punishment prescribed by s 195(1) for` `gang-robbery punishment, for the s 195 illustration`)'s `maximum term in months` EQUALS JUST 240
        #ASSERT (`punishment prescribed by s 195(1) for` `gang-robbery punishment, for the s 195 illustration`)'s caning EQUALS `not prescribed`
        -- s 512(3)'s reader still sees a minimum sentence in it
        #ASSERT `fixed by law or carries a minimum sentence` (`punishment prescribed by s 195(1) for` `gang-robbery punishment, for the s 195 illustration`)
        ''')

    # ------------------------------------------------------------ 196-200
    t.add("§§ `ss 196-200 - punished as if false evidence`")
    fx("Using False Evidence Facts", "certificate issued in a judicial proceeding", ["issues or signs any certificate", "the certificate is required by law to be given or signed",
                                                                                    "knowing or believing that the certificate is false in any material point", "in any stage of a judicial proceeding"])
    t.add('''
        -- s 197: "shall be punished in the same manner as if he gave false evidence" - read with s 193's first limb
        #ASSERT `offence under s 197` `certificate issued in a judicial proceeding`
        #ASSERT (`charge under s 197` `certificate issued in a judicial proceeding`)'s punishment EQUALS "in the same manner as if he gave false evidence (section 193: imprisonment for a term which may extend to 7 years, and shall also be liable to fine)"
        -- s 198 needs "corruptly" and use; issuing is not using
        #ASSERT NOT `offence under s 198` `certificate issued in a judicial proceeding`
        ''')
    fx("Using False Evidence Facts", "s 200 Explanation - an informal declaration", ["makes a statement in a declaration made or subscribed by him",
                                                                                     "a court of justice, public servant or other person is bound or authorised by law to receive the declaration as evidence of any fact",
                                                                                     "the statement in the declaration is false", "knows or believes the statement in the declaration to be false or does not believe it to be true",
                                                                                     "touching any point material to the object for which the declaration is made or used"],
       comment="s 200 Explanation: a declaration inadmissible merely for informality is still a declaration within ss 199 and 200 - so the leaf holds.")
    t.add('''
        #ASSERT `offence under s 199` `s 200 Explanation - an informal declaration`
        #ASSERT (`charge under s 199` `s 200 Explanation - an informal declaration`)'s punishment EQUALS "in the same manner as if he gave false evidence (section 193: imprisonment for a term which may extend to 3 years, and shall also be liable to fine)"
        ''')

    fx("Using False Evidence Facts", "certificate used, believed but not known false", ["corruptly", "uses or attempts to use the certificate as a true certificate",
                                                                                       "knowing or believing that the certificate is false in any material point"])
    t.add('''
        -- s 198: "knowing the same to be false" - belief short of knowledge is not enough (FORK JO-4)
        #ASSERT NOT `offence under s 198` `certificate used, believed but not known false`
        ''')
    fx("False Evidence Facts", "fabrication for a capital charge, innocent executed", ["causes any circumstance to exist"] + fab +
       ["intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence which is capital",
        "an innocent person is convicted and executed in consequence of the false evidence"])
    t.add('''
        -- s 194: the death limb reaches "the person who gives such false evidence" - not a fabricator (FORK JO-12)
        #ASSERT `offence under s 194` `fabrication for a capital charge, innocent executed`
        #ASSERT (`charge under s 194` `fabrication for a capital charge, innocent executed`)'s punishment EQUALS "imprisonment for life, or with imprisonment for a term which may extend to 20 years, and shall, if he is not sentenced to imprisonment for life, also be liable to fine"
        ''')

    # ------------------------------------------------------------ 201-203
    t.add("§§ `ss 201-203 - screening an offender`")
    fx("Offence Information Facts", "s 201 illus", ["knowing or having reason to believe that an offence has been committed", "causes any evidence of the commission of that offence to disappear",
                                                    "with the intention of screening the offender from legal punishment", "the offence is punishable with death"],
       {"the offence": "murder", "what was done": "by assisting B to hide the body of Z"},
       "s 201 illus: A, knowing that B has murdered Z, assists B to hide the body to screen B.")
    t.add('''
        -- s 201 illus: "A is liable to imprisonment for 10 years, and also to fine."
        #ASSERT `offence under s 201` `s 201 illus`
        #ASSERT (`charge under s 201` `s 201 illus`)'s punishment EQUALS "imprisonment for a term which may extend to 10 years, and shall also be liable to fine"
        #ASSERT (`punishment prescribed by s 201(a)`)'s `maximum term in months` EQUALS JUST 120
        #ASSERT (`punishment prescribed by s 201(a)`)'s fine EQUALS `shall also be liable to`
        #ASSERT (`charge under s 201` `s 201 illus`)'s text EQUALS "''' + OPEN + '''knowing or having reason to believe that an offence, namely murder, had been committed, did cause evidence of the commission of that offence to disappear, or give information respecting it which you knew or believed to be false, with the intention of screening the offender from legal punishment, to wit, by assisting B to hide the body of Z''' + close("201") + '''"
        -- s 201 (a)-(c): one-fourth of the longest term (theft, s 379: 3 years = 36 months -> 9 months)
        #ASSERT `one-fourth part of the longest term of imprisonment` 36 EQUALS 9
        ''')
    fx("Offence Information Facts", "s 201 without a tier", ["knowing or having reason to believe that an offence has been committed", "causes any evidence of the commission of that offence to disappear",
                                                             "with the intention of screening the offender from legal punishment"],
       comment="FORK JO-3: the screened offence's punishment is unknown, so no paragraph of s 201 prescribes a punishment and the charge refuses.")
    t.add('''
        #ASSERT `causes disappearance of evidence of an offence to screen the offender` `s 201 without a tier`
        #ASSERT NOT `offence under s 201` `s 201 without a tier`
        #ASSERT (`charge under s 201` `s 201 without a tier`)'s refusal EQUALS "A charge under section 201 would assert that the facts fulfil every legal condition of causing disappearance of evidence of an offence committed, or giving false information touching it, to screen the offender (CPC s 123(5)). On the facts given they do not: the offence is punishable with death, with imprisonment for life or up to 20 years, or where it is punishable with imprisonment for any term not extending to 20 years."
        ''')

    # ------------------------------------------------------------ 204A
    t.add("§§ `s 204A - perverting the course of justice`")
    fx("Course of Justice Facts", "s 204A Explanation 1", ["does an act that has a tendency to obstruct, prevent, pervert or defeat the course of justice",
                                                           "intending to obstruct, prevent, pervert or defeat the course of justice",
                                                           "the act is a mere warning to a witness that he may be prosecuted for perjury if he gives false evidence"])
    fx("Course of Justice Facts", "s 204A Explanation 2", ["does an act that has a tendency to obstruct, prevent, pervert or defeat the course of justice",
                                                           "intending to obstruct, prevent, pervert or defeat the course of justice"],
       {"what was done": "by leaving Singapore unlawfully to avoid serving your sentence of imprisonment"},
       "s 204A Explanation 2: a person sentenced to imprisonment leaves Singapore unlawfully to avoid serving it.")
    t.add('''
        -- s 204A Explanation 1: "A mere warning to a witness ... is insufficient to constitute an offence."
        #ASSERT NOT `offence under s 204A` `s 204A Explanation 1`
        -- s 204A Explanation 2: absconding "has done an act which has a tendency to obstruct and defeat the course of justice"
        #ASSERT `offence under s 204A` `s 204A Explanation 2`
        #ASSERT (`charge under s 204A` `s 204A Explanation 2`)'s text EQUALS "''' + OPEN + '''did an act which had a tendency to obstruct, prevent, pervert or defeat the course of justice, intending to obstruct, prevent, pervert or defeat the course of justice, to wit, by leaving Singapore unlawfully to avoid serving your sentence of imprisonment''' + close("204A") + '''"
        #ASSERT (`charge under s 204A` `s 204A Explanation 2`)'s punishment EQUALS "imprisonment for a term which may extend to 7 years, or with fine, or with both"
        ''')

    # ------------------------------------------------------------ 212
    t.add("§§ `ss 212, 216, 216A, 216B - harbouring`")
    fx("Harbouring Facts", "s 212 illus (a)", ["an offence has been committed", "conceals the person", "knows or has reason to believe the person to be the offender",
                                               "with the intention of screening him from legal punishment",
                                               "the offence is punishable with imprisonment for life or with imprisonment which may extend to 20 years"],
       {"the person harboured": "B", "the offence": "gang-robbery"})
    t.add('''
        -- s 212 illus (a): "A is liable to imprisonment for a term not exceeding 7 years, and is also liable to fine."
        #ASSERT `offence under s 212` `s 212 illus (a)`
        #ASSERT (`charge under s 212` `s 212 illus (a)`)'s punishment EQUALS "imprisonment for a term which may extend to 7 years, and shall also be liable to fine"
        ''')
    fx("Harbouring Facts", "s 212 illus (b)", ["an offence has been committed", "supplies the person with shelter, food, drink, money, clothes, arms, ammunition, or means of conveyance",
                                               "knows or has reason to believe the person to be the offender", "the offence is punishable with imprisonment which may extend to one year and not to 20 years"],
       comment="s 212 illus (b): A gives spouse B, a house-breaker, food and shelter with no intention to screen B.")
    fx("Harbouring Facts", "s 212 illus (c)", ["an offence has been committed", "supplies the person with shelter, food, drink, money, clothes, arms, ammunition, or means of conveyance",
                                               "knows or has reason to believe the person to be the offender", "with the intention of screening him from legal punishment",
                                               "the offence is punishable with imprisonment for life or with imprisonment which may extend to 20 years"],
       comment="s 212 illus (c): A gives spouse B, a gang-robber about to flee, food and shelter to help B evade detection.")
    t.add('''
        -- s 212 illus (b): "A is not guilty of the offence of harbouring."
        #ASSERT `harbours within section 216B` `s 212 illus (b)`
        #ASSERT NOT `offence under s 212` `s 212 illus (b)`
        -- s 212 illus (c): "A is guilty of the offence of harbouring."
        #ASSERT `offence under s 212` `s 212 illus (c)`
        ''')

    # ------------------------------------------------------------ escape
    t.add("§§ `ss 224, 225 - escape and rescue`")
    fx("Escape Facts", "escape from lawful custody", ["escapes or attempts to escape from custody in which he is lawfully detained", "for an offence with which he is charged or of which he has been convicted"],
       {"what was done": "by running out of the Ang Mo Kio Police Division lock-up"})
    t.add('''
        #ASSERT `offence under s 224` `escape from lawful custody`
        #ASSERT (`charge under s 224` `escape from lawful custody`)'s text EQUALS "''' + OPEN + '''did intentionally offer resistance or illegal obstruction to your lawful apprehension, or escape or attempt to escape from custody in which you were lawfully detained, for an offence with which you were charged or of which you had been convicted, to wit, by running out of the Ang Mo Kio Police Division lock-up''' + close("224") + '''"
        ''')
    fx("Escape Facts", "rescue of a person under sentence of death", ["rescues or attempts to rescue another person from custody in which that person is lawfully detained",
                                                                      "the other person is apprehended or detained for an offence", "the other person is under sentence of death"])
    t.add('''
        -- s 225(e): "under sentence of death" - imprisonment for life or up to 15 years, and fine
        #ASSERT `offence under s 225` `rescue of a person under sentence of death`
        #ASSERT (`charge under s 225` `rescue of a person under sentence of death`)'s punishment EQUALS "imprisonment for life or imprisonment for a term not exceeding 15 years, and shall also be liable to fine"
        #ASSERT (`punishment prescribed by s 225(e)`)'s `maximum term in months` EQUALS JUST 180
        ''')

    # ------------------------------------------------------------ Chapter 14
    t.add("§§ `ss 267A, 267B - affray`")
    fx("Affray Facts", "an affray at a hawker centre", ["2 or more persons fight", "the accused is one of the persons fighting", "in a public place", "they disturb the public peace"],
       {"the other persons": "Lim Boon Huat", "what was done": "by exchanging blows with the said Lim Boon Huat"})
    fx("Affray Facts", "a fight at home", ["2 or more persons fight", "the accused is one of the persons fighting", "they disturb the public peace"])
    t.add('''
        #ASSERT `commits an affray` `an affray at a hawker centre`
        #ASSERT (`charge under s 267B` `an affray at a hawker centre`)'s text EQUALS "''' + OPEN + '''together with Lim Boon Huat, did disturb the public peace by fighting in a public place, and thereby commit an affray, to wit, by exchanging blows with the said Lim Boon Huat''' + close("267B") + '''"
        #ASSERT (`charge under s 267B` `an affray at a hawker centre`)'s punishment EQUALS "imprisonment for a term which may extend to one year, or with fine which may extend to $5,000, or with both"
        -- s 267A: "in a public place" - a fight at home is not an affray
        #ASSERT NOT `offence under s 267B` `a fight at home`
        #ASSERT (`charge under s 267B` `a fight at home`)'s refusal EQUALS "A charge under section 267B would assert that the facts fulfil every legal condition of affray (CPC s 123(5)). On the facts given they do not: in a public place; the elements of section 267A taken together."
        ''')
    t.add("§§ `ss 268, 290, 291 - public nuisance`")
    fx("Public Nuisance Facts", "a knowing nuisance", ["does any act or is guilty of an illegal omission",
                                                      "which causes any common injury, danger or annoyance to the public or to the people in general who dwell or occupy property in the vicinity",
                                                      "the case is not otherwise punishable by this Code",
                                                      "the offender knew that the act or omission will cause or will probably cause any common injury, danger or annoyance"])
    t.add('''
        #ASSERT `is guilty of a public nuisance` `a knowing nuisance`
        -- s 290(b): knowledge - up to 3 months, or fine up to $2,000, or both
        #ASSERT (`charge under s 290` `a knowing nuisance`)'s punishment EQUALS "imprisonment for a term which may extend to 3 months, or with fine which may extend to $2,000, or with both"
        -- s 291 needs an injunction by a public servant
        #ASSERT NOT `offence under s 291` `a knowing nuisance`
        ''')
    t.add("§§ `ss 284-289 - dangerous conduct`")
    fx("Dangerous Conduct Facts", "fatal rash handling of fuel", ["does any act with any dangerous or harmful substance", "so rashly or negligently", "causes the death of any other person"])
    fx("Dangerous Conduct Facts", "cigarette dropped, fire 45 minutes later", ["deposits, drops, places or throws a cigarette, cigar, match stick, charcoal, incense, embers or any thing likely to cause fire in a place",
                                                                              "a fire occurs at or in the vicinity of that place within 60 minutes from the time of that act", "so rashly or negligently", "such fire occurs", "endangers human life"])
    t.add('''
        -- s 284(1)(e), punished by (3)(d)
        #ASSERT `offence under s 284` `fatal rash handling of fuel`
        #ASSERT (`charge under s 284` `fatal rash handling of fuel`)'s punishment EQUALS "imprisonment for a term which may extend to 7 years, or with fine, or with both"
        -- s 286: the contribution is presumed; s 285(1)(b), punished by (2)(a)
        #ASSERT `is presumed to have substantially contributed to the risk of fire within section 286` `cigarette dropped, fire 45 minutes later`
        #ASSERT `offence under s 285` `cigarette dropped, fire 45 minutes later`
        #ASSERT (`charge under s 285` `cigarette dropped, fire 45 minutes later`)'s punishment EQUALS "imprisonment for a term which may extend to one year, or with fine which may extend to $5,000, or with both"
        -- s 286: "within 60 minutes from the time of that act"
        #ASSERT `within 60 minutes` 45
        #ASSERT `within 60 minutes` 60
        #ASSERT NOT `within 60 minutes` 61
        ''')
    t.add("§§ `ss 292-294 - obscenity`")
    fx("Obscenity Facts", "obscene act on a bus", ["to the annoyance of others", "does any obscene act in any public place"])
    fx("Obscenity Facts", "obscene film sold to a 20-year-old", ["the object is an obscene object", "sells, lets to hire, distributes, exhibits or circulates, or offers or attempts to do so, an obscene object to a person",
                                                                "the person is below 21 years of age"])
    fx("Obscenity Facts", "religious painting", ["the object is an obscene object", "the object is kept or used bona fide for religious purposes",
                                                 "sells, lets to hire, distributes, publicly exhibits or puts into circulation the obscene object"])
    t.add('''
        #ASSERT `offence under s 294` `obscene act on a bus`
        #ASSERT `offence under s 293` `obscene film sold to a 20-year-old`
        -- s 292 Exception: religious objects
        #ASSERT NOT `offence under s 292` `religious painting`
        -- thresholds
        #ASSERT `below 21 years of age` 20
        #ASSERT NOT `below 21 years of age` 21
        #ASSERT `below 18 years of age` 17
        #ASSERT NOT `below 18 years of age` 18
        #ASSERT `below 16 years of age` 15
        #ASSERT NOT `below 16 years of age` 16
        #ASSERT `10 or more individuals` 10
        #ASSERT NOT `10 or more individuals` 9
        ''')
    t.add("§§ `Chapter 15 - race`")
    fx("Racial Feelings Facts", "a racial slur", ["with deliberate intention of wounding the racial feelings of any person",
                                                  "utters any word or makes any sound in the hearing of that person, makes any gesture or places any object in the sight of that person, or causes any matter to be seen or heard by that person"],
       {"the person": "Rajendran s/o Muthu", "what was done": "by shouting a racial slur at him"})
    t.add('''
        #ASSERT `offence under s 298` `a racial slur`
        #ASSERT (`charge under s 298` `a racial slur`)'s text EQUALS "''' + OPEN + '''did, with deliberate intention of wounding the racial feelings of one Rajendran s/o Muthu, utter words or make sounds in the hearing of, or make gestures or place objects in the sight of, that person, to wit, by shouting a racial slur at him''' + close("298") + '''"
        ''')
    t.write()
