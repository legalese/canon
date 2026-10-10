# International Arbitration Act 1994 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, with amendments to Act 5
of 2025 (in force 9 March 2025) shown. The deposit labels itself "Current version as
at 01 Oct 2026". The arrangement of sections at the top of the deposit does not match
the body (it numbers "Court may set aside award" as 22); this row follows the body,
where setting aside is s 24 and arbitrator liability s 25.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the questions
a party or practitioner meets first: whether Part 2 and the Model Law govern the
arbitration (ss 5, 15, 26), whether the agreement is in writing (s 2A), the stay of
court proceedings (s 6), the default number and appointment of arbitrators (ss 9,
9A), the deadline to challenge a jurisdiction ruling (s 10(3)), security for costs
against foreign claimants (s 12(4)), setting aside (s 24 and Model Law Article 34) and
refusing enforcement of a foreign award (s 31). Tribunal and court interim powers,
orders to attend, conciliation, interest and costs, privacy and reporting of court
proceedings, immunities, the IPR Part, limitation and the three-party appointment
rule are not encoded.

## What the Act turns out to say

### 1. Singapore's test for "international" is wider than the Model Law's

Model Law Article 1(3)(a) asks whether the parties have their places of business "in
different States". s 5(2)(a) displaces it ("Despite Article 1(3)") with a test met if
"at least one of the parties" has its place of business in any State other than
Singapore. Separately, two Singapore firms are in an international arbitration if
they choose a seat outside Singapore (s 5(2)(b)(i)), or if a substantial part of the
obligations is to be performed abroad (b)(ii). Two Singapore firms with a Singapore
seat and Singapore performance are not, unless they agree in writing that the Part or
the Model Law applies (s 5(1)). Asserted.

### 2. Adopting institutional rules does not opt out; saying so expressly does

s 15(1): an express agreement that the Model Law or Part 2 is not to apply, or that
the Arbitration Act 2001 is to apply, takes the arbitration out of Part 2. s 15(2): a
reference to rules of arbitration "is not of itself sufficient". Arbitrations
commenced before 27 January 1995 are outside Part 2 unless the parties agreed in
writing otherwise (s 26(1)). Asserted.

### 3. A mistake of law or fact is not a ground for setting aside

Article 34(1) makes setting aside the "only" recourse and (2) lists the grounds "only
if". s 24 adds two: fraud or corruption, and a prejudicial breach of natural justice.
Neither list includes an error of law or fact; s 25(b) separately exempts the
arbitrator from liability for "any mistake in law, fact or procedure". The
application must be made within three months of receiving the award, or of the
disposal of an Article 33 request. Treating exactly three months as in time is an
inference. Asserted.

### 4. The grounds for refusing a foreign award are a closed list, and not the same list

s 31(1): enforcement may be refused in the cases in subsections (2) and (4) "but not
otherwise". s 31(2)(f) (award not yet binding, or set aside where made) has no
counterpart in Article 34. s 24's fraud and natural-justice grounds are not in s 31
as such. Whether they can be raised through (2)(c) or the public-policy ground in
(4)(b) is something the text does not answer, so the encoding says no. Asserted.

### 5. A stay is mandatory, but the window closes once the defendant engages on the merits

s 6(2): the court "is to make an order" staying the proceedings unless the agreement
is "null and void, inoperative or incapable of being performed". Under s 6(1) the
application comes after the notice of intention to contest and before any pleading
(except one disputing jurisdiction) or "any other step". Asserted.

### 6. Short default clocks

If the parties set no number, there is one arbitrator (s 9). With two parties and
three arbitrators, the appointing authority (the president of the SIAC Court of
Arbitration, s 8(2)) appoints the third on a party's request once 30 days pass
without agreement (s 9A(2)). A jurisdiction ruling can be taken to the General
Division of the High Court within 30 days of notice (s 10(3)). Asserted.

### 7. Being foreign is not, by itself, a reason for security for costs

s 12(4): security must not be ordered "by reason only" that the claimant lives
abroad or is a foreign-incorporated or foreign-managed body. The encoding says
only that s 12(4) does not bar other reasons; whether they succeed is for the
tribunal. Asserted.

## What would need doing before this is worth anything

- The Model Law (First Schedule) was read only for Articles 1(3) and 34; Articles 8,
  10, 11, 16 and 36, which the Act modifies or displaces, were not encoded.
- s 5(2)(b) speaks of "the State in which the parties have their places of business";
  the encoding takes this as a yes/no input and does not model parties in
  different States, multiple places of business or habitual residence (s 5(3)).
- No case law on public policy, natural justice or the stay was searched.
