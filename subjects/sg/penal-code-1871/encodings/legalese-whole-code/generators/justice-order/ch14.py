"""Chapters 13, 14, 15 (ss 264-298A) -> pc-justice-order-public.l4."""
from lib import Facts, Pun, pred, mu, or_both, and_fine
from build import Module, COVERAGE, family, recite

DEP = "/Users/mengwong/src/legalese/pc-encode/deposit/"
WD = ("what was done", "S", "What the accused did, as it is to read in the charge after \"to wit,\"")

HEADER = """-- Singapore Penal Code 1871 - Chapter 13 (repealed, ss 264-267), Chapter 14
-- (Offences affecting the public tranquility, public health, safety,
-- convenience, decency and morals, ss 267A-294) and Chapter 15 (Offences
-- relating to race, ss 295-298A).
--
-- Source: Penal Code 1871, 2020 Revised Edition, SSO "Current version as at
-- 09 Sep 2026" (inputs/PC1871.txt), quoted mechanically above each rule.
--
-- Part of the "justice-order" group; read the header of pc-justice-order.l4
-- first, which this module imports for its recital helper (`to wit`). The same
-- conventions hold: one facts record per family, flat BOOLEAN leaves, a
-- defining predicate per defining section, `offence under s N` and
-- `charge under s N` per punishing section.
--
-- Sections whose punishment turns on the RESULT of the act (ss 284, 285, 287,
-- 288, 289: "likely to cause hurt", "causes grievous hurt", "causes death")
-- are one offence each, and the charge builder picks the punishing paragraph
-- by the gravest result established (FORK JO-8).
"""


def build():
    m = Module(DEP + "pc-justice-order-public.l4", HEADER,
               ["IMPORT prelude", "IMPORT `pc-domain`", "IMPORT `pc-general`", "IMPORT `pc-justice-order`"])
    m.chapter("Chapter 13 - (repealed)")
    for n in ["264", "265", "266", "267"]:
        m.repealed(n, "[Repealed by Act 15 of 2019]")
    m.chapter("Chapter 14 - Offences affecting the public tranquility, public health, safety, convenience, decency and morals")

    # ---------------------------------------------------------------- affray
    af = Facts("Affray Facts", "Who fought, where, and what it did to the public peace",
               [("2 or more persons fight", "B", "Did 2 or more persons (the accused among them) fight? (s 267A)"),
                ("the accused is one of the persons fighting", "B", "Was the accused one of those fighting? (s 267A)"),
                ("in a public place", "B", "Was the fight in a public place? (s 267A)"),
                ("they disturb the public peace", "B", "Did the fighting disturb the public peace? (s 267A)"),
                ("the other persons", "S", "The others who fought, as the charge is to name them"), WD],
               "Penal Code 1871 ss 267A, 267B - the operative atoms")
    m.section("267A")
    m.add(af)
    m.add(pred("`commits an affray`", af, 'Whether the accused "commits an affray" within section 267A of the Penal Code 1871', '''
            "Where"
        AND f's `2 or more persons fight`
        AND f's `the accused is one of the persons fighting`
        AND f's `in a public place`
        AND f's `they disturb the public peace`
        AND "they are said to commit an affray"
        '''))
    COVERAGE["267A"] = ("encoded", "`Affray Facts`; `commits an affray` (definition; punished by s 267B)")
    m.section("267B")
    family(m, "267B", af, "`commits an affray`", "", [("f's `2 or more persons fight`", "2 or more persons fight"), ("f's `the accused is one of the persons fighting`", "the accused is one of them"),
                                                      ("f's `in a public place`", "in a public place"), ("f's `they disturb the public peace`", "disturb the public peace")],
           "affray", 'CONCAT "together with ", f\'s `the other persons`, ", did disturb the public peace by fighting in a public place, and thereby commit an affray", (`to wit` (f\'s `what was done`))',
           "public-order", "ss 267A, 267B", puns=[or_both("267B", "267B", 1, maxfine=5000)], verb_exists=True)
    COVERAGE["267B"] = ("encoded", "`offence under s 267B`, `charge under s 267B`")

    # ---------------------------------------------------------------- 267C
    ic = Facts("Incitement Facts", "What the accused uttered, placed, published or made, what it contained, and what the accused intended or knew",
               [("utters any words, or makes any sign or visible representation", "B", "(s 267C(1)(a))"),
                ("places before a person any object", "B", "(s 267C(1)(b))"),
                ("posts, publishes, distributes, sells or offers for sale any document", "B", "(s 267C(1)(c))"),
                ("communicates any electronic record", "B", "(s 267C(1)(d))"),
                ("makes, prints, reproduces, imports, possesses or has under his control such a document for the purpose of posting, publishing, distributing, selling or offering it for sale", "B", "(s 267C(2)(a))"),
                ("makes such an electronic record for the purpose of communicating it", "B", "(s 267C(2)(b))"),
                ("containing any incitement to violence, counselling disobedience to the law or to a lawful order of a public servant, or likely to lead to any breach of the peace", "B",
                 "Did it contain incitement to violence, counselling disobedience to the law or to a lawful order of a public servant (which includes giving instruction, advice or information promoting such disobedience, s 267C(4)), or was it likely to lead to a breach of the peace? (s 267C(1))"),
                ("intending for violence, disobedience to the law or such lawful order, or breach of the peace to occur", "B", "(s 267C(1)(e), (2)(c)) - a fault element"),
                ("knowing or having reason to believe that violence, disobedience to the law or such lawful order, or breach of the peace is likely to occur as a result", "B", "(s 267C(1)(f), (2)(d)) - a fault element"),
                WD],
               "Penal Code 1871 s 267C - the operative atoms")
    m.section("267C")
    m.add(ic)
    family(m, "267C", ic, "`utters words or makes a document containing incitement to violence`",
           "Whether section 267C(1) or (2) of the Penal Code 1871 applies to the accused",
           [("(f's `utters any words, or makes any sign or visible representation` OR f's `places before a person any object` OR f's `posts, publishes, distributes, sells or offers for sale any document` OR f's `communicates any electronic record` OR f's `makes, prints, reproduces, imports, possesses or has under his control such a document for the purpose of posting, publishing, distributing, selling or offering it for sale` OR f's `makes such an electronic record for the purpose of communicating it`)",
             "utters words, places an object, publishes a document or communicates an electronic record (subsection (1)(a)-(d)), or makes or holds one for that purpose (subsection (2)(a)-(b))"),
            ("f's `containing any incitement to violence, counselling disobedience to the law or to a lawful order of a public servant, or likely to lead to any breach of the peace`", "containing any incitement to violence, counselling disobedience to the law or to a lawful order of a public servant, or likely to lead to any breach of the peace"),
            ("(f's `intending for violence, disobedience to the law or such lawful order, or breach of the peace to occur` OR f's `knowing or having reason to believe that violence, disobedience to the law or such lawful order, or breach of the peace is likely to occur as a result`)", "intending, or knowing or having reason to believe it likely, that violence, disobedience or breach of the peace will occur")],
           "uttering words, making document, etc., containing incitement to violence",
           recite("did utter words, publish a document or communicate an electronic record (or make or hold one for that purpose) containing incitement to violence, counselling disobedience to the law, or likely to lead to a breach of the peace, intending or knowing or having reason to believe that violence, disobedience or a breach of the peace was likely to occur"),
           "public-order", "s 267C", puns=[or_both("267C", "267C(3)", 5)],
           comment="FORK JO-9: subsections (1) and (2) are read as one offence, punished by (3); the (2)(c)-(d) mental elements (\"by the carrying out of the purpose\") share the (1)(e)-(f) leaves.")
    COVERAGE["267C"] = ("encoded", "`Incitement Facts`; `utters words or makes a document containing incitement to violence`, `offence under s 267C`, `charge under s 267C`; (4) widens the content leaf")

    # ---------------------------------------------------------------- nuisance
    pn = Facts("Public Nuisance Facts", "The act or omission, what it did to the public, and what the accused knew",
               [("does any act or is guilty of an illegal omission", "B", "Did the accused do an act, or commit an illegal omission (s 43)? (s 268)"),
                ("which causes any common injury, danger or annoyance to the public or to the people in general who dwell or occupy property in the vicinity", "B", "Did it cause common injury, danger or annoyance to the public, or to the people in general who dwell or occupy property in the vicinity? (s 268) - that it also causes some convenience or advantage is no excuse (Explanation)"),
                ("which must necessarily cause injury, obstruction, danger or annoyance to persons who may have occasion to use any public right", "B", "Must it necessarily cause injury, obstruction, danger or annoyance to persons who may have occasion to use a public right? (s 268)"),
                ("the case is not otherwise punishable by this Code", "B", "Is the public nuisance NOT otherwise punishable by this Code? (s 290)"),
                ("the offender knew that the act or omission will cause or will probably cause any common injury, danger or annoyance", "B", "Did the accused know the act or omission would (or would probably) cause common injury, danger or annoyance to the public or those in the vicinity? (s 290(b))"),
                ("this is a second or subsequent conviction", "B", "Would this be the accused's second or subsequent conviction? (s 290(c))"),
                ("having been enjoined by a public servant with lawful authority not to repeat or continue the nuisance", "B", "Had a public servant with lawful authority to do so enjoined the accused not to repeat or continue the nuisance? (s 291)"),
                ("repeats or continues the public nuisance", "B", "Did the accused repeat or continue the public nuisance? (s 291)"),
                WD],
               "Penal Code 1871 ss 268, 290, 291 - the operative atoms")
    m.section("268")
    m.add(pn)
    m.add(pred("`is guilty of a public nuisance`", pn, 'Whether the accused "is guilty of a public nuisance" within section 268 of the Penal Code 1871', '''
            "A person is guilty of a public nuisance, who"
        AND f's `does any act or is guilty of an illegal omission`
        AND (    f's `which causes any common injury, danger or annoyance to the public or to the people in general who dwell or occupy property in the vicinity`
             OR  f's `which must necessarily cause injury, obstruction, danger or annoyance to persons who may have occasion to use any public right` )
        '''))
    COVERAGE["268"] = ("encoded", "`Public Nuisance Facts`; `is guilty of a public nuisance` (definition; punished by ss 290, 291); the Explanation is in the leaf's @desc")

    # ---------------------------------------------------------------- hoaxes
    hx = Facts("Harmful Thing Hoax Facts", "What the accused communicated, placed or sent, and what the accused knew or intended",
               [("transmits or communicates, or causes to be transmitted or communicated, information", "B", "(s 268A)"),
                ("which contains a reference to the presence in any place, location, conveyance or means of transportation of any thing likely to cause hurt or damage to property", "B", "(s 268A(a))"),
                ("knows that such reference is false or fabricated", "B", "(s 268A(b)) - a fault element"),
                ("places any thing in any place, location, conveyance or means of transportation", "B", "(ss 268B(1)(a), 268C(1)(a))"),
                ("sends any thing from one place to another by post, courier or any other means", "B", "(ss 268B(1)(b), 268C(1)(b))"),
                ("without reasonable excuse", "B", "Was it without reasonable excuse? (ss 268B, 268C)"),
                ("with the intention of inducing in one or more other persons a belief that the thing is likely to cause hurt or damage to property", "B", "(s 268B(1)) - no particular person need be in mind (s 268B(2))"),
                ("intentionally", "B", "Was the placing or sending intentional? (s 268C(1))") if False else ("does so intentionally", "B", "Was the placing or sending intentional? (s 268C(1))"),
                ("knowing that there is a real risk that one or more persons would believe that the thing is likely to cause hurt or damage to property", "B", "(s 268C(1)) - no particular person need be in mind (s 268C(2))"),
                WD],
               "Penal Code 1871 ss 268A-268C - the operative atoms")
    m.section("268A")
    m.add(hx)
    family(m, "268A", hx, "`communicates false information of a harmful thing`", "Whether the accused communicates false information of a harmful thing (s 268A of the Penal Code 1871)",
           [("f's `transmits or communicates, or causes to be transmitted or communicated, information`", "transmits or communicates, or causes to be transmitted or communicated, information"),
            ("f's `which contains a reference to the presence in any place, location, conveyance or means of transportation of any thing likely to cause hurt or damage to property`", "(a) which contains a reference to the presence of any thing likely to cause hurt or damage to property"),
            ("f's `knows that such reference is false or fabricated`", "(b) knows that such reference is false or fabricated")],
           "communicating false information of harmful thing", recite("did communicate information containing a reference to the presence of a thing likely to cause hurt or damage to property, knowing that reference to be false or fabricated"),
           "public-order", "s 268A", puns=[or_both("268A", "268A", 7, maxfine=50000)], lead='"Any person who"')
    COVERAGE["268A"] = ("encoded", "`Harmful Thing Hoax Facts`; `communicates false information of a harmful thing`, `offence under s 268A`, `charge under s 268A`")
    place = ("(f's `places any thing in any place, location, conveyance or means of transportation` OR f's `sends any thing from one place to another by post, courier or any other means`)", "(a) places any thing in any place or conveyance, or (b) sends any thing by post, courier or other means")
    m.section("268B")
    family(m, "268B", hx, "`places or sends a thing with intent to cause fear of harm`", "Whether the accused places or sends a thing intending to induce a belief it is harmful (s 268B(1) of the Penal Code 1871)",
           [("f's `without reasonable excuse`", "without reasonable excuse"), place,
            ("f's `with the intention of inducing in one or more other persons a belief that the thing is likely to cause hurt or damage to property`", "with the intention of inducing in one or more other persons a belief that the thing is likely to cause hurt or damage to property")],
           "placing or sending thing with intent to cause fear of harm", recite("did without reasonable excuse place or send a thing with the intention of inducing in others a belief that it was likely to cause hurt or damage to property"),
           "public-order", "s 268B", puns=[or_both("268B", "268B(1)", 7, maxfine=50000)], lead='"Any person who"')
    COVERAGE["268B"] = ("encoded", "`places or sends a thing with intent to cause fear of harm`, `offence under s 268B`, `charge under s 268B`; (2) is in the leaf's @desc")
    m.section("268C")
    family(m, "268C", hx, "`places or sends a thing causing fear of harm`", "Whether the accused intentionally places or sends a thing knowing of a real risk it will be believed harmful (s 268C(1) of the Penal Code 1871)",
           [("f's `does so intentionally`", "intentionally"), ("f's `without reasonable excuse`", "and without reasonable excuse"), place,
            ("f's `knowing that there is a real risk that one or more persons would believe that the thing is likely to cause hurt or damage to property`", "knowing that there is a real risk that one or more persons would believe that the thing is likely to cause hurt or damage to property")],
           "placing or sending thing causing fear of harm", recite("did intentionally and without reasonable excuse place or send a thing, knowing that there was a real risk that others would believe it was likely to cause hurt or damage to property"),
           "public-order", "s 268C", puns=[or_both("268C", "268C(1)", months=6, maxfine=5000)], lead='"Any person who"')
    COVERAGE["268C"] = ("encoded", "`places or sends a thing causing fear of harm`, `offence under s 268C`, `charge under s 268C`; (2) is in the leaf's @desc")

    # ---------------------------------------------------------------- health
    ph = Facts("Public Health Facts", "The act, the article, drug, water or air concerned, and what the accused knew or intended",
               [("unlawfully or negligently", "B", "Was the act done unlawfully (s 43) or negligently (s 26F)? (s 269)"),
                ("intentionally or rashly", "B", "Was the act done intentionally (s 26C) or rashly (s 26E)? (s 270)"),
                ("does any act which is likely to spread the infection of any disease dangerous to life", "B", "Was the act likely to spread the infection of a disease dangerous to life? (ss 269, 270)"),
                ("knows or has reason to believe the act to be likely to spread the infection", "B", "Did the accused know, or have reason to believe, it was likely to spread the infection? (ss 269, 270) - a fault element"),
                ("knowingly disobeys a rule lawfully made and promulgated for quarantine or for regulating intercourse with places where an infectious disease prevails", "B", "Did the accused knowingly disobey a rule lawfully made and promulgated for putting a vessel into quarantine, regulating intercourse of quarantined vessels with the shore or other vessels, or regulating intercourse between places where an infectious disease prevails and other places? (s 271)"),
                ("adulterates any article of food or drink so as to make it noxious as food or drink", "B", "(s 272)"),
                ("intending to sell it as food or drink, or knowing it likely to be sold as food or drink", "B", "(s 272) - a fault element"),
                ("sells, or offers or exposes for sale, as food or drink, an article which has been rendered or has become noxious or is unfit for food or drink", "B", "(s 273)"),
                ("knowing or having reason to believe that it is noxious as food or drink", "B", "(s 273) - a fault element"),
                ("adulterates any drug or medical preparation so as to lessen its efficacy, change its operation or make it noxious", "B", "(s 274)"),
                ("intending or knowing it likely that it will be sold or used for any medicinal purpose as if unadulterated", "B", "(s 274) - a fault element"),
                ("knowing a drug or medical preparation to have been so adulterated, sells, offers or exposes it for sale, issues it from a dispensary as unadulterated, or causes it to be used by a person not knowing of the adulteration", "B", "(s 275)"),
                ("knowingly sells, offers or exposes for sale, or issues from a dispensary, any drug or medical preparation as a different drug or medical preparation", "B", "(s 276)"),
                ("voluntarily corrupts or fouls the water of any public spring or reservoir so as to render it less fit for its ordinary purpose", "B", "(s 277)"),
                ("voluntarily vitiates the atmosphere in any place so as to make it noxious to the health of persons dwelling or carrying on business in the neighbourhood or passing along a public way", "B", "(s 278)"),
                WD],
               "Penal Code 1871 ss 269-278 - the operative atoms")
    m.section("269")
    m.add(ph)
    spread = [("f's `does any act which is likely to spread the infection of any disease dangerous to life`", "does any act which is likely to spread the infection of any disease dangerous to life"),
              ("f's `knows or has reason to believe the act to be likely to spread the infection`", "which he knows or has reason to believe to be likely to spread the infection")]
    family(m, "269", ph, "`negligently does an act likely to spread infection`", "Whether the accused unlawfully or negligently does an act likely to spread a dangerous infection (s 269 of the Penal Code 1871)",
           [("f's `unlawfully or negligently`", "unlawfully or negligently")] + spread, "negligent act likely to spread infection of any disease dangerous to life",
           recite("did unlawfully or negligently do an act which was, and which you knew or had reason to believe to be, likely to spread the infection of a disease dangerous to life"),
           "public-health", "s 269", puns=[or_both("269", "269", 1)])
    COVERAGE["269"] = ("encoded", "`Public Health Facts`; `negligently does an act likely to spread infection`, `offence under s 269`, `charge under s 269`")
    m.section("270")
    family(m, "270", ph, "`intentionally does an act likely to spread infection`", "Whether the accused intentionally or rashly does an act likely to spread a dangerous infection (s 270 of the Penal Code 1871)",
           [("f's `intentionally or rashly`", "intentionally or rashly")] + spread, "intentional or rash act likely to spread infection of any disease dangerous to life",
           recite("did intentionally or rashly do an act which was, and which you knew or had reason to believe to be, likely to spread the infection of a disease dangerous to life"),
           "public-health", "s 270", puns=[or_both("270", "270", 4)])
    COVERAGE["270"] = ("encoded", "`intentionally does an act likely to spread infection`, `offence under s 270`, `charge under s 270`")
    simple = [
        ("271", "`disobeys a quarantine rule`", "disobedience to a quarantine rule",
         [("f's `knowingly disobeys a rule lawfully made and promulgated for quarantine or for regulating intercourse with places where an infectious disease prevails`", "knowingly disobeys any rule lawfully made and promulgated for quarantine or for regulating intercourse with places where an infectious disease prevails")],
         "did knowingly disobey a rule lawfully made and promulgated for quarantine", or_both("271", "271", 2)),
        ("272", "`adulterates food or drink intended for sale`", "adulteration of food or drink which is intended for sale",
         [("f's `adulterates any article of food or drink so as to make it noxious as food or drink`", "adulterates any article of food or drink, so as to make such article noxious as food or drink"),
          ("f's `intending to sell it as food or drink, or knowing it likely to be sold as food or drink`", "intending to sell such article as food or drink, or knowing it to be likely that the same will be sold as food or drink")],
         "did adulterate an article of food or drink so as to make it noxious, intending to sell it or knowing it likely to be sold as food or drink", or_both("272", "272", 3)),
        ("273", "`sells noxious food or drink`", "sale of noxious food or drink",
         [("f's `sells, or offers or exposes for sale, as food or drink, an article which has been rendered or has become noxious or is unfit for food or drink`", "sells, or offers or exposes for sale, as food or drink, any article which has been rendered or has become noxious, or is in a state unfit for food or drink"),
          ("f's `knowing or having reason to believe that it is noxious as food or drink`", "knowing or having reason to believe that the same is noxious as food or drink")],
         "did sell, or offer or expose for sale, as food or drink an article which was noxious or unfit, knowing or having reason to believe it to be noxious", or_both("273", "273", 3)),
        ("274", "`adulterates drugs`", "adulteration of drugs",
         [("f's `adulterates any drug or medical preparation so as to lessen its efficacy, change its operation or make it noxious`", "adulterates any drug or medical preparation in such a manner as to lessen its efficacy, change its operation, or make it noxious"),
          ("f's `intending or knowing it likely that it will be sold or used for any medicinal purpose as if unadulterated`", "intending that it shall be sold or used for, or knowing it likely that it will be sold or used for, any medicinal purpose, as if it had not undergone such adulteration")],
         "did adulterate a drug or medical preparation so as to lessen its efficacy, change its operation or make it noxious, intending or knowing it likely to be sold or used for a medicinal purpose as unadulterated", or_both("274", "274", 3)),
        ("275", "`sells adulterated drugs`", "sale of adulterated drugs",
         [("f's `knowing a drug or medical preparation to have been so adulterated, sells, offers or exposes it for sale, issues it from a dispensary as unadulterated, or causes it to be used by a person not knowing of the adulteration`", "knowing any drug or medical preparation to have been so adulterated, sells, offers or exposes it for sale, issues it as unadulterated, or causes it to be used by a person not knowing of the adulteration")],
         "knowing a drug or medical preparation to have been adulterated, did sell it, offer or expose it for sale, issue it as unadulterated, or cause it to be used for medicinal purposes", or_both("275", "275", 3)),
        ("276", "`sells a drug as a different drug`", "sale of any drug as a different drug or preparation",
         [("f's `knowingly sells, offers or exposes for sale, or issues from a dispensary, any drug or medical preparation as a different drug or medical preparation`", "knowingly sells, or offers or exposes for sale, or issues from a dispensary, any drug or medical preparation, as a different drug or medical preparation")],
         "did knowingly sell, offer or expose for sale, or issue from a dispensary, a drug or medical preparation as a different drug or medical preparation", or_both("276", "276", 3)),
        ("277", "`fouls the water of a public spring or reservoir`", "fouling the water of a public spring or reservoir",
         [("f's `voluntarily corrupts or fouls the water of any public spring or reservoir so as to render it less fit for its ordinary purpose`", "voluntarily corrupts or fouls the water of any public spring or reservoir, so as to render it less fit for the purpose for which it is ordinarily used")],
         "did voluntarily corrupt or foul the water of a public spring or reservoir so as to render it less fit for the purpose for which it is ordinarily used", or_both("277", "277", 3)),
        ("278", "`makes the atmosphere noxious to health`", "making atmosphere noxious to health",
         [("f's `voluntarily vitiates the atmosphere in any place so as to make it noxious to the health of persons dwelling or carrying on business in the neighbourhood or passing along a public way`", "voluntarily vitiates the atmosphere in any place so as to make it noxious to the health of persons in general dwelling or carrying on business in the neighbourhood or passing along a public way")],
         "did voluntarily vitiate the atmosphere in a place so as to make it noxious to the health of persons in the neighbourhood or passing along a public way", or_both("278", "278", 3)),
    ]
    for sec, verb, name, elems, rec, pun in simple:
        m.section(sec)
        family(m, sec, ph, verb, f"Whether the accused commits the acts section {sec} of the Penal Code 1871 describes ({name})", elems, name, recite(rec), "public-health", f"s {sec}", puns=[pun])
        COVERAGE[sec] = ("encoded", f"{verb}, `offence under s {sec}`, `charge under s {sec}`")

    # ---------------------------------------------------------------- rash conduct on ways and water
    rc = Facts("Rash Conduct Facts", "What the accused drove, rode or navigated, how, and with what danger",
               [("drives any vehicle, or rides, on any public way", "B", "(s 279)"),
                ("navigates any vessel", "B", "(s 280)"),
                ("in a manner so rash or negligent as to endanger human life, or to be likely to cause hurt or injury to any other person", "B", "Was it done so rashly (s 26E) or negligently (s 26F) as to endanger human life, or to be likely to cause hurt or injury to another? (ss 279, 280)"),
                ("exhibits any false light, mark or buoy", "B", "(s 281)"),
                ("intending or knowing it to be likely that such exhibition will mislead any navigator", "B", "(s 281) - a fault element"),
                ("knowingly or negligently conveys, or causes to be conveyed, for hire any person by water in a vessel", "B", "(s 282)"),
                ("when the vessel is in such a state or so loaded as to endanger the life of that person", "B", "(s 282)"),
                ("by doing any act, or by omitting to take order with any property in his possession or under his charge, causes danger, obstruction or injury to any person", "B", "(s 283)"),
                ("in any public way or public line of navigation", "B", "(s 283)"),
                WD],
               "Penal Code 1871 ss 279-283 - the operative atoms")
    m.section("279")
    m.add(rc)
    manner = ("f's `in a manner so rash or negligent as to endanger human life, or to be likely to cause hurt or injury to any other person`", "in a manner so rash or negligent as to endanger human life, or to be likely to cause hurt or injury to any other person")
    rspecs = [
        ("279", "`drives rashly on a public way`", "rash driving or riding on a public way", [("f's `drives any vehicle, or rides, on any public way`", "drives any vehicle, or rides, on any public way"), manner],
         "did drive a vehicle, or ride, on a public way in a manner so rash or negligent as to endanger human life, or to be likely to cause hurt or injury to another person", or_both("279", "279", 1, maxfine=5000)),
        ("280", "`navigates a vessel rashly`", "rash navigation of a vessel", [("f's `navigates any vessel`", "navigates any vessel"), manner],
         "did navigate a vessel in a manner so rash or negligent as to endanger human life, or to be likely to cause hurt or injury to another person", or_both("280", "280", 1, maxfine=5000)),
        ("281", "`exhibits a false light, mark or buoy`", "exhibition of a false light, mark or buoy",
         [("f's `exhibits any false light, mark or buoy`", "exhibits any false light, mark or buoy"), ("f's `intending or knowing it to be likely that such exhibition will mislead any navigator`", "intending or knowing it to be likely that such exhibition will mislead any navigator")],
         "did exhibit a false light, mark or buoy, intending or knowing it to be likely that it would mislead a navigator", or_both("281", "281", 7)),
        ("282", "`conveys a person by water in an unsafe vessel`", "conveying person by water for hire in a vessel overloaded or unsafe",
         [("f's `knowingly or negligently conveys, or causes to be conveyed, for hire any person by water in a vessel`", "knowingly or negligently conveys, or causes to be conveyed, for hire any person by water in any vessel"),
          ("f's `when the vessel is in such a state or so loaded as to endanger the life of that person`", "when that vessel is in such a state or so loaded as to endanger the life of that person")],
         "did knowingly or negligently convey for hire a person by water in a vessel in such a state or so loaded as to endanger that person's life", or_both("282", "282", 1, maxfine=3000)),
        ("283", "`causes danger or obstruction in a public way`", "danger or obstruction in a public way or navigation",
         [("f's `by doing any act, or by omitting to take order with any property in his possession or under his charge, causes danger, obstruction or injury to any person`", "by doing any act, or by omitting to take order with any property in his possession or under his charge, causes danger, obstruction or injury to any person"),
          ("f's `in any public way or public line of navigation`", "in any public way or public line of navigation")],
         "did by an act, or by omitting to take order with property in your possession or charge, cause danger, obstruction or injury to a person in a public way or public line of navigation",
         Pun("283", "283", "fine which may extend to $1,000", fine="sb", maxfine=1000)),
    ]
    for i, (sec, verb, name, elems, rec, pun) in enumerate(rspecs):
        if i:
            m.section(sec)
        family(m, sec, rc, verb, f"Whether the accused commits the acts section {sec} of the Penal Code 1871 describes ({name})", elems, name, recite(rec), "public-safety", f"s {sec}", puns=[pun])
        COVERAGE[sec] = ("encoded", f"{verb}, `offence under s {sec}`, `charge under s {sec}`")
    COVERAGE["279"] = ("encoded", "`Rash Conduct Facts`; " + COVERAGE["279"][1])

    import ch14b as _b
    _b.PN = pn
    _b.ch14b(m)
    m.write()
