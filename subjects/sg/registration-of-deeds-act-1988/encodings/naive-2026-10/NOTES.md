# Registration of Deeds Act 1988 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 October 2025. The deposit's arrangement of sections runs one ahead of the body
(it lists "Short title" as s 2); the encoding follows the body.

**Checks:** three case files, 331 assertions satisfied, 0 errors, 0 warnings.

## Why this Act

A citation count across the 527 Singapore Acts deposited in this repository found
**37 Acts that cite the Registration of Deeds Act 1988**, for an Act of 66,000
characters, about half of which is legislative history. It governs land that is
**not** under the Land Titles Act 1993, the "common-law" or "old-system" title, and
so is the other half of the picture the `land-titles-act-1993` row draws.

## Scope

The **whole Act** except s 3 (appointing the Registrar), s 29 (rules), the
continuity provisions in s 31(1), (2), (4) and (5), and the legislative history.

**No rules under the Act were retrieved.** The forms, the fees, the survey
dispensation under s 13(2) and the exemptions s 29(1)(h) and (i) allow all live
there.

## What the Act turns out to say

### 1. Not registering makes an assurance inadmissible, not void

s 4: an unregistered assurance affecting land in Singapore "is not admissible in
any court as evidence of title to the land". The Act does not say the assurance is
void or passes nothing. The sanction is evidential. Asserted.

### 2. A provisional registration can stay in limbo indefinitely

s 7(1): provisional registration becomes complete, with retrospective effect to
the provisional date and time, "on compliance with section 13(1)" (or with all of
it except (c), the survey condition, if that has been dispensed with). s 7(4):
after **six months** the provisional registration is **void** if s 13(1) "(other
than paragraph (c))" has not been fully complied with.

So an instrument that is stamped, free of demanded land-revenue arrears, paid for
and lawful, but whose land has **not been surveyed** and has no dispensation, is
neither complete under s 7(1) nor void under s 7(4). It stays provisionally
registered, at six months or seven years. The Act does not say what priority it
has in that state. Asserted at five months and at seven years.

### 3. Residential property loses the backdating, and nothing replaces it

s 7(5): s 7(1) "does not apply to any assurance in respect of any estate or
interest in any residential property within the meaning of the Residential
Property Act 1976". So a residential assurance gets no retrospection to the
provisional date. And because s 7(1) is the only provision that says when
provisional registration becomes registration, the Act states **no date of
registration at all** for it. Asserted as that absence.

### 4. Equitable liens are worthless against a buyer for value until a signed memorandum is registered

s 6(2): an unpaid vendor's lien, a charge by deposit of title deeds, "or
otherwise" has no "effect or priority" against an assurance for valuable
consideration until a memorandum is registered. The memorandum must be signed by
the person against whom the lien is claimed (s 6(1)), so a purchaser who will not
sign leaves the unpaid vendor with a caveat. A gift (no consideration) does not
defeat the lien. Asserted.

### 5. The Registrar does not test a caveat's merits or its notice

s 8(4) requires refusal of a caveat that discloses no interest or does not
identify the lot. s 8(6): "the Registrar must not be concerned to consider whether
or not a caveator's claim is justified." s 8(7): a claimant-caveator must serve
notice by registered post on the proprietor and prior claimants, "and the
Registrar must not be concerned to inquire whether or not the notice has been
effected." A groundless caveat in proper form, never notified, is registered and
stands for **five years** (s 8(9)) unless withdrawn or cancelled by the court.
Asserted.

### 6. Back-dating by caveat needs the same interest and the same person

s 8(8): a later assurance in favour of the caveator (or the named caveatee)
conveying **the same estate or interest** as the caveat describes, presented while
the caveat is in force, takes the caveat's registration date "for all purposes". A
lease to a caveator whose caveat claimed a purchase gets nothing, nor does a
conveyance after the five years have run. Asserted.

### 7. Notice is irrelevant to priority; only actual fraud by the registrant defeats it

s 14(1): priority by date of registration, not date of execution. s 14(3):
priorities have full effect "except in cases of actual fraud, to which the person
by or on whose behalf the registration is made is a party", and no one loses
priority "merely in consequence of the person having been affected with actual or
constructive notice". A purchaser who registers first, **knowing** of an earlier
unregistered conveyance, wins. s 14(4) keeps volunteers in their grantor's shoes
and preserves the voidness of dispositions in fraud (for instance of creditors).
s 14(2): where two instruments are registered on an identical date, the Act
says nothing about their priority. Asserted.

### 8. Tacking needs authorisation or agreement; mere knowledge is not enough

s 15: a further advance ranks ahead of a later mortgage only if the prior mortgage
authorises further advances or revolving credit, or the subsequent mortgagee
**agrees**. s 15(2): otherwise "the right to tack does not apply to mortgages".
A second mortgagee who knew and said nothing has not agreed. "Prior mortgage"
includes a charge protected only by an accepted caveat (s 2(1)). Asserted.

### 9. Fiduciaries who rely on a search certificate are immune from its errors

s 23: a solicitor, trustee, executor, agent or other fiduciary who obtains an
official search certificate or certified copy "is not answerable for any loss,
damage or injury that arises from any error" in it. No good faith or reasonable
care condition is written in. Asserted across five fiduciaries and two documents
(and not for an informal enquiry or a non-fiduciary).

### 10. Rectification has no time limit; refusing to produce is prison-only

s 24(1): any person claiming an interest in land in Singapore may apply "at any
time". s 24(7): a custodian who "refuses or neglects" to produce an instrument
under a rectification order commits an offence punishable by imprisonment of up to
**two years**. No fine is provided, and **neglect** (forgetting) is enough.
Asserted.

### 11. The short-lease exclusion counts options and ignores break clauses

s 25(1): the Act does not extend to a lease of up to **seven years** with actual
possession from the making. s 25(2): a lessee's right or option to extend counts as
part of the term, and the possibility of earlier determination is ignored. So a
5-year lease with a 3-year option is an 8-year lease and is within the Act; a
3-year lease without possession is within the Act; and "lease" includes an
agreement for a lease (s 2(1)). Asserted.

### 12. The pre-1988 short-lease rule ignores possession

s 31(3): a lease "for a term exceeding 3 years but less than 7 years" made before
30 November 1988 and never registered may be registered "despite section 25", and
"unless so registered is not admissible in any court as evidence of title". It
does **not** exclude leases with possession. A five-year lease with possession
made in 1985 is inadmissible unless registered; the same lease made in 1990 is
outside the Act. A pre-1988 lease of exactly seven years, or exactly three, is
caught by neither branch of s 31(3). Asserted.

### 13. Service is at the last known address in Singapore, not the address for service

s 8(2)(a) requires a caveat to state the parties' "addresses for the service of
notices under this Act". But s 30(1) deems service only where a notice is sent by
registered post "to the person's last known address in Singapore", even if
returned. A party whose stated address for service is abroad is not within the
deeming at all. s 30(2) disapplies s 72 of the Conveyancing and Law of Property
Act 1886 for notices to proprietors. Asserted.

### 14. Smaller things worth recording

- **s 11:** personal appearance before the Registrar is the rule in form and the
  exception in practice. Certification by an advocate and solicitor, a consular
  officer, or a notary in the country of execution displaces it; where no notary
  practises, the executant's own advocate and solicitor may certify (s 11(7)).
- **s 13(1)(b):** land-revenue arrears block registration only once **demanded**.
- **s 13(3):** the Collector may correct a wrong lot or area endorsement if all
  parties **who can be found within Singapore** admit the error. Absent, dead or
  emigrated parties do not stop it.
- **s 26:** the Registrar's wilful misconduct: up to **seven years**, with a fine of
  no stated maximum. **s 27:** false statements, impersonation and the like,
  committed by anyone: $5,000 or three years. Careless or innocent falsity is not
  an offence.
- **s 21(3):** a certified copy proves contents but does not dispense with the
  original where it is otherwise required, nor prove due execution.

## Relation to other rows

`subjects/sg/land-titles-act-1993/encodings/naive-2026-10/` encodes Part 17 of the
Land Titles Act, which converts land from this Act's register into the Torrens
register. The two rows are not linked by IMPORT.

## What would need doing before this is worth anything

- **Retrieve the Registration of Deeds Rules.** The survey dispensation, the
  forms and the fees all depend on them, and s 29(1)(h) and (i) allow exemptions
  this row does not contain.
- **No case law was searched.** Findings 2, 3, 7, 12 and 13 are readings of
  drafting that a court may have explained. s 14(3)'s "actual fraud" in particular
  has a body of case law behind it in other jurisdictions.
- Whether land is "residential property", whether a claim discloses an "estate or
  interest", and whether fraud is "actual" are taken as supplied facts.
- Dates are plain numbers (months, years); no calendar arithmetic.
