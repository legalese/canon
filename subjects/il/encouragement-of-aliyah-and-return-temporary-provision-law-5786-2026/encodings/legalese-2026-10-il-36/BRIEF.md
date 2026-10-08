# Encoding brief: the Encouragement of Aliyah and Return (Temporary Provision) Law, 5786-2026, in L4

Row IL-36, run id `IL-36-20261008`, encoder `enc-il-36` (one session, no sub-agents).
This brief is the whole specification.
It restates the lead's task in the template of `l4-ide/skills/encoding-a-subject/assets/brief-template.md`, with the scope pinned from the text before any L4 was written.
Where the encoding later settled something the text leaves open, NOTES.md records it as a fork or an assumption; this brief does not.

## The subject

**חוק עידוד עלייה לישראל וחזרה אליה (הוראת שעה), התשפ״ו–2026** — the Encouragement of Aliyah and Return (Temporary Provision) Law, 5786-2026.
It is not a free-standing Act.
It is chapter D, enacted by section 9, of the Economic Efficiency Law (Legislative Amendments for Achieving the Budget Targets for Budget Year 2026), 5786-2026, Sefer HaChukim 3511 (31 March 2026), pp. 416-418.
Its six sections exempt from income tax, for tax years 2026 to 2030 and up to a ceiling per year, the income from personal exertion produced in Israel of an immigrant ("עולה") who first became an Israeli resident, or a veteran returning resident ("תושב חוזר ותיק") who became one, from 5 November 2025 to the end of tax year 2026.
It is made against the Income Tax Ordinance [New Version], which supplies the definitions it leans on (resident, chargeable income, income from personal exertion, other income, relative, material shareholder, transparent corporation, veteran returning resident).
The Ordinance is **not** a source to encode here; each such definition is an input with a citation.

| vintage | source | where |
| --- | --- | --- |
| AS ENACTED, 31 March 2026 | Sefer HaChukim 3511, pp. 416-418 (Knesset PDF `25_lsr_12235101.pdf`, PDF pp. 4-6, sha256 `72244dba261c44d2818f80708fa2dece5d8b99f75e788f48e290942ff4734155`) | `../../registers/source-bundle/encouragement-of-aliyah-and-return-law-5786-2026.he.txt` (a transcription from the page images, checked against the PDF's text layer; see NOTES.md section 0) |

Hebrew is authoritative.
No amendment of the Law is in the sources, so there is one vintage.
The PDF's text layer garbles digits and punctuation (NOTES.md section 0); the transcription, not the raw extraction, is what the encoding quotes.

## Scope — pinned, do not widen or narrow

The whole of the Law: sections 1 (definitions), 2(a) to (e) (the exemption), 3(a) and (b) (the exemption of a non-resident entity's business income), 4 (a limit on application), 5 (savings of laws), 6 (commencement and application), and, as inert text, sections 8 and 9 of the enacting chapter.
Section 5 and sections 8 and 9 say nothing a computation reads and are quoted, not encoded.
The Income Tax Ordinance (ss 1, 14, 62A, 64, 88, 97) is not encoded: what it decides is an input.
The Law of Return, the Absorption Basket Law and the Citizenship Law are not encoded: what they decide (a visa or certificate; a class entitled to a basket; a cancellation of citizenship) is an input.
The capstone (row IL-07) is not edited.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames, each starting `@lang en`: a nouns module (`DECLARE` only) that the others import; one rules module per section (s 1, s 2, s 3, s 4, ss 5-6); a module of answers that resolves the readings of the forks; a builders module; a tests module.
   Identifiers are English backtick names; Hebrew is quoted only in `-- src:N |` comments generated mechanically from line N of the transcription, and in short runs checked by `tools/hebcheck.py` to occur verbatim in it.
2. A tests module asserting what the text says: both sides of the 5 November 2025 and 31 December 2026 edges; each year's ceiling and both sides of it; the relative ceiling; section 2(c)'s total; section 2(d)'s pro rata for 2026 worked by hand; every income type in and out of scope; the election; each branch of section 3; section 4's 75-day edge and its years; and each named reading of each fork.
3. `NOTES.md`: scope, a coverage table with no row left `deferred`, a fork register, an answer table, what `check.sh` prints, open questions.
4. `check.sh` (the skill's template), `encoding.json`, `SOURCE-LICENSE.md` (in the subject directory).

## Rules that matter

- **Encode isomorphically.** One source provision, one recognisable place, with an `@ref` naming the section and the line of the transcription.
- **Where the text is silent or ambiguous** (Meng, SHRUG, 2026-10-08): one named switch per ambiguity, the default a refusal by name saying the text does not decide, the other readings kept by name and tested; a default declines only where the readings give different answers to the question asked.
- **Never invent a number.** The ceilings and the 75 days are the Law's; every other figure is an input.
- **A failing assertion is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code**; record the `l4` sha256 before and after each `check.sh` run.
- Money is new Israeli shekels, as a bare `NUMBER`; days are calendar days (`IMPORT daydate`); a tax year is a calendar year.
- Semi-cleanroom: nothing from the Axiom Foundation or any RuleSpec repository was read.
- Git is read-only for the encoder; the lead commits.

## Toolchain

`/Users/mengwong/.local/bin/l4` (it has no `--version`; NOTES.md section 0 identifies the build used), `JL4_LIBRARY_PATH` unset.
`l4 check FILE` type-checks; `l4 run FILE` also evaluates every `#EVAL` and `#ASSERT`.
