"""Turn first_schedule_rows.json (first_schedule_extract.py) into cpc-first-schedule.l4.

Every printed cell in columns 3, 4, 5 and 7 is mapped to one of a few controlled phrases; a phrase the script does not know is an
error, so a changed or misread cell cannot slip through as a wrong constructor.  The printed text of a cell that is not a fixed
answer ("According as to whether ...", "The court by which ... is triable") is kept in the row's derivation note.

Three printed rows hold more than one row of the table because the PDF has no ruled lines between them:
  * s 512(2) and the four rows under the heading "Offences against laws other than the Penal Code 1871" that follow it;
These are split here, by hand, from the printed text.  The four other-law rows get the section "Other written law".

Usage: python first_schedule_l4.py first_schedule_rows.json ../cpc-first-schedule.l4
"""
import json, re, sys

ARREST = {
    'May arrest without warrant': 'May arrest without warrant',
    'May not arrest without warrant': 'May not arrest without warrant',
}
PROCESS = {'Warrant': 'A warrant ordinarily issues', 'Summons': 'A summons ordinarily issues'}
BAIL = {'Bailable': 'Bailable', 'Not bailable': 'Not bailable'}
COURT = {"Magistrate's Court or District Court": "Magistrate's Court or District Court",
         'District Court': 'District Court',
         '': 'General Division of the High Court only'}
UNDER = 'As for the underlying offence'

def arrest_of(t):
    if t in ARREST: return ARREST[t], ''
    if t.startswith('According as to whether') or t.startswith('May arrest without warrant, if arrest for the offence') or t.startswith('May arrest without warrant if arrest for the offence'):
        return UNDER, t
    raise SystemExit('unknown arrest cell: ' + t)

def process_of(t):
    if t in PROCESS: return PROCESS[t], ''
    if t.startswith('According as to whether') : return UNDER, t
    if t == 'According to the offence committed by the person hired, engaged or employed':
        return 'As for the offence committed by the person hired, engaged or employed', t
    raise SystemExit('unknown process cell: ' + t)

def bail_of(t):
    if t in BAIL: return BAIL[t], ''
    if t.startswith('According as to whether'): return UNDER, t
    raise SystemExit('unknown bail cell: ' + t)

def court_of(t):
    if t in COURT: return COURT[t], ''
    if t.startswith('The court by which'): return UNDER, t
    raise SystemExit('unknown court cell: ' + t)

def chapter_of(s):
    s = re.sub(r'^(CHAPTER \w+)\s*[^\w\s]+\s*', r'\1 -- ', s)
    return s.replace('�', '--')

def q(s):
    assert '"' not in s and '\\' not in s, s
    return '"%s"' % s

def base_of(sec):
    m = re.match(r'^(\d+[A-Z]{0,3})', sec)
    return m.group(1) if m else ''

def main(src, out):
    rows = json.load(open(src, encoding='utf-8'))
    # split the final merged row: s 512(2) and the four rows of the "other written laws" band
    last = rows[-1]
    assert last['cells'][0] == '512(2)', last['cells'][0]
    last['cells'] = ['512(2)',
        'If the attempted offence is punishable with any punishment or combination of punishments other than death or imprisonment for life',
        'According as to whether the offence is one in respect of which the police may arrest without warrant or not',
        'According as to whether the offence is one in respect of which a summons or warrant shall ordinarily issue',
        'According as to whether the offence attempted is bailable or not',
        'The punishment provided for the offence, except that the court is not bound to impose any specified minimum sentence or mandatory minimum sentence of imprisonment, or fine or caning',
        'The court by which the offence attempted is triable']
    other = [
        ('If punishable with death, imprisonment for 7 years or upwards', 'May arrest without warrant', 'A warrant ordinarily issues', 'Not bailable'),
        ('If punishable with imprisonment for 3 years or upwards but less than 7 years', 'May arrest without warrant', 'A warrant ordinarily issues', 'Not bailable'),
        ('If punishable with imprisonment for less than 3 years', 'May not arrest without warrant unless specifically empowered by the law offended against', 'A summons ordinarily issues', 'Bailable'),
        ('If punishable with fine only', 'May not arrest without warrant unless specifically empowered by the law offended against', 'A summons ordinarily issues', 'Bailable'),
    ]
    lines = []
    n_std = n_der = 0
    for r in rows:
        c = r['cells']
        a, an = arrest_of(c[2]); p, pn = process_of(c[3]); b, bn = bail_of(c[4]); k, kn = court_of(c[6])
        notes = []
        for label, txt in (('arrest', an), ('process', pn), ('bail', bn), ('court', kn)):
            if txt: notes.append('%s: %s' % (label, txt))
        if notes: n_der += 1
        else: n_std += 1
        pages = r['pages'][0]
        lines.append((c[0], base_of(c[0]), c[1], a, p, b, c[5], k, chapter_of(r['chapter']) + (' / ' + r['sub'] if r['sub'] else ''), ' | '.join(notes), pages))
    chap_other = 'OFFENCES AGAINST LAWS OTHER THAN THE PENAL CODE 1871'
    for off, a, p, b in other:
        lines.append(('Other written law', '', off, a, p, b, '', 'According to sections 7, 8 and 9', chap_other, '', 454))
    # emit
    o = []
    o.append('''IMPORT prelude
IMPORT `cpc-types`

-- Criminal Procedure Code 2010, First Schedule: "Tabular statement of offences under the Penal Code 1871",
-- Singapore Statutes Online, current version as at 01 Oct 2026 (pages 385 to 454 of source/CPC2010.pdf).
-- GENERATED by generators/first_schedule_extract.py and generators/first_schedule_l4.py from the PDF: do not edit by hand.
--
-- The seven printed columns, and where each lands:
--   1 Penal Code 1871 section            -> `printed section` (and `base section`, the section without its subsection)
--   2 Offence                            -> `offence description`
--   3 Whether the police may ordinarily
--     arrest without warrant or not      -> `arrest rule`
--   4 Whether a warrant or a summons
--     shall ordinarily issue             -> `process rule`
--   5 Whether bailable of right or not   -> `bail rule`
--   6 Maximum punishment under the
--     Penal Code 1871                    -> `maximum punishment`, as printed
--   7 By what court triable besides the
--     General Division of High Court     -> `court rule`
-- plus `chapter heading` (the chapter and sub-heading the row sits under), `derivation note` (the printed words of a cell that is
-- not a fixed answer but says "as for the offence abetted, attempted or the subject of the row"; empty for the others) and
-- `page of the SSO PDF` (the page the row starts on).
--
-- Explanatory Notes printed above the table: (1) the entries in the second and sixth columns "are not intended as definitions of
-- the offences and punishments described in the several corresponding sections of the Penal Code 1871, or even as abstracts of
-- those sections, but merely as references to the subject of the section"; in the case of many offences punishable by fine the
-- maximum fine is limited by the Penal Code 1871 and such offences are marked * in the sixth column.  (2) "The entries in the
-- third column of this Schedule are not intended in any way to restrict the powers of arrest without warrant which may be lawfully
-- exercised by police officers."  The offence elements are taken from the Penal Code, not from this table.
--
-- %d rows from the table as printed (%d with every cell a fixed answer, %d where a cell is derived from the offence the row is
-- ancillary to), and 4 rows from the band "Offences against laws other than the Penal Code 1871" printed after s 512(2).

§ `The rows of the First Schedule`

-- section    offence    arrest   process   bail   maximum punishment   court   chapter   derivation note   page
@ref "Criminal Procedure Code 2010, First Schedule"
`the rows of the First Schedule` MEANS
    LIST
''' % (len(rows), n_std, n_der))
    for i, ln in enumerate(lines):
        sec, base, off, a, p, b, pun, k, chap, der, pg = ln
        lead = '        ' if i == 0 else '      , '
        o.append('%s(`First Schedule Row` OF %s, %s, %s, `%s`, `%s`, `%s`, %s, `%s`, %s, %s, %d)\n' % (lead, q(sec), q(base), q(off), a, p, b, q(pun), k, q(chap), q(der), pg))
    open(out, 'w', encoding='utf-8', newline='\n').write(''.join(o))
    print(len(lines), 'rows written;', n_std, 'standard,', n_der, 'derived')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
