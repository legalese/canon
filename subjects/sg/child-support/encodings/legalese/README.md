# What a Singapore family gets under the SG Child Support Package

An executable encoding of the package of family measures announced at Singapore's **National Day
Rally on 23 August 2026**, and of the schemes it replaces.

> **This is an announcement, not law.** No Bill has been introduced and the Child Development
> Co-Savings Act 2001 is unamended. Every figure produced at a rule date on or after 1 April 2027
> states a **policy intention**. **This is not legal advice.**

## Why this subject is shaped the way it is

Two regimes, one subject, because they are two halves of one announcement and they **share their
nouns**: the same child's date of birth decides a Baby Gift cohort in `sg-csp.l4` and a
qualifying-child age band in `sg-childcare-leave.l4`. Splitting them would duplicate the family and
let the copies disagree.

| module | what it holds |
| --- | --- |
| `sg-child-support-domain.l4` | the nouns, the calendar arithmetic, and the two materialised forks |
| `sg-csp.l4` | the money: the outgoing schemes, the five Package lines, and the transition |
| `sg-childcare-leave.l4` | CDCSA ss 12B, 12C, 12CA, and the announced merger as a dated arm |
| `sg-csp-openfisca.l4` | the money projected into the subset `l4 openfisca` accepts |
| `sg-child-support.l4` | the composition and four `@export` decision functions |
| `cases/` | 71 scenario assertions (79 across the module set) |

## The rule-version axis is the point

The subject **is** a transition, so every figure is dated. Ask for the same child at two rule dates
and you get the two regimes:

```
`EVAL UNDER RULES EFFECTIVE AT` (YMD 2026 1 1)  ...   -- Baby Bonus + Large Families Scheme
`EVAL UNDER RULES EFFECTIVE AT` (YMD 2027 10 1) ...   -- the Package, caps harmonised
```

A reader who does not pin a rule date must not be handed an announced figure without being told it
is one.

## The app does not restate the law

`app/build-scenarios.mjs` writes one `#EVAL` per question into a generated L4 module, runs
`l4 run --json`, and records **what the encoding answered** — 1,388 values over 88 children, 20
co-matching windows and 108 leave scenarios. `app/index.html` only presents that. The only
arithmetic in JavaScript is multiplying a per-child entitlement by a population figure the user
types, in the budget panel, and it says so.

```bash
L4=/path/to/l4 JL4_LIBRARY_PATH=/path/to/jl4-core/libraries node app/build-scenarios.mjs
node app/build-app.mjs        # inlines outcomes.json -> index.html
```

## What it found

Three things the headline conceals, all in [`report/CONVERSION-REPORT.md`](report/CONVERSION-REPORT.md):

1. **The cash line falls** for every child born since 14 February 2023 — by $1,000 for a first or
   second child and **$3,000 for a third or subsequent**, because the $10,000 Baby Gift is a floor
   replacing an $11,000/$13,000 Cash Gift.
2. **A deadline worth acting on.** CDA co-matching caps harmonise to $5,000 on **1 October 2027**.
   A family with a fifth child born before then loses **$10,000** of headroom if they have not
   saved into the account by 30 September 2027.
3. **"The Government will cover the cost" is capped at $500 a day** while the day count roughly
   doubles, so above a gross daily rate of about $800 (one child) or $667 (three) the **employer
   pays more** than today.

## Read this before relying on it

**Status `draft`. No domain expert has reviewed this against the sources; HG1 is waived on the
record.**

- **Nine forks** in [`registers/fork-register.json`](registers/fork-register.json), two of them
  materialised so both readings execute. F1 alone moves **$5,000 per child**.
- **F5 is a known gap**: the Act's per-child lifetime leave caps cannot survive the merger and the
  announcement does not say what replaces them, so the announced arm answers per relevant period
  only.
- The encoding **refuses** the outgoing-scheme comparison for a birth before 2015-01-01 rather than
  quote a Baby Bonus rate nobody measured. The Package-side answer is total from a 2009 birth.
- The employer-cost finding counts **childcare leave only** and is a lower bound.

`NOTES.md` carries the rest of this encoding's idiosyncrasies.
