---
name: scheme-console
description: Model a statute in the scheme console — add or change a scheme definition so an Act can be run forward in time with actors, acts and clocks, and its consequences traced to provisions. Use when asked to simulate a statute or scheme, add an Act to the console, build a legislative simulation, model actors and events under an Act, or work on tools/scheme-console.
---

# Adding a statute to the scheme console

The console at `tools/scheme-console/` runs a legislative scheme forward in time. **The engine
contains no statute.** Adding an Act means writing a scheme definition — data, not code — and
changing nothing else.

## Before writing anything

1. Read `tools/scheme-console/AUTHORING.md` in full. It is the vocabulary: every field, the
   four `origin` values, the operator and effect lists, the trigger types. Do not infer the
   format from `schemes.js` alone — several things that look optional are not.
2. Read the subject's own encoding under `subjects/<jurisdiction>/<subject>/` and its
   `NOTES.md`. The scheme should use the Act's own terms and the encoding's own reading of
   them, including which fork was taken where one exists.
3. Decide what the scheme is *for*. A scheme that models every section is a worse
   demonstration than one that models the provisions where time, actors or routing do the
   work. Name the scope in the scheme's `scope` field and keep to it.

## The three things to get right

**Every fact declares where it came from.** `origin` is `"birth"`, `"innate"`, `"conferred"`
(with `by` naming the act) or `"exogenous"`. This is the whole basis of simulation mode, and
it is also what makes a hole findable: a fact the corpus reads that no provision can confer.

**Never store an age.** A `"birth"` field writes a date of birth; age is computed against a
real calendar when a rule asks. Thirty-day months get "three months" and "18 years" wrong,
which is the class of error this tool exists to find.

**Nature constrains, law does not.** Simulation mode must refuse the naturally impossible and
permit the unlawful — a console that would not let you break the law can never show you an
offence. Three cases, and each is modelled differently:

| | how to model it |
| --- | --- |
| naturally impossible (a dog whelped aged ten) | `origin` handles it; write nothing |
| legally void (a shopkeeper "declaring" a dog dangerous) | give it an action, let anyone do it, write a rule that changes nothing and says why |
| prohibited but effective (an unlawful transfer) | fully available; a rule records the offence |

Do not hide a button to enforce the law. A disabled control teaches a drafter nothing.

## After writing

Run the checker and fix everything it reports before trusting any output:

```bash
node tools/scheme-console/check.js
```

It catches the failures that matter: conferred facts with no act that confers them, acts that
claim to set something and do not, declared observations no rule can reach, rules triggering
on missing actions or types, and creation exercised in both modes for every creatable type.

## Reporting what it finds

A finding the console produces is **demonstrated on stated facts, not by an `#ASSERT`**. Say
so. Promoting one into a subject's L4 modules as an assertion is a separate step and should be
offered, not assumed.

Record findings in the subject's `INCIDENTS.md`, not in the tool directory, following the
classes and status vocabulary in `CLAUDE.md`. Interpretive forks go in
`registers/fork-register.json` instead. Where a finding was first found elsewhere — in someone
else's talk, in an existing register — mark it **not discovered here** and attribute it.

A finding a simulation arrives at is better evidenced than one a scenario asserts, because an
asserted state may be one the rules could never reach. The console tags each observation with
the mode it arose in; carry that distinction into the write-up.
