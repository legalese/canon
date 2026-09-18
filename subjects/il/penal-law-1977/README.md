# Penal Law 5737-1977 — חוק העונשין, תשל״ז–1977

**Status 2026-09-16: source deposited, nothing encoded.** This row exists so that a `go` run on
the Israeli Penal Law can start from a text that is already on disk, hashed and dated, and so
that the Singapore Penal Code subject (`sg/penal-code-1871`) has a sibling to pace against.

## What is here

| file | what it is |
| --- | --- |
| `subject.json` | descriptor — citation, authority, source note, pacing note |
| `source/penal-law-1977.wikitext` | the Open Book of Laws page, raw wikitext (614 KB), revision 3023424 — **the structured form**; keep parsers on this, not on the `.txt` |
| `source/penal-law-1977.txt` | the same revision rendered to plain text (8,139 lines) — for reading, grepping and the pipeline's natural-language stages |
| `source/revision.json` | the Wikisource revision record the deposit was taken from |
| `source/SHA256SUMS` | digests of both texts |
| `source/fetch.sh` | re-fetches; with a `revid` argument, re-fetches exactly that revision |
| `source/SOURCE-LICENSE.md` | the two open source-terms questions |

## Shape of the text

Four parts (`ח:קטע1`): a preliminary part (Amendment 39 of 1994, which replaced it), Part A
general, Part B offences, and the comparison tables; 21 chapters (`ח:קטע2`), 75 sub-chapters
(`ח:קטע3`), and **651 sections in the Act proper** (`ח:סעיף`, lettered insertions such as 34כד
counted). Every section carries its amendment history in brackets. Amendments run to No. 155 (in
force from the gazette of 30 June 2026, on the page a week later).

**Counting sections — three numbers, only one of which is the sections of the Act.** Corrected
2026-09-18; the figure here previously read 666, which counts 15 things that are not sections.

| count | what it is |
| --- | --- |
| **651** | **sections of the Act** — 17 preliminary + 138 Part A + 496 Part B. Use this one. |
| 666 | the above **plus the 15 `ח:סעיף` uses inside the comparison table**, whose "numbers" are the lettered rows א…יד and whose titles are empty. They are rows of a concordance to the 1936 Ordinance, not sections. |
| 673 | the above **plus 7 uses of `ח:סעיף*`** — a *different*, starred template marking schedule items (`תוספת 2 פרט 1`…`6`). A prefix-matching regex on `{{ח:סעיף` silently swallows these. |

Measured on the deposited revision; reproduce with the snippet in "Reproducing the counts" below.
Anything that reports coverage as "N of M sections encoded" wants **651** as M.

The `ח:` template vocabulary is a de-facto schema: `ח:סעיף` section · `ח:ת` paragraph ·
`ח:תת`/`ח:תתת`/`ח:תתתת` nested subsections · `ח:פנימי` internal cross-reference (1,085 of them —
the citation graph of the Act, for free) · `ח:חיצוני` reference to another Act · `ח:תיבה`
gazette citation · `ח:הערה` editorial note.

## Where the official text is

- Original enactment: Sefer HaChukim 864, 4 August 1977, p. 226 — on `reshumot.justice.gov.il`
  (`officialGazette/statuteBook/864`), geo-blocked outside Israel; a copy is in Meng's
  `~/Dropbox/Documents/papers/israel-reshumot/`.
- Every amendment: the 264 `https://fs.knesset.gov.il/…/law/…_lsr_….pdf` links embedded in the
  wikitext, reachable from anywhere. Knesset legislation-database id **2000479**.

## Reproducing the counts

Nothing needs re-fetching; the deposited revision is the input. This prints all three numbers and
the per-part breakdown, so a disagreement says *which* number moved:

```bash
python3 - <<'EOF'
import re
L = open('source/penal-law-1977.wikitext', encoding='utf-8').read().split('\n')
starts = [i for i, l in enumerate(L) if l.startswith('{{ח:קטע1')]
names  = ['preliminary', 'Part A general', 'Part B offences', 'comparison table']
act = 0
for n, a, b in zip(names, starts, starts[1:] + [len(L)]):
    seg = '\n'.join(L[a:b])
    c = len(re.findall(r'\{\{ח:סעיף\|', seg))
    if n != 'comparison table': act += c
    print(f'{n:18} sections={c:4}  starred={len(re.findall(r"\{\{ח:סעיף\*\|", seg))}')
w = '\n'.join(L)
print(f'\nAct proper      = {act}   <- the denominator')
print(f'+ comparison tbl = {len(re.findall(r"\{\{ח:סעיף\|", w))}')
print(f'+ ח:סעיף* items  = {len(re.findall(r"\{\{ח:סעיף\*?\|", w))}')
EOF
```

Expected on revision 3023424: `651`, `666`, `673`.

**Two traps, both hit for real on 2026-09-18.** A regex of `{{ח:סעיף` without the closing `|`
is a prefix match and silently counts the starred template too. And RTL text in a terminal is
rendered in *visual* order, so eyeballing `grep` output to check a Hebrew section id is
unreliable — an earlier pass this way reported 45 duplicate section numbers that do not exist.
Work in Python and print `repr()`, which renders nothing.
