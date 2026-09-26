"""Chapter 14 ss 284-294, Chapter 15."""
from lib import Facts, Pun, pred, mu, or_both, and_fine
from build import COVERAGE, family, recite

WD = ("what was done", "S", "What the accused did, as it is to read in the charge after \"to wit,\"")

LIKELY = "likely to cause hurt or injury to any other person"
ENDANGER = "endangers human life"
HURT = "causes hurt or injury to any other person"
GH = "causes grievous hurt to any other person"
DEATH = "causes the death of any other person"
PROP = "causes damage to or diminishes the value or utility of any property belonging to any other person or the Government"
LIKELY_GH = "is likely to cause grievous hurt"


def gravest(sec, table):
    """table: list of (leaf, pun name), gravest first; last entry's leaf ignored (the default)."""
    expr = ""
    for leaf, name in table[:-1]:
        expr += f"IF f's `{leaf}` THEN (`punishment prescribed by s {name}`)'s words ELSE "
    return expr + f"(`punishment prescribed by s {table[-1][1]}`)'s words"


def ch14b(m):
    dc = Facts("Dangerous Conduct Facts", "What the accused did or omitted with a substance, fire, machinery, building or animal, how, and with what result",
               [("does any act with any dangerous or harmful substance", "B", "Did the accused do an act with a dangerous or harmful substance - which includes fire or anything likely to cause fire (s 284(4))? An act includes omitting to take sufficient measures with such a substance in his possession against probable danger to life, grievous hurt or hurt (s 284(2))."),
                ("does any act with any machinery in his possession or under his care", "B", "Did the accused do an act with machinery in his possession or care? An act includes omitting to take sufficient measures with it (s 287(2))."),
                ("so rashly or negligently", "B", "Was it done so rashly (s 26E) or negligently (s 26F)? (ss 284, 285, 287)"),
                ("with any fire or thing likely to cause fire, causes or substantially contributes to the risk of causing a fire", "B", "Did the accused, with fire or anything likely to cause fire, cause or substantially contribute to the risk of causing a fire? (s 285(1)); s 286 may presume the contribution"),
                ("such fire occurs", "B", "Did such a fire occur? (s 285(1))"),
                ("deposits, drops, places or throws a cigarette, cigar, match stick, charcoal, incense, embers or any thing likely to cause fire in a place", "B", "(s 286)"),
                ("a fire occurs at or in the vicinity of that place within 60 minutes from the time of that act", "B", "(s 286) - the helper `within 60 minutes` decides it from the minutes elapsed"),
                ("the contrary is proved", "B", "Has the accused proved that he did not substantially contribute to the risk of the fire? (s 286 \"until the contrary is proved\")"),
                ("in pulling down or repairing any building, knowingly or negligently omits to take sufficient measure against probable danger to human life from its fall", "B", "(s 288(1))"),
                ("knowingly or negligently omits to take sufficient measure with any animal against probable danger to human life or of grievous hurt from it", "B", "(s 289(1))"),
                (LIKELY, "B", "Was it (or the fire) likely to cause hurt or injury to another? (ss 284(1)(a), 285(1)(a), 287(1)(a)) - \"hurt\" is s 319, pc-body-a"),
                (ENDANGER, "B", "Did it (or the fire, or the omission) endanger human life? (ss 284(1)(b), 285(1)(b), 287(1)(b), 288(1)(a), 289(1)(b))"),
                (LIKELY_GH, "B", "Was the omission likely to cause grievous hurt (s 320, pc-body-a)? (s 289(1)(a))"),
                (PROP, "B", "(s 285(1)(c))"),
                (HURT, "B", "Did it cause hurt or injury to another? (ss 284(1)(c) - which says \"hurt\" only, 285(1)(d), 287(1)(c)) - s 319, pc-body-a"),
                (GH, "B", "Did it cause grievous hurt to another? (ss 284(1)(d) - which adds \"or injury\", 285(1)(e), 287(1)(d), 289(1)(c)) - s 320, pc-body-a"),
                (DEATH, "B", "Did it cause the death of another? (ss 284(1)(e), 285(1)(f), 287(1)(e), 288(1)(b), 289(1)(d))"),
                WD],
               "Penal Code 1871 ss 284-289 - the operative atoms; hurt and grievous hurt are pc-body-a's (cross-module joins)")
    m.section("284")
    m.add(dc)
    res = lambda leaves: ("(" + " OR ".join(f"f's `{l}`" for l in leaves) + ")", "with one of the results the subsection lists")
    rn = ("f's `so rashly or negligently`", "so rashly or negligently")
    family(m, "284", dc, "`does a rash act with a dangerous substance`", "Whether the accused does an act with a dangerous or harmful substance so rashly or negligently as section 284(1) of the Penal Code 1871 describes",
           [("f's `does any act with any dangerous or harmful substance`", "does, with any dangerous or harmful substance, any act"), rn, res([LIKELY, ENDANGER, HURT, GH, DEATH])],
           "rash or negligent conduct with respect to dangerous or harmful substance", recite("did an act with a dangerous or harmful substance so rashly or negligently as to endanger human life or to be likely to cause, or to cause, hurt, grievous hurt or death to another person"),
           "public-safety", "s 284", lead='"A person shall be guilty of an offence who"',
           puns=[or_both("284(3)(a)", "284(3)(a)", 1, maxfine=5000), or_both("284(3)(b)", "284(3)(b)", 3), or_both("284(3)(c)", "284(3)(c)", 6), or_both("284(3)(d)", "284(3)(d)", 7)],
           pun_expr=gravest("284", [(DEATH, "284(3)(d)"), (GH, "284(3)(c)"), (HURT, "284(3)(b)"), (None, "284(3)(a)")]))
    COVERAGE["284"] = ("encoded", "`Dangerous Conduct Facts`; `does a rash act with a dangerous substance`, `offence under s 284`, `charge under s 284`; punishments `s 284(3)(a)`-`(d)` picked by the gravest result (FORK JO-8)")

    m.section("285")
    m.add(pred("`is presumed to have substantially contributed to the risk of fire within section 286`", dc,
               "Whether a person is presumed, until the contrary is proved, to have substantially contributed to the risk of causing a fire (s 286 of the Penal Code 1871)", '''
            "In any proceedings for an offence under section 285, where any person"
        AND f's `deposits, drops, places or throws a cigarette, cigar, match stick, charcoal, incense, embers or any thing likely to cause fire in a place`
        AND "and"
        AND f's `a fire occurs at or in the vicinity of that place within 60 minutes from the time of that act`
        AND "that person is, until the contrary is proved, presumed to have substantially contributed to the risk of causing that fire"
        AND NOT f's `the contrary is proved`
        '''))
    m.helper('''
        @export Whether a fire occurred "within 60 minutes from the time of that act" (s 286 of the Penal Code 1871)
        GIVEN minutes IS A NUMBER @desc The minutes between the act and the fire
        GIVETH A BOOLEAN
        DECIDE `within 60 minutes` minutes IF minutes AT MOST 60
        ''')
    family(m, "285", dc, "`causes or contributes to the risk of a dangerous fire`", "Whether the accused rashly or negligently causes or contributes to the risk of a fire which occurs with a result section 285(1) of the Penal Code 1871 lists",
           [("(f's `with any fire or thing likely to cause fire, causes or substantially contributes to the risk of causing a fire` OR `is presumed to have substantially contributed to the risk of fire within section 286` f)", "with any fire or any thing likely to cause fire, causes or substantially contributes to the risk of causing a fire (or is presumed to, s 286)"),
            rn, ("f's `such fire occurs`", "if such fire occurs"), res([LIKELY, ENDANGER, PROP, HURT, GH, DEATH])],
           "causing or contributing to risk of dangerous fire", recite("did rashly or negligently cause or substantially contribute to the risk of causing a fire, which fire occurred and endangered human life or was likely to cause, or caused, hurt, grievous hurt, death or damage to property"),
           "public-safety", "s 285",
           puns=[or_both("285(2)(a)", "285(2)(a)", 1, maxfine=5000), or_both("285(2)(b)", "285(2)(b)", months=18), or_both("285(2)(c)", "285(2)(c)", 3), or_both("285(2)(d)", "285(2)(d)", 6), or_both("285(2)(e)", "285(2)(e)", 7)],
           pun_expr=gravest("285", [(DEATH, "285(2)(e)"), (GH, "285(2)(d)"), (HURT, "285(2)(c)"), (PROP, "285(2)(b)"), (None, "285(2)(a)")]))
    COVERAGE["285"] = ("encoded", "`causes or contributes to the risk of a dangerous fire`, `offence under s 285`, `charge under s 285`; punishments `s 285(2)(a)`-`(e)`")
    m.section("286", extra_comment="Encoded above, beside s 285 which it serves: `is presumed to have substantially contributed to the risk of fire within section 286`, and the `within 60 minutes` helper.")
    COVERAGE["286"] = ("encoded", "`is presumed to have substantially contributed to the risk of fire within section 286` (a presumption, wired into the s 285 ladder as an alternative limb), `within 60 minutes`")

    m.section("287")
    family(m, "287", dc, "`does a rash act with machinery`", "Whether the accused does an act with machinery so rashly or negligently as section 287(1) of the Penal Code 1871 describes",
           [("f's `does any act with any machinery in his possession or under his care`", "does, with any machinery in the person's possession or under the person's care, any act"), rn, res([LIKELY, ENDANGER, HURT, GH, DEATH])],
           "rash or negligent conduct with respect to any machinery", recite("did an act with machinery in your possession or care so rashly or negligently as to endanger human life or to be likely to cause, or to cause, hurt, grievous hurt or death to another person"),
           "public-safety", "s 287", lead='"A person shall be guilty of an offence who"',
           puns=[or_both("287(3)(a)", "287(3)(a)", 1, maxfine=5000), or_both("287(3)(b)", "287(3)(b)", 3), or_both("287(3)(c)", "287(3)(c)", 6), or_both("287(3)(d)", "287(3)(d)", 7)],
           pun_expr=gravest("287", [(DEATH, "287(3)(d)"), (GH, "287(3)(c)"), (HURT, "287(3)(b)"), (None, "287(3)(a)")]))
    COVERAGE["287"] = ("encoded", "`does a rash act with machinery`, `offence under s 287`, `charge under s 287`; punishments `s 287(3)(a)`-`(d)`")

    m.section("288")
    family(m, "288", dc, "`omits precautions in pulling down or repairing a building`", "Whether the accused omits sufficient precautions in pulling down or repairing a building, endangering life or causing death (s 288(1) of the Penal Code 1871)",
           [("f's `in pulling down or repairing any building, knowingly or negligently omits to take sufficient measure against probable danger to human life from its fall`", "in pulling down or repairing any building, knowingly or negligently omits to take such measure as is sufficient to guard against probable danger to human life from its fall"),
            res([ENDANGER, DEATH])],
           "negligence in pulling down or repairing buildings", recite("in pulling down or repairing a building, did knowingly or negligently omit to take sufficient measures against probable danger to human life from its fall, which omission endangered human life or caused death"),
           "public-safety", "s 288", lead='"A person shall be guilty of an offence who"',
           puns=[or_both("288(2)(a)", "288(2)(a)", 1, maxfine=5000), or_both("288(2)(b)", "288(2)(b)", 7)],
           pun_expr=gravest("288", [(DEATH, "288(2)(b)"), (None, "288(2)(a)")]))
    COVERAGE["288"] = ("encoded", "`omits precautions in pulling down or repairing a building`, `offence under s 288`, `charge under s 288`; punishments `s 288(2)(a)`, `(b)`")

    m.section("289")
    family(m, "289", dc, "`omits precautions with an animal`", "Whether the accused omits sufficient precautions with an animal, with a result section 289(1) of the Penal Code 1871 lists",
           [("f's `knowingly or negligently omits to take sufficient measure with any animal against probable danger to human life or of grievous hurt from it`", "knowingly or negligently omits to take such measure with any animal as is sufficient to guard against probable danger to human life or of grievous hurt"),
            res([LIKELY_GH, ENDANGER, GH, DEATH])],
           "negligence with respect to any animal", recite("did knowingly or negligently omit to take sufficient measures with an animal against probable danger to human life or of grievous hurt, which omission endangered human life or was likely to cause, or caused, grievous hurt or death"),
           "public-safety", "s 289", lead='"A person shall be guilty of an offence who"',
           puns=[or_both("289(2)(a)", "289(2)(a)", 1, maxfine=5000), or_both("289(2)(b)", "289(2)(b)", 6), or_both("289(2)(c)", "289(2)(c)", 7)],
           pun_expr=gravest("289", [(DEATH, "289(2)(c)"), (GH, "289(2)(b)"), (None, "289(2)(a)")]))
    COVERAGE["289"] = ("encoded", "`omits precautions with an animal`, `offence under s 289`, `charge under s 289`; punishments `s 289(2)(a)`-`(c)`")

    # ---------------------------------------------------------------- 290, 291
    m.section("290", extra_comment="Paragraph (a) is the base; (b) (knowledge) and (c) (a second or subsequent conviction) share one heavier punishment. A charge picks (b) or (c) where their leaf holds.")
    pnf = PN
    family(m, "290", pnf, "`is guilty of a public nuisance`", "", [("f's `does any act or is guilty of an illegal omission`", "does any act or is guilty of an illegal omission"),
                                                                   ("(f's `which causes any common injury, danger or annoyance to the public or to the people in general who dwell or occupy property in the vicinity` OR f's `which must necessarily cause injury, obstruction, danger or annoyance to persons who may have occasion to use any public right`)", "which causes common injury, danger or annoyance to the public, or must necessarily cause it to persons using a public right")],
           "public nuisance", recite("did commit a public nuisance"), "public-order", "ss 268, 290", verb_exists=True,
           puns=[Pun("290(a)", "290(a)", "fine which may extend to $2,000", fine="sb", maxfine=2000),
                 or_both("290(b)", "290(b)", months=3, maxfine=2000), or_both("290(c)", "290(c)", months=3, maxfine=2000)],
           pun_expr="IF f's `the offender knew that the act or omission will cause or will probably cause any common injury, danger or annoyance` THEN (`punishment prescribed by s 290(b)`)'s words ELSE IF f's `this is a second or subsequent conviction` THEN (`punishment prescribed by s 290(c)`)'s words ELSE (`punishment prescribed by s 290(a)`)'s words",
           extra=[("f's `the case is not otherwise punishable by this Code`", "in any case not otherwise punishable by this Code")])
    COVERAGE["290"] = ("encoded", "`offence under s 290`, `charge under s 290`; punishments `s 290(a)`-`(c)`")
    m.section("291")
    family(m, "291", pnf, "`continues a public nuisance after injunction`", "Whether the accused repeats or continues a public nuisance after being enjoined by a public servant not to (s 291 of the Penal Code 1871)",
           [("f's `repeats or continues the public nuisance`", "repeats or continues a public nuisance"), ("`is guilty of a public nuisance` f", "a public nuisance (section 268)"),
            ("f's `having been enjoined by a public servant with lawful authority not to repeat or continue the nuisance`", "having been enjoined by any public servant who has lawful authority to issue such injunction not to repeat or continue such nuisance")],
           "continuance of nuisance after injunction to discontinue", recite("having been enjoined by a public servant with lawful authority not to repeat or continue a public nuisance, did repeat or continue that nuisance"),
           "public-order", "s 291", puns=[or_both("291", "291", months=6)])
    COVERAGE["291"] = ("encoded", "`continues a public nuisance after injunction`, `offence under s 291`, `charge under s 291`")

    # ---------------------------------------------------------------- obscenity
    ob = Facts("Obscenity Facts", "The object, act or words, what the accused did with them, and to whom",
               [("the object is an obscene object", "B", "Is it an obscene object - an obscene book, pamphlet, paper, drawing, painting, representation or figure, or any other obscene object, including data capable of conversion into images or writing (s 292(2))? It is deemed not obscene if the dealing is authorised by or under written law (s 292(3), the next leaf)."),
                ("the dealing is authorised by or under any written law", "B", "Is the dealing in the object authorised by or under written law? If so it is deemed not obscene (s 292(3), for ss 292, 292B and 293)"),
                ("the object is kept or used bona fide for religious purposes", "B", "Is it a book, pamphlet, writing, drawing or painting kept or used bona fide for religious purposes, or a representation on or in a temple, an idol car, or kept or used for a religious purpose? (Exception to ss 292 and 292B)"),
                ("sells, lets to hire, distributes, publicly exhibits or puts into circulation the obscene object", "B", "(s 292(1)(a))"),
                ("makes, produces or has in his possession the obscene object for the purposes of sale, hire, distribution, public exhibition or circulation", "B", "(s 292(1)(b))"),
                ("imports, exports or conveys the obscene object for those purposes, or knowing or having reason to believe it will be so dealt with", "B", "(s 292(1)(c))"),
                ("takes part in, or receives profits from, a business in which he knows or has reason to believe obscene objects are so made or dealt with", "B", "(s 292(1)(d))"),
                ("advertises or makes known that a person is engaged or ready to engage in such an act, or that an obscene object can be procured from or through any person", "B", "(s 292(1)(e))"),
                ("offers or attempts to do any such act", "B", "(s 292(1)(f))"),
                ("by electronic means, to 10 or more individuals", "B", "Was the act done (or for the purpose of being done) by electronic means to 10 or more individuals? (s 292(1A)) - the helper `10 or more individuals` decides it from the count"),
                ("the object depicts an image of a person who is, appears to a reasonable observer to be, or is implied to be, below 18 years of age", "B", "(ss 292(1B), 292(1C)(a), 292B(2)) - the helper `below 18 years of age` decides it from an age"),
                ("on 2 or more occasions, sells, lets to hire, distributes, publicly exhibits or circulates by electronic means an obscene object to a total of 10 or more individuals", "B", "(s 292(1C))"),
                ("imports, exports, conveys, sells, lets to hire, distributes, puts into circulation, makes, produces or is in possession of a child sex-doll", "B", "Did the accused so deal in a child sex-doll - an anatomically correct doll, mannequin or robot with the features of (or appearing to a reasonable observer to resemble) a person below 16 years of age, intended for use in sexual activities (s 292A(2))? (s 292A(1))"),
                ("an obscene object is sold, let for hire, distributed, publicly exhibited or circulated to 10 or more individuals on an online location", "B", "(s 292B(1)) - \"online location\" is an internet domain, website, webpage, chatroom, channel, group, forum or other internet location (s 292B(3))"),
                ("develops, maintains, organises, manages, supervises, regulates membership of or access to, or exercises editorial control over, the online location", "B", "(s 292B(1)(a)(i)-(iv)) - whether or not the person provides the online service"),
                ("intended that the online location be used to enable or facilitate the sale, hire, distribution, public exhibition or circulation of obscene objects generally", "B", "(s 292B(1)(b))"),
                ("sells, lets to hire, distributes, exhibits or circulates, or offers or attempts to do so, an obscene object to a person", "B", "(s 293)"),
                ("the person is below 21 years of age", "B", "Was the person below 21 years of age? (s 293) - the helper `below 21 years of age` decides it from the age"),
                ("to the annoyance of others", "B", "Was it done to the annoyance of others? (s 294)"),
                ("does any obscene act in any public place", "B", "(s 294(a))"),
                ("sings, recites or utters any obscene words in or near any public place", "B", "(s 294(b))"),
                WD],
               "Penal Code 1871 ss 292-294 - the operative atoms")
    m.section("292", extra_comment="FORK JO-10: s 292(1) is one offence with limbs (a)-(f); (1A) and (1B) raise its punishment where the dealing is electronic to 10 or more individuals, or the object depicts a person below 18. The charge picks the punishment from those two leaves. Paragraph-by-paragraph pairing of (1A)(a)-(h) with (1)(a)-(f) is collapsed into one leaf.")
    m.add(ob)
    m.helper('''
        @export Whether a number of individuals is "10 or more individuals" (ss 292(1A), 292(1C), 292B(1) of the Penal Code 1871)
        GIVEN n IS A NUMBER @desc The number of individuals
        GIVETH A BOOLEAN
        DECIDE `10 or more individuals` n IF n AT LEAST 10

        ''')
    m.add(pred("`the object is obscene within section 292`", ob, 'Whether an object is an "obscene object" for sections 292, 292B and 293 of the Penal Code 1871, read with s 292(3) and the Exception', '''
            f's `the object is an obscene object`
        AND NOT f's `the dealing is authorised by or under any written law`
        AND NOT f's `the object is kept or used bona fide for religious purposes`
        '''))
    child = "f's `the object depicts an image of a person who is, appears to a reasonable observer to be, or is implied to be, below 18 years of age`"
    elec = "f's `by electronic means, to 10 or more individuals`"
    family(m, "292", ob, "`deals in an obscene object`", "Whether the accused does any act in section 292(1)(a) to (f) of the Penal Code 1871 with an obscene object",
           [("`the object is obscene within section 292` f", "any obscene object (subsections (2), (3) and the Exception)"),
            ("(f's `sells, lets to hire, distributes, publicly exhibits or puts into circulation the obscene object` OR f's `makes, produces or has in his possession the obscene object for the purposes of sale, hire, distribution, public exhibition or circulation` OR f's `imports, exports or conveys the obscene object for those purposes, or knowing or having reason to believe it will be so dealt with` OR f's `takes part in, or receives profits from, a business in which he knows or has reason to believe obscene objects are so made or dealt with` OR f's `advertises or makes known that a person is engaged or ready to engage in such an act, or that an obscene object can be procured from or through any person` OR f's `offers or attempts to do any such act`)",
             "does any act in paragraphs (a) to (f) of subsection (1)")],
           "sale of obscene objects", recite("did sell, distribute, exhibit, circulate, make, possess, import, export or convey, or deal in, an obscene object, or offer or attempt to do so"),
           "obscenity", "s 292",
           puns=[or_both("292(1)", "292(1)", months=3), or_both("292(1A)", "292(1A)", 2),
                 and_fine("292(1B)(a)", "292(1B)(a)", 4, words="imprisonment for a term which may extend to 4 years, and shall also be liable to a fine"), or_both("292(1B)(b)", "292(1B)(b)", 2)],
           pun_expr=f"IF {child} AND {elec} THEN (`punishment prescribed by s 292(1B)(a)`)'s words ELSE IF {child} THEN (`punishment prescribed by s 292(1B)(b)`)'s words ELSE IF {elec} THEN (`punishment prescribed by s 292(1A)`)'s words ELSE (`punishment prescribed by s 292(1)`)'s words")
    m.offence("292(1C)", ob, "distributing obscene objects electronically on 2 or more occasions to 10 or more individuals", '''
            "Whoever"
        AND f's `on 2 or more occasions, sells, lets to hire, distributes, publicly exhibits or circulates by electronic means an obscene object to a total of 10 or more individuals`
        AND `the object is obscene within section 292` f
        ''')
    from lib import charge as _charge
    m.add(_charge("292(1C)", ob, '"distributing obscene objects by electronic means on 2 or more occasions"',
                  f"IF {child} THEN (`punishment prescribed by s 292(1C)(a)`)'s words ELSE (`punishment prescribed by s 292(1C)(b)`)'s words",
                  recite("did on 2 or more occasions sell, distribute, exhibit or circulate by electronic means an obscene object to a total of 10 or more individuals"),
                  [mu("f's `on 2 or more occasions, sells, lets to hire, distributes, publicly exhibits or circulates by electronic means an obscene object to a total of 10 or more individuals`", "on 2 or more occasions, by electronic means, to a total number of 10 or more individuals"),
                   mu("`the object is obscene within section 292` f", "any obscene object")]))
    m.add(and_fine("292(1C)(a)", "292(1C)(a)", 4, words="imprisonment for a term which may extend to 4 years, and shall also be liable to a fine"), or_both("292(1C)(b)", "292(1C)(b)", 2))
    from build import catalogue
    catalogue("292(1C)", "distributing obscene objects by electronic means on 2 or more occasions", "s 292(1C)", "obscenity", ob, ["the object is obscene within section 292"])
    COVERAGE["292"] = ("encoded", "`Obscenity Facts`; `the object is obscene within section 292`, `deals in an obscene object`, `offence under s 292`, `charge under s 292` (punishment from (1), (1A), (1B)(a)/(b)), `offence under s 292(1C)`, `charge under s 292(1C)`; helpers `10 or more individuals`, `below 18 years of age`")

    m.section("292A")
    family(m, "292A", ob, "`deals in a child sex-doll`", "Whether the accused deals in or possesses a child sex-doll (s 292A(1) of the Penal Code 1871)",
           [("f's `imports, exports, conveys, sells, lets to hire, distributes, puts into circulation, makes, produces or is in possession of a child sex-doll`", "imports, exports, conveys, sells, lets to hire, distributes, puts into circulation, makes, produces or is in possession of a child sex-doll")],
           "possession, distribution, etc., of child sex-doll", recite("did import, export, convey, sell, distribute, make, produce or possess a child sex-doll"),
           "obscenity", "s 292A", puns=[or_both("292A", "292A(1)", 2)], lead='"Any person who"')
    COVERAGE["292A"] = ("encoded", "`deals in a child sex-doll`, `offence under s 292A`, `charge under s 292A`; (2) is the leaf's @desc; helper `below 16 years of age`")

    m.section("292B")
    family(m, "292B", ob, "`runs an online location for obscene objects`", "Whether the accused is liable under section 292B(1) of the Penal Code 1871 for an online location used to circulate obscene objects",
           [("f's `an obscene object is sold, let for hire, distributed, publicly exhibited or circulated to 10 or more individuals on an online location`", "if any obscene object is sold, let for hire, distributed, publicly exhibited or circulated to 10 or more individuals on an online location"),
            ("`the object is obscene within section 292` f", "obscene object (section 292(2), (3) and the Exception)"),
            ("f's `develops, maintains, organises, manages, supervises, regulates membership of or access to, or exercises editorial control over, the online location`", "(a) develops and maintains, organises, manages or supervises, manages membership of or access to, or exercises editorial control over the online location"),
            ("f's `intended that the online location be used to enable or facilitate the sale, hire, distribution, public exhibition or circulation of obscene objects generally`", "(b) intended that the online location be used to enable or facilitate the circulation of obscene objects generally")],
           "obscene object on online location", recite("did develop, maintain, manage or control an online location on which an obscene object was circulated to 10 or more individuals, intending that it be used to facilitate the circulation of obscene objects generally"),
           "obscenity", "s 292B", lead='"any person"',
           puns=[and_fine("292B(1)", "292B(1)", 5), and_fine("292B(2)", "292B(2)", 7)],
           pun_expr=f"IF {child} THEN (`punishment prescribed by s 292B(2)`)'s words ELSE (`punishment prescribed by s 292B(1)`)'s words")
    COVERAGE["292B"] = ("encoded", "`runs an online location for obscene objects`, `offence under s 292B`, `charge under s 292B`; punishments `s 292B(1)`, `s 292B(2)`; (3) in @desc")

    m.section("293")
    family(m, "293", ob, "`deals in an obscene object with a young person`", "Whether the accused sells, distributes or exhibits an obscene object to a person below 21 (s 293 of the Penal Code 1871)",
           [("f's `sells, lets to hire, distributes, exhibits or circulates, or offers or attempts to do so, an obscene object to a person`", "sells, lets to hire, distributes, exhibits or circulates, or offers or attempts to do so"),
            ("f's `the person is below 21 years of age`", "to any person below 21 years of age"), ("`the object is obscene within section 292` f", "any obscene object as defined in section 292(2)")],
           "sale, etc., of obscene objects to young person", recite("did sell, distribute, exhibit or circulate an obscene object to a person below 21 years of age, or offer or attempt to do so"),
           "obscenity", "s 293", puns=[or_both("293", "293", 1)])
    COVERAGE["293"] = ("encoded", "`deals in an obscene object with a young person`, `offence under s 293`, `charge under s 293`; helper `below 21 years of age`")

    m.section("294")
    family(m, "294", ob, "`does an obscene act in a public place`", "Whether the accused, to the annoyance of others, does an obscene act or utters obscene words in or near a public place (s 294 of the Penal Code 1871)",
           [("f's `to the annoyance of others`", "to the annoyance of others"),
            ("(f's `does any obscene act in any public place` OR f's `sings, recites or utters any obscene words in or near any public place`)", "(a) does any obscene act in any public place, or (b) sings, recites or utters any obscene words in or near any public place")],
           "obscene acts", recite("did, to the annoyance of others, do an obscene act in a public place, or sing, recite or utter obscene words in or near a public place"),
           "obscenity", "s 294", puns=[or_both("294", "294", months=3)])
    COVERAGE["294"] = ("encoded", "`does an obscene act in a public place`, `offence under s 294`, `charge under s 294`")

    # ---------------------------------------------------------------- Chapter 15
    m.chapter("Chapter 15 - Offences relating to race")
    for n in ["295", "296", "297"]:
        m.repealed(n, "[Repealed by Act 31 of 2019 wef 01/11/2022]")
    rf = Facts("Racial Feelings Facts", "What the accused said, did or showed, and with what intention or knowledge",
               [("with deliberate intention of wounding the racial feelings of any person", "B", "(s 298) - a fault element"),
                ("utters any word or makes any sound in the hearing of that person, makes any gesture or places any object in the sight of that person, or causes any matter to be seen or heard by that person", "B", "(s 298)"),
                ("by words, signs, visible representations or otherwise, knowingly promotes or attempts to promote, on grounds of race, disharmony or feelings of enmity, hatred or ill will between different racial groups", "B", "(s 298A(a))"),
                ("commits any act which he knows is prejudicial to the maintenance of harmony between different racial groups", "B", "(s 298A(b))"),
                ("which disturbs or is likely to disturb the public tranquility", "B", "(s 298A(b))"),
                ("the person", "S", "The person whose racial feelings were to be wounded (s 298), as the charge is to name them"), WD],
               "Penal Code 1871 ss 298, 298A - the operative atoms")
    m.section("298")
    m.add(rf)
    family(m, "298", rf, "`wounds the racial feelings of a person`", "Whether the accused, with deliberate intention of wounding a person's racial feelings, utters words or makes sounds, gestures or objects perceptible to that person (s 298 of the Penal Code 1871)",
           [("f's `with deliberate intention of wounding the racial feelings of any person`", "with deliberate intention of wounding the racial feelings of any person"),
            ("f's `utters any word or makes any sound in the hearing of that person, makes any gesture or places any object in the sight of that person, or causes any matter to be seen or heard by that person`", "utters any word or makes any sound in the hearing, or makes any gesture or places any object in the sight, of that person, or causes any matter to be seen or heard by that person")],
           "uttering words, etc., with deliberate intent to wound the racial feelings of any person",
           'CONCAT "did, with deliberate intention of wounding the racial feelings of one ", f\'s `the person`, ", utter words or make sounds in the hearing of, or make gestures or place objects in the sight of, that person", (`to wit` (f\'s `what was done`))',
           "race", "s 298", puns=[or_both("298", "298", 3)])
    COVERAGE["298"] = ("encoded", "`Racial Feelings Facts`; `wounds the racial feelings of a person`, `offence under s 298`, `charge under s 298`")
    m.section("298A")
    family(m, "298A", rf, "`promotes enmity between racial groups`", "Whether the accused promotes racial enmity (s 298A(a)) or knowingly commits an act prejudicial to racial harmony that disturbs public tranquility (s 298A(b)) of the Penal Code 1871",
           [("(f's `by words, signs, visible representations or otherwise, knowingly promotes or attempts to promote, on grounds of race, disharmony or feelings of enmity, hatred or ill will between different racial groups` OR (f's `commits any act which he knows is prejudicial to the maintenance of harmony between different racial groups` AND f's `which disturbs or is likely to disturb the public tranquility`))",
             "(a) knowingly promotes or attempts to promote racial disharmony, enmity, hatred or ill will, or (b) commits an act he knows is prejudicial to racial harmony which disturbs or is likely to disturb the public tranquility")],
           "promoting enmity between different groups on grounds of race and doing acts prejudicial to maintenance of harmony",
           recite("did knowingly promote or attempt to promote, on grounds of race, disharmony or feelings of enmity, hatred or ill will between different racial groups, or commit an act which you knew was prejudicial to the maintenance of harmony between different racial groups and which disturbed or was likely to disturb the public tranquility"),
           "race", "s 298A", puns=[or_both("298A", "298A", 3)])
    COVERAGE["298A"] = ("encoded", "`promotes enmity between racial groups`, `offence under s 298A`, `charge under s 298A`")


PN = None

