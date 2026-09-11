# Penal Code 1871 — conversion report

**Date:** 2026-09-09
**Subject:** `penal-code-1871`
**Source:** Singapore Statutes Online, `PC1871`, current version as at 09 Sep 2026,
deposited at `registers/source-bundle/PC1871.txt` and `.pdf`.
**Status declared:** `draft` — the encoding exists and is machine-checked; no claim of
fidelity is made and no human gate has been granted.

---

## 1. What was asked for, and what this is

The Penal Code is the wrong shape for a complete encoding. It has 500-plus operative
sections, most of which describe conduct an AI agent will never be asked to screen — mutiny,
piracy, offences relating to coin, the whole of the sexual-offences chapter. Encoding all of
it would produce a great deal of L4 that nothing calls.

So the subject was scoped to a **screen**: the question "is the act I am about to take, or
the act this user is asking me to take, an offence under one of the provisions an AI system
actually walks into?" That is cheating, fraud, criminal breach of trust, forgery, defamation,
criminal intimidation, abetment, conspiracy and attempt — plus the general parts of the Code
that decide whether any of those tests is even reached.

Two entry points in `agent-compliance.l4` answer it:

| question | answered by |
| --- | --- |
| Which encoded offences are indicated on these facts? | `the offence screen of` |
| Is any encoded offence indicated? | `any screened offence is indicated` |

## 2. What was encoded

| module | covers | lines | `@ref` | `#ASSERT` |
| --- | --- | ---: | ---: | ---: |
| `types.l4` | records and enums only; no rules | 297 | 0 | 0 |
| `chapter-1-preliminary.l4` | ss 2, 4, 4B | 58 | 4 | 0 |
| `chapter-2-definitions.l4` | ss 6A–12, 17, 19–22A, 27–31A, 40–51 | 700 | 50 | 8 |
| `chapter-2-explanations.l4` | ss 23–26, 26A–26H | 352 | 19 | 4 |
| `chapter-2-participation.l4` | ss 32–38 | 245 | 9 | 5 |
| `chapter-3-punishments.l4` | ss 53, 54, 72, 73, 74, 74A–74E | 538 | 14 | 7 |
| `chapter-4-exceptions.l4` | s 6 and the whole of Chapter 4, ss 76–95 | 453 | 29 | 0 |
| `chapter-5-abetment.l4` | ss 107, 108, 108A, 108B | 67 | 4 | 0 |
| `chapter-5a-conspiracy.l4` | ss 120A, 120B | 88 | 3 | 4 |
| `chapter-17-cheating.l4` | ss 415, 416, 416B, 418, 420, 420A | 231 | 10 | 6 |
| `chapter-17-property.l4` | ss 378, 403, 405 | 86 | 3 | 2 |
| `chapter-17-fraud.l4` | ss 416A, 424A, 424B | 151 | 7 | 4 |
| `chapter-18-forgery.l4` | ss 463, 464 | 46 | 2 | 0 |
| `chapter-21-22-speech.l4` | ss 499, 503, 504, 505 | 165 | 6 | 2 |
| `chapter-23-attempts.l4` | s 511 | 50 | 1 | 2 |
| `agent-compliance.l4` | the screen, and the Schedule-to-s-4B classifier | 136 | 5 | 0 |
| `agent-cases.l4` | scenario fixtures | 350 | 0 | 9 |
| **total** | | **4,013** | **166** | **53** |

62 `@export` entry points. The module split follows the convention of the other subjects in
this corpus: `types.l4` for the shared ontology, one module per structural division of the
instrument, a flat directory, and the source text deposited under `registers/source-bundle/`.

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

Counted section by section in `registers/coverage-register.md`: **126 of the Act's 525 live
sections are encoded, about 24%**, and 288 live sections sit in chapters with nothing encoded
at all. `registers/missing-sections.md` names every one of the 399 unencoded sections
individually. In summary: Chapters 6 to 16, most of Chapter 17, most of Chapter 18, the ten
s 499 exceptions as individual tests, and any computation of sentence for a particular
offence.

Two of these are worth naming here because a caller could be misled:

- **Chapter 16 is not encoded** — ss 299 to 377D, the whole of the offences affecting the
  human body, and the largest single absence at 120 live sections. Chapter 4A now decides
  when the right of private defence justifies an act, but the offence that act would
  otherwise be is not encoded, so the justification cannot be reported against a hurt or
  homicide charge.
- **The s 499 exceptions** collapse into one caller-asserted flag,
  `a section 499 exception applies`. The encoding does not decide whether the imputation was
  for the public good; it asks the caller.

**Changed 11 Sep 2026.** Chapter 4A (the right of private defence, ss 96 to 106A) *was* the
absence named here, and is now encoded in full and wired into every offence wrapper through
s 6. So is the rest of what `coverage-register.md` §6 called more than a scope choice:
ss 111, 113 and 114 of Chapter 5, and ss 3, 4A and 5 of Chapter 1.

## 5. Interpretive choices

Thirty are recorded in `NOTES.md` §3, each tied to the words of the section that
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

Three fidelity passes, a coverage pass and a mechanical pass, all recorded:

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
- `report/machine-evaluation.md` — a **mechanical** pass running every module through the
  `jl4-lsp` language server as a batch checker: **18 modules, 0 type errors, 88 of 88
  assertions satisfied**, no directive skipped or stubbed. §7.2 of that report records two
  blind spots in the available engine, one of which retracts a claim the first run made
  about how far a clean result reaches. Limits of the run are in that file.

Neither establishes fidelity. A passing assertion confirms the encoding does what the encoder
intended; it says nothing about whether the intention is a correct reading of the Code.

## 7. Status

`draft`. No HG1 or HG2 grant. The subject is safe to call and safe to read; it is not safe to
rely on as advice, and the screen is deliberately **over-inclusive on offences and
under-inclusive on defences** — it encodes the whole of Chapter 4 but no private
defence, so a FALSE from `any screened offence is indicated` is more trustworthy than a TRUE.
