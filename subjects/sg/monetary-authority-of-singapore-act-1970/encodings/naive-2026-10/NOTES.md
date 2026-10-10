# Monetary Authority of Singapore Act 1970 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/MASA1970.txt`, with amendments to Act 12 of 2024
(in force 30 August 2024) shown. Large parts (ss 31 to 126, Part 5C, s 177) are
shown as repealed by Act 18 of 2022.

**Checks:** one case file, 110 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**30 of the 527 Singapore Acts** deposited here cite it. It is an institutional
Act: most of it sets up the Authority and lists its powers. This row takes the
rules with decision content: the reserve-deficit rule (s 6(4)), the board's
size, terms, disqualification, quorum and conflicts (ss 7, 8, 10, 12, 13), the
information offences (ss 14A to 14C), immunity and indemnity (ss 22, 22A),
primary dealers for MAS securities (ss 145, 146, 148, 149, 150(6)), and
prosecution and composition (ss 173, 176). Not encoded: objects and functions,
the banking powers in s 23, investment, special loans (s 26), the real-time
gross settlement system, the Financial Sector Development Fund, book-entry MAS
securities (Part 5A), and accounts and audit.

## What the Act turns out to say

### 1. A contractor who leaks or misuses personal data is outside ss 14A and 14B

MAS's own directors, officers and employees must not disclose "any information"
acquired in their duties (s 14A(1)). Contractors, consultants, agents and their
employees are bound only as to information "other than personal data about an
individual" (s 14A(2)), and the same carve-out appears in the misuse offence
(s 14B(2)(a)). So a contractor who discloses or profits from personal data
commits no offence under this Act. That other law (the PDPA, which s 14 names)
reaches it is an inference; s 14A(4) and s 14B(4) preserve such other law.
Asserted.

### 2. Re-identification binds only MAS's own staff

s 14C(1)(c) limits the re-identification offence to a person who "is or has
been a director or an officer or employee of the Authority". A contractor who
re-identifies a person in anonymised MAS data commits no s 14C offence. The
specified-purpose defence needs both a reasonable belief and notice to the
Authority "as soon as was practicable" (s 14C(2)(c)); belief alone fails.
Asserted.

### 3. Misusing information is an offence only if someone gains, or is harmed or loses

s 14B needs a result: a gain for the user or another, harm to an individual, or
a loss to another person. Knowing, unauthorised use with no such result is no
s 14B offence (though disclosure may still offend s 14A). The defendant may
prove, on a balance of probabilities, that the information was "generally
available information" or the use was lawful. Asserted.

### 4. A cancelled primary dealer who appeals keeps trading; one suspended does not get that

s 149(2)(a): an appealed cancellation "does not take effect unless the order is
confirmed" or the appeal is dismissed or withdrawn. Every other order appealed
against "takes effect and must be complied with" meanwhile (s 149(2)(b)). The
appeal window is 14 days from receipt (s 149(1)); a reprimand cannot be appealed
and takes effect on service (s 148(9)); other orders wait 21 days after service
(s 148(7)). Whether s 149(2)(b) brings an appealed suspension into effect before
day 22 the text does not say; the encoding keeps the 21 days. Asserted.

### 5. Being a bank's director bars a MAS director absolutely; the rest is the President's discretion

s 10(1): no one may be appointed as or "remain" a director who is a director or
salaried official of a financial institution licensed or approved by MAS.
s 10(2)'s grounds (bankruptcy, a fraud conviction, three consecutive absences
without leave, failing to disclose an interest under s 13) only allow the
President to terminate. Asserted.

### 6. Quorum is the larger of 4 and a simple majority, and interested directors do not count

s 12(2) as amended by Act 12 of 2024 (which also requires a meeting in every
calendar quarter, s 12(1), (4)). With 14 directors, 7 present is no quorum.
An interested director "must be disregarded" for the quorum on that contract
(s 13(2)(b)), but no board act "may be questioned" for breach of s 13 (s 13(3)).
The chairperson has a casting vote on a tie. Reading "a simple majority of the
directors" as more than half of all directors in office, chair included, is an
inference. Asserted.

### 7. A reserve deficit takes the year's profit first, up to the whole of it

s 6(4): if net profit is larger than the deficit in the General Reserve Fund, at
least enough to clear the deficit must be credited; if not larger, "the whole of
the net profit". Only then may the rest go to the Government (s 6(3)), though
s 6(3A) lets the Authority pay the Government more out of the Fund itself.
Asserted (s 6(3A) is not modelled).

### 8. Penalties, and compounding at half the maximum fine

Information offences: $20,000 or 2 years or both. Acting as a primary dealer
without appointment: $125,000 or 3 years for an individual, $250,000 for others,
plus $12,500 or $25,000 a day for a continuing offence (s 145(7)). Obstructing an
inspection: $50,000 or 2 years, plus $5,000 a day (s 150(6)). No prosecution
without the Public Prosecutor's written consent (s 173); a District Court may
impose the full penalty (s 175). The Authority may compound a prescribed offence
for at most half the maximum fine (s 176(1)), including one compoundable when
committed but no longer (s 176(1A)). Asserted.

## What would need doing before this is worth anything

- s 148(5) reads in the deposit as an opportunity "of being heard by a
  representative in writing, being a period of at least 21 days but not more than
  28 days"; the sentence looks garbled and was not encoded.
- Which offences are prescribed as compoundable, the regulations under ss 14D and
  151, and the Minister's daily-penalty formula under s 148(3) were not retrieved.
- s 176(1A) uses the maximum fine at the time of the offence; only current
  maxima are encoded.
- No case law was searched.
