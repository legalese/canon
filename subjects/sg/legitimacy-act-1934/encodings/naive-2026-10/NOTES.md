# Legitimacy Act 1934 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
5/12/2025"), deposited as `LA1934.txt`. The revised edition incorporates amendments
up to 1 December 2021; the latest amendment annotated is Act 19 of 2025 (wef
5 December 2025) against s 4(1). s 3(4) and the Schedule were deleted by Act 17 of
2021 (wef 29 May 2022). The arrangement of sections at the top of the deposit is one
line out of step with the body; this row follows the body.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it decides whether a child born before
the parents married becomes legitimate when they marry, and whether that child, or a
child who stays illegitimate, inherits from a parent who dies without a will. (An
automated count found 2 of the 527 deposited Singapore Acts citing it by title; that
count undercounts and is not a measure of importance.)

The row takes ss 3, 4, 5, 7, 9, 10 and 11. Not encoded: the procedural parts of s 4
(affidavits, costs, citation, rules); s 6 and s 8, which simply apply the general law
"as if" the person were legitimate; the intestacy shares themselves (Intestate
Succession Act); and what "domiciled" means. Dates are numbers in YYYYMMDD form.

## What the Act turns out to say

### 1. An illegitimate child inherits from the mother only if she leaves no legitimate issue

s 10(1): when the mother of an illegitimate (not legitimated) child dies intestate,
the child takes as if born legitimate only if she "does not leave any legitimate issue
her surviving". One legitimate half-sibling shuts the illegitimate child out of the
mother's intestacy. s 10(2) runs the other way: the mother takes from the child as if
"the only surviving parent". The section says nothing at all about the father, so this
Act gives no intestacy right between an illegitimate child and the father. Asserted
(the father point is an observation of absence, not asserted).

### 2. Singapore legitimation needs a registered marriage

s 3(2): "Nothing in this Act shall operate to legitimate a person unless" the marriage
was solemnised and registered under the old Christian or Civil Marriage Ordinances, or
registered or deemed registered under the Women's Charter 1961. Asserted.

### 3. s 3 looks at either parent's domicile; s 9 only at the father's

s 3(1) legitimates if "the father or mother" was domiciled in Singapore at the
marriage. s 9(1), for legitimation by foreign law, looks only at whether "the father"
was domiciled in a country whose law legitimated the child by the marriage, and
applies "notwithstanding" that the father's domicile at the birth did not permit
legitimation. Whether s 3(2)'s registration rule also governs s 9 is not said; this row
does not apply it to s 9 (an inference). Asserted.

### 4. Recognised foreign legitimation can date from 17 May 1934; Singapore legitimation only from 18 May

s 3(1) legitimates "from 18 May 1934 or from the date of the marriage, whichever last
happens"; s 9(1) recognises legitimation "from 17 May 1934 or from the date of the
marriage, whichever last happens". Because s 5(1) lets a legitimated person take in the
estate of an intestate dying "after the date of legitimation", a person recognised
under s 9 with a pre-1934 marriage takes from an intestate who died on 18 May 1934,
while one legitimated under s 3 does not. Whether the one-day difference is deliberate
the text does not say. Asserted.

### 5. A legitimated child ranks as born on the day of legitimation

s 5(2): where property turns on the seniority of a person's children, a legitimated
child ranks "as if he or they had been born on the day when he or they became
legitimated". A child born in 1990 and legitimated in 2000 ranks behind a half-sibling
born legitimate in 1995. Children legitimated by the same marriage rank among
themselves by actual birth. A will can override all of s 5 by a contrary intention
(s 5(3)). Asserted.

### 6. A declaration of legitimacy binds everyone, except those it does not

s 4(1): anyone, "whether domiciled in Singapore or elsewhere, and whether a citizen of
Singapore or not", may apply, and the decree is binding "on the Government and on all
persons whomsoever". But s 4(6) says it does not prejudice anyone if obtained by fraud
or collusion, or anyone not cited or made a party (or claiming through such a party).
Asserted.

### 7. A child who died before the marriage still passes legitimation to its family

s 7: if an illegitimate person dies before the parents marry but leaves a spouse or
issue living at the marriage, and would have been legitimated had they lived, the
spouse and issue take as if the person had been legitimated on the marriage date.
Asserted.

## What would need doing before this is worth anything

- "Domicile" and "registered or deemed to be registered" under the Women's Charter
  are taken as given facts; neither was researched.
- How s 10 interacts with the Intestate Succession Act shares was not read.
- No case law was searched, including on whether s 3(2) reaches s 9.
