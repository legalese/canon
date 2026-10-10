# Legal Aid and Advice Act 1995 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/12/2025"), deposited as `../../registers/source-bundle/LAAA1995.txt`. The revised
edition incorporates amendments to 1 December 2021; later amendments are annotated,
the latest being Act 32 of 2024 (in force 1 April 2025) and Act 31 of 2023 (s 5(6),
in force 1 December 2025).

**Checks:** one module, one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Chosen for its everyday-life relevance to ordinary people in Singapore, not by
citation count: it decides who can have a state-funded lawyer for a divorce, a
maintenance claim, a work injury claim or a civil suit, and who can get free legal
advice. This row takes the provisions an applicant or aided person meets: who and
for what (s 5 and the Schedule), the grant decision (s 8), a minor's application
(s 6(3)-(5), s 22A(2)), the 14-day stays (ss 10(3), 17), what a filed Grant of Aid
spares the aided person (s 12(4), (5)), the expenses deposit (s 13), what comes out
of a recovery (ss 16(3), (4), 22A(3), (4)), appeals (s 18), legal advice (s 20), the
offence (s 21) and privilege (s 22).

Not encoded: the Director and the solicitor panels (ss 3, 4, 4A), professional
deputies (s 6A), inquiry powers (s 7), the Minister's authorised persons (s 8(5)-(7)),
applications by both sides (s 11), filing mechanics (s 12(1)-(3), (6)),
court-ordered costs against an aided person (s 14), discharge of the solicitor
(s 15), the rest of s 16, rules of court (s 19), recovery as a debt (s 22B) and the
regulations (s 23). **The means test is prescribed by regulations that were not
retrieved; here it is a bare yes/no.**

## What the Act turns out to say

### 1. Legal advice is open to foreigners living here; legal aid is not

s 5(1) gives legal aid only to "a citizen or permanent resident of Singapore". s 20(1)
makes legal advice available to "persons resident and present in Singapore", with no
citizenship test, so a foreigner resident in Singapore may get advice (if they cannot
afford it in the ordinary way, s 20(4)) but not aid for the case itself. "Present"
is a separate condition: a resident who is abroad does not qualify on the text.
Advice never covers foreign law (s 20(2)). Asserted.

### 2. Who decides the merits depends on the kind of case

s 8(1)(b): for prescribed proceedings the Director alone judges whether there are
reasonable grounds; for every other case it is "a board (consisting of the Director
and at least 2 solicitors on an appropriate panel)". The Minister may override the
means test where it is "just and proper" (s 8(4)(b)) and may authorise aid to anyone
in the public interest (s 8(4)(a)). Reading (4)(b) as still needing the merits limb
is an inference from its cross-reference to subsections (1) and (2). Asserted.

### 3. A minor's means can include the guardian's, but not every guardian's

s 6(4)(b), (5): if the minor is unmarried and the guardian is a "relative", both are
means-tested; otherwise only the minor. "Relative" covers either parent of a
legitimate child, an adopting parent, and "in the case of an illegitimate child, the
mother": an illegitimate child's father acting as guardian is not counted. The same
test decides who pays a contribution (s 22A(2)). Asserted.

### 4. Applying for aid freezes the other side's case for 14 days

s 17(2): once the Director files notice of an application, "all steps in those
proceedings are stayed for a period of 14 days", and time limits stop running, unless
the court orders otherwise. Injunctions, receivers, caveat orders and orders to
prevent "an irremediable injustice" are not stopped (s 17(3)). Cancelling a Grant of
Aid triggers the same 14-day stay (s 10(3)) but s 10 has no list of protected
orders. The counting of days is a reading. Asserted.

### 5. Aid is not wholly free

A filed Grant of Aid removes court fees, service and Sheriff fees, the cost of the
judge's notes, liability for the other side's costs and the Official Assignee's
bankruptcy deposit (s 12(4)), and solicitors may not take a fee from the aided person
(s 12(5)). But that is "subject to sections 13 and 22A": the Director may require a
deposit for out-of-pocket expenses and contributions. Costs recovered go to the
Director (s 16(3), (4)), and an unpaid contribution may be deducted from what is
recovered, except work injury compensation (s 22A(3), (4)). Asserted.

### 6. Two of the three offences carry no "knowingly"

s 21: knowingly making a false statement, failing to make "full and frank disclosure"
of means, or failing to report a change that may make one ineligible: a fine up to
$5,000, up to 6 months, or both. Only limb (a) says "knowingly". Asserted.

### 7. Privilege does not cover means

s 22(2): the solicitor-client privileges "are not to arise in relation to any
information tendered to the Director concerning the property or income of the
applicant". Asserted.

### 8. An appeal needs a fresh application, unless it is interlocutory

s 18: a fresh application within the prescribed time, with the s 8 conditions applied
again; late applications may be considered if a notice of appeal was filed first or
there are extenuating circumstances. Interlocutory appeals are exempt (s 18(3)).
Asserted.

## What would need doing before this is worth anything

- The Legal Aid and Advice Regulations (means criteria, prescribed proceedings,
  prescribed times, contribution rules) were not retrieved; every threshold that
  matters to an applicant lives there.
- The Director's discretions (s 8(3) refusal, s 16(7) and s 22A(6) waivers, s 13(4)
  hardship) are not modelled.
- No case law or Legal Aid Bureau guidance was searched.
