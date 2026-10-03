# Scheme console

A day-stepped simulation of a legislative scheme. Lay the actors out, bring new ones into
existence, click one, tell it to do something, and watch what the statute does about it —
with every consequence traced to the provision that produced it.

**The console has no statute in it.** The kinds of actor, what it takes to bring one into
existence, the actions, the consequences, the clocks and the things worth counting all arrive
as a scheme definition. Two statutes run on the same engine here; a third is a third object
in `schemes.js` and no change to the engine.

| File | What it is |
| --- | --- |
| `engine.js` | The engine. A fact base, a small expression language, a forward-chaining rule pass, and a calendar. Names no statute — grep it. |
| `schemes.js` | Two scheme definitions: Dog Act 1976 (WA) and Retail Barring Orders Bill 2025 (WA). Data, not code. |
| `index.html` | The console: canvas, inspector, event log, observation counters. |
| `check.js` | Correctness pass. Run it after changing a scheme. |
| `AUTHORING.md` | **How to write a scheme.** Read this before adding one. |

## Running it

Open `index.html` in a browser — it loads `engine.js` and `schemes.js` from the same
directory and needs no server, no build and no network beyond a webfont.

```bash
node tools/scheme-console/check.js     # headless: every scenario, both modes, all structure, a generated year
```

## Three modes

One toggle in the toolbar: **Scenarios**, **Simulation**, **Discussion**.

**Scenarios** — you write the events. Two ways, switched beside the clock:

- **God mode** — you may set any fact, including an age. This is how you set up a case to
  demonstrate. Findings reached this way are worth less as evidence, because a state you
  assert may be one the rules could never reach.
- **Nature mode** — only what could really happen. Actors are born at nought, age is worked
  out from a date of birth against a real calendar, and every other fact has to be conferred
  by somebody's act. The creation form shows the conferred facts greyed out, naming the act
  that would confer each one.

**+ New scenario** starts with nobody and records everything you do as steps; save it and it
joins the list, marked "yours".

**Simulation** — the app writes the events itself, from the scheme's `simulation` section:
parameters you set (pups per month, the share of owners who comply, attacks per dog per
year…) and generators that make things happen at those rates, always through somebody's act,
so a generated run obeys every rule and counts as Nature mode. Play, pause and a speed slider
move the clock; a seed makes a run repeatable; a run can start from a scenario and be saved
as one. Every default rate is illustrative.

**Discussion** — talk to Claude about the law on screen. It opens with the ten-stage process
and the two human gates the law went through, then answers from the scheme, the text and the
L4 together. The console only shows laws encoded in L4: it has no way to add a law, because
the real process cannot run inside it.

**Your review.** Anyone can record a verdict on an incident and save scenarios of their own. Where
the page cannot write them to its database (anyone but its owner, on a personal plan), they stay on
the page until it closes. **Export**, under Incidents, saves the verdicts, notes and scenarios for
the law on screen as a JSON file; **Import** loads one back. This is how a legal drafter keeps
their review of a console handed to them.

The line is **what does the constraining**: nature, not law. Nature mode refuses the
impossible and permits the unlawful, because a console that would not let you break the law
could never show you an offence. A third case sits between: an act by somebody with no power
to do it is allowed, and does nothing at all. All three are demonstrated in the Dog Act
scheme — a dog cannot be whelped aged ten, a shopkeeper may purport to declare a dog
dangerous and achieve nothing, and a restricted breed pup may be handed over in a transfer
that is both effective and a crime.

## Adding an Act you have encoded

An Act encoded in L4 here reaches the console in five steps. The first is yours; Claude Code
does the rest when asked ("add <subject> to the console").

1. **Encode it** under `subjects/<jurisdiction>/<subject>/`, as usual: the `.l4` modules with
   `@ref` on each rule, the source text in `sources/` (or `registers/source-bundle/`), and a
   `SOURCE-LICENSE.md` saying whose text it is and on what terms. Findings go in `INCIDENTS.md`.
2. **Write its scheme** in `schemes.js`, using the `scheme-console` skill and `AUTHORING.md`:
   actor types, actions and rules taken from the encoding's reading of the Act, observations
   with `ref`s pointing at `INCIDENTS.md`, scenarios that demonstrate each finding, and a
   `simulation` section with parameters, defaults and generators. Scope it to where clocks and
   actors do the work, and say so in `scope`.
3. **Add it to `bundle.js`**: the subject folder, where its L4 lives, and its text files. Give a
   text its `licence` line only if the licence is recorded — the published console is shared by
   link, so bundling a text publishes it. Then run `node tools/scheme-console/bundle.js`, which
   writes `corpus/<scheme id>.json`.
4. **Check it**: `node tools/scheme-console/check.js` must report no problems, including the
   generated year and the saved-run replay.
5. **Publish** the console with `corpus/` alongside the page. The law appears under "Encoded in
   L4" in all three modes. In Discussion, Claude reads the scheme, the text and the L4 together; for
   an Act too large to send whole, it sends the sections the question names, then the sections
   the scheme cites, and the modules that encode them.

Re-run steps 3 to 5 whenever the encoding or the text changes, so the console never quotes a
stale encoding.

## Status

**A demonstration artifact, not part of the pipeline.** Nothing it produces has been through
a machine check in this corpus: a finding demonstrated here is demonstrated on stated facts,
not by an `#ASSERT`, and turning one into an assertion in the subject's own modules is a
separate step. Neither scheme is a complete model of its Act; each covers the provisions named
in its `scope`, which is enough to show the method and not enough to advise anyone.

Findings it has produced are recorded in the relevant subject's `INCIDENTS.md`, not here. See
`subjects/western-australia/dog-act-1976/INCIDENTS.md`.

## Known limits

- The expression language is deliberately small — booleans, comparisons, arithmetic,
  relationship lookups, named definitions, calendar ages and a day counter. It can be grown
  without rewriting any scheme.
- A scheme is hand-written JSON-in-JS. The product version wants an authoring front end;
  Oracle Policy Modeling's Word-document rules are the model to beat.
- `schemes.js` holds every statute in one file. Once there are more than a few, split it so
  each Act's scheme sits beside its own encoding in `subjects/`.
- The texts of the Retail Barring Orders Bill and the Rent Cap Bill are not bundled: their
  subjects record where each print came from but not its licence. Add a `licence` line in
  `bundle.js` once that is settled.
- The Retail Barring Orders scheme declares no conferred facts: orders, service and
  cancellation are attributes smeared across the respondent rather than a `matter` actor with
  state of its own. Fixing that is the natural next piece of work, and would make the
  provenance checks bite on that scheme too.
