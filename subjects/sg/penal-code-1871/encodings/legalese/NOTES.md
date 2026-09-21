# NOTES — sg/penal-code-1871, encoding row `legalese`

**Status: `draft`.** Eleven modules. Section 301 was hand-encoded on 2026-08-26 (see the end of this
file); the rest was encoded on 2026-09-17 for the **charge generator** proof of concept, by one
Claude Fable session and three Opus encoder agents working to one brief, against verbatim
statutory text from the lawplain corpus. No claim of fidelity is made, and **no human has read
the encodings yet** — Meng has said he will edit the `.l4` in place when he has time, and the
downstream (goldens, the app's fixtures, the deployed bundle) is regenerated from here.

## What it is

The row now encodes the offences a demo charge generator needs, and the **form of a charge**:

| module | defines | punishes | reported case the recital is pinned to |
| --- | --- | --- | --- |
| `penal-code-general.l4` | ss 22–25; CPC 2010 ss 123–126 (`Particulars`, `Charge`, the opening/closing words) | — | Lewis Christine (the header), Sarjit Singh (the s 34 rider) |
| `cheating-415-417-420.l4` | s 415 | ss 417, 420 | Lewis Christine v PP [2001] SGHC 113 — s 420, price-tag switch |
| `theft-378-379.l4` | s 378 | s 379 | (none quoted) — s 378 Illustration (q), the bank transfer |
| `extortion-383-384.l4` | s 383 | s 384 | Sarjit Singh Rapati v PP [2005] SGHC 28 — s 384 r/w s 34 |
| `robbery-390-392.l4` | s 390 (over theft and extortion) | ss 392, 393, 394 | Chen Weixiong Jerriek v PP [2003] SGHC 103 — s 392 r/w s 34; s 394 |
| `cbt-405-406.l4` | s 405 | s 406 | Carl Elias Moses v PP [1995] 3 SLR 748, as quoted in Viswanathan Ramachandran v PP [2003] SGHC 183 — **refused as laid** |
| `cbt-407-409.l4` | — (it uses s 405) | ss 407, 408, 409 | (none quoted) — the Carl Elias Moses entrustment in three supposed capacities; s 405 Illustrations (b) and (c) |
| `criminal-intimidation-503-506.l4` | s 503 | s 506 | Chan Yok Tuang v PP [2008] SGHC 137 — **refused** |
| `hurt-321-323A.l4` | s 321 | s 323A | Ang Boon Han v PP [2024] SGHC 221 |
| `charge-sheet.l4` | — | — | the router: `applicable charges` over one `Complaint` |
| `culpable-homicide-301.l4` | s 301 | — | (illustrations only) |

Every punishing section exports three things: a boolean `offence under s N` (the ladder), a
`charge under s N` returning a `Charge` record (the recital, or a refusal), and the defining
section's own ladder (`cheats`, `commits theft`, …). A charge is laid under the punishing section
(CPC s 123(4)), and its elements are the defining section's — the two are kept apart on purpose.

## The charge is a statutory form, and s 123(5) is the whole point

CPC 2010 s 123(5): *the fact that the charge is made is equivalent to a statement that every
legal condition required by law to constitute the offence charged was fulfilled.* So `Charge`
carries `made out`, and `text` is built ONLY when it holds; otherwise `refusal` names the
elements that are missing. Two of the seven bench cases are there to make this visible:

- **Carl Elias Moses** — the charge as laid alleged entrustment with *warrants* and
  misappropriation of the *proceeds*. `CBT Facts` has ONE `property` field read by both the
  entrustment and the misappropriation clauses, so the flawed allegation cannot be written: the
  honest answer to "misappropriated **that** property?" is FALSE and the charge is refused. The
  amended charge (entrusted with the proceeds) is framed. The module's header explains it for a
  lawyer.
- **Chan Yok Tuang** — the words "I will shoot her to death" threaten the person, not the
  reputation the charge pleaded; and the statement of facts showed no intent to alarm. With the
  facts as they were, `intent to cause alarm` is FALSE and no charge is framed.

**Recital depth is section-dependent** (CPC s 125): cheating, extortion, criminal breach of
trust and criminal intimidation recite the *manner* ("by deceiving her to believe …"); theft and
robbery do not (Illustration (a)); s 323A recites "to wit, …". The positive bench charges are
asserted **verbatim from the judgment for the body** (from "did …" to the end of the body); the
CPC s 124 header and the closing words are normalised across the row:

- "on or about 8.10 pm" → "at about 8.10 pm"; "at or about" → "at about"; "with furtherance of
  the common intention of you all" / "of you both" → "and in furtherance of the common intention
  of you all"; "Penal Code, Chapter 224" / "Cap 224, 1985 Rev Ed" → "Penal Code 1871".

## Interpretation calls

Each module records its own in a header comment beside the fixture that makes it, so a reader
finds the call next to the facts it decides. The ones worth knowing before relying on the row:

- **ss 24 and 25 are flat booleans on every offence record**, with the definition quoted in the
  field's `@desc`; they are ALSO encoded as ladders of their own in `penal-code-general.l4` and
  exported, for drill-down. They are not nested into the offence records because a call to
  another rule draws as ONE box on the caller's ladder, and the ladders exist to be clicked leaf
  by leaf (`penal-code-general.l4`, "A design call").
- **Robbery nests** `theft IS A Theft Facts` and `extortion IS AN Extortion Facts` (s 390(1): "in
  all robbery there is either theft or extortion"); the unused limb is an all-FALSE record. The
  s 390(2) harms for Chen Weixiong are classified in the module header (three calls).
- **Extortion** — two calls on Sarjit Singh, in the module header (which fear limb; the s 383
  harm kind for wrongful confinement is "body").
- **s 392's night-time limb is a sentencing provision**, not an element: the charge recites the
  same words and only `punishment` changes. **s 394** is framed on the same `Robbery Facts`.
- **Pronouns** are an enum on each facts record (`he`/`she`/`they`) because the charges say
  "by deceiving *her*", "which *she* would not have done".
- **Illustrations and Explanations are not rules.** They ride as comments and in `@desc` text
  (e.g. s 415 Explanation 1, "a dishonest concealment of facts is a deception", is the `@desc` of
  `deceived the victim`).

## What is not here

No s 109 abetment, no general attempt under s 511 (s 393, the attempt at robbery specifically, IS encoded since 2026-09-21), no CPC s 124(4) amalgamation (Song Hauming Oskar [2021]
SGHC 169, the 103-occasion Diners Club case, was on the bench for it and is not encoded), no
s 320 definition of grievous hurt (a leaf on `Hurt Facts`), no ss 299–300 (an ontology in the
s 301 module). **The criminal breach of trust family no longer belongs on this list**: ss 407, 408
and 409 were added on 2026-09-21 (see below), so the row now covers ss 405–409 entire. What is
still absent beside them is ss 403–404, dishonest misappropriation of property, which is a
different offence and not an aggravation of s 405. The evidence layer — what a fact rests on — is not encoded; it lives in the app.

## Provenance and what has been checked

Statutory text **verbatim from the lawplain `statutes` corpus** (`PC1871`, current in-force
text as at 2026-09-17, carrying the Act 21 of 2025 and Act 15 of 2019 amendment stamps) and
the CPC 2010 text from the same corpus. Judgments from lawplain `judgments`; the charges are
quoted in each module's header exactly as the judgment prints them.

Checked against the l4-ide `l4` binary built 2026-09-15 from `unstable` (`388f86059`), with
`JL4_LIBRARY_PATH` pinned to `jl4-core/libraries`:

| module | `#ASSERT` | result |
| --- | --- | --- |
| penal-code-general | 12 | all satisfied |
| cheating-415-417-420 | 11 | all satisfied |
| theft-378-379 | 12 | all satisfied |
| extortion-383-384 | 12 | all satisfied |
| robbery-390-392 | 50 | all satisfied |
| cbt-405-406 | 17 | all satisfied |
| cbt-407-409 | 32 | all satisfied |
| criminal-intimidation-503-506 | 15 | all satisfied |
| hurt-321-323A | 17 | all satisfied |
| charge-sheet | 6 | all satisfied |
| culpable-homicide-301 | 8 | all satisfied |

**192 in total**, re-counted on 2026-09-21 with `grep -ch '^#ASSERT' *.l4` after ss 407–409
landed; it read **157** for the row as it stood immediately before that.
The figure of 133 this file and `encoding.json` both carried before that date was wrong by one even for the row as it then stood: the same count gives **132**; it then read **149** until the s 392 implication below added eight.
Nothing in the row had moved when the 132/133 discrepancy was found; the number had simply never been re-derived.

**Anchor the grep.** The unanchored `grep -c '#ASSERT' *.l4` this line carried until 2026-09-21 gave the same answer for as long as no comment in the row named the directive. Two comments in `robbery-390-392.l4` do, so it over-counts. The anchored form above is the one to use.

Every module round-trips `l4 format` byte-identically, re-checked on 2026-09-21 across all
eleven, including `cbt-407-409.l4`. The whole row deploys to `jl4-service`
as one bundle (`sg-penal-code`, 10 files, 37 exports) and all 38 fixtures evaluate over HTTP to
the verdict the asserts state. **That deploy predates both the s 392 implication and ss 407–409**
and has not been re-run since; it does not even have the right number of FILES any more, the row
now being eleven. (For what it is worth, `grep -ch '^@export' *.l4` gives 44 now, gave 38 after
the s 392 implication and 34 before it — which is not 37 at any point, so the two numbers are not
measuring the same thing and this one should not be used to "correct" that one.)

`tests/` holds jl4-test goldens generated by copying the row under `jl4/examples/legal/` in an
l4-ide worktree; they are a **point-in-time record**, not a live gate — canon has no CI and the
row is not in l4-ide's corpus globs. Regenerate the same way. **The goldens were NOT regenerated
for any of the four 2026-09-21 changes below** — the s 393 addition, the s 390(2)
re-granularisation, s 392 as an implication, or ss 407–409 — so `tests/robbery-390-392.*.golden`
and `tests/charge-sheet.*.golden` predate all four and will not match until someone re-blesses
them, and there is no `tests/cbt-407-409.*.golden` at all.
The robbery goldens cite line numbers (`robbery-390-392.l4:671:1-48:`), and every one of the
first three changes moved them, so the mismatch is total rather than local.

## 2026-09-21 — section 393, attempt to commit robbery

The row already covered ss 390, 392 and 394 when this was written; what it lacked was s 393.
Added, in `robbery-390-392.l4` (the filename is kept, as it already covered s 394):

- the verbatim text of s 393 in the module header, and a fifth recorded interpretation call;
- `offence under s 393`, a one-leaf ladder over the `attempting to commit robbery` field that
  already existed for s 394;
- `the recital of the attempted robbery`, `elements of attempted robbery not made out` and
  `charge under s 393`, exported;
- two fixtures, `the handphone not taken from Ng Juin Chye Joel` and
  `Chen Weixiong Jerriek, the attempt` — **constructed, not reported**: the Chen facts with one
  leaf changed, `moves that property` set FALSE;
- sixteen `#ASSERT`s (26 → 42), and a `393` row in `charge-sheet.l4`'s router with one more
  assert (2 → 3).

**Why s 393 has a one-leaf ladder, and why no "not completed" condition was added.** The section
says only "Whoever attempts to commit robbery". That an attempt is not usually charged once the
offence is complete is a matter of how the Prosecution picks a charge, not a legal condition the
section states, and CPC s 123(5) makes the charge a claim about the conditions the section
states. Pang Khang Chau J read s 393 as a true attempt-punishing provision, unlike ss 354A, 391,
397, 459 and 460, in *Public Prosecutor v CRH* [2024] SGHC 34 at [75].

**One existing rule changed.** `the person robbed`, `the thing robbed` and
`the person robbed, spoken of` chose the theft limb or the extortion limb by asking
`theft is robbery`. On an attempt neither aggravation is made out, so that test picks the wrong
limb and the recital comes out blank. They now delegate to a new
`pleaded as a theft-robbery`, which prefers the extortion limb when its own aggravation holds
and takes the theft limb otherwise whenever a victim was named there. **Every pre-existing
assert in the row still passes**, and on all four robbery fixtures the new selector returns what
`theft is robbery` returned.

**No s 393 charge is quoted verbatim in any judgment on this row's bench**, so the s 393 recital
is derived from the s 392 one and is a fixture of this module, not an oracle — the same caveat
the s 394 recital already carried.

## 2026-09-21 — s 390(2) at Woon’s granularity

Woon, *Essential Criminal Law* ch 8 p 187 draws s 390(2) as a normalised diagram — series is AND,
parallel is OR, the offender at the left and “commits robbery” at the right.
Laid beside this module’s ladder it disagreed in two places, and on both the statutory text is on
Woon’s side, so the module moved.

**“Voluntarily” is its own conjunct.**
The text reads *“the offender, for that end, voluntarily causes or attempts to cause”*, so the
adverb stands in front of both verbs.
The module had a single `voluntarily causes` leaf in parallel with `attempts to cause`, which
leaves the attempt limb with no adverb at all — an involuntary attempt would have satisfied the
subsection.
The leaf is now split into `voluntarily`, a series conjunct, followed by a parallel choice of
`causes` or `attempts to cause`, which is exactly the shape of the three boxes on p 187.

**“Carrying away” and “attempting to carry away” are two occasions, not one.**
The text reads *“in carrying away or attempting to carry away property obtained by the theft”*,
and p 187 draws them as two parallel boxes joining at “property obtained by theft”.
The single leaf `in carrying away or attempting to carry away property obtained by the theft` is
now `in carrying away property obtained by the theft` and
`in attempting to carry away property obtained by the theft`, so the timing group has four
parallel limbs rather than three.

**What moved and what did not.**
`projections/robbery-390-2.sentences` goes from **36 ways** to satisfy s 390(2) to **48** — four
timing limbs × two of causes-or-attempts × six harms — and `robbery-390-2.svg` widens from 2846
to 2894 px.
The other five figures are byte-identical, because only s 390(2) changed.
**No answer on the bench changes, and the row still has 149 `#ASSERT`s, all satisfied.**
Every fixture has both carrying-away leaves FALSE, so splitting a FALSE OR-limb in two changes
nothing; and wherever the old fused `voluntarily causes` was TRUE, both `voluntarily` and `causes`
are TRUE, so the new series conjunct is satisfied too.
Re-run with the `l4` binary built from `legalese/l4-ide` `3effdaaad`
(branch `robbery-demo`, not `unstable`), `JL4_LIBRARY_PATH` pinned:
149 satisfied, zero failed, zero `DiagnosticSeverity_Error`, and `robbery-390-392.l4` still
round-trips `l4 format` byte-identically.

**Three field names changed**, so anything that supplies `Robbery Facts` by name has to follow:
`voluntarily causes` → `voluntarily` + `causes`, and
`in carrying away or attempting to carry away property obtained by the theft` → the two leaves
above.
`charge-sheet.l4` names none of them (it nests the whole record and reuses this module’s named
fixtures), so it needed no edit.
The charge generator app in `legalese/l4-ide` **does** name them — in
`ts-apps/charge-generator/src/lib/interview/preloads/chen-weixiong.ts`,
`…/chen-weixiong-attempt.ts` and `src/lib/fixtures/bench.json` — and was deliberately left alone
here, because that repository is not this row’s to edit.
Its preloads will fail against a bundle rebuilt from this module until they are updated.
(`src/lib/catalogue.ts` matches only on `voluntarily causes hurt`, the s 394 field, which is
untouched.)

## 2026-09-21 — s 392 as an implication, with the liability on the right

Woon's diagrams in *Essential Criminal Law* ch. 8 read left to right.
"Offender" is the leftmost box, the elements run across in series (AND) and in parallel (OR), and the **rightmost box is the conclusion** — "Commits Robbery" (p. 187).
The row's generated figures did not look like that, and the reason turns out to be a keyword rather than a drawing choice.

A `DECIDE … IF` is a **biconditional**: it says what a name MEANS.
Everything in its ladder is therefore antecedent, and the conclusion is the frame the whole picture sits inside rather than a box in it.
`projections/robbery-392.svg` shows exactly that — one leaf, `commits robbery`, behind the chapeau "Whoever", and nothing at all on the right.

`IMPLIES` is one-way, and the ladder core draws it differently: a scope on the left, a labelled seam, and the consequent on the right, ending in **two lamps**.
So s 392 is now encoded a second time, in that shape, and `projections/robbery-392-implies.txt` is the picture:

```
                                                                                          ┌─( )  complies
     392. Whoever      ┌─────────────────────────┐         ┌────────────────────────────┐ │
●──────────────────────┤ `commits robbery` OF f  │ IMPLIES │ `liable under s 392` OF f  ├─┿
                       └─────────────────────────┘         └────────────────────────────┘ │
                                                                                          └─( )  in breach
```

**Nothing was replaced.**
`offence under s 392`, the punishment string inside `charge under s 392` and all 42 of the module's previous assertions are untouched; four decisions and eight assertions were added beside them.

### Why definitions stay `DECIDE … IF` while punishment is `IMPLIES`

This is not house style — the two keywords say different things, and s 390 and s 392 want different ones.

**s 390 defines, so it is a biconditional.**
"In all robbery there is either theft or extortion" runs both ways: facts that satisfy the elements *are* robbery, and conduct that is robbery *must* satisfy them.
``DECIDE `commits robbery` f IF …`` is exactly that, and re-spelling it as an implication would throw away the converse — which is the direction a defence reads, and the direction `elements of robbery not made out` relies on when it names what is missing.

**s 392 punishes, so it is one-way.**
"Whoever commits robbery shall be punished with …" entails the liability from the robbery and says nothing in the other direction.
A person serving 4 years and 8 strokes is not thereby a robber: s 393, s 394 and many other sections prescribe sentences in that range.
Written as a biconditional the section would assert a converse the statute does not, and that converse is false.

That asymmetry is what the consequent node in Woon's diagrams encodes.
"Commits Robbery" sits at the right-hand end of the arrows and nowhere else, and the diagram gives a reader no way to run it backwards.
`IMPLIES` is the L4 keyword with that property, and it is the one s 392 now uses.

### The supplied `NOT`, which the statute does not write

s 392 states its ordinary limb **unconditionally** — "Whoever commits robbery shall be punished with [2 to 10 years and at least 6 strokes]" — and only then adds "and if the robbery is committed after 7 p.m. and before 7 a.m. [3 to 14 and at least 12]".
Read literally, both limbs attach to a night robbery.
`liable to the ordinary punishment under s 392` therefore carries a `NOT` that is **supplied, not read**: it records the settled construction that the specific provision displaces the general one.
`charge under s 392` has always made the same call, silently, inside its `IF … THEN … ELSE`; the only thing that has changed is that an inert chapeau now says so in the picture.

### What the picture says and the boolean does not

`liable under s 392` is a **tautology over these facts**, by construction: the two limbs partition on one boolean, so their disjunction is TRUE for every `Robbery Facts` there is.
That is the shape of the section rather than a slip in the encoding — s 392 attaches a punishment to every robbery and excludes none.

The consequence has to be said out loud, because a green run does not say it.
**`#ASSERT` on `whoever commits robbery shall be so punished`, and on `liable under s 392`, CANNOT FAIL.**
Three of the eight new assertions are in that class; they record the shape rather than probing it.
The five that can fail are the four limb assertions — which pin *which* punishment attaches, and each of which would flip if the night flag moved — and the `commits robbery` line of the vacuity control.

The same tautology is why the vacuity control needs two lines rather than one.
On `Chen Weixiong Jerriek, no aggravation` the implication is TRUE **vacuously**, the scope having failed; on the Chen facts it is TRUE because the rule bit and the consequent held.
In the boolean those two TRUEs are indistinguishable, and would be even if the consequent were not a tautology.
The ladder tells them apart — with the scope dark, no current leaves it and **neither lamp lights**, which `ladder-core`'s `verdictFor` reports as `NotApplicable` rather than `Complies`.
That distinction is the whole reason for drawing this section with a seam, and it is available in no other carrier this row produces.

### A silent gap in `.sentences`, found by doing this

`projections/robbery-392-implies.sentences` reads **"0 ways this can be satisfied."**
That is false about the rule and true about the tool: `expandSentences` in `ts-shared/ladder-core/src/sentences.ts` has cases for `And`, `Or` and `Not` and none for `Implies`, so an implication body falls through its `default` arm to `leafLabel`, which returns `""` for an `Implies` node, and the enumeration comes back empty.
It **fails silently** — no warning, exit 0, and a file whose text reads as a finding about the section.
The `.svg`, `.txt` and `.mmd` carriers are all fine; only this one is wrong, and only for a rule whose body is an implication, which until now no figure in this row had.
Worth an l4-ide issue.
`.mmd` is a separate matter and is **not** a defect: it flattens the seam to `sequence(scope, terminal("IMPLIES"), requirement)` on purpose, and `mermaid.ts` argues the case at the site.

## 2026-09-21 — sections 407, 408 and 409, the aggravated breach-of-trust sections

The row encoded s 405 and s 406 and stopped there.
That was a declared scope limit, but a silent one in the deployed surface: for an employee's criminal breach of trust — Woon's "very common form", and the modal real charge — `applicable charges` answered "406" and understated the maximum by eight years, with nothing in the output saying a more serious section had never been considered.
Added in a new module, `cbt-407-409.l4`.

**A sibling module, not more of `cbt-405-406.l4`.**
That file is the row's negative exhibit: its header is one long argument about one flawed charge, and its bench walks three states of that single file.
The aggravated sections ask a different question over a different record, and folding them in would bury the exhibit.
The row's filenames name their sections, so a file named for its own three is what a reader will look for.
(`robbery-390-392.l4` kept its name when ss 393 and 394 arrived because those punish the SAME facts record it already declared; these three do not.)

**Built on the s 405 node exactly as Woon draws it.**
*Essential Criminal Law* p. 196 (s 408) and p. 198 (s 409) both put a single box, "Criminal breach of trust in respect of that property", immediately before the consequent, with the capacity elements in series to its left.
`Aggravated CBT Facts` nests `breach of trust IS A CBT Facts` and every rule ends in `commits criminal breach of trust` (c's `breach of trust`) — which draws as ONE box on the caller's ladder, so the picture matches.
It is the same nesting `Robbery Facts` uses for its theft and extortion, and it means the one `property` field the Carl Elias Moses design turns on is still the one property all the way up: s 407's "in respect of SUCH property" and ss 408 and 409's "in respect of THAT property" cannot come apart from the entrustment, because there is nowhere to write a second property down.

**s 407 is encoded on the IN-FORCE text, which names no occupation.**
Before Act 15 of 2019 the section read "being entrusted with property as a carrier, wharfinger or keeper of a warehouse".
It now asks what the property was entrusted FOR — transportation for hire, or storage for rent or charge — and the carrier and the warehouse operator survive only as the section's Illustration.
The two leaves are the two purposes; the occupations ride in their `@desc`.
A ladder built on the old occupations would put the wrong question to an investigating officer.

**s 408's capacity is two leaves, because the section is two conditions.**
"Being an employee, AND being in any manner entrusted IN SUCH CAPACITY" — it is not enough that a person who happens to be an employee was entrusted.
Woon draws it as two boxes in series, and the bench separates them: `Carl Elias Moses, an employee but not entrusted as one` fails s 408 on that leaf alone and still makes out s 406.

**s 409(1)(c) carries the statutory carve-out, which Woon's figure drops.**
On p. 198 the residual limb is a bare box, "In other professional capacity", in parallel with the other two groups.
The statute writes it "in his professional capacity (**other than** by way of a trade, profession or business mentioned in paragraph (b))", and that parenthesis is what makes (c) residual rather than an overlap with (b).
The leaf is named with the exclusion and its `@desc` spells it out; a comment at the site says the encoding follows the statute and not the box.
A figure of parallel branches cannot show an exclusion without an extra node, so this is a limit of the drawing rather than a mistake in the book.

**s 409(2) and s 409(3) are definitions and avoidance of doubt, not elements.**
They ride in the `@desc` of the leaf each governs, as Illustrations do elsewhere in this row.
The two that change an answer rather than describe one are both in s 409(3): an unpaid office-holder still holds the office, and a contractual recital that no fiduciary relationship arises does not stop one arising.
s 408(2)'s extensions of "employee" work the same way.

**Woon's sub-boxes are kept.**
Paragraph (b) is two columns in series — {trade | profession | business} then {banker | merchant | factor | broker | attorney | agent} — and paragraph (g) is "key executive of a" then {corporation | unincorporated association | partnership}.
Both are inlined at that granularity rather than hidden behind a named sub-rule, so the ladder shows what the page shows.

**One breaking change to `Complaint`.**
`charge-sheet.l4`'s `breach of trust` field keeps its name and changes TYPE, from `CBT Facts` to `Aggravated CBT Facts`.
The s 406 row now reaches through two records; the three new rows read the outer one.
`applicable charges` lists **"409", "408", "407"** above **"406"** — most serious first within the family, as the header already promises — and s 406 always accompanies whichever aggravated section is made out, because every one of them is built on it.
Anything that supplies a `Complaint` by name has to follow.
Measured, the charge generator app in `legalese/l4-ide` does **not**: `grep -rn 'applicable charges\|Complaint' ts-apps/charge-generator/src/` on the `robbery-demo` worktree returns two hits, both the prose title "Complaint by Trans-Pacific Credit Pte Ltd" on an evidence card, and the app drives `charge under s 406` over a `CBT Facts` directly — a record this change does not touch.
So unlike the s 390(2) field renames, this one does not reach the app.
That repository is not this row's to edit and was again left alone.

**The recitals are constructed, not reported.**
No s 407, s 408 or s 409 charge is quoted verbatim in any judgment on this row's bench, so the three bodies are derived from the s 406 recital — capacity words, then that recital unchanged — and are fixtures of this module, NOT oracles.
The same caveat the s 393 and s 394 recitals already carry.
The capacities on the Carl Elias Moses fixtures are supposed too: the charge actually laid against him was under s 406, and nothing in the judgment says in what capacity Trans-Pacific Credit Pte Ltd entrusted him.

**Six fixtures, 32 assertions, and what they can and cannot catch.**
The fixtures are the Carl Elias Moses entrustment as an employee (s 408), as a director (s 409(1)(d)), and as an employee NOT entrusted in that capacity (the negative); Illustration (b) to s 405, the warehouse operator, for s 407's storage limb; Illustration (c), the Penang agent, for s 409(1)(b); and the same agent with the trade-profession-business column removed.
`charge-sheet.l4` gains three complaints and three assertions (3 → 6): an employee's complaint answers `LIST "408", "406"`, a director's `LIST "409", "406"`, and the employee not entrusted as one `LIST "406"`.
**No assertion in the module is a tautology, and two are weaker than they look.**
The all-dark control (`Carl Elias Moses, as charged, no aggravating capacity`) is FALSE under all three sections for two independent reasons — no capacity AND no s 405 case — so the three boolean asserts on it would not flip if only one half broke; the refusal-text assert beside them is the one that discriminates, because it requires the refusal to name BOTH rows.
And `#ASSERT `offence under s 406` (… 's `breach of trust`)` restates a fact `cbt-405-406.l4` already asserts; it is there to show that the CAPACITY is what the aggravated section adds, not to probe s 405 again.
Measured positive control, twice, on copies in the scratchpad: setting `entrusted in such capacity` TRUE on the negative fixture fails **4** of the 32, and setting `his business` TRUE on the Penang agent fixture that lacks it fails **2**.
So the s 408 second leaf and the paragraph (b) conjunction are both load-bearing.

Run with the `l4` binary built from `legalese/l4-ide` branch `robbery-demo`, `JL4_LIBRARY_PATH` pinned: **192 satisfied across the row, zero failed, zero `DiagnosticSeverity_Error`**, and all eleven modules still round-trip `l4 format` byte-identically.

## projections/

**Eight** decisions out of `robbery-390-392.l4`, four carriers each, **generated from the module
through `jl4-lsp`** and so incapable of drifting from it; plus one hand-drawn page figure that
is a second source and says so. Two of the eight, `robbery-392-implies` and
`robbery-392-liability`, were added on 2026-09-21 with the s 392 implication, and the generator
in l4-ide does not yet know about them — see the README. The full account, including how to regenerate and what each
carrier drops, is [`projections/README.md`](projections/README.md).

The carrier to read first is `projections/robbery-390-2.sentences`: **48 ways to satisfy
s 390(2)**, one per line. Four timing limbs, times two of causes-or-attempts, times six harms.
That number is the section, not the encoding. It read 36 until 2026-09-21; see
“s 390(2) at Woon’s granularity” above.

## Section 390 stated as elements, in plain English

Written out here so a criminal-law textbook's list can be laid beside it line by line.

**This list is a TRANSCRIPTION and therefore a second source.** The module is the authority and
`projections/robbery-390-2.sentences` is its generated prose; if this list and those disagree,
this list is wrong. It exists because the generated prose carries the L4's own leaf names
(`f's \`in order to commit theft\``), which is exact but is not what a reader compares against a
textbook.

**Robbery, s 390(1).** Robbery is not a third offence beside theft and extortion. It is either
of those two, with something added. So:

1. There was a theft, and s 390(2) upgrades it; **or**
2. There was an extortion, and s 390(3) upgrades it.

**When theft is robbery, s 390(2).** Every one of these must hold:

1. The accused committed theft (s 378).
2. The violence was done on one of four occasions — before the theft, in order to bring it about;
   or while the theft was being committed; or afterwards, while carrying away what had been taken;
   or afterwards, while attempting to carry away what had been taken.
3. The violence was done **for that end**, that is, for the purpose of the theft. Violence that
   merely happened to accompany a theft is not enough.
4. What was done was done **voluntarily**. The adverb governs the causing and the attempt alike.
5. The accused either actually caused the harm, or attempted to cause it.
6. The harm was one of six — death; hurt; wrongful restraint; fear of instant death; fear of
   instant hurt; fear of instant wrongful restraint.
7. It was caused to **any person**, not necessarily the person robbed.

**When extortion is robbery, s 390(3).** Every one of these must hold:

1. The accused committed extortion (s 383).
2. At the time of the extortion the accused was **present** — near enough to put the other person
   in fear of instant death, instant hurt or instant wrongful restraint (the Explanation).
3. The extortion was committed **by** putting that person in fear of one of three things —
   instant death, instant hurt, or instant wrongful restraint.
4. That feared harm was to the person put in fear, **or** to some other person.
5. By being so put in fear, that person delivered up the thing extorted **then and there**.

**Punishment and the related offences.**

- **s 392** punishes robbery: 2 to 10 years and at least 6 strokes; 3 to 14 years and at least
  12 strokes if committed after 7 p.m. and before 7 a.m. The night limb is a sentencing
  provision, **not an element** — the charge is made out and recites identical words either way.
- **s 393** punishes an attempt at robbery: 2 to 7 years and at least 6 strokes. One element,
  "attempts to commit robbery".
- **s 394** punishes hurt voluntarily caused in committing **or in attempting to commit**
  robbery: 5 to 20 years and at least 12 strokes. It reaches every person jointly concerned,
  not only the one who caused the hurt.

**Not encoded, and a textbook will have them:** s 391 gang-robbery and s 395 its punishment,
s 396 gang-robbery with murder, s 397 (deadly weapon), and ss 398–402. The row stops at the
four sections above.

The row now has a `projections/` directory; it still has no `registers/`, `report/` or `gates/`.
