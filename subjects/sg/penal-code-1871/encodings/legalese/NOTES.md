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
| `misappropriation-403.l4` | s 403 (it defines and punishes in one) | s 403 | (none quoted) — s 403 Illustrations (a) and (c), Explanation 2 Illustrations (a) and (f) |
| `cbt-405-406.l4` | s 405 | s 406 | Carl Elias Moses v PP [1995] 3 SLR 748, as quoted in Viswanathan Ramachandran v PP [2003] SGHC 183 — **refused as laid** |
| `criminal-intimidation-503-506.l4` | s 503 | s 506 | Chan Yok Tuang v PP [2008] SGHC 137 — **refused** |
| `hurt-321-323A.l4` | s 321 | s 323A | Ang Boon Han v PP [2024] SGHC 221 |
| `charge-sheet.l4` | — | — | the router: `applicable charges` over one `Complaint` |
| `culpable-homicide-301.l4` | s 301 | — | (illustrations only) |

Every punishing section exports three things: a boolean `offence under s N` (the ladder), a
`charge under s N` returning a `Charge` record (the recital, or a refusal), and the defining
section's own ladder (`cheats`, `commits theft`, …). A charge is laid under the punishing section
(CPC s 123(4)), and its elements are the defining section's — the two are kept apart on purpose.

**s 403 is the one exception, and it is the statute's doing, not a shortcut.** It defines and
punishes in a single sentence, and — unlike s 378 ("is said to commit theft") and s 405 ("commits
'criminal breach of trust'") — it never names an offence for a separate section to reach. So
`misappropriation-403.l4` exports TWO things: `offence under s 403`, which IS the defining ladder,
and `charge under s 403`. There is deliberately no `commits dishonest misappropriation` wrapper;
a wrapper would draw as one box and would be named after the section's heading rather than its
enacting words.

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
- **s 403 takes `movable property`, which is NARROWER than the `property` of ss 404 and 405.**
  s 22 defines the two separately, and 2019 widened "property" (things in action, other intangible
  or incorporeal property, virtual currency) without touching "movable property". Do not build
  `Misappropriation Facts` by copying `CBT Facts`: it would import the wide gloss AND the two
  entrustment leaves, which s 403 does not have. An entrustment leaf carried across would be FALSE
  in every finder case in Explanation 2 and would silently refuse charges that ought to frame.
- **Illustrations and Explanations are not rules.** They ride as comments and in `@desc` text
  (e.g. s 415 Explanation 1, "a dishonest concealment of facts is a deception", is the `@desc` of
  `deceived the victim`).

## What is not here

No s 404 (dishonest misappropriation of property possessed by a deceased person), no ss 407–409
(criminal breach of trust of property entrusted for transportation or storage; by employees; and by a
public servant, banker, merchant, agent, director, officer, partner, key executive or fiduciary),
no s 109 abetment, no general attempt under s 511 (s 393, the attempt at robbery specifically, IS encoded since 2026-09-21), no CPC s 124(4) amalgamation (Song Hauming Oskar [2021]
SGHC 169, the 103-occasion Diners Club case, was on the bench for it and is not encoded), no
s 320 definition of grievous hurt (a leaf on `Hurt Facts`), no ss 299–300 (an ontology in the
s 301 module). The evidence layer — what a fact rests on — is not encoded; it lives in the app.

## Provenance and what has been checked

Statutory text **verbatim from the lawplain `statutes` corpus** (`PC1871`, current in-force
text as at 2026-09-17, carrying the Act 21 of 2025 and Act 15 of 2019 amendment stamps) and
the CPC 2010 text from the same corpus. Judgments from lawplain `judgments`; the charges are
quoted in each module's header exactly as the judgment prints them.

Checked on 2026-09-21 against the l4-ide `l4` binary built from the `robbery-demo` branch (the
same binary the s 403 work used, not one built from `unstable`), with `JL4_LIBRARY_PATH` pinned
to `jl4-core/libraries`:

| module | `#ASSERT` | result |
| --- | --- | --- |
| penal-code-general | 12 | all satisfied |
| cheating-415-417-420 | 11 | all satisfied |
| theft-378-379 | 12 | all satisfied |
| extortion-383-384 | 12 | all satisfied |
| robbery-390-392 | 50 | all satisfied |
| misappropriation-403 | 21 | all satisfied |
| cbt-405-406 | 17 | all satisfied |
| criminal-intimidation-503-506 | 15 | all satisfied |
| hurt-321-323A | 17 | all satisfied |
| charge-sheet | 5 | all satisfied |
| culpable-homicide-301 | 8 | all satisfied |

**180 in total**, counted on 2026-09-21 with `grep -ch '^#ASSERT' *.l4`.
The figure of 133 this file and `encoding.json` both carried before that date was wrong by one even for the row as it then stood: the same count gives **132**; it then read **149** until the s 392 implication added eight, and **157** until s 403 added twenty-one and the s 403 router rows added two.
Nothing in the row had moved when the 132/133 discrepancy was found; the number had simply never been re-derived.

**Anchor the grep.** The unanchored `grep -c '#ASSERT' *.l4` gives **181** for 180 assertions, because exactly one comment line names the directive in prose (`robbery-390-392.l4:367`). The anchored form above is the one to use.

Every module round-trips `l4 format` byte-identically, re-checked on 2026-09-21 across all eleven modules including `misappropriation-403.l4`. The whole row deploys to `jl4-service`
as one bundle (`sg-penal-code`, 10 files, 37 exports) and all 38 fixtures evaluate over HTTP to
the verdict the asserts state. **That deploy predates the s 392 implication AND s 403** and has not been
re-run since; it is a ten-file bundle and the row now has eleven modules, so it cannot answer about
s 403 at all. (For what it is worth, `grep -ch '^@export' *.l4` gives 40 now, gave 38 before s 403
and 34 before the s 392 implication — which is not 37 at any point, so the two numbers are not
measuring the same thing and this one should not be used to "correct" that one.)

`tests/` holds jl4-test goldens generated by copying the row under `jl4/examples/legal/` in an
l4-ide worktree; they are a **point-in-time record**, not a live gate — canon has no CI and the
row is not in l4-ide's corpus globs. Regenerate the same way. **The goldens were NOT regenerated
for any of the four 2026-09-21 changes below** — the s 393 addition, the s 390(2)
re-granularisation, s 392 as an implication, or s 403 — so `tests/robbery-390-392.*.golden` and
`tests/charge-sheet.*.golden` predate all four and will not match until someone re-blesses them.
The robbery goldens cite line numbers (`robbery-390-392.l4:671:1-48:`), and every one of the
first three changes moved them, so the mismatch is total rather than local.
`misappropriation-403.l4` has **no goldens at all** — four files are owed under `tests/` when the
row is next re-blessed, on the four-per-module pattern.

## 2026-09-21 — section 403, criminal misappropriation

Added `misappropriation-403.l4`, from Woon, *Essential Criminal Law* ch 8 p 189, where s 403 is
drawn as four boxes: `Dishonestly` in series into a parallel pair `Misappropriates` /
`Converts to own use`, rejoining into `Movable property`, feeding the consequent.
That is exactly the section's operative words with nothing invented and nothing dropped, so the
ladder is his diagram: `dishonestly AND (misappropriates OR converts to his own use) AND movable
property`, three elements and one disjunction.
Twenty-one `#ASSERT`s, nine fixtures, and two exports.

**Why two exports and not three.**
s 403 defines and punishes in one sentence and never says "is said to commit", so there is no
named offence for a wrapper rule to carry — see the exception recorded under "What it is" above.
Woon's rightmost box reads "Commits Dishonest misappropriation", but that wording is the section's
heading rather than its enacting words, and it is there to keep his chapter's diagrams uniform.

**The adverb is in SERIES, and one fixture exists to prove it.**
"Whoever dishonestly misappropriates or converts to his own use" puts the adverb in front of both
verbs, so it governs the conversion branch too.
The tempting alternative — dishonesty attached to `misappropriates`, `converts to his own use` left
bare — is a wrong-answer defect, not a factoring preference.
`the umbrella sold before the mistake was discovered` is the record that catches it: both act
leaves TRUE, the adverb FALSE, offence FALSE.
Measured by mutation on 2026-09-21: re-factoring the ladder that way turns two of the twenty-one
assertions red, and no other fixture in the module notices.

**Two traps, both recorded in the module header.**
The object is `movable property` (s 22, the NARROW term — everything except land, benefits to arise
out of land, and things attached to or permanently fastened to the earth), not the `property` of
ss 404 and 405.
And there is **no entrustment element**: s 403 is s 405's first limb minus entrustment, with "that
property" relaxed to "movable property", which makes `cbt-405-406.l4` the obvious template and the
wrong one.
Carrying an entrustment leaf across would be FALSE in every finder case in Explanation 2 — the
bulk of this section's illustrations — and would silently refuse charges that ought to frame.

**Explanation 2 hides a bracketing fork, and it is not settled.**
The guilt clause reads "…if he appropriates it to his own use, when he knows or has the means of
discovering the owner, or before he has used reasonable means to discover and give notice to the
owner, and has kept the property a reasonable time to enable the owner to claim it."

| reading | bracketing |
| --- | --- |
| 1 | `(knows or has the means) OR before (reasonable means AND reasonable time)` |
| 2 | `((knows or has the means) OR before-reasonable-means) AND before-reasonable-time` |

| the finder | reading 1 | reading 2 |
| --- | --- | --- |
| knows the owner; appropriates the same afternoon, having kept the property no reasonable time | guilty | guilty |
| knows the owner; HAS kept the property a reasonable time; then appropriates it | guilty | **not guilty** |

**Reading 1 is preferred, and the argument is from Illustrations (d), (e) and (g) only.**
Each states guilt FLATLY although the finder may well have held the property a while — (d) "but
afterwards appropriates it", (e) "afterwards discovers that it belongs to Z", (g) "retains the
money and appropriates it".
On reading 1 the knows-or-has-the-means limb decides all three by itself and timing never arises;
on reading 2 each turns on a timing fact the illustration does not supply.
An illustration that states guilt flatly is poor evidence for a construction that makes guilt
conditional on something it is silent about.

**Illustrations (b) and (f) are NOT the argument**, although they are the vivid pair and the
obvious ones to reach for.
Work reading 2 through them: in (b) the finder knows the owner from the letter and appropriates at
once, so both conjuncts hold and he is guilty; in (f) the ring is sold immediately without any
attempt to find the owner, so both conjuncts hold and he is guilty.
Reading 2 convicts in both and agrees with reading 1 in both — they discriminate nothing.
Every timing-bearing illustration to Explanation 2 has the finder appropriating quickly, which is
why the preference has to rest on (d), (e) and (g).

**Where the reading lives.**
The row's convention keeps Explanations in `@desc` text rather than in rules, so the fork is **not
mechanically encoded**: it is carried in the `dishonestly` input of one fixture,
`the purse kept a reasonable time`, and in the assertion over it.
A ruling for reading 2 flips that one boolean and nothing else — not the ladder, not another
fixture, not the charge builder.
**OPEN FOR MENG.**

**Also open for Meng: the recital depth.**
CPC s 125 makes it section-dependent and s 403 sits between the row's two groups — no manner limbs
of the s 405 kind (which argues for the bare theft treatment, s 125 Illustration (a)), but two
distinct named acts, and a charge that does not say which is alleged leaves the accused guessing.
The module takes the middle and recites the verb or verbs that are TRUE:
`did dishonestly misappropriate movable property, to wit, <the property>`.
**CONSTRUCTED, NOT REPORTED** — no s 403 charge is on this row's bench, so it is a fixture of the
encoding and not an oracle.

**Misappropriation and conversion are not equals, and the ladder does not say so.**
In *Wong Seng Kwan v PP* [2012] SGHC 81 at [42]–[46] the High Court took the view that the two
terms mean different things; Chong J at [46] put conversion as a **subset** of misappropriation,
since conversion additionally requires acting in a manner inconsistent with the rights of the true
owner.
Both leaves are kept, because both words are in the section; the entailment is doctrine, not
statutory words, and hard-wiring it would over-constrain a fact-finder the section leaves free.
Two consequences: the OR is doctrinally redundant (an OR is indifferent to a subset relation among
its disjuncts, so no answer moves either way), and `converts` TRUE with `misappropriates` FALSE is
a combination the doctrine says should not arise.
The ladder admits it, and `the horse, on the conversion limb alone` probes it on purpose — labelled
in the module as a probe of the encoding rather than as a case.

**`charge-sheet.l4` gained three things.**
A `misappropriation IS A \`Misappropriation Facts\`` field on `Complaint` (placed beside
`breach of trust`, the family it belongs to); an `IMPORT`; and a `"403"` row in `applicable charges`
**after `"406"`**.
That placement is the router's stated rule, most serious first within each family — s 406 carries
up to 7 years and s 403 up to 2 — and NOT a section-number rule, which would put 403 first.
The list has never been in section order anyway: `"394"` precedes `"392"` and `"420"` precedes
`"417"`.
**No implication row is owed between `"379"` and `"403"`.**
The 394/392/379 rows overlap because s 390(1) says in terms that in all robbery there is either
theft or extortion; nothing of the kind ties theft to misappropriation.
They are alternatives, not a hierarchy.

**The dangling forward reference is now discharged.**
`theft-378-379.l4:151` has always told the reader that a ring lying on the high road "is in
nobody's possession, so there is nothing to take it out of — that is misappropriation, not theft",
pointing at a section the row did not encode.
Two new router fixtures make the boundary executable: `the ring found on the high road`
(s 378 Illustration (g) beside s 403 Explanation 2 Illustration (f) — the statute's own pairing,
since s 378 Illustration (g) cross-refers to criminal misappropriation in terms) returns exactly
`LIST "403"`, and `the dollar found on the high road` (Explanation 2 Illustration (a), the finder
who merely picks it up) returns **`EMPTY`**.
That second one is the router's first vacuity control: until now every assertion over
`applicable charges` named at least one section, so a router that over-reported would have been
caught and one that reported spuriously on empty facts would not.

**What this did NOT change.**
Every pre-existing assertion in the row still passes, and no answer on the bench moves.
The three existing `Complaint` fixtures each gained `misappropriation IS \`no misappropriation\``,
an all-FALSE record, so their charge lists are unchanged.
Nothing under `ts-apps/charge-generator/src` in `legalese/l4-ide` constructs a `Complaint`
field-by-field — checked on 2026-09-21, the only two occurrences of the word there are inside
prose strings in the Carl Elias Moses preloads — so the new field breaks no preload.

**What is not encoded.**
s 404 (dishonest misappropriation of property possessed by a deceased person at the time of his
death), which is s 403's sibling and reaches `property` of any kind; and ss 407–409, the aggravated
criminal breach of trust sections.
Explanation 2's good-faith limb ("it is sufficient if, at the time of appropriating it, he does not
believe it to be his own property, or in good faith believe that the real owner cannot be found")
rides in the `dishonestly` `@desc` and is not a leaf, on the same convention that keeps the rest of
Explanation 2 out of the ladder.

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
