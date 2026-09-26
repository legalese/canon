"""Chapter 11 - False evidence and offences against public justice (ss 191-229)."""
from lib import Facts, Pun, pred, charge, mu, or_both, and_fine, heading
from build import Module, Tests, COVERAGE, catalogue, TIER_DEATH, TIER_LIFE, tier_puns, tier_expr
import build

DEP = "/Users/mengwong/src/legalese/pc-encode/deposit/"

HEADER = """-- Singapore Penal Code 1871 - Chapter 11 (False evidence and offences against
-- public justice, ss 191-229) and Chapter 12 (Offences relating to Government
-- stamps, ss 230-263).
--
-- Source: Penal Code 1871, 2020 Revised Edition, SSO "Current version as at
-- 09 Sep 2026" (inputs/PC1871.txt). Section text is quoted above each rule,
-- copied mechanically from the source with page footers removed and curly
-- quotes and dashes made ASCII.
--
-- The group is "justice-order" (notes/PLAN.md s 1); Chapters 13-15 are in
-- pc-justice-order-public.l4, and the tests for both in
-- pc-justice-order-tests.l4.
--
-- What the reader must know before reading:
--
-- * The charge-generator contract (BRIEF.md, PLAN.md s 3, s 8). Each offence
--   family has ONE facts record `<Family> Facts`, taken as `GIVEN f`. Each
--   defining section is a BOOLEAN over f named in the section's own verb; each
--   punishing section has `offence under s N` (BOOLEAN) and `charge under s N`
--   (a Charge). Every leaf is a flat BOOLEAN; STRING fields are recited only.
-- * Where a section's punishment turns on how the PREDICATE offence is punished
--   (ss 201, 212, 213, 214, 216, 221, 222, 225 - "if the offence is punishable
--   with death ..."), the tier is a BOOLEAN leaf in the Code's words, and the
--   charge builder picks the punishment by it, as the reference row does for
--   s 420(2). The tier is an element of the offence ladder, because the section
--   prescribes no punishment outside its tiers (FORK JO-3).
-- * Where a section punishes "in the same manner as if he gave false evidence"
--   (ss 196-200), the charge recites that phrase and names the s 193 limb that
--   the facts select (FORK JO-2).
-- * Cross-references to other groups' sections are BOOLEAN leaves whose @desc
--   names the owning module (PLAN.md s 1, "cross-module joins owed").
-- * No offence ladder repeats a General Exception (PLAN.md s 5). Exceptions
--   printed inside a section of these Chapters are part of that section.
"""

IMPORTS = ["IMPORT prelude", "IMPORT `pc-domain`", "IMPORT `pc-general`"]


def build():
    m = Module(DEP + "pc-justice-order.l4", HEADER, IMPORTS)
    m.chapter("Chapter 11 - False evidence and offences against public justice")

    m.helper('''
        §§ `Helpers for the recital`

        -- ", to wit, <what was done>" - the particulars a Singapore charge gives
        -- after the statutory words. Omitted when the officer gives none.

        -- s 201(c), 212(1)(c), 213(c), 214(c), 216(1)(c): "one-fourth part of the
        -- longest term of imprisonment provided for that offence".
        @export The term which is "one-fourth part of the longest term of imprisonment provided for" an offence (ss 201(c), 212(1)(c), 213(c), 214(c), 216(1)(c) of the Penal Code 1871)
        GIVEN months IS A NUMBER @desc The longest term of imprisonment provided for the offence, in months
        GIVETH A NUMBER
        `one-fourth part of the longest term of imprisonment` months MEANS months / 4
        ''')

    # ------------------------------------------------------------ ss 191-195
    fe = Facts("False Evidence Facts",
               "What the accused stated or fabricated, and for what proceeding",
               [
                   # s 191
                   ("legally bound by an oath to state the truth", "B", "Was the accused legally bound by an oath to state the truth? (s 191)"),
                   ("bound by an express provision of law to state the truth", "B", "Was the accused bound by an express provision of law to state the truth? (s 191)"),
                   ("bound by law to make a declaration upon any subject", "B", "Was the accused bound by law to make a declaration upon the subject? (s 191)"),
                   ("makes a statement", "B", "Did the accused make a statement? It counts whether made verbally or otherwise (Explanation 1), and a statement of the accused's own belief counts (Explanation 2)."),
                   ("the statement is false", "B", "Was the statement false? A statement that the accused believes or knows a thing which he does not believe or know is false (Explanation 2; illustrations (b), (d))."),
                   ("he knows or believes the statement to be false", "B", "Did the accused know or believe the statement to be false? (s 191) - a fault element"),
                   ("he does not believe the statement to be true", "B", "Did the accused not believe the statement to be true? (s 191) - a fault element"),
                   ("the statement", "S", "What the accused stated, as it is to read after \"to wit, by stating\" - for example \"that he heard Z admit the justice of B's claim\""),
                   # s 192
                   ("causes any circumstance to exist", "B", "Did the accused cause a circumstance to exist? (s 192) - for example, putting jewels in another's box"),
                   ("makes any false entry in any book or record or electronic record", "B", "Did the accused make a false entry in a book, record or electronic record? (s 192)"),
                   ("makes any document or electronic record containing a false statement", "B", "Did the accused make a document or electronic record containing a false statement? (s 192)"),
                   ("intending that it may appear in evidence in a judicial proceeding", "B", "Did the accused intend that the circumstance, entry or statement may appear in evidence in a judicial proceeding? (s 192)"),
                   ("intending that it may appear in evidence in a proceeding taken by law before a public servant as such", "B", "... in a proceeding taken by law before a public servant as such (s 21)? (s 192)"),
                   ("intending that it may appear in evidence before an arbitrator", "B", "... before an arbitrator? (s 192)"),
                   ("intending that it may cause a person forming an opinion upon the evidence to entertain an erroneous opinion touching a point material to the result", "B",
                    "Did the accused intend that, so appearing in evidence, it may cause a person who is to form an opinion upon the evidence in that proceeding to entertain an erroneous opinion touching a point material to its result? (s 192)"),
                   ("the fabrication", "S", "What the accused did to fabricate the evidence, as it is to read after \"to wit,\" - for example \"by putting jewels into a box belonging to Z\""),
                   # s 193
                   ("gives it intentionally", "B", "Did the accused give the false evidence intentionally (s 26C)? (s 193) - a fault element"),
                   ("in any stage of a judicial proceeding", "B", "Was the false evidence given in a stage of a judicial proceeding (s 193)? A court-martial trial is one (Explanation 1); so is an investigation directed by law preliminary to a proceeding before a court (Explanation 2), and an investigation directed by a court and conducted under its authority (Explanation 3)."),
                   ("for the purpose of being used in any stage of a judicial proceeding", "B", "Was the false evidence fabricated for the purpose of being used in a stage of a judicial proceeding? (s 193; Explanations 1-3 as above)"),
                   # s 194
                   ("intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence which is capital", "B",
                    "Did the accused intend thereby to cause, or know it to be likely that he would thereby cause, any person to be convicted of an offence which is capital by this Code or any other law in force? (s 194)"),
                   ("an innocent person is convicted and executed in consequence of the false evidence", "B", "Was an innocent person convicted and executed in consequence of the false evidence? (s 194)"),
                   # s 195
                   ("intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for a term of 7 years or upwards", "B",
                    "Did the accused intend, or know it likely, that he would thereby cause any person to be convicted of an offence which is not capital but is punishable with imprisonment for a term of 7 years or upwards (s 41 reads 'or upwards')? (s 195(1))"),
                   ("intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for life", "B",
                    "Did the accused intend, or know it likely, that he would thereby cause any person to be convicted of an offence which is not capital but is punishable with imprisonment for life? (s 195(2))"),
                   ("the offence intended", "S", "The offence of which the accused meant someone to be convicted, as it is to read in the charge - for example \"gang-robbery\""),
               ],
               "Penal Code 1871 ss 191-195 - the operative atoms, and the particulars CPC s 124 requires")

    m.section("191")
    m.add(fe)
    m.add(pred("`gives false evidence`", fe,
               'Whether the accused "gives false evidence" within section 191 of the Penal Code 1871',
               '''
                   "Whoever, being"
               AND (    f's `legally bound by an oath to state the truth`
                    OR  f's `bound by an express provision of law to state the truth`
                    OR  f's `bound by law to make a declaration upon any subject` )
               AND f's `makes a statement`
               AND f's `the statement is false`
               AND "and which he either"
               AND (    f's `he knows or believes the statement to be false`
                    OR  f's `he does not believe the statement to be true` )
               AND "is said to give false evidence"
               ''', ref="Penal Code 1871 s 191, Explanations 1 and 2"))
    COVERAGE["191"] = ("encoded", "`False Evidence Facts`; `gives false evidence` (definition; punished by ss 193-195)")

    m.section("192")
    m.add(pred("`fabricates false evidence`", fe,
               'Whether the accused "fabricates false evidence" within section 192 of the Penal Code 1871',
               '''
                   "Whoever"
               AND (    f's `causes any circumstance to exist`
                    OR  f's `makes any false entry in any book or record or electronic record`
                    OR  f's `makes any document or electronic record containing a false statement` )
               AND (    f's `intending that it may appear in evidence in a judicial proceeding`
                    OR  f's `intending that it may appear in evidence in a proceeding taken by law before a public servant as such`
                    OR  f's `intending that it may appear in evidence before an arbitrator` )
               AND f's `intending that it may cause a person forming an opinion upon the evidence to entertain an erroneous opinion touching a point material to the result`
               AND "is said to fabricate false evidence"
               ''', ref="Penal Code 1871 s 192"))
    COVERAGE["192"] = ("encoded", "`fabricates false evidence` (definition; punished by ss 193-195)")

    m.section("193")
    p193j = and_fine("193 (judicial proceeding)", "193", 7)
    p193o = and_fine("193 (any other case)", "193", 3)
    m.add(p193j, p193o)
    m.add(pred("`the false evidence is in a stage of a judicial proceeding`", fe,
               'Whether the false evidence falls under the first, heavier limb of section 193 of the Penal Code 1871 (a stage of a judicial proceeding) rather than "any other case"',
               '''
                   (    `gives false evidence` f
                    AND f's `in any stage of a judicial proceeding` )
               OR  (    `fabricates false evidence` f
                    AND f's `for the purpose of being used in any stage of a judicial proceeding` )
               '''))
    m.offence("193", fe, "punishment for false evidence", '''
            (    "Whoever"
             AND f's `gives it intentionally`
             AND `gives false evidence` f )
        OR  (    "or"
             AND `fabricates false evidence` f )
        ''', comment="Both limbs of s 193 have the same elements; they differ in punishment only, by whether the evidence is in (or for) a stage of a judicial proceeding. One offence, two punishment records (PLAN s 6).")
    m.helper('''
        GIVEN f IS A `False Evidence Facts`
        GIVETH A STRING
        `the false evidence recital` f MEANS
            `joined with` ", and " (concat (LIST
                (`included if` (f's `gives it intentionally` AND `gives false evidence` f)
                    (CONCAT "did intentionally give false evidence",
                            (IF f's `in any stage of a judicial proceeding` THEN " in a stage of a judicial proceeding" ELSE ""),
                            (`to wit` (IF f's `the statement` EQUALS "" THEN "" ELSE CONCAT "by stating ", f's `the statement`)),
                            ", which statement you knew or believed to be false or did not believe to be true")),
                (`included if` (`fabricates false evidence` f)
                    (CONCAT "did fabricate false evidence",
                            (IF f's `for the purpose of being used in any stage of a judicial proceeding` THEN " for the purpose of being used in a stage of a judicial proceeding" ELSE ""),
                            (`to wit` (f's `the fabrication`))))))

        GIVEN f IS A `False Evidence Facts`
        GIVETH A LIST OF STRING
        `elements of false evidence not made out` f MEANS
            concat (LIST
                (`missing unless` (`gives false evidence` f OR `fabricates false evidence` f) "gives false evidence (section 191) or fabricates false evidence (section 192)"),
                (`missing unless` (`fabricates false evidence` f OR f's `gives it intentionally`) "intentionally (section 193)"))
        ''')
    m.add(charge("193", fe, '"giving or fabricating false evidence"',
                 "IF `the false evidence is in a stage of a judicial proceeding` f THEN (`punishment prescribed by s 193 (judicial proceeding)`)'s words ELSE (`punishment prescribed by s 193 (any other case)`)'s words",
                 "`the false evidence recital` f",
                 ["(`elements of false evidence not made out` f)"],
                 title="punishment for false evidence"))
    COVERAGE["193"] = ("encoded", "`offence under s 193`, `charge under s 193`, `the false evidence is in a stage of a judicial proceeding`; punishments `s 193 (judicial proceeding)`, `s 193 (any other case)`")
    catalogue("193", "giving or fabricating false evidence", "ss 191, 192, 193", "false-evidence", fe,
              ["gives false evidence", "fabricates false evidence"])

    m.section("194")
    m.add(Pun("194", "194", "imprisonment for life, or with imprisonment for a term which may extend to 20 years, and shall, if he is not sentenced to imprisonment for life, also be liable to fine",
              life="or", imp="or", maxm=240, fine="al"))
    m.add(Pun("194 (innocent person executed)", "194", "either with death or the punishment hereinbefore described",
              death="or", life="or", imp="or", maxm=240, fine="al"))
    m.offence("194", fe, "giving or fabricating false evidence with intent to procure conviction of a capital offence", '''
            "Whoever"
        AND (    `gives false evidence` f
             OR  `fabricates false evidence` f )
        AND f's `intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence which is capital`
        ''')
    m.add(charge("194", fe, '"giving or fabricating false evidence with intent to procure conviction of a capital offence"',
                 "IF f's `an innocent person is convicted and executed in consequence of the false evidence` AND `gives false evidence` f THEN (`punishment prescribed by s 194 (innocent person executed)`)'s words ELSE (`punishment prescribed by s 194`)'s words",
                 'CONCAT "did give or fabricate false evidence, intending thereby to cause, or knowing it to be likely that you would thereby cause, a person to be convicted of an offence which is capital, namely ", f\'s `the offence intended`, (`to wit` (`joined with` ", and " (append (`included if` (NOT (f\'s `the statement` EQUALS "")) (f\'s `the statement`)) (`included if` (NOT (f\'s `the fabrication` EQUALS "")) (f\'s `the fabrication`)))))',
                 [mu("`gives false evidence` f OR `fabricates false evidence` f", "gives false evidence (section 191) or fabricates false evidence (section 192)"),
                  mu("f's `intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence which is capital`", "intending thereby to cause, or knowing it to be likely that he will thereby cause, any person to be convicted of an offence which is capital")]))
    COVERAGE["194"] = ("encoded", "`offence under s 194`, `charge under s 194`; punishments `s 194`, `s 194 (innocent person executed)`")
    catalogue("194", "giving or fabricating false evidence with intent to procure conviction of a capital offence", "ss 191, 192, 194", "false-evidence", fe,
              ["gives false evidence", "fabricates false evidence"])

    m.section("195")
    m.helper('''
        -- s 195(1) punishes "as a person convicted of that offence would be liable to
        -- be punished, except that he shall not be punished with caning". So the
        -- punishment is a function of the OTHER offence's punishment: the same
        -- record, with caning struck out and the section renamed.
        @export The punishment under section 195(1) of the Penal Code 1871: that of the offence the false evidence was meant to procure a conviction for, "except that he shall not be punished with caning"
        GIVEN p IS A Punishment @desc The punishment prescribed for the offence the accused intended someone to be convicted of
        GIVETH A Punishment
        `punishment prescribed by s 195(1) for` p MEANS
            Punishment WITH
                section                  IS "195(1)"
                words                    IS "as a person convicted of that offence would be liable to be punished, except that he shall not be punished with caning"
                death                    IS p's death
                `imprisonment for life`  IS p's `imprisonment for life`
                imprisonment             IS p's imprisonment
                `maximum term in months` IS p's `maximum term in months`
                `minimum term in months` IS p's `minimum term in months`
                `forfeiture of property` IS p's `forfeiture of property`
                fine                     IS p's fine
                `maximum fine`           IS p's `maximum fine`
                `minimum fine`           IS p's `minimum fine`
                caning                   IS `not prescribed`
                `minimum strokes`        IS NOTHING
                `maximum strokes`        IS NOTHING
                `or with both`           IS p's `or with both`
        ''')
    m.add(Pun("195(2)", "195(2)", "imprisonment for a term which may extend to 20 years", imp="sb", maxm=240))
    m.offence("195(1)", fe, "giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for 7 years or upwards", '''
            "Whoever"
        AND (    `gives false evidence` f
             OR  `fabricates false evidence` f )
        AND f's `intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for a term of 7 years or upwards`
        ''')
    m.add(charge("195(1)", fe, '"giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment"',
                 '"as a person convicted of that offence would be liable to be punished, except that he shall not be punished with caning"',
                 'CONCAT "did give or fabricate false evidence, intending thereby to cause, or knowing it to be likely that you would thereby cause, a person to be convicted of an offence which is not capital but punishable with imprisonment for a term of 7 years or upwards, namely ", f\'s `the offence intended`, (`to wit` (`joined with` ", and " (append (`included if` (NOT (f\'s `the statement` EQUALS "")) (f\'s `the statement`)) (`included if` (NOT (f\'s `the fabrication` EQUALS "")) (f\'s `the fabrication`)))))',
                 [mu("`gives false evidence` f OR `fabricates false evidence` f", "gives false evidence (section 191) or fabricates false evidence (section 192)"),
                  mu("f's `intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for a term of 7 years or upwards`", "intending or knowing it likely to cause a conviction of an offence not capital but punishable with imprisonment for 7 years or upwards")]))
    m.offence("195(2)", fe, "giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for life", '''
            "Whoever"
        AND (    `gives false evidence` f
             OR  `fabricates false evidence` f )
        AND f's `intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for life`
        ''')
    m.add(charge("195(2)", fe, '"giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for life"',
                 "(`punishment prescribed by s 195(2)`)'s words",
                 'CONCAT "did give or fabricate false evidence, intending thereby to cause, or knowing it to be likely that you would thereby cause, a person to be convicted of an offence which is not capital but punishable with imprisonment for life, namely ", f\'s `the offence intended`, (`to wit` (`joined with` ", and " (append (`included if` (NOT (f\'s `the statement` EQUALS "")) (f\'s `the statement`)) (`included if` (NOT (f\'s `the fabrication` EQUALS "")) (f\'s `the fabrication`)))))',
                 [mu("`gives false evidence` f OR `fabricates false evidence` f", "gives false evidence (section 191) or fabricates false evidence (section 192)"),
                  mu("f's `intending or knowing it to be likely that he will thereby cause any person to be convicted of an offence not capital but punishable with imprisonment for life`", "intending or knowing it likely to cause a conviction of an offence not capital but punishable with imprisonment for life")]))
    COVERAGE["195"] = ("encoded", "`offence under s 195(1)`, `charge under s 195(1)`, `offence under s 195(2)`, `charge under s 195(2)`; `punishment prescribed by s 195(1) for` (a function of the other offence's Punishment), `punishment prescribed by s 195(2)`")
    for s, title in [("195(1)", "giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for 7 years or upwards"),
                     ("195(2)", "giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for life")]:
        catalogue(s, title, "ss 191, 192, 195", "false-evidence", fe, ["gives false evidence", "fabricates false evidence"])

    # ------------------------------------------------------------ ss 196-200
    ue = Facts("Using False Evidence Facts",
               "What evidence, certificate or declaration the accused made or used, and what the accused knew of it",
               [
                   # s 196
                   ("uses or attempts to use as true or genuine evidence any evidence", "B", "Did the accused use, or attempt to use, as true or genuine evidence any evidence? (s 196)"),
                   ("corruptly", "B", "Did the accused act corruptly? (ss 196, 198, 200) - the Code does not define the word"),
                   ("knows the evidence to be false or fabricated", "B", "Did the accused know the evidence to be false or fabricated? (s 196) - a fault element"),
                   # s 197
                   ("issues or signs any certificate", "B", "Did the accused issue or sign a certificate? (s 197)"),
                   ("the certificate is required by law to be given or signed", "B", "Is the certificate one required by law to be given or signed? (s 197)"),
                   ("the certificate relates to a fact of which it is by law admissible in evidence", "B", "Does the certificate relate to a fact of which such a certificate is by law admissible in evidence? (s 197)"),
                   ("knowing or believing that the certificate is false in any material point", "B", "Did the accused know or believe the certificate to be false in a material point? (ss 197, 198) - a fault element"),
                   # s 198
                   ("uses or attempts to use the certificate as a true certificate", "B", "Did the accused use, or attempt to use, such a certificate as a true certificate? (s 198)"),
                   ("knowing the certificate to be false in any material point", "B", "Did the accused KNOW the certificate to be false in a material point? (s 198 - knowledge; belief is not enough, unlike s 197) - a fault element"),
                   # s 199
                   ("makes a statement in a declaration made or subscribed by him", "B", "Did the accused make a statement in a declaration he made or subscribed? A declaration inadmissible merely for some informality still counts (s 200 Explanation). (s 199)"),
                   ("a court of justice, public servant or other person is bound or authorised by law to receive the declaration as evidence of any fact", "B", "Is a court of justice, a public servant or another person bound or authorised by law to receive the declaration as evidence of any fact? (s 199)"),
                   ("the statement in the declaration is false", "B", "Was the statement false? (s 199)"),
                   ("knows or believes the statement in the declaration to be false or does not believe it to be true", "B", "Did the accused know or believe it to be false, or not believe it to be true? (s 199) - a fault element"),
                   ("touching any point material to the object for which the declaration is made or used", "B", "Did the statement touch a point material to the object for which the declaration was made or used? (s 199)"),
                   # s 200
                   ("uses or attempts to use as true any such declaration", "B", "Did the accused use, or attempt to use, as true a declaration of the kind in s 199? (s 200)"),
                   ("knowing the declaration to be false in any material point", "B", "Did the accused know the declaration to be false in a material point? (s 200) - a fault element"),
                   # the s 193 limb
                   ("in any stage of a judicial proceeding", "B", "Was the evidence, certificate or declaration used or given in a stage of a judicial proceeding? This selects which of s 193's two punishments applies \"as if he gave false evidence\" (FORK JO-2)."),
                   ("what was used or made", "S", "The evidence, certificate or declaration, as it is to read after \"to wit,\""),
               ],
               "Penal Code 1871 ss 196-200 - the operative atoms")

    same = "in the same manner as if he gave false evidence"

    def s193_limb(prefix):
        return (f'CONCAT "{prefix} (section 193: ", (IF f\'s `in any stage of a judicial proceeding` THEN (`punishment prescribed by s 193 (judicial proceeding)`)\'s words '
                f'ELSE (`punishment prescribed by s 193 (any other case)`)\'s words), ")"')

    m.section("196")
    m.add(ue)
    m.add(pred("`corruptly uses evidence known to be false`", ue,
               'Whether the accused corruptly uses or attempts to use as true evidence known to be false or fabricated (s 196 of the Penal Code 1871)',
               '''
                   "Whoever"
               AND f's corruptly
               AND f's `uses or attempts to use as true or genuine evidence any evidence`
               AND "which he"
               AND f's `knows the evidence to be false or fabricated`
               '''))
    m.offence("196", ue, "using evidence known to be false", '''
        `corruptly uses evidence known to be false` f
        ''')
    m.add(charge("196", ue, '"using evidence known to be false"', s193_limb("in the same manner as if he gave or fabricated false evidence"),
                 'CONCAT "did corruptly use or attempt to use as true or genuine evidence evidence which you knew to be false or fabricated", (`to wit` (f\'s `what was used or made`))',
                 [mu("f's corruptly", "corruptly"), mu("f's `uses or attempts to use as true or genuine evidence any evidence`", "uses or attempts to use as true or genuine evidence any evidence"),
                  mu("f's `knows the evidence to be false or fabricated`", "which he knows to be false or fabricated")]))
    COVERAGE["196"] = ("encoded", "`Using False Evidence Facts`; `corruptly uses evidence known to be false`, `offence under s 196`, `charge under s 196`")
    catalogue("196", "using evidence known to be false", "s 196", "false-evidence", ue, ["corruptly uses evidence known to be false"])

    m.section("197")
    m.add(pred("`issues or signs a false certificate`", ue,
               'Whether the accused issues or signs a certificate known or believed false in a material point (s 197 of the Penal Code 1871)',
               '''
                   "Whoever"
               AND f's `issues or signs any certificate`
               AND (    f's `the certificate is required by law to be given or signed`
                    OR  f's `the certificate relates to a fact of which it is by law admissible in evidence` )
               AND f's `knowing or believing that the certificate is false in any material point`
               '''))
    m.offence("197", ue, "issuing or signing a false certificate", "`issues or signs a false certificate` f")
    m.add(charge("197", ue, '"issuing or signing a false certificate"', s193_limb(same),
                 'CONCAT "did issue or sign a certificate required by law to be given or signed, or relating to a fact of which it is by law admissible in evidence, knowing or believing that the certificate was false in a material point", (`to wit` (f\'s `what was used or made`))',
                 [mu("f's `issues or signs any certificate`", "issues or signs any certificate"),
                  mu("f's `the certificate is required by law to be given or signed` OR f's `the certificate relates to a fact of which it is by law admissible in evidence`", "required by law to be given or signed, or relating to a fact of which such certificate is by law admissible in evidence"),
                  mu("f's `knowing or believing that the certificate is false in any material point`", "knowing or believing that such certificate is false in any material point")]))
    COVERAGE["197"] = ("encoded", "`issues or signs a false certificate`, `offence under s 197`, `charge under s 197`")
    catalogue("197", "issuing or signing a false certificate", "s 197", "false-evidence", ue, ["issues or signs a false certificate"])

    m.section("198")
    m.add(pred("`uses as true a certificate known to be false`", ue,
               'Whether the accused corruptly uses as true a certificate known to be false in a material point (s 198 of the Penal Code 1871)',
               '''
                   "Whoever"
               AND f's corruptly
               AND f's `uses or attempts to use the certificate as a true certificate`
               AND f's `knowing the certificate to be false in any material point`
               ''', comment="s 198 reads \"knowing the same to be false\", narrower than s 197's \"knowing or believing\", so it has its own leaf (FORK JO-4)."))
    m.offence("198", ue, "using as a true certificate one known to be false in a material point", "`uses as true a certificate known to be false` f")
    m.add(charge("198", ue, '"using as a true certificate one known to be false in a material point"', s193_limb(same),
                 'CONCAT "did corruptly use or attempt to use as a true certificate a certificate which you knew to be false in a material point", (`to wit` (f\'s `what was used or made`))',
                 [mu("f's corruptly", "corruptly"), mu("f's `uses or attempts to use the certificate as a true certificate`", "uses or attempts to use any such certificate as a true certificate"),
                  mu("f's `knowing the certificate to be false in any material point`", "knowing the same to be false in any material point")]))
    COVERAGE["198"] = ("encoded", "`uses as true a certificate known to be false`, `offence under s 198`, `charge under s 198`")
    catalogue("198", "using as a true certificate one known to be false in a material point", "s 198", "false-evidence", ue, ["uses as true a certificate known to be false"])

    m.section("199")
    m.add(pred("`makes a false statement in a declaration receivable as evidence`", ue,
               'Whether the accused makes a false statement in a declaration which is by law receivable as evidence (s 199 of the Penal Code 1871)',
               '''
                   "Whoever"
               AND f's `makes a statement in a declaration made or subscribed by him`
               AND f's `a court of justice, public servant or other person is bound or authorised by law to receive the declaration as evidence of any fact`
               AND f's `the statement in the declaration is false`
               AND f's `knows or believes the statement in the declaration to be false or does not believe it to be true`
               AND f's `touching any point material to the object for which the declaration is made or used`
               '''))
    m.offence("199", ue, "false statement made in any declaration which is by law receivable as evidence", "`makes a false statement in a declaration receivable as evidence` f")
    m.add(charge("199", ue, '"false statement made in a declaration which is by law receivable as evidence"', s193_limb(same),
                 'CONCAT "did, in a declaration made or subscribed by you, which a court of justice, public servant or other person was bound or authorised by law to receive as evidence of a fact, make a statement which was false and which you knew or believed to be false or did not believe to be true, touching a point material to the object for which the declaration was made or used", (`to wit` (f\'s `what was used or made`))',
                 [mu("f's `makes a statement in a declaration made or subscribed by him`", "makes a statement in a declaration made or subscribed by him"),
                  mu("f's `a court of justice, public servant or other person is bound or authorised by law to receive the declaration as evidence of any fact`", "which declaration a court of justice, public servant or other person is bound or authorised by law to receive as evidence"),
                  mu("f's `the statement in the declaration is false`", "which is false"),
                  mu("f's `knows or believes the statement in the declaration to be false or does not believe it to be true`", "which he knows or believes to be false or does not believe to be true"),
                  mu("f's `touching any point material to the object for which the declaration is made or used`", "touching any point material to the object for which the declaration is made or used")]))
    COVERAGE["199"] = ("encoded", "`makes a false statement in a declaration receivable as evidence`, `offence under s 199`, `charge under s 199`")
    catalogue("199", "false statement made in a declaration which is by law receivable as evidence", "s 199", "false-evidence", ue, ["makes a false statement in a declaration receivable as evidence"])

    m.section("200")
    m.add(pred("`uses as true a declaration known to be false`", ue,
               'Whether the accused corruptly uses as true a declaration known to be false in a material point (s 200 of the Penal Code 1871)',
               '''
                   "Whoever"
               AND f's corruptly
               AND f's `uses or attempts to use as true any such declaration`
               AND f's `knowing the declaration to be false in any material point`
               '''))
    m.offence("200", ue, "using as true any such declaration known to be false", "`uses as true a declaration known to be false` f")
    m.add(charge("200", ue, '"using as true a declaration known to be false"', s193_limb(same),
                 'CONCAT "did corruptly use or attempt to use as true a declaration which you knew to be false in a material point", (`to wit` (f\'s `what was used or made`))',
                 [mu("f's corruptly", "corruptly"), mu("f's `uses or attempts to use as true any such declaration`", "uses or attempts to use as true any such declaration"),
                  mu("f's `knowing the declaration to be false in any material point`", "knowing the same to be false in any material point")]))
    COVERAGE["200"] = ("encoded", "`uses as true a declaration known to be false`, `offence under s 200`, `charge under s 200`; the Explanation widens the s 199 leaf")
    catalogue("200", "using as true a declaration known to be false", "ss 199, 200", "false-evidence", ue, ["uses as true a declaration known to be false"])

    from ch11b import ch11b
    ch11b(m)
    m.write()


