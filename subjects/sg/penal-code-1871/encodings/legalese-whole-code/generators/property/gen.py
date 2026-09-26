#!/usr/bin/env python3
"""PROPERTY GROUP ONLY. Build deposit/pc-property-*.l4 from property/src/*.l4.in.

{{TEXT:378}}  -> the section's text, verbatim from inputs/PC1871.txt (Chapter 17),
                 page footers removed, commented out, ASCII-folded.
{{P:379}}     -> the `punishment prescribed by s 379` record, from the table below.
"""
import re, sys, os, glob

SRC = '/Users/mengwong/src/legalese/pc-encode/inputs/PC1871.txt'
OUT = '/Users/mengwong/src/legalese/pc-encode/deposit'
TPL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')

lines = open(SRC, encoding='utf-8').read().split('\n')
body = lines[10212:11764]  # Chapter 17 (1-based 10213..11764)
body = [l for l in body if not re.search(r'Singapore Statutes Online|PDF created date', l)
        and not re.match(r'^\s*Penal Code 1871\s*$', l)
        and not re.match(r'^\s*\d+\s*$', l)
        and not re.match(r'^\s*2020 Ed\.\s*$', l)]

def fold(s):
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'),
                 ('—', '-'), ('–', '-'), (' ', ' ')]:
        s = s.replace(a, b)
    assert all(ord(c) < 128 for c in s), repr(s)
    return s

starts = []
for i, l in enumerate(body):
    m = re.match(r'^\s{2,4}(\d{3}[A-Z]?)\.', l)
    if m:
        starts.append((m.group(1), i))
index = {s: i for s, i in starts}

def section_text(sec):
    i = index[sec]
    nxt = [j for s, j in starts if j > i]
    end = nxt[0] if nxt else len(body)
    chunk = body[i:end]
    # strip the trailing heading of the next section: trailing lines that are
    # blank or end without sentence punctuation
    while chunk and (chunk[-1].strip() == '' or not re.search(r'[.\];:,)—-]\s*$', chunk[-1].strip())):
        chunk.pop()
    out = []
    for l in chunk:
        l = fold(l.rstrip())
        out.append(('-- ' + l.strip()) if l.strip() else '--')
    res = []
    for l in out:
        if l == '--' and res and res[-1] == '--':
            continue
        res.append(l)
    return '\n'.join(res)

N, S, O, L = '`not prescribed`', '`shall be punished with`', '`or with`', '`shall also be liable to`'
def P(words, imp=N, mx=None, mn=None, fine=N, both=False, death=N, life=N, forf=N, maxfine=None, minfine=None, caning=N, minst=None, maxst=None):
    return dict(words=words, death=death, life=life, imp=imp, mx=mx, mn=mn, forf=forf, fine=fine,
                maxfine=maxfine, minfine=minfine, caning=caning, minst=minst, maxst=maxst, both=both)

def ofb(words, months):
    return P(words, imp=O, mx=months, fine=O, both=True)

T = {
 '379':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '379A': P("imprisonment for a term which may extend to 7 years, and shall also be liable to fine", imp=S, mx=84, fine=L),
 '380':  P("imprisonment for a term which may extend to 7 years, and shall also be liable to fine", imp=S, mx=84, fine=L),
 '381':  P("imprisonment for a term which may extend to 7 years, and shall also be liable to fine", imp=S, mx=84, fine=L),
 '382':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to caning", imp=S, mx=120, caning=L),
 '384':  P("imprisonment for a term of not less than 2 years and not more than 7 years and shall also be liable to caning", imp=S, mx=84, mn=24, caning=L),
 '385':  P("imprisonment for a term of not less than 2 years and not more than 5 years and shall also be liable to caning", imp=S, mx=60, mn=24, caning=L),
 '386':  P("imprisonment for a term of not less than 2 years and not more than 10 years and with caning", imp=S, mx=120, mn=24, caning=S),
 '387':  P("imprisonment for a term of not less than 2 years and not more than 7 years and shall also be liable to caning", imp=S, mx=84, mn=24, caning=L),
 '388':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning", imp=S, mx=120, fine=L, caning=L),
 '389':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning", imp=S, mx=120, fine=L, caning=L),
 '392':  P("imprisonment for a term of not less than 2 years and not more than 10 years and shall also be punished with caning with not less than 6 strokes", imp=S, mx=120, mn=24, caning=S, minst=6),
 '392, after 7 p.m. and before 7 a.m.':
         P("imprisonment for a term of not less than 3 years and not more than 14 years and shall also be punished with caning with not less than 12 strokes", imp=S, mx=168, mn=36, caning=S, minst=12),
 '393':  P("imprisonment for a term of not less than 2 years and not more than 7 years and shall also be liable to caning", imp=S, mx=84, mn=24, caning=L),
 '394':  P("imprisonment for a term of not less than 5 years and not more than 20 years and shall also be punished with caning with not less than 12 strokes", imp=S, mx=240, mn=60, caning=S, minst=12),
 '395':  P("imprisonment for a term of not less than 5 years and not more than 20 years and shall also be punished with caning with not less than 12 strokes", imp=S, mx=240, mn=60, caning=S, minst=12),
 '396':  P("death or imprisonment for life, and if he is not sentenced to death, shall also be punished with caning with not less than 12 strokes", death=O, life=O, caning=S, minst=12),
 '397':  P("caning with not less than 12 strokes, in addition to any other punishment to which he may be liable under any other section of this Code", caning=S, minst=12),
 '399':  P("imprisonment for a term of not less than 3 years and not more than 10 years and shall also be liable to caning", imp=S, mx=120, mn=36, caning=L),
 '400':  P("imprisonment for life, or with imprisonment for a term which may extend to 10 years, and shall also be liable to caning", life=O, imp=O, mx=120, caning=L),
 '401':  P("imprisonment for a term which may extend to 7 years", imp=S, mx=84),
 '402':  P("imprisonment for a term which may extend to 7 years, and shall also be liable to caning", imp=S, mx=84, caning=L),
 '403':  ofb("imprisonment for a term which may extend to 2 years, or with fine, or with both", 24),
 '404':  P("imprisonment for a term which may extend to 3 years, and shall also be liable to fine", imp=S, mx=36, fine=L),
 '404, clerk or servant':
         P("imprisonment for a term which may extend to 3 years, and shall also be liable to fine; and if the offender at the time of such person's decease was employed by him as a clerk or servant, the imprisonment may extend to 7 years", imp=S, mx=84, fine=L),
 '406':  ofb("imprisonment for a term which may extend to 7 years, or with fine, or with both", 84),
 '407':  P("imprisonment for a term which may extend to 15 years, and shall also be liable to fine", imp=S, mx=180, fine=L),
 '408':  P("imprisonment for a term which may extend to 15 years, and shall also be liable to fine", imp=S, mx=180, fine=L),
 '409':  P("imprisonment for a term which may extend to 20 years, and shall also be liable to fine", imp=S, mx=240, fine=L),
 '411(1)': ofb("imprisonment for a term which may extend to 5 years, or with fine, or with both", 60),
 '411(2)': P("imprisonment for a term which may extend to 5 years, and shall also be liable to fine; and may be disqualified for such period as the court may order from the date of his release from imprisonment from holding or obtaining a driving licence under the Road Traffic Act 1961", imp=S, mx=60, fine=L),
 '412':  P("imprisonment for a term which may extend to 20 years, and shall also be liable to fine", imp=S, mx=240, fine=L),
 '413':  P("imprisonment for a term which may extend to 20 years, and shall also be liable to fine", imp=S, mx=240, fine=L),
 '414(1)': ofb("imprisonment for a term which may extend to 5 years, or with fine, or with both", 60),
 '414(2)': P("imprisonment for a term which may extend to 5 years, and shall also be liable to fine; and may be disqualified for such period as the court may order from the date of his release from imprisonment from holding or obtaining a driving licence under the Road Traffic Act 1961", imp=S, mx=60, fine=L),
 '416A': P("imprisonment for a term which may extend to 3 years, or with fine which may extend to $10,000, or with both", imp=O, mx=36, fine=O, maxfine=10000, both=True),
 '417':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '418':  ofb("imprisonment for a term which may extend to 5 years, or with fine, or with both", 60),
 '419':  ofb("imprisonment for a term which may extend to 5 years, or with fine, or with both", 60),
 '420(1)': P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning or to both", imp=S, mx=120, fine=L, caning=L, both=True),
 '420(2)': P("imprisonment for a term which may extend to 10 years and with caning with not less than 6 strokes, and shall also be liable to fine", imp=S, mx=120, caning=S, minst=6, fine=L),
 '420A': P("imprisonment for a term not exceeding 10 years, or to fine, or to both", imp=O, mx=120, fine=O, both=True),
 '421':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '422':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '423':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '424':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '424A': ofb("imprisonment for a term which may extend to 20 years, or with fine, or with both", 240),
 '424B': ofb("imprisonment for a term which may extend to 20 years, or with fine, or with both", 240),
 '426':  ofb("imprisonment for a term which may extend to 2 years, or with fine, or with both", 24),
 '427':  ofb("imprisonment for a term which may extend to 10 years, or with fine, or with both", 120),
 '428':  ofb("imprisonment for a term which may extend to 5 years, or with fine, or with both", 60),
 '435':  P("imprisonment for a term which may extend to 7 years, and shall also be liable to fine", imp=S, mx=84, fine=L),
 '436':  P("imprisonment for life, or with imprisonment for a term which may extend to 10 years, and shall also be liable to fine", life=O, imp=O, mx=120, fine=L),
 '437':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine", imp=S, mx=120, fine=L),
 '438':  P("imprisonment for life, or with imprisonment for a term which may extend to 10 years, and shall, if he is not sentenced to imprisonment for life, also be liable to fine", life=O, imp=O, mx=120, fine=L),
 '439':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine", imp=S, mx=120, fine=L),
 '440':  P("imprisonment for a term which may extend to 5 years, and shall also be liable to fine", imp=S, mx=60, fine=L),
 '447':  P("imprisonment for a term which may extend to 3 months, or with fine which may extend to $1,500, or with both", imp=O, mx=3, fine=O, maxfine=1500, both=True),
 '448':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
 '449':  P("imprisonment for life, or with imprisonment for a term not exceeding 15 years, and shall, if he is not sentenced to imprisonment for life, also be liable to fine", life=O, imp=O, mx=180, fine=L),
 '450':  P("imprisonment for a term not exceeding 15 years, and shall also be liable to fine", imp=S, mx=180, fine=L),
 '451':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine", imp=S, mx=120, fine=L),
 '452':  P("imprisonment for a term which may extend to 10 years, and shall also be liable to fine, or to caning", imp=S, mx=120, fine=L, caning=L),
 '453':  P("imprisonment for a term which may extend to 2 years, or with fine, or with both; and any instrument or article, mentioned in paragraph (a) or (c), found in the possession of that person shall be forfeited", imp=O, mx=24, fine=O, both=True, forf=S),
 '458A': P("caning in addition to the punishment prescribed for that offence", caning=L),
 '459':  P("imprisonment for a term of not less than 3 years and not more than 20 years and with caning", imp=S, mx=240, mn=36, caning=S),
 '460':  P("imprisonment for a term of not less than 3 years and not more than 20 years", imp=S, mx=240, mn=36),
 '461':  ofb("imprisonment for a term which may extend to 2 years, or with fine, or with both", 24),
 '462':  ofb("imprisonment for a term which may extend to 3 years, or with fine, or with both", 36),
}

def mb(x):
    return 'NOTHING' if x is None else f'JUST {x}'

def punishment(sec):
    p = T[sec]
    return f'''@ref Penal Code 1871 s {sec}
`punishment prescribed by s {sec}` MEANS Punishment WITH
    section                  IS "{sec}"
    words                    IS "{p['words']}"
    death                    IS {p['death']}
    `imprisonment for life`  IS {p['life']}
    imprisonment             IS {p['imp']}
    `maximum term in months` IS {mb(p['mx'])}
    `minimum term in months` IS {mb(p['mn'])}
    `forfeiture of property` IS {p['forf']}
    fine                     IS {p['fine']}
    `maximum fine`           IS {mb(p['maxfine'])}
    `minimum fine`           IS {mb(p['minfine'])}
    caning                   IS {p['caning']}
    `minimum strokes`        IS {mb(p['minst'])}
    `maximum strokes`        IS {mb(p['maxst'])}
    `or with both`           IS {"TRUE" if p['both'] else "FALSE"}'''

used = set()
def sub(m):
    kind, arg = m.group(1), m.group(2)
    if kind == 'TEXT':
        return section_text(arg)
    used.add(arg)
    return punishment(arg)

if __name__ == '__main__':
    for t in sorted(glob.glob(os.path.join(TPL, 'pc-property-*.l4.in'))):
        s = open(t, encoding='utf-8').read()
        s = re.sub(r'\{\{(TEXT|P):([^}]+)\}\}', sub, s)
        for c in s:
            if ord(c) >= 128 and c != '§':
                sys.exit(f'{t}: non-ASCII {c!r}')
        out = os.path.join(OUT, os.path.basename(t)[:-3])
        open(out, 'w', encoding='utf-8').write(s)
        print('wrote', out)
    missing = set(T) - used
    if missing:
        print('punishments not placed:', sorted(missing))
