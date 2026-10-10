# Electric Vehicles Charging Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** informal consolidation, "version in force from 1/7/2026", retrieved 1
October 2026. Amendment annotations seen: S 795/2023 (wef 8 December 2023), Act 5 of
2026 (wef 4 May 2026) and Act 15 of 2026 (wef 1 July 2026, the latest annotated).

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** (Tier 1 of the remaining Acts): anyone who
owns an electric vehicle, puts a charger in a home or condominium car park, or owns a
building whose car park has to be wired for charging meets it. An automated count found
4 of the 527 deposited Singapore Acts citing it by its title, which undercounts and is
no measure of importance.

This row takes who is a charging station operator and when a licence is needed
(ss 4(1), 41), charging with an unregistered charger (s 18), registration marks,
certificates and transfers (ss 20, 21, 26, 27), improper charging, tampering and labels
(ss 30-32), defect warnings (s 36), "repeat offender" (s 2), the tiered maximum
penalties for ten offences (ss 6, 18, 20, 23, 24, 27, 29, 30, 32, 39), composition
(s 81), the trigger for charging points in car parks (ss 61, 62, 65(4)) and the appeal
window (s 68(2)). Not encoded: homologation (ss 7-13), advertising (ss 14-17), trial
chargers (s 28), safety directives beyond the penalty, licensing beyond s 41, step-in,
enforcement powers and the Schedule's transitional rules. Much of the Act's working
detail (inspection intervals, banned locations, permissible purposes, charging-point
formulas, which offences are compoundable, exemptions) is left to Regulations and
Gazette orders, none of which was retrieved.

## What the Act turns out to say

### 1. On the words alone, a householder with a wall charger is a "charging station operator"

s 4(1)(c) makes a charging station operator of anyone who "has charge and control of any
charging point in any place in Singapore (whether or not in the course of any business)
... unless excluded by the Minister by order in the Gazette". Engaging in conduct as a
charging station operator is a "regulated activity" (s 2), and undertaking one without a
licence or a s 92 exemption is a **strict liability** offence (s 41): up to $10,000 or 6
months for an individual, plus $250 a day after conviction. Whether a Gazette order or
exemption takes householders out was not retrieved; it is an inference that one must
exist for the scheme to work. Asserted (on the words, with exclusion and exemption as
inputs).

### 2. The owner's duty to register has no penalty of its own; the person charging carries the risk

s 19(1) says the person with charge and control "must apply to the LTA to register the EV
charger before" first use, but s 19 creates no offence and the Act has no general penalty
section (none found on a search). What bites is s 18: an offence to charge, or allow
charging, with an unregistered charger if the person "knows that, or is reckless as to
whether" it is unregistered, $5,000 or 6 months for an individual. Asserted.

### 3. Businesses pay double, except for two paperwork offences where they pay two and a half times

Ten offences share a four-tier pattern (individual, individual repeat offender,
non-individual, non-individual repeat offender), and the non-individual ceiling is twice
the individual one, except under s 20 (mark not affixed within 60 days) and s 27
(registration not transferred), where $1,000 becomes $2,500. A repeat offender is one with
an earlier conviction for the same offence within 5 years (s 2); every tier doubles.
Asserted.

### 4. Selling a charger moves the registration; lending or hiring it out does not, but hire-purchase does

s 27 requires the registered responsible person who disposes of the charger, or transfers
possession "otherwise than temporarily", to apply to transfer the registration. s 27(4)
excludes hiring and lending, an agent for sale, a bailee for repair or storage, and a
court order, but carves hire-purchase back out of the hiring exception. Asserted.

### 5. A defect warning is fined per charger, with a ceiling

Ignoring a manufacturer's s 35 warning (stop charging, do not supply, install or certify
until rectified) costs up to $2,000 per charger, capped at $20,000, plus $250 a day after
conviction (s 36(2)). Asserted.

### 6. Car parks: the 280kVA and 8-lot thresholds

Part 8 bites on new or re-erected buildings, on works raising gross floor area by at least
50%, and on electrical work needing approval to raise the approved load above 280kVA
(s 61). The charging-point duty falls away where fewer than 8 parking lots result
(s 62(2)), and Government or public-authority works on their own land are out (s 62(1)).
An owner doing electrical work has 12 months from switch-on or the load increase, or longer
if the LTA approves in writing (s 65(4)). Asserted.

### 7. Smaller points

Composition is capped at the lower of half the maximum fine and $5,000, for prescribed
offences only (s 81). Appeals to the Minister must be in writing with grounds within 28
days, and the decision must be complied with meanwhile (s 68). Wilful tampering likely to
endanger life or property carries up to $100,000 or 5 years (s 31). Asserted.

## What would need doing before this is worth anything

- The Regulations and Gazette orders were not retrieved: who is excluded from s 4(1)(c)
  or exempt under s 92, the inspection intervals, banned locations, permissible purposes,
  the charging-point formulas and the compoundable offences. Finding 1 in particular may
  be wholly answered by an exclusion order.
- The boundary of "within the period of 5 years" (s 2) and of the day-counts in ss 20, 21
  and 68 is read inclusively without authority.
- The licensing scheme (ss 42-55) and the s 64 duties of developers are not encoded.
- No LTA guidance or case law was searched.
