#!/usr/bin/env python3
"""Generate tier-3 tests for the HVAC work-licensing encodings.

This is an INDEPENDENT re-implementation, in Python, of the rules quoted in
the comments of ../encodings/legalese/hvac-law.l4 and hvac-fees.l4.  It is
deliberately NOT a transliteration of the L4: every expected value below is
computed from a reading of the statute text, so that the two encodings can
disagree and the disagreement shows up as a failed assertion.

Deterministic and seedless: the same input tree always yields the same file.
Python 3 standard library only.

Usage:  python3 source/gen-tests.py
Writes: encodings/legalese/hvac-tests-generated.l4
"""

from __future__ import annotations

import datetime
import math
import pathlib
from fractions import Fraction

# ---------------------------------------------------------------------------
# Independent re-implementation of the rules
# ---------------------------------------------------------------------------

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def month_length(year: int, month: int) -> int:
    if month == 2 and is_leap(year):
        return 29
    return DAYS_IN_MONTH[month - 1]


def add_months(d: datetime.date, months: int) -> datetime.date:
    """Anniversary arithmetic, CLAMPING the day to the target month's length.

    31 January plus one month is 28 February (29 in a leap year); 29 February
    plus twelve months is 28 February.  This is the reading the statute needs
    for "three months from publication" and "eighteen months from the
    commencement day": the period ends in the named month, never spills into
    the next one.
    """
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    return datetime.date(year, month, min(d.day, month_length(year, month)))


def add_years(d: datetime.date, years: int) -> datetime.date:
    return add_months(d, years * 12)


def round_half_up(x: Fraction) -> int:
    """reg. 3(a): "rounded to the nearest whole new shekel".

    The text does not settle the exact half; half-up is the reading adopted
    (fork F2).  Computed on exact rationals, so a product that lands precisely
    on a half is recognised as such.
    """
    return math.floor(x + Fraction(1, 2))


def updated_fee(fee: int, new_index: Fraction, base_index: Fraction) -> int:
    """reg. 3(a): the reg. 2 amounts are updated by the rate of change of the
    new index against the base index, and rounded to the nearest whole shekel.
    """
    return round_half_up(Fraction(fee) * new_index / base_index)


def licence_expires_on(grant: datetime.date) -> datetime.date:
    """s.8: a licence is valid for five years, or until 31 March of the fifth
    year from the year in which it was granted, WHICHEVER IS EARLIER.

    "The fifth year from the grant year" is read as grant year + 5 (fork F1).
    """
    five_years = add_years(grant, 5)
    march_cap = datetime.date(grant.year + 5, 3, 31)
    return min(five_years, march_cap)


def commencement_day(published: datetime.date,
                     fee_regs_in_force: datetime.date) -> datetime.date:
    """s.63(a)(1): three months from publication, or the commencement of the
    fee regulations under s.59, WHICHEVER IS LATER."""
    return max(add_months(published, 3), fee_regs_in_force)


def non_flammable_from(commencement: datetime.date) -> datetime.date:
    """s.63(a)(2): for every other system, eighteen months from the
    commencement day."""
    return add_months(commencement, 18)


GRADES = ("Grade 1", "Grade 2", "Grade 3")


def lowest_grade(kw: Fraction) -> str:
    """s.2: a Grade 1 licence reaches 18 kW, a Grade 2 licence 70 kW, and a
    Grade 3 licence any system.  The lowest grade that may do the work is
    therefore the first of those whose ceiling the system does not exceed."""
    if kw <= 18:
        return "Grade 1"
    if kw <= 70:
        return "Grade 2"
    return "Grade 3"


def rank(grade: str) -> int:
    return GRADES.index(grade) + 1


def licence_permits(grade: str, kw: Fraction) -> bool:
    return rank(grade) >= rank(lowest_grade(kw))


def may_perform_work(licence: str | None, kw: Fraction, exempted: bool) -> bool:
    """s.3(a): a person shall not do the work unless holding a licence of the
    type suited to the system.  s.3(b): unless the Minister has exempted that
    type of system by order, in which case no licence is called for."""
    if exempted:
        return True
    if licence is None:
        return False
    return licence_permits(licence, kw)


def further_renewal_available(renewals_already_granted: int) -> bool:
    """s.9(b): the temporary licence may be renewed for TWO further periods of
    at most a year each, so a third renewal is not available."""
    return renewals_already_granted < 2


def latest_temporary_day(first_granted: datetime.date) -> datetime.date:
    """s.9: one year, plus two renewals of at most one year each -- three years
    from the first grant at the outside."""
    return add_years(first_granted, 3)


# --- s.6 with the Second Schedule -----------------------------------------

NO_FURTHER = ("no further requirements", None)
NO_ROUTE = ("no route in the Second Schedule", None)


def training(hours: int):
    return ("training of up to", hours)


PART_A = {  # Grade 1
    "no prior training or experience": training(350),
    "Ministry of Education climate-control certificate, 3 units": NO_FURTHER,
    "qualifying experience": training(220),
    "Division completion certificate, refrigeration and air conditioning": training(50),
}

PART_B = {  # Grade 2
    "no prior training or experience": training(480),
    "Ministry of Education climate-control certificate, 5 units": training(50),   # item 5(3); fork F4
    "registered certified technician, having completed a study programme with the completion course": NO_FURTHER,  # item 2
    "registered certified technician, refrigeration and air conditioning": training(50),  # item 6
    "holds a Grade 1 licence": training(100),
    "Division completion certificate, grade 1": training(100),
    "Ministry of Education climate-control certificate, 3 units": training(100),
    "qualifying experience": training(330),
    "Division completion certificate, refrigeration and air conditioning": training(50),
    "Division youth vocational school completion certificate": training(50),
}

PART_C = {  # Grade 3
    "no prior training or experience": training(720),
    "registered practical engineer, having completed a study programme with the completion course": NO_FURTHER,  # item 2
    "registered practical engineer, refrigeration and air conditioning": training(50),  # item 7
    "holds a Grade 1 licence": training(290),
    "Division completion certificate, grade 1": training(290),
    "Ministry of Education climate-control certificate, 3 units": training(290),
    "holds a Grade 2 licence": training(240),
    "Division completion certificate, grade 2": training(240),
    "Ministry of Education climate-control certificate, 5 units": training(240),
    "qualifying experience": training(455),
    "Division completion certificate, refrigeration and air conditioning": training(200),
    "registered engineer, mechanical branch": training(230),
}

SCHEDULE = {"Grade 1": PART_A, "Grade 2": PART_B, "Grade 3": PART_C}


def schedule_requires(grade: str, prior: str):
    return SCHEDULE[grade].get(prior, NO_ROUTE)


def route_is_time_limited(prior: str) -> bool:
    """The experience-only rows (Part A item 2, Part B item 4, Part C item 5)
    each stand for three years from the commencement day; nothing else in the
    Schedule is time-limited."""
    return prior == "qualifying experience"


def route_open(prior: str, commencement: datetime.date,
               application: datetime.date) -> bool:
    if not route_is_time_limited(prior):
        return True
    return application < add_years(commencement, 3)


class Applicant:
    def __init__(self, name, adult, citizen, unfit, holds_certificate,
                 priors, completed_studies):
        self.name = name
        self.adult = adult
        self.citizen = citizen
        self.unfit = unfit
        self.holds_certificate = holds_certificate
        self.priors = tuple(priors)      # column A of the Second Schedule; registry membership is one of them
        self.completed_studies = completed_studies


def personal_conditions(a: Applicant) -> bool:
    """s.6(a)(1)-(3)."""
    return a.adult and a.citizen and not a.unfit


def training_condition(a: Applicant, grade: str, commencement: datetime.date,
                       application: datetime.date) -> bool:
    """s.6(a)(4): the completion certificate (a), OR -- limbs (b) and (c), both
    "in accordance with the conditions in the Second Schedule" -- any row of the
    Schedule that one of the applicant's prior qualifications opens, still open
    on the application date, whose column B is satisfied."""
    if a.holds_certificate:
        return True
    for prior in a.priors:
        if not route_open(prior, commencement, application):
            continue
        kind, _hours = schedule_requires(grade, prior)
        if kind == "no further requirements":
            return True
        if kind == "training of up to" and a.completed_studies:
            return True
    return False


def registrar_shall_grant(a: Applicant, grade: str,
                          commencement: datetime.date,
                          application: datetime.date) -> bool:
    return (personal_conditions(a)
            and training_condition(a, grade, commencement, application))


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def num(x) -> str:
    """Render an exact number as an L4 numeric literal.

    Only terminating decimals are emitted; a non-terminating rational would
    have to be rounded, which would put an inexact value into a test whose
    whole point is exactness, so it is refused loudly instead.
    """
    f = Fraction(x)
    if f.denominator == 1:
        return str(f.numerator)
    den = f.denominator
    twos = fives = 0
    while den % 2 == 0:
        den //= 2
        twos += 1
    while den % 5 == 0:
        den //= 5
        fives += 1
    if den != 1:
        raise ValueError(f"{x} has no terminating decimal expansion")
    places = max(twos, fives)
    scaled = f.numerator * 10 ** places // f.denominator
    sign = "-" if scaled < 0 else ""
    digits = str(abs(scaled)).rjust(places + 1, "0")
    return f"{sign}{digits[:-places]}.{digits[-places:]}"


def ymd(d: datetime.date) -> str:
    return f"YMD {d.year} {d.month} {d.day}"


def bracketed(d: datetime.date) -> str:
    return f"({ymd(d)})"


def grade_lit(g: str) -> str:
    return f"`{g}`"


class Emitter:
    def __init__(self):
        self.lines: list[str] = []
        self.counts: dict[str, int] = {}
        self.family: str | None = None

    def family_section(self, family: str, title: str, blurb: list[str]):
        self.family = family
        self.counts.setdefault(family, 0)
        self.blank()
        self.raw(f"§ `{title}`")
        self.blank()
        for line in blurb:
            self.raw(f"-- {line}" if line else "--")
        self.blank()

    def raw(self, line: str = ""):
        self.lines.append(line)

    def blank(self):
        if self.lines and self.lines[-1] != "":
            self.lines.append("")

    def comment(self, text: str = ""):
        self.raw(f"-- {text}" if text else "--")

    def assert_(self, expr: str):
        """One directive, one line -- #ASSERT never wraps."""
        assert "\n" not in expr
        self.raw(f"#ASSERT {expr}")
        self.counts[self.family] += 1

    def assert_bool(self, expr: str, expected: bool):
        self.assert_(expr if expected else f"NOT {expr}")

    def text(self) -> str:
        return "\n".join(self.lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# The families
# ---------------------------------------------------------------------------

FEES = (40, 158, 194, 284, 398)

COMMON_INDEX_PAIRS = (
    (Fraction(100), Fraction(100), "no change: the index stood still"),
    (Fraction("105.3"), Fraction("104.1"), "a small rise, the pair used in the encoding's own illustrations"),
    (Fraction("112.4"), Fraction(100), "a larger rise"),
    (Fraction("99.2"), Fraction("101.5"), "a fall: the updated fee goes down"),
    (Fraction(101), Fraction(100), "a rise of one per cent"),
)


def half_pairs(fee: int):
    """Index pairs engineered so that fee * new / base is EXACTLY a half.

    Taking the base index as twice the fee makes the product new/2, so an odd
    new index puts it precisely on the boundary.  These are the cases that
    tell half-up apart from half-even and from truncation.
    """
    out = []
    for ratio, label in ((Fraction(1), "just above par"),
                         (Fraction("1.03"), "a three per cent rise"),
                         (Fraction("0.97"), "a three per cent fall")):
        half = Fraction(math.floor(fee * ratio)) + Fraction(1, 2)
        new = 2 * half
        base = Fraction(2 * fee)
        assert Fraction(fee) * new / base == half
        out.append((new, base, half, label))
    return out


def family_indexation(e: Emitter):
    e.family_section(
        "a",
        "reg. 3 -- the annual indexation of the fees",
        ["reg. 3(a): the reg. 2 amounts are updated on 1 January of each year by the",
         "rate of change of the new index against the base index, and rounded to the",
         "nearest whole new shekel. The rounding of an exact half is not settled by the",
         "text; half-up is the reading adopted. The fees are the five distinct amounts",
         "that appear across the three vintages of reg. 2: 40, 158, 194, 284 and 398."])
    e.comment("Ordinary movements of the index, across all five fee amounts.")
    for new, base, note in COMMON_INDEX_PAIRS:
        e.blank()
        e.comment(f"new index {num(new)} against base index {num(base)} -- {note}.")
        for fee in FEES:
            expected = updated_fee(fee, new, base)
            e.assert_(f"`the updated fee` {fee} {num(new)} {num(base)} EQUALS {expected}")
    e.blank()
    e.comment("Exactly on the half. Each pair below is engineered so that the product")
    e.comment("fee x new / base is a whole number of shekels plus exactly one half, which")
    e.comment("is where half-up, half-even and truncation part company. Half-up rounds")
    e.comment("every one of them away from zero.")
    for fee in FEES:
        e.blank()
        for new, base, half, label in half_pairs(fee):
            expected = round_half_up(half)
            e.comment(f"{fee} x {num(new)} / {num(base)} = {num(half)} exactly -- {label}.")
            e.assert_(f"`the updated fee` {fee} {num(new)} {num(base)} EQUALS {expected}")


VALIDITY_DAYS = ((1, 1), (1, 15), (2, 28), (3, 31), (4, 1), (6, 30), (9, 1), (12, 31))
VALIDITY_YEARS = (2025, 2026, 2027, 2028)


def family_validity(e: Emitter):
    e.family_section(
        "b",
        "s.8 -- the period of validity of a licence",
        ["s.8: a licence is valid for five years, or until 31 March of the fifth year",
         "from the year in which it was granted, whichever is the earlier. So a licence",
         "granted after 31 March is cut short by the 31 March cap, and one granted on or",
         "before it runs its full five years. The fifth year from the grant year is read",
         "as grant year + 5."])
    for year in VALIDITY_YEARS:
        e.blank()
        e.comment(f"Granted in {year}. The cap falls on 31 March {year + 5}.")
        for month, day in VALIDITY_DAYS:
            grant = datetime.date(year, month, day)
            expiry = licence_expires_on(grant)
            which = "five years" if expiry != datetime.date(year + 5, 3, 31) else "the 31 March cap"
            e.assert_(f"`the licence expires on` {bracketed(grant)} EQUALS {ymd(expiry)}"
                      + f"   -- {which}")
    e.blank()
    e.comment("The leap day: five years from 29 February 2028 is clamped to 28 February")
    e.comment("2033, which is earlier than the 31 March 2033 cap and so governs.")
    leap = datetime.date(2028, 2, 29)
    e.assert_(f"`the licence expires on` {bracketed(leap)} EQUALS {ymd(licence_expires_on(leap))}")


COMMENCEMENT_CASES = (
    (datetime.date(2025, 1, 14), datetime.date(2025, 7, 16),
     "what actually happened: published 14 January 2025, the fee regulations in force from 16 July 2025, which is the later"),
    (datetime.date(2025, 1, 14), datetime.date(2025, 3, 1),
     "the counterfactual: had the fee regulations come into force on 1 March 2025, three months from publication would have been the later"),
    (datetime.date(2025, 1, 14), datetime.date(2025, 4, 14),
     "the tie: the fee regulations in force on the very day three months from publication falls"),
    (datetime.date(2025, 11, 30), datetime.date(2025, 12, 1),
     "a month-end clamp: 30 November plus three months is 28 February, there being no 30 February"),
    (datetime.date(2027, 11, 30), datetime.date(2028, 1, 1),
     "the same clamp in a leap year: 29 February 2028"),
    (datetime.date(2025, 1, 31), datetime.date(2025, 1, 1),
     "31 January plus three months is 30 April, April being a thirty-day month"),
    (datetime.date(2025, 8, 31), datetime.date(2025, 1, 1),
     "31 August plus three months is 30 November"),
    (datetime.date(2024, 11, 30), datetime.date(2024, 12, 1),
     "30 November 2024 plus three months is 28 February 2025, which is not a leap year"),
)

EIGHTEEN_MONTH_CASES = (
    (datetime.date(2025, 7, 16), "the real commencement day"),
    (datetime.date(2025, 4, 14), "the counterfactual commencement day"),
    (datetime.date(2026, 2, 28), "an ordinary 28 February"),
    (datetime.date(2028, 2, 29), "a leap day: August has thirty-one days, so nothing is clamped"),
    (datetime.date(2025, 8, 31), "31 August plus eighteen months is clamped to 28 February 2027"),
    (datetime.date(2026, 8, 31), "the same clamp landing in a leap year: 29 February 2028"),
    (datetime.date(2025, 12, 31), "31 December plus eighteen months is clamped to 30 June"),
    (datetime.date(2025, 3, 31), "31 March plus eighteen months is clamped to 30 September"),
)


def family_commencement(e: Emitter):
    e.family_section(
        "c",
        "s.63 -- commencement",
        ["s.63(a)(1): for systems using a flammable refrigerant, the Law commences three",
         "months from its publication or on the commencement of the fee regulations under",
         "s.59, whichever is the later -- and that day is 'the commencement day'.",
         "s.63(a)(2): for a system on a refrigerant outside the Fourth Schedule, eighteen months from the commencement day.",
         "Both periods are month arithmetic, so both clamp to the length of the month",
         "they land in."])
    e.comment("s.63(a)(1): the later of three months from publication and the fee")
    e.comment("regulations coming into force.")
    for published, regs, note in COMMENCEMENT_CASES:
        answer = commencement_day(published, regs)
        e.blank()
        e.comment(f"{note.capitalize()}.")
        e.assert_(f"`the commencement day` {bracketed(published)} {bracketed(regs)} EQUALS {ymd(answer)}")
    e.blank()
    e.comment("s.63(a)(2): eighteen months from the commencement day.")
    for day, note in EIGHTEEN_MONTH_CASES:
        answer = non_flammable_from(day)
        e.blank()
        e.comment(f"{note.capitalize()}.")
        e.assert_(f"`the Law applies to systems on refrigerants outside the Fourth Schedule from` {bracketed(day)} EQUALS {ymd(answer)}")


KW_VALUES = (Fraction(0), Fraction(1), Fraction("17.99"), Fraction(18),
             Fraction("18.01"), Fraction(50), Fraction("69.99"), Fraction(70),
             Fraction("70.01"), Fraction(100), Fraction(1000))


def family_grades(e: Emitter):
    e.family_section(
        "d",
        "ss.2 and 3 -- the grades and the duty to hold a licence",
        ["s.2: a Grade 1 licence reaches a system of up to 18 kW, a Grade 2 licence up to",
         "70 kW, and a Grade 3 licence any system. s.3(a): a person shall not perform the",
         "work unless holding a licence of the type suited to that system. s.3(b): the",
         "Minister may exempt types of system by order, and an exempted system needs no",
         "licence at all. The cooling outputs below sit on both sides of each ceiling,",
         "a hundredth of a kilowatt apart, because 'up to' includes the ceiling itself."])
    e.comment("The lowest grade that may work on a system of the stated output.")
    for kw in KW_VALUES:
        e.assert_(f"`the lowest grade permitted to work on a system of` {num(kw)} EQUALS {grade_lit(lowest_grade(kw))}")
    e.blank()
    e.comment("A licence holder, on a system that has not been exempted by order. A")
    e.comment("licence of a higher grade reaches down to the smaller systems as well.")
    for grade in GRADES:
        e.blank()
        e.comment(f"A {grade} licence.")
        for kw in KW_VALUES:
            expected = may_perform_work(grade, kw, False)
            e.assert_bool(f"`the licence grade reaches the system` (JUST {grade_lit(grade)}) {num(kw)} FALSE", expected)
    e.blank()
    e.comment("No licence at all, on a system that has not been exempted: never permitted,")
    e.comment("however small the system.")
    for kw in KW_VALUES:
        e.assert_bool(f"`the licence grade reaches the system` NOTHING {num(kw)} FALSE",
                      may_perform_work(None, kw, False))
    e.blank()
    e.comment("No licence, on a system the Minister has exempted under s.3(b): always")
    e.comment("permitted, however large the system.")
    for kw in KW_VALUES:
        e.assert_bool(f"`the licence grade reaches the system` NOTHING {num(kw)} TRUE",
                      may_perform_work(None, kw, True))


TEMPORARY_GRANTS = (
    (datetime.date(2025, 7, 16), "the commencement day itself"),
    (datetime.date(2025, 12, 31), "the last day of a year"),
    (datetime.date(2026, 1, 1), "the first day of a year"),
    (datetime.date(2028, 2, 29), "a leap day, clamped to 28 February 2031"),
)


def family_foreign_expert(e: Emitter):
    e.family_section(
        "e",
        "s.9 -- the foreign expert's temporary licence",
        ["s.9(a): the registrar may grant a foreign expert a temporary Grade 3 licence",
         "for a period of up to one year. s.9(b): it may be renewed for two further",
         "periods of at most one year each -- so a third renewal is not available, and",
         "the licence cannot run beyond three years from the day it was first granted."])
    e.comment("s.9(b): two renewals, and no more.")
    for n in range(5):
        e.assert_bool(f"`a further renewal of the temporary licence is available` {n}",
                      further_renewal_available(n))
    e.blank()
    e.comment("The outside date, one year plus two renewals of a year each.")
    for grant, note in TEMPORARY_GRANTS:
        e.comment(f"First granted on {grant.isoformat()}, {note}.")
        e.assert_(f"`the latest day a temporary licence can run to` {bracketed(grant)} EQUALS {ymd(latest_temporary_day(grant))}")


COMMENCEMENT = datetime.date(2025, 7, 16)

APPLICATION_DATES = (
    (datetime.date(2025, 7, 16), "the commencement day itself"),
    (datetime.date(2026, 1, 1), "well inside the three years"),
    (datetime.date(2028, 7, 15), "the last day the experience route is open"),
    (datetime.date(2028, 7, 16), "three years to the day: the experience route has closed"),
    (datetime.date(2030, 1, 1), "long after it closed"),
)

DANA = Applicant(
    name="Dana, who relies on her experience",
    adult=True, citizen=True, unfit=False,
    holds_certificate=False,
    priors=["qualifying experience"], completed_studies=True)

NOA = Applicant(
    name="Noa, with the five-unit certificate",
    adult=True, citizen=True, unfit=False,
    holds_certificate=False,
    priors=["Ministry of Education climate-control certificate, 5 units"],
    completed_studies=True)

NOA_WITH_CERTIFICATE = Applicant(
    name="Noa, once she holds the completion certificate",
    adult=True, citizen=True, unfit=False,
    holds_certificate=True,
    priors=["Ministry of Education climate-control certificate, 5 units"],
    completed_studies=True)

FIXTURES = (DANA, NOA, NOA_WITH_CERTIFICATE)


def emit_fixture(e: Emitter, a: Applicant):
    e.raw(f"`{a.name}` MEANS Applicant WITH")
    fields = (
        ("is an adult", a.adult),
        ("is an Israeli citizen or resident", a.citizen),
        ("is unfit by reason of a conviction or pending indictment", a.unfit),
        ("holds a completion certificate for the grade", a.holds_certificate),
    )
    width = max(len(f"`{n}`") for n, _ in fields)
    width = max(width, len("`prior qualifications`"),
                len("`completed the supplementary studies the Schedule requires`"))
    for name, value in fields:
        e.raw(f"    {('`' + name + '`').ljust(width)} IS {'TRUE' if value else 'FALSE'}")
    priors = ", ".join(f"`{p}`" for p in a.priors)
    e.raw(f"    {'`prior qualifications`'.ljust(width)} IS LIST {priors}")
    e.raw(f"    {'`completed the supplementary studies the Schedule requires`'.ljust(width)}"
          f" IS {'TRUE' if a.completed_studies else 'FALSE'}")


def family_schedule(e: Emitter):
    e.family_section(
        "f",
        "s.6 with the Second Schedule -- the sunset on the experience route",
        ["s.6(a): the registrar shall grant the licence to an applicant who is an adult,",
         "an Israeli citizen or resident, not unfit by reason of a conviction, and who",
         "satisfies s.6(a)(4) -- the completion certificate, or a row of the Second",
         "Schedule (where registration in the technicians and engineers registry also",
         "lives) that one of the applicant's prior qualifications opens.",
         "",
         "The experience-only rows of the Schedule (Part A item 2, Part B item 4, Part C",
         "item 5) each stand for three years from the commencement day and no longer.",
         "The commencement day is 16 July 2025, so those rows close on 16 July 2028.",
         "Nothing else in the Schedule is time-limited.",
         "",
         "Three applicants, alike in everything the Schedule does not reach."])
    for a in FIXTURES:
        e.blank()
        emit_fixture(e, a)
    e.blank()
    e.comment("Dana's route is the experience row, so her answer turns on the date she")
    e.comment("applies -- and on nothing else. All three grades close together.")
    for grade in GRADES:
        e.blank()
        e.comment(f"{grade}: Part {'ABC'[rank(grade) - 1]} of the Schedule asks her for supplementary")
        kind, hours = schedule_requires(grade, DANA.priors[0])
        e.comment(f"studies of up to {hours} hours, which she has completed.")
        for application, note in APPLICATION_DATES:
            expected = registrar_shall_grant(DANA, grade, COMMENCEMENT, application)
            e.assert_bool(f"`the registrar shall grant the licence` `{DANA.name}` {grade_lit(grade)} "
                          f"{bracketed(COMMENCEMENT)} {bracketed(application)}", expected)
    e.blank()
    e.comment("Noa's route is the five-unit certificate, which the Schedule does not")
    e.comment("time-limit. Part B item 5 asks 50 hours of her (item 1(2) would ask nothing,")
    e.comment("fork F4), which she has done, so a Grade 2 licence is hers on every one of")
    e.comment("those dates, including the ones on which Dana's route has closed.")
    for application, note in APPLICATION_DATES:
        e.assert_bool(f"`the registrar shall grant the licence` `{NOA.name}` `Grade 2` "
                      f"{bracketed(COMMENCEMENT)} {bracketed(application)}",
                      registrar_shall_grant(NOA, "Grade 2", COMMENCEMENT, application))
    e.blank()
    e.comment("Part A, however, has no row for the five-unit certificate at all: it is the")
    e.comment("THREE-unit certificate that opens the Grade 1 door. So Noa has no route to a")
    e.comment("Grade 1 licence on any date -- a refusal that has nothing to do with the")
    e.comment("sunset, and does not move when the sunset passes.")
    for application, note in APPLICATION_DATES:
        e.assert_bool(f"`the registrar shall grant the licence` `{NOA.name}` `Grade 1` "
                      f"{bracketed(COMMENCEMENT)} {bracketed(application)}",
                      registrar_shall_grant(NOA, "Grade 1", COMMENCEMENT, application))
    e.blank()
    e.comment("Part C does have a row for her, asking 240 hours of supplementary studies,")
    e.comment("which she has done -- so Grade 3 is open although Grade 1 is not.")
    for application, note in APPLICATION_DATES[:2]:
        e.assert_bool(f"`the registrar shall grant the licence` `{NOA.name}` `Grade 3` "
                      f"{bracketed(COMMENCEMENT)} {bracketed(application)}",
                      registrar_shall_grant(NOA, "Grade 3", COMMENCEMENT, application))
    e.blank()
    e.comment("The Second Schedule is a route, not the only one. Once Noa holds the")
    e.comment("completion certificate for the grade, s.6(a)(4)(a) answers on its own and")
    e.comment("the Grade 1 door opens.")
    for application, note in (APPLICATION_DATES[0], APPLICATION_DATES[-1]):
        e.assert_bool(f"`the registrar shall grant the licence` `{NOA_WITH_CERTIFICATE.name}` `Grade 1` "
                      f"{bracketed(COMMENCEMENT)} {bracketed(application)}",
                      registrar_shall_grant(NOA_WITH_CERTIFICATE, "Grade 1", COMMENCEMENT, application))


FAMILY_TITLES = {
    "a": "reg. 3 indexation",
    "b": "s.8 validity",
    "c": "s.63 commencement",
    "d": "ss.2-3 grades",
    "e": "s.9 foreign expert",
    "f": "s.6 Second Schedule",
}


HEADER = """\
-- THIS FILE IS GENERATED by source/gen-tests.py. DO NOT EDIT IT BY HAND.
-- Regenerate with:  python3 source/gen-tests.py
--
-- Tier 3: a generated test suite for hvac-law.l4 and hvac-fees.l4.
--
-- Every expected value here was computed by an INDEPENDENT re-implementation,
-- in Python, of the rules quoted in the comments of those two files -- not by
-- running the L4. The two encodings are meant to be able to disagree; where
-- they do, the assertion goes red and somebody has to decide which reading of
-- the statute is right.
--
-- The families, and what each is looking for:
--   a. reg. 3, the annual indexation -- exact rational arithmetic, and the
--      rounding of a product that lands precisely on a half shekel.
--   b. s.8, the period of validity -- the race between five years and the
--      31 March cap, and the clamp on a leap-day grant.
--   c. s.63, commencement -- the later of two days, and month arithmetic that
--      clamps to the length of the month it lands in.
--   d. ss.2 and 3, the grades -- both sides of each kilowatt ceiling, the
--      unlicensed person, and the exempted system.
--   e. s.9, the foreign expert -- two renewals and no more.
--   f. s.6 with the Second Schedule -- the three-year sunset on the
--      experience route, against a route that never sunsets.
@lang en

IMPORT prelude
IMPORT daydate
IMPORT `hvac-law`
IMPORT `hvac-fees`
"""


def main():
    here = pathlib.Path(__file__).resolve().parent
    out_path = here.parent / "encodings" / "legalese" / "hvac-tests-generated.l4"

    e = Emitter()
    e.raw(HEADER.rstrip("\n"))
    family_indexation(e)
    family_validity(e)
    family_commencement(e)
    family_grades(e)
    family_foreign_expert(e)
    family_schedule(e)

    out_path.write_text(e.text(), encoding="utf-8")

    total = sum(e.counts.values())
    parts = ", ".join(f"{k} {FAMILY_TITLES[k]} {v}" for k, v in sorted(e.counts.items()))
    print(f"{out_path.relative_to(here.parent)}: {total} assertions across "
          f"{len(e.counts)} families -- {parts}")


if __name__ == "__main__":
    main()
