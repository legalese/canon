# Debt Collection Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not loadable in this
session, so `encoding.json`'s stock method line overstates it slightly). No
pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** Act 27 of 2022, informal consolidation, "version in force from
1/12/2023", as deposited at `../../registers/source-bundle/DCA2022.txt` (SSO page
retrieved 2026-10-01). The latest amendment annotated is S 723/2023 wef 01/12/2023.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for **everyday-life relevance**: anyone chased for a debt by an agency, a
bank, a card issuer or a moneylender, and anyone who takes work as a debt
collector, meets this Act. (An automated count found 1 of the 527 deposited
Singapore Acts citing it by title; that undercounts and is not a measure of
importance.) This row takes who needs a licence or a class licence (ss 2, 6,
First Schedule), who may act as an individual collector (s 17), the offences and
which are arrestable (ss 6(5), 7(6), 17(3), 18(2), 28(3), 33), failing an
officer's requirement (s 34), composition (s 35), conviction grounds for cancelling
a collector's approval (s 25(1)(d), Second Schedule), appeals (s 37) and the
transitional period (s 46). Licence and approval procedure, class licence orders,
codes of practice, the rest of regulatory action, enforcement powers, corporate
liability, service and regulations are not encoded.

## What the Act turns out to say

### 1. The Act itself says almost nothing about how a collector may treat a debtor

There is no conduct rule for collectors anywhere in the Act's operative sections.
Treatment of debtors is left to licence conditions (s 10(3), which may require
compliance with the Penal Code 1871 and the Protection from Harassment Act 2014),
class licence conditions (s 14(3), e.g. first ascertaining that the person "is the
debtor"), codes of practice (s 16) and regulations (s 45(2)(i)-(n), including a
power to stop collection once the debtor says the debt is disputed). A breach of a
code "does not of itself" make a licensee criminally liable (s 16(9)). Not asserted:
none of those instruments was retrieved.

### 2. Banks and moneylenders collecting their own debts need a class licence, and the exclusions do not help them

s 6(2) requires a regulated business (banks, merchant banks, card issuers, finance
companies, licensed or exempt moneylenders: First Schedule Part 2) to be covered by
a class licence to collect its own debts. The s 6(4) exclusion reaches only
subsections (1) and (3). A creditor that is neither, such as a landlord collecting
its own rent, is outside s 6 altogether. Asserted.

### 3. A bank may only use its own employees; an excluded law firm only its own employees too

s 17(2): an individual may collect for a regulated business only if it is "the
individual's employer" and a class licensee and the debt is within the class
licence. s 17(1)(b) likewise lets an individual collect for an excluded person only
if that person is the individual's employer. So a contractor collecting for a law
practice, or a non-employee collecting for a bank, commits the s 17 offence unless
approved through a licensee. Asserted.

### 4. Only an entity can be licensed

s 6(1) requires "an entity which is authorised ... by a valid licence"; "entity"
(s 2(1)) means a registered company, a sole proprietorship or partnership registered
under the Business Names Registration Act 2014, an LLP, an LP or a prescribed
structure. A suspended licence does not count (s 2(4)(a)). Asserted.

### 5. A repeat unlicensed operator faces a mandatory minimum fine

s 6(5)(b): for a repeat offender, a fine "of not less than $20,000 and not more than
$100,000" or up to 5 years. First offence: up to $20,000 or 2 years. "Repeat
offender" is not defined in the deposited text of this Act. Only the s 6(1) and
s 17 offences are arrestable (s 33). Composition is capped at the lower of half the
maximum fine and $5,000 (s 35). Asserted.

### 6. Appeals are short and do not stop the decision

s 37(2): 14 days after service; (5) the Minister's decision is final; (7) the
decision must be complied with pending appeal unless the Minister directs otherwise.
The 14-day window is asserted.

### 7. The excluded persons grew in 2023

S 723/2023 added accounting corporations, firms and LLPs, chartered accountants and
public accountants (First Schedule para 1(ea)-(ee)), and Second Schedule item 3A
(s 11(1)(a) of the Miscellaneous Offences (Public Order and Nuisance) Act 1906).
The chartered-accountant exclusion is asserted.

## What would need doing before this is worth anything

- The class licence order(s) under s 14, the codes of practice under s 16 and any
  regulations under s 45 were not retrieved; they hold the rules a debtor would
  actually rely on.
- Treating the excluded persons as otherwise carrying on a debt collection business
  is an inference (marked in the `.l4`).
- s 46 is collapsed to flags; the commencement date (and so the start dates) is not
  in the deposit.
- No case law or Ministry guidance was searched.
