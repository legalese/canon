# Source licence — encoding row `legalese-2026-10-vn-17`

The source is Tasco Insurance's voluntary motor vehicle insurance rules (Decision 168/2024), a private insurer's standard terms; its licence position is recorded in the subject's own file, `../../SOURCE-LICENSE.md`, which governs where this file is silent: **terms undetermined**, the PDF and its OCR text are not held in the repository, and Meng's ruling of 2026-10-06 allows quoting the encoded clauses as short `-- src:N |` comment lines, one clause at a time.

**What this encoding quotes.** 980 `-- src:N |` lines across the modules (892 distinct OCR lines of the 2,743 non-blank lines of `../../source/raw/tasco-voluntary-motor.txt`):

- the decision and the rules (PDF pages 1-29): 815 distinct lines of 1,072 non-blank. Almost all of the rules are operative and the brief asks for the text of each rule above it, so most of the rules are quoted. Provisions that are inert (the decision's recitals, the preamble's purpose, the lists of rights in Articles 4.1 and 5.1, Articles 4.2.7-4.2.10, 5.2.1-5.2.4, 5.2.8-5.2.11, Article 24's repetition of Article 14, BS02's body) are cited by line, not quoted;
- the appendix (pages 30-58, 60-82): 75 lines, the title, the section headings, the notes and the special cases. Its 1,136 rows are **not** quoted; each row in the L4 carries its item number and OCR line instead (NOTES.md, D-01);
- the cover letter (page 59): 2 lines, the typed dates.

The lead should weigh the 815 of 1,072 against the ruling, which covers short clause-level lines and does not cover reproducing the document, before committing. If it is too much, the removal path in `../../SOURCE-LICENSE.md` stands: deleting every `-- src:` line leaves the rules and tests unchanged.

The encoding itself (the `.l4` modules, `check.sh` and the notes) is Apache-2.0. That does not extend to the quoted source text.
