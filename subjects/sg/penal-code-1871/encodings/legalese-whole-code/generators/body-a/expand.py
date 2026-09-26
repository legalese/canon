#!/usr/bin/env python3
"""Expand %%PUNISH and %%FIXTURE blocks in an L4 template into full literals.

%%PUNISH <sec> | <words> | death | life | imp | max | min | forf | fine | maxfine | minfine | caning | minstr | maxstr | both
  kinds: - (not prescribed), S (shall be punished with), O (or with), L (shall also be liable to)
  numbers: blank -> NOTHING

%%FIXTURE <name>
type: <Record>
<field>: <string value>          (STRING fields; quoted for you)
particulars: <raw L4 expr>
true: <field>                     (BOOLEAN fields set TRUE; all others FALSE)
%%END

Every field name is checked against the DECLARE blocks in the files named on
the command line (and the template itself). An unknown field is an error.
"""
import re, sys

KIND = {'-': '`not prescribed`', 'S': '`shall be punished with`', 'O': '`or with`', 'L': '`shall also be liable to`'}

def decls(text):
    out = {}
    cur = None
    for line in text.splitlines():
        m = re.match(r'^DECLARE (`[^`]+`|\w+) HAS\s*$', line)
        if m:
            cur = m.group(1).strip('`'); out[cur] = {}; continue
        if cur is None: continue
        if line.strip() == '' or line.strip().startswith('--'):
            continue
        m = re.match(r'^    (`[^`]+`|\w+)\s+IS AN? (`[^`]+`|\w+)', line)
        if m:
            out[cur][m.group(1).strip('`')] = m.group(2).strip('`'); continue
        if not line.startswith(' '):
            cur = None
    return out

def q(name):
    return name if re.fullmatch(r'[a-z]\w*', name) and ' ' not in name else '`' + name + '`'

def lstr(s):
    return '"' + s.replace('"', '\\"') + '"'

def punish(spec):
    p = [x.strip() for x in spec.split('|')]
    assert len(p) == 15, (len(p), spec)
    sec, words, death, life, imp, mx, mn, forf, fine, mxf, mnf, can, mns, mxs, both = p
    num = lambda v: 'NOTHING' if v == '' else 'JUST ' + v
    lines = [
        f'@ref Penal Code 1871 s {sec}',
        f'`punishment prescribed by s {sec}` MEANS Punishment WITH',
        f'    section                  IS {lstr(sec.split(",")[0])}',
        f'    words                    IS {lstr(words)}',
        f'    death                    IS {KIND[death]}',
        f'    `imprisonment for life`  IS {KIND[life]}',
        f'    imprisonment             IS {KIND[imp]}',
        f'    `maximum term in months` IS {num(mx)}',
        f'    `minimum term in months` IS {num(mn)}',
        f'    `forfeiture of property` IS {KIND[forf]}',
        f'    fine                     IS {KIND[fine]}',
        f'    `maximum fine`           IS {num(mxf)}',
        f'    `minimum fine`           IS {num(mnf)}',
        f'    caning                   IS {KIND[can]}',
        f'    `minimum strokes`        IS {num(mns)}',
        f'    `maximum strokes`        IS {num(mxs)}',
        f'    `or with both`           IS {"TRUE" if both == "T" else "FALSE"}',
    ]
    return '\n'.join(lines)

def fixture(block, D):
    name = block[0].strip()
    fields = {}
    typ = None
    trues = []
    for l in block[1:]:
        if not l.strip() or l.strip().startswith('--'): continue
        k, _, v = l.partition(':')
        k = k.strip(); v = v.strip()
        if k == 'type': typ = v
        elif k == 'true': trues += [x.strip() for x in v.split(';') if x.strip()]
        else: fields[k] = v
    if typ not in D: sys.exit(f'fixture {name}: unknown type {typ}')
    decl = D[typ]
    for t in trues:
        if t not in decl: sys.exit(f'fixture {name}: unknown field {t!r} in {typ}')
        if decl[t] != 'BOOLEAN': sys.exit(f'fixture {name}: {t} is not BOOLEAN')
    for k in fields:
        if k not in decl: sys.exit(f'fixture {name}: unknown field {k!r} in {typ}')
    w = max(len(q(f)) for f in decl)
    out = [f'`{name}` MEANS {q(typ)} WITH']
    for f, t in decl.items():
        if f in fields:
            v = fields[f] if t != 'STRING' else lstr(fields[f])
        elif t == 'BOOLEAN': v = 'TRUE' if f in trues else 'FALSE'
        elif t == 'STRING': v = '""'
        elif t == 'Particulars': v = '`the particulars`'
        else: sys.exit(f'fixture {name}: no default for field {f} of type {t}')
        out.append(f'    {q(f).ljust(w)} IS {v}')
    return '\n'.join(out)

def main():
    tmpl, outp, *others = sys.argv[1:]
    text = open(tmpl).read()
    D = {}
    for o in others + [tmpl]:
        D.update(decls(open(o).read()))
    res = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('%%PUNISH '):
            res.append(punish(l[len('%%PUNISH '):])); i += 1; continue
        if l.startswith('%%FIXTURE '):
            blk = [l[len('%%FIXTURE '):]]
            i += 1
            while not lines[i].startswith('%%END'):
                blk.append(lines[i]); i += 1
            i += 1
            res.append(fixture(blk, D)); continue
        res.append(l); i += 1
    open(outp, 'w').write('\n'.join(res) + '\n')

main()
