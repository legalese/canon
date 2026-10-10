# Oaths and Declarations Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1 December 2023, with the amendment by Act 25 of 2023 (s 15(2A)) shown.

**Checks:** one case file, 87 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. The Act is short (19
sections). This row takes the provisions with decision content: who must swear and
the alternatives of affirmation and caution (ss 4-6), the effect of an omitted or
irregular oath (s 8), before whom a statutory declaration must be made in and
outside Singapore (ss 11, 12), the false-declaration offence and its maximum terms
(s 14), and oaths of office and judicial oaths, including by video link (ss 15, 16).
Not encoded: the power to administer oaths (s 3), form and manner left to the Rules
of Court (s 7), ss 9, 10 and 13 beyond their pointer to ss 11-12, regulations and
Schedule amendment (ss 17, 18) and savings (s 19). Who is a "prescribed person"
under s 11(1)(b) is left to regulations, which were not retrieved.

## What the Act turns out to say

### 1. Remote oath-taking in this Act covers only oaths of office and judicial oaths

s 15(2A), added by Act 25 of 2023 with effect from 1 December 2023, allows an oath
under s 15(1) or (2), or an affirmation under s 16, to be taken "through a live video
link or live television link" if the administrator can maintain visual contact and
communicate throughout, confirm identity, and (if the oath is to be subscribed)
verify it by inspection. Nothing in this Act's text extends that to a witness's oath
under s 4 or to a statutory declaration under s 11. Whether other written law does
was not checked. Asserted.

### 2. The geography of who may take a declaration has gaps

In Singapore (s 11(1)(b)): a court, a person acting judicially, or a prescribed
person. In the UK or the Commonwealth (s 12(1)): a local notary public, justice of
the peace, or person authorised by local law. Outside the Commonwealth (s 12(2)): a
consul or vice consul, or a person authorised by local law. Read as written, a consul
is not named for a Commonwealth country, and a notary public is not named for a
non-Commonwealth place; each qualifies there only through local-law authority. The
First Schedule form is required by s 11(1)(a) for declarations made in Singapore; s
12 says nothing about form. Asserted.

### 3. A false declaration used in an investigation carries 7 years, not 3

s 14(1)(c): up to 7 years where the declaration is made or used "in any stage of a
judicial proceeding"; otherwise up to 3 years (d); a fine may be added in both.
s 14(2) treats a subordinate military court trial as a judicial proceeding, and an
investigation "directed by law that is preliminary to a proceeding before a court",
or one directed by a court, as a stage of one. Prosecution needs the Public
Prosecutor's written consent (s 14(4)). Asserted.

### 4. A declaration made abroad is caught only if meant for Singapore

s 14(3) applies the making limb (1)(a) to a declaration made outside Singapore "if
the person knows or has reason to believe that the statutory declaration is intended
to be used in Singapore". This encoding treats a declaration made abroad without that
knowledge as outside (1)(a) — an inference from (3), which would otherwise do
nothing. The use limb (1)(b) covers a declaration "made in or outside Singapore"
without that condition. Asserted.

### 5. A missing oath does not spoil the evidence, or the duty to be truthful

s 8: no omission to swear, affirm or caution, and no irregularity of form or manner,
may invalidate proceedings, make evidence inadmissible, or affect the obligation to
state the truth. Asserted.

### 6. Affirmation and caution are alternatives, on stated grounds only

s 5: affirmation instead of oath for a person "of some other religion according to
which oaths are not of binding force" (Hindus and Muslims are named) or with a
conscientious objection; s 16 gives office holders the same choice, with "So help me
God" omitted. s 6: a person too young, in the court's opinion, to swear or affirm
"may" be cautioned instead. The encoding reads s 6 as excluding oath and affirmation
once that opinion is formed — an inference. Official court interpreters and
certificated public-service interpreters already sworn to their duties need not swear
again (s 4(2)). Asserted.

## What would need doing before this is worth anything

- The regulations naming "prescribed persons" under s 11(1)(b) were not retrieved.
- Other written law conferring power to administer oaths or take declarations
  (ss 3(2), 11(2), 15(3)) was not read, and may overtake findings 1 and 2.
- The Rules of Court prescribing the form of witness oaths (s 7) were not read.
- No case law was searched, including on the s 6 reading and the s 14(3) inference.
