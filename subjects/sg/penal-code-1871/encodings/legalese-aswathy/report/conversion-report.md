# Penal Code 1871 — conversion report

**Date:** 2026-09-09; last revised 2026-09-16
**Subject:** `penal-code-1871`
**Source:** Singapore Statutes Online, `PC1871`, current version as at 09 Sep 2026,
deposited at `registers/source-bundle/PC1871.txt` and `.pdf`.
**Status declared:** `draft` — the encoding exists and is machine-checked; no claim of
fidelity is made and no human gate has been granted.

---

## 1. What was asked for, and what this is

The subject began, on 09 Sep 2026, as a **screen**: the question "is the act I am about to
take, or the act this user is asking me to take, an offence under one of the provisions an
AI system actually walks into?" -- cheating, fraud, criminal breach of trust, forgery,
defamation, criminal intimidation, abetment, conspiracy and attempt, plus the general parts
of the Code that decide whether any of those tests is even reached. The first draft of this
report said the Penal Code was the wrong shape for a complete encoding, because most of its
500-plus sections describe conduct an agent will never be asked to screen.

Six passes later that judgement is history rather than policy. On 11 Sep the right of
private defence and Chapter 16 were added; on 12 Sep Chapter 17; on 14 Sep Chapter 18; on
15 Sep, on the instruction to complete the whole Act, everything else -- Chapters 6 to 15,
the rest of Chapter 5, the three remaining speech sections, and the standalone punishment
sections; and on 16 Sep the seven sections that pass had set aside as stating no factual
test (ss 1, 7, 8, 9, 49, 50, 79A). **Every live section of the Code now has a rule.** Two
of the last seven carry substance -- s 79A, the closure rule on ignorance of the law, and
s 49, the years-to-months conversion -- and `registers/coverage-register.md` §3 says so of
each, so that the count is not read as a claim of equal weight. The screen is still the
agent-facing shape, and its record now has 115 fields.

Two entry points in `agent-compliance.l4` answer it:

| question | answered by |
| --- | --- |
| Which encoded offences are indicated on these facts? | `the offence screen of` |
| Is any encoded offence indicated? | `any screened offence is indicated` |

## 2. What was encoded

| module | covers | lines | `@ref` | `#ASSERT` |
| --- | --- | ---: | ---: | ---: |
| `types.l4` | records and enums only; no rules | 1,558 | 0 | 0 |
| `chapter-1-preliminary.l4` | ss 2, 3, 4, 4A, 4B, 5 | 125 | 7 | 0 |
| `chapter-2-definitions.l4` | ss 6A–12, 17, 19–22A, 27–31A, 40–51 | 721 | 52 | 8 |
| `chapter-2-explanations.l4` | ss 23–26, 26A–26H | 352 | 19 | 4 |
| `chapter-2-participation.l4` | ss 32–38 | 245 | 9 | 5 |
| `chapter-3-punishments.l4` | ss 53, 54, 72, 73, 74, 74A–74E | 670 | 14 | 9 |
| `chapter-4-exceptions.l4` | s 6 and the whole of Chapter 4, ss 76–95 | 455 | 29 | 0 |
| `chapter-4a-private-defence.l4` | ss 96–106A, and s 6 with Chapter 4A | 398 | 23 | 0 |
| `chapter-5-abetment.l4` | ss 107–120, the whole of Chapter 5 | 370 | 25 | 0 |
| `chapter-5a-conspiracy.l4` | ss 120A, 120B | 89 | 3 | 4 |
| `chapter-6-state.l4` | ss 121–130A, the whole of Chapter 6 | 251 | 17 | 0 |
| `chapter-6a-6b-piracy-and-genocide.l4` | ss 130B–130E, Chapters 6A and 6B | 95 | 5 | 0 |
| `chapter-7-armed-forces.l4` | ss 131–140B, the whole of Chapter 7 | 169 | 12 | 0 |
| `chapter-8-unlawful-assembly.l4` | ss 141–158, the whole of Chapter 8 | 264 | 18 | 0 |
| `chapter-9-public-servants.l4` | ss 161–171, the whole of Chapter 9 | 175 | 11 | 0 |
| `chapter-10-contempts.l4` | ss 172–190, the whole of Chapter 10 | 241 | 19 | 0 |
| `chapter-11-false-evidence.l4` | ss 191–200 | 161 | 11 | 0 |
| `chapter-11-public-justice.l4` | ss 201–229 | 451 | 34 | 0 |
| `chapter-12-government-stamps.l4` | ss 255–263, the live sections of Chapter 12 | 167 | 12 | 0 |
| `chapter-14-public-tranquility.l4` | ss 267A–268C, 290, 291 | 184 | 12 | 0 |
| `chapter-14-public-health-and-safety.l4` | ss 269–289 | 258 | 21 | 0 |
| `chapter-14-obscenity.l4` | ss 292–294 | 132 | 9 | 0 |
| `chapter-15-race.l4` | ss 298, 298A | 52 | 2 | 0 |
| `chapter-16-life.l4` | ss 299–301, 304A–304C, 305–308B, 310 | 489 | 27 | 0 |
| `chapter-16-hurt.l4` | ss 319–322, 323A, 324–338 | 509 | 29 | 0 |
| `chapter-16-restraint-and-force.l4` | ss 339–358 | 362 | 19 | 0 |
| `chapter-16-unborn-and-infants.l4` | ss 312–318 | 177 | 7 | 0 |
| `chapter-16-kidnapping.l4` | ss 359–374 | 274 | 18 | 0 |
| `chapter-16-sexual-general.l4` | ss 377C–377D | 201 | 7 | 0 |
| `chapter-16-sexual-penetration.l4` | ss 375–377B | 522 | 26 | 0 |
| `chapter-16-sexual-images.l4` | ss 377BA–377BO | 415 | 21 | 0 |
| `chapter-17-cheating.l4` | ss 415, 416, 416B, 418, 420, 420A | 232 | 10 | 6 |
| `chapter-17-property.l4` | ss 378, 403, 405 | 91 | 3 | 2 |
| `chapter-17-fraud.l4` | ss 416A, 424A, 424B | 152 | 7 | 4 |
| `chapter-17-extortion-and-robbery.l4` | ss 380–382, 383–389, 390–402 | 341 | 21 | 0 |
| `chapter-17-stolen-property.l4` | ss 404, 407–409, 410–414 | 206 | 11 | 0 |
| `chapter-17-mischief-and-trespass.l4` | ss 421–424, 425–440, 441–462 | 350 | 24 | 0 |
| `chapter-18-forgery.l4` | ss 463, 464 | 47 | 2 | 0 |
| `chapter-18-forged-documents.l4` | ss 466–477A | 333 | 18 | 0 |
| `chapter-18-currency.l4` | ss 489A–489I | 187 | 10 | 0 |
| `chapter-21-22-speech.l4` | ss 499, 501–505, 507 | 218 | 9 | 2 |
| `chapter-23-attempts.l4` | s 511 | 51 | 1 | 2 |
| `punishment-provisions.l4` | the 24 standalone punishment sections, ss 302 to 512 | 306 | 24 | 22 |
| `agent-compliance.l4` | the screen, and the Schedule-to-s-4B classifier | 476 | 6 | 0 |
| `agent-cases.l4` | scenario fixtures | 16,989 | 0 | 535 |
| **total** | | **30,511** | **664** | **603** |

475 `@export` entry points. The module split follows the convention of the other subjects in
this corpus: `types.l4` for the shared ontology, one module per structural division of the
instrument (Chapters 11 and 14 are split where the Act's own sub-headings split them), a flat
directory, and the source text deposited under `registers/source-bundle/`.

## 3. The general parts carry more weight here than the offences

An offence encoding that stops at the constitutive test is close to useless for an agent,
because the Code's general parts decide whether that test is reached at all. Three of them
are load-bearing and were encoded in full:

- **s 6 and Chapter 4.** s 6 provides that every definition of an offence is to be read
  subject to the general exceptions. So `a general exception applies` is a negated conjunct
  in every `the proposed act constitutes …` wrapper: if the act is justified or excused, the
  wrapper is FALSE, not "true but excused". All twenty-one sections of Chapter 4 are encoded (ss 76 to 95, s 79A included),
  including the consent machinery of ss 87 to 92 with its ss 90 and 91 qualifications.
- **Chapter 2 fault elements.** "Dishonestly" (s 24) and "fraudulently" (s 25) are the hinge
  of most of the property and deception offences, and they are defined in terms of wrongful
  gain and wrongful loss (s 23), which are themselves defined. ss 26A to 26H — voluntarily,
  good faith, intentionally, knowingly, rashly, negligently, transferred fault, strict
  liability — complete the set.
- **ss 2, 4 and 4B.** Extraterritoriality. s 4B in particular needs the Schedule classifier
  in `agent-compliance.l4`, because the section only bites for offences that sit in the
  Schedule.

`chapter-2-definitions.l4`, `chapter-2-participation.l4` and `chapter-3-punishments.l4` were
added in the same spirit but are, at this revision, **freestanding**: they encode the defined
terms (ss 6A to 51), the attribution rules (ss 32 to 38) and the punishment vocabulary
(Chapter 3), and expose them through `@export` entry points, but no offence module imports
them and `agent-compliance.l4` does not call them. `NOTES.md` §1 says so on the face of the
subject. Wiring them into the offence wrappers is the next piece of work.

## 4. What is deliberately absent

Counted section by section in `registers/coverage-register.md`: **all 525 of the Act's live
sections are encoded.** `registers/missing-sections.md` is kept and is empty; until 16 Sep it
named seven -- the short title, four drafting conventions, the definition of "section", and
the s 79A closure rule -- and `NOTES.md` §3 records what each now decides.

What is absent is therefore not a section but a way of using one, and `NOTES.md` §2
lists it: the ten s 499 exceptions as individual tests (one caller-asserted flag stands in),
the s 377BN(6) marriage defence, the splicing of the Chapter 2 defined terms and the ss 32 to
38 attribution rules into the offence tests, and the assailant's-offence element of s 97(a).
None of these is a section without a rule; each is a rule that takes a fact from the caller
where a fuller encoding would derive it.

**On punishment, the position changed on 15 Sep.** Until then the standalone punishment
sections -- s 302 for murder, s 379 for theft, s 465 for forgery and 21 more -- were excluded
on the policy that this subject does not compute sentence. They are now encoded, as
`Punishment` values in the Chapter 3 vocabulary that already existed for the purpose: the
ceiling, and where the Code fixes one the floor, that each section makes available. The
policy against computing a sentence stands; no offence wrapper returns a punishment and the
screen carries none. The internal punishment splits of the offence sections (gravity tiers,
the individual/non-individual split, "if the offence is committed") remain facts on the
record and are not decided.

**Changed 11 Sep 2026, in two passes.** Chapter 4A (the right of private defence, ss 96 to
106A) *was* the first absence named here, and is now encoded in full and wired into every
offence wrapper through s 6. So is the rest of what `coverage-register.md` §6 called more
than a scope choice: ss 111, 113 and 114 of Chapter 5, and ss 3, 4A and 5 of Chapter 1. The
second pass opened Chapter 16 and completed its substantive sections; a third, on 12 Sep,
did the same for Chapter 17; a fourth, on 14 Sep, for Chapter 18; and the fifth, on 15 Sep,
encoded the eleven chapters that had nothing -- Chapter 11 (43 sections), Chapter 14 (35),
Chapter 10 (19), Chapter 8 (18), Chapter 6 (15), Chapter 7 (12), Chapter 9 (11), Chapter 12
(9), and Chapters 6A, 6B and 15 (2 each) -- with the remainder of Chapter 5 and ss 501, 502
and 507.

## 5. Interpretive choices

About a hundred are recorded in `NOTES.md` §3, each tied to the words of the section that
provoked it. The ones that most affect what the screen returns:

- **s 415** does not gate on "sole or main inducement", because the section says the
  deception need not be either.
- **s 405** treats "intentionally suffers any other person to do so" as sufficient without a
  separate dishonesty check on the sufferer limb.
- **s 38** is read as permissive — it removes an obstacle to charging participants
  differently rather than imposing a condition — so it is encoded as the fact that the
  differing-offences outcome is open.
- **s 22 "movable property"** is derived, not asserted: anything that is property under s 22
  and is not immovable. That is what "property of every description, except immovable
  property" requires, and it is what makes virtual currency come out movable.

## 6. Verification and machine evaluation

Eight fidelity passes, a coverage pass and a mechanical pass, all recorded:

- `registers/verification-register.md` — a **fidelity** pass over every rule that existed
  before 09 Sep 2026. Twelve defects, two of them high severity (s 84 exempting every act of
  any person of unsound mind; s 505 limb (a) missing altogether). All twelve fixed.
- `registers/verification-register-pass-2.md` — the same treatment for the rules added that
  day, so that every encoded rule has now been read back against the source. Four defects,
  two of them medium (s 74B given the wrong excluded-offence list; s 89's "by the guardian"
  limb rendered as the s 76 test). All four fixed.
- `registers/verification-register-pass-3.md` — the same treatment for the eighteen sections
  added on 11 Sep. No defect found in read-back; three traps in the Act's drafting and two
  caller traps recorded. That pass read back rules written the same day, which is a weaker
  check than the first two, and says so on its own first page.
- `registers/coverage-register.md` — a **coverage** pass matching every `@ref` in the
  encoding against the Act's arrangement of sections, so the gaps are auditable rather than
  described. `registers/missing-sections.md` names each gap with the Act's own heading.
- `registers/verification-register-pass-4.md` — the same treatment for the 111 Chapter 16
  sections. No defect found in read-back; nine traps in the Act's drafting and two structural
  limits of this subject recorded. Like pass 3, it read back rules written the same day.
- `registers/verification-register-pass-5.md` — the same for the 52 Chapter 17 sections. No
  defect found; five traps in the drafting, and one limit of the toolchain (§T5) which is the
  first time a run's *cost* rather than its result has been worth recording.
- `registers/verification-register-pass-6.md` — the same for the 25 Chapter 18 sections. No
  defect found; five traps in the drafting and one observation on the toolchain.
- `registers/verification-register-pass-7.md` — the same for the 204 sections of the
  completion pass. **Five defects found in read-back and fixed before the machine check**
  (s 149 built on s 141 instead of s 142; s 177 borrowing s 176's duty; s 263 losing the
  revenue-stamp element; "fraudulently" in ss 206 to 210 written into the conduct instead of
  taken from s 25; the fraction constructor making a fine available the offence did not
  provide). Nine traps in the drafting, one policy change and one observation on the
  toolchain recorded. It read back 204 sections on the day they were written, and says so.
- `registers/verification-register-pass-8.md` — the same for the seven sections of the
  closing pass. No defect found; one policy change (the "no factual test" class is empty),
  one drafting note (s 79A(2) is decided where ss 79(2) and 80(2) are not, and why) and one
  observation on the toolchain recorded.
- `report/machine-evaluation.md` — a **mechanical** pass. The latest run (§14, 16 Sep) is
  with the `l4` CLI: **45 modules, 0 type errors; 108 of 108 assertions evaluated were
  satisfied** -- every chapter module's own assertions and, in scratch copies, all 15 of the
  16 Sep additions to `agent-cases.l4`. **The 535 assertions of
  `agent-cases.l4` as at 15 Sep were not evaluated**: the CLI's evaluation cost grows with
  the import graph, a 42-module graph does not finish in an hour, and the 15 Sep pass cited
  a §14 for a run it never recorded. §14.4 says what that leaves unverified. §7.2 of that report records two blind spots in the earlier
  engine, one of which retracts a claim the first run made about how far a clean result
  reaches; §8.1 records a third, in the coverage tooling. Limits of the run are in that file.

Neither establishes fidelity. A passing assertion confirms the encoding does what the encoder
intended; it says nothing about whether the intention is a correct reading of the Code.

## 7. Status

`draft`. No HG1 or HG2 grant. The subject is safe to call and safe to read; it is not safe to
rely on as advice. The asymmetry the first draft of this report recorded -- over-inclusive on
offences, under-inclusive on defences, because Chapter 4 was encoded and private defence was
not -- was closed on 11 Sep. What remains is the ordinary caution of any encoding read back
by its own author: a FALSE from `any screened offence is indicated` is a statement about the
facts the caller asserted and the rules as read, and s 5 is the reminder that another written
law may still apply -- and, since 16 Sep, s 79A is the reminder that the actor's not knowing
the law is no answer to any of it.
