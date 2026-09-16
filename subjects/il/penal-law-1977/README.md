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
(`ח:קטע3`), 666 sections (`ח:סעיף`, lettered insertions such as 34כד counted). Every section
carries its amendment history in brackets. Amendments run to No. 155 (in force from the gazette
of 30 June 2026, on the page a week later).

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
