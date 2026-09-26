# encodings/legalese-2026-09 — notes

Written 2026-09-04, the day the row was started. The spec this row implements is
`legalese/l4-ide` `specs/todo/yc-safe/SPEC.md` (branch `mengwong/yc-safe` at the time of
writing); its §6 describes the modules, §7 the acceptance cases, §11 the rulings. This file
says what the row is, what it does not have, and where it deviates from the sidecar shape.

## What it is

Three modules, one case file, one golden:

| file | what it does |
| --- | --- |
| `safe-form.l4` | the deal as the generator supplies it (mirrors `deal.json`), and `validate deal`: the reasons a deal cannot be filled onto one of YC's six published forms |
| `safe.l4` | one Safe, section by section — §1(a) conversion for all three economic variants, §1(b) Liquidity Event entitlement, §1(c) Dissolution, §1(d) priority as a payout function, §1(e) termination, the §2 price definitions, §5(a) majority-in-interest |
| `safe-portfolio.l4` | what `safe.l4` needs from a whole cap table: the Company Capitalization fixpoint and the cap-versus-price partition (`convert`), the round convention the instrument is silent about, the pro rata allocation, the post-round cap table, and the Liquidity Capitalization with each Safe's cash-out-or-convert choice (`liquidity`) |
| `cases/user-guide-appendix-ii.l4` | YC's own worked examples (User Guide Appendix II, Example 1, Q1–Q5) as `#ASSERT`s, plus synthetic mixed-portfolio and refusal cases that say they are synthetic |
| `cases/deal.example.json` | the same Example 1 as a `deal.json` the generator can run |
| `tests/user-guide-appendix-ii.golden` | the case file's output, point in time (see `tests/README.md`) |

Run the cases with the row on the library path — a module under `cases/` cannot otherwise
find its parents:

```
JL4_LIBRARY_PATH=$PWD l4 run cases/user-guide-appendix-ii.l4
```

86 assertions, all satisfied, on 2026-09-04 with `l4` built from l4-ide `unstable`
`b457b359`.

## Where it matches the User Guide, and where it does not

Company Capitalization and the cap-method share counts match the guide to the share
(11,764,705; 588,235; 1,176,470). The round price, option pool increase, new-money shares
and pro rata shares match to within 0.05%: the guide rounds the pool increase to the
nearest thousand (1,695,000 where the closed form gives 1,694,570) and prices to four
decimals, then computes onward from the rounded figures; this row keeps exact rationals and
rounds shares down once at the end. That is fork **F3** in `../../registers/fork-register.json`.
Q5's mixed partition (one Safe at cap, one at the round price) settles in two passes of the
fixpoint where the guide stops after one and a half, on the same partition (fork **F2**).

## What it does not have

- **Almost no deontic layer.** The Company's obligations to issue shares (§1(a)), pay
  (§1(b), (c)) and pay the Dividend Amount (§5(c)) are stated as amounts and decisions, not
  as `PARTY … MUST … WITHIN` rules. The one exception is the MFN form's §3 amendment
  provision — the family's only hard deadline (10 days) — which `safe.l4` states as a
  regulative rule with three `#TRACE`s in the cases (election in time; permission lapsing;
  Company failing to restate).
- **No event definitions.** Change of Control, Direct Listing, IPO and Dissolution Event
  are inputs (a Liquidity Event happened or did not), not predicates over transactions.
  They are also where the jurisdiction forms differ substantively (variation register
  J16–J21); an encoding that computed them would need a jurisdiction axis this row does
  not carry.
- **No representations** (§3, §4) and no assignment/notice/severability (§5(b)–(g)).
- **No pre-money arithmetic.** User Guide Example 2 mixes a pre-money Safe with a
  post-money one; its pre-money half waits for the `yc-safe-premoney` leaf.
- **A four-count cap table** (common, options outstanding, promised options, unissued
  pool). Real cap tables carry classes, vesting and other convertibles; SPEC.md §10 Q1.
- **Not the ruled sidecar shape.** No `projections/`, `report/` or `gates/`: the
  encoding pipeline is not run on this subject (SPEC.md §1, ruling R2). `registers/` at
  the subject level carries the source bundle and the fork register, validated with
  l4-ide's `etc/go/lib/register-validate.mjs`.

## Language notes a later editor will want

- `NOT` is low-precedence: `NOT p AND q` is `NOT (p AND q)`. Every `NOT` under a
  connective in these modules is parenthesised for that reason; do not "tidy" them.
- Multi-parameter `GIVEN`s are laid out one parameter per line because the one-line form
  breaks on `LIST OF` types.
- The JSON boundary uses a record of `MAYBE` fields (`TermsIn`) rather than the sum type
  (`EconomicTerms` in `safe.l4`) because `l4 batch` decodes records and lists by field
  name but did not decode sum-type constructors from JSON in either shape tried.

## Licence

The L4 is Apache-2.0. The quoted form text is © 2023 Y Combinator Management, LLC under
CC BY-ND 4.0 International; see `../../SOURCE-LICENSE.md` for what that does and does not
settle, including the open question whether a formalisation is an adaptation.
