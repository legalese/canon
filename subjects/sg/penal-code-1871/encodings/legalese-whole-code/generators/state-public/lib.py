"""Generator library for the state-public group's L4 (Penal Code 1871, ss 121-190).

The ladders, leaves, recitals and tests are written by hand in the part files
(part_*.py). This library only does the mechanical parts: it quotes each
section's text from inputs/PC1871.txt into comments, lays out the facts
records, the Punishment records, the charge builders and the test fixtures, so
that every one of them has the same shape.

Run:  python3 notes/state-public-gen/build.py
"""
import json
import re

SRC = "/Users/mengwong/src/legalese/pc-encode/inputs/PC1871.txt"

ASCII = {
    "’": "'", "‘": "'", "“": '"', "”": '"',
    "—": "-", "–": "-", "…": "...", " ": " ",
}


def to_ascii(s):
    for k, v in ASCII.items():
        s = s.replace(k, v)
    s.encode("ascii")  # raises if anything is left
    return s


def _load_body(start=3710, end=4839):
    lines = open(SRC, encoding="utf-8").read().split("\n")[start - 1:end - 1]
    out = []
    for ln in lines:
        if "Singapore Statutes Online" in ln or "PDF created date" in ln or "Informal Consolidation" in ln:
            continue
        if re.match(r"^\s*(\[[^\]]*\]\s*)+$", ln):
            continue
        out.append(to_ascii(ln.rstrip()))
    return out


SEC_START = re.compile(r"^\s{2,}(\d+[A-Z]*)\.(?=\s|-)")


def load_sections():
    body = _load_body()
    starts = [(i, SEC_START.match(l).group(1)) for i, l in enumerate(body) if SEC_START.match(l)]
    secs = {}
    for k, (i, num) in enumerate(starts):
        j = starts[k + 1][0] if k + 1 < len(starts) else len(body)
        block = body[i:j]
        # split into paragraphs; drop trailing headings of the next section
        paras, cur = [], []
        for l in block:
            if l.strip() == "":
                if cur:
                    paras.append(cur)
                    cur = []
            else:
                cur.append(l)
        if cur:
            paras.append(cur)

        def is_heading(p):
            last = p[-1].strip()
            if re.match(r"^CHAPTER \w+$", last) or last.isupper():
                return True
            return not re.search(r"[.;:,]$", last) or last.startswith("Piracy by law of nations")
        while paras and is_heading(paras[-1]):
            paras.pop()
        # a heading glued to the last paragraph without a blank line
        if paras and len(paras[-1]) > 1 and not re.search(r"[.;:,]$", paras[-1][-1].strip()):
            paras[-1] = paras[-1][:-1]
        if "[Repealed" in block[0]:
            paras = [[block[0]]]
        joined = []
        for p in paras:
            para = " ".join(re.sub(r"\s+", " ", l.strip()) for l in p)
            if joined and not re.search(r"[.;:-]$", joined[-1]) and not para.startswith("(") \
                    and joined[-1] not in ("Illustration", "Illustrations"):
                joined[-1] += " " + para
            else:
                joined.append(para)
        text = []
        for para in joined:
            text.append(para)
            text.append("")
        secs[num] = text[:-1] if text else text
    return secs


SECTIONS = load_sections()


def quote(num):
    """The section's text, as a comment block."""
    import textwrap
    out = []
    for l in SECTIONS[num]:
        if l == "":
            out.append("--")
        else:
            for w in textwrap.wrap(l, 76):
                out.append("--   " + w)
    return "\n".join(out)


def q(name):
    return name if re.fullmatch(r"[a-z][a-z]*", name) else f"`{name}`"


def s(text):
    return json.dumps(to_ascii(text))


def art(t):
    return "AN" if t[0].lower() in "aeiou" else "A"


FIELDS = {}

PARTICULARS = ("particulars", "Particulars", "Who is charged, and when and where the offence was committed")
TO_WIT = ("to wit", "S", "How the accused did it, as it is to read after \"to wit,\" at the end of the charge - for example \"by refusing to alight from the vehicle when directed to do so\"; leave blank if not needed")
INDIVIDUAL = ("the accused is an individual", "B", "Is the accused an individual (a human being)? Paragraph (a) of the punishment applies to an individual; paragraph (b), \"in any other case\", to a company, association or body of persons (s 11). This leaf chooses the punishment, not whether the offence is made out.")


def facts(tname, ref, fields, desc_comment=None):
    allf = [PARTICULARS] + list(fields)
    names = [f[0] for f in allf]
    assert len(names) == len(set(names)), (tname, names)
    FIELDS[tname] = allf
    out = []
    if desc_comment:
        out += ["-- " + l for l in desc_comment.split("\n")]
    out += [f"@ref {ref}", f"DECLARE `{tname}` HAS"]
    for (n, t, d) in allf:
        tt = {"B": "A BOOLEAN", "S": "A STRING", "P": "A Person"}.get(t, "A " + t)
        out.append(f"    {q(n)}")
        out.append(f"        IS {tt} @desc {to_ascii(d)}")
    return "\n".join(out)


KIND = {"np": "`not prescribed`", "sh": "`shall be punished with`", "or": "`or with`", "al": "`shall also be liable to`"}


def mb(x):
    return "NOTHING" if x is None else f"JUST {x}"


PUNISHMENTS = {}


def pun(sec, words, death="np", life="np", imp="np", mx=None, mn=None, forf="np", fine="np",
        maxfine=None, minfine=None, caning="np", minstr=None, maxstr=None, both=False, name=None):
    name = name or f"punishment prescribed by s {sec}"
    PUNISHMENTS[name] = words
    return "\n".join([
        f"@ref Penal Code 1871 s {sec}",
        f"`{name}` MEANS Punishment WITH",
        f"    section                  IS {s(sec)}",
        f"    words                    IS {s(words)}",
        f"    death                    IS {KIND[death]}",
        f"    `imprisonment for life`  IS {KIND[life]}",
        f"    imprisonment             IS {KIND[imp]}",
        f"    `maximum term in months` IS {mb(mx)}",
        f"    `minimum term in months` IS {mb(mn)}",
        f"    `forfeiture of property` IS {KIND[forf]}",
        f"    fine                     IS {KIND[fine]}",
        f"    `maximum fine`           IS {mb(maxfine)}",
        f"    `minimum fine`           IS {mb(minfine)}",
        f"    caning                   IS {KIND[caning]}",
        f"    `minimum strokes`        IS {mb(minstr)}",
        f"    `maximum strokes`        IS {mb(maxstr)}",
        f"    `or with both`           IS {'TRUE' if both else 'FALSE'}",
    ])


def pw(name):
    """The words of a punishment, as an L4 expression."""
    return f"(`{name}`)'s words"


EXPORTS = []   # (kind, name, ftype)


RULE_BODIES = {}
CHARGES = []   # (sec, offname, offfn, ftype)


def rule(name, ftype, export, body, comment=None):
    EXPORTS.append(("bool", name, ftype))
    RULE_BODIES[name] = body
    out = []
    if comment:
        out += ["-- " + l if l else "--" for l in comment.split("\n")]
    out += [
        f"@export {to_ascii(export)}",
        f"GIVEN f IS {art(ftype)} `{ftype}` @desc The facts of the case",
        "GIVETH A BOOLEAN",
        f"DECIDE {q(name)} f IF",
        body.rstrip("\n"),
    ]
    return "\n".join(out)


def charge(sec, offname, offfn, recital, missing, ftype, secexpr=None, punexpr=None, export=None):
    """missing: list of (L4 boolean expression, the Code's words for it)."""
    EXPORTS.append(("charge", f"charge under s {sec}", ftype))
    CHARGES.append((sec, offname, offfn, ftype))
    secexpr = secexpr or s(sec)
    punexpr = punexpr or pw(f"punishment prescribed by s {sec}")
    export = export or f"Frame a charge under section {sec} of the Penal Code 1871 ({offname}), or say why none can be framed"
    ms = ",\n".join(f"            (`missing unless` ({e}) {s(w)})" for e, w in missing)
    return "\n".join([
        f"@export {to_ascii(export)}",
        f"GIVEN f IS {art(ftype)} `{ftype}` @desc The facts of the case, and the particulars of the charge",
        "GIVETH A Charge",
        f"`charge under s {sec}` f MEANS",
        f"    `frame the charge` (f's particulars) {secexpr} {s(offname)}",
        f"        ({punexpr})",
        f"        ({q(offfn)} f)",
        f"        ({recital})",
        "        (concat (LIST",
        ms + "))",
    ])


def by_individual(sec_a, sec_b):
    return f"(IF f's `the accused is an individual` THEN {s(sec_a)} ELSE {s(sec_b)})"


def pun_by_individual(name_a, name_b):
    return f"IF f's `the accused is an individual` THEN {pw(name_a)} ELSE {pw(name_b)}"


# ---------------------------------------------------------------------------
# tests
# ---------------------------------------------------------------------------

def fixture(name, ftype, trues=(), strs=None, persons=None, parts="`sample particulars`", comment=None):
    strs = strs or {}
    persons = persons or {}
    fields = FIELDS[ftype]
    known = {f[0] for f in fields}
    for t in list(trues) + list(strs) + list(persons):
        assert t in known, f"{name}: no field {t!r} in {ftype}"
    out = []
    if comment:
        out += ["-- " + l for l in comment.split("\n")]
    out.append(f"`{name}` MEANS `{ftype}` WITH")
    for (n, t, d) in fields:
        if n == "particulars":
            v = parts
        elif t == "B":
            v = "TRUE" if n in trues else "FALSE"
        elif t == "S":
            v = s(strs.get(n, ""))
        elif t == "P":
            v = persons.get(n, "`nobody`")
        else:
            raise ValueError(t)
        out.append(f"    {q(n)} IS {v}")
    return "\n".join(out)


def everything_true(ftype):
    return [f[0] for f in FIELDS[ftype] if f[1] == "B"]


def pun_ab(base, a_term_words, a_months, a_fine_words, a_maxfine, b_words="fine which may extend to $10,000", b_maxfine=10000):
    """The (a) individual / (b) any other case pair that Chapter 10 uses throughout."""
    a = pun(f"{base}(a)",
            f"imprisonment for a term which may extend to {a_term_words}, or with {a_fine_words}, or with both",
            imp="or", mx=a_months, fine="or", maxfine=a_maxfine, both=True)
    b = pun(f"{base}(b)", b_words, fine="sh", maxfine=b_maxfine)
    return a + "\n\n" + b


def simple_pun(sec, term_words, months, fine_words="fine", maxfine=None, name=None):
    """'imprisonment for a term which may extend to X, or with fine [...], or with both'."""
    return pun(sec, f"imprisonment for a term which may extend to {term_words}, or with {fine_words}, or with both",
               imp="or", mx=months, fine="or", maxfine=maxfine, both=True, name=name)


def section(num, heading):
    return f"§§ `s {num} - {to_ascii(heading)}`\n\n{quote(num)}"


PS = ("public servant", "B", "Is the person concerned a public servant within section 21 of the Penal Code 1871 - for example a police officer, or an officer of the Government or of a statutory body with a duty of maintaining law and order? (Chapter 2 ladder: `public servant within section 21`.)")
PS_21_2 = ("public servant", "B", "Is the person concerned a public servant within section 21, read with section 21(2): for this section a judge as defined in the Administration of Justice (Protection) Act 2016 is NOT a public servant? (Chapter 2 ladder: `public servant within section 21, for sections 175, 178, 179, 180 and 228`.)")
THE_PS = ("the public servant", "P", "The public servant concerned, as the charge names them - for example Sergeant Lim Ah Seng, a police officer attached to Ang Mo Kio Police Division")
