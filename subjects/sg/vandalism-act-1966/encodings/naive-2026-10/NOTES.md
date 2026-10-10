# Vandalism Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
incorporates all amendments up to and including 1 December 2021 and comes into
operation on 31 December 2021. No later amendment is annotated.

**Checks:** one case file, 49 assertions satisfied, 0 errors.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. The Act is eight short
sections, so this row encodes every operative one: the definition (s 2), the
offence and punishment (s 3), production of written authority on demand (s 4),
seizure (s 5), arrestable and non-bailable (s 6), the presumption on receiving
stolen public property (s 7) and revocation of a secondhand goods dealer's licence
(s 8). The arrangement of sections at the head of the deposit is numbered one out
of step with the body; the body's numbers are used.

Not encoded: what ss 325(1) and 330(1) of the Criminal Procedure Code 2010 say (the
caning is "subject to" them; here a single input flag), what "arrestable" and
"non-bailable" entail, and the content of s 411 of the Penal Code 1871.

## What the Act turns out to say

### 1. Caning is mandatory, and the exception is narrow

s 3: on conviction the offender "shall also ... be punished with caning with not
less than 3 strokes and not more than 8 strokes". The only exception is a **first
conviction** for marking with "pencil, crayon, chalk or other delible substance",
or for posting a notice or hanging a flag. Marking in paint, or stealing, destroying
or damaging public property, attracts mandatory caning even on a first conviction;
a second poster offence does too. The fine (up to $2,000) and imprisonment (up to
3 years) are alternatives to each other; the caning is in addition. Asserted.

### 2. Damaging private property is not vandalism under this Act

Paragraph (b) of the definition is "stealing, destroying or damaging any **public**
property". Private property comes in only through paragraph (a): marking, posting
and flag-hanging without the owner's or occupier's written consent. (Whether
damaging private property is an offence under some other law was not read.)
Asserted.

### 3. Written permission cures paragraph (a), not paragraph (b)

Paragraph (a) is qualified by "without the written authority" (public property) or
"without the written consent of the owner or occupier" (private property).
Paragraph (b) carries no such qualifier, so the encoding treats damaging public
property as vandalism even with written authority. That is a literal reading; the
text does not say whether authorised destruction (say, a demolition) is meant to be
caught. Asserted.

### 4. Failing to show the permission slip is itself arrestable and non-bailable

s 4: the written authority or consent must be produced on demand to police,
Special Constabulary, Auxiliary Police, or the military police of the SAF or of a
lawfully present armed force; failure is an offence with a fine of up to $500. s 6
makes "every offence" under the Act arrestable and non-bailable, which on its words
includes this $500 offence. A private security guard or a town council officer is
not on the s 4(1) list, and neither can seize under s 5. Asserted.

### 5. Receivers of stolen public property are presumed to know

s 7 reverses the burden in a prosecution under s 411 of the Penal Code 1871 where
the stolen property is public property: knowledge and dishonesty are presumed
"until the contrary is proved". s 8 makes revocation of a secondhand goods dealer's
licence or exemption mandatory ("shall") on such a conviction. Asserted.

### 6. "Public property" is wider than the Singapore Government

It includes property of "the government of any Commonwealth or foreign country",
any statutory body or authority, and any armed force lawfully present in Singapore.
Asserted.

## What would need doing before this is worth anything

- Read ss 325(1) and 330(1) of the Criminal Procedure Code 2010 and replace the
  input flag with their actual conditions.
- Check whether "causes any such act to be done" and "attempts" carry the same
  caning rule; the encoding treats all three forms of the offence alike, as s 3's
  wording suggests.
- No case law on authorised destruction of public property or on the delible /
  indelible line was searched.
