# `source/` — the sources, and the test generator

The PDFs and wiki dumps here are the primary sources the encodings in
`../encodings/legalese/` were made from; `revisions.json` records which revision of each
was taken.

## `gen-tests.py` — the tier-3 test generator

`gen-tests.py` writes `../encodings/legalese/hvac-tests-generated.l4`, which holds **193
assertions** over `hvac-law.l4` and `hvac-fees.l4`.

Regenerate it from the repository root of this subject:

```sh
python3 source/gen-tests.py
```

It takes no arguments, reads nothing but its own source, and is deterministic and seedless:
the same script always writes the same file, byte for byte. Python 3 standard library only.

Then run the generated module, with a binary and a prelude that match each other:

```sh
sh encodings/legalese/check.sh          # runs it alongside everything else in the subject
```

### Why it is a generator and not a handwritten file

Every expected value in the generated module is computed by an **independent
re-implementation, in Python, of the statute** — the rules quoted in the comments of the two
`.l4` files, read again from scratch. It is deliberately not a transliteration of the L4. Two
readings of the same text can disagree, and when they do the assertion goes red and somebody
has to decide which one the statute supports. A test file that was written by reading the L4
could not do that.

The generator computes on `fractions.Fraction` throughout, so the indexation cases that land
on exactly half a shekel are exactly half a shekel, not a float that is nearly one.

### The six families

| § | rule | assertions | what it is looking for |
|---|------|-----------:|------------------------|
| a | reg. 3, annual indexation | 40 | five fee amounts against six index movements, and fifteen pairs engineered so the exact product is a half shekel — where half-up, half-even and truncation part company |
| b | s.8, period of validity | 33 | the race between five years and the 31 March cap, across four grant years and both sides of 31 March, plus a leap-day grant |
| c | s.63, commencement | 16 | the later of two days, and month arithmetic that clamps to the length of the month it lands in, including into February of a leap year |
| d | ss.2 and 3, the grades | 66 | both sides of each kilowatt ceiling a hundredth apart, every grade against every output, the unlicensed person, and the system exempted by order |
| e | s.9, the foreign expert | 9 | two renewals and no more, and the three-year outside date |
| f | s.6 with the Second Schedule | 29 | the three-year sunset on the experience route, against a route that never sunsets and a certificate that bypasses the Schedule entirely |

**Do not edit the generated file.** It says so on its first line. Change the rule in
`gen-tests.py` and regenerate.
