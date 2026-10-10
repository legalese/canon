# Guardianship of Infants Act 1934 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021),
informal consolidation, "version in force from 2/1/2025", deposited as
`../../registers/source-bundle/GIA1934.txt`. The latest amendments annotated are
Act 3 of 2022 and Act 18 of 2023, both in force 2 January 2025 (s 5A(6) to (8)).

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its **everyday-life relevance**: it is the Act under which a parent
asks the court for custody, access or maintenance of a child, enforces an access
order the other parent has broken, or names a guardian for a child by will. It
is short (21 sections), so the row covers most of it: ss 3 to 8, 11, 11A, 16 to
18 and 21. Not encoded: attachment of pensions and income (s 9), trusts for
maintenance (s 12), production and return of an infant (ss 13, 14), security and
accounts (s 15), small estates (s 19), applications for directions (s 20), and
the rest of s 5A (compensation, programmes, bonds, Family Court procedure, High
Court orders).

## What the Act turns out to say

### 1. Breaking an access order can mean prison, per breach

s 5A(3)(e): "for every breach of the access order" the court may fine the parent
who denied access up to $20,000 or imprison them up to 12 months, or both. The
encoding multiplies the maxima by the number of breaches (three breaches: up to
$60,000); whether sentences run consecutively is not said, so that total is the
encoding's reading. The court may also order make-up access, which under s 5A(4)
"must not give X more access than what X is entitled to under the access order"
— measured against the entitlement, not the access denied. Asserted.

### 2. Enforcement or contempt, not both

s 5A(6) (in force 2 January 2025): for a given breach X "may do either, but not
both" of applying to enforce under s 5A and bringing contempt proceedings.
Asserted.

### 3. Only parents and Act guardians can apply for custody under s 5

s 5 orders on custody, access and maintenance are made "upon the application of
either parent or of any guardian appointed under this Act". A grandparent or the
child has no standing under s 5 itself. By contrast s 6(3) lets "any person"
apply to be appointed guardian, but only where the infant has no parent, no
guardian of the person and nobody else with parental rights. Asserted.

### 4. A testamentary guardian can be shut out by the surviving parent

Either parent may appoint a guardian "by deed or will" (s 7(1), (2)) — a letter
or an oral wish is not enough. The appointee acts jointly with the surviving
parent "unless the mother or father objects" (s 7(3)); if they object, the
appointee's remedy is to apply to the court, which may leave the parent as sole
guardian, order joint guardianship, or make the appointee sole guardian (s 7(4)).
Where no guardian was appointed, or the appointee is dead or refuses to act, the
court may appoint a co-guardian (s 6). Asserted.

### 5. A guardian of property is held to $100 a month

s 18(1): a guardian of an infant's property may spend income on maintenance and
education, but "no sum exceeding $100 per month" without the court's permission;
capital needs a court order (s 18(2)). s 16(1) requires the court's permission to
sell, mortgage, exchange or part with possession of any of the infant's property,
or to lease land "for a term exceeding one year" (a 12-month lease does not need
it; 13 months does). A disposal in breach "may be declared void" (s 16(2)) — it
stands until declared. s 18(1) and s 16(1) carry the annotation "[Act 25 of 2021
wef 15/10/2024]"; the deposit does not show what that amendment changed. Asserted.

### 6. The Act never says who an "infant" is

s 2 defines only "court". No age is given for "infant", and s 11(b) requires the
court to consider the infant's wishes "where the infant is of an age to express an
independent opinion", again without an age. s 5A switches to "child". The age of
majority must come from elsewhere (an inference; not checked). The encoding takes
both as inputs. Asserted (s 11(b) only).

### 7. Welfare first, and advice that need not be followed

s 3 makes welfare "the first and paramount consideration" and denies either parent
a superior right "save insofar as such welfare otherwise requires". On custody,
s 11A requires the court, "whenever it is practicable", to have regard to advice
from someone trained or experienced in child welfare, "but shall not be bound to
follow such advice". s 11A asserted; s 3 is quoted, not encoded.

## What would need doing before this is worth anything

- The Act 25 of 2021 changes to ss 16 and 18 and the Act 18 of 2023 change to s 11
  were not traced to the amending Acts.
- The Family Justice Rules referred to in s 5A(7) were not retrieved.
- No case law on custody, access or the s 5A penalties was searched.
- The relationship with the Women's Charter 1961 (custody and maintenance on
  divorce) was not examined.
