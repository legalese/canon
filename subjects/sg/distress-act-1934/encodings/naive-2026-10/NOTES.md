# Distress Act 1934 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition (incorporating all amendments up to and including
1 December 2021), informal consolidation, version in force from 1/4/2022, as deposited
at `../../registers/source-bundle/DA1934.txt`. The latest amendment annotated is Act 25
of 2021, with effect from 1 April 2022 (ss 5(1) and 20).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0032** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The Act is short (24 sections), so the row takes nearly all of
its substantive rules: ss 3-5, 8-10, 12, 13, 15 and 19-24. Not encoded: the
definitions beyond their effect (s 2), joint owners (s 6), the form of the writ (s 7),
the s 11 deeming and deduction machinery, the s 14 notice diverting an under-tenant's
rent, the judge's discretions under ss 16-18 and 23(3)-(4), and the Rules of Court
(not retrieved).

## What the Act turns out to say

### 1. A landlord can recover at most 12 months' rent by distress, and only through the court

s 4: "No landlord shall distrain for rent except in the manner provided by this Act" —
there is no self-help seizure. s 5(1): the writ is for rent due "for a period not
exceeding 12 completed months of the tenancy immediately preceding the date of the
application". With 18 months unpaid at $1,000, the writ reaches $12,000. (Treating the
cap as monthly rent times the lesser of the months in arrear and 12 is an inference for
a constant rent.) The Act does not apply to rents due to the Government (s 3). Asserted.

### 2. A lodger or under-tenant can save his own goods, but usually by paying the head tenant's arrears

s 10(2): an under-tenant or lodger whose goods are seized for the head tenant's rent
gets them released only if the tenant has no interest in them **and** he pays "an
amount equal to the arrears of rent" to the landlord or into court and undertakes to
pay future rent direct. s 10(3) caps that payment at the rent he himself owes — but for
an under-tenant only if he pays "at least 75% of the full monthly letting value". An
under-tenant on a cheap sublet owed $800 can be made to pay the full $3,000 arrears; a
lodger owed $600 pays $600. A stranger to the tenancy pays nothing. Asserted.

### 3. Some goods can never be rescued this way

s 12 shuts s 10 off for the tenant's spouse's goods, hire-purchase goods, a partner's
goods, a company's goods where the tenant works for it, and — except for a lodger —
goods in a shared business or left in an office a month after notice. s 13 shuts it
off for an under-tenant whose sublet breaches a written covenant; it says nothing of a
lodger, so a lodger in the same position is not shut out. Asserted.

### 4. The sheriff is paid first, the landlord second, the tenant gets any balance

s 19: proceeds go first to "the sheriff's fees and expenses", then rent and costs; the
balance returns to the tenant. Where goods are already held under another court's
enforcement order, s 20 gives the landlord priority over the enforcement creditor, but
"not in any case" beyond "the last 6 months' rent". Asserted.

### 5. Short clocks everywhere

The sale may not be named for less than 6 days after the notice, and paying within 5
days stops it (s 9). Goods removed to defeat distress may be followed within 30 days
with a judge's order, or seized without one while in transit (s 21); a good-faith
purchaser for fair value keeps them, and has 4 days to apply (s 22). For deserted
premises (rent at least 75% of annual value, at least 2 months in arrear, abandoned
with nothing worth distraining) the landlord gets possession if no one applies within
10 days, and the tenancy ends (s 23) — but not in the District Court (s 23(5)).
Asserted.

### 6. Exempt property: what is in use, clothing, bedding, other people's goods

s 8 excludes things "in actual use", the tenant's "necessary wearing apparel and
necessary bedding", goods held for repair or carriage in his trade, inn guests' goods,
goods in the custody of the law, and tools not in use only where other property covers
the debt. The only offence is selling seized goods unlawfully: a fine up to $200
(s 24). Asserted.

## What would need doing before this is worth anything

- The Rules of Court governing the writ, the prescribed forms and the sale were not
  read; s 24's offence depends on them.
- Whether the s 23(2) 10 days are counted inclusively is not decided; the cases avoid
  the boundary.
- s 5(1) "12 completed months" was read as a cap on months of arrears; a varying rent,
  or arrears partly outside the window, is not modelled.
- No case law on distress was searched.
