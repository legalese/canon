"""Build L4 test fixtures from the DECLAREs in a types module.

An L4 record cannot be built with some of its fields missing and has no update form, so a test that
needs a 40-field record with two fields true has to spell out all forty.  This helper reads the
record declarations from the types module and writes each fixture in full: every BOOLEAN field FALSE
except the ones the case names, and every enum field at an explicit value.

Fields are named in a case by a unique substring of the field name, so a case reads like the source and
a typo or an ambiguous fragment is an error and not a silently different fixture.

Usage (see ea_tests.py): from fixtures import Types, Out
"""
import re, sys

class Types:
    errors = []
    def __init__(self, *paths):
        self.records = {}   # name -> [(field, type)]
        self.enums = {}     # name -> [constructors]
        txt = '\n'.join(open(p, encoding='utf-8').read().replace('\r\n', '\n') for p in paths)
        lines = txt.split('\n')
        i = 0
        while i < len(lines):
            m = re.match(r'DECLARE `([^`]+)` HAS\s*$', lines[i])
            if m:
                name = m.group(1); fields = []; i += 1
                while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                    fm = re.match(r'\s{4}`([^`]+)` IS (?:A|AN) (`[^`]+`|\w+)\s*$', lines[i])
                    if fm:
                        fields.append((fm.group(1), fm.group(2).strip('`')))
                    i += 1
                self.records[name] = fields
                continue
            m = re.match(r'DECLARE `([^`]+)` IS ONE OF\s*$', lines[i])
            if m:
                name = m.group(1); cons = []; i += 1
                while i < len(lines) and lines[i].startswith('    '):
                    cm = re.match(r'\s{4}(`[^`]+`|\w+)\s*$', lines[i])
                    if cm:
                        cons.append(cm.group(1).strip('`'))
                    i += 1
                self.enums[name] = cons
                continue
            i += 1

    def resolve(self, record, fragment):
        exact = [f for f, _ in self.records[record] if f == fragment]
        if len(exact) == 1:
            return exact[0]
        hits = [f for f, _ in self.records[record] if fragment in f]
        if len(hits) != 1:
            Types.errors.append(f"{record}: fragment {fragment!r} matches {len(hits)} fields" + (": " + " | ".join(h[:70] for h in hits) if hits else ""))
            return fragment
        return hits[0]

    def fixture(self, var, record, true=(), values=None):
        values = values or {}
        chosen = {self.resolve(record, t) for t in true}
        vals = {self.resolve(record, k): v for k, v in values.items()}
        out = ['`%s` MEANS `%s` WITH' % (var, record)]
        for f, t in self.records[record]:
            if t == 'BOOLEAN':
                v = 'TRUE' if f in chosen else 'FALSE'
            elif t == 'STRING':
                v = '"%s"' % vals.get(f, '')
            elif t == 'NUMBER':
                v = str(vals.get(f, 0))
            elif t in self.enums:
                v = '`%s`' % vals.get(f, self.enums[t][-1])
            elif t in self.records:
                v = '`%s`' % vals[f]
            else:
                raise SystemExit(f"unsupported field type {t} in {record}.{f}")
            if f in vals and t == 'BOOLEAN':
                raise SystemExit(f"{f} is BOOLEAN; name it in true=[...]")
            out.append('    `%s` IS %s' % (f, v))
        return '\n'.join(out)

class Out:
    def __init__(self, types, header):
        self.t = types; self.parts = [header.rstrip('\n') + '\n']
    def note(self, text):
        self.parts.append(''.join('-- %s\n' % l for l in text.split('\n')))
    def section(self, title, level=1):
        self.parts.append('%s `%s`\n' % ('§' * level, title))
    def case(self, var, record, *true, **values):
        vals = {k.replace('__', ' '): v for k, v in values.items()}
        self.parts.append(self.t.fixture(var, record, true, vals) + '\n')
    def raw(self, text):
        self.parts.append(text.rstrip('\n') + '\n')
    def assert_(self, expr):
        self.parts.append('#ASSERT ' + expr + '\n')
    def refused(self, expr, because=None):
        self.parts.append('#ASSERT REFUSED ' + expr + ('\nBECAUSE "%s"' % because if because else '') + '\n')
    def write(self, path):
        if Types.errors:
            print(chr(10).join(sorted(set(Types.errors))))
            raise SystemExit(f"{len(set(Types.errors))} bad fragment(s); nothing written")
        open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(self.parts))
