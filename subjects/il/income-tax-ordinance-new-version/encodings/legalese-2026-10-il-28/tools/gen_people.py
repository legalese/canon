#!/usr/bin/env python3
"""Generate ito-il28-test-people.l4: the taxpayers and the readings the tests use, every field spelled out.
Run: python3 -I tools/gen_people.py > ito-il28-test-people.l4
The EXPECTED VALUES are not here: they are in the tests modules, written by hand from the Hebrew."""
BASE = dict(
    year=2025, individual=True, woman=False, israeli_resident=False,
    area=False, citizen=False, law_of_return=False, area_months=None,
    favoured=False, dependent=False, proved=False, exertion=True,
    worker=False, fwl_resident=False, visa=False, permitted=False, expert=False,
    b1=False, caring_permit=False, extended=False, months=12, income_2_1_2=True)
B = lambda b: "TRUE" if b else "FALSE"
def rec(**kw):
    d = dict(BASE); d.update(kw)
    res = ("`the Area residence entered held for the whole tax year`" if d["area_months"] is None else
           f"`a resident of the Area for only part of the tax year` {d['area_months']}")
    return f"""Taxpayer WITH
    `the tax year`                                            IS {d['year']}
    `an individual`                                           IS {B(d['individual'])}
    `a woman`                                                 IS {B(d['woman'])}
    `an Israeli resident in the tax year`                     IS {B(d['israeli_resident'])}
    `a resident of the Area`                                  IS {B(d['area'])}
    `an Israeli citizen under the Citizenship Law`            IS {B(d['citizen'])}
    `entitled to immigrate under the Law of Return`           IS {B(d['law_of_return'])}
    `the taxpayer's residence in the Area over the tax year`  IS {res}
    `a favoured individual within section 37`                 IS {B(d['favoured'])}
    `the spouse's livelihood was upon the taxpayer`           IS {B(d['dependent'])}
    `the taxpayer proved it to the assessor's satisfaction`   IS {B(d['proved'])}
    `the taxpayer had income from personal exertion in the tax year` IS {B(d['exertion'])}
    `a worker`                                                IS {B(d['worker'])}
    `a resident of Israel within the Foreign Workers Law`     IS {B(d['fwl_resident'])}
    `holds a visa under section 2 of the Entry into Israel Law, or needs one` IS {B(d['visa'])}
    `stay in Israel or the Area and employment there are permitted by law` IS {B(d['permitted'])}
    `an expert from abroad or a guest lecturer`               IS {B(d['expert'])}
    `holds a B/1 temporary worker visa and licence`           IS {B(d['b1'])}
    `holds a permit to work in the caring sector`             IS {B(d['caring_permit'])}
    `the stay is extended under section 3A(b) of the Entry into Israel Law` IS {B(d['extended'])}
    `the months of the tax year spent in Israel or the Area`  IS {d['months']}
    `the income taxed is income under section 2(1) or (2)`    IS {B(d['income_2_1_2'])}"""
AREA = dict(area=True)
S37 = dict(favoured=True, dependent=True, proved=True)
LEGAL = dict(worker=True, visa=True, permitted=True, b1=True)
CARING = dict(LEGAL, caring_permit=True, extended=True)
people = {}
def add(name, *bases, **kw):
    d = {}
    for b in bases: d.update(b)
    d.update(kw)
    people[name] = rec(**d)
# ---- residents of the Area ----
add("an Area man", **AREA)
add("an Area woman", AREA, woman=True)
add("an Area man with a dependent spouse, a favoured individual, proved", AREA, **S37)
add("an Area man whose spouse's dependence is not proved", AREA, favoured=True, dependent=True, proved=False)
add("an Area man whose spouse is not dependent", AREA, favoured=True, dependent=False, proved=True)
add("an Area man who is not a favoured individual", AREA, favoured=False, dependent=True, proved=True)
add("an Area man without income from personal exertion", AREA, exertion=False)
add("an Area man resident in the Area for 6 months", AREA, area_months=6)
add("an Area woman resident in the Area for 6 months", AREA, woman=True, area_months=6)
add("an Area man resident in the Area for 0 months", AREA, area_months=0)
add("an Area man resident in the Area for 12 months entered as part of a year", AREA, area_months=12)
add("an Area man resident in the Area for 11 months", AREA, area_months=11)
add("an Area man resident in the Area for 1 month", AREA, area_months=1)
add("an Area company", AREA, individual=False)
add("an Israeli citizen resident in the Area", AREA, citizen=True)
add("a resident of the Area entitled to immigrate under the Law of Return", AREA, law_of_return=True)
add("a person entitled to immigrate under the Law of Return who is not a resident of the Area", law_of_return=True)
add("a resident of the Area who is also an Israeli resident", AREA, israeli_resident=True)
add("a man with no tie to the Area")
for y in (1994, 1995, 2016, 2017, 2022, 2023):
    add(f"an Area man in {y}", AREA, year=y)
    add(f"an Area man with a dependent spouse, a favoured individual, proved, in {y}", AREA, S37, year=y)
# ---- foreign workers ----
for res, rn in ((True, "an Israeli resident"), (False, "not an Israeli resident")):
    add(f"a caring-sector legal foreign man, {rn}", CARING, israeli_resident=res)
    add(f"a caring-sector legal foreign woman, {rn}", CARING, israeli_resident=res, woman=True)
    add(f"a legal foreign man, not in the caring sector, {rn}", LEGAL, israeli_resident=res)
    add(f"a legal foreign woman, not in the caring sector, {rn}", LEGAL, israeli_resident=res, woman=True)
add("a caring-sector legal foreign man, an Israeli resident, for 6 months", CARING, israeli_resident=True, months=6)
add("a caring-sector legal foreign woman, an Israeli resident, for 6 months", CARING, israeli_resident=True, woman=True, months=6)
add("a legal foreign man, not in the caring sector, an Israeli resident, for 9 months", LEGAL, israeli_resident=True, months=9)
add("a caring-sector legal foreign man, an Israeli resident, for 0 months", CARING, israeli_resident=True, months=0)
add("a caring-sector legal foreign man, an Israeli resident, for 13 months", CARING, israeli_resident=True, months=13)
add("a caring-sector legal foreign man, an Israeli resident, for -1 months", CARING, israeli_resident=True, months=-1)
add("a foreign man with a B/1 visa whose stay is not permitted by law", LEGAL, israeli_resident=True, permitted=False)
add("a foreign man who is an expert from abroad", LEGAL, israeli_resident=True, expert=True)
add("a foreign man who holds no B/1 visa", LEGAL, israeli_resident=True, b1=False)
add("a foreign man who needs no visa", LEGAL, israeli_resident=True, visa=False)
add("an Israeli citizen who works in Israel", LEGAL, israeli_resident=True, citizen=True, visa=False)
add("a worker who is a resident of Israel under the Foreign Workers Law", LEGAL, israeli_resident=True, fwl_resident=True, visa=False)
add("a person who is not a worker", LEGAL, israeli_resident=True, worker=False)
add("a caring-sector legal foreign woman, an Israeli resident, taxed on other income", CARING, israeli_resident=True, woman=True, income_2_1_2=False)
add("a legal foreign man with a caring-sector permit whose stay is not extended, an Israeli resident", LEGAL, israeli_resident=True, caring_permit=True, extended=False)
add("a legal foreign man whose stay is extended but who has no caring-sector permit, an Israeli resident", LEGAL, israeli_resident=True, caring_permit=False, extended=True)
add("a caring-sector legal foreign man without income from personal exertion, an Israeli resident", CARING, israeli_resident=True, exertion=False)
add("a caring-sector legal foreign man without income from personal exertion, not an Israeli resident", CARING, israeli_resident=False, exertion=False)
for y in (2001, 2002, 2014, 2015, 2018, 2019):
    add(f"a caring-sector legal foreign man, an Israeli resident, in {y}", CARING, israeli_resident=True, year=y)
add("a legal foreign man, not in the caring sector, who is also a resident of the Area and not an Israeli citizen", LEGAL, area=True)
add("a caring-sector legal foreign man who is also a resident of the Area and not an Israeli citizen", CARING, area=True)
add("a foreign man who needs a visa but is not legal, who is also a resident of the Area and not an Israeli citizen", worker=True, visa=True, area=True)

# ---- readings ----
FORKS = [
 ("F1", "fork F1, section 36A and residence", "A reading of section 36A on residence",
  ["section 36A has no residence condition", "section 36A gives its half point only to an Israeli resident", "declined where residence decides section 36A"]),
 ("F2", "fork F2, section 36 and income from personal exertion", "A reading of section 36 on income from personal exertion",
  ["section 36 for every individual", "section 36 only for an individual with income from personal exertion", "declined where income from personal exertion decides section 36"]),
 ("F4", "fork F4, residence in the Area for part of a tax year", None,
  ["one residence status for the whole tax year", "apportioned by the months of residence, as section 41 apportions", "declined for residence in part of a tax year"]),
 ("FW1", "fork FW1, the cited sections' conditions", None,
  ["the regulations give their points without the cited sections' residence conditions", "the cited sections' own residence conditions still apply", "declined where the cited sections' residence conditions decide"]),
 ("FW2", "fork FW2, the tax years from 2002 to 2014", None,
  ["no instrument under section 48A applied before the regulations of 5775-2014", None, "declined for the tax years from 2002 to 2014"]),
 ("FW3", "fork FW3, regulation 3(d) and deductions", None,
  ["regulation 3(d) reaches credits only, which is all the power of section 48A gives", "regulation 3(d) reaches the whole chapter as it is written", "declined where regulation 3(d) and the chapter's deductions meet"]),
 ("OV", "fork OV, both instruments reach the taxpayer", None,
  ["the foreign worker regulations prevail", "the Area order prevails", "declined where the order and the regulations both reach the taxpayer"]),
]
# values listed as [reading A, reading B, declined]; for FW3 reading A = credits only, B = whole chapter
# (the NOTES.md fork register gives the same lettering); FW2 has only A and declined.
def readings(**pick):
    lines = ["`The readings of the forks of row IL-28` WITH"]
    for fid, field, _t, vals in FORKS:
        v = vals[{"A": 0, "B": 1, "D": 2}[pick.get(fid, "D")]]
        assert v, (fid, pick)
        lines.append(f"    `{field}` IS `{v}`")
    return "\n".join(lines)
named = {"the default readings": readings()}
for fid, field, _t, vals in FORKS:
    for k in ("A", "B"):
        if vals[{"A": 0, "B": 1}[k]]:
            named[f"the default readings but {fid} is {k}"] = readings(**{fid: k})
named["the default readings but F1 is A and FW1 is B"] = readings(F1="A", FW1="B")
named["the default readings but F2 is B and FW1 is D"] = readings(F2="B")
named["the default readings but F4 is B and F1 is A"] = readings(F4="B", F1="A")
named["the default readings but FW1 is A and F2 is A"] = readings(FW1="A", F2="A")
named["the default readings but FW1 is A and OV is A"] = readings(FW1="A", OV="A")
named["the default readings but FW1 is A and OV is B"] = readings(FW1="A", OV="B")
named["the default readings but FW1 is B and F1 is B"] = readings(FW1="B", F1="B")
named["the default readings but FW1 is B and F1 is A"] = readings(FW1="B", F1="A")
named["the default readings but FW1 is B and F1 is D"] = readings(FW1="B")

print("""@lang en

IMPORT prelude
IMPORT `ito-il28-nouns`

-- ===========================================================================
-- Row IL-28: the taxpayers and the readings the tests use, generated by tools/gen_people.py.
-- Every field of every taxpayer is spelled out. No expected value is here: they are in the tests modules,
-- written by hand from the Hebrew text before the code was run.
--
-- Lettering of the readings: A is the first reading listed under the fork in ito-il28-nouns.l4 and NOTES.md,
-- B the second, D the declined default. FW2 has no B.
-- ===========================================================================

§ `The taxpayers`
""")
for n, r in people.items():
    print(f"`{n}` MEANS {r}\n")
print("§ `The readings`\n")
for n, r in named.items():
    print(f"`{n}` MEANS {r}\n")
