"""Module and test builders, plus the coverage ledger."""
import textwrap
from lib import quote, heading, Facts, Pun, pred, charge, mu, and_fine

COVERAGE = {}   # section -> (disposition, functions/reason)


class Module:
    def __init__(self, path, header, imports):
        self.path, self.parts = path, [header.rstrip() + "\n", "\n".join(imports) + "\n"]

    def chapter(self, title):
        self.parts.append(f"§ `{title}`\n")

    def section(self, n, title=None, extra_comment=None, quote_it=True):
        t = title or heading(n)
        self.parts.append(f"§§ `s {n} - {t}`\n")
        if quote_it:
            self.parts.append(quote(n) + "\n")
        if extra_comment:
            self.parts.append("\n".join("-- " + l for l in textwrap.wrap(extra_comment, 84)) + "\n")

    def repealed(self, n, note):
        self.parts.append(f"-- s {n}. {note}\n")
        COVERAGE[n] = ("repealed", note)

    def add(self, *texts):
        for t in texts:
            self.parts.append(t.l4() if hasattr(t, "l4") else t)

    def offence(self, sec, facts, title, body, comment=None):
        out = []
        if comment:
            out.append("\n".join("-- " + l for l in textwrap.wrap(comment, 84)))
        out.append(f"@export Whether the accused has committed an offence punishable under section {sec} of the Penal Code 1871 ({title})")
        out.append(f"GIVEN f IS A {facts.ident} @desc {facts.about}")
        out.append("GIVETH A BOOLEAN")
        out.append(f"DECIDE `offence under s {sec}` f IF")
        out.append(textwrap.indent(textwrap.dedent(body).strip("\n"), "    "))
        self.parts.append("\n".join(out) + "\n")

    def helper(self, text):
        self.parts.append(textwrap.dedent(text).strip("\n") + "\n")

    def write(self):
        open(self.path, "w").write("\n".join(self.parts))


class Tests:
    def __init__(self, path, header, imports):
        self.path, self.parts = path, [header.rstrip() + "\n", "\n".join(imports) + "\n"]

    def add(self, text):
        self.parts.append(textwrap.dedent(text).strip("\n") + "\n")

    def fixture(self, facts, name, true=(), strings=None, comment=None):
        if comment:
            self.parts.append("\n".join("-- " + l for l in textwrap.wrap(comment, 84)))
        self.parts.append(facts.fixture(name, true, strings))

    def write(self):
        open(self.path, "w").write("\n".join(self.parts))


# one catalogue entry per punishing section, for the report
CATALOGUE = []


def catalogue(section, title, defines, family, facts, definition_fns):
    CATALOGUE.append(dict(section=section, title=title, defines=defines, family=family,
                          offenceFn=f"offence under s {section}", chargeFn=f"charge under s {section}",
                          definitionFns=definition_fns, factsType=facts.name, factsParam="f"))


# ------------------------------------------------------------------ tiers
TIER_DEATH = "the offence is punishable with death"
TIER_LIFE = "the offence is punishable with imprisonment for life or with imprisonment which may extend to 20 years"


def tier_puns(sec, c_words=None):
    """The (a)/(b)/(c) punishments common to ss 201, 212, 213, 214, 216."""
    a = and_fine(f"{sec}(a)", f"{sec}(a)", 10)
    b = and_fine(f"{sec}(b)", f"{sec}(b)", 7)
    c = Pun(f"{sec}(c)", f"{sec}(c)", c_words or "imprisonment for a term which may extend to one-fourth part of the longest term of imprisonment provided for that offence, or with fine, or with both",
            imp="or", fine="or", both=True)
    return a, b, c


def tier_expr(sec, tier_c):
    return (f"IF f's `{TIER_DEATH}` THEN (`punishment prescribed by s {sec}(a)`)'s words "
            f"ELSE IF f's `{TIER_LIFE}` THEN (`punishment prescribed by s {sec}(b)`)'s words "
            f"ELSE (`punishment prescribed by s {sec}(c)`)'s words")




def ladder(elems, lead='"Whoever"'):
    lines = [f"    {lead}"] if lead else []
    first = not lead
    for expr, _ in elems:
        lines.append(("    " if first else "AND ") + expr)
        first = False
    return "\n".join(lines)


def missing_of(elems):
    return [mu(e, w) for e, w in elems if w]


def family(m, sec, facts, verb, export, elems, name, recital, fam, defines,
           puns=(), pun_expr=None, extra=(), comment=None, title=None, verb_exists=False, lead='"Whoever"'):
    """One punishing section over a defining predicate `verb` built from elems.
    extra: further (expr, words) elements the PUNISHING section adds (tiers, aggravation)."""
    for p in puns:
        m.add(p)
    if not verb_exists:
        m.add(pred(verb, facts, export, ladder(elems, lead)))
    body = f'    "Whoever"\nAND {verb} f' + "".join(f"\nAND {e}" for e, _ in extra)
    m.offence(sec, facts, title or name, body, comment=comment)
    if pun_expr is None:
        pun_expr = f"(`punishment prescribed by s {sec}`)'s words"
    miss = missing_of(elems) + missing_of(extra) + [mu(f"{verb} f", f"the elements of section {defines.split(',')[0].replace('ss ', '').replace('s ', '')} taken together")]
    m.add(charge(sec, facts, f'"{name}"', pun_expr, recital, miss, title=title or name))
    catalogue(sec, name, defines, fam, facts, [verb.strip('`')])


def recite(phrase, field="what was done"):
    return f'CONCAT "{phrase}", (`to wit` (f\'s `{field}`))'
