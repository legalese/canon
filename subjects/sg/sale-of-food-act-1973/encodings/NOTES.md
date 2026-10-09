# Sale of Food Act 1973 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (Parts 1–7; the Act has no Schedule), as printed in SSO's informal consolidation of the version in force from 1 May 2026. The source is the text already deposited in this repository: no PDF was supplied, and none is needed.

**Inputs.** The following are taken as given rather than worked out:
- the court's findings: knowledge, prejudice, insanitary conditions, reasonable excuse, authority;
- the Director-General's and the Minister's discretions;
- prescribed standards, substances and compoundable offences;
- classifications that turn on other Acts: the Environmental Public Health Act's First Schedule purposes, health products, medicinal products and poisons.

### The top-level goal

`the food position for` a `Food case` (`sfa-goal.l4`) answers: *for this article and what this person did with it, does the Sale of Food Act reach it, is an offence committed, does a defence answer it, and what is the most it can cost?*

It returns:
- whether the article is food;
- whether the Act reaches it;
- whether the conduct contravenes the Act;
- whether a defence answers the charge;
- the maximum penalty;
- the most that may be collected to compound;
- the courts that may try it.

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Is it food? Is it unsafe, unsuitable or adulterated? Is this a food business, and a non-retail one? Is this a sale? | `food`, `unsafe`, `unsuitable`, `adulterated`, `a food business`, `a non-retail food business`, `a sale within the Act` | ss 2A–2F, 25 | `sfa-definitions.l4` |
| 2 | Does the conduct contravene the Act, and what is the most it can cost or be compounded for? | `the conduct contravenes the Act`, `the maximum penalty for`, `the most that may be collected to compound…` | Parts 3, 4, 7; ss 5–10, 10K, 33(5), 46(6), 48–50, 56(1)(r) | `sfa-offences.l4` |
| 3 | Does a defence answer it, and who else is liable? | `a defence answers the charge`, `the warranty defence is made out`, `the carrier or publisher defence is made out`, the s 26 and s 27 rules | ss 16A(6)–(7), 26, 27, 31–33, 40(4)–(5) | `sfa-offences.l4` |
| 4 | Seizure, directions, compensation, licences, appeals, summons and notice periods | `a complaint about a seizure is still in time…`, `the direction takes effect on…`, `the last day to seek review of compensation…`, `the proportionate licence fee for…`, `the last day to appeal against…`, `the summons is returnable late enough…`, `notice was given 3 clear days before…` | Parts 2, 2A, 6, 7 | `sfa-procedure.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| long title, ss 1, 3 | carried as text |
| s 2 | read into the facts: advertisement, premises, proprietor and so on |
| ss 2A–2F | Goal 1 |
| ss 4–8, 10 | Goal 4 (s 4(2)–(3)). The offences in ss 5(4)–(5), 6(4), 7(2) and 10(3) are in Goal 2. The powers are carried as text |
| ss 10A–10L | Goal 4: who may be directed (10A), when a direction takes effect (10C(4)), how long it lasts (10B(5)), compensation (10I), appeal (10J). Offences under s 10K are in Goal 2. 10B–10H and 10L are carried as text |
| ss 11–20 | Goal 2. The defences in s 16A(6)–(7) are in Goal 3 |
| ss 21–24 | Goal 2 (ss 21, 22(5), 23, 24(1)). The power in s 22(6) is in Goal 4. The rest is carried as text |
| ss 25–28 | s 25 is in Goal 1; ss 26 and 27 are in Goal 3; s 28 is carried as text |
| ss 29–39 | s 29 (courts), s 30(1) (summons period) and s 34(1) (analyst's notice) are in Goal 4; ss 31–33 are in Goal 3; the rest is carried as text |
| ss 40–56 | s 40 is in Goals 2 and 3; s 41 in Goal 2; ss 45 and 46(9), (12), (14) in Goal 4; ss 48–50 in Goal 2; s 55 in Goal 4. The rest is carried as text |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 14 "more than 50 parts … in one million parts" | Is exactly 50 parts per million an offence? | No | "more than" |
| F2 | s 30(1) "not … returnable in less than 14 days from the date on which it is served" | Is 14 days enough? | Yes: served D, returnable on D + 14 or later | "less than 14 days" |
| F3 | s 34(1) "at least 3 clear days before the day on which the summons is returnable" | Which days count? | Clear days exclude both the notice day and the return day, so notice falls on the return day − 4 or earlier | Clear days |
| F4 | s 10I(5)(b) "within 14 days after the 28-day period … ends" | When is the last day? | received + 28 + 14 | The text |
| F5 | s 32 | Does it reach a s 16A publishing charge? | No. s 32 speaks of "a prosecution for selling", and s 16A has its own defences | s 16A(6) opens "Without affecting section 32"; the independent pass noted this, and the point is left open (§5) |
| F6 | s 41(2) "without authority" | Does the authority input answer obstruction under s 41(1)? | It answers only the mark or seal limb. Obstruction of an officer is an offence whatever the person's authority | s 41(1) has no such words |

## 4. Tests

- **`sfa-tests.l4`, 92 assertions.** Expected values are worked from the source. They cover:
  - the definitions;
  - each offence, with its edges (50 ppm, knowledge, licensing, retail versus non-retail);
  - every penalty limb and composition;
  - the warranty defence's 7-day notice and its rule for warrantors resident abroad;
  - the carrier and publisher defence;
  - every Goal 4 period;
  - whole cases through the top-level goal.
- **The independent pass:**
  - **Files.** `tests-independent.l4` (139 assertions), `independent-expectations.md` and `INDEPENDENT-TEST-REPORT.md`. A separate session wrote its expectations from the source before reading the encoding.
  - **Result.** All 139 passed, none refusing.
  - **Fixed after it.** The report found five conditions the encoding did not model. Each made the conduct an offence where the Act does not:
    - s 10K(1): failure with a reasonable excuse;
    - s 10K(3): removing a direction no longer in force;
    - s 41(2): acting with authority;
    - s 6(3): refusing to sell less than a whole unopened package;
    - s 7(1)(b): other food taken without the purchaser's request or consent.

    All five were added as inputs, with five more assertions. The independent file was changed only in plumbing: the four constructors now take their new argument, set so that each expected value is unchanged.
- **Simplifications the report lists, kept as they are:**
  - s 2E (sale) and s 2B classification are inputs;
  - the presumptions in ss 2E(3), 16A(4)–(5) and 28 are carried as text;
  - s 46(6)'s voiding of the licence, s 46(12)(c) suspension, s 33(4) and s 10I(7) are carried as text;
  - s 56(1)(r) is reported as the ceiling regulations may set;
  - the s 46(9) fee is computed as if charged;
  - the s 4(2) 48 hours is given as elapsed hours.

## 5. Open questions

- F5: does s 32's reasonable-steps proviso reach an advertising charge under s 16A? s 16A(6) opens "Without affecting section 32".

## 6. Checks

See `encoding.json` → `checks`.
