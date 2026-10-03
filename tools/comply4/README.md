# Comply4

A regulatory compliance console. A regulated party answers questions about itself and its
product; Comply4 says which duties under a law arise, which are met, which are not, which fall
due later, and which cannot be settled yet — each traced to its provision and to the answers
that decided it.

Standalone. It shares nothing with `tools/scheme-console/`: that tool runs a statute forward in
time to find defects in the drafting; this one applies a law to one party's facts.

**The engine has no law in it.** A law arrives as a rule pack. The first is the ASEAN Cosmetic
Directive.

| File | What it is |
| --- | --- |
| `index.html` | The console. Loads the scripts below from the same directory. |
| `engine.js` | Three-valued rule evaluation, duty status, reasons, and a structural lint for packs. Names no law. |
| `intake.js` | Content intake: builds the prompt that asks Claude to read a piece of content, checks the reply against the pack, and merges the answers with their provenance. Names no law. |
| `laws/acd.js` | The rule pack: questions, duties, provisions, the readings taken, example products. Data. |
| `laws/acd.l4` | The same rules in L4. A working draft — see Status. |
| `laws/acd-cases.js` | Stated facts and the status each must produce. |
| `build.js` | Generates `laws/acd-cases.l4` (the cases as `#ASSERT`s) and `laws/acd-l4.js` (the L4 text the console shows). |
| `check.js` | The whole check: engine logic, pack lint, every case, then `build.js` and `l4 run`. |

## Running it

Open `index.html` in a browser. No server, no build, no network beyond a webfont. Opened
this way the questions work and content intake does not: reading content needs Claude, which
the page only has when published as a claude.ai artifact.

```bash
node tools/comply4/check.js
```

That must end `0 failed`, and its `l4:` line must show every assertion satisfied. `l4 run` exits 0
even when an assertion fails, so `check.js` counts the outcomes itself; if `l4` is not on the
PATH it says the L4 assertions were not run.

## Adding content

Besides answering questions, a user can add content: files (PDF, Word, spreadsheet, text),
photos, pasted text, or the address of a web page. For each item:

1. **The page turns it into text or images.** PDFs, Word documents and spreadsheets are read in
   the browser; a scanned PDF is sent as page images. The file itself is never stored.
2. **Claude reads it** (the artifact `sample` capability, on the viewer's own account). The
   prompt lists the pack's questions and the pack's `intake.guidance`, and asks what the content
   is, what product it concerns, and which questions the content itself answers, each with the
   evidence for it and a confidence.
3. **The reply is checked against the pack.** An answer to a question that does not exist, of
   the wrong type, naming an option the question lacks, or with no evidence is discarded.
4. **The answers are merged, marked with their source.** An answer already held — given by
   hand, or read from other content — is never overwritten; a differing reading is shown as a
   conflict for the user to settle. Removing an item removes the answers resting on it.
5. **The rules decide**, exactly as for answers typed by hand.

Claude never decides compliance. It reads; `engine.js` determines. Every answer it supplies is
shown with what it rests on and can be changed.

Web pages are opened by the Claude desktop app's own browser (`mcp` capability, server
`host:claude_browser`, tools `navigate` and `get_page_text`), which asks the viewer about each
site. Anywhere else the page says so and asks for the text or a screenshot instead.

The Annexes are still not bundled. The guidance lets Claude flag an ingredient it is confident
is on an Annex, at no more than medium confidence and saying it rests on its own knowledge;
it may never certify that a formula is clear of them.

## How a duty is decided

Every answer is yes, no or not given, and the logic is three-valued: a duty reads **needs
information** exactly when the answers so far cannot settle it, and names the questions that
would. The statuses:

| Status | Meaning |
| --- | --- |
| Not applicable | The duty does not arise on these facts. |
| Needs information | The answers given cannot settle it. |
| Met | |
| Due | Not yet done, and the time for doing it has not passed. |
| Not met | |
| Advice not followed | A "should" in the text. Never counted as a breach. |

Each duty is marked as a **duty on you** (the text binds the responsible company or person by
name) or a **condition for marketing** (the text binds Member States to keep non-conforming
products off the market, so it reaches a company through national law).

## The console and the L4 agree, by construction

`laws/acd.js` names, for every question and every duty, the L4 field or rule that says the same
thing. `build.js` takes each stated case, asks the console's engine for the status of every
duty, and writes that status as an `#ASSERT` against the L4 rules. If the two sets of rules ever
part, `l4 run laws/acd-cases.l4` reports a failed assertion and `check.js` fails.

Cases in which some duty is unsettled are left out of the L4 file: the L4 is two-valued.

## Adding a law

1. Write `laws/<id>.js` in the shape of `laws/acd.js`: groups, facts, parts, duties, each duty
   with a provision in `ref`, a paraphrase in `text`, and `metWhen`. Paraphrase; do not bundle a
   source text whose licence is not recorded.
2. Write `laws/<id>.l4` and give each fact and duty its `l4` name.
3. Write `laws/<id>-cases.js`. Aim for at least one case per duty that is not met.
4. Add the pack to `packs` in `check.js` and a `build('<id>')` line in `build.js`, and load its
   two scripts in `index.html`.
5. Run `check.js`.

## Status

**A first build, not reviewed by anyone.** In particular:

- `laws/acd.l4` is **not a canon encoding**. It has not been through the `encoding-a-subject`
  workflow, has no coverage table, fork register or independent test pass, and is not filed
  under `subjects/`. Where the ASEAN Cosmetic Directive belongs in the jurisdiction tree is
  undecided — ASEAN has no ISO 3166 code.
- The Directive was read in an unofficial text (Centre for International Law, NUS) and
  Appendix II in the Health Sciences Authority's copy. Neither is bundled; neither has a
  recorded licence. Later ASEAN Cosmetic Committee decisions were not checked.
- The Annexes are not modelled. The console asks whether a formula is within them.
- Appendices III, IV and VI are each one yes-or-no question.
- National implementing law, which is what actually binds a company and sets penalties, is out
  of scope.
- The readings taken where the text is ambiguous are listed in the pack's `observations` and on
  each duty's `reading`. They are one reader's choices.
