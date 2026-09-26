"""Chapter 11, ss 201-229."""
from lib import Facts, Pun, pred, charge, mu, or_both, and_fine
from build import COVERAGE, catalogue, TIER_DEATH, TIER_LIFE, tier_puns, tier_expr, family, recite, ladder

WD = ("what was done", "S", "What the accused did, as it is to read in the charge after \"to wit,\"")
TIER_C_201 = "the offence is punishable with imprisonment for any term not extending to 20 years"
TIER_C_212 = "the offence is punishable with imprisonment which may extend to one year and not to 20 years"
TIER_C_213 = "the offence is punishable with imprisonment not extending to 20 years"
KNOW = ("knowing or having reason to believe that an offence has been committed", "B",
        "Did the accused know, or have reason to believe (s 26), that an offence had been committed? For ss 201-203, \"offence\" includes an act done outside Singapore which would be punishable here under ss 302, 304, 382, 392-397, 399, 402, 435, 436, 449, 450, 459 or 460 (s 203 Explanation).")
TIERS = lambda c: [
    (TIER_DEATH, "B", "Is the offence (the one screened, harboured or concealed) punishable with death? - its punishment is in its own section, possibly in another group's module"),
    (TIER_LIFE, "B", "Is that offence punishable with imprisonment for life, or with imprisonment which may extend to 20 years?"),
    (c, "B", f"Is that offence one where \"{c.replace('the offence is ', '')}\"? - the words differ from section to section and are the Code's own"),
    ("the offence", "S", "The offence, as it is to be named in the charge - for example \"murder\""),
]


def tiered(sec, c):
    a, b, cc = tier_puns(sec)
    elems = [(f"(f's `{TIER_DEATH}` OR f's `{TIER_LIFE}` OR f's `{c}`)",
              f"the offence is punishable with death, with imprisonment for life or up to 20 years, or where {c.replace('the offence is ', 'it is ')}")]
    return (a, b, cc), elems


def ch11b(m):
    # ------------------------------------------------------------ ss 201-203
    oi = Facts("Offence Information Facts",
               "What the accused knew of an offence, and what the accused did or omitted about it",
               [KNOW,
                ("causes any evidence of the commission of that offence to disappear", "B", "Did the accused cause evidence of the commission of that offence to disappear? (s 201)"),
                ("gives any information respecting the offence which he knows or believes to be false", "B", "Did the accused give information about the offence which the accused knew or believed to be false? (ss 201, 203)"),
                ("with the intention of screening the offender from legal punishment", "B", "Did the accused act with the intention of screening the offender from legal punishment? (s 201) - a fault element"),
                ("intentionally omits to give any information respecting that offence", "B", "Did the accused intentionally omit to give information about the offence? (s 202)"),
                ("which he is legally bound to give", "B", "Was the accused legally bound to give that information (s 43)? (s 202)"),
                ] + TIERS(TIER_C_201) + [WD],
               "Penal Code 1871 ss 201-203 - the operative atoms")
    m.section("201")
    m.add(oi)
    puns, tier = tiered("201", TIER_C_201)
    family(m, "201", oi, "`causes disappearance of evidence of an offence to screen the offender`",
           'Whether the accused causes evidence of an offence to disappear, or gives false information touching it, to screen the offender (s 201 of the Penal Code 1871)',
           [(f"f's `{KNOW[0]}`", "knowing or having reason to believe that an offence has been committed"),
            ("(f's `causes any evidence of the commission of that offence to disappear` OR f's `gives any information respecting the offence which he knows or believes to be false`)",
             "causes any evidence of the commission of that offence to disappear, or gives any information respecting the offence which he knows or believes to be false"),
            ("f's `with the intention of screening the offender from legal punishment`", "with the intention of screening the offender from legal punishment")],
           "causing disappearance of evidence of an offence committed, or giving false information touching it, to screen the offender",
           'CONCAT "knowing or having reason to believe that an offence, namely ", f\'s `the offence`, ", had been committed, did cause evidence of the commission of that offence to disappear, or give information respecting it which you knew or believed to be false, with the intention of screening the offender from legal punishment", (`to wit` (f\'s `what was done`))',
           "screening", "s 201", puns=puns, pun_expr=tier_expr("201", TIER_C_201), extra=tier,
           comment="The tier is an element of the offence: s 201 prescribes a punishment only where the screened offence is punishable as (a), (b) or (c) says (FORK JO-3).")
    COVERAGE["201"] = ("encoded", "`Offence Information Facts`; `causes disappearance of evidence of an offence to screen the offender`, `offence under s 201`, `charge under s 201`; punishments `s 201(a)`-`(c)`")

    m.section("202")
    family(m, "202", oi, "`intentionally omits to give information of an offence`",
           'Whether the accused, bound to inform, intentionally omits to give information of an offence (s 202 of the Penal Code 1871)',
           [(f"f's `{KNOW[0]}`", "knowing or having reason to believe that an offence has been committed"),
            ("f's `intentionally omits to give any information respecting that offence`", "intentionally omits to give any information respecting that offence"),
            ("f's `which he is legally bound to give`", "which he is legally bound to give")],
           "intentional omission to give information of an offence by a person bound to inform",
           'CONCAT "knowing or having reason to believe that an offence, namely ", f\'s `the offence`, ", had been committed, did intentionally omit to give information respecting that offence which you were legally bound to give", (`to wit` (f\'s `what was done`))',
           "screening", "s 202", puns=[or_both("202", "202", months=6)])
    COVERAGE["202"] = ("encoded", "`intentionally omits to give information of an offence`, `offence under s 202`, `charge under s 202`")

    m.section("203")
    family(m, "203", oi, "`gives false information respecting an offence`",
           'Whether the accused gives false information respecting an offence (s 203 of the Penal Code 1871)',
           [(f"f's `{KNOW[0]}`", "knowing or having reason to believe that an offence has been committed"),
            ("f's `gives any information respecting the offence which he knows or believes to be false`", "gives any information respecting that offence which he knows or believes to be false")],
           "giving false information respecting an offence committed",
           'CONCAT "knowing or having reason to believe that an offence, namely ", f\'s `the offence`, ", had been committed, did give information respecting that offence which you knew or believed to be false", (`to wit` (f\'s `what was done`))',
           "screening", "s 203", puns=[or_both("203", "203", 2)])
    COVERAGE["203"] = ("encoded", "`gives false information respecting an offence`, `offence under s 203`, `charge under s 203`; the Explanation widens the knowledge leaf")

    # ------------------------------------------------------------ s 204
    ed = Facts("Evidence Document Facts", "The document or electronic record, and what the accused did to it",
               [("secretes or destroys the document or electronic record", "B", "Did the accused secrete or destroy the document or electronic record? (s 204)"),
                ("obliterates or renders illegible the whole or any part of it", "B", "Did the accused obliterate it, or render the whole or part of it illegible? (s 204)"),
                ("he may be lawfully compelled to produce it as evidence before a court of justice or in a proceeding lawfully held before a public servant as such", "B", "Could the accused be lawfully compelled to produce it as evidence before a court of justice, or in a proceeding lawfully held before a public servant as such? (s 204)"),
                ("with the intention of preventing it from being produced or used as evidence", "B", "Did the accused intend to prevent it from being produced or used as evidence before that court or public servant? (s 204) - a fault element"),
                ("after he has been lawfully summoned or required to produce it for that purpose", "B", "Had the accused been lawfully summoned or required to produce it for that purpose? (s 204)"),
                WD],
               "Penal Code 1871 s 204 - the operative atoms")
    m.section("204", extra_comment="FORK JO-5: the intention and \"after he has been lawfully summoned\" are read as alternatives, each attaching to every act.")
    m.add(ed)
    family(m, "204", ed, "`destroys a document to prevent its production as evidence`",
           'Whether the accused secretes, destroys or obliterates a document or electronic record to prevent its production as evidence (s 204 of the Penal Code 1871)',
           [("(f's `secretes or destroys the document or electronic record` OR f's `obliterates or renders illegible the whole or any part of it`)", "secretes or destroys, or obliterates or renders illegible, any document or electronic record"),
            ("f's `he may be lawfully compelled to produce it as evidence before a court of justice or in a proceeding lawfully held before a public servant as such`", "which he may be lawfully compelled to produce as evidence before a court of justice or a public servant"),
            ("(f's `with the intention of preventing it from being produced or used as evidence` OR f's `after he has been lawfully summoned or required to produce it for that purpose`)", "with the intention of preventing its production or use as evidence, or after being lawfully summoned or required to produce it")],
           "destruction of document or electronic record to prevent its production as evidence",
           recite("did secrete, destroy, obliterate or render illegible a document or electronic record which you could be lawfully compelled to produce as evidence, with the intention of preventing it from being produced or used as evidence"),
           "course-of-justice", "s 204", puns=[or_both("204", "204", 2)])
    COVERAGE["204"] = ("encoded", "`Evidence Document Facts`; `destroys a document to prevent its production as evidence`, `offence under s 204`, `charge under s 204`")

    # ------------------------------------------------------------ s 204A
    cj = Facts("Course of Justice Facts", "The act, its tendency, and what the accused knew or intended by it",
               [("does an act that has a tendency to obstruct, prevent, pervert or defeat the course of justice", "B",
                 "Did the accused do an act that has a tendency to obstruct, prevent, pervert or defeat the course of justice? A person sentenced to imprisonment who leaves or attempts to leave Singapore unlawfully to avoid serving the sentence has done such an act (Explanation 2)."),
                ("knowing that the act is likely to obstruct, prevent, pervert or defeat the course of justice", "B", "Did the accused know that the act was likely to obstruct, prevent, pervert or defeat the course of justice? (s 204A(a)) - a fault element"),
                ("intending to obstruct, prevent, pervert or defeat the course of justice", "B", "Did the accused intend to obstruct, prevent, pervert or defeat the course of justice? (s 204A(b)) - a fault element"),
                ("the act is a mere warning to a witness that he may be prosecuted for perjury if he gives false evidence", "B", "Was the act no more than a warning to a witness that he may be prosecuted for perjury if he gives false evidence? (Explanation 1: that is insufficient)"),
                WD],
               "Penal Code 1871 s 204A and its Explanations - the operative atoms")
    m.section("204A")
    m.add(cj)
    family(m, "204A", cj, "`does an act tending to obstruct, prevent, pervert or defeat the course of justice`",
           'Whether the accused does an act tending to obstruct, prevent, pervert or defeat the course of justice, with the knowledge or intention s 204A of the Penal Code 1871 requires',
           [("f's `does an act that has a tendency to obstruct, prevent, pervert or defeat the course of justice`", "does an act that has a tendency to obstruct, prevent, pervert or defeat the course of justice"),
            ("(f's `knowing that the act is likely to obstruct, prevent, pervert or defeat the course of justice` OR f's `intending to obstruct, prevent, pervert or defeat the course of justice`)",
             "(a) knowing that the act is likely to, or (b) intending to, obstruct, prevent, pervert or defeat the course of justice"),
            ("NOT f's `the act is a mere warning to a witness that he may be prosecuted for perjury if he gives false evidence`", "not a mere warning to a witness that he may be prosecuted for perjury (Explanation 1)")],
           "obstructing, preventing, perverting or defeating the course of justice",
           'CONCAT "did an act which had a tendency to obstruct, prevent, pervert or defeat the course of justice, ", (IF f\'s `intending to obstruct, prevent, pervert or defeat the course of justice` THEN "intending to obstruct, prevent, pervert or defeat the course of justice" ELSE "knowing that the act was likely to obstruct, prevent, pervert or defeat the course of justice"), (`to wit` (f\'s `what was done`))',
           "course-of-justice", "s 204A", puns=[or_both("204A", "204A", 7)])
    COVERAGE["204A"] = ("encoded", "`Course of Justice Facts`; `does an act tending to obstruct, prevent, pervert or defeat the course of justice`, `offence under s 204A`, `charge under s 204A`; Explanation 1 is a NOT-limb, Explanation 2 widens the act leaf")

    # ------------------------------------------------------------ s 204B
    wb = Facts("Witness Bribery Facts", "What was given, asked or attempted, and on what understanding about a witness or an offence",
               [("gives, confers, procures, promises or offers to give, confer or procure, or attempts to procure, any gratification to, upon or for any person", "B", "Did the accused give, confer or procure (or promise, offer or attempt to) any gratification to, upon or for any person? (s 204B(1)(a), (b))"),
                ("upon an agreement or understanding that a person aware of an offence which any person is legally bound to report will abstain from reporting it to the police or an investigating agency", "B", "Was it upon an agreement or understanding that a person aware of an offence (one which someone is legally bound to give information about) would abstain from reporting it to the police or an agency charged by law with investigating offences? (s 204B(1)(a))"),
                ("upon an agreement or understanding that a person called or to be called as a witness in a judicial proceeding will give false testimony, withhold true testimony or abstain from giving evidence", "B", "Was it upon an agreement or understanding that a witness (called or to be called) in a judicial proceeding would give false testimony, withhold true testimony or abstain from giving evidence? (s 204B(1)(b), (d)) - \"judicial proceeding\" is any proceeding in which evidence is or may be legally taken (s 204B(2))"),
                ("attempts by any means to induce a person called or to be called as a witness in a judicial proceeding to give false testimony, withhold true testimony or abstain from giving evidence", "B", "Did the accused attempt by any means to induce such a witness to give false testimony, withhold true testimony or abstain from giving evidence? (s 204B(1)(c))"),
                ("asks, receives or obtains, or agrees or attempts to receive or obtain, any property or benefit for himself or any other person", "B", "Did the accused ask for, receive or obtain (or agree or attempt to) any property or benefit for himself or another? (s 204B(1)(d))"),
                WD],
               "Penal Code 1871 s 204B - the operative atoms")
    m.section("204B")
    m.add(wb)
    g = "f's `gives, confers, procures, promises or offers to give, confer or procure, or attempts to procure, any gratification to, upon or for any person`"
    rep = "f's `upon an agreement or understanding that a person aware of an offence which any person is legally bound to report will abstain from reporting it to the police or an investigating agency`"
    wit = "f's `upon an agreement or understanding that a person called or to be called as a witness in a judicial proceeding will give false testimony, withhold true testimony or abstain from giving evidence`"
    ind = "f's `attempts by any means to induce a person called or to be called as a witness in a judicial proceeding to give false testimony, withhold true testimony or abstain from giving evidence`"
    ask = "f's `asks, receives or obtains, or agrees or attempts to receive or obtain, any property or benefit for himself or any other person`"
    family(m, "204B", wb, "`bribes or suborns a witness`",
           'Whether the accused commits any of the acts in section 204B(1)(a) to (d) of the Penal Code 1871 (bribery of witnesses)',
           [(f"(({g} AND {rep}) OR ({g} AND {wit}) OR {ind} OR ({ask} AND {wit}))",
             "(a) gratification for not reporting an offence, (b) gratification for false or withheld testimony, (c) an attempt to induce a witness to give false testimony, withhold true testimony or abstain, or (d) asking or receiving a benefit for that")],
           "bribery of witnesses", recite("did give or offer gratification, or attempt to induce a witness, or ask for or receive a benefit, upon an understanding that an offence would not be reported or that a witness in a judicial proceeding would give false testimony, withhold true testimony or abstain from giving evidence"),
           "course-of-justice", "s 204B", puns=[or_both("204B", "204B(1)", 7)])
    COVERAGE["204B"] = ("encoded", "`Witness Bribery Facts`; `bribes or suborns a witness`, `offence under s 204B`, `charge under s 204B`; (2) is the @desc of the witness leaf")

    # ------------------------------------------------------------ s 205
    pe = Facts("Personation in Suit Facts", "Whom the accused personated, and what the accused did in that character",
               [("falsely personates another", "B", "Did the accused falsely personate another person? (s 205)"),
                ("in such assumed character makes an admission or statement, confesses judgment, causes process to be issued, becomes bail or security, or does any other act", "B", "In that assumed character, did the accused make an admission or statement, confess judgment, cause process to issue, become bail or security, or do any other act? (s 205)"),
                ("in any suit or criminal prosecution", "B", "Was it in a suit or a criminal prosecution? (s 205)"),
                WD],
               "Penal Code 1871 s 205 - the operative atoms")
    m.section("205")
    m.add(pe)
    family(m, "205", pe, "`falsely personates another in a suit or prosecution`",
           'Whether the accused falsely personates another for an act or proceeding in a suit or criminal prosecution (s 205 of the Penal Code 1871)',
           [("f's `falsely personates another`", "falsely personates another"),
            ("f's `in such assumed character makes an admission or statement, confesses judgment, causes process to be issued, becomes bail or security, or does any other act`", "in such assumed character makes any admission or statement, confesses judgment, causes process to issue, becomes bail or security, or does any other act"),
            ("f's `in any suit or criminal prosecution`", "in any suit or criminal prosecution")],
           "false personation for the purpose of an act or proceeding in a suit",
           recite("did falsely personate another and in such assumed character do an act in a suit or criminal prosecution"),
           "course-of-justice", "s 205", puns=[or_both("205", "205", 3)])
    COVERAGE["205"] = ("encoded", "`Personation in Suit Facts`; `falsely personates another in a suit or prosecution`, `offence under s 205`, `charge under s 205`")

    # ------------------------------------------------------------ ss 206-210
    df = Facts("Decree Fraud Facts", "What the accused did with property, a claim or a decree, and what the accused intended",
               [("fraudulently", "B", "Did the accused act fraudulently (s 25)?"),
                ("removes, conceals, transfers or delivers to any person any property or interest in it", "B", "Did the accused remove, conceal, transfer or deliver to anyone any property or interest in property? (s 206)"),
                ("accepts, receives or claims any property or interest in it, knowing that he has no right or rightful claim to it", "B", "Did the accused accept, receive or claim property or an interest in it, knowing he had no right or rightful claim to it? (s 207)"),
                ("practises any deception touching any right to any property or interest in it", "B", "Did the accused practise any deception touching a right to property or an interest in it? (s 207)"),
                ("intending to prevent it being taken as a forfeiture or in satisfaction of a fine under a sentence pronounced or known likely to be pronounced", "B", "Did the accused intend to prevent the property or interest being taken as a forfeiture, or in satisfaction of a fine, under a sentence pronounced (or known to be likely to be pronounced) by a court or other competent authority? (ss 206, 207)"),
                ("intending to prevent it being taken in execution of a decree or order, or under an enforcement order, made or known likely to be made in a civil suit", "B", "Did the accused intend to prevent it being taken in execution of a decree or order, or under or pursuant to an enforcement order, made (or known likely to be made) by a court in a civil suit? (ss 206, 207)"),
                ("causes or suffers a decree or order to be passed against him for a sum not due, a larger sum than is due, or property to which the person is not entitled", "B", "Did the accused cause or suffer a decree or order to be passed against himself at the suit of any person for a sum not due, for more than is due, or for property or an interest to which that person is not entitled? (s 208)"),
                ("causes or suffers a decree or order to be executed or enforced against him after it has been satisfied", "B", "Did the accused cause or suffer a decree or order to be executed or enforced against himself after it had been satisfied, or for anything for which it had been satisfied? (s 208)"),
                ("obtains a decree or order against any person for a sum not due, a larger sum than is due, or property to which he is not entitled", "B", "Did the accused obtain a decree or order against anyone for a sum not due, for more than is due, or for property or an interest to which the accused is not entitled? (s 210)"),
                ("causes a decree or order to be executed or enforced against any person after it has been satisfied, or suffers or permits any such act in his name", "B", "Did the accused cause a decree or order to be executed or enforced against anyone after it had been satisfied (or for anything for which it had been satisfied), or suffer or permit any such act to be done in his name? (s 210)"),
                WD],
               "Penal Code 1871 ss 206-210 - the operative atoms")
    m.section("206")
    m.add(df)
    intent = "(f's `intending to prevent it being taken as a forfeiture or in satisfaction of a fine under a sentence pronounced or known likely to be pronounced` OR f's `intending to prevent it being taken in execution of a decree or order, or under an enforcement order, made or known likely to be made in a civil suit`)"
    intent_w = "intending thereby to prevent that property or interest from being taken as a forfeiture, in satisfaction of a fine, or in execution of a decree, order or enforcement order"
    family(m, "206", df, "`fraudulently removes or conceals property to prevent its seizure`",
           'Whether the accused fraudulently removes, conceals, transfers or delivers property to prevent its seizure (s 206 of the Penal Code 1871)',
           [("f's fraudulently", "fraudulently"),
            ("f's `removes, conceals, transfers or delivers to any person any property or interest in it`", "removes, conceals, transfers, or delivers to any person any property or any interest therein"),
            (intent, intent_w)],
           "fraudulent removal or concealment of property to prevent its seizure",
           recite("did fraudulently remove, conceal, transfer or deliver property, intending thereby to prevent it from being taken as a forfeiture, in satisfaction of a fine, or in execution of a decree, order or enforcement order"),
           "decree-fraud", "s 206", puns=[or_both("206", "206", 2)])
    COVERAGE["206"] = ("encoded", "`Decree Fraud Facts`; `fraudulently removes or conceals property to prevent its seizure`, `offence under s 206`, `charge under s 206`")

    m.section("207")
    family(m, "207", df, "`fraudulently claims property to prevent its seizure`",
           'Whether the accused fraudulently claims property, or practises deception touching a right to it, to prevent its seizure (s 207 of the Penal Code 1871)',
           [("((f's fraudulently AND f's `accepts, receives or claims any property or interest in it, knowing that he has no right or rightful claim to it`) OR f's `practises any deception touching any right to any property or interest in it`)",
             "fraudulently accepts, receives or claims property knowing he has no right to it, or practises any deception touching any right to property"),
            (intent, intent_w)],
           "fraudulent claim to property to prevent its seizure",
           recite("did fraudulently accept, receive or claim property to which you knew you had no right, or practise deception touching a right to property, intending thereby to prevent it from being taken as a forfeiture, in satisfaction of a fine, or in execution of a decree, order or enforcement order"),
           "decree-fraud", "s 207", puns=[or_both("207", "207", 2)])
    COVERAGE["207"] = ("encoded", "`fraudulently claims property to prevent its seizure`, `offence under s 207`, `charge under s 207`")

    m.section("208")
    family(m, "208", df, "`fraudulently suffers a decree for a sum not due`",
           'Whether the accused fraudulently causes or suffers a decree for a sum not due, or its execution after satisfaction (s 208 of the Penal Code 1871)',
           [("f's fraudulently", "fraudulently"),
            ("(f's `causes or suffers a decree or order to be passed against him for a sum not due, a larger sum than is due, or property to which the person is not entitled` OR f's `causes or suffers a decree or order to be executed or enforced against him after it has been satisfied`)",
             "causes or suffers a decree or order to be passed against him for a sum not due or a larger sum, or to be executed after it has been satisfied")],
           "fraudulently suffering a decree for a sum not due",
           recite("did fraudulently cause or suffer a decree or order to be passed against you for a sum not due, or to be executed or enforced against you after it had been satisfied"),
           "decree-fraud", "s 208", puns=[or_both("208", "208", 2)])
    COVERAGE["208"] = ("encoded", "`fraudulently suffers a decree for a sum not due`, `offence under s 208`, `charge under s 208`")
    m.repealed("209", "[Repealed by Act 15 of 2019]")

    m.section("210")
    family(m, "210", df, "`fraudulently obtains a decree for a sum not due`",
           'Whether the accused fraudulently obtains a decree for a sum not due, or causes it to be executed after satisfaction (s 210 of the Penal Code 1871)',
           [("f's fraudulently", "fraudulently"),
            ("(f's `obtains a decree or order against any person for a sum not due, a larger sum than is due, or property to which he is not entitled` OR f's `causes a decree or order to be executed or enforced against any person after it has been satisfied, or suffers or permits any such act in his name`)",
             "obtains a decree or order for a sum not due or a larger sum, or causes it to be executed after it has been satisfied")],
           "fraudulently obtaining a decree for a sum not due",
           recite("did fraudulently obtain a decree or order against a person for a sum not due, or cause a decree or order to be executed or enforced against a person after it had been satisfied"),
           "decree-fraud", "s 210", puns=[or_both("210", "210", 2)])
    COVERAGE["210"] = ("encoded", "`fraudulently obtains a decree for a sum not due`, `offence under s 210`, `charge under s 210`")

    # ------------------------------------------------------------ s 211
    fc = Facts("False Charge Facts", "The proceeding or charge, and what the accused knew and intended",
               [("with intent to cause injury to any person", "B", "Did the accused intend to cause injury (s 44) to the person? (s 211) - a fault element"),
                ("institutes or causes to be instituted any criminal proceeding against that person", "B", "Did the accused institute, or cause to be instituted, a criminal proceeding against the person? (s 211)"),
                ("falsely charges any person with having committed an offence", "B", "Did the accused falsely charge the person with having committed an offence? (s 211)"),
                ("knowing that there is no just or lawful ground for such proceeding or charge", "B", "Did the accused know there was no just or lawful ground for the proceeding or charge? (s 211) - a fault element"),
                ("the criminal proceeding is instituted on a false charge of an offence punishable with death, or imprisonment for 7 years or upwards", "B", "Was a criminal proceeding instituted on a false charge of an offence punishable with death, or with imprisonment for 7 years or upwards (s 41)? (s 211, second limb)"),
                ("the person", "S", "The person falsely charged, as the charge is to name them"),
                WD],
               "Penal Code 1871 s 211 - the operative atoms")
    m.section("211")
    m.add(fc)
    family(m, "211", fc, "`falsely charges an offence with intent to injure`",
           'Whether the accused, with intent to injure, institutes a criminal proceeding or falsely charges an offence knowing there is no just ground (s 211 of the Penal Code 1871)',
           [("f's `with intent to cause injury to any person`", "with intent to cause injury to any person"),
            ("(f's `institutes or causes to be instituted any criminal proceeding against that person` OR f's `falsely charges any person with having committed an offence`)", "institutes or causes to be instituted any criminal proceeding against that person, or falsely charges any person with having committed an offence"),
            ("f's `knowing that there is no just or lawful ground for such proceeding or charge`", "knowing that there is no just or lawful ground for such proceeding or charge")],
           "false charge of offence made with intent to injure",
           'CONCAT "did, with intent to cause injury to one ", f\'s `the person`, ", institute a criminal proceeding against, or falsely charge, that person with having committed an offence, knowing that there was no just or lawful ground for such proceeding or charge", (`to wit` (f\'s `what was done`))',
           "false-charge", "s 211",
           puns=[or_both("211", "211", 2), and_fine("211 (grave offence)", "211", 7, words="imprisonment for a term which may extend to 7 years and shall also be liable to fine")],
           pun_expr="IF f's `the criminal proceeding is instituted on a false charge of an offence punishable with death, or imprisonment for 7 years or upwards` THEN (`punishment prescribed by s 211 (grave offence)`)'s words ELSE (`punishment prescribed by s 211`)'s words")
    COVERAGE["211"] = ("encoded", "`False Charge Facts`; `falsely charges an offence with intent to injure`, `offence under s 211`, `charge under s 211`; punishments `s 211`, `s 211 (grave offence)`")

    # ------------------------------------------------------------ ss 212, 216, 216A, 216B
    hb = Facts("Harbouring Facts", "Whom the accused harboured or concealed, what the accused knew, and why",
               [("harbours the person", "B", "Did the accused harbour the person in the ordinary sense? (\"harbour\" is widened by s 216B)"),
                ("conceals the person", "B", "Did the accused conceal the person? (ss 212, 216)"),
                ("supplies the person with shelter, food, drink, money, clothes, arms, ammunition, or means of conveyance", "B", "Did the accused supply the person with shelter, food, drink, money, clothes, arms, ammunition or means of conveyance? (s 216B)"),
                ("assists the person in any way to evade apprehension", "B", "Did the accused assist the person in any way to evade apprehension? (s 216B)"),
                ("an offence has been committed", "B", "Had an offence been committed? For s 212 it includes an act abroad punishable here under ss 302, 304, 382, 392-397, 399, 402, 435, 436, 449, 450, 459 or 460 (s 212(2))."),
                ("knows or has reason to believe the person to be the offender", "B", "Did the accused know, or have reason to believe (s 26), that the person was the offender? (s 212) - a fault element"),
                ("with the intention of screening him from legal punishment", "B", "Did the accused intend to screen the person from legal punishment? (s 212) - a fault element; providing food and shelter to a spouse without that intention is not harbouring (illustration (b))"),
                ("the person escaped from lawful custody for an offence of which he was convicted or charged", "B", "Had the person, convicted of or charged with an offence and in lawful custody for it, escaped from that custody? (s 216(1)); \"offence\" includes an extraditable act abroad (s 216(2))"),
                ("a public servant in the exercise of lawful powers ordered the person to be apprehended for an offence", "B", "Had a public servant, exercising lawful powers, ordered the person to be apprehended for an offence? (s 216(1))"),
                ("knowing of such escape or order for apprehension", "B", "Did the accused know of the escape or the order for apprehension? (s 216) - a fault element"),
                ("with the intention of preventing him from being apprehended", "B", "Did the accused intend to prevent the person from being apprehended? (s 216) - a fault element"),
                ("knowing or having reason to believe that the persons are about to commit or have recently committed robbery or gang-robbery", "B", "Did the accused know or have reason to believe that the persons were about to commit, or had recently committed, robbery or gang-robbery (ss 390, 391, pc-property)? It is immaterial whether within or outside Singapore (s 216A Explanation)."),
                ("with the intention of facilitating the robbery or gang-robbery or of screening them from punishment", "B", "Did the accused intend to facilitate the robbery or gang-robbery, or to screen them from punishment? (s 216A) - a fault element"),
                ] + TIERS(TIER_C_212)[:3] + [("the person harboured", "S", "The person harboured or concealed, as the charge is to name them"),
                                            ("the offence", "S", "The offence, as it is to be named in the charge - for example \"gang-robbery\""), WD],
               "Penal Code 1871 ss 212, 216, 216A, 216B - the operative atoms")
    m.section("212")
    m.add(hb)
    m.parts.append("-- s 216B (\"harbour\") is encoded below, in its own place; the ss 212, 216 and 216A ladders call it as one box.\n")
    puns, tier = tiered("212", TIER_C_212)
    for p in puns:
        p.section = p.section.replace("212(", "212(1)(")
    family(m, "212", hb, "`harbours an offender`",
           'Whether the accused harbours or conceals an offender with the intention of screening him from legal punishment (s 212(1) of the Penal Code 1871)',
           [("f's `an offence has been committed`", "whenever an offence has been committed"),
            ("(`harbours within section 216B` f OR f's `conceals the person`)", "harbours or conceals a person"),
            ("f's `knows or has reason to believe the person to be the offender`", "whom he knows or has reason to believe to be the offender"),
            ("f's `with the intention of screening him from legal punishment`", "with the intention of screening him from legal punishment")],
           "harbouring an offender",
           'CONCAT "did harbour or conceal one ", f\'s `the person harboured`, ", whom you knew or had reason to believe to be the offender in respect of an offence, namely ", f\'s `the offence`, ", with the intention of screening that person from legal punishment", (`to wit` (f\'s `what was done`))',
           "harbouring", "s 212", puns=puns, pun_expr=tier_expr("212", TIER_C_212), extra=tier, lead='"Whenever"')
    CATALOGUE_FIX = None
    COVERAGE["212"] = ("encoded", "`Harbouring Facts`; `harbours an offender`, `offence under s 212`, `charge under s 212`; punishments `s 212(a)`-`(c)`; (2) widens the offence leaf")

    # ------------------------------------------------------------ ss 213-215
    sg = Facts("Screening Gift Facts", "What gratification or restitution was taken, given or offered, and in consideration of what",
               [("accepts, agrees to accept, or attempts to obtain any gratification or restitution of property for himself or any other person", "B", "Did the accused accept, agree to accept or attempt to obtain gratification, or restitution of property, for himself or another? (s 213)"),
                ("gives or causes, or offers or agrees to give or cause, any gratification, or to restore or cause the restoration of property, to any person", "B", "Did the accused give (or cause, offer or agree to give) gratification, or restore (or cause restoration of) property, to any person? (s 214)"),
                ("in consideration of concealing an offence, screening any person from legal punishment for it, or not proceeding against any person to bring him to legal punishment", "B", "Was it in consideration of concealing an offence, screening anyone from legal punishment for it, or not proceeding against anyone to bring him to legal punishment? (ss 213, 214)"),
                ("the offence may lawfully be compounded", "B", "May the offence lawfully be compounded? (Exception to ss 213 and 214: they do not extend to it)"),
                ("takes, or agrees or consents to take, any gratification under pretence or on account of helping any person to recover movable property of which he has been deprived by an offence", "B", "Did the accused take (or agree or consent to take) gratification, under pretence or on account of helping someone recover movable property of which he had been deprived by an offence under this Code? (s 215)"),
                ("uses all means in his power to cause the offender to be apprehended and convicted", "B", "Did the accused use all means in his power to cause the offender to be apprehended and convicted? (s 215: if so, no offence)"),
                ] + TIERS(TIER_C_213) + [WD],
               "Penal Code 1871 ss 213-215 - the operative atoms")
    m.section("213")
    m.add(sg)
    comp = ("NOT f's `the offence may lawfully be compounded`", "not a case in which the offence may lawfully be compounded (Exception)")
    cons = ("f's `in consideration of concealing an offence, screening any person from legal punishment for it, or not proceeding against any person to bring him to legal punishment`", "in consideration of concealing an offence, screening any person from legal punishment, or not proceeding against any person")
    puns, tier = tiered("213", TIER_C_213)
    family(m, "213", sg, "`takes a gift to screen an offender`",
           'Whether the accused takes or seeks gratification or restitution in consideration of screening an offender (s 213 of the Penal Code 1871, read with its Exception)',
           [("f's `accepts, agrees to accept, or attempts to obtain any gratification or restitution of property for himself or any other person`", "accepts, or agrees to accept, or attempts to obtain any gratification or restitution of property"), cons, comp],
           "taking gifts to screen an offender from punishment",
           'CONCAT "did accept, agree to accept or attempt to obtain gratification or restitution of property in consideration of concealing an offence, namely ", f\'s `the offence`, ", or of screening a person from legal punishment for it", (`to wit` (f\'s `what was done`))',
           "screening", "s 213", puns=puns, pun_expr=tier_expr("213", TIER_C_213), extra=tier)
    COVERAGE["213"] = ("encoded", "`Screening Gift Facts`; `takes a gift to screen an offender`, `offence under s 213`, `charge under s 213`; the Exception is a NOT-limb")

    m.section("214")
    puns, tier = tiered("214", TIER_C_213)
    family(m, "214", sg, "`offers a gift to screen an offender`",
           'Whether the accused gives or offers gratification or restoration of property in consideration of screening an offender (s 214 of the Penal Code 1871, read with its Exception)',
           [("f's `gives or causes, or offers or agrees to give or cause, any gratification, or to restore or cause the restoration of property, to any person`", "gives or causes, or offers or agrees to give or cause, any gratification, or to restore or cause the restoration of any property"), cons, comp],
           "offering gift or restoration of property in consideration of screening offender",
           'CONCAT "did give or offer gratification, or restore property, to a person in consideration of that person concealing an offence, namely ", f\'s `the offence`, ", or screening a person from legal punishment for it", (`to wit` (f\'s `what was done`))',
           "screening", "s 214", puns=puns, pun_expr=tier_expr("214", TIER_C_213), extra=tier)
    COVERAGE["214"] = ("encoded", "`offers a gift to screen an offender`, `offence under s 214`, `charge under s 214`; the Exceptions paragraph is a NOT-limb of both ss 213 and 214")

    m.section("215")
    family(m, "215", sg, "`takes a gift to help recover stolen property`",
           'Whether the accused takes gratification on account of helping recover property lost by an offence, without using all means to have the offender apprehended (s 215 of the Penal Code 1871)',
           [("f's `takes, or agrees or consents to take, any gratification under pretence or on account of helping any person to recover movable property of which he has been deprived by an offence`", "takes any gratification under pretence or on account of helping any person to recover movable property of which he has been deprived by an offence"),
            ("NOT f's `uses all means in his power to cause the offender to be apprehended and convicted`", "unless he uses all means in his power to cause the offender to be apprehended and convicted")],
           "taking gift to help to recover stolen property",
           recite("did take gratification under pretence or on account of helping a person to recover movable property of which that person had been deprived by an offence, without using all means in your power to cause the offender to be apprehended and convicted"),
           "screening", "s 215", puns=[or_both("215", "215", 2)])
    COVERAGE["215"] = ("encoded", "`takes a gift to help recover stolen property`, `offence under s 215`, `charge under s 215`; \"unless he uses all means\" is a NOT-limb")

    m.section("216")
    puns, tier = tiered("216", TIER_C_212)
    for p in puns:
        p.section = p.section.replace("216(", "216(1)(")
    family(m, "216", hb, "`harbours an escaped offender`",
           'Whether the accused harbours or conceals a person who has escaped from custody or whose apprehension has been ordered, to prevent apprehension (s 216(1) of the Penal Code 1871)',
           [("(f's `the person escaped from lawful custody for an offence of which he was convicted or charged` OR f's `a public servant in the exercise of lawful powers ordered the person to be apprehended for an offence`)", "a person in lawful custody for an offence escapes, or a public servant orders a person to be apprehended for an offence"),
            ("f's `knowing of such escape or order for apprehension`", "knowing of such escape or order for apprehension"),
            ("(`harbours within section 216B` f OR f's `conceals the person`)", "harbours or conceals that person"),
            ("f's `with the intention of preventing him from being apprehended`", "with the intention of preventing him from being apprehended")],
           "harbouring an offender who has escaped from custody, or whose apprehension has been ordered",
           'CONCAT "knowing that one ", f\'s `the person harboured`, " had escaped from lawful custody, or had been ordered to be apprehended, for an offence, namely ", f\'s `the offence`, ", did harbour or conceal that person with the intention of preventing that person from being apprehended", (`to wit` (f\'s `what was done`))',
           "harbouring", "s 216", puns=puns, pun_expr=tier_expr("216", TIER_C_212), extra=tier, lead='"Whenever"')
    COVERAGE["216"] = ("encoded", "`harbours an escaped offender`, `offence under s 216`, `charge under s 216`; punishments `s 216(a)`-`(c)`; (2) widens the escape leaf")

    m.section("216A")
    family(m, "216A", hb, "`harbours robbers or gang-robbers`",
           'Whether the accused harbours persons about to commit, or who have recently committed, robbery or gang-robbery (s 216A of the Penal Code 1871)',
           [("f's `knowing or having reason to believe that the persons are about to commit or have recently committed robbery or gang-robbery`", "knowing or having reason to believe that any persons are about to commit or have recently committed robbery or gang-robbery"),
            ("`harbours within section 216B` f", "harbours them or any of them"),
            ("f's `with the intention of facilitating the robbery or gang-robbery or of screening them from punishment`", "with the intention of facilitating the commission of such robbery or gang-robbery or of screening them from punishment")],
           "harbouring robbers or gang-robbers",
           'CONCAT "knowing or having reason to believe that ", f\'s `the person harboured`, " were about to commit or had recently committed robbery or gang-robbery, did harbour them with the intention of facilitating the commission of such robbery or gang-robbery or of screening them from punishment", (`to wit` (f\'s `what was done`))',
           "harbouring", "s 216A", puns=[and_fine("216A", "216A", 7)])
    COVERAGE["216A"] = ("encoded", "`harbours robbers or gang-robbers`, `offence under s 216A`, `charge under s 216A`; the Explanation widens the knowledge leaf")

    m.section("216B")
    m.add(pred("`harbours within section 216B`", hb,
               'Whether the accused "harbours" a person, as the word is used in sections 212, 216 and 216A of the Penal Code 1871 (s 216B)',
               '''
                   f's `harbours the person`
               OR  (    "includes the supplying a person with"
                    AND f's `supplies the person with shelter, food, drink, money, clothes, arms, ammunition, or means of conveyance` )
               OR  (    "or the assisting a person in any way to"
                    AND f's `assists the person in any way to evade apprehension` )
               '''))
    COVERAGE["216B"] = ("encoded", "`harbours within section 216B` (definition; the drill-down for ss 212, 216, 216A)")

    ch11c(m)


from ch11c import ch11c  # noqa: E402
