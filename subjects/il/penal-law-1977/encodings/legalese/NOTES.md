# NOTES — Penal Law 5737-1977, robbery (Hebrew-canonical encoding)

**Status 2026-09-21: draft, one module, unreviewed by a Hebrew-reading lawyer.**
This row encodes five sections of the Israeli Penal Law and nothing else.
It was built to stand beside `sg/penal-code-1871`'s `robbery-390-392.l4` so that the same crime can be read in two codes at once.

## What is here

| file | what it is |
| --- | --- |
| `robbery.l4` | the encoding — Hebrew identifiers, Hebrew `@nlg` heralds, English `@nlg:en` heralds, 13 fact patterns and 65 assertions |
| `projections/robbery-nlg-he.txt` | `l4 nlg --lang he` |
| `projections/robbery-nlg-en.txt` | `l4 nlg --lang en` |
| `projections/robbery-he.html` | `l4 render --lang he --format html` |
| `projections/robbery-en.html` | `l4 render --lang en --format html` |
| `encoding.json` | the row descriptor |

Source terms are recorded once, at the subject level, in `../../source/SOURCE-LICENSE.md`, and are **open**.
Read that file before deriving anything from this row.
It has two questions rather than one, because the consolidated text was read from a Wikisource volunteer project and not from an official publisher.

## Section numbers, as found in the deposited wikitext

Every number below was read from `../../source/penal-law-1977.wikitext`, revision 3023424, at the line given.
The brief that commissioned this row guessed at the numbering; the numbering here is what the text says.

| § | Hebrew rubric | line | what it does |
| --- | --- | --- | --- |
| Part XI | פרק י״א: פגיעות ברכוש | 2821 | offences against property |
| ch. א׳ | סימן א׳: גניבה | 2822 | theft |
| 383 | גניבה – מהי | 2824 | what theft is: (a)(1) taking and carrying away, (a)(2) conversion by a lawful possessor, (c) the extended definitions |
| 384 | דין הגונב | 2839 | the penalty for theft — three years, subject to any other penalty prescribed by reason of the circumstances |
| ch. ג׳ | סימן ג׳: שוד | 2914 | robbery |
| 402(א) | שוד | 2917 | robbery — fourteen years |
| 402(ב) | — | 2918 | aggravated robbery — twenty years |
| 403 | נסיון שוד | 2921 | assault for the purpose of robbery — seven years, or twenty in s 402(b) circumstances |
| 404 | דרישת נכס באיומים | 2924 | demanding property by threats — five years, or ten if carrying a weapon |

One near miss worth recording, because a search for שוד finds it first: **s 169, שוד ים, is piracy**, not robbery, and sits in a different Part.
It is not encoded here.

## What is encoded

`גונב דבר` — s 383(a), both limbs.
`הרי זה שוד` — s 402(a), as four cumulative conditions each of which is itself a choice: the theft, the timing, the act, the purpose.
`נסיבות סעיף 402(ב)` — the three aggravating circumstances, standing alone.
`שוד בנסיבות מחמירות` — s 402(b), which is `הרי זה שוד` and one of those three.
`תקיפה לשם שוד` — s 403.
`דרישת נכס באיומים` — s 404.
`העונש המרבי בשנות מאסר` — the maximum term, over all five sections.
`הסעיף שלפיו יוגש כתב האישום` — which section the charge would be laid under.

The last two are ordered most-serious-first, and that order is not arbitrary.
The closing words of s 384 say the three years apply *"if no other penalty has been prescribed for the theft by reason of its circumstances"*, so theft is residual by its own terms and goes last.

## Interpretive choices

Each of these is a call this encoding made.
None of them has been reviewed by anyone who practises Israeli criminal law.

**F1. The s 402(b) circumstances are split out into a rule of their own.**
s 402(b) is written as attributes of "the robber", which presupposes a robbery.
But s 403 sends the reader to *"נסיבות כאמור בסעיף 402(ב)"* in a case where no robbery was completed.
So the three circumstances have to be nameable without a robbery attached, and they are.

**F2. Violence used only to get away is not robbery under this encoding.**
This is the sharpest finding, and it is asserted as a fixture (`אלימות להימלטות בלבד`).
s 402(a) reaches violence *"immediately after"* the theft, so the timing limb is satisfied.
But the purposes it names are a closed list of three — to obtain the thing, to retain it, or to prevent or overcome resistance to the theft — and violence used purely to escape arrest, with the thing already secure, matches none of them.
The result is theft at three years, not robbery at fourteen.
Contrast the fixture immediately above it, where the same post-taking violence is used *to retain the thing* and is robbery.

**F3. A threat alone is enough, but only with a completed theft.**
s 402(a) says *"מבצע או מאיים לבצע"*, so threatened violence satisfies the act limb.
It does not dispense with the opening words *"הגונב דבר"*.
A threat that produces nothing is s 404, not s 402, and the fixture `דרישה מאוימת שלא נענתה` asserts that.

**F4. The s 383(c) extended definitions ride on the leaf, not beside it.**
s 383(c)(1) says a taking includes obtaining possession by trick or **by intimidation**; (c)(2) says carrying includes moving the thing from its place.
Those are written into the `@desc` of `נטילה` and `נשיאה` rather than lifted into leaves of their own.
A consequence the encoding does not resolve, because the statute does not either: where possession was obtained *by intimidation*, the same threat can satisfy both the taking under s 383(c)(1)(b) and the violence limb of s 402(a).

**F5. "בחבורה" is left unquantified.**
The statute names no minimum number and this encoding adds none.

**F6. A case outside all five sections refuses; it does not score zero.**
`העונש המרבי בשנות מאסר` ends in `REFUSE`, because the Act has 651 sections and this row encodes five of them.
Zero years would be a false answer dressed as a computed one.

**F7. Every figure is a maximum.**
These sections prescribe maximum terms and no minima, so the number this encoding returns is a ceiling, never a sentence.
That differs from Singapore, where s 392 and s 394 carry floors and mandatory caning.

## What is NOT encoded

The general part in its entirety — attempt (ss 25–27), parties to an offence, and the criminal-responsibility chapter Amendment 39 of 1994 replaced.
s 383(b), the corporate-officer clause.
s 384א, aggravated theft by the kind or value of the thing.
ss 385–401, the remaining theft-adjacent offences, including theft by a public servant (s 390 of this Act, which despite the number is not robbery) and theft by an employee (s 391).
ss 405–409, burglary and housebreaking, which sit in the sub-chapter immediately after robbery.
s 169, piracy.
Sentencing law, forfeiture, and anything procedural.

There is no `cases/` directory and no reported judgment is pinned to any fixture.
The thirteen fact patterns are constructed, not reported, and are fixtures of this module rather than an oracle.

## Element-by-element: Israel s 402 against Singapore s 390

**This table is one reading, by the session that wrote this encoding, and has been reviewed by nobody.**
The Singapore text is quoted from `subjects/sg/penal-code-1871/encodings/legalese/robbery-390-392.l4`, which quotes it from Singapore Statutes Online.
The Israeli text is quoted from the deposit in `../../source/`.

| element | Israel, s 402 | Singapore, s 390 |
| --- | --- | --- |
| base offence | theft only, s 383 | theft **or** extortion — s 390(1), "in all robbery there is either theft or extortion" |
| timing | "at the time of the act, or immediately before or after it" | "in order to commit theft, or in committing the theft, or in carrying away or attempting to carry away property obtained by the theft" |
| conduct | commits **or threatens to commit** an act of violence | "voluntarily causes or attempts to cause" — a threat reaches robbery only through the *fear* harms below |
| object of the violence | "against a person **or property**" | any *person* only; property is never the object |
| the harms | not enumerated — "an act of violence", left open | six, enumerated: death, hurt, wrongful restraint, fear of instant death, of instant hurt, of instant wrongful restraint |
| purposive link | three named purposes: to obtain the stolen thing, to retain it, or to prevent or overcome resistance to the theft | two words — "for that end" — carrying the same work |
| extortion limb | none; a demand by threats is a separate offence at s 404 | s 390(3), requiring presence, fear of *instant* harm, and delivery "then and there" |
| aggravation | s 402(b): armed, in company, or wounded/struck/other violence to the body → twenty years | s 392: committed between 7 p.m. and 7 a.m. → a higher range; s 394: hurt caused → a separate offence |
| incomplete offence | s 403: assault for the purpose of robbery — seven years, twenty in s 402(b) circumstances | s 394 reaches an attempted robbery; s 392 does not |
| penalty | fourteen years maximum, twenty if aggravated; no minimum, no caning | s 392: two to ten years and caning of not less than six strokes; three to fourteen and twelve strokes at night |

Four differences seem to us worth arguing about, in descending order of how much they change an answer.

1. **Singapore's robbery can be an extortion; Israel's cannot.**
   This is the largest structural gap, and it is why the Singapore module nests two records while this one nests none.
   Israel routes the extortionate case to s 404 at five years, against Singapore's robbery range.
2. **Israel's violence may be against property; Singapore's may not.**
   Smashing a display case to reach the thing is within s 402(a) and is asserted here as `אלימות בנכס כדי להשיג את הדבר`.
   On the Singapore text the same facts are theft, unless a person was also put in fear.
3. **Israel names three purposes where Singapore says "for that end".**
   A closed list is narrower than an open phrase, which is what produces F2 above.
   Whether a Singapore court would reach the escaping thief through "carrying away … for that end" is a question this table cannot settle.
4. **Israel enumerates no harms.**
   "An act of violence" carries everything Singapore's six harms carry and, on its face, more.

## Reproducing the four renders

The binary must be at least as new as the corpus it reads.
The four files in `projections/` were produced by an `l4` built from `legalese/l4-ide` at `ff5358620` (2026-09-21), a commit on the `unstable` line that carries both `l4 nlg --lang` and `l4 render --lang`.
They were also produced independently by a second binary, built at `7af775364` with in-flight lexer changes on top, and the four files came out byte-identical, so nothing here depends on that branch.

```bash
cd subjects/il/penal-law-1977/encodings/legalese
export JL4_LIBRARY_PATH=<l4-ide-worktree>/jl4-core/libraries
l4 run robbery.l4
l4 nlg    --lang en             robbery.l4 -o projections/robbery-nlg-en.txt
l4 nlg    --lang he             robbery.l4 -o projections/robbery-nlg-he.txt
l4 render --lang en --format html robbery.l4 -o projections/robbery-en.html
l4 render --lang he --format html robbery.l4 -o projections/robbery-he.html
```

**`l4 nlg` with no `--lang` prints Hebrew, not English.**
The module declares `@lang he`, which makes the untagged herald the module's default rendering, and the default is what a bare run selects.
So the English projection is produced by `--lang en` and not by omitting the flag.

## Things a reader should not be surprised by

**The linearizer's own connective vocabulary stays English in both renderings.**
"with", "is equal to" and "not" are the frame the linearizer puts around a herald, and a language tag names the herald rather than the frame.
The Hebrew projection therefore reads as Hebrew clauses joined by English joints.

**Field heralds do not reach either projection.**
An `@nlg` on a record field is carried in the source and is dropped by both `l4 nlg` and `l4 render`, which print the field's type instead.
So this module puts the gloss of each leaf in `@desc`, bilingually, where it reaches the OpenAPI and MCP schemas.
The open ruling behind this is recorded in `legalese/l4-ide` at `specs/todo/MULTILINGUAL-NLG-SPEC.md` §6.2.

**The HTML documents open with `<html lang="en">` in both cases.**
That attribute is hard-coded by the renderer and is wrong for the Hebrew document.
Nothing in the page sets `dir="rtl"` either, so the Hebrew renders left-to-right at the block level and relies on the browser's bidi algorithm inside each line.

**No bidi control marks appear anywhere in the source.**
L4 rejects RLM and LRM inside backticks, so a Hebrew module cannot embed the marks an editor would want for clean display.
This is a known hard limit, not an oversight.

**The projections are a point-in-time record.**
canon runs no CI, and this module is outside `l4-ide`'s corpus globs, so nothing regenerates them when the printer changes.
Re-run the commands above before trusting a file in `projections/`.
