# PLAN — conventions for the L4 encoding of the Penal Code 1871

Written by the ontology agent on 2026-09-26, before any encoder started.
Every encoder follows this file; where it and `BRIEF.md` disagree, `BRIEF.md` wins and the disagreement is a finding to report.
The shared modules it describes exist and run clean: `deposit/pc-domain.l4`, `deposit/pc-general.l4` and `deposit/pc-general-tests.l4` show 0 errors and 0 warnings, and 115 of 115 assertions satisfied (`deposit/check.sh`), on the toolchain named in `BRIEF.md` with `JL4_LIBRARY_PATH` unset.

## 1. Modules, owners, and the import graph

| module | owner | covers |
| --- | --- | --- |
| `pc-domain.l4` | ontology | shared nouns only: `Pronoun`, `Sex`, `Kind of person`, `Person`, `Particulars`, `Place`, `Property`, `Document`, `Office`, `Fault word` |
| `pc-general.l4` | ontology | Chapter 2 (ss 6-52) as ladders; `Punishment` and its readers (ss 41, 53); `Charge` and the charge-wording helpers (CPC 2010 ss 123-126) |
| `pc-general-part.l4` | general-part | Chapter 1 (ss 1-5), Chapter 3 (ss 53-75), Chapter 5 (ss 107-120), Chapter 5A (ss 120A-120B), Chapter 23 (ss 511-512) |
| `pc-exceptions.l4` | exceptions | Chapter 4 (ss 76-95), Chapter 4A (ss 96-106A) |
| `pc-state-public.l4` | state-public | Chapters 6, 6A, 6B, 7, 8, 9, 10 (ss 121-190) |
| `pc-justice-order.l4` | justice-order | Chapters 11, 12, 13, 14, 15 (ss 191-298A) |
| `pc-body-a.l4` | body-a | Chapter 16, "Offences affecting life" to "Criminal force and assault" (ss 299-358) |
| `pc-body-b.l4` | body-b | Chapter 16, "Kidnapping, abduction, slavery and forced labour" to the end (ss 359-377D) |
| `pc-property.l4` | property | Chapter 17 (ss 378-462) |
| `pc-documents-defamation.l4` | documents-defamation | Chapters 18, 20, 21, 22 (ss 463-510) |

Each group's tests go in `pc-<group>-tests.l4`.
A large group may split into `pc-<group>-<part>.l4` (for example `pc-property-theft.l4`, `pc-property-cheating.l4`), keeping `pc-<group>-tests.l4` or `pc-<group>-<part>-tests.l4` beside each.
No basename may equal a library's (`prelude`, `daydate`, `math`, `time`, `legal-persons`, …).
ASCII only in the `.l4` files, except the `§` / `§§` section markers the brief requires: straight quotes for the Code's curly ones, `-` for its dashes, `...` for an ellipsis. The shared modules follow this.

**The import graph, during the parallel phase.**
Every group module starts:

```l4
IMPORT prelude
IMPORT `pc-domain`
IMPORT `pc-general`
```

and imports **nothing else from another group**, because the other group's module may not exist or may not compile yet.
Within your own group, import your own parts freely (robbery imports theft, as in the reference row).

**A cross-reference to another group's section** becomes a BOOLEAN leaf in your facts record, named in the Code's words, whose `@desc` cites the section and says who owns it:

```l4
    `voluntarily causes hurt` IS A BOOLEAN @desc Did the accused voluntarily cause hurt (s 321)? — defined in pc-body-a; joined at integration
```

List every such leaf in your report under "cross-module joins owed".
At integration these become calls into the owning module, along these edges only (so the graph stays acyclic): `property → body-a` (ss 382, 394, 397, 459-460 read hurt), `documents-defamation → property` (s 468 reads s 415), `body-b → body-a` (s 367 reads grievous hurt), `justice-order → state-public`, and every group `→ general-part` and `→ exceptions`.
If you need an edge not on this list, say so in your report; do not create it.

**Who owns a definition that other chapters use.**
The section's own group — "hurt" and "grievous hurt" (ss 319-320) are body-a's; "theft" (s 378), "stolen property" (s 410), "cheat" (s 415), "mischief" (s 425) and "house-breaking" (s 442) are property's; "forgery" and "false document" (ss 463-464) and "criminal intimidation" (s 503) are documents-defamation's; "unlawful assembly" (s 141) is state-public's; "false evidence" (s 191) is justice-order's; "abet" (s 107), "criminal conspiracy" (s 120A), "attempt" (s 511), and the enhanced-penalty definitions of ss 73-74E ("domestic worker", "vulnerable person", "intimate relationship") are general-part's; consent (s 90) and private defence are exceptions'.
Chapter 2's words ("public servant", "dishonestly", "document", "valuable security", …) are already in `pc-general.l4` — never redefine them.

## 2. Names

- **Backticked names that read like the Code.**
  A leaf is the Code's own words for the element (`` `deceived the victim` ``, `` `dishonestly` ``, `` `movable property` ``), not a paraphrase and not an abbreviation.
- **The three names the charge generator calls, per offence, spelled exactly:**
  - the defining predicate, named after the section's own verb: `` cheats f ``, `` `commits theft` f ``, `` `voluntarily causes hurt` f ``, `` `commits criminal breach of trust` f ``;
  - `` `offence under s N` f `` — BOOLEAN, one per **punishing** section or subsection that punishes differently (`` `offence under s 420` ``; where subsections differ in elements, `` `offence under s 376(1)` ``, and so on — use the section's own subsection numbering, with no space);
  - `` `charge under s N` f `` — returns a `Charge`.
  The `N` is the punishing section as the Code prints it: `323A`, `376AA`, `377BE`, `489A`, `130E`.
- **Chapter 2's words** are `` `<the word> within section N` `` (`` `dishonestly within section 24` ``, `` `public servant within section 21` ``).
  Do the same for a definition section in your own chapters that other sections read (`` `grievous hurt within section 320` `` is fine; so is the section's own verb form if the Code uses one).
- **The facts record** is `` `<Family> Facts` `` (`` `Theft Facts` ``, `` `Rape Facts` ``, `` `Unlawful Assembly Facts` ``), and the single input is always `GIVEN f IS A …` — the catalogue records `factsParam: 'f'`.
- **A punishment** is `` `punishment prescribed by s N` `` (§6).
- **A named refusal**'s name is its message (§7).
- Mixfix traps: no segment may contain `--`; a one-argument pattern may not end with a keyword segment (`writing-l4-rules/references/gotchas.md`).
  Record field names and enum constructors share one namespace with functions: a field named `death` and a constructor named `death` collide, and the error names neither (measured writing `pc-general.l4`).

## 3. The facts record, and what a ladder may contain

The charge generator (`reference/charge-generator-README.md`) draws each exported `DECIDE` as a ladder, labels each leaf by pretty-printing it, parses `f's field` back to a field path, lets the investigator toggle each leaf Unknown → True → False, and **completes a partial record against the export's schema with every unknown element FALSE**.
Everything below follows from that.

1. **One facts record per offence family, the single input of every export for that family.**
   It carries (a) the particulars — `particulars IS A Particulars` (from `pc-domain`), and the victim as `victim IS A Person` or as the reference row's three flat strings; (b) the elements, as **flat BOOLEAN leaves**; (c) the STRING fields the recital needs (what was taken, what the victim was deceived into).
2. **A ladder is a boolean combination of `f's leaf` terms and inert strings.**
   Inert strings quote the section between the leaves (TRUE under AND, FALSE under OR) — the reference row's "inert style"; `cheating-415-417-420.l4` is the model.
   The linter warns ("AND and OR operators appear at the same indentation level") when a `..` or `...` continuation sits in the same column as an `AND` or `OR`; in a ladder that has both, write the joins as `AND`/`OR` and keep `..` for runs of one operator. `pc-general.l4` is warning-free and shows the shapes.
   A call to another rule (`` cheats f ``) is drawn as ONE box; the catalogue stacks that rule's own ladder under the card as a `definitionFns` entry, so make the callee an `@export`ed DECIDE over the same `f` (or a record nested in `f`, as robbery nests theft).
3. **Chapter 2 words ride as flat leaves too.**
   `dishonestly`, `fraudulently`, `voluntarily`, `in good faith`, `public servant`, `movable property`, `valuable security`, `document`: a BOOLEAN leaf with that name, whose `@desc` quotes or paraphrases the Chapter 2 definition and cites it.
   Do **not** nest `` `Dishonesty Facts` `` inside your record and call `` `dishonestly within section 24` `` on it: the ladder would show one untoggleable box.
   The Chapter 2 ladder is the drill-down; name it in your report as a `DEFINITION_LADDERS` entry (`{ fn, leaf, section }`), as the catalogue does for ss 24 and 25.
4. **No `MAYBE`, no `LIST`, no `NUMBER` among the leaves an exported ladder reads.**
   Schema completion fills unknowns with FALSE; it has no safe filler for those types, and a NUMBER filled with 0 turns "below 16 years of age" TRUE — a charge asserting a fact nobody supplied (FORK G-6).
   STRING particulars are fine; they are recited, not tested.
5. **Numeric thresholds (ages, amounts, weights, strokes).**
   The ladder reads a BOOLEAN leaf in the Code's words — `` `the victim is below 16 years of age` `` — and the same module exports a helper over the number that decides it, named the same way, with the boundary tests on the helper:

   ```l4
   @export Whether a person of the given age is "below 16 years of age" (s 376A)
   GIVEN years IS A NUMBER @desc The person's age in completed years
   GIVETH A BOOLEAN
   DECIDE `below 16 years of age` years IF years < 16

   #ASSERT `below 16 years of age` 15
   #ASSERT NOT `below 16 years of age` 16
   ```

   Fixtures set the leaf from the helper (`` `the victim is below 16 years of age` IS `below 16 years of age` 15 ``), so the threshold is tested and the ladder stays safe.
6. **Every exported function has `@export <one line>`, and every `GIVEN` a `@desc`.**
   Every field of a facts record has a `@desc` phrased as the question an investigator is asked.
7. **Fault and physical elements.**
   Where it matters (s 26G transferred fault, s 26H strict liability, s 79 mistake), say in the leaf's `@desc` whether it is a fault element or a physical element (s 22A).
   Where a section uses a fault word — "intentionally", "knowingly", "rashly", "negligently" — the leaf is that word; s 26D(3), 26E(3) and 26F(2) (which lower words a higher state of mind satisfies) are `` `the fault element` required `is established by` proven `` in `pc-general.l4`, for the drill-down.
8. **Illustrations and Explanations.**
   An Explanation is law: it either widens a leaf (say so in the leaf's `@desc`) or adds a limb (encode it in the ladder, citing it as the reference row cites s 25 Explanation 1).
   An Illustration is a test (§9).

## 4. The shared nouns, and what to add

`pc-domain.l4` holds only what a witness could testify to and more than one chapter uses: persons (`Person`, `Pronoun`, `Sex`, `Kind of person`), `Particulars`, `Place`, `Property` (s 22 atoms), `Document` (ss 29-31A atoms), `Office` (s 21 atoms), and `Fault word`.
Age and sex are deliberately **not** on `Person`: where a section turns on them they are elements of that offence and live in its facts record as §3.5 says.
If you need a noun the domain lacks and another group plainly will too (a vehicle, a weapon, a dwelling-house, a vessel, a child), declare it in your own module and propose it in your report under "proposed shared nouns"; do not edit `pc-domain.l4`.

## 5. General exceptions and private defence (Chapters 4 and 4A)

s 6 says every definition and penal provision is "understood subject to" the General Exceptions and the Right of Private Defence, "though those exceptions are not repeated".
The encoding follows the Code: **no offence ladder repeats a general exception.**

- The exceptions group exports, per exception, a BOOLEAN ladder over its own facts record (`` `Unsoundness of Mind Facts` ``, `` `Private Defence Facts` ``, …), named `` `exception under s N` e `` (most of ss 76-95 begin "Nothing is an offence …", but not all — s 78, s 90 and s 91 are worded otherwise, so the name does not quote them), and one roll-up, `` `a general exception applies` e ``, over a record nesting them.
- A charge is not refused because an exception might apply: CPC s 123(5) asserts the conditions required to **constitute** the offence, and a general exception is not one of them — the burden of bringing a case within one is on the accused (Evidence Act 1893 s 107; **not in this job's inputs — the exceptions encoder should verify it and cite it, or drop the citation**).
- The charge sheet at integration reads both: an offence made out and no exception established.
- **Exceptions inside an offence's own section** (s 300's Exceptions 1-7, s 499's) are not general exceptions; they are part of that section, and its encoder puts them in its ladder, citing them.
- The s 26G(5) and s 301(2) rule — the accused may rely on a defence as though the act concerned the intended person — is the exceptions group's to wire; `pc-general.l4`'s s 26G ladder takes "a defence or exception applies" as one leaf.

## 6. Punishment

Every punishing section (or subsection that punishes differently) declares its punishment once, verbatim, as data:

```l4
@ref Penal Code 1871 s 417
`punishment prescribed by s 417` MEANS Punishment WITH
    section                  IS "417"
    words                    IS "imprisonment for a term which may extend to 3 years, or with fine, or with both"
    death                    IS `not prescribed`
    `imprisonment for life`  IS `not prescribed`
    imprisonment             IS `or with`
    `maximum term in months` IS JUST 36
    `minimum term in months` IS NOTHING
    `forfeiture of property` IS `not prescribed`
    fine                     IS `or with`
    `maximum fine`           IS NOTHING
    `minimum fine`           IS NOTHING
    caning                   IS `not prescribed`
    `minimum strokes`        IS NOTHING
    `maximum strokes`        IS NOTHING
    `or with both`           IS TRUE
```

- `words` is copied mechanically from the section, from "imprisonment"/"death"/"fine" to the end of the punishing clause, without "shall be punished with".
  It is what goes into the `Charge`'s `punishment` field: pass `` (`punishment prescribed by s 417`)'s words ``.
- Each kind is `shall be punished with` (mandatory), `or with` (one of alternatives), `shall also be liable to` (discretionary, in addition), or `not prescribed` — the Code's own verbs; see `` `How a punishment is prescribed` `` in `pc-general.l4`.
- Terms are in **months** (3 years = 36; 20 years = 240), fines in dollars, and a bound the section does not state is `NOTHING` — never `0`.
- Where a punishment depends on a fact (s 420(1) vs (2); an aggravated limb; a repeat offender), declare one record per variant and choose between them in the charge builder with `IF … THEN … ELSE` on the leaf, as the reference row does for s 420(2).
- `pc-general.l4` reads these records for other sections: `` `punishable with death or imprisonment for life` `` (ss 115, 118, 512(1)), `` `punishable with imprisonment` `` (ss 116, 120), `` `fixed by law or carries a minimum sentence` `` (s 512(3)), and `` `punishable with imprisonment for` n `months or upwards within section 41` ``.
- The enhanced penalties of ss 73-74E (twice the maximum, and so on) are general-part's, over a `Punishment`; offence modules do not fold them in.

## 7. When the Code does not answer

`REFUSE` in a **named definition whose name is its message**, with an `@ref` above it saying why (`writing-l4-rules/references/source-patterns/11-when-the-encoding-cannot-answer.md`); `MAYBE` only where the Code itself names an absent case.
Never `FALSE`, `0`, `""` or a plausible default; never a home-made three-valued enum.
The model in `pc-general.l4` is s 41 over a punishment with no stated maximum.
A refusal is a rule's output, never a facts-record field (§3.4).

## 8. The charge

Declared once, in `pc-general.l4`: `Charge` (`section`, `offence`, `made out`, `text`, `refusal`, `punishment` — identical to the reference row's) and its builders, identical in name and wording to the reference row's `penal-code-general.l4`, so its charge texts reproduce byte for byte (asserted in `pc-general-tests.l4`).

- `` `frame the charge` (f's particulars) "N" "<offence name>" (`punishment prescribed by s N`)'s words (`offence under s N` f) (<recital> f) (<missing elements> f) `` — builds the text only when made out; otherwise the refusal names the missing elements.
- `` `frame the charge read with` p "N" (LIST "511") … `` — the same, for a charge read with further sections (abetment s 109, attempt s 511, conspiracy s 120B; FORK G-7 on the number); the `section` field becomes `"379 read with 511"`.
  Common intention (s 34) is added by `Particulars`, never by you.
- Recital depth is section-dependent (CPC s 125): recite the **manner** where the offence is one of deception, threat or breach of trust (cheating, extortion, criminal breach of trust, intimidation, forgery, false evidence); the reference row's theft and robbery builders show the short form.
- The offence name is the one the Code gives it (CPC s 123(2)): the section's heading, or the offence's name in the defining words.
- The missing-elements list uses `` `missing unless` (leaf) "<the Code's words for it>" ``, in the order the section states them, ending with the defining predicate taken together, as `` `elements of cheating not made out` `` does.
- Helpers available: `` `missing unless` ``, `` `included if` ``, `` `joined with` ``, `` `one` name description ``, `` `one person` p ``, the three pronoun functions.
- Where an offence has no natural charge (a definition-only section, a general exception, an interpretation section, a deeming rule), there is no `offence under` or `charge under` for it: say so in the coverage table.

**For the catalogue.**
For each punishing section you encode, give in your report one `OFFENCES` entry (`reference/charge-generator-catalogue.ts`): `section`, `title`, `defines`, `family`, `offenceFn`, `chargeFn`, `definitionFns`, `factsType`, `factsParam: 'f'`.
`family` is a closed union in the app; propose a new slug when your offence belongs to none of `cheating`, `theft`, `extortion`, `robbery`, `cbt`, `intimidation`, `hurt`.

## 9. Tests

- `pc-<group>-tests.l4` IMPORTs `prelude`, `pc-domain`, `pc-general` and your module(s).
- Every Illustration you can express is an `#ASSERT`, cited on the line above: `-- s 378 illus (a)`.
  An Illustration that says an offence is committed asserts `` `offence under s N` `` (and, where it quotes one, the charge's `made out`); one that says it is not asserts the `NOT`.
- Boundary cases for every threshold, age and amount — on the §3.5 helper, both sides of the line.
- Where an Illustration cannot be expressed on your atoms, say which and why in your coverage notes; do not bend the atoms to fit.
- At least one charge per family asserted **as text**, and one refusal.
- A failing assertion is a finding: never edit the expected value to match. Leave it failing and report it.
- Count with `L4=<L4_BIN> deposit/check.sh`, or grep `DiagnosticSeverity_Error` and an anchored `Message: assertion satisfied`; a failed assertion is logged twice by the unanchored grep (measured writing `pc-general-tests.l4`), so do not count `assertion failed` lines unanchored and report them as a number of assertions.
- Run only your own files while others are writing theirs.

## 10. Layout of a module

- Header comment naming the Chapters and sections covered, the source ("Penal Code 1871, 2020 Revised Edition, SSO current version as at 09 Sep 2026"), and anything the reader must know before reading.
- `§` per Chapter (or Chapter part), `§§` per section, titled with the section number and heading: `` §§ `s 379 — punishment for theft` ``.
- The section's text quoted in a comment above its rule, copied from `inputs/PC1871.txt`, with the page footers ("Singapore Statutes Online … PDF created date …") removed.
- One section, one recognisable place.
  A repealed section is a one-line comment `-- s 377A. [Repealed by …]` in its place, and a row in the coverage table.
