# How a 36x9 salary table is written out as L4.
#
# Shared by build-salary-table-module.py and build-catala-module.py so that the
# two renderings of the same grid cannot drift in layout, only in surroundings.
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
# amounts. That took the line from 320 characters to 184.

SUBJ = '`the seniority`'
CTOR = '`a row of the combined salary table`'
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
    heads = ', '.join(f'rank {d}'.rjust(AMTW) for d in range(1, 10))
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
        'GIVEN `the seniority` IS A NUMBER',
        'GIVETH A `a row of the combined salary table`',
        f'`{name}` `the seniority`',
        f'    @nlg the row of the {label} table at the given seniority',
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
        subj = '`the rank`' if first else '^'.ljust(len('`the rank`'))
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
