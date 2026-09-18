# How a 36x9 salary table is written out as L4 — the HEBREW copy.
#
# A copy of ../../legalese/source/_tablefmt.py with the emitted identifiers in
# Hebrew. It is a COPY rather than a shared import on purpose: the English
# original is also read by build-catala-module.py, which stays English, so
# translating the original in place would have changed that generator's output
# too.
#
# WHY A COPY IS SAFE HERE. Nothing below is hand-aligned. Every column is
# computed from len(SUBJ) and len(CTOR), so translating those two constants
# moves the whole grid — the ruler comment and every ditto caret with it.
# Hebrew identifiers are one codepoint per character and carry no combining
# marks, and L4 counts source columns in codepoints, so Python's len() is the
# same measure the lexer uses. No bidi control character (RLM, LRM) appears
# anywhere: those are a lex error inside backticks, and display order is the
# viewer's business, not the file's.
#
# THE LAYOUT, and why. A row of this table is nine amounts at one seniority.
# Everything else on the line — the guard subject, THEN, the record
# constructor, OF — is the same on all thirty-six rows, and repeating it
# thirty-six times is ink that carries no data. So:
#
#   * the record is built POSITIONALLY with `OF`, which drops nine field names
#     and nine `IS` keywords from every row. Position carries the rank, and the
#     ruler comment names the columns once, above the table.
#   * the tokens that repeat are written once on the first row and dittoed with
#     `^` after it. A caret means "the token at this column on the line above",
#     so every column is fixed-width and each caret sits exactly under what it
#     copies.
#
# What is left on a row is what actually varies: the seniority, and nine
# amounts.

SUBJ = '`הוותק`'
CTOR = '`שורה בטבלת השכר המשולב`'
RANK = '`הדרגה`'
AMTW = 9          # the widest amount in either table, 16_886.09
SENW = 2          # seniority is 1..36


def _guard(v, first, last):
    """The `IF … THEN` (or `OTHERWISE`) part, at a width that never varies."""
    subj = SUBJ if first else '^'.ljust(len(SUBJ))
    width = len(f'           IF {subj} EQUALS  {"":>{SENW}} ')
    if first:
        return f'    BRANCH IF {subj} AT MOST {v:>{SENW}} '
    if last:
        return '           OTHERWISE'.ljust(width)
    return f'           IF {subj} EQUALS  {v:>{SENW}} '


def _amount_column():
    """The column the first amount starts at — the ruler has to match it."""
    return len(_guard(1, True, False)) + len('THEN') + 1 + len(CTOR) + 1 + len('OF') + 1


def ruler():
    """Name the nine columns once, over the amounts they head."""
    heads = ', '.join(f'דרגה {d}'.rjust(AMTW) for d in range(1, 10))
    return '    --' + ' ' * (_amount_column() - 6) + heads


def rows(grid, num):
    """Every row of the table, as L4 lines. `num` formats one amount."""
    out = [ruler()]
    for v in range(1, 37):
        first, last = v == 1, v == 36
        ctor = CTOR if first else '^'.ljust(len(CTOR))
        of = 'OF' if first else '^ '
        then = '    ' if last else ('THEN' if first else '^   ')
        amounts = ', '.join(num(grid[(v, d)]).rjust(AMTW) for d in range(1, 10))
        out.append(f'{_guard(v, first, last)}{then} {ctor} {of} {amounts}')
    return out


def signature(name, label):
    """The four lines above the table proper."""
    return [
        f'GIVEN {SUBJ} IS A NUMBER',
        f'GIVETH A {CTOR}',
        f'`{name}` {SUBJ}',
        f'    @nlg שורת {label} לפי הוותק הנתון',
        '    MEANS',
    ]


def branch_over_rank(values, indent, num):
    """A nine-armed BRANCH on `the rank`, dittoed the same way.

    Used for the Tosefet Ofek 2022 appendices, which give one amount per rank.
    """
    pad = ' ' * indent
    out = []
    for i, v in enumerate(values, start=1):
        first, last = i == 1, i == 9
        subj = RANK if first else '^'.ljust(len(RANK))
        then = 'THEN' if first else '^   '
        if first:
            guard = f'{pad}BRANCH IF {subj} AT MOST 1 '
        elif last:
            guard = f'{pad}       OTHERWISE'.ljust(len(f'{pad}       IF {subj} EQUALS  1 '))
            then = '    '
        else:
            guard = f'{pad}       IF {subj} EQUALS  {i} '
        out.append(f'{guard}{then} {num(v).rjust(8)}')
    return out
