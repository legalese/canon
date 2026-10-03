# Encoding notes -- Cat Act 2011 (WA), LQA run, steps 4A and 5A

Against the Cat Act 2011 compilation 00-l0-01 (currency start 25 Sep 2025) and the Cat
Regulations 2012 compilation 02-b0-00 (currency start 24 Jul 2025). Written 2026-10-01.

**These are not findings.** Each entry is a question the encoding forced, a choice it made, or
something that looked wrong, with the provision and how it was noticed. Step 7A (Probe) decides
which become candidates, and records `found_by` honestly: an entry noticed by a casual read is
`RD` even though it is written down here. No incidents.json exists. **No human gate (6H) has
been granted over this encoding.** The parliamentary documents in `sources/internal/` were not
read for this step.

How noticed: **ENC** writing the L4 or the scheme forced it; **CHK** the compiler or a checker
reported it; **TST** a case surfaced it; **RD** visible on reading the provision.

Entries N-01 to N-07 are about the tools and the pipeline, not the law (they belong to the
harness and corpus registers, not the incident register).

---

## Tools and pipeline

**N-01. A subject cannot import the jurisdiction library module.** (CHK) `l4` resolves an
`IMPORT` by bare module name in the importing file's own folder and in two library folders; a
relative path (`IMPORT "../x.l4"`, ``IMPORT `../lib/x` ``) is a parse error or resolves to the
basename. So `_jurisdiction/library/wa-interpretation-act-1984.l4` cannot be imported from this
subject. The subject holds a byte-identical copy, `wa-interpretation-act-1984.l4`, which is what
the modules compile against. Both files had sha256
`7e97e6f5ab7c0297ee55724a6211b76d12832360072ba4008776e5ec66faa429` at 4A. A reviewer at 6H should
re-check that they still match; nothing enforces it. The pipeline's "reused from the
jurisdiction library" has no working mechanism in this toolchain.

**N-02. No standard library (corpus H-04 still holds).** (CHK) `IMPORT daydate` and `IMPORT
prelude` resolve to nothing, so the calendar (leap years, day numbers, weekdays) is built inside
the Interpretation Act module from date components. It is asserted against IA s. 62's own
examples, but it is a hand-built calendar, not `daydate`.

**N-03. Infix mixfix calls fail to parse after `...` or `..` when the first argument is
parenthesised, and with a string literal as the first argument.** (CHK) `... (o's \`name\`)
\`is an owner of\` c \`on\` t` and `#ASSERT NOT "Ana" \`is an owner of\` ...` both fail. Worked
around with prefix forms (`` `the person` o `is an owner of` ... ``) and `WHERE` names. Same family
as corpus H-06.

**N-04. A `GIVEN` with a `LIST OF` parameter followed by another parameter on the same line is a
parse error;** so is a record field `IS LIST a, b` followed by another field on the same line.
(CHK) Parameters were put on separate lines.

**N-05. A mixfix definition's `GIVEN` order must match the order the parameters appear in the
name.** (CHK) Not in `gotchas.md`. The error ("names in a type signature must match") is clear
once met.

**N-06. The console engine has no weekday or holiday operator,** so the scheme's 7-day clocks
(ss. 15, 20, 24) end on the 7th day after, never moved off an excluded day. The L4 does move them
(IA s. 61(1)(e)). (ENC) The scheme's log says so where it applies. A console run near a weekend
can therefore report a contravention a day or three early.

**N-07. The approved reference register, read against what the encoding needed.** (ENC) Not
edited (3H). (a) REF-41 lists ss. 5(1), 14(1), 18(1) as continuing duties for IA s. 71; whether
s. 71(2) reaches a duty to "ensure" is itself FORK-12. (b) s. 16 (keep and maintain) and s. 21
(give a certificate, no time fixed) are also duties with no period to which s. 71(2) may apply;
REF-41 does not list them. (c) IA s. 63 ("with all convenient speed"), which decides when the
s. 21 duty is broken, is not in the register (N-31). (d) IA s. 5 ("year means a period of 12
months") is needed to reckon s. 9(2)(e)'s "3 years" and r. 12's "3 years" under s. 62; REF-42
names s. 62 only. The library module encodes the s. 5 definition only as the conversion of years
to months. None of these makes a disposition unworkable.

## Part 1

**N-08. How age is reckoned is not stated.** (ENC) ss. 4(1)(c), 5(1), 9(2)(a), 14, 18. FORK-01.

**N-09. Is a child keeper still an owner beside the parent?** (ENC) s. 4(1)(b)-(c). FORK-02.

**N-10. A person taken to keep a cat under s. 4(2) has no day on which keeping began.** (ENC)
s. 4(2) with s. 5(2)(a). The presumption makes the database-named person a keeper "in the
absence of evidence to the contrary", but s. 5(2)(a) asks how long the person has kept the cat.
The encoding treats such an owner (and a registered owner who does not keep the cat) as not
within s. 5(2)(a).

**N-11. After a transfer, the registered owner remains "the owner".** (ENC) s. 4(1)(a), with
ss. 5, 6, 24, 25. For a registered cat the owner is "the registered owner", the person in whose
name it is registered. Nothing in Part 2 moves the registration to the purchaser: s. 24 requires
the seller to tell the local government the purchaser's name and address, but does not say the
registration is then in the purchaser's name, and s. 12(4) only corrects errors. Until the
registration expires the seller (who no longer has the cat) bears s. 6(1) and s. 25, and the
purchaser bears none of them. Noticed writing the scheme's `acquire` rule.

**N-12. s. 4(1)(c) names "parent or guardian"; the encoding takes who that is as a fact.** (ENC)

**N-13. "Microchipped" depends on who implanted the chip.** (ENC, TST) s. 3(1) with r. 8: a
working, compliant chip implanted by someone who is not a "microchip implanter" (r. 7) does not
make the cat microchipped, so the s. 14(1) duty stays unmet. Meeting it then takes a second
implant by an implanter, and s. 17 forbids removing the first chip without reasonable excuse.
Asserted on "Lee's cat".

## Part 2 Division 1

**N-14. "The person" in s. 5(2)(a) for an owner who does not personally keep the cat.** (ENC)
FORK-03.

**N-15. Counting "less than 14 days".** (ENC) s. 5(2)(a), (b). FORK-04.

**N-16. Does s. 5(2)(b) reach a non-resident?** (ENC) FORK-09.

**N-17. A cat registered with the "wrong" local government after its owner moves.** (ENC)
s. 5(1), r. 13, s. 10(a)(iii). s. 5(1) requires registration "with the local government in whose
district the cat is ordinarily kept". r. 13 lets a moving owner "notify both ... to continue that
period of registration with the new local government", but says nothing of what the notice does:
whether the cat is then "registered with" the new local government under s. 9, by which
decision, with what number or tag. Until something makes it so, the owner who has moved is in
breach of s. 5(1). Encoded: r. 13 as a bare permission; s. 5(1) compares the registering local
government with the district.

**N-18. A kitten under 6 months must be refused registration unless it is sterilised.** (TST)
s. 9(2)(d), (4), with s. 18(3). s. 9(4) saves an unsterilised cat only if exempt under s. 18(2);
under 6 months no certificate can apply (s. 18(3)) and kittens are rarely owned by breeders, so
an owner who registers a young kitten early (before the s. 5 duty) must be refused. Asserted on
"Kitty". The same for microchipping under s. 9(2)(c), (3) and s. 14(3).

**N-19. "Satisfied" in s. 9(2) is taken to follow the facts.** (ENC) The local government's
satisfaction is not modelled separately; where the facts are as stated, it is taken to be
satisfied.

**N-20. Two or more offences "against any of" three Acts.** (ENC) s. 9(2)(e), s. 10(b).
FORK-10.

**N-21. "Within the previous 3 years" of what.** (ENC) s. 9(2)(e). FORK-11. s. 10(b) by
contrast fixes its 12 months "before the cancellation".

**N-22. A requirement under s. 9(5) for more than 21 days.** (ENC) s. 9(5)-(6). The Act limits
the time to 21 days but does not say what follows if a local government specifies more. Encoded:
such a requirement is not one "under subsection (5)", so s. 9(6) cannot rest on it.

**N-23. A refusal to consider under s. 9(6) needs no notice, and is not a decision s. 13 lists.**
(ENC) s. 13(2) names refusals to grant or renew and cancellations; a refusal to consider is
neither, so the applicant is owed no written notice or reasons under s. 13 (and Part 4 Division 5,
out of scope, keys its objection rights to the same list in s. 68).

**N-24. Whom s. 13 notice goes to, and "the person's rights".** (RD, ENC) s. 13(1). Notice goes
"to the owner of the cat", while the decision is on an application by the applicant; where they
differ (a child applicant and the parent, FORK-02; a cat whose registered owner is not the
applicant on renewal) the section does not say which. s. 13(1)(c) then speaks of "the person's
rights" with no person introduced. The encoding does not model the recipient.

**N-25. s. 13 has no penalty.** (ENC) So IA s. 72 makes no offence of it and IA s. 71 does not
apply; a late or missing notice has no consequence in Part 2.

**N-26. The register's conditional items.** (ENC) r. 16(c) (postal address "if different") and
r. 16(m) (breed "if known") are required only conditionally; the encoding's s. 12(3) test asks
for every item.

## Part 2 Division 2

**N-27. A certificate given before 6 months.** (ENC) ss. 14(3), 18(3). FORK-13.

**N-28. s. 15 has no addressee if no company has agreed to keep the cat's records.** (ENC)
s. 15 with s. 3(1) "microchip database company" (b). The implanter must notify "the microchip
database company for that cat", which is the company that "keeps, or has agreed to keep" its
records. If none has agreed (or the cat's records are with a company r. 6 does not prescribe),
there is no such company and the duty has no object. Encoded: the s. 15 duty arises only when
there is a company for the cat.

**N-29. s. 16 obliges a company to keep only the s. 15 information.** (ENC) s. 16. The company
must keep "the information prescribed under section 15" -- the r. 17 items. It has no duty to
record the s. 20 sterilisation notice or the s. 24 and s. 25 notices of a new owner or address,
and it cannot keep information an implanter never gave it (a breach of s. 15 becomes a breach
of s. 16 by someone else).

## Part 2 Division 3

**N-30. "Sterilised by a veterinarian".** (ENC, TST) s. 18(1). A cat desexed by someone who is
not a "veterinarian" (Veterinary Practice Act 2021 s. 3: a WA or interstate veterinarian) -- for
example, before it came from overseas -- is "sterilised" (s. 3(1)) but its owner can never meet
s. 18(1), short of a second operation. Asserted on "Dex". s. 9(2)(d) asks only whether the cat
is sterilised.

**N-31. s. 21 fixes no time.** (ENC) The duty to give the certificate has no period, so when it
is broken is IA s. 63 ("with all convenient speed"), which is not in the reference register and
is not encoded (N-07). The encoding says only whether the duty arose and whether, by a given
day, the certificate has been given to an owner.

**N-32. r. 18's first limb cannot apply to an unsterilised cat.** (ENC) s. 19, r. 18(1). s. 19
forbids identifying a cat as sterilised "in the manner prescribed" if it is not sterilised; r. 18
prescribes "a sterilisation certificate given in relation to that cat under section 21" or the
ear tattoo. A certificate "under section 21" is given by a veterinarian who has sterilised the
cat, so for an unsterilised cat none can exist: a false certificate is not "given ... under
section 21", and s. 19 then reaches only the tattoo. Encoded literally (the certificate is a
prescribed manner); the cases exercise the tattoo.

**N-33. s. 18(2)(b) asks whether "an approved cat breeder" owns the cat for breeding; the
encoding judges it by the owner whose duty is in question.** (ENC) With several owners (FORK-02)
the cat is exempt if any of them is an approved breeder owning it for breeding; the encoding
only knows the breeder status of the owner it is asked about. s. 9(4) uses the applicant.

**N-34. s. 20 "a microchipped cat" is judged on the day of sterilising.** (ENC)

## Part 2 Division 4

**N-35. In a reclaim, who transfers?** (ENC) s. 3(1) "transfer" (b), s. 22. FORK-14.

**N-36. A kitten under 6 months that cannot safely be microchipped cannot lawfully be
transferred.** (ENC) s. 23(1) with s. 14(2)-(3). s. 23(1) allows the transfer of an unchipped
cat only if the seller is satisfied a s. 14(2) certificate applies, and under 6 months none can.
s. 23(2) has the voucher route for sterilisation; s. 23(1) has none for microchipping.

**N-37. Satisfaction about a class that does not exist.** (ENC) s. 23(2)(a)(iii). No class of
cats is prescribed as exempt from sterilisation (REF-35), so a seller "satisfied" that a cat
belongs to one is satisfied of nothing. Encoded: both the satisfaction and the class are
required, so the limb never applies.

**N-38. r. 19 and the SAFE entities; "veterinary premises" as an "organisation or person".**
(ENC) FORK-08 for the SAFE entities. Separately, r. 9(2)(d) and (e) are a cat management
facility and veterinary premises -- a place, not an "organisation or person" as r. 19 requires.
Encoded: a transfer to a cat management facility or to registered veterinary premises is within
r. 19.

**N-39. s. 24 on an offer for sale.** (TST) s. 3(1) "transfer" (a) includes "offer for sale".
Within 7 days after that "transfer" the seller must notify "the name and address of the purchaser
of the cat", and an offer not yet taken up has no purchaser. Asserted: on an offer of the
registered, chipped Tess, the duty arises and no notice can meet it.

**N-40. s. 24(a) has no addressee for an unregistered cat, and s. 24(b) none for a cat with no
company.** (ENC) Encoded as duties arising only when there is a local government with which the
cat is registered on the day of transfer, or a company for the cat. "Address" in s. 24(a)(i)
and (b)(i) is read as the residential address.

**N-41. s. 24 and s. 25 overlap on a change of owner.** (ENC) The purchaser's name is a change
to "the cat owner's full name" (r. 16(a), r. 17(g)), so the owner -- for a registered cat, the
seller as registered owner (N-11) -- also owes s. 25 notices of the same change, on the same
7-day clock.

## Part 2 Division 5

**N-42. The cat's age as a "change".** (ENC) s. 25(b), r. 17(m). FORK-15.

**N-43. Changes to the implanter's details.** (ENC) s. 25(b), r. 17(c)-(e). A change to the
implanter's name or business contact details is literally "a change to ... the information
prescribed under section 15 in respect of the cat", and the owner, who may not know of it, must
notify it. Encoded literally; not exercised by a case.

## The regulations

**N-44. "Has effect from the period specified in the registration certificate".** (RD) r.
12(2)(a). "From the period" reads as a slip for "from the date" or "for the period"; and Form 2,
the certificate (r. 14), has a field for the expiry date only, not for a starting date or period.
The encoding takes the date registration has effect as a supplied fact.

**N-45. "The next 31 October".** (ENC) r. 12(2)(a)(i). FORK-05.

**N-46. "31 October in the final year of that period".** (ENC, TST) r. 12(2)(a)(ii). FORK-06.
On the reading taken, a 3-year registration taking effect on 31 October lasts two years and a
day, while a 1-year registration taking effect that day lasts a year (FORK-05). Found when an
`#EVAL` for a 31 October start returned 2028.

**N-47. r. 12(2)(b), renewal outside the 21 days.** (ENC) The regulation allows a renewal "to
take effect as from 1 November ... within the preceding period of 21 days" (11-31 October, IA
s. 61(1)(c)). It does not say whether a renewal may be made at another time, nor whether an
application after a registration has expired is a "renewal" (s. 8, Sch. 3) or a grant.

**N-48. The $10 fee "after 31 May".** (ENC) Sch. 3 item 1(a). FORK-07.

**N-49. The pensioner rate turns on the "owner", the fee on the applicant.** (ENC) Sch. 3
cl. 1(3) halves the fee "if the owner of a cat is a pensioner". With several owners (FORK-02),
or a renewal by a registered owner who is not the keeper, the owner and the applicant may differ.
Encoded on the applicant.

**N-50. r. 9(3)(b) "a total of 12 weeks".** (ENC) Counted as 84 days. "A total" suggests
placements are added together; whether placements by different SAFE entities, or by Cat Haven
and then a SAFE entity, count to the same total is not said. Encoded as a supplied total.

**N-51. r. 15(1)(c) and (3): the colour Gazette notice is missing** (3H gap, REF-30), so
whether a tag is "the colour representing the year of expiry" is a supplied fact.

**N-52. r. 10 exempts the owner, not a class of cats.** (RD) s. 6(2) speaks of "a class of cats
prescribed as exempt"; r. 10(2) instead exempts "the owner of a cat that is being exhibited ...
but only while that cat is being exhibited". Encoded as the s. 6(2) class.

## Interpretation Act

**N-53. Counting s. 71's "separate and further" offences.** (ENC) IA s. 71(1)(e), (2): "each
day after the day of the conviction during which the failure ... continues". Encoded: the days
from the day after conviction to the day before the thing is done (on the day it is done the
failure ends), or to the day counted to. Whether the day the thing is done counts is not said.

**N-54. Whether s. 71(2) reaches "must ensure" duties.** (ENC) FORK-12.

**N-55. Commencement.** (ENC) s. 2(a): the day of assent is a fact; the compilation table gives
9 Nov 2011. s. 2(c) lists "14(1)" and "18(1)", so ss. 14(2)-(3) and 18(2)-(3) commenced a year
before the duties they qualify.

## The scheme

**N-56. What the console does not model.** (ENC) s. 25, s. 10, fees, r. 9 custody and foster
exemptions, cat management facilities and reclaiming, child keepers' parents (FORK-02), and
excluded days (N-06). All are in the L4. The scheme names its scope.
