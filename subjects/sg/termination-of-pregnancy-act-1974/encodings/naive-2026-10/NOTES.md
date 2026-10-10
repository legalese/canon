# Termination of Pregnancy Act 1974 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, "version in force from
5/12/2025", as deposited at `../../registers/source-bundle/TPA1974.txt`. The cover
says the revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated in the text is Act 19 of 2025 (wef 5 December 2025), which
rewrote the definition of "approved institution" by reference to the Healthcare
Services Act 2020.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it decides whether, where, by whom and
how late in a pregnancy a woman in Singapore may have a pregnancy terminated, and it
protects her against coercion and her records against disclosure. This row takes
the protection from the abortion offences (s 3(1)), who and where (s 3(2), s 10),
who may have a termination (s 3(3)), the duration limits (s 4), the s 3 offence
(s 3(4)), coercion (s 5), conscientious objection (s 6), disclosure (s 7) and the
maximum penalties.

Not encoded: the definitions as such (s 2), the inspection power (s 8) and the
regulation-making power (s 11). The regulations were not retrieved, so who is an
"authorised medical practitioner", the "prescribed" qualifications and period, the
"prescribed" persons and purposes for disclosure, and the form of consent are each
a yes/no fact here. The Act says nothing about the consent of a minor's parent or of
a husband; nothing here adds any.

## What the Act turns out to say

### 1. Breaching the week limits is not itself an offence under this Act

s 4 forbids treatment beyond 24 weeks without necessity, and between 16 and 24 weeks
by an unqualified practitioner, but it has no penalty clause. The only penalty for
treatment, s 3(4), reaches a person who contravenes "this section", i.e. s 3. So an
authorised practitioner in an approved institution terminating a citizen's
pregnancy at 30 weeks without necessity does not commit the s 3(4) offence. Such a
termination does fall outside s 3(1), which protects "Subject to the provisions of
this Act", and so back under Penal Code ss 312 to 315; that last step is an
inference, since the Act does not say it in terms. Asserted (the s 3(4) result and
the loss of protection as encoded).

### 2. A pregnancy of exactly 24 weeks falls between the two limbs

s 4(1)(a) applies to a pregnancy "of more than 24 weeks' duration"; s 4(1)(b) to one
"of more than 16 weeks' duration but less than 24 weeks' duration". Read literally,
exactly 24 weeks is in neither, so no s 4 restriction applies to it. s 4(2), which
counts "to the end of the 24th week", may be meant to close the gap; that is not
decided here. Encoded literally. Asserted.

### 3. The residence rule yields only to a threat to life, not to grave injury

s 3(3) limits treatment to citizens and citizens' wives, work-pass holders and their
wives, and women resident at least 4 months before the treatment. Its exception is
treatment "immediately necessary to save the life of the pregnant woman". Unlike
s 4(1)(a) and s 6(3), it does not mention preventing "grave permanent injury". So a
visitor facing grave permanent injury, but not death, is not eligible. Asserted.

### 4. Drug-only treatment escapes both the hospital rule and the qualification rule

s 10: where treatment "consists solely of the use of drugs prescribed by an
authorised medical practitioner", it need not be in an approved institution and the
practitioner need not hold the prescribed qualifications or skill. The second relief
reaches the 16-to-24-week limb of s 4(1)(b), so an ordinary authorised practitioner
may prescribe drug-only treatment at 20 weeks. s 10 does not touch the 24-week limit
or the residence rule. Asserted.

### 5. Conscientious objection gives way only in an emergency

s 6(1) frees anyone with a conscientious objection from any contractual or legal duty
to participate; the burden is on the objector, and testifying on oath or affirmation
may discharge it (s 6(2)). By s 6(3) it does not affect a duty to participate in
treatment "immediately necessary to save the life or to prevent grave permanent
injury". Asserted (the s 6(2) burden is not encoded).

### 6. Coercion and disclosure are separate offences

Compelling or inducing a woman against her will, by coercion or intimidation, to
undergo treatment is an offence ($3,000 or 3 years, s 5). Anyone who keeps the
records or takes part must not disclose facts about the treatment without her
express consent, except to prescribed persons for prescribed purposes ($2,000 or 12
months, s 7). Asserted.

## What would need doing before this is worth anything

- The Termination of Pregnancy Regulations were not retrieved: authorisation of
  practitioners, prescribed qualifications and period, prescribed disclosures and
  the consent form are all left as facts.
- Penal Code ss 312 to 315 were not read; finding 1's step back into them is an
  inference.
- How "4 months" of residence and the week count are measured at the margins is not
  decided; no case law was searched.
