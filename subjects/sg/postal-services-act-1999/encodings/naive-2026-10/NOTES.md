# Postal Services Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text following the conventions of the
`writing-l4-rules` skill as shown in the example rows (the skill itself was not
loadable in this session) and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/PSA1999.txt`. The edition says it incorporates
amendments up to 1 December 2021; later amendments are annotated in the text, the
latest being Act 15 of 2026 (wef 1 July 2026), with Act 30 of 2021 (wef 2 November
2022) and Act 25 of 2021 (wef 1 April 2022). The arrangement of sections at the top
of the deposit is out of step with the body (it lists "Postage stamps" as s 18; the
body has s 19). Section numbers here follow the body.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**8 of the 527 Singapore Acts** deposited here cite it. This row takes the rules an
ordinary sender, courier, building owner or parcel-locker user meets: what a letter
is, the Postal Authority's monopoly on carrying letters and its exceptions, stamps
bearing "Singapore", keeping or opening other people's mail and locker parcels,
prohibited items in public parcel lockers, rival parcel lockers on specified
premises, the penalties, composition and the licensee's exclusion of liability.
Licensing machinery, the Postal Authority's powers, the parcel-locker installation
and entry powers, codes and directions, control of designated licensees,
international matters and most enforcement powers are not encoded.

## What the Act turns out to say

### 1. Carrying a fourth letter for a friend is an offence

s 4 gives the Postal Authority "the exclusive privilege of conveying from one place to
another letters", and s 33 makes it an offence to convey a letter without a s 6
licence, "Subject to section 5". The first s 5 exception is "letters not exceeding 3
in number" carried without reward. A neighbour carrying 3 letters for free is
outside s 33; carrying 4 is inside it, and no penalty being expressed, s 52 applies
(up to $10,000 or 3 years). Asserted.

### 2. "Letter" stops at 500 grams and excludes catalogues and newspapers

s 2(2): a letter is a written communication on a physical medium "not exceeding 500
grams in weight", delivered otherwise than electronically to a particular addressee
or address, and "does not include any book, catalogue, newspaper or periodical". A
600-gram document and an email are not letters, so the monopoly does not reach them.
Asserted.

### 3. The monopoly exempts paid direct mail and messenger services, but not a paid consignee's letter

s 5(1)(d) and (e) exempt direct mail, letters carried by the sender personally, and
intra-organisational mailroom and messenger services, with no condition about reward.
The "Consignee's letter" exception in s 5(1)(c) applies only "without hire, reward or
other profit", so a consignee's letter carried for a fee is not exempt. Asserted.

### 4. Only HDB common property, not condominium common property, is protected for the public parcel locker network

s 39G makes it an offence for anyone other than the public parcel locker network
operator to provide or operate a parcel locker on "specified premises". s 23A lists
HDB common property, bus interchanges, railway premises, People's Association
community centres and premises prescribed by Ministerial order. Condominium common
property and shopping malls are not listed, so a locker there is not within s 39G
unless prescribed. Asserted.

### 5. A parent may open a child's letter but may not keep it in transit, and an addressee cannot authorise anyone

s 36(2) exempts a parent or guardian of a minor or ward addressee, but only from
s 36(1)(b) (opening or impeding delivery of a letter), not from (1)(a) (retaining a
postal article in transmission). s 36 has no exception for the addressee's consent.
By contrast, s 39I(2)(a), for parcels collected from a public parcel locker, expressly
excuses a person "the intended recipient of the parcel authorises". Asserted.

### 6. Penalties range from $5,000 to $50,000, and composition is capped at the lower of $5,000 and half the maximum fine

Damaging postal plant (s 31) or a public parcel locker (s 39E): $50,000 or 3 years.
A postal officer's fraudulent marking (s 34(2)) or defacing a parcel's identifying
mark (s 39H(2)): $5,000 or 12 months. Disfiguring postal plant (s 29(7)): a fine up to
$10,000 with no imprisonment, plus $1,000 a day continuing. Everything else: s 52.
s 51 caps a composition sum at "the lower of" $5,000 and half the maximum fine, so a
$5,000 offence compounds for at most $2,500. Which offences are compoundable is left
to regulations (s 51(3)), not read. Asserted.

### 7. The licensee's exclusion of liability does not cover its own default

s 57(1) excludes a public postal licensee's liability for loss, misdelivery, delay,
service failure, loss of secrecy and remittance errors only where "due to the act or
default of another person, or an accident or some other cause beyond the control of"
the licensee. Asserted.

### 8. Prohibited items in a locker: knowledge matters

s 39J(2) excuses a person who "does not know, and has no reason to believe" that the
thing is a prohibited item. Asserted.

## What would need doing before this is worth anything

- Treating the Postal Authority and its staff as outside s 33 is an inference from
  s 4(2); s 33 itself speaks only of acting without a s 6 licence.
- The Minister may vary the s 5 exceptions by Gazette order (s 5(2)) and prescribe
  further specified premises (s 23A); no orders were retrieved.
- Regulations prescribing compoundable offences and non-transmissible articles were
  not read.
- The continuing-offence further fine is encoded per day; "or part of a day" is not
  modelled.
- No case law was searched.
