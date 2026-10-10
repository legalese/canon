# Medicines (Advertisement and Sale) Act 1955 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as shown in the finished example rows (the skill
itself could not be loaded in this session). No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MASA1955.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021. The latest amendment annotated is Act 11 of 2023, with effect from
26 June 2023 (s 4 repealed, s 6(1) and (3) amended, s 6(4) deleted, s 9
substituted). The retrieval record says "Current version as at 01 Oct 2026".

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is **REQ-0024** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet.

The Act is short (nine sections, one of them repealed, and a Schedule), so the row
covers almost all of it: the definition of "substance recommended as a medicine"
(s 2), the ban on advertising remedies for the Schedule diseases and conditions
(s 3), the ban on advertising for procuring miscarriage (s 5), the offences,
presumption and defences (s 6), composition labelling (s 7) and the Minister's
exemption (s 9). Not encoded: s 1, the Minister's power to amend the Schedule
(s 3(3)) beyond reading the Schedule as deposited, court jurisdiction (s 8), and
the meaning of "appropriate designation" (s 7(2)(a)), which depends on the Poisons
Act 1938, the Poisons Rules and the British Pharmacopoeia.

## What the Act turns out to say

### 1. The Government's exception covers disease advertising, but not miscarriage advertising

The proviso to s 3(1) exempts advertisements published by the Government, a public
authority, a public hospital's governing body, or a person the Minister has
authorised. s 5 has no such proviso. The only way out of s 5 is a Minister's order
under s 9, and s 9 names s 5 alone. So a Ministry of Health advertisement about
procuring miscarriage contravenes s 5 unless exempted by order, and a s 9 order
does nothing for a s 3 advertisement. Asserted.

### 2. Advertising to doctors is a defence under s 3, but not under s 5

s 3(2) lets a person charged prove the advertisement was published only so far as
was reasonably necessary to reach doctors, dentists, nurses, midwives, pharmacists,
public authorities, hospital governing bodies and trainees. That defence is written
into s 3 only. Under s 5 the only professional defence is the narrower s 6(3)(b):
publication only in a technical publication circulating mainly among those
professions. A direct mailing to doctors about procuring miscarriage is therefore
caught. Asserted.

### 3. The Schedule is specific: diabetes and hypertension are in, heart disease is not

The Schedule lists 19 diseases and conditions, from blindness and cancer to
"Sexual function", "Impotency", "Frigidity" and "Conception and pregnancy".
Diabetes and hypertension are listed. Heart disease, obesity and the common cold
are not, so s 3 does not touch advertisements for remedies for them. s 3 also speaks
only of "treatment of human beings". Reading that literally, an advertisement for
prevention alone, or for treating animals, falls outside it. That reading is an
inference from the words. Asserted.

### 4. A maker or seller named in the advertisement is presumed to have published it

Under s 6(2), if an offending advertisement presents the article as made, imported
or sold by the person charged, that person is presumed to have taken part in
publishing it "unless the contrary is proved". It is also a defence to prove that
he did not know and had no reason to believe he was taking part (s 6(3)(a)).
Asserted.

### 5. A medicine sold by retail must carry its composition in English

s 7(1) applies to a retail sale, or a free sample given to induce retail sales, of
a "substance recommended as a medicine". That term covers anything presented as
preventing or treating a human ailment, unless the terms definitely indicate a food
or drink (s 2). The label must be in English (other languages are allowed in
addition) and must give either the designation of the substance or the designation
of each active constituent or ingredient. If constituents or ingredients are named,
their quantities must be given too. Medicine made up and prescribed for a
particular person is exempt. Asserted.

### 6. The herbal and mineral-water defence protects shop sales only

s 7(4) is a defence for "a person charged with selling" who proves "the sale was
effected at a shop". It applies only where the article was nothing but dried,
crushed or comminuted plants (with or without water), or natural mineral water or an
imitation of it. A free sample of the same herbs, the same herbs sold from a place
that is not a shop, and a plant extract (processed further) get no defence. The
encoding treats a market stall as "not a shop". That is an assumption: the Act does
not define "shop". Asserted.

### 7. Penalties are small and imprisonment for labelling comes only on a repeat

After Act 11 of 2023, s 6(1) sets a maximum of $1,000 or one year for a first
advertising conviction, and $2,000 or 2 years for a subsequent one. s 7(3) sets $1,000
(no imprisonment) for a first labelling conviction, and $2,000 or 6 months for a
subsequent one. Asserted.

## What would need doing before this is worth anything

- "Appropriate designation" (s 7(2)(a)) needs the Poisons Act 1938 and the Poisons
  Rules, rules 22 and 23, together with the British Pharmacopoeia and Codex. None was
  read.
- No Gazette notification under s 3(3) varying the Schedule, and no s 9 order, was
  searched. The Schedule here is the one in the deposit.
- How the Health Products Act 2007 and the Medicines Act 1975 overlap with this Act
  was not examined.
- "Shop", "sell by retail" and "calculated to lead to" are undefined in the Act and
  are modelled as plain facts. No case law was searched.
- `encoding.json`'s method line comes from the shared helper and says the skill was
  used. In this session the skill could not be loaded, and the example rows were
  followed instead.
