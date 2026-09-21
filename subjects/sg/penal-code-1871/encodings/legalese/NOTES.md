# NOTES — sg/penal-code-1871, encoding row `legalese`

**Status: `draft`.** Ten modules. Section 301 was hand-encoded on 2026-08-26 (see the end of this
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
| `theft-378-379.l4` | s 378 | ss 379, 380 | (none quoted) — s 378 Illustration (q), the bank transfer; s 380 Illustration none, and no reported charge |
| `extortion-383-384.l4` | s 383 | s 384 | Sarjit Singh Rapati v PP [2005] SGHC 28 — s 384 r/w s 34 |
| `robbery-390-392.l4` | s 390 (over theft and extortion) | ss 392, 393, 394 | Chen Weixiong Jerriek v PP [2003] SGHC 103 — s 392 r/w s 34; s 394 |
| `cbt-405-406.l4` | s 405 | s 406 | Carl Elias Moses v PP [1995] 3 SLR 748, as quoted in Viswanathan Ramachandran v PP [2003] SGHC 183 — **refused as laid** |
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
- **s 380 nests** `theft IS A Theft Facts` inside `Theft in Dwelling Facts`, for the same reason
  robbery does, and because extending `Theft Facts` would have meant editing all six
  `Theft Facts WITH` literals in the row. Woon treats s 380 as *defining* an offence ("theft in
  dwelling is defined in section 380 PC", ch. 8 p. 185); this row treats it as a punishing section
  carrying extra elements, so his `Commits Theft in dwelling` node maps to `offence under s 380`
  and **no `commits theft in dwelling` ladder exists**. The two readings agree on what must be
  proved. See the module header.
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
s 301 module).

**Of the theft family's five punishing sections, three are still not here**, and every one of them
is heavier than s 379. The filename `theft-378-379.l4` should not be read as the whole family:

| section | what it adds to theft | punishment, verbatim |
| --- | --- | --- |
| **s 379A** | theft of a motor vehicle **or** any component part of one | 7 years, "and shall also be liable to fine"; on conviction the court **shall** disqualify from holding or obtaining a driving licence, "unless the court for special reasons thinks fit to order otherwise" — discretionary to excuse, not discretionary to impose. s 379A(3) defines "motor vehicle" and "component part" |
| **s 381** | being a clerk or servant, **or** employed in that capacity, theft of property in the possession of the master or employer | 7 years, "and shall also be liable to fine" |
| **s 382** | having made preparation for causing death **or** hurt **or** restraint, **or** fear of any of those, to any person, in order to commit the theft **or** to escape after it **or** to retain what was taken | 10 years, "and shall also be punished with caning with not less than 3 strokes" — the caning is **mandatory**, not "liable to" |

None was encoded with s 380 because none is cheap in the way s 380 was. s 379A needs the
definitional subsection and a disqualification that is a sentencing order rather than an element;
s 381 needs the clerk-or-servant relation, which s 27 already touches; and s 382 is a
**two-disjunction** section of the same family as s 380 — preparation for one of six harms, for one
of three purposes — so whoever encodes it should read "The shape of s 380" in
`theft-378-379.l4` first. The evidence layer — what a fact rests on — is not encoded; it lives in the app.

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
| theft-378-379 | 31 | all satisfied |
| extortion-383-384 | 12 | all satisfied |
| robbery-390-392 | 50 | all satisfied |
| cbt-405-406 | 17 | all satisfied |
| criminal-intimidation-503-506 | 15 | all satisfied |
| hurt-321-323A | 17 | all satisfied |
| charge-sheet | 5 | all satisfied |
| culpable-homicide-301 | 8 | all satisfied |

**178 in total**, re-counted on 2026-09-21 with `grep -ch '^#ASSERT' *.l4` after s 380 added 21
(19 in `theft-378-379.l4`, 2 in `charge-sheet.l4`). It read **157** immediately before that.
The figure of 133 this file and `encoding.json` both carried before that date was wrong by one even for the row as it then stood: the same count gives **132**; it then read **149** until the s 392 implication below added eight.
Nothing in the row had moved when the 132/133 discrepancy was found; the number had simply never been re-derived.

**Anchor the grep.** The unanchored `grep -c '#ASSERT' *.l4` this line carried until 2026-09-21 gave the same answer for as long as no comment in the row named the directive. **One** comment now does — `robbery-390-392.l4:367` — so the unanchored form returns **179** for 178 assertions. The anchored form above is the one to use.

Every module round-trips `l4 format` byte-identically, re-checked on 2026-09-21 including the s 392 implication below. The whole row deploys to `jl4-service`
as one bundle (`sg-penal-code`, 10 files, 37 exports) and all 38 fixtures evaluate over HTTP to
the verdict the asserts state. **That deploy predates the s 392 implication** and has not been
re-run since; the four decisions it added are `@export`ed, so the bundle's export count is no
longer whatever 37 was counting. (For what it is worth, `grep -ch '^@export' *.l4` gives 38 now
and gave 34 before — which is not 37 either way, so the two numbers are not measuring the same
thing and this one should not be used to "correct" that one.)

`tests/` holds jl4-test goldens generated by copying the row under `jl4/examples/legal/` in an
l4-ide worktree; they are a **point-in-time record**, not a live gate — canon has no CI and the
row is not in l4-ide's corpus globs. Regenerate the same way. **The goldens were NOT regenerated
for any of the four 2026-09-21 changes below** — the s 393 addition, the s 390(2)
re-granularisation, s 392 as an implication, or s 380 — so `tests/robbery-390-392.*.golden`,
`tests/theft-378-379.*.golden` and `tests/charge-sheet.*.golden` predate them and will not match
until someone re-blesses them.
The robbery goldens cite line numbers (`robbery-390-392.l4:671:1-48:`), and every one of the
three changes moved them, so the mismatch is total rather than local.

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

## 2026-09-21 — section 380, theft in dwelling

Woon, *Essential Criminal Law* ch. 8 §8.1.1 (p. 185), gives theft in dwelling its own heading, its
own diagram and its own consequent node, and calls it "by far the most common version" of theft —
expressly covering shop theft, "because shops are generally buildings used for the custody of
property".
The row had nothing: a grep for `380` across every `.l4`, `.md` and `.json` here returned zero hits,
and `Theft Facts` had no locus field, so the offence could not even be expressed on the record.

Added, in `theft-378-379.l4` (the filename is kept, as `robbery-390-392.l4`'s was when it grew ss 393 and 394):

- the verbatim text of s 380 in the module header, two new header sections ("The shape of s 380"
  and "Why s 380 nests a theft"), and the s 380 recital note;
- `Theft in Dwelling Facts` — a `theft IS A Theft Facts` plus five booleans, `building` / `tent` /
  `vessel` / `as a human dwelling` / `for the custody of property`;
- `offence under s 380`, `the place the theft was committed in`,
  `what that place was used for`, `the recital of the theft in dwelling`,
  `elements of theft in dwelling not made out` and `charge under s 380`, exported;
- three new `Theft Facts` and seven `Theft in Dwelling Facts` fixtures, all **constructed** — the
  bench has no reported s 380 case;
- nineteen `#ASSERT`s (12 → 31).

And in `charge-sheet.l4`: a `theft in dwelling` field on `Complaint`, a `380` row in
`applicable charges` **above** the `379` row, three locus records for the existing complaints, two
new complaints, and two more asserts (3 → 5).

**Two OR-groups in series, not a flat conjunction.**
s 380 is the first section this module encodes with any disjunctive limb, and it has two:
`(building OR tent OR vessel) AND (used as a human dwelling OR used for the custody of property)`,
both conjoined with the theft.
Encoding it as a flat five-leaf conjunction would be a **wrong answer**, not a different factoring:
it would demand a building that was at once a dwelling and a store, and would refuse every shop
theft. That is measured rather than argued — rewriting the rule as a flat conjunction in a scratch
copy fails **6** of the module's assertions, `Tan Mei Ling, in the supermarket` among them.

**Every limb is pinned by an assertion that can fail.** Two further scratch mutants: fusing the
whole locus into one inert string (so s 380 becomes s 379) fails **4**; dropping the nested
`commits theft` conjunct fails **2**. The two rarest disjuncts, `tent` and `vessel`, have
constructed fixtures of their own for exactly this reason — without them an encoding that dropped
either would still have run green.

**s 380 is a punishing section here, and Woon calls it a defining one.**
p. 185 says in terms that "theft in dwelling is defined in section 380 PC", and his figure's
rightmost node reads `Commits Theft in dwelling`. This row keeps its defining/punishing split
(CPC s 123(4)): s 378 is the only section in the group that says "is said to commit", s 380 says
only "shall be punished", so `offence under s 380` is the name and **no `commits theft in dwelling`
ladder was created**. The difference is one of characterisation; nothing about what must be proved
turns on it. The module header says so in those words rather than explaining Woon's label away as
shorthand — it is not shorthand, it is his reading.

**A divergence the type does not prevent, ruled rather than fixed.**
`Complaint` now carries both `theft` and `theft in dwelling`, and the second nests a `Theft Facts`
of its own. Nothing ties the two together, so a hand-built `Complaint` whose two theft records
disagree could return s 380 without s 379 — which s 380 itself forbids, theft being an element of
theft in dwelling. The row **already** has that shape for robbery, whose `Robbery Facts` nests its
own `Theft Facts` beside the `theft` field, and it is handled the same way: every fixture supplies
the SAME named theft record to both. The alternative — five locus booleans loose on `Complaint` —
was rejected because it breaks the router's one rule, one nested facts record per offence family.
The comment on `DECLARE Complaint` records the call.

**No projection was regenerated**, and none needed to be: all eight figures come from
`robbery-390-392.l4`, which this change did not touch. There is no theft ladder in `projections/`
at all — see that README, which now says so and records why adding one is not a three-line change
to l4-ide's demo.

**Re-run over the whole row: 178 satisfied, zero failed, zero `DiagnosticSeverity_Error`**, and all
ten modules still round-trip `l4 format` byte-identically.
The binary was a snapshot taken on 2026-09-21 from a build in the `legalese/l4-ide` worktree
`l4wt/robbery-demo`, with `JL4_LIBRARY_PATH` pinned to that worktree's `jl4-core/libraries`.
It is **not** demonstrably the same build as the `3effdaaad` one named under s 390(2) above — that
worktree's HEAD had moved to `7f4eb74ca` by the time this ran, and a copied binary carries no
version string to check it against. Both runs were green; that is all the two have in common on the
record.

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
