"""Extract the CPC 2010 First Schedule ("Tabular statement of offences under the Penal Code 1871") from the SSO PDF.

Why not the obvious readings.  `pdftotext -layout` scrambles the table: stacked section numbers drift away from the
rows they belong to.  PyMuPDF's table finder drops whole rows (ss 113 to 118 vanish) because the table has no ruled
lines.  Word-by-word assignment lets sub-headings leak into the row above.  This script reads the PDF's text spans
with their positions and font sizes: body text is 10 pt, chapter headings, sub-headings and the title are 11 pt or 13 pt
and are kept out of the rows, 9 pt italic is the marginal amendment note and is dropped, and each span is placed in a
column by its left edge.  A new row starts at each section number in the first column, so a wrapped cell stays with
its row and no row can vanish.

The columns, from the printed heading: 1 Penal Code 1871 section; 2 Offence; 3 whether the police may ordinarily
arrest without warrant or not; 4 whether a warrant or a summons shall ordinarily issue in the first instance;
5 whether bailable of right or not; 6 maximum punishment under the Penal Code 1871; 7 by what court triable besides the
General Division of High Court.

Output: first_schedule_rows.json -- one object per printed row: the seven cells exactly as printed (whitespace
collapsed), the pages it spans, the chapter heading and the sub-heading it falls under.  Nothing is normalised here.

Usage: python first_schedule_extract.py <CPC2010.pdf> <first_schedule_rows.json>
"""
import collections, json, re, sys
import pymupdf

FIRST, LAST = 384, 454          # 0-based page indexes; the First Schedule is pages 385 to 454 of the SSO PDF as at 01 Oct 2026
EDGES = [0, 156, 276, 360, 445, 529, 630]   # printed left edges of columns 1 to 7 are 78, 158, 278, 362, 447, 531, 632; a cell's text never starts left of its edge
SEC_START = re.compile(r'^\d+[A-Z]{0,3}(?:\([0-9A-Za-z]+\))*\(?(?=\s|$)')
FOOTER_Y = 545

def col_of(x0):
    c = 0
    for i, e in enumerate(EDGES):
        if x0 >= e:
            c = i
    return c

def norm(s):
    s = s.replace('’', "'").replace('�', "'")
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'\(\s+', '(', re.sub(r'\s+\)', ')', s))

def words_of(page):
    """Split every span into words using the position of each character, so that a span that runs across
    two columns is still read as two cells."""
    out = []
    for b in page.get_text('rawdict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                word, x0 = '', None
                for ch in sp['chars']:
                    if ch['c'] == ' ':
                        if word:
                            out.append((x0, sp['bbox'][1], word, sp['size'], sp['flags']))
                        word, x0 = '', None
                    else:
                        if x0 is None:
                            x0 = ch['bbox'][0]
                        word += ch['c']
                if word:
                    out.append((x0, sp['bbox'][1], word, sp['size'], sp['flags']))
    return out

def main(pdf, out):
    d = pymupdf.open(pdf)
    rows, cur, cur_band = [], None, None
    chapter, sub = '', ''
    heading_open, sub_open = False, False
    started = False
    for pi in range(FIRST, LAST):
        toks = [t for t in words_of(d[pi]) if t[1] < FOOTER_Y]
        # Body text is 10 pt, but rows added by amendment are set in 11 pt, so size does not tell a heading from a row:
        # headings are found by their text (CHAPTER..., capitals) and sub-headings by being centred italic lines.
        # Only the 9 pt marginal notes are dropped on size.
        bands = {}
        for t in toks:
            bands.setdefault(round(t[1] / 4), []).append(t)
        for band in sorted(bands):
            ws = sorted(bands[band], key=lambda t: t[0])
            text = norm(' '.join(t[2] for t in ws))
            if all(t[3] < 9.5 for t in ws):
                continue                                   # footer or marginal amendment note (9 pt)
            if text.startswith('CHAPTER') or text.startswith('OFFENCES AGAINST LAWS OTHER THAN'):
                chapter, sub = text, ''
                heading_open, sub_open = True, False
                continue                                   # chapter heading, set in 10 pt
            if all(t[4] == 6 and t[3] > 9.5 and t[0] > 150 for t in ws) and not text.startswith('['):
                sub = (sub + ' ' + text) if sub_open else text   # centred italic line alone on its band: a sub-heading
                sub_open = True
                continue
            if heading_open and text.isupper() and ws[0][0] > 150:
                chapter = chapter + ' ' + text             # the second line of a wrapped chapter heading
                continue
            sub_open = False
            heading_open = False
            if not started:
                first = ws[0]
                if col_of(first[0]) == 0 and SEC_START.match(norm(first[2])) and norm(first[2]) != '1':
                    started = True                         # skip the explanatory notes and the column titles
                else:
                    continue
            # a cell's words on this band, in column order
            cells = {}
            for t in ws:
                cells.setdefault(col_of(t[0]), []).append(t[2])
            for c in sorted(cells):
                t = norm(' '.join(cells[c]))
                if c == 0 and SEC_START.match(t) and (cur is None or band != cur_band or not cur['cells'][0]):
                    cur = {'cells': [''] * 7, 'pages': [pi + 1], 'chapter': chapter, 'sub': sub}
                    cur['cells'][0] = t
                    cur_band = band
                    rows.append(cur)
                    continue
                if cur is None:
                    continue
                cur['cells'][c] = (cur['cells'][c] + ' ' + t).strip()
                if (pi + 1) not in cur['pages']:
                    cur['pages'].append(pi + 1)
    for r in rows:
        r['cells'] = [norm(c) for c in r['cells']]
    json.dump(rows, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(rows), 'printed rows')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
