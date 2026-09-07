"""Wrap the very long lines `l4 catala` emits, without changing a token.

A 36-arm BRANCH lowers to a right-nested `if … then … else (if … )` chain, and
the emitter puts the whole chain on one line. For the two salary tables that is
9,771 characters — a line no reviewer will read, and one that defeats every
diff, blame and side-by-side view a reader might bring to it.

Catala is not layout-sensitive inside a code block, so a newline is just
whitespace: breaking the chain before each `else (if (` puts ONE SENIORITY ROW
on each line and changes nothing the parser sees. The claim that it changes
nothing is not taken on trust — source/run-catala.sh typechecks the wrapped
file and re-runs all six worked cases against it.

Indentation is constant rather than nested. The chain is 36 deep; indenting by
depth would put the last row 144 columns to the right and undo the point of
wrapping.

    python3 source/wrap-catala.py catala/ofek_hadash.catala_en
"""
import re
import sys

# Only wrap what is actually unreadable. A few hundred characters is a long
# line; ten thousand is a different kind of object.
THRESHOLD = 400
SPLIT = ' else (if ('
INDENT = ' ' * 4


def wrap(text):
    out = []
    for line in text.split('\n'):
        if len(line) <= THRESHOLD or SPLIT not in line:
            out.append(line)
            continue
        lead = re.match(r'[ \t]*', line).group(0)
        parts = line.split(SPLIT)
        out.append(parts[0])
        for p in parts[1:]:
            out.append(f'{lead}{INDENT}else (if ({p}')
    return '\n'.join(out)


if __name__ == '__main__':
    path = sys.argv[1]
    before = open(path, encoding='utf8').read()
    after = wrap(before)
    # A wrap that changed anything but whitespace would be a bug, not a wrap.
    if before.split() != after.split():
        sys.exit('refusing to write: wrapping changed the token stream')
    open(path, 'w', encoding='utf8').write(after)
    widest_before = max(len(x) for x in before.split('\n'))
    widest_after = max(len(x) for x in after.split('\n'))
    print(f'   longest line {widest_before} -> {widest_after} characters')
