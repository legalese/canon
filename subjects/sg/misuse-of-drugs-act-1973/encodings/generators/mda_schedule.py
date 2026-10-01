"""Write mda-second-schedule.l4 (the Second Schedule as printed) and mda-section-punishments.l4 (the punishments the sections state).

The figures are transcribed from source/MDA1973.txt lines 5869 to 6770 (the Second Schedule) and from the sections named in each row.  The
tests (mda_tests_*.py) read their expected values from the same text separately: they do not import this file's rows.

Run: python generators/mda_schedule.py"""
import os

ROW = os.path.join(os.path.dirname(__file__), '..')
Y = 12  # months in a year


def P(death=False, life=False, maxm=0, minm=0, maxf=0, minf=0, mins=0, maxs=0, alt=False):
    b = lambda v: 'TRUE' if v else 'FALSE'
    return '(`Punishment` OF %s, %s, %d, %d, %d, %d, %d, %d, %s)' % (b(death), b(life), maxm, minm, maxf, minf, mins, maxs, b(alt))


def B(lo=0, lo_inc=False, hi=0, hi_inc=False, mo=0, mo_inc=False):
    b = lambda v: 'TRUE' if v else 'FALSE'
    return '(`Quantity Band` OF %d, %s, %d, %s, %d, %s)' % (lo, b(lo_inc), hi, b(hi_inc), mo, b(mo_inc))


NOBAND = B()
COL = {'class': '`Third to fifth columns: by the class of drug`', 'six': '`Sixth column: a specified drug or quantity`', 'gen': '`Seventh column: general`'}
rows = []  # (section, item, nature, col, class, quantity-of, band, residual, subject33_3B, punishment)


def row(section, item, nature, col, cls, qof, band, residual, s3b, pun):
    rows.append((section, item, nature, COL[col], '`%s`' % cls, '`%s`' % qof, band, 'TRUE' if residual else 'FALSE', 'TRUE' if s3b else 'FALSE', pun))


NONE = 'Not in any class'
NOTHING = 'Nothing specified'
LIFE30 = dict(life=True, maxm=30 * Y, maxs=15)   # "Maximum 30 years or imprisonment for life and 15 strokes"

# -- third to fifth columns -------------------------------------------------------------------------------------------------------------------------
for sec, item, nature, a, b, c in [
    ('5', '(1)', 'Unauthorised traffic in controlled drug except as otherwise provided in this Schedule',
     P(maxm=20 * Y, minm=5 * Y, mins=5, maxs=15), P(maxm=20 * Y, minm=3 * Y, mins=3, maxs=10), P(maxm=10 * Y, minm=2 * Y, mins=2, maxs=5)),
    ('6', '(1)', 'Unauthorised manufacture of controlled drug except as otherwise provided in this Schedule',
     P(minm=10 * Y, mins=5, **LIFE30), P(minm=10 * Y, mins=5, **LIFE30), P(maxm=20 * Y, minm=5 * Y, mins=5, maxs=15)),
    ('7', '(1)', 'Unauthorised import or export of controlled drug except as otherwise provided in this Schedule',
     P(minm=5 * Y, mins=5, **LIFE30), P(minm=5 * Y, mins=5, **LIFE30), P(maxm=20 * Y, minm=3 * Y, mins=5, maxs=15)),
    ('11', '', 'Being the owner, tenant, occupier or person concerned in the management of premises and permitting or suffering certain activities to take place there',
     P(maxm=10 * Y, minm=2 * Y, maxf=40000, minf=4000, alt=True), P(maxm=10 * Y, minm=2 * Y, maxf=40000, minf=4000, alt=True), P(maxm=5 * Y, minm=12, maxf=10000, minf=2000, alt=True)),
    ('11E', '', 'Causing or procuring young person or vulnerable person to commit certain offences',
     P(maxm=30 * Y, minm=10 * Y, mins=10, maxs=15), P(maxm=30 * Y, minm=6 * Y, mins=6, maxs=15), P(maxm=20 * Y, minm=4 * Y, mins=4, maxs=15)),
]:
    for cls, pun in zip(['Class A drug', 'Class B drug', 'Class C drug'], [a, b, c]):
        row(sec, item, nature, 'class', cls, NOTHING, NOBAND, sec in ('5', '6', '7'), False, pun)

# -- sixth column: traffic (5) and import or export (7) ---------------------------------------------------------------------------------------------
SIX_PUN_LOWER = P(minm=20 * Y, mins=15, **LIFE30)
DEATH = P(death=True)
trade = [  # (item, what, quantity-of, lower band, upper band)
    ('(2)', 'opium where the quantity is --', 'Opium', B(800, True, 1200, True, 20, True), B(1200, False, 0, False, 30, False)),
    ('(3)', 'controlled drug (except opium) containing such quantity of morphine being --', 'Morphine in a controlled drug, opium excluded', B(20, True, 30, True), B(30)),
    ('(4)', 'controlled drug containing such quantity of diamorphine being --', 'Diamorphine', B(10, True, 15, True), B(15)),
    ('(5)', 'controlled drug containing such quantity of cocaine being --', 'Cocaine', B(20, True, 30, True), B(30)),
    ('(6)', 'cannabis where the quantity is --', 'Cannabis', B(330, True, 500, True), B(500)),
    ('(7)', 'cannabis mixture where the quantity is --', 'Cannabis mixture', B(660, True, 1000, True), B(1000)),
    ('(8)', 'cannabis resin where the quantity is --', 'Cannabis resin', B(130, True, 200, True), B(200)),
    ('(9)', 'controlled drug containing such quantity of methamphetamine being --', 'Methamphetamine', B(167, True, 250, True), B(250)),
]
for sec, verb in [('5', 'traffic in'), ('7', 'import or export of')]:
    for item, what, qof, lo, hi in trade:
        row(sec, item + '(a)', 'Unauthorised %s %s' % (verb, what), 'six', NONE, qof, lo, False, False, P(minm=20 * Y, mins=15, **LIFE30))
        row(sec, item + '(b)', 'Unauthorised %s %s' % (verb, what), 'six', NONE, qof, hi, False, False, DEATH)
# -- sixth column: manufacture (6) ------------------------------------------------------------------------------------------------------------------
for item, what, qof in [('(2)', 'morphine, or any salt of morphine, ester of morphine or salt of ester of morphine', 'Manufacture of morphine or a salt, ester or salt of ester of morphine'),
                        ('(3)', 'diamorphine or any salt of diamorphine', 'Manufacture of diamorphine or a salt of diamorphine'),
                        ('(4)', 'cocaine or any salt of cocaine', 'Manufacture of cocaine or a salt of cocaine'),
                        ('(5)', 'methamphetamine or any salt of methamphetamine', 'Manufacture of methamphetamine or a salt of methamphetamine')]:
    row('6', item, 'Unauthorised manufacture of ' + what, 'six', NONE, qof, NOBAND, False, False, DEATH)
# -- sixth column: possession (8(a)) ----------------------------------------------------------------------------------------------------------------
LOW = P(maxm=10 * Y, maxf=20000, alt=True)            # "Maximum 10 years or $20,000 or both (subject to section 33(3B))"
MID = P(maxm=20 * Y, minm=10 * Y, mins=5, maxs=10)    # "Maximum 20 years and 10 strokes / Minimum 10 years and 5 strokes"
TOP = P(maxm=30 * Y, minm=20 * Y, mins=10, maxs=15)   # "Maximum 30 years and 15 strokes / Minimum 20 years and 10 strokes"
poss = [
    ('(1)', 'cannabis where the quantity is --', 'Cannabis', B(0, False, 330), B(330, True, 500, True), B(500)),
    ('(2)', 'cannabis mixture where the quantity is --', 'Cannabis mixture', B(0, False, 660), B(660, True, 1000, True), B(1000)),
    ('(3)', 'cannabis resin where the quantity is --', 'Cannabis resin', B(0, False, 130), B(130, True, 200, True), B(200)),
    ('(4)', 'controlled drug containing a quantity of cocaine that is --', 'Cocaine', B(0, False, 20), B(20, True, 30, True), B(30)),
    ('(5)', 'controlled drug containing a quantity of diamorphine that is --', 'Diamorphine', B(0, False, 10), B(10, True, 15, True), B(15)),
    ('(6)', 'controlled drug containing a quantity of methamphetamine that is --', 'Methamphetamine', B(0, False, 167), B(167, True, 250, True), B(250)),
    ('(7)', 'controlled drug (except opium) containing a quantity of morphine that is --', 'Morphine in a controlled drug, opium excluded', B(0, False, 20), B(20, True, 30, True), B(30)),
    ('(8)', 'opium where the quantity is --', 'Opium', B(0, False, 800), B(800, True, 1200, True, 20, True), B(1200, False, 0, False, 30, False)),
]
for item, what, qof, lo, mid, top in poss:
    row('8(a)', item + '(a)', 'Unauthorised possession of ' + what, 'six', NONE, qof, lo, False, True, LOW)
    row('8(a)', item + '(b)', 'Unauthorised possession of ' + what, 'six', NONE, qof, mid, False, False, MID)
    row('8(a)', item + '(c)', 'Unauthorised possession of ' + what, 'six', NONE, qof, top, False, False, TOP)
row('8(a)', '(9)', 'Unauthorised possession of a controlled drug except as otherwise provided in this Schedule', 'six', NONE, NOTHING, NOBAND, True, True, LOW)
# -- seventh column: general ------------------------------------------------------------------------------------------------------------------------
for sec, nature, pun in [
    ('9', 'Possession of pipes, utensils, etc., for smoking, administration or consumption of a controlled drug', P(maxm=3 * Y, maxf=10000, alt=True)),
    ('10', 'Cultivation of cannabis, opium, coca plant', P(maxm=20 * Y, minm=3 * Y, maxf=40000, minf=5000, alt=True)),
    ('10A', 'Manufacture, supply, possession, import or export of equipment, materials or substances useful for manufacture of controlled drugs', P(maxm=20 * Y, maxf=200000, alt=True)),
    ('30(1)(a)', 'Obstructing exercise of powers', P(maxm=3 * Y, minm=6, maxf=5000, minf=1000, alt=True)),
    ('30(1)(b)', 'Failure to comply with lawful requirements', P(maxm=3 * Y, minm=6, maxf=5000, minf=1000, alt=True)),
    ('30(1)(c)', 'Failure to furnish information', P(maxm=3 * Y, minm=6, maxf=5000, minf=1000, alt=True)),
    ('30(1)(d)', 'Furnishing false information', P(maxm=12, maxf=5000, alt=True)),
    ('31(2A)', 'Failure to comply with order of Director for urine test', P(maxm=4 * Y, maxf=10000, alt=True)),
    ('31A(2A)', 'Failure to comply with order of Director for hair test', P(maxm=4 * Y, maxf=10000, alt=True)),
    ('31B(2)', 'Failure to provide oral fluid', P(maxm=2 * Y, maxf=5000, alt=True)),
]:
    row(sec, '', nature, 'gen', NONE, NOTHING, NOBAND, False, False, pun)

HEAD = """IMPORT prelude
IMPORT `mda-types`

-- Misuse of Drugs Act 1973, Second Schedule "Offences punishable on conviction" (sections 2, 33(1), (2), (3), (3B) and (4D) and 33B(1)), as printed.
-- Source: source/MDA1973.txt lines 5869 to 6770.  GENERATED by generators/mda_schedule.py: do not edit by hand.
--
-- %d rows.  Every printed cell is a row here.  Four printed entries are NOT rows because the Schedule itself says they are deleted: 8(b) and 13
-- ("[Deleted by Act 1 of 2019]") and 31(2) and 31A(2) (same); the punishment for 8(b), 31(2) and 31A(2) is in section 33(3A) and is in
-- mda-section-punishments.l4.
--
-- A row says what the Schedule prints for one section, one numbered item (and lettered paragraph) and one column.  Third to fifth columns: the
-- punishment by class of drug (Class A, B, C), "except as otherwise provided in this Schedule" (so the row is RESIDUAL: a sixth-column row that
-- applies wins).  Sixth column: the punishment for a SPECIFIED DRUG or QUANTITY (section 33(2)(b)); on manufacture, for a specified drug, and on
-- traffic, import, export or possession, for a specified quantity of the drug, or of the morphine, diamorphine, cocaine or methamphetamine a controlled
-- drug contains.  Seventh column: the punishment whether or not a controlled drug is involved (section 33(2)(c)).
--
-- columns of each row:
--   section  item  general nature of the offence  column  class of drug  quantity of  quantity band(lower, incl, upper, incl, morphine lower, incl)
--   residual  subject to section 33(3B)  punishment(death, life, max months, min months, max fine, min fine, min strokes, max strokes, alternative)

§ `The Second Schedule`

@ref "Misuse of Drugs Act 1973, Second Schedule"
`the Second Schedule` MEANS
    LIST
""" % len(rows)
lines = []
for i, r in enumerate(rows):
    lead = '        ' if i == 0 else '      , '
    lines.append('%s(`Second Schedule Row` OF "%s", "%s", "%s", %s, %s, %s, %s, %s, %s, %s)' % ((lead,) + (r[0], r[1], r[2].replace('"', "'")) + r[3:]))
open(os.path.join(ROW, 'mda-second-schedule.l4'), 'w', encoding='utf-8', newline='\n').write(HEAD + '\n'.join(lines) + '\n')

# --------------------------------------------------------------------------------------------------------------------------------------------------
sp = []  # (offence, band, provision, engages, punishment)
def S(offence, band, prov, engages, pun): sp.append((offence, band, prov, engages, pun))

S('11A', 'Base band', '11A(1)', 'arranging or planning a gathering of 2 or more persons at which a controlled drug is to be consumed or trafficked', P(maxm=20 * Y, minm=3 * Y, maxs=10))
S('11A', 'Enhanced band', '33(4C)', 'a person 21 years of age or older, and the gathering consists of a young person or a vulnerable person', P(maxm=20 * Y, minm=5 * Y, mins=3, maxs=10))
S('11B(1) or (2)', 'Base band', '11B(3)', 'exposing a child to a controlled drug or paraphernalia; permitting a young person to consume', P(maxm=10 * Y))
S('11B(1) or (2)', 'Repeat band', '11B(3A)', 'a previous conviction under 11B(1) or (2) or 11N(1) or (2)', P(maxm=10 * Y, minm=2 * Y))
S('11C(1)', 'Base band', '11C(2)', 'introducing a person to a drug trafficker', P(maxm=10 * Y))
S('11C(1)', 'Repeat band', '11C(2A)', 'a previous conviction under 11C(1) or 11O(1)', P(maxm=10 * Y, minm=2 * Y))
S('11D(1)', 'Base band', '11D(3)', 'teaching or instructing another to cultivate, manufacture, consume, traffic, import or export', P(maxm=10 * Y))
S('11D(1)', 'Repeat band', '11D(4)', 'a previous conviction under 11D(1) or 11P(1)', P(maxm=10 * Y, minm=2 * Y))
S('11D(2)', 'Base band', '11D(4A)', 'disseminating or publishing information on those activities', P(maxm=5 * Y, maxf=10000, alt=True))
S('11D(2)', 'Repeat band', '11D(4B)', 'a previous conviction under 11D(2) or 11P(2)', P(maxm=5 * Y, minm=12))
S('11F(1)', 'Base band', '11F(3)', 'trafficking in a psychoactive substance', P(maxm=10 * Y, minm=2 * Y, maxf=10000, minf=4000))
S('11F(1)', 'Repeat band', '11F(4)', 'a previous conviction under 11F(1) or 11H(1), or under 5(1) or 7', P(maxm=20 * Y, minm=4 * Y, maxf=20000, minf=8000))
S('11F(1)', 'Enhanced band', '11F(5)', 'a person 21 years of age or older, and the intended recipient is a young person or a vulnerable person', P(maxm=20 * Y, minm=4 * Y, mins=4, maxs=15))
S('11G(1)', 'Base band', '11G(2)', 'manufacturing a psychoactive substance', P(maxm=20 * Y, minm=5 * Y, maxf=20000, minf=10000))
S('11H(1)', 'Base band', '11H(2)', 'importing or exporting a psychoactive substance', P(maxm=20 * Y, minm=3 * Y, maxf=20000, minf=6000))
S('11H(1)', 'Repeat band', '11H(3)', 'a previous conviction under 11H(1) or 11F(1), or under 5(1) or 7', P(maxm=20 * Y, minm=4 * Y, maxf=20000, minf=8000))
S('11H(1)', 'Enhanced band', '11H(4)', 'a person 21 years of age or older, and the intended recipient is a young person or a vulnerable person', P(maxm=20 * Y, minm=4 * Y, mins=4, maxs=15))
S('11I(1)(a)', 'Base band', '11I(2)', 'possession of a psychoactive substance', P(maxm=10 * Y, maxf=20000, alt=True))
S('11I(1)(a)', 'Repeat band', '11I(3)', 'a previous conviction under 11I(1)(a) or under 8(a)', P(maxm=10 * Y, minm=2 * Y, maxf=20000))
S('11K(1)', 'Base band', '11K(2)', 'possession of paraphernalia for a psychoactive substance', P(maxm=3 * Y, maxf=10000, alt=True))
S('11L(1)', 'Base band', '11L(2)', 'owner, tenant, occupier or person in charge permitting use for a psychoactive substance', P(maxm=5 * Y, minm=12, maxf=10000, minf=2000, alt=True))
S('11M(1)', 'Base band', '11M(2)', 'arranging or planning a gathering at which a psychoactive substance is to be consumed or trafficked', P(maxm=20 * Y, minm=3 * Y, maxs=10))
S('11M(1)', 'Enhanced band', '11M(3)', 'a person 21 years of age or older, and the gathering consists of a young person or a vulnerable person', P(maxm=20 * Y, minm=5 * Y, mins=3, maxs=10))
S('11N(1) or (2)', 'Base band', '11N(3)', 'exposing a child to a psychoactive substance; permitting a young person to consume', P(maxm=10 * Y))
S('11N(1) or (2)', 'Repeat band', '11N(4)', 'a previous conviction under 11N(1) or (2) or 11B(1) or (2)', P(maxm=10 * Y, minm=2 * Y))
S('11O(1)', 'Base band', '11O(2)', 'introducing a person to a psychoactive substance trafficker', P(maxm=10 * Y))
S('11O(1)', 'Repeat band', '11O(3)', 'a previous conviction under 11O(1) or 11C(1)', P(maxm=10 * Y, minm=2 * Y))
S('11P(1)', 'Base band', '11P(3)', 'instructing another in activities relating to psychoactive substances', P(maxm=10 * Y))
S('11P(1)', 'Repeat band', '11P(4)', 'a previous conviction under 11P(1) or 11D(1)', P(maxm=10 * Y, minm=2 * Y))
S('11P(2)', 'Base band', '11P(5)', 'disseminating or publishing such information', P(maxm=5 * Y, maxf=10000, alt=True))
S('11P(2)', 'Repeat band', '11P(6)', 'a previous conviction under 11P(2) or 11D(2)', P(maxm=5 * Y, minm=12))
S('11Q(1)', 'Base band', '11Q(2)', 'causing or procuring a young person or a vulnerable person to commit an offence under 11F(1) or 11H(1)', P(maxm=20 * Y, minm=4 * Y, mins=4, maxs=15))
S('13(a) or (c)', 'Base band', '13(d)', 'aiding an offence abroad under a corresponding law; an act preparatory to an act outside Singapore which would be an offence here', P(maxm=10 * Y, minm=2 * Y, maxf=40000, minf=4000, alt=True))
S('8(a)', 'Repeat band', '33(3B)', 'a previous conviction under 8(a) or 11I(1)(a), and convicted of an offence under 8(a) that the sixth column says is subject to 33(3B)', P(maxm=10 * Y, minm=2 * Y, maxf=20000))
S('8(b), 31(2) or 31A(2)', 'Base band', '33(3A)', 'an offence committed on or after 1 April 2019', P(maxm=10 * Y, minm=12, maxf=20000))
S('8(b), 31(2) or 31A(2)', 'Repeat band', '33(4), 33(4AA), 33(4AB)', 'a previous conviction under 8(b), 11I(1)(b), 31(2) or 31A(2), or a previous admission under 34(2) to an approved institution, or a previous conviction under section 34 of the Singapore Armed Forces Act 1972 for consumption; see the section for the exact combinations', P(minm=3 * Y))
S('11I(1)(b)', 'Base band', '33(3C)', 'consumption of a psychoactive substance', P(maxm=10 * Y, maxf=20000, alt=True))
S('11I(1)(b)', 'Repeat band', '33(3D)', 'a previous conviction under 8(b), 11I(1)(b), 31(2) or 31A(2), or a previous admission under 34(2), or a previous conviction under section 34 of the Singapore Armed Forces Act 1972', P(maxm=10 * Y, minm=3 * Y))
S('8(b) for a specified drug, 31(2) or 31A(2)', 'Repeat band', '33A(1)', 'two previous admissions or convictions in the combinations 33A(1)(a) to (f)', P(maxm=7 * Y, minm=5 * Y, mins=3, maxs=6))
S('8(b) for a specified drug, 31(2) or 31A(2)', 'Enhanced band', '33A(2)', 'a person convicted under 33A(1), (1A) or (1B) who is again convicted', P(maxm=13 * Y, minm=7 * Y, mins=6, maxs=12))
for cls, a, b, c in [('Class A drug', 10 * Y, 30 * Y, (10, 15)), ('Class B drug', 6 * Y, 30 * Y, (6, 15)), ('Class C drug', 4 * Y, 20 * Y, (4, 15))]:
    S('5(1) or 7, %s' % cls, 'Repeat band', '33(4A)', 'a previous conviction under 5(1), 7, 11F(1) or 11H(1), and again convicted under 5(1) or 7', P(maxm=b, minm=a, mins=c[0], maxs=c[1]))
    S('5(1) or 7, %s' % cls, 'Enhanced band', '33(4B)', 'a person 21 years of age or older, and the intended recipient is a young person or a vulnerable person', P(maxm=b, minm=a, mins=c[0], maxs=c[1]))
S('34A(2)', 'Base band', '34A(2)', 'a parent or guardian failing to attend counselling', P(maxf=5000))
S('38A(5)', 'Base band', '38A(5)', 'failing to comply with a notice for information about an inmate on leave', P(maxf=1500))
S('40B(4)(a)', 'Base band', '40B(4)(a)', 'failing without reasonable excuse to submit to photographs, finger impressions, particulars or body samples', P(maxm=1, maxf=1000, alt=True))

HEAD2 = """IMPORT prelude
IMPORT `mda-types`

-- Misuse of Drugs Act 1973: the punishments the SECTIONS state, as against the Second Schedule's table (mda-second-schedule.l4).
-- Source: the sections named in each row's `provision that states the punishment` (source/MDA1973.txt).  GENERATED by generators/mda_schedule.py.
-- %d rows.  A row is one band of one offence's punishment: its base band, the band for a repeat offender, and the band for an enhanced case (the age
-- of the offender and the status of the intended recipient).  `what engages the band` is the section's own condition in words; the caller says whether
-- it is met.  A figure of 0 means none printed; a repeat band that prints only a minimum ("not less than 3 years" in section 33(4)) has maximum 0.
-- Not rows: the punishments for the offences in Part 6 (committee of inquiry: ss 44(3), 45(2), 46, 52) and the regulation-making power's fine
-- (s 58(1)(l)), which concern inquiries into approved institutions and subsidiary legislation.

§ `The punishments the sections state`

@ref "Misuse of Drugs Act 1973, ss 11A to 11Q, 13, 33, 33A, 34A, 38A, 40B"
`the punishments the sections state` MEANS
    LIST
""" % len(sp)
lines = []
for i, r in enumerate(sp):
    lead = '        ' if i == 0 else '      , '
    lines.append('%s(`Section Punishment Row` OF "%s", `%s`, "%s", "%s", %s)' % (lead, r[0], r[1], r[2], r[3].replace('"', "'"), r[4]))
open(os.path.join(ROW, 'mda-section-punishments.l4'), 'w', encoding='utf-8', newline='\n').write(HEAD2 + '\n'.join(lines) + '\n')
print('rows: second schedule %d, section punishments %d' % (len(rows), len(sp)))
