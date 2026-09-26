"""Chapter 11 ss 217-229, and Chapter 12 (ss 230-263)."""
from lib import Facts, Pun, pred, mu, or_both, and_fine
from build import COVERAGE, family, recite

WD = ("what was done", "S", "What the accused did, as it is to read in the charge after \"to wit,\"")
PS = ("being a public servant", "B", "Was the accused a public servant (s 21)? - the drill-down is `public servant within section 21` in pc-general")


def ch11c(m):
    # ------------------------------------------------------------ ss 217-220
    pj = Facts("Public Servant Justice Facts", "The public servant's office, what he did, and what he knew or intended",
               [PS,
                ("knowingly disobeys any direction of the law as to the way in which he is to conduct himself as such public servant", "B", "Did the accused knowingly disobey a direction of the law as to how he was to conduct himself as a public servant? (s 217)"),
                ("charged as such public servant with the preparation of any record or other writing", "B", "Was the accused, as a public servant, charged with preparing a record or other writing? (s 218)"),
                ("frames that record or writing in a manner which he knows to be incorrect", "B", "Did the accused frame it in a manner he knew to be incorrect? (s 218)"),
                ("intending or knowing it to be likely that he will thereby cause loss or injury to the public or to any person", "B", "Did the accused intend, or know it likely, to cause loss or injury to the public or any person? (s 218) - a fault element"),
                ("intending or knowing it to be likely that he will thereby save any person from legal punishment or subject him to a lesser punishment", "B", "Did the accused intend, or know it likely, to save any person from legal punishment (or, for s 217, subject him to a lesser punishment than he is liable to)? (ss 217, 218) - a fault element"),
                ("intending or knowing it to be likely that he will thereby save any property from forfeiture or any charge to which it is liable by law", "B", "Did the accused intend, or know it likely, to save property from forfeiture or a charge to which it is liable by law? (ss 217, 218) - a fault element"),
                ("corruptly", "B", "Did the accused act corruptly? (ss 219, 220) - the Code does not define the word"),
                ("with intent to cause injury to any person", "B", "Did the accused intend to cause injury (s 44) to any person? (ss 219, 220) - a fault element"),
                ("makes or pronounces in any stage of a judicial proceeding any report, order, verdict or decision", "B", "Did the accused make or pronounce a report, order, verdict or decision in a stage of a judicial proceeding? (s 219)"),
                ("which he knows to be contrary to law", "B", "Did the accused know it to be contrary to law? (s 219) - a fault element"),
                ("being in an office that gives him legal authority to commit persons for trial or to confinement, or to keep persons in confinement", "B", "Did the accused hold an office giving him legal authority to commit persons for trial or to confinement, or to keep persons in confinement? (s 220(1))"),
                ("commits a person for trial or to confinement, or keeps a person in confinement, in the exercise of that authority", "B", "In the exercise of that authority, did the accused commit a person for trial or to confinement, or keep a person in confinement? (s 220(1)(a))"),
                ("knowing that in doing so he is acting contrary to law", "B", "Did the accused know that in doing so he was acting contrary to law? (s 220(1)(b)) - a fault element"),
                WD],
               "Penal Code 1871 ss 217-220 - the operative atoms")
    m.section("217")
    m.add(pj)
    ps = ("f's `being a public servant`", "being a public servant")
    save_p = "f's `intending or knowing it to be likely that he will thereby save any person from legal punishment or subject him to a lesser punishment`"
    save_q = "f's `intending or knowing it to be likely that he will thereby save any property from forfeiture or any charge to which it is liable by law`"
    family(m, "217", pj, "`disobeys a direction of law to save a person from punishment`",
           'Whether a public servant knowingly disobeys a direction of law intending or knowing it likely to save a person from punishment or property from forfeiture (s 217 of the Penal Code 1871)',
           [ps, ("f's `knowingly disobeys any direction of the law as to the way in which he is to conduct himself as such public servant`", "knowingly disobeys any direction of the law as to the way in which he is to conduct himself as such public servant"),
            (f"({save_p} OR {save_q})", "intending or knowing it likely thereby to save any person from legal punishment, or any property from forfeiture or charge")],
           "public servant disobeying a direction of law with intent to save person from punishment or property from forfeiture",
           recite("being a public servant, did knowingly disobey a direction of the law as to the way in which you were to conduct yourself as such public servant, intending thereby to save, or knowing it to be likely that you would thereby save, a person from legal punishment or property from forfeiture"),
           "public-servant-justice", "s 217", puns=[or_both("217", "217", 2)])
    COVERAGE["217"] = ("encoded", "`Public Servant Justice Facts`; `disobeys a direction of law to save a person from punishment`, `offence under s 217`, `charge under s 217`")

    m.section("218")
    family(m, "218", pj, "`frames an incorrect record to save a person from punishment`",
           'Whether a public servant frames a record or writing he knows to be incorrect, with the intent or knowledge s 218 of the Penal Code 1871 requires',
           [ps, ("f's `charged as such public servant with the preparation of any record or other writing`", "being, as such public servant, charged with the preparation of any record or other writing"),
            ("f's `frames that record or writing in a manner which he knows to be incorrect`", "frames that record or writing in a manner which he knows to be incorrect"),
            (f"(f's `intending or knowing it to be likely that he will thereby cause loss or injury to the public or to any person` OR {save_p} OR {save_q})", "with intent to cause, or knowing it likely to cause, loss or injury, or to save any person from legal punishment or property from forfeiture")],
           "public servant framing an incorrect record or writing with intent to save person from punishment, or property from forfeiture",
           recite("being a public servant charged with the preparation of a record or writing, did frame that record or writing in a manner which you knew to be incorrect, with intent to cause, or knowing it to be likely that you would thereby cause, loss or injury, or to save a person from legal punishment or property from forfeiture"),
           "public-servant-justice", "s 218", puns=[or_both("218", "218", 3)])
    COVERAGE["218"] = ("encoded", "`frames an incorrect record to save a person from punishment`, `offence under s 218`, `charge under s 218`")

    m.section("219")
    family(m, "219", pj, "`makes an order in a judicial proceeding known to be contrary to law`",
           'Whether a public servant, corruptly or with intent to injure, makes a report, order, verdict or decision in a judicial proceeding which he knows to be contrary to law (s 219 of the Penal Code 1871)',
           [ps, ("(f's corruptly OR f's `with intent to cause injury to any person`)", "corruptly or with intent to cause injury to any person"),
            ("f's `makes or pronounces in any stage of a judicial proceeding any report, order, verdict or decision`", "makes or pronounces in any stage of a judicial proceeding any report, order, verdict or decision"),
            ("f's `which he knows to be contrary to law`", "which he knows to be contrary to law")],
           "public servant in a judicial proceeding making an order which he knows to be contrary to law",
           recite("being a public servant, did corruptly or with intent to cause injury to a person make or pronounce in a stage of a judicial proceeding a report, order, verdict or decision which you knew to be contrary to law"),
           "public-servant-justice", "s 219", puns=[or_both("219", "219", 7)])
    COVERAGE["219"] = ("encoded", "`makes an order in a judicial proceeding known to be contrary to law`, `offence under s 219`, `charge under s 219`")

    m.section("220")
    family(m, "220", pj, "`commits a person for trial or confinement knowing it contrary to law`",
           'Whether a person with legal authority to commit or confine commits or keeps a person in confinement corruptly or with intent to injure, knowing it contrary to law (s 220(1) of the Penal Code 1871)',
           [("f's `being in an office that gives him legal authority to commit persons for trial or to confinement, or to keep persons in confinement`", "being in an office that gives him legal authority to commit persons for trial or to confinement, or to keep persons in confinement"),
            ("(f's corruptly OR f's `with intent to cause injury to any person`)", "(a) corruptly or with intent to cause injury to any person"),
            ("f's `commits a person for trial or to confinement, or keeps a person in confinement, in the exercise of that authority`", "(a) commits the person for trial or to confinement, or keeps the person in confinement, in the exercise of that authority"),
            ("f's `knowing that in doing so he is acting contrary to law`", "(b) knowing that in doing so he is acting contrary to law")],
           "commitment for trial or confinement by person having authority who knows he is acting contrary to law",
           recite("being in an office giving you legal authority to commit persons for trial or to confinement, did corruptly or with intent to cause injury commit or keep a person in confinement in the exercise of that authority, knowing that in doing so you were acting contrary to law"),
           "public-servant-justice", "s 220", puns=[or_both("220", "220(2)", words="imprisonment for a term that may extend to 7 years, or with fine, or with both", years=7)],
           comment="s 220(1) defines the offence and s 220(2) punishes it; the charge is laid under section 220 (FORK JO-6 on whether to cite \"220(1)\" or \"220(2)\").")
    COVERAGE["220"] = ("encoded", "`commits a person for trial or confinement knowing it contrary to law`, `offence under s 220`, `charge under s 220`; punishment `s 220` (section field \"220(2)\")")

    # ------------------------------------------------------------ ss 221-223, 225A
    ep = Facts("Escape by Public Servant Facts", "The public servant's duty to apprehend or confine, the person concerned, and what the public servant did",
               [PS,
                ("legally bound as such public servant to apprehend or to keep in confinement the person", "B", "Was the accused, as a public servant, legally bound to apprehend or keep the person in confinement? (ss 221-223, 225A)"),
                ("the person is charged with or liable to be apprehended for an offence", "B", "Was the person charged with, or liable to be apprehended for, an offence? (s 221)"),
                ("the person is under sentence of a court of justice for an offence, or lawfully committed to custody", "B", "Was the person under sentence of a court for an offence, or lawfully committed to custody? (s 222)"),
                ("the person is charged with or convicted of an offence, or lawfully committed to custody", "B", "Was the person charged with or convicted of an offence, or lawfully committed to custody? (s 223)"),
                ("intentionally omits to apprehend the person", "B", "Did the accused intentionally omit to apprehend the person? (ss 221, 222)"),
                ("intentionally suffers the person to escape", "B", "Did the accused intentionally suffer the person to escape? (ss 221, 222)"),
                ("intentionally aids the person in escaping or attempting to escape from confinement", "B", "Did the accused intentionally aid the person in escaping or attempting to escape? (ss 221, 222)"),
                ("negligently suffers the person to escape from confinement", "B", "Did the accused negligently (s 26F) suffer the person to escape from confinement? (s 223)"),
                ("the case is not provided for in section 221, 222 or 223, or in any other law for the time being in force", "B", "Is the case one NOT provided for in s 221, 222 or 223 or in any other law in force? (s 225A)"),
                ("omits to apprehend the person or suffers him to escape from confinement", "B", "Did the accused omit to apprehend the person, or suffer him to escape from confinement? (s 225A)"),
                ("does so intentionally", "B", "Did the accused do so intentionally? (s 225A(a))"),
                ("does so negligently", "B", "Did the accused do so negligently? (s 225A(b))"),
                ("the offence is punishable with death", "B", "Is the offence the person was charged with or liable to be apprehended for punishable with death? (s 221(a))"),
                ("the offence is punishable with imprisonment for life, or imprisonment for a term which may extend to 20 years", "B", "Is that offence punishable with imprisonment for life, or for a term which may extend to 20 years? (s 221(b))"),
                ("the offence is punishable with imprisonment for a term less than 20 years", "B", "Is that offence punishable with imprisonment for a term less than 20 years? (s 221(c))"),
                ("the person is under sentence of death", "B", "Is the person under sentence of death? (s 222(a))"),
                ("the person is subject by a sentence of a court of justice, or by commutation, to imprisonment for a term of 20 years or upwards", "B", "Is the person subject, by a court's sentence or its commutation, to imprisonment for 20 years or upwards? (s 222(b))"),
                ("the person is subject by a sentence of a court of justice to imprisonment for a term less than 20 years, or was lawfully committed to custody", "B", "Is the person subject by a court's sentence to imprisonment for less than 20 years, or was he lawfully committed to custody? (s 222(c))"),
                ("the person", "S", "The person concerned, as the charge is to name them"),
                WD],
               "Penal Code 1871 ss 221-223, 225A - the operative atoms")
    m.section("221")
    m.add(ep)
    bound = ("f's `legally bound as such public servant to apprehend or to keep in confinement the person`", "legally bound as such public servant to apprehend or to keep in confinement the person")
    acts = ("(f's `intentionally omits to apprehend the person` OR f's `intentionally suffers the person to escape` OR f's `intentionally aids the person in escaping or attempting to escape from confinement`)",
            "intentionally omits to apprehend such person, or intentionally suffers such person to escape, or intentionally aids such person in escaping or attempting to escape")
    family(m, "221", ep, "`intentionally omits to apprehend a person charged with an offence`",
           'Whether a public servant bound to apprehend or confine a person charged with or liable to apprehension for an offence intentionally omits to apprehend him, or suffers or aids his escape (s 221 of the Penal Code 1871)',
           [ps, bound, ("f's `the person is charged with or liable to be apprehended for an offence`", "any person charged with or liable to be apprehended for an offence"), acts],
           "intentional omission to apprehend on the part of a public servant bound by law to apprehend",
           recite("being a public servant legally bound to apprehend or keep in confinement a person charged with or liable to be apprehended for an offence, did intentionally omit to apprehend that person, or intentionally suffer or aid that person to escape"),
           "escape", "s 221",
           puns=[and_fine("221(a)", "221(a)", 10, words="imprisonment for a term which may extend to 10 years, and shall also be liable to fine"),
                 and_fine("221(b)", "221(b)", 7, words="imprisonment for a term which may extend to 7 years, and shall also be liable to fine"),
                 or_both("221(c)", "221(c)", 5)],
           pun_expr="IF f's `the offence is punishable with death` THEN (`punishment prescribed by s 221(a)`)'s words ELSE IF f's `the offence is punishable with imprisonment for life, or imprisonment for a term which may extend to 20 years` THEN (`punishment prescribed by s 221(b)`)'s words ELSE (`punishment prescribed by s 221(c)`)'s words",
           extra=[("(f's `the offence is punishable with death` OR f's `the offence is punishable with imprisonment for life, or imprisonment for a term which may extend to 20 years` OR f's `the offence is punishable with imprisonment for a term less than 20 years`)", "the offence is punishable with death, with imprisonment for life or up to 20 years, or with imprisonment for a term less than 20 years")])
    COVERAGE["221"] = ("encoded", "`Escape by Public Servant Facts`; `intentionally omits to apprehend a person charged with an offence`, `offence under s 221`, `charge under s 221`; punishments `s 221(a)`-`(c)`")

    m.section("222")
    family(m, "222", ep, "`intentionally omits to apprehend a person under sentence`",
           'Whether a public servant bound to apprehend or confine a person under sentence or lawfully committed to custody intentionally omits to apprehend him, or suffers or aids his escape (s 222 of the Penal Code 1871)',
           [ps, bound, ("f's `the person is under sentence of a court of justice for an offence, or lawfully committed to custody`", "any person under sentence of a court of justice for any offence, or lawfully committed to custody"), acts],
           "intentional omission to apprehend on the part of a public servant bound by law to apprehend person under sentence of a court of justice",
           recite("being a public servant legally bound to apprehend or keep in confinement a person under sentence of a court of justice or lawfully committed to custody, did intentionally omit to apprehend that person, or intentionally suffer or aid that person to escape"),
           "escape", "s 222",
           puns=[Pun("222(a)", "222(a)", "imprisonment for life or with imprisonment for a term which may extend to 20 years, and shall also be liable to fine", life="or", imp="or", maxm=240, fine="al"),
                 and_fine("222(b)", "222(b)", 10),
                 or_both("222(c)", "222(c)", words="imprisonment for a term which may extend to 7 years, or with fine or with both", years=7)],
           pun_expr="IF f's `the person is under sentence of death` THEN (`punishment prescribed by s 222(a)`)'s words ELSE IF f's `the person is subject by a sentence of a court of justice, or by commutation, to imprisonment for a term of 20 years or upwards` THEN (`punishment prescribed by s 222(b)`)'s words ELSE (`punishment prescribed by s 222(c)`)'s words",
           extra=[("(f's `the person is under sentence of death` OR f's `the person is subject by a sentence of a court of justice, or by commutation, to imprisonment for a term of 20 years or upwards` OR f's `the person is subject by a sentence of a court of justice to imprisonment for a term less than 20 years, or was lawfully committed to custody`)", "the person is under sentence of death, or of imprisonment, or was lawfully committed to custody")])
    COVERAGE["222"] = ("encoded", "`intentionally omits to apprehend a person under sentence`, `offence under s 222`, `charge under s 222`; punishments `s 222(a)`-`(c)`")

    m.section("223")
    family(m, "223", ep, "`negligently suffers a person to escape`",
           'Whether a public servant bound to keep a person in confinement negligently suffers him to escape (s 223 of the Penal Code 1871)',
           [ps, bound, ("f's `the person is charged with or convicted of an offence, or lawfully committed to custody`", "any person charged with or convicted of any offence, or lawfully committed to custody"),
            ("f's `negligently suffers the person to escape from confinement`", "negligently suffers such person to escape from confinement")],
           "escape from confinement negligently suffered by a public servant",
           recite("being a public servant legally bound to keep in confinement a person charged with or convicted of an offence, or lawfully committed to custody, did negligently suffer that person to escape from confinement"),
           "escape", "s 223", puns=[or_both("223", "223", 2)])
    COVERAGE["223"] = ("encoded", "`negligently suffers a person to escape`, `offence under s 223`, `charge under s 223`")

    # ------------------------------------------------------------ ss 224, 225, 225B
    es = Facts("Escape Facts", "The apprehension or custody concerned, and what the accused did to resist it or escape from it",
               [("intentionally offers resistance or illegal obstruction to the lawful apprehension of himself", "B", "Did the accused intentionally offer resistance or illegal obstruction to his own lawful apprehension? (ss 224, 225B)"),
                ("for an offence with which he is charged or of which he has been convicted", "B", "Was that apprehension or custody for an offence with which he was charged or of which he had been convicted? (s 224)"),
                ("escapes or attempts to escape from custody in which he is lawfully detained", "B", "Did the accused escape, or attempt to escape, from custody in which he was lawfully detained? (ss 224, 225B)"),
                ("intentionally offers resistance or illegal obstruction to the lawful apprehension of another person", "B", "Did the accused intentionally offer resistance or illegal obstruction to the lawful apprehension of another person? (ss 225, 225B)"),
                ("rescues or attempts to rescue another person from custody in which that person is lawfully detained", "B", "Did the accused rescue, or attempt to rescue, another person from custody in which that person was lawfully detained? (ss 225, 225B)"),
                ("the other person is apprehended or detained for an offence", "B", "Was the other person being apprehended, or detained, for an offence? (s 225)"),
                ("the other person is charged with or liable to be apprehended for an offence punishable with imprisonment for life or imprisonment for a term which may extend to 20 years", "B", "(s 225(b))"),
                ("the other person is charged with or liable to be apprehended for an offence punishable with death", "B", "(s 225(c))"),
                ("the other person is liable under a sentence of a court of justice, or by commutation, to imprisonment for a term of 10 years or upwards", "B", "(s 225(d))"),
                ("the other person is under sentence of death", "B", "(s 225(e))"),
                ("the case is not provided for in section 224 or 225, or in any other law for the time being in force", "B", "Is the case one NOT provided for in s 224 or 225 or in any other law in force? (s 225B)"),
                ("the person", "S", "Whose apprehension or custody it was, as the charge is to name them (for ss 225 and 225B)"),
                WD],
               "Penal Code 1871 ss 224, 225, 225B - the operative atoms")
    m.section("224", extra_comment="The Explanation (punishment is in addition to that for the original offence) is a sentencing rule, not an element; it rides here as a comment.")
    m.add(es)
    family(m, "224", es, "`resists or escapes lawful apprehension for his own offence`",
           'Whether the accused intentionally resists his own lawful apprehension, or escapes or attempts to escape lawful custody, for an offence he is charged with or convicted of (s 224 of the Penal Code 1871)',
           [("(f's `intentionally offers resistance or illegal obstruction to the lawful apprehension of himself` OR f's `escapes or attempts to escape from custody in which he is lawfully detained`)", "intentionally offers any resistance or illegal obstruction to the lawful apprehension of himself, or escapes or attempts to escape from lawful custody"),
            ("f's `for an offence with which he is charged or of which he has been convicted`", "for any offence with which he is charged, or of which he has been convicted")],
           "resistance or obstruction by a person to his lawful apprehension",
           recite("did intentionally offer resistance or illegal obstruction to your lawful apprehension, or escape or attempt to escape from custody in which you were lawfully detained, for an offence with which you were charged or of which you had been convicted"),
           "escape", "s 224", puns=[or_both("224", "224", 2)])
    COVERAGE["224"] = ("encoded", "`Escape Facts`; `resists or escapes lawful apprehension for his own offence`, `offence under s 224`, `charge under s 224`")

    m.section("225", extra_comment="Paragraph (a) is the base punishment; (b)-(e) aggravate it by the other person's situation. Where more than one aggravating paragraph is made out, the charge picks the heaviest in the order (e), (c), (d), (b) - FORK JO-7.")
    p225 = [or_both("225(a)", "225(a)", 5), and_fine("225(b)", "225(b)", 7), and_fine("225(c)", "225(c)", 10), and_fine("225(d)", "225(d)", 10),
            Pun("225(e)", "225(e)", "imprisonment for life or imprisonment for a term not exceeding 15 years, and shall also be liable to fine", life="or", imp="or", maxm=180, fine="al")]
    family(m, "225", es, "`resists the lawful apprehension of another person`",
           'Whether the accused intentionally resists the lawful apprehension of another person for an offence, or rescues or attempts to rescue him from lawful custody (s 225 of the Penal Code 1871)',
           [("(f's `intentionally offers resistance or illegal obstruction to the lawful apprehension of another person` OR f's `rescues or attempts to rescue another person from custody in which that person is lawfully detained`)", "intentionally offers any resistance or illegal obstruction to the lawful apprehension of any other person, or rescues or attempts to rescue any other person from lawful custody"),
            ("f's `the other person is apprehended or detained for an offence`", "for an offence")],
           "resistance or obstruction to the lawful apprehension of another person",
           'CONCAT "did intentionally offer resistance or illegal obstruction to the lawful apprehension of one ", f\'s `the person`, ", or rescue or attempt to rescue that person from lawful custody, for an offence", (`to wit` (f\'s `what was done`))',
           "escape", "s 225", puns=p225,
           pun_expr="IF f's `the other person is under sentence of death` THEN (`punishment prescribed by s 225(e)`)'s words ELSE IF f's `the other person is charged with or liable to be apprehended for an offence punishable with death` THEN (`punishment prescribed by s 225(c)`)'s words ELSE IF f's `the other person is liable under a sentence of a court of justice, or by commutation, to imprisonment for a term of 10 years or upwards` THEN (`punishment prescribed by s 225(d)`)'s words ELSE IF f's `the other person is charged with or liable to be apprehended for an offence punishable with imprisonment for life or imprisonment for a term which may extend to 20 years` THEN (`punishment prescribed by s 225(b)`)'s words ELSE (`punishment prescribed by s 225(a)`)'s words")
    COVERAGE["225"] = ("encoded", "`resists the lawful apprehension of another person`, `offence under s 225`, `charge under s 225`; punishments `s 225(a)`-`(e)`")

    m.section("225A")
    family(m, "225A", ep, "`omits to apprehend in a case not otherwise provided for`",
           'Whether a public servant bound to apprehend or confine a person, in a case not provided for elsewhere, omits to apprehend him or suffers his escape, intentionally or negligently (s 225A of the Penal Code 1871)',
           [ps, bound, ("f's `the case is not provided for in section 221, 222 or 223, or in any other law for the time being in force`", "in any case not provided for in section 221, 222 or 223, or in any other law"),
            ("f's `omits to apprehend the person or suffers him to escape from confinement`", "omits to apprehend that person, or suffers him to escape from confinement"),
            ("(f's `does so intentionally` OR f's `does so negligently`)", "(a) intentionally or (b) negligently")],
           "public servant omitting to apprehend or suffering other persons to escape in cases not already provided for",
           recite("being a public servant legally bound to apprehend or keep in confinement a person, did omit to apprehend that person or suffer that person to escape from confinement"),
           "escape", "s 225A", puns=[or_both("225A(a)", "225A(a)", 3), or_both("225A(b)", "225A(b)", 2)],
           pun_expr="IF f's `does so intentionally` THEN (`punishment prescribed by s 225A(a)`)'s words ELSE (`punishment prescribed by s 225A(b)`)'s words")
    COVERAGE["225A"] = ("encoded", "`omits to apprehend in a case not otherwise provided for`, `offence under s 225A`, `charge under s 225A`; punishments `s 225A(a)`, `(b)`")

    m.section("225B")
    family(m, "225B", es, "`resists apprehension or escapes in a case not otherwise provided for`",
           'Whether the accused, in a case not provided for elsewhere, intentionally resists lawful apprehension, escapes lawful custody or rescues another from it (s 225B of the Penal Code 1871)',
           [("f's `the case is not provided for in section 224 or 225, or in any other law for the time being in force`", "in any case not provided for in section 224 or 225, or in any other law"),
            ("(f's `intentionally offers resistance or illegal obstruction to the lawful apprehension of himself` OR f's `intentionally offers resistance or illegal obstruction to the lawful apprehension of another person` OR f's `escapes or attempts to escape from custody in which he is lawfully detained` OR f's `rescues or attempts to rescue another person from custody in which that person is lawfully detained`)",
             "intentionally offers any resistance or illegal obstruction to lawful apprehension, or escapes or attempts to escape from lawful custody, or rescues or attempts to rescue any other person from lawful custody")],
           "resistance or obstruction to lawful apprehension, or escape, or rescue, in cases not otherwise provided for",
           recite("did intentionally offer resistance or illegal obstruction to lawful apprehension, or escape or attempt to escape from lawful custody, or rescue or attempt to rescue another person from lawful custody"),
           "escape", "s 225B", puns=[or_both("225B", "225B", 1)])
    COVERAGE["225B"] = ("encoded", "`resists apprehension or escapes in a case not otherwise provided for`, `offence under s 225B`, `charge under s 225B`")

    # ------------------------------------------------------------ s 225C
    dl = Facts("Disobedience of Law Facts", "What the law in force prohibited or enjoined, and what the accused did or omitted",
               [("does anything which by any law in force in Singapore he is prohibited from doing", "B", "Did the accused do something a law in force in Singapore prohibits him from doing? (s 225C)"),
                ("omits to do anything which by any law in force in Singapore he is enjoined to do", "B", "Did the accused omit to do something a law in force in Singapore enjoins him to do? (s 225C)"),
                ("no special punishment is provided by the law for such commission or omission", "B", "Is there NO special punishment provided by that law for the act or omission? (s 225C)"),
                ("the law", "S", "The law prohibiting or enjoining it, as the charge is to name it"), WD],
               "Penal Code 1871 s 225C - the operative atoms")
    m.section("225C")
    m.add(dl)
    family(m, "225C", dl, "`disobeys a law where no special punishment is provided`",
           'Whether the accused does what a law in force prohibits, or omits what it enjoins, where no special punishment is provided (s 225C of the Penal Code 1871)',
           [("(f's `does anything which by any law in force in Singapore he is prohibited from doing` OR f's `omits to do anything which by any law in force in Singapore he is enjoined to do`)", "does anything which by any law in force in Singapore he is prohibited from doing, or omits to do anything which he is so enjoined to do"),
            ("f's `no special punishment is provided by the law for such commission or omission`", "when no special punishment is provided by the law for such commission or omission")],
           "offences against laws of Singapore where no special punishment is provided",
           'CONCAT "did an act which you were prohibited from doing, or omitted to do an act which you were enjoined to do, by ", f\'s `the law`, ", for which no special punishment is provided by that law", (`to wit` (f\'s `what was done`))',
           "general-disobedience", "s 225C", puns=[Pun("225C", "225C", "fine not exceeding $2,000", fine="sb", maxfine=2000)])
    COVERAGE["225C"] = ("encoded", "`Disobedience of Law Facts`; `disobeys a law where no special punishment is provided`, `offence under s 225C`, `charge under s 225C`")

    m.repealed("226", "[Repealed by Act 31 of 2023 wef 30/05/2025]")
    m.repealed("227", "[Repealed by Act 1 of 2014]")

    # ------------------------------------------------------------ ss 228, 229
    cp = Facts("Court Proceedings Facts", "What the accused did to or in a judicial proceeding or ADR process",
               [("intentionally offers any insult to a public servant", "B", "Did the accused intentionally offer an insult to a public servant? (s 228) - for s 228 a judge as defined in the Administration of Justice (Protection) Act 2016 is not a public servant (s 21(2))"),
                ("intentionally causes any interruption to a public servant", "B", "Did the accused intentionally cause an interruption to a public servant? (s 228)"),
                ("while the public servant is sitting in any stage of a judicial proceeding", "B", "Was the public servant then sitting in a stage of a judicial proceeding? (s 228)"),
                ("while the public servant is conducting mediation or other alternative dispute resolution process under written law", "B", "Was the public servant then conducting a mediation or other ADR process under written law? (s 228)"),
                ("by personation or otherwise, intentionally causes or knowingly suffers himself to be returned, empanelled or sworn as an assessor", "B", "Did the accused, by personation or otherwise, intentionally cause or knowingly suffer himself to be returned, empanelled or sworn as an assessor? (s 229)"),
                ("in a case in which he knows that he is not entitled by law to be so returned, empanelled or sworn", "B", "Did he know he was not entitled by law to be so returned, empanelled or sworn? (s 229)"),
                ("knowing himself to have been so returned, empanelled or sworn contrary to law, voluntarily serves as such assessor", "B", "Knowing he had been returned, empanelled or sworn contrary to law, did he voluntarily serve as assessor? (s 229)"),
                ("the public servant", "S", "The public servant, as the charge is to name them"), WD],
               "Penal Code 1871 ss 228, 229 - the operative atoms")
    m.section("228")
    m.add(cp)
    family(m, "228", cp, "`insults or interrupts a public servant sitting in a judicial proceeding`",
           'Whether the accused intentionally insults or interrupts a public servant sitting in a judicial proceeding or conducting ADR under written law (s 228 of the Penal Code 1871)',
           [("(f's `intentionally offers any insult to a public servant` OR f's `intentionally causes any interruption to a public servant`)", "intentionally offers any insult or causes any interruption to any public servant"),
            ("(f's `while the public servant is sitting in any stage of a judicial proceeding` OR f's `while the public servant is conducting mediation or other alternative dispute resolution process under written law`)", "while such public servant is sitting in any stage of a judicial proceeding or conducting any mediation or other ADR process under written law")],
           "intentional insult or interruption to a public servant sitting in a judicial proceeding",
           'CONCAT "did intentionally offer an insult or cause an interruption to ", f\'s `the public servant`, ", a public servant, while sitting in a stage of a judicial proceeding or conducting a mediation or other alternative dispute resolution process under written law", (`to wit` (f\'s `what was done`))',
           "court-proceedings", "s 228", puns=[or_both("228", "228", 1, maxfine=5000)])
    COVERAGE["228"] = ("encoded", "`Court Proceedings Facts`; `insults or interrupts a public servant sitting in a judicial proceeding`, `offence under s 228`, `charge under s 228`")

    m.section("229")
    family(m, "229", cp, "`personates an assessor`",
           'Whether the accused causes himself to be returned, empanelled or sworn as an assessor knowing he is not entitled, or knowingly serves when wrongly returned (s 229 of the Penal Code 1871)',
           [("((f's `by personation or otherwise, intentionally causes or knowingly suffers himself to be returned, empanelled or sworn as an assessor` AND f's `in a case in which he knows that he is not entitled by law to be so returned, empanelled or sworn`) OR f's `knowing himself to have been so returned, empanelled or sworn contrary to law, voluntarily serves as such assessor`)",
             "intentionally causes or knowingly suffers himself to be returned, empanelled or sworn as an assessor knowing he is not entitled, or knowingly serves as such assessor contrary to law")],
           "personation of an assessor",
           recite("did cause or suffer yourself to be returned, empanelled or sworn as an assessor knowing that you were not entitled by law to be, or knowing yourself to have been so returned contrary to law did voluntarily serve as such assessor"),
           "court-proceedings", "s 229", puns=[or_both("229", "229", 2)])
    COVERAGE["229"] = ("encoded", "`personates an assessor`, `offence under s 229`, `charge under s 229`")

    ch12(m)


def ch12(m):
    m.chapter("Chapter 12 - Offences relating to Government stamps")
    for n in ["230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "241A", "242", "243"]:
        m.repealed(n, "[Repealed by Act 15 of 2019]")
    m.repealed("243A", "[Repealed by Act 51 of 2007]")
    m.parts.append("-- [There are no sections 244 and 245.]\n")
    COVERAGE["244-245"] = ("absent", "The Code prints \"[There are no sections 244 and 245.]\"")
    for n in ["246", "247", "248", "249", "250", "251", "252", "253", "254", "254A"]:
        m.repealed(n, "[Repealed by Act 15 of 2019]")

    gs = Facts("Government Stamp Facts", "The stamp or instrument, and what the accused did with it and knew of it",
               [("a stamp issued by the Government for the purpose of revenue", "B", "Is the stamp concerned (or counterfeited) one issued by the Government for the purpose of revenue? It includes a stamp certificate issued under the Stamp Duties Act 1929 (s 255(2), for ss 255-262)."),
                ("counterfeits the stamp", "B", "Did the accused counterfeit the stamp (s 28)? Making a genuine stamp of one denomination appear like a genuine stamp of another is counterfeiting (s 255 Explanation)."),
                ("knowingly performs any part of the process of counterfeiting the stamp", "B", "Did the accused knowingly perform any part of the process of counterfeiting it? (s 255(1))"),
                ("has in his possession any instrument or material", "B", "Did the accused have an instrument or material in his possession? (s 256)"),
                ("makes, performs any part of the process of making, buys, sells or disposes of any instrument", "B", "Did the accused make (or perform part of the process of making), buy, sell or dispose of an instrument? (s 257)"),
                ("for the purpose of being used, or knowing or having reason to believe that it is intended to be used, for counterfeiting the stamp", "B", "Was the instrument or material for the purpose of counterfeiting such a stamp, or did the accused know or have reason to believe it was intended to be so used? (ss 256, 257)"),
                ("sells or offers for sale the stamp", "B", "Did the accused sell or offer the stamp for sale? (s 258)"),
                ("knows or has reason to believe the stamp to be a counterfeit", "B", "Did the accused know, or have reason to believe, the stamp to be a counterfeit? (s 258) - a fault element"),
                ("has in his possession the stamp", "B", "Did the accused have the stamp in his possession? (s 259)"),
                ("knows the stamp to be a counterfeit", "B", "Did the accused know the stamp to be a counterfeit? (ss 259, 260) - a fault element"),
                ("intending to use or dispose of it as a genuine stamp, or in order that it may be used as a genuine stamp", "B", "Did the accused intend to use or dispose of it as genuine, or that it may be used as genuine? (s 259)"),
                ("uses the stamp as genuine", "B", "Did the accused use the stamp as genuine? (s 260)"),
                ("fraudulently or with intent to cause loss to the Government", "B", "Did the accused act fraudulently (s 25) or with intent to cause loss to the Government? (ss 261-263)"),
                ("removes or effaces from a substance bearing the stamp any writing or document for which the stamp has been used", "B", "Did the accused remove or efface, from a substance bearing the stamp, a writing or document for which it had been used? (s 261)"),
                ("removes from a writing or document a stamp which has been used for it", "B", "Did the accused remove from a writing or document a stamp used for it? (s 261)"),
                ("in order that the stamp may be used for a different writing or document", "B", "Was that done so the stamp could be used for a different writing or document? (s 261)"),
                ("uses the stamp for any purpose", "B", "Did the accused use the stamp for any purpose? (s 262)"),
                ("knows the stamp to have been before used", "B", "Did the accused know the stamp had been used before? (ss 262, 263) - a fault element"),
                ("erases or removes from the stamp any mark put or impressed upon it for the purpose of denoting that it has been used", "B", "Did the accused erase or remove from the stamp a mark denoting that it had been used? (s 263)"),
                ("knowingly has in his possession, or sells or disposes of, a stamp from which such a mark has been erased or removed", "B", "Did the accused knowingly possess, or sell or dispose of, a stamp from which such a mark had been erased or removed? (s 263)"),
                ("sells or disposes of a stamp which he knows to have been used", "B", "Did the accused sell or dispose of a stamp he knew to have been used? (s 263)"),
                WD],
               "Penal Code 1871 ss 255-263 - the operative atoms")
    stamp = ("f's `a stamp issued by the Government for the purpose of revenue`", "any stamp issued by the Government for the purpose of revenue")
    m.section("255")
    m.add(gs)
    family(m, "255", gs, "`counterfeits a Government stamp`",
           'Whether the accused counterfeits, or knowingly performs part of the process of counterfeiting, a Government revenue stamp (s 255(1) of the Penal Code 1871)',
           [("(f's `counterfeits the stamp` OR f's `knowingly performs any part of the process of counterfeiting the stamp`)", "counterfeits, or knowingly performs any part of the process of counterfeiting"), stamp],
           "counterfeiting a Government stamp", recite("did counterfeit, or knowingly perform part of the process of counterfeiting, a stamp issued by the Government for the purpose of revenue"),
           "government-stamps", "s 255", puns=[and_fine("255", "255(1)", 10)])
    COVERAGE["255"] = ("encoded", "`Government Stamp Facts`; `counterfeits a Government stamp`, `offence under s 255`, `charge under s 255`; (2) and the Explanation widen the leaves")
    specs = [
        ("256", "`possesses an instrument for counterfeiting a Government stamp`", "having possession of an instrument or material for the purpose of counterfeiting a Government stamp",
         [("f's `has in his possession any instrument or material`", "has in his possession any instrument or material"),
          ("f's `for the purpose of being used, or knowing or having reason to believe that it is intended to be used, for counterfeiting the stamp`", "for the purpose of being used, or knowing or having reason to believe that it is intended to be used, for counterfeiting"), stamp],
         "did have in your possession an instrument or material for the purpose of counterfeiting a stamp issued by the Government for the purpose of revenue", and_fine("256", "256", 7)),
        ("257", "`makes or sells an instrument for counterfeiting a Government stamp`", "making or selling an instrument for the purpose of counterfeiting a Government stamp",
         [("f's `makes, performs any part of the process of making, buys, sells or disposes of any instrument`", "makes, performs any part of the process of making, buys, sells or disposes of, any instrument"),
          ("f's `for the purpose of being used, or knowing or having reason to believe that it is intended to be used, for counterfeiting the stamp`", "for the purpose of being used, or knowing or having reason to believe that it is intended to be used, for counterfeiting"), stamp],
         "did make, buy, sell or dispose of an instrument for the purpose of counterfeiting a stamp issued by the Government for the purpose of revenue", and_fine("257", "257", 7)),
        ("258", "`sells a counterfeit Government stamp`", "sale of counterfeit Government stamp",
         [("f's `sells or offers for sale the stamp`", "sells, or offers for sale, any stamp"),
          ("f's `knows or has reason to believe the stamp to be a counterfeit`", "which he knows or has reason to believe to be a counterfeit"), stamp],
         "did sell or offer for sale a stamp which you knew or had reason to believe to be a counterfeit of a stamp issued by the Government for the purpose of revenue", and_fine("258", "258", 7)),
        ("259", "`possesses a counterfeit Government stamp`", "having possession of a counterfeit Government stamp",
         [("f's `has in his possession the stamp`", "has in his possession any stamp"), ("f's `knows the stamp to be a counterfeit`", "which he knows to be a counterfeit"), stamp,
          ("f's `intending to use or dispose of it as a genuine stamp, or in order that it may be used as a genuine stamp`", "intending to use or dispose of the same as a genuine stamp, or in order that it may be used as a genuine stamp")],
         "did have in your possession a stamp which you knew to be a counterfeit of a stamp issued by the Government for the purpose of revenue, intending to use or dispose of it as a genuine stamp", and_fine("259", "259", 7)),
        ("260", "`uses as genuine a counterfeit Government stamp`", "using as genuine a Government stamp known to be counterfeit",
         [("f's `uses the stamp as genuine`", "uses as genuine any stamp"), ("f's `knows the stamp to be a counterfeit`", "knowing it to be a counterfeit"), stamp],
         "did use as genuine a stamp, knowing it to be a counterfeit of a stamp issued by the Government for the purpose of revenue", or_both("260", "260", 7)),
        ("261", "`removes writing from a Government stamp to cause loss to the Government`", "effacing any writing from a substance bearing a Government stamp, or removing from a document a stamp used for it, with intent to cause loss to Government",
         [("f's `fraudulently or with intent to cause loss to the Government`", "fraudulently or with intent to cause loss to the Government"),
          ("(f's `removes or effaces from a substance bearing the stamp any writing or document for which the stamp has been used` OR f's `removes from a writing or document a stamp which has been used for it`)", "removes or effaces from a substance bearing the stamp the writing for which it was used, or removes from a writing a stamp used for it"),
          stamp, ("f's `in order that the stamp may be used for a different writing or document`", "in order that such stamp may be used for a different writing or document")],
         "did fraudulently or with intent to cause loss to the Government remove a stamp issued by the Government for the purpose of revenue from the writing for which it had been used, or the writing from it, in order that the stamp may be used for a different writing", or_both("261", "261", 3)),
        ("262", "`uses a Government stamp known to have been before used`", "using a Government stamp known to have been before used",
         [("f's `fraudulently or with intent to cause loss to the Government`", "fraudulently or with intent to cause loss to the Government"),
          ("f's `uses the stamp for any purpose`", "uses for any purpose"), stamp, ("f's `knows the stamp to have been before used`", "which he knows to have been before used")],
         "did fraudulently or with intent to cause loss to the Government use a stamp issued by the Government for the purpose of revenue which you knew to have been before used", or_both("262", "262", 2)),
        ("263", "`erases the used mark from a Government stamp`", "erasure of mark denoting that stamp has been used",
         [("f's `fraudulently or with intent to cause loss to the Government`", "fraudulently or with intent to cause loss to the Government"),
          ("(f's `erases or removes from the stamp any mark put or impressed upon it for the purpose of denoting that it has been used` OR f's `knowingly has in his possession, or sells or disposes of, a stamp from which such a mark has been erased or removed` OR f's `sells or disposes of a stamp which he knows to have been used`)",
           "erases or removes the mark denoting use, or knowingly has, sells or disposes of a stamp so erased, or sells or disposes of a stamp known to have been used"), stamp],
         "did fraudulently or with intent to cause loss to the Government erase or remove the mark denoting that a stamp issued by the Government for the purpose of revenue had been used, or possess, sell or dispose of such a stamp", or_both("263", "263", 3)),
    ]
    for sec, verb, name, elems, rec, pun in specs:
        m.section(sec)
        family(m, sec, gs, verb, f"Whether the accused commits the acts section {sec} of the Penal Code 1871 describes ({name})", elems, name, recite(rec),
               "government-stamps", f"s {sec}", puns=[pun])
        COVERAGE[sec] = ("encoded", f"{verb}, `offence under s {sec}`, `charge under s {sec}`")
