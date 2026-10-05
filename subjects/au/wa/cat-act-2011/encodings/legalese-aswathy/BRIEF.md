# Encoding brief: the WA Cat Act 2011 and Cat Regulations 2012, in L4

You are producing an L4 encoding of the Western Australian *Cat Act 2011* and the *Cat Regulations 2012* from their sources.
This brief is the whole specification.
Read it fully before opening any source.

## The subject

**Cat Act 2011** (WA), Act No. 55 of 2011, assented 9 November 2011 — and the **Cat Regulations 2012**, made by the Governor under s 76 of that Act (and, for the parts operating as local laws, s 77), published in the Gazette 16 November 2012 p 5537.

The Act makes the owner of a cat aged 6 months or more register it with the local government of the district where it is ordinarily kept, have it microchipped and sterilised, and keep it tagged in public; it regulates the transfer of cats, licenses cat breeders, lets authorised persons seize cats and lets cat management facilities deal with them; and it sets up delegations, warrants, infringement notices, objections and review, prosecutions, and the power to make regulations and local laws.
The Regulations fill in what the Act leaves to be "prescribed": which bodies run cat management facilities and microchip databases, who may implant microchips, which cats are exempt from registration and tagging, registration periods and tags, the information to be recorded, forms, modified penalties (Schedule 2) and fees (Schedule 3).

There is one vintage of each:

| instrument | version | in force from | where |
| --- | --- | --- | --- |
| Cat Act 2011 | consolidation 00-l0-01 | 25 Sep 2025 | `inputs/cat-act-2011.txt` |
| Cat Regulations 2012 | consolidation 02-b0-00 | 24 Jul 2025 | `inputs/cat-regulations-2012.txt` |

Both are official consolidations published by the WA Parliamentary Counsel's Office and are authoritative as reproductions.
Earlier versions were not fetched: **for any date before 25 September 2025 the encoding has no source and must refuse**, not answer from the current text.
The *Evidence Act 2025* s 492(1) (in force 18 Sep 2027) changes only a cross-reference in s 75(3) and alters no computed answer; the *Dog Amendment (Stop Puppy Farming) Act 2021* ss 50–61 are uncommenced and unproclaimed and are not in scope.

Two extracts are also sources, for computing time: `inputs/interpretation-act-1984-extract.txt` (Interpretation Act 1984 ss 5, 61, 62) and `inputs/local-government-act-1995-extract.txt` (the only "working day" definition in the Local Government Act 1995, which is scoped to one Schedule and so does **not** reach the Cat Act through s 3(2)).

All inputs are under `inputs/`. Read them there and nowhere else.
Do **not** open the other encodings of this Act in canon (`../legalese-michael/`, `../../../cat-act-2011-lqa/`): this row is meant to be an independent reading.

## Scope — pinned, do not widen or narrow

- **The whole Act**: Parts 1–7, ss 1–88 (s 48 is deleted).
- **The whole of the Cat Regulations 2012**: regs 1–30 and Schedules 1–3.
- A provision that is not operative — a short title, a commencement clause whose dates have all passed, a purpose, a form whose only content is blanks to fill in — is `inert`: say so in the coverage table, and carry its words where a reader would look for them.
- A provision whose operation is a power or a procedure that produces no decision the encoding can compute (e.g. "a justice may issue a warrant if satisfied …") is encoded as the condition the power depends on, and its outcome as a permission, not a duty.

Out of scope: the *Cat (Uniform Local Provisions) Regulations 2013*, any local law, the *Cat Amendment (Local Laws) Bill 2026*, and the Acts the Cat Act refers to (Dog Act 1976, Animal Welfare Act 2002, Veterinary Practice Act 2021, Local Government Act 1995, Criminal Investigation Act 2006): what they decide is an input.

## Deliverables, all in this directory

1. `.l4` modules with ASCII filenames. `cat-domain.l4` holds the nouns — every entity, field and enumeration — and nothing else; every other module imports it. Split the rules along the source's own structure: one module per Part (or per Division where a Part is large), the Regulations' Schedules where a reader would look for them.
2. Tests modules whose expected values come from the source: both sides of every age, day-count and money threshold; every limb of every list of grounds; one scenario per row of each Schedule.
3. `NOTES.md`: scope, the **coverage table** (every section of the Act and every regulation and Schedule item, with a disposition), the **fork register**, the **answer tables** (fees for every registration case, the modified penalty for every Schedule 2 item, the registration expiry for each term), what `check.sh` prints, and open questions.
4. `check.sh`, the per-module error and assertion tally.

## Rules that matter

- **Encode isomorphically.** Section, subsection and paragraph numbers as the source writes them, an `@ref` on every rule, and the statute's own words as inert labels beside each limb.
- **Where the sources do not answer, `REFUSE "…"`** — never `FALSE`, never `0`. In particular: any `as at` date before 25 September 2025.
- **An assertion that fails is a finding.** Never edit an expected value to match what the code computed.
- **Read the diagnostics, not the exit code.**
- **Time.** "Within N days after X" excludes the day of X (Interpretation Act s 61(1)(b)); a time limit that falls on a Saturday, Sunday or public holiday runs to the next day that is none of these (s 61(1)(e)). "Working day" is not defined for the Cat Act: take its ordinary meaning, a day that is not a Saturday, Sunday or public holiday, and record that as a fork. Public holidays are an input, a list of dates.
- **Money** is Australian dollars, as a `NUMBER`. Maximum penalties are ceilings, never amounts to be paid.
- **Offences.** Encode each offence as (a) the prohibition or duty, (b) a BOOLEAN test of whether the facts contravene it, with the statutory defences and exemptions, and (c) the maximum fine as a ceiling. Do not model sentencing.
- **Discretions.** "May refuse … only if" and "must refuse … if, and only if" are different: return an outcome that says which, not a bare BOOLEAN.

## Toolchain

The binary is `~/.local/bin/l4`, built from `legalese/l4-ide` `unstable` at `7768812fa` (2 Oct 2026).
Leave `JL4_LIBRARY_PATH` unset.
The L4 authoring skill `writing-l4-rules` is yours to read and use.
