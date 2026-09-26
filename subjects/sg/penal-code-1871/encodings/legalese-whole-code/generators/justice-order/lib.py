"""Generator library for the justice-order group's L4 (Penal Code 1871, Chapters 11-15).

The spec files (ch11.py, ch12_15.py) describe each section; this library turns
them into L4 text: quoted source, facts records, defining predicates, offence
ladders, punishment records, charge builders, and full-literal test fixtures.
"""
import re, textwrap

SRC = "/Users/mengwong/src/legalese/pc-encode/inputs/PC1871.txt"
ASCII = {"’": "'", "‘": "'", "“": '"', "”": '"', "—": "-", "–": "-",
         "…": "...", " ": " "}


def asciify(s):
    for k, v in ASCII.items():
        s = s.replace(k, v)
    return s


def _load():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    toc = {}
    last = None
    for ln in lines[6:1232]:
        ln = ln.replace("\f", "")
        if not ln.strip() or "Singapore Statutes Online" in ln or "PDF created" in ln:
            continue
        m = re.match(r"^\s*(\d+[A-Z]*)\s+(\S.*)$", ln)
        if m:
            last = m.group(1)
            toc[last] = m.group(2).strip()
        elif last and not ln.strip().isupper() and not ln.strip().startswith(("CHAPTER", "Section")):
            toc[last] += " " + ln.strip()
    body = [asciify(l) for l in lines[4838:6514]
            if "Singapore Statutes Online" not in l and "PDF created date" not in l]
    starts = []
    for i, l in enumerate(body):
        m = re.match(r"^\s*(\d+[A-Z]*)\.(\s|-|—)", l)
        if m:
            starts.append((i, m.group(1)))
    secs = {}
    for k, (i, n) in enumerate(starts):
        j = starts[k + 1][0] if k + 1 < len(starts) else len(body)
        chunk = [re.sub(r"\s+", " ", l).strip() for l in body[i:j]]
        chunk = [c for c in chunk if c]
        # cut a trailing CHAPTER heading block
        for ci, c in enumerate(chunk):
            if c.startswith("CHAPTER"):
                chunk = chunk[:ci]
                break
        # cut the next section's heading (from the TOC) off the tail
        if k + 1 < len(starts):
            nxt = asciify(toc.get(starts[k + 1][1], ""))
            nxt_n = re.sub(r"\W+", "", nxt).lower()
            for cut in range(1, 5):
                tail = re.sub(r"\W+", "", "".join(chunk[-cut:])).lower()
                if nxt_n and tail == nxt_n:
                    chunk = chunk[:-cut]
                    break
        secs[n] = chunk
    return toc, secs


TOC, SECS = _load()


def heading(n):
    return asciify(TOC.get(n, "?"))


PARA = re.compile(r"^(\(\w+\)|Explanation|Explanations|Illustration|Illustrations|Exception|Exceptions|\[|\d+[A-Z]*\.|\"|\(\d+[A-Z]*\))")


def quote(n, width=84):
    paras = []
    for c in SECS[n]:
        if not paras or PARA.match(c):
            paras.append(c)
        else:
            paras[-1] += " " + c
    out = []
    for p in paras:
        ind = "   " if re.match(r"^\((\w+|\d+)\)", p) and not re.match(r"^\(\d+[A-Z]*\)", p) else ""
        for i, w in enumerate(textwrap.wrap(p, width - len(ind))):
            out.append("-- " + ind + ("" if i == 0 else "  " if ind else "") + w)
    return "\n".join(out)


# ---------------------------------------------------------------- punishment
KIND = {"np": "`not prescribed`", "sb": "`shall be punished with`", "or": "`or with`", "al": "`shall also be liable to`"}


def mb(x):
    return "NOTHING" if x is None else f"JUST {x}"


class Pun:
    def __init__(self, name, section, words, death="np", life="np", imp="np", maxm=None, minm=None,
                 fine="np", maxfine=None, minfine=None, caning="np", mins=None, maxs=None, both=False,
                 ref=None):
        self.__dict__.update(locals())
        del self.__dict__["self"]

    @property
    def ident(self):
        return f"`punishment prescribed by s {self.name}`"

    def l4(self):
        return f"""@ref Penal Code 1871 s {self.ref or self.section}
{self.ident} MEANS Punishment WITH
    section                  IS "{self.section}"
    words                    IS "{self.words}"
    death                    IS {KIND[self.death]}
    `imprisonment for life`  IS {KIND[self.life]}
    imprisonment             IS {KIND[self.imp]}
    `maximum term in months` IS {mb(self.maxm)}
    `minimum term in months` IS {mb(self.minm)}
    `forfeiture of property` IS `not prescribed`
    fine                     IS {KIND[self.fine]}
    `maximum fine`           IS {mb(self.maxfine)}
    `minimum fine`           IS {mb(self.minfine)}
    caning                   IS {KIND[self.caning]}
    `minimum strokes`        IS {mb(self.mins)}
    `maximum strokes`        IS {mb(self.maxs)}
    `or with both`           IS {"TRUE" if self.both else "FALSE"}
"""


def or_both(name, sec, years=None, months=None, maxfine=None, words=None):
    """'imprisonment for a term which may extend to N years, or with fine [which may extend to $X], or with both'"""
    m = months if months is not None else years * 12
    term = (f"{years} years" if years and years != 1 else "one year") if months is None else f"{months} months"
    if words is None:
        f = "fine" if maxfine is None else f"fine which may extend to ${maxfine:,}"
        words = f"imprisonment for a term which may extend to {term}, or with {f}, or with both"
    return Pun(name, sec, words, imp="or", maxm=m, fine="or", maxfine=maxfine, both=True)


def and_fine(name, sec, years, words=None):
    """'imprisonment for a term which may extend to N years, and shall also be liable to fine'"""
    if words is None:
        words = f"imprisonment for a term which may extend to {years} years, and shall also be liable to fine"
    return Pun(name, sec, words, imp="sb", maxm=years * 12, fine="al")


# ---------------------------------------------------------------- facts
FACTS = {}


class Facts:
    """A facts record. fields: list of (name, 'B'|'S', desc). Names are L4 identifiers WITHOUT backticks."""

    def __init__(self, name, about, fields, ref, comment=""):
        self.name, self.about, self.fields, self.ref, self.comment = name, about, fields, ref, comment
        FACTS[name] = self
        names = [f[0] for f in fields]
        assert len(names) == len(set(names)), (name, [x for x in names if names.count(x) > 1])

    @property
    def ident(self):
        return f"`{self.name}`"

    def l4(self):
        w = max(len(f[0]) for f in self.fields) + 2
        w = min(w, 40)
        out = []
        if self.comment:
            out.append("\n".join("-- " + l for l in textwrap.wrap(self.comment, 84)))
        out.append(f"@ref {self.ref}")
        out.append(f"DECLARE {self.ident} HAS")
        out.append(f"    {'particulars':<{w}} IS A Particulars @desc Who is charged, and when and where the offence was committed")
        for n, t, d in self.fields:
            ty = "BOOLEAN" if t == "B" else "STRING"
            nm = f"`{n}`"
            if len(nm) > w:
                out.append(f"    {nm}\n    {'':<{w}} IS A {ty} @desc {d}")
            else:
                out.append(f"    {nm:<{w}} IS A {ty} @desc {d}")
        return "\n".join(out) + "\n"

    def fixture(self, fname, true=(), strings=None, particulars="`the particulars`"):
        strings = strings or {}
        true = set(true)
        bad = [t for t in true if t not in {f[0] for f in self.fields}]
        assert not bad, (self.name, fname, bad)
        bad = [t for t in strings if t not in {f[0] for f in self.fields}]
        assert not bad, (self.name, fname, bad)
        out = [f"`{fname}` MEANS {self.ident} WITH", f"    particulars IS {particulars}"]
        for n, t, _ in self.fields:
            if t == "B":
                out.append(f"    `{n}` IS {'TRUE' if n in true else 'FALSE'}")
            else:
                v = strings.get(n, "").replace('"', '\\"')
                out.append(f'    `{n}` IS "{v}"')
        return "\n".join(out) + "\n"


def pred(name, facts, export, body, ref=None, comment=None):
    """A BOOLEAN DECIDE over f."""
    out = []
    if comment:
        out.append("\n".join("-- " + l for l in textwrap.wrap(comment, 84)))
    if ref:
        out.append(f"@ref {ref}")
    out.append(f"@export {export}")
    out.append(f"GIVEN f IS A {facts.ident} @desc {facts.about}")
    out.append("GIVETH A BOOLEAN")
    out.append(f"DECIDE {name} f IF")
    out.append(textwrap.indent(textwrap.dedent(body).strip("\n"), "    "))
    return "\n".join(out) + "\n"


def charge(sec, facts, offence_name, pun_expr, recital, missing, title=None):
    """`charge under s N` f."""
    title = title or offence_name
    miss = ",\n                ".join(missing)
    return f"""@export Frame a charge under section {sec} of the Penal Code 1871 ({title}), or say why none can be framed
GIVEN f IS A {facts.ident} @desc {facts.about}, and the particulars of the charge
GIVETH A Charge
`charge under s {sec}` f MEANS
    `frame the charge` (f's particulars) "{sec}" {offence_name}
        ({pun_expr})
        (`offence under s {sec}` f)
        ({recital})
        (concat (LIST
                {miss}))
"""


def mu(expr, words):
    """`missing unless` (expr) "words" """
    return f'(`missing unless` ({expr}) "{words}")'
