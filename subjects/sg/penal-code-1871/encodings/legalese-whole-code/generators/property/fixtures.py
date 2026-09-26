#!/usr/bin/env python3
"""PROPERTY GROUP ONLY. Expand fixture blocks in property/tests.l4.in into
deposit/pc-property-tests.l4.

  @@FIX `name` : Type [< `base`]
  leaf-name-or-unique-prefix          -> TRUE
  -leaf-name-or-prefix                -> back to its default (unset from base)
  =field-or-prefix => L4 expression   -> that expression
  @@END

Defaults: BOOLEAN FALSE, STRING "", Pronoun he, Particulars `the particulars`,
a nested facts record `nothing established - <Type>` (emitted once per type).
Every field of the record is written out, so a fixture is a complete literal.
"""
import re, sys, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
DEP = '/Users/mengwong/src/legalese/pc-encode/deposit'

def parse_records():
    recs = {}
    for p in sorted(glob.glob(os.path.join(DEP, 'pc-property-*.l4'))):
        if p.endswith('-tests.l4'):
            continue
        L = open(p).read().split('\n')
        i = 0
        while i < len(L):
            m = re.match(r'^DECLARE `([^`]+)` HAS\s*$', L[i])
            if not m:
                i += 1; continue
            name = m.group(1); fields = []; i += 1
            while i < len(L) and (L[i].startswith('    ') or L[i].strip() == '' or L[i].strip().startswith('--')):
                l = L[i]
                fm = re.match(r'^    (`[^`]+`|[A-Za-z]\w*)\s*(IS AN? (.+?))?\s*(@desc.*)?$', l)
                if fm and not l.startswith('     ') and not l.strip().startswith('--'):
                    fname = fm.group(1).strip('`')
                    ftype = fm.group(3)
                    if ftype is None:
                        tm = re.match(r'^\s+IS AN? (.+?)\s*(@desc.*)?$', L[i + 1])
                        ftype = tm.group(1); i += 1
                    fields.append((fname, ftype.strip().strip('`')))
                i += 1
            recs[name] = fields
    return recs

R = parse_records()

def default(t):
    if t == 'BOOLEAN': return 'FALSE'
    if t == 'STRING': return '""'
    if t == 'Pronoun': return 'he'
    if t == 'Particulars': return '`the particulars`'
    if t in R: return f'`nothing established - {t}`'
    sys.exit('no default for type ' + t)

def q(n):
    return n if re.fullmatch(r'[a-z]\w*', n) and n not in ('do',) else f'`{n}`'

def match(t, pre):
    names = [f for f, _ in R[t]]
    c = [f for f in names if f == pre] or [f for f in names if f.startswith(pre)]
    if len(c) != 1:
        sys.exit(f'field prefix {pre!r} for {t}: {len(c)} matches: {c[:5]}')
    return c[0]

fix = {}
out = []
nones = set()
def emit(name, t, vals):
    out.append(f'{name} MEANS `{t}` WITH')
    w = max(len(q(f)) for f, _ in R[t])
    for f, ft in R[t]:
        out.append(f'    {q(f).ljust(w)} IS {vals.get(f, default(ft))}')
    out.append('')

def need_none(t):
    for f, ft in R[t]:
        if ft in R and ft not in nones:
            need_none(ft)
    if t not in nones:
        nones.add(t)
        emit(f'`nothing established - {t}`', t, {})

L = open(os.path.join(HERE, 'tests.l4.in')).read().split('\n')
i = 0
while i < len(L):
    l = L[i]
    m = re.match(r'^@@NONES (.+)$', l)
    if m:
        for t in m.group(1).split(','):
            need_none(t.strip())
        i += 1; continue
    m = re.match(r'^@@FIX (`[^`]+`) : (.+?)(?: < (`[^`]+`))?\s*$', l)
    if m:
        name, t, base = m.group(1), m.group(2).strip().strip('`'), m.group(3)
        if t not in R: sys.exit('unknown record ' + t)
        vals = dict(fix[base][1]) if base else {}
        if base and fix[base][0] != t: sys.exit('base type mismatch ' + name)
        i += 1
        while L[i] != '@@END':
            s = L[i].strip()
            if s.startswith('-'):
                vals.pop(match(t, s[1:].strip()), None)
            elif s.startswith('='):
                a, b = s[1:].split('=>', 1); vals[match(t, a.strip())] = b.strip()
            elif s and not s.startswith('--'):
                vals[match(t, s)] = 'TRUE'
            i += 1
        fix[name] = (t, vals)
        emit(name, t, vals)
        i += 1; continue
    out.append(l); i += 1

s = '\n'.join(out)
for c in s:
    if ord(c) >= 128 and c != '§':
        sys.exit(f'non-ASCII {c!r}')
open(os.path.join(DEP, 'pc-property-tests.l4'), 'w').write(s)
print('wrote pc-property-tests.l4;', len(fix), 'fixtures')
