# Encoding brief: National Insurance Law Schedule A1 Part D, ss 72 and 335, and ss 65 and 67A, in L4 (row IL-08)

Row IL-08, run id `IL-08-20261007`, encoder `enc-il-08` (one session, no sub-agents).
The full brief, which covers both halves of the row, is the Income Tax Ordinance half's `BRIEF.md`: `../../../income-tax-ordinance-new-version/encodings/legalese-2026-10-il-08/BRIEF.md`.
This file restates what is particular to the National Insurance Law half.

## The subject

**חוק הביטוח הלאומי [נוסח משולב], התשנ״ה–1995**, the National Insurance Law [Consolidated Version], as consolidated on Hebrew Wikisource and deposited at `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` (retrieved 2026-10-06, sha256 `78bf47ee…552a97`).
Hebrew is authoritative; the file is an unofficial consolidation stated as amended at retrieval.
Where an amending Law matters, the enacted Laws deposited under `../../registers/source-bundle/amending-laws/` take precedence.
None of the three deposited appears to touch this half: a search of their `pdftotext` text on 2026-10-07 for "335" (and "533", for the extractor's reversed digits), "לוח א'1", "סעיף 72" and "תקופת הקצבה" found nothing, and the consolidation shows no amendment of these provisions later than תשע״ח־5 (s 335) and תש״ף (Schedule A1 Part D), with none at all on s 72.

## Scope, as ruled (`l4-pipeline/BACKLOG.md`, Tier 1, row IL-08)

**The row's own list:** NII s 65, s 67A and Schedule A1 Part D.
**Added from the capstone's gap order:** NII s 72 and s 335.
s 65 is encoded in full by row IL-06 and is not re-encoded; s 67A does not exist in the deposited text (both are given their dispositions in `NOTES.md`).

## Deliverables, all in this directory

`.l4` modules (a nouns module, one module each for Part D, s 72 and s 335, and two tests modules), `NOTES.md`, `check.sh`, `encoding.json`, `SOURCE-LICENSE.md` and `tools/`, under the rules the Income Tax Ordinance half's brief states.

## Toolchain

`/Users/mengwong/.local/bin/l4` (no `--version`), `JL4_LIBRARY_PATH` unset; `L4=/Users/mengwong/.local/bin/l4 ./check.sh`.
