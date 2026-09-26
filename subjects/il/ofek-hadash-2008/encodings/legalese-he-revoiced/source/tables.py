"""Parse the salary and Tosefet Ofek grids out of the Ofek Hadash corpus.

The authoritative printing is the follow-up committee decision of 14 January
2025, which corrected a scribal error in the 19 October 2022 wage agreement and
reissued its appendices to the AGORA. Everything downstream reads this module,
so there is exactly one place where a number enters the encoding from a source
document.

Point this at a checkout of
    https://github.com/morimovilimcatala/ofek-hadash-corpus
via OFEK_CORPUS, or pass the path as argv[1].
"""
import html
import os
import re
import sys

CORRECTION = ('agreements/ofek-hadash/'
              '2025-01-14_ofek-hadash_vaadat-maakev_taut-sofer-correction_'
              'agorot-salary-tables.html')
SHEKEL_BA = 'tables/2022-09-01_ofek-hadash_salary-table_BA.html'


def corpus_root(argv=None):
    if argv and len(argv) > 1:
        return argv[1]
    root = os.environ.get('OFEK_CORPUS')
    if not root:
        sys.exit('set OFEK_CORPUS to a checkout of the ofek-hadash-corpus repository')
    return root


def _text(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s))).strip()


def cells(rowhtml):
    """(text, colspan) for each cell of one <tr>, in document order."""
    out = []
    for m in re.finditer(r'<t([hd])([^>]*)>([\s\S]*?)</t\1>', rowhtml):
        attrs, inner = m.group(2), m.group(3)
        span = 1
        cs = re.search(r'colspan="(\d+)"', attrs)
        if cs:
            span = int(cs.group(1))
        out.append((_text(inner), span))
    return out


def _rows(tbl):
    return re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', tbl)


def grid(tbl):
    """A salary grid, three ways.

    full      (seniority, rank) -> amount for all 9 ranks, the last defined
              value carried into the ranks beyond it (which is how the shekel
              printing renders them, as merged cells)
    frontier  seniority -> how many ranks the table actually separates there
    margins   seniority -> the step percentage printed in the left margin,
              where the printing carries one
    """
    full, frontier, margins = {}, {}, {}
    for r in _rows(tbl):
        cs = cells(r)
        first = cs[0][0] if cs else ''
        if not re.fullmatch(r'\d+', first):
            continue
        v = int(first)
        col, defined, last = 1, 0, None
        for txt, span in cs[1:]:
            if txt.endswith('%'):
                margins[v] = float(txt.rstrip('% ')) / 100
                continue
            if txt == '':
                continue
            if re.fullmatch(r'[\d,]+(\.\d+)?', txt):
                val = float(txt.replace(',', ''))
                last = val
                defined += 1
                for k in range(span):
                    full[(v, col + k)] = val
                col += span
        for d in range(col, 10):
            full[(v, d)] = last
        frontier[v] = defined
    return full, frontier, margins


def row_of_amounts(tbl):
    """The single data row of a Tosefet Ofek appendix: rank 1..9."""
    for r in _rows(tbl):
        cs = [c for c, _ in cells(r)]
        vals = [c for c in cs if re.fullmatch(r'[\d,]+\.\d+', c)]
        if len(vals) == 9:
            return [float(v.replace(',', '')) for v in vals]
    raise LookupError('no nine-amount row in this table')


def load(root):
    """Every grid this encoding reads, from the corrected 14.1.2025 printing."""
    h = open(os.path.join(root, CORRECTION), encoding='utf8').read()
    t = re.findall(r'<table>([\s\S]*?)</table>', h)
    if len(t) != 6:
        raise LookupError(f'expected 6 appendix tables in the correction, found {len(t)}')
    ba, front_ba, _ = grid(t[0])
    ma, front_ma, _ = grid(t[1])
    if front_ba != front_ma:
        raise LookupError('the BA and MA grids disagree about which ranks they separate')
    return {
        'BA': ba, 'MA': ma, 'frontier': front_ba,
        # appendix bet = from 1.9.2022; gimel = from 1.9.2023 (the correction
        # fixes the date the 2022 agreement misprinted as 1.1.23)
        'tosefet': {('BA', 2022): row_of_amounts(t[2]), ('BA', 2023): row_of_amounts(t[3]),
                    ('MA', 2022): row_of_amounts(t[4]), ('MA', 2023): row_of_amounts(t[5])},
    }


def margins_from_shekel_printing(root):
    """The step percentages, which only the shekel printing carries."""
    h = open(os.path.join(root, SHEKEL_BA), encoding='utf8').read()
    tbl = re.findall(r'<table>([\s\S]*?)</table>', h)[0]
    _, _, margins = grid(tbl)
    rank_step = None
    for r in _rows(tbl):
        for txt, _span in cells(r):
            if txt.endswith('%') and rank_step is None:
                rank_step = float(txt.rstrip('% ')) / 100
        if rank_step is not None:
            break
    return margins, rank_step


def l4num(x):
    """A number as L4 writes it: _ for thousands, no trailing .00."""
    s = f'{x:,.2f}'.replace(',', '_')
    return s[:-3] if s.endswith('.00') else s
