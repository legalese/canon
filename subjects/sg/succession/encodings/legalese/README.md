# What happens after a death in Singapore

An executable encoding of three Acts, read together as they are actually read — by a family
asking *"what happens now?"*:

| Act                                   | the question it answers here              |
| ------------------------------------- | ----------------------------------------- |
| **Wills Act 1838**                    | is there a valid, unrevoked will?         |
| **Probate and Administration Act 1934** | who administers, what comes off the top, and when? |
| **Intestate Succession Act 1967**     | who takes what is left, and in what shares? |

## Why three Acts are one subject

They are three views of one event and they share their nouns. The same person is the PAA's
"deceased", the Wills Act's "testator" and the ISA's "intestate"; the same human being is a
beneficiary under a will, a next-of-kin under ISA rule 3, and a person "interested in the estate"
with standing under PAA s 18(2). Encoding them separately would triplicate the family tree and let
the copies disagree.

So `sg-succession-domain.l4` owns the nouns, each Act module owns its own verbs and imports the
ontology, and `sg-succession.l4` is the only place they meet.

## What is here

```
sg-succession-domain.l4   the shared ontology — Person, Family, Estate, Will, Case
sg-wills.l4               WA 1838 — formal validity, capacity, revocation, the s 27 privilege
sg-isa.l4                 ISA 1967 — all ten sections, s 7 rules 1–9, per stirpes
sg-paa.l4                 PAA 1934 — which grant, to whom, the Schedules, the timetable
sg-succession.l4          the composition, and the order the questions must be asked in
cases/                    178 scenario assertions, including one witness per materialised fork
registers/                source bundle · external-modification sweep · fork register
app/                      a browsable tool, built by RUNNING the encoding (see below)
report/                   the pipeline's conversion report and its hash-chained run journal
source/fetch-sso.py       re-runs the fetch, reproducibly
```

## The app does not restate the law

`app/build-scenarios.mjs` writes one `#EVAL` per scenario into a temporary L4 module, runs
`l4 run --json`, and records **what the encoding answered**. `app/index.html` only presents that.
Nothing on the page is computed in JavaScript except the conversion of an exact share into dollars
and cents — done by largest-remainder in whole cents, so the column adds up exactly.

L4 numbers are exact rationals: three thirds are exactly one estate, and the case suite asserts it
rather than assuming it.

## Read this before relying on it

**Status: `draft`. No domain expert has reviewed this against the statutes.** The pipeline's HG1
gate was waived on the record, and the waiver says so.

Two known gaps, both in [`registers/fork-register.json`](registers/fork-register.json):

- **F6 — ISA s 6(b) half-blood ranking is not implemented.** An estate entered with both whole- and
  half-blood siblings divides equally, where the live reading gives the half-blood nothing while a
  whole-blood sibling is represented. There is a case asserting the *wrong* answer on purpose so
  the gap cannot be forgotten. **This is the first thing to fix.**
- **F2 — legitimacy is delegated, not decided.** ISA s 3 confines "child" to a legitimate or
  court-adopted child; the tool cannot see legitimacy and takes the `children` list as given.

Two interpretive forks are **materialised**, so both readings execute and the tests show what turns
on the difference: F1 (does stirpital division start at the child generation when every child
predeceased?) and F3 (does rule 6's "children" stop representation one generation down?).

**This is not legal advice.**
