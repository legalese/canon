# Women's Charter 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, version in force from 17/8/2026. The latest amendment
annotated in the deposit is Act 21 of 2025 wef 17/08/2026.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance** to ordinary people in Singapore: it
decides who may marry, who must maintain whom, who may seek protection from family
violence, and when a divorce is granted. (An automated count found 0 of the 527
deposited Singapore Acts citing it by its slug title; that count undercounts Acts
cited by short titles and is not a measure of importance.)

The Act runs to several hundred pages, so this row takes void marriages (ss 9, 11,
11A, 12, 13), marrying again during a spouse's lifetime (s 6A), the licence waiting
period and consents for under-21s (ss 17(2), 21A), maintenance of a wife, an
incapacitated husband and children (s 69), protection orders (ss 60, 60A, 63C), and
divorce jurisdiction, the three-year bar and irretrievable breakdown (ss 93, 94, 95,
95A). Not encoded: the prohibited degrees (s 10, First Schedule), the Second Schedule
list of whose consent is needed, solemnisation procedure and caveats, family violence
assessment and enforcement powers, maintenance enforcement (s 71 onward), custody,
division of matrimonial assets and post-divorce maintenance, judicial separation,
nullity procedure, and the Part 10A mediation and parenting provisions.

## What the Act turns out to say

### 1. Six months back together kills an adultery claim, but not a behaviour claim

s 95A(2)(b): if the applicant lives with the respondent "for more than 6 months"
after knowing of the adultery, the applicant "may not rely on that act of
adultery". For behaviour, s 95A(3) only says that 6 months or less is to be
ignored; on the words, a longer period is not a bar. For desertion and living apart,
up to 6 months together keeps the period continuous, but that time "does not count
towards the length" (s 95A(4), (5)), so 24 months of desertion with 3 months back
together is not enough, and 27 months is. The encoding treats more than 6 months
together as breaking the period entirely, which is a simplification. Asserted.

### 2. A married 17-year-old cannot, on the literal words, apply for her own protection order

s 60(2) lists who may apply for family violence against Y: if Y is below 18, a
family member, guardian or carer; only "in any other case" Y. s 60(3) says a person
below 18 may not apply "unless the person is married or was previously married",
which reads as though a married minor might apply for herself, but (2)(a) does not
list Y. The encoding follows the literal words (a married 17-year-old victim may not
apply herself; a family member may). This is a reading, not tested law; the Family
Justice Rules and the protector route (s 60(1)) were not examined beyond the text.
Asserted.

### 3. Two ages for marriage: 18 for validity, 21 for consents

A marriage where either party is below 18 is void unless a special marriage licence
authorised it (s 9). Separately, a "minor" for the consent rules is a person "below
21 years of age" (s 21A(5)), and the Registrar must not issue a licence to a
never-married minor without the Second Schedule consents (or the court's consent in
lieu, or dispensation). A previously married or widowed minor needs none (s
21A(4)). Asserted.

### 4. A husband can claim maintenance only if incapacitated

s 69(1) lets a wife claim on proof of neglect; s 69(1A) gives the same claim to "an
incapacitated husband", defined in s 2 as one incapacitated from earning a
livelihood by disability or illness and unable to maintain himself. An able husband
has no claim under s 69. Child maintenance stops at 21 unless disability, national
service, education or training, or special circumstances justify it (s 69(5), (6));
a child of 21 or over may apply in person, and a sibling of 21 or over may apply
for a child below 21 (s 69(3)). Asserted.

### 5. Marrying again is punished harder when the first marriage was concealed

s 6A: up to 10 years and liable to a fine up to $15,000 where the former marriage
was concealed from the new spouse; up to 7 years and $10,000 otherwise. The
exception for a spouse absent and unheard of for 7 years applies only if the new
partner is told "the real state of facts". Asserted.

### 6. Divorce: three years' marriage, then one of six facts, then "just and reasonable"

No divorce application may be filed until 3 years after the marriage, save with
permission for "exceptional hardship" or "exceptional depravity" (s 94). The court
must be satisfied of one of the six s 95A facts (including, since the Act 3 of 2022
amendment wef 1 July 2024, a written agreement that the marriage has broken down,
which the court must not accept if reconciliation remains reasonably possible), and
that granting the divorce is "just and reasonable" (s 95(2)(c)). Jurisdiction needs
domicile or 3 years' habitual residence of either party (s 93). Asserted.

## What would need doing before this is worth anything

- The prohibited degrees, the Second Schedule consents and the 1 October 2016 start
  date of s 11A are not modelled.
- Periods of more than 6 months together are treated as resetting desertion or
  separation to zero; the text does not say that.
- No Family Justice Rules, subsidiary legislation or case law were read; finding 2
  in particular needs checking against practice.
- Nothing on Part 10 (division of matrimonial assets, custody, post-divorce
  maintenance), where most contested divorces are actually fought.
