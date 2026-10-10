# Payroll Tax Act 1965 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
9/3/2025"), deposited at `../../registers/source-bundle/PTA1965.txt`. The revised
edition incorporates amendments up to 1 December 2021; the latest amendment annotated
in the body is Act 5 of 2025 (wef 9 March 2025), to s 12(2), (3) and (3A).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**REQ-0064** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining Singapore
Acts, ordered by everyday-life relevance. The requirement asks what the Act decides for
an employer or employee it applies to; no scenario has asked a sharper question yet.
The Act has only 12 sections, so nearly all of the operative Part 3 is encoded: ss 4 to
8, 10, 11(2) and 12(4) to (6), (8). Not encoded: Part 2 (approval of tax forms, s 3, and
its Schedule), s 9 (recovery as a debt due to the Government), the regulation-making
heads in s 11(1), (3), (4), and the administrative provisions of s 12(1) to (3A) and (7).

## What the Act turns out to say

### 1. The Act charges every employer every month, but sets no rate

s 5 charges payroll tax "on every employer" on the payroll for January 1965 "and of each
subsequent month". s 6(1) leaves the rate entirely to a Minister's order. No order was
deposited, so this row cannot say what any employer actually owes: every calculation
takes the rate as an input. Whether an order is in force, and at what rate, is not in
the deposit. Asserted (with the rate as a parameter).

### 2. A fraction of a dollar is dropped, never rounded up

s 6(2): where the tax "contains a fraction of a dollar, the tax payable shall be taken to
be that amount less that fraction". At 2% on a payroll of $12,345 the tax is $246, not
$246.90 or $247. Asserted.

### 3. Household staff are outside the Act only if they serve the household

s 4 excludes "any domestic servant, gardener or driver, wholly and exclusively employed
by an individual otherwise than in connection with his trade, business, profession or
vocation". A driver employed by an individual for his business, or by a company, is an
employee whose pay counts. A director or office-holder is included; this row reads
them as still needing the month's Singapore link (an inference: the text adds them to
the class without saying). An employee on leave counts if the leave is attributable to
earlier Singapore services. Asserted.

### 4. Only cash counts, and "cash" is wide

"Remuneration" covers wages, salary, commission, bonuses, allowances (including housing)
and other emoluments "paid in cash"; "cash" includes notes, cheques or any commercial
equivalent of money in any currency. A housing allowance paid in kind is outside.
Leave pay is added by "and includes any leave pay", which this row reads as outside the
cash qualifier (a reading; the grammar allows the other). Payroll also includes "a
proportion" of the civilian pay an employer must pay under s 24 of the Enlistment Act
1970; the proportion is not stated in this Act. Asserted.

### 5. Exemptions: government by name, everyone else only by Gazette

s 7 exempts the Government, accredited foreign governments and local authorities
outright. Any other body or class is exempt only if the Minister gazettes it, "wholly
or to such extent" as specified; a charity not named in a notification pays in full.
Asserted.

### 6. Deadline, joint employers, agents and penalties

Payment is due by the 14th of the following month or a later date under regulations;
failing is an offence, up to $1,000 or 6 months or both (s 8). Joint employers are
jointly and severally liable, and a payer recovers from the others in proportion to
their share of the payroll (s 10(1)). Company secretaries, managers, principal officers
and directors *in Singapore* answer for the company's acts (s 10(2)). A declared agent
pays from moneys held for the employer (s 10(3); the cap at those moneys is an
inference). Regulations may impose a fine of double the unpaid tax plus up to $5,000 or
3 years (s 11(2)). Unlawful disclosure of payroll tax documents is an offence, up to
$1,000 or 6 months, prosecuted only by the Public Prosecutor (s 12(5), (6)). Asserted,
except the Public Prosecutor rule (encoded, not asserted).

## What would need doing before this is worth anything

- Retrieve the Minister's order(s) under s 6(1) prescribing the rate, if any is in force,
  and any s 7(d) exemption notifications.
- Retrieve the regulations under s 11 (notice of liability, records, refunds,
  remission, penalties) and any later-date rule under s 8(1).
- Find the proportion of Enlistment Act civilian pay that enters the payroll.
- No case law or Comptroller practice was searched.
