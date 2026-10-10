# Prevention of Human Trafficking Act 2014 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation marked "version in force from 17/8/2026", deposited as
`../../registers/source-bundle/PHTA2014.txt`. The latest amendment annotated is Act 21
of 2025 (Criminal Law (Miscellaneous Amendments) Act 2025), with effect from 17 August
2026, against the penalties in s 4(1) and s 6(2). The deposit does not show the
penalties as they stood before that amendment.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0058** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Act is short (24 sections), so the row takes almost every rule a
person can be on either side of: the s 2 definitions the offence turns on, the
trafficking offence (s 3), penalties and aggravating factors (s 4), abetment (s 5),
receiving payments (s 6), the 48-hour detention limit (s 9(3)), the penalties for
obstruction, identifying a victim and false statements (ss 17, 18(4), 20), the
private-hearing rule and publication ban (s 18), and informer protection (s 21).
Not encoded: the enforcement powers (ss 7, 8, 10 to 16) beyond the obstruction
penalty, bail, the "reasonable in the circumstances" limb of s 9(3), victim assistance
(s 19, discretionary), the elements of the s 20 offence, ss 22 to 24.

## What the Act turns out to say

### 1. For a child, no means need be shown; for an adult of 18, one must

s 3(2) makes recruiting, transporting, transferring, harbouring or receiving a child
for exploitation an offence by itself. s 3(1), for anyone else, also needs one of six
listed means (coercion, abduction, fraud, abuse of power, abuse of vulnerability, or
paying the person in control). "Child" is "below 18 years of age", so recruiting a
16-year-old for sex work with no means is trafficking, and recruiting an 18-year-old
for forced labour with no means is not. Asserted.

### 2. A fine and a prison term are both mandatory; caning is discretionary

s 4(1) says the offender "shall be punished with a fine not exceeding $100,000 and with
imprisonment for a term not exceeding 10 years, and shall be liable to caning not
exceeding 6 strokes" (second or subsequent: $150,000, 15 years, 9 strokes). s 6(2) is
identical for knowingly receiving payments. By contrast ss 17, 18(4) and 20 say "or ...
or to both". The reading of "second or subsequent offence" as an offence after a
previous conviction is an inference; the text does not define it. Asserted.

### 3. Consent is irrelevant, and so is doing part of it abroad

s 3(3): the victim's consent (or, for a child, the child's, parent's or guardian's) is
irrelevant. s 3(4): it does not matter that the act is done partly outside Singapore.
The encoding carries both facts on the record and gives them no effect; a 17-year-old
brought from abroad with parental consent for forced labour is a trafficking case.
Asserted.

### 4. Receiving payments reaches only exploitation in Singapore

s 3 covers exploitation "whether in Singapore or elsewhere", but s 6(1) catches only a
person who knowingly receives payment connected with exploitation "in Singapore".
Asserted.

### 5. "Abuse of the position of vulnerability" is a closed list

s 2 defines it ("means") as taking advantage of a position resulting from illegal entry
or stay, pregnancy, illness, infirmity or disability, or impaired decision-making from
those. Poverty and lawful foreign-worker status are not on the list; such a case would
have to be put as coercion, deception or debt bondage. Debt bondage needs services
pledged for a debt and either the value not credited or the length or nature not
defined. Asserted.

### 6. Abetment's intention requirement does not attach to instructing

s 5(1)(a) — instructing another to commit the offence — needs nothing more; (b)
providing financing, transport, shelter or a facility, and (c) participating, both
need "the intention of facilitating" the offence. A landlord providing shelter without
that intention does not abet under s 5 (the Penal Code's general abetment is preserved
by s 5(2) and is not modelled). Asserted.

### 7. Victim protection: child cases must be private; the publication ban applies regardless

s 18(1): in a case involving sexual exploitation, the court must hear it in private if
the victim is a child and may order privacy otherwise. s 18(3): the ban on identifying
the victim applies whether or not the hearing is private. The maximum for breach is
$5,000 or 3 years or both. Asserted.

### 8. Detention without warrant: 48 hours, journey excluded

s 9(3): no more than 48 hours "exclusive of the time necessary for the journey" to the
Magistrate's Court, and no longer than reasonable. Only the outer limit is modelled.
Informers (s 21) may be unmasked only if the informer wilfully lied (in proceedings for
the offence) or if justice requires it (in other proceedings). Asserted.

## What would need doing before this is worth anything

- The pre-2026 penalties (before Act 21 of 2025) were not retrieved; a conduct date
  before 17 August 2026 is not handled.
- The Penal Code's general abetment, conspiracy and attempt provisions, and any caning
  exemptions in the Criminal Procedure Code, were not read.
- No case law on "abuse of power", "coercion" or "forced labour" (undefined here) was
  searched.
- s 3(4)'s proviso (the act "if done wholly in Singapore, would constitute an offence")
  is assumed satisfied, not tested.
