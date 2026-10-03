# Incidents -- Cat Act 2011 (WA), LQA run cat-act-2011-lqa

Against the Cat Act 2011 compilation 00-l0-01 (currency start 25 Sep 2025) and the Cat Regulations 2012 compilation 02-b0-00. Steps 7A-10A, 2 October 2026. The machine-readable register is `incidents.json`; this is its prose, and the two must agree. `REPORT.md` is the summary a drafter reads first.

Every finding was made against the pinned print and re-checked on 2 October 2026 against the current print on the WA legislation website (still 00-l0-01; regulations still 02-b0-00). Status `OPEN` means the challenge at 9A did not answer it; `VERIFIED-NO-DEFECT` means something in the 0H or 3H set did, and names it. "Found by" is the casual-reader test of `LQA-PIPELINE.md`, recorded when the finding was first made.

**Not released.** No 12H signature exists. The parliamentary documents cited (explanatory memoranda, the Council's notice paper) are held for internal analysis only (3H decision); they are cited by clause, not reproduced.

---

## Open findings

### D-01 -- After a transfer the registered owner remains "the owner"; the new keeper cannot register the cat

- **Provision:** s. 4(1)(a), with ss. 5, 6, 8(1), 12(4), 24, 25
- **Category:** D (also L)
- **Status:** OPEN, severity high
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** For a registered cat, 'owner' means only the registered owner (s. 4(1)(a)), and no provision moves a registration to the purchaser: s. 24 requires notice of the purchaser's name but nothing then registers the cat in it, and s. 12(4) corrects only errors. Until the registration ends -- never, for a lifetime registration -- the seller remains liable under ss. 5, 6(1), 14, 18 and 25 for a cat it no longer has, the purchaser has none of those duties, and the purchaser cannot apply to register the cat because only 'the owner' may (s. 8(1)). Noticed writing the scheme's acquire rule (ENCODING-NOTES N-11).

**Why it matters.** Every sale or gift of a registered cat leaves the register, and the Act's duties, with the wrong person. The person who has the cat cannot register it in their own name or district; the person who parted with it remains liable for tags (s. 6(1)), changes of details (s. 25) and, if the cat moves district, registration (s. 5(1)). With a lifetime registration that never ends.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 4 -- the owners of` `Tess, sold to Ben` `on` (`the date` 2027 6 1) EQUALS LIST "Ana" ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 8(1) -- the applicant may apply` (`an application by` `Ben` `Tess, sold to Ben` `for the grant of registration` (`the date` 2027 6 1) `one year` 10 (`the date` 2027 6 3)) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 6(1) --` `Ana` `contravenes the subsection for` `Tess, sold to Ben` `on` (`an outing on` (`the date` 2027 6 1) TRUE FALSE NOTHING) ``
- scenario "Ben buys Tess, then applies to register her in his own name" (console)
- simulation: seed 1, 365 days, default parameters (console)
- text: Cat Act 2011 (00-l0-01), s. 4(1)(a): "in the case of a cat that is registered, the registered owner of the cat"
- text: Cat Act 2011 (00-l0-01), s. 8(1): "The owner of a cat that is ordinarily kept in the district of a local government may apply to that local government"

**Challenge (2026-10-02).** Nothing in the 0H or 3H set moves a registration. Section 12(1) requires an accurate and up-to-date register, and a local government may in practice record the purchaser's name on a s. 24 notice; but the register records 'the cat owner's full name' (r. 16(a)), and the cat owner is defined by the registration (s. 4(1)(a)), so recording a new name is circular rather than an answer -- a court might hold it registers the cat in the purchaser's name, but nothing says so. Interpretation Act s. 10(c) does not help: s. 4(1)(a) and (b) are alternatives keyed to whether the cat is registered. Section 10 gives no ground to cancel on a transfer. The Cat Bill 2011 EM (cl. 24) expected the s. 24 notice to let local governments ensure the cat is registered by its new owner, which s. 8(1) prevents. Not answered.

**Suggested repair.** Provide that on receiving a s. 24 notice the local government records the purchaser as the registered owner (or that the registration ends on transfer), and let the person who keeps the cat apply under s. 8(1). The uncommenced centralised-register amendments (Dog Amendment (Stop Puppy Farming) Act 2021 ss. 50-59) do not address this.

### D-05 -- A cat chipped by a vet registered only in another State, or overseas, is not "microchipped"

- **Provision:** s. 3(1) "microchipped", "microchip implanter"; Cat Regulations 2012 rr. 7, 8; Veterinary Practice Act 2021 ss. 3, 22(1)(c)
- **Category:** D (also I)
- **Status:** OPEN, severity medium-high
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** A chip counts only if implanted by a 'microchip implanter' (r. 8): a 'veterinarian' or WA veterinary nurse (r. 7(1)), or a holder of the r. 7(2) qualifications. Since 2022 'veterinarian' means a WA veterinarian or an interstate one registered under VPA s. 22, which requires that the person 'practises veterinary medicine in this State'. A cat chipped in Melbourne by a Victorian vet, or overseas, is therefore 'not microchipped' however good the chip: the owner is in breach of s. 14(1) from the day it arrives, registration must be refused (s. 9(2)(c)), and the only cure is a second chip, while s. 17 forbids removing the first. Noticed as N-13 (a chip by an unqualified person); the interstate case found reading VPA s. 22.

**Why it matters.** People move to WA with cats every day. Each cat chipped in another State or overseas is, in law, unchipped: its owner commits an offence from arrival, the local government must refuse to register it, and compliance needs a second implant.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 3(1) --` `Lulu, chipped in Melbourne` `is microchipped on` (`the date` 2026 10 1) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 14(1) --` `Ana` `contravenes the subsection for` `Lulu, chipped in Melbourne` `on` (`the date` 2026 10 1) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9 -- the decision required on` (`an application by` `Ana` `Lulu, chipped in Melbourne` `for the grant of registration` (`the date` 2026 10 1) `one year` 10 (`the date` 2026 10 5)) EQUALS `must refuse` ``
- scenario "Lulu, chipped and desexed by a Melbourne vet, comes to Perth" (console)
- text: Cat Regulations 2012 (02-b0-00), r. 8: "a microchip is implanted in the prescribed manner if it is implanted by a microchip implanter"
- text: Veterinary Practice Act 2021 (00-f0-01), s. 22(1)(c): "the person practises veterinary medicine in this State"

**Challenge (2026-10-02).** Interpretation Act s. 16 (references as amended) confirms the narrower definition applies. Nothing in the 0H or 3H set recognises interstate or overseas implants or deems a cat microchipped by its chip alone. Not answered.

**Suggested repair.** Make 'microchipped' turn on the device and its record (a compliant chip, implanted, readable, recorded with a prescribed company), or prescribe in r. 7 persons authorised to implant in another State or country.

### U-06 -- "The person" in s. 5(2)(a): how long has a parent, or a business owner, kept the cat?

- **Provision:** s. 5(2)(a), with s. 4(1)(b), (c)
- **Category:** U (also R); fork FORK-03
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 5(2)(a) disapplies s. 5(1) while 'the cat has been kept by the person for less than 14 days', but s. 5(1) speaks only of 'the owner'. For an owner through someone else's keeping -- the parent of a child keeper (s. 4(1)(c)), or an owner of a business that keeps the cat (s. 4(1)(b)) -- the choice decides liability: reading A (taken) attributes the keeping and puts the parent in breach after 14 days; reading B, the more literal, exempts such owners for ever. ENCODING-NOTES N-14.

**Why it matters.** Whether a parent whose child keeps a cat, or the owners of a business that keeps one, are ever liable under s. 5(1) depends on a reading the text does not settle.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 5(1) --` `Ana` `contravenes the subsection for` `Mo` `on` (`the date` 2026 3 20) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 5(2)(a), reading B of FORK-03 -- the cat` `Mo` `has been kept by` `Ana` `for less than 14 days on` (`the date` 2027 3 20) ``
- scenario "Kit, a child, takes in Mo and applies to register him" (console)

**Challenge (2026-10-02).** Interpretation Act s. 18 favours reading A (reading B makes s. 4(1)(c) idle for s. 5), which is why it was taken; but the text supplies no antecedent for 'the person' and the drafter could have written 'the owner' or 'the cat has been kept by the owner, or by the person by whose keeping the owner is an owner'. The choice is consequential and was left open.

**Suggested repair.** Replace 'the person' in s. 5(2)(a) and (b) with 'the owner', and say whose keeping counts for an owner under s. 4(1)(b) (business) and (c).

### L-09 -- An owner who moves district is in breach of s. 5(1) at once, and r. 13's notice has no stated effect

- **Provision:** s. 5(1); Cat Regulations 2012 r. 13; s. 10(a)(iii)
- **Category:** L (also P, T)
- **Status:** OPEN, severity medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 5(1) requires registration 'with the local government in whose district the cat is ordinarily kept'. On the day an owner moves, the cat is registered with the wrong local government and the owner is in breach: s. 5(2)(a) counts how long the person has kept the cat, not how long it has been in the district. Regulation 13 lets the owner 'notify both the former and the new local government to continue that period of registration with the new local government', but neither the Act nor the regulations say what the notice does -- whether the cat is then 'registered with' the new local government, by whose decision, with what number or tag. Registration under s. 9 follows only an application under s. 8. ENCODING-NOTES N-17.

**Why it matters.** Moving house within WA is ordinary. Every owner of a registered cat who moves district commits an offence on the day of the move, and the regulation meant to deal with it has no legal effect anyone can identify.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 5(1) --` `Ana` `contravenes the subsection for` `Tess, moved to Kalamunda` `on` (`the date` 2026 4 2) ``
- scenario "Ana moves with Tess to Kalamunda and notifies both councils" (console)
- text: Cat Regulations 2012 (02-b0-00), r. 13: "the owner may notify both the former and the new local government to continue that period of registration with the new local government"

**Challenge (2026-10-02).** Interpretation Act s. 43(1) would make r. 13 void only to the extent it is inconsistent with the Act; it is not inconsistent, it is inert. No provision in the set gives the notice an effect or gives a moving owner a period of grace. Not answered.

**Suggested repair.** Provide in the Act that on a r. 13 notice the cat is taken to be registered with the new local government for the rest of the period (with a new tag if needed), and give a period of grace in s. 5(2) for an owner who moves within the State.

### D-10 -- An owned cat at the vet, or boarding at an approved facility, must be refused registration

- **Provision:** s. 9(2)(b); s. 5(2)(c); Cat Regulations 2012 r. 9(2)(d), (e); s. 3(1) "cat management facility" (c)
- **Category:** D (also L, I)
- **Status:** OPEN, severity medium
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Regulation 9(2) exempts from registration a cat 'in the custody of' (d) a cat management facility or (e) veterinary premises. A cat management facility includes any facility 'operated by a person or body approved in writing by a local government' (s. 3(1)), such as a boarding cattery. Read with s. 9(2)(b), which obliges a local government to refuse registration of a cat in a class prescribed as exempt, an owned cat that is at the vet or boarding when its application or renewal is decided must be refused. The class was described as cats 'waiting to be rehomed' (Cat Bill 2011 EM, cl. 5); the Act itself distinguishes cats kept temporarily at a facility at the owner's request (s. 29). Found setting r. 9 beside s. 9(2)(b).

**Why it matters.** A local government deciding a renewal while the cat is at the vet, or boarding, must refuse it -- and then give notice of refusal and review rights. The class designed for shelter cats catches owned cats in ordinary temporary care.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9 -- the decision required on` (`an application by` `Ana` `Tess, at the vet` `for the renewal of registration` (`the date` 2026 10 20) `one year` 20 (`the date` 2026 10 22)) EQUALS `must refuse` ``
- scenario "Tess is at the vet when her renewal is decided" (console)
- text: Cat Regulations 2012 (02-b0-00), r. 9(2)(e): "veterinary premises as defined in the Veterinary Practice Act 2021 section 3"
- text: Cat Act 2011 (00-l0-01), s. 29: "This Division does not apply to a cat kept temporarily at a cat management facility at the request of its owner."

**Challenge (2026-10-02).** Interpretation Act s. 18 (purpose) could support reading 'custody' as custody pending rehoming, but s. 9(2) is mandatory ('must refuse ... if, and only if') and 'custody' has no such limit. The refusal triggers s. 13 notice and review, but the owner must then reapply. Not answered.

**Suggested repair.** Limit r. 9(2)(d) and (e) to cats not kept at the facility or premises at the request of their owner (as s. 29 does for Part 3 Division 3), or make s. 9(2)(b) a discretionary ground.

### U-13 -- "Within the previous 3 years": before the application or before the decision?

- **Provision:** s. 9(2)(e)
- **Category:** U; fork FORK-11
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Refusal is mandatory if the applicant 'has been convicted within the previous 3 years of 2 or more offences'. Counted back from the decision (reading A, taken), a conviction can fall out of the window while the application waits; counted from the application (reading B, as Form 1 Part F asks 'in past 3 years'), it cannot. The outcome can turn on how quickly the local government decides. ENCODING-NOTES N-21.

**Why it matters.** A mandatory refusal can turn on how quickly the local government processes the application.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 9(2)(e) -- applies to` `Sam's application` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9(2)(e), reading B of FORK-11 -- applies to` `Sam's application` ``
- scenario "Ben, with two recent convictions, applies to register his cat" (console)
- text: Cat Regulations 2012 (02-b0-00), Sch. 1 Form 1 Part F: "in past 3 years"

**Challenge (2026-10-02).** No provision in the set fixes the day; s. 10(b) by contrast fixes its 12 months 'before the cancellation'. Left open.

**Suggested repair.** Say 'within the 3 years before the application was made' (or 'before the decision').

### P-15 -- A refusal to consider an application carries no notice, no reasons and no review, and leaves the owner in breach

- **Provision:** s. 9(6); s. 13(2); s. 68
- **Category:** P (also E)
- **Status:** OPEN, severity medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** If the applicant does not meet a s. 9(5) requirement in time, the local government 'may refuse to consider' the application (s. 9(6)). That is neither a grant nor a refusal: it is not a decision s. 13(2) lists, so no notice, reasons or statement of rights is owed, and Part 4 Division 5 gives no objection or review (s. 68 lists the same decisions). The application is never determined, and the owner remains bound by s. 5(1) and in breach. ENCODING-NOTES N-23.

**Why it matters.** The applicant has no decision to object to or review, no reasons, and remains in breach of s. 5(1). The power is open-ended in effect: an application can be left unconsidered and nothing follows.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9(6) -- the local government may refuse to consider` (`Ana's application, required to answer within` 7) `given the holidays` `the holidays` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 13(2) -- notice must be given of` `refuse to consider the application under s 9(6)` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 5(1) --` `Ana` `contravenes the subsection for` `Max, taken in on 1 March` `on` (`the date` 2027 2 1) ``
- scenario "The council refuses to consider Ana's application for Tom" (console)
- text: Cat Act 2011 (00-l0-01), s. 68: "This Division applies when a local government makes a decision to"

**Challenge (2026-10-02).** Interpretation Act s. 63 (all convenient speed) does not apply: deciding is not required once the power to refuse to consider is used. Judicial review would remain, but the scheme's own review (Part 4 Division 5) is excluded. The applicant may apply again. Not answered.

**Suggested repair.** Make a refusal to consider a decision to which ss. 13 and 68 apply, or replace s. 9(6) with a power to refuse the application on the ground of non-compliance.

### R-17 -- Section 13 notice goes to "the owner", and "the person's rights" has no antecedent

- **Provision:** s. 13(1)
- **Category:** R
- **Status:** OPEN, severity low
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Notice of a refusal or cancellation goes 'to the owner of the cat', and must state 'the person's rights under Part 4 Division 5'. Section 13 introduces no person: it reads as copied from s. 40(1), which gives notice 'to the person affected by the decision'. Where the applicant and the owner differ, or a cat has several owners (a child applicant and the parent, FORK-02), the section does not say who is owed the notice; and because review is open only to a person given notice (E-18), that decides who may seek review. Lead from 2A; ENCODING-NOTES N-24.

**Why it matters.** The notice decides who may object and seek review (E-18), and the section does not say who gets it when the applicant is not the only owner.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 4 -- the owners of` `Mo` `on` (`the date` 2026 10 1) EQUALS LIST "Kit", "Ana" ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9 -- the decision required on` (`an application by` `Kit` `Mo` `for the grant of registration` (`the date` 2026 11 15) `one year` 20 (`the date` 2026 11 20)) EQUALS `must refuse` ``
- scenario "Kit, a child, takes in Mo and applies to register him" (console)
- text: Cat Act 2011 (00-l0-01), s. 40(1): "the local government is to give to the person affected by the decision notice in writing of"

**Challenge (2026-10-02).** A court would very likely read 'the person' as 'the owner' (an obvious slip), and Interpretation Act s. 10(c) lets 'the owner' include all owners. That answers the antecedent but not which of several owners, or a non-owner applicant, is owed notice. OPEN at low.

**Suggested repair.** In s. 13(1), give notice 'to the applicant and to each owner of the cat' and refer to 'the rights of the person to whom notice is given'.

### E-18 -- If the local government gives no s. 13 notice, the owner loses the objection and review rights

- **Provision:** s. 13(1); ss. 69(1), 71(1)
- **Category:** E (also P)
- **Status:** OPEN, severity medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 13 requires written notice of a refusal or cancellation, with reasons and the person's rights, within 7 days. It carries no penalty and no other consequence (so Interpretation Act s. 71 does not apply). But the right to object (s. 69(1)) and to apply to the State Administrative Tribunal (s. 71(1)) belongs only to 'a person who has been given notice under section 13 or 40'. A local government that gives no notice therefore removes the owner's review, and nothing in the Act cures it. ENCODING-NOTES N-25 (no penalty); the review link found reading Part 4 Division 5 as text.

**Why it matters.** The person most affected by a refusal or cancellation loses the review the Act provides because of the local government's own default.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 13(1) -- notice of` `refuse to grant or renew the registration under s 9` `made on` (`the date` 2026 12 18) `is duly given by` (`a full notice given on` (`the date` 2027 2 1)) `given the holidays` `the holidays` ``
- scenario "The council refuses Tom and gives no notice" (console)
- text: Cat Act 2011 (00-l0-01), s. 69(1): "A person who has been given notice under section 13 or 40 of a decision may object to the decision"
- text: Cat Act 2011 (00-l0-01), s. 71(1): "A person who has been given notice under section 13 or 40 of a decision may apply to the State Administrative Tribunal"

**Challenge (2026-10-02).** No provision in the set supplies a time from which the right runs without notice, or deems notice given. The State Administrative Tribunal Act was not in the 0H or 3H set; whether it supplies a route is recorded as a gap. Not answered from the set.

**Suggested repair.** Key ss. 69 and 71 to the decision rather than to notice of it (for example 'a person whose application is refused, or the owner of a cat whose registration is cancelled'), with time running from notice or, if none is given, from when the person learns of the decision.

### U-19 -- Does a veterinary certificate given before 6 months start to apply at 6 months?

- **Provision:** ss. 14(2), (3), 18(2)(a), (3)
- **Category:** U; fork FORK-13
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** 'A certificate ... cannot apply in respect of a cat that is under 6 months of age.' Judged on the day in question (reading A, taken), a certificate given at 5 months begins to apply when the cat turns 6 months; judged when it was given (reading B), it never applies, and the owner is in breach of s. 14(1) or 18(1) from the 6-month birthday unless a fresh certificate is obtained. ENCODING-NOTES N-27.

**Why it matters.** An owner with an early veterinary certificate may be in breach on the cat's 6-month birthday.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 14(2) --` (`Chip, certificate given on` (`the date` 2026 6 5)) `is exempt from microchipping on` (`the date` 2026 7 1) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 14(2), reading B --` (`Chip, certificate given on` (`the date` 2026 6 5)) `is exempt from microchipping on` (`the date` 2026 7 1) ``
- scenario "Dr Vu certifies that chipping may harm 2-month-old Tom" (console)

**Challenge (2026-10-02).** The Council inserted s. 14(3) and s. 18(3) by amendment (LC SNP 197-2, 15/14 and 16/18) without saying which; the present tense favours A. Left open.

**Suggested repair.** Say 'A certificate referred to in subsection (2) has no effect if given in respect of a cat that is under 6 months of age' (or the opposite).

### R-20 -- Section 15 has no addressee until a microchip database company has agreed to keep the cat's records

- **Provision:** s. 15; s. 3(1) "microchip database company" (b)
- **Category:** R (also E)
- **Status:** OPEN, severity medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The implanter must notify 'the microchip database company for that cat', which s. 3(1)(b) defines as the company that 'keeps, or has agreed to keep' records about the cat and its owner. Until some company has agreed, there is no such company, and the duty has no object: an implanter who arranges nothing commits no offence, and the chip identifies nobody -- the purpose of microchipping (Cat Bill 2011 EM, cl. 14). The 2021 amendments repair s. 16 but not s. 15. ENCODING-NOTES N-28.

**Why it matters.** The chip is the identification the scheme relies on; if no database holds its number, it identifies nobody, and the implanter who arranged nothing commits no offence.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 15 -- the duty to notify applies to the implant in` `Pip, chipped, no database` ``
- scenario "Dr Vu chips Tom but arranges no database" (console)
- text: Cat Act 2011 (00-l0-01), s. 3(1) "microchip database company" (b): "in relation to a particular cat, means the microchip database company that keeps, or has agreed to keep, records containing information about that cat and its owner"

**Challenge (2026-10-02).** Interpretation Act s. 18 might read 'the company for that cat' as 'a prescribed company of the implanter's choice', but the definition is express. Nothing in the set obliges anyone to arrange a database. Not answered.

**Suggested repair.** Require the implanter to give the notice 'to a microchip database company' (any prescribed company), which then becomes the company for the cat.

### W-21 -- Section 16 requires the database company to keep information it was never given

- **Provision:** s. 16; s. 15
- **Category:** W
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** A 'microchip database company for a cat must keep and maintain ... the information prescribed under section 15'. If the implanter breaches s. 15 and never notifies the company, the company is in breach of s. 16 for information it has never had: one person's offence makes another's. The 2021 amending Act limits the duty to information 'that has been given to it' (s. 53), not yet commenced; its explanatory memorandum (cl. 53) gives the reason. ENCODING-NOTES N-29.

**Why it matters.** One person's offence (the implanter's under s. 15) makes another (the company's under s. 16). Parliament has already enacted the fix; it has not been proclaimed.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 16 -- the company for` `Pip, chipped, company never told` `contravenes the section, holding` EMPTY ``
- scenario "Dr Vu chips Tom and never tells the database company" (console)
- simulation: seed 1, 365 days, default parameters (console)
- text: Dog Amendment (Stop Puppy Farming) Act 2021, as passed, s. 53: "that has been given to it"
- text: Explanatory Memorandum, Dog Amendment (Stop Puppy Farming) Bill 2021 (internal copy), cl. 53 (checked against the pinned copy; not reproduced)

**Challenge (2026-10-02).** A company that 'has agreed to keep' records about the cat (s. 3(1)) but received nothing cannot comply; Criminal Code s. 23A (unwilled omissions) might excuse it at trial, but the duty is impossible as drafted, and the enacted repair confirms it. Not answered.

**Suggested repair.** Commence the Dog Amendment (Stop Puppy Farming) Act 2021 s. 53.

### D-22 -- A cat desexed by a vet registered only in another State, or overseas, is never "sterilised by a veterinarian"

- **Provision:** s. 18(1); s. 3(1) "veterinarian"; Veterinary Practice Act 2021 ss. 3, 22(1)(c), 228
- **Category:** D (also I, M)
- **Status:** OPEN, severity medium-high
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 18(1) requires the owner to ensure the cat is sterilised 'by a veterinarian'. Since the Veterinary Practice Act 2021 s. 228 (in force 18 June 2022) substituted its own definition, that means a WA veterinarian or an interstate veterinarian who practises in WA. The owner of a cat desexed in another State or overseas can never comply, short of a second operation on a sterile cat; yet s. 9(2)(d) asks only whether the cat is 'sterilised', so the cat must be registered. ENCODING-NOTES N-30 (a cat desexed before it came from overseas).

**Why it matters.** As for D-05, but worse: the owner of a cat desexed in another State or overseas can never comply with s. 18(1). The 2022 definition change appears to have narrowed the Act without that consequence being considered.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 18(1) --` `Ana` `contravenes the subsection for` `Lulu, desexed in Melbourne` `on` (`the date` 2026 10 1) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 9(2)(d), (4) -- applies to` (`an application by` `Ana` `Lulu, desexed in Melbourne` `for the grant of registration` (`the date` 2026 10 1) `one year` 10 (`the date` 2026 10 5)) ``
- scenario "Lulu, chipped and desexed by a Melbourne vet, comes to Perth" (console)
- text: Cat Act 2011 (00-l0-01), s. 18(1): "must ensure that the cat is sterilised by a veterinarian"
- text: Veterinary Practice Act 2021 (00-f0-01), s. 22(1)(c): "the person practises veterinary medicine in this State"

**Challenge (2026-10-02).** Interpretation Act s. 18 (purpose) might support reading 'by a veterinarian' as 'by a person then qualified as a veterinarian wherever practising', but the definition is express and was substituted deliberately in 2022 (VPA s. 228). Nothing in the set answers it.

**Suggested repair.** Require that the cat be sterilised (as s. 9(2)(d) does), or 'by a veterinarian or a person registered or licensed to practise veterinary surgery in another State, a Territory or another country'.

### R-24 -- Section 19 does not reach a false certificate of sterilisation

- **Provision:** s. 19; Cat Regulations 2012 r. 18(1); s. 21
- **Category:** R
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 19 forbids identifying an unsterilised cat as sterilised 'in the manner prescribed'. Regulation 18(1) prescribes 'a sterilisation certificate given in relation to that cat under section 21' or the ear tattoo. A certificate under s. 21 is one a veterinarian gives after sterilising the cat, so a false certificate for an entire cat is never 'given under section 21': it is not a prescribed manner, and s. 19 reaches only the tattoo. A false certificate shown to a purchaser or a local government is the more likely abuse. ENCODING-NOTES N-32.

**Why it matters.** False certificates are the obvious way to pass off an entire cat as desexed; the offence designed to stop it does not reach them.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 19 -- identifying by` `some other means` `Tom` `as sterilised on` (`the date` 2026 10 1) `contravenes the section` ``
- scenario "Ben sells Tom with a false certificate of sterilisation" (console)
- text: Cat Regulations 2012 (02-b0-00), r. 18(1): "A cat is identified as sterilised by a sterilisation certificate given in relation to that cat under section 21 of the Act or a sterilisation tattoo on the cat's ear."

**Challenge (2026-10-02).** Section 85 (false information) reaches a false statement 'in relation to an application under this Act' or to an authorised person, but not one made to a purchaser. Interpretation Act s. 18 cannot turn a certificate not given under s. 21 into one that was. Not answered.

**Suggested repair.** Prescribe in r. 18 'a document that purports to be a certificate of sterilisation' (or 'a certificate of sterilisation, whether or not given under section 21').

### U-27 -- On a reclaim from a cat management facility, who is the "seller"?

- **Provision:** s. 3(1) "transfer" (b); ss. 22, 23, 24
- **Category:** U; fork FORK-14
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** 'Transfer' includes 'to reclaim from a cat management facility'. Section 22 makes the seller 'the person by whom the cat is transferred'. Reading A (taken, following s. 33) makes the facility's operator the seller: the operator contravenes s. 23 when it releases an unchipped or entire cat to its owner, and owes a s. 24 notice of a 'purchaser' who was the owner throughout. Reading B makes the reclaiming owner the seller, with no purchaser at all. Either way the definition fits reclaiming poorly, and who commits the offence turns on the choice. ENCODING-NOTES N-35.

**Why it matters.** Every reclaim from a pound of an unchipped or entire cat is, on the reading taken, an offence by the pound's operator, or, on the other, an offence by the owner -- and either way s. 24 requires a meaningless notice.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `the person named` "City of Perth" `contravenes s 23 by` `Ana reclaims Tom from the pound` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `reading B -- the person named` "Ana" `contravenes s 23 by` `Ana reclaims Tom from the pound` ``
- scenario "The council impounds Tom; Ana reclaims him unchipped" (console)

**Challenge (2026-10-02).** Section 33 ('before the cat is reclaimed or otherwise transferred from that facility') supports reading A, and s. 33 lets the operator chip and desex first; but s. 33 is permissive and does not settle who commits s. 23, nor make the s. 24 notice sensible. Left open.

**Suggested repair.** State in s. 22 that on a reclaim the operator is the seller and the person reclaiming the purchaser, and disapply s. 24 to a reclaim by the cat's owner.

### R-29 -- Regulation 19's reference to r. 9 now exempts transfers to vet clinics and approved facilities from s. 23

- **Provision:** Cat Regulations 2012 r. 19, r. 9(2)(d), (e); s. 23(3)
- **Category:** R (also M)
- **Status:** OPEN, severity low-medium
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Regulation 19 disapplies s. 23(1) and (2) (no transfer unless microchipped and sterilised) for a transfer 'to an organisation or person set out in regulation 9'. Regulation 9 was replaced in 2018 and amended in 2022, and now sets out a cat management facility -- including any facility a local government has approved -- veterinary premises, and foster care, as well as the named bodies. Because the reference runs with r. 9 as amended (Interpretation Act s. 16(2)), anyone may now give or sell an unchipped, entire cat to a vet clinic or to an approved private facility. Premises and facilities are not 'an organisation or person' at all, so the reach of the exemption is also uncertain. Nothing shows the widening was considered. Lead from 2A; with ENCODING-NOTES N-38.

**Why it matters.** Section 23 is the Act's point-of-sale control. Its exemption now extends to transfers to any vet clinic and any private facility a local government has approved, which nobody appears to have decided.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 23(1) -- contravened by the transfer` (`a transfer of` `Tom` `give away` (`the date` 2026 10 1) "Ana" (JUST "Westside Vet Clinic") (`veterinary premises` TRUE) FALSE) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 23(2) -- contravened by the transfer` (`a transfer of` `Tom` `sell` (`the date` 2026 10 1) "Ana" (JUST "Purrfect Boarding Pty Ltd") (`a facility` `an approved boarding cattery`) FALSE) ``
- scenario "Ana gives unchipped Tom up to her vet clinic" (console)
- text: Cat Regulations 2012 (02-b0-00), r. 19: "do not apply if a cat is being transferred to an organisation or person set out in regulation 9"
- text: Cat Regulations 2012 (02-b0-00), r. 9 history note: "[Regulation 9 inserted: Gazette 23 Mar 2018 p. 1026-7; amended: SL 2022/94 r. 5.]"
- text: Interpretation Act 1984, s. 16(2): "shall be construed as a reference to such provision as it may from time to time be amended"

**Challenge (2026-10-02).** Interpretation Act s. 16(2) confirms the widening is effective law rather than answering it. The heading of r. 19 ('Transfer of exempt cats') is not part of the regulation (IA s. 32(2)). The amending regulations of 2018 and 2022 are a 3H gap (unavailable), so whether r. 19 was considered then cannot be checked. Not answered.

**Suggested repair.** Replace the reference in r. 19 with a closed list of transferees (Cat Haven, RSPCA WA, the Commonwealth biosecurity Department, a local government's cat management facility, a SAFE entity), or limit it to transfers for rehoming.

### U-30 -- Are the SAFE groups "set out in regulation 9" for r. 19?

- **Provision:** Cat Regulations 2012 r. 19, r. 9(1), (3)(b)
- **Category:** U; fork FORK-08
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Regulation 9 names the SAFE entities in a definition (r. 9(1)) and as bodies that place cats into foster care (r. 9(3)(b)), not as custodians. Reading A (taken) treats them as 'set out in regulation 9', so a transfer to a SAFE group is outside s. 23; reading B confines r. 19 to custodians, so giving an unchipped or entire stray to a SAFE group is an offence. ENCODING-NOTES N-38.

**Why it matters.** Giving a stray to a SAFE rescue group is an ordinary act; whether it is an offence depends on an unsettled reading.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `r 19 -- the recipient` (`a SAFE entity` `Saving Animals from Euthanasia Incorporated`) `is set out in regulation 9, the facility being a cat management facility` FALSE ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `r 19 -- reading B, the recipient` (`a SAFE entity` `Saving Animals from Euthanasia Incorporated`) `is set out in regulation 9, the facility being a cat management facility` FALSE ``
- scenario "Ana gives Tom to a SAFE rescue group" (console)

**Challenge (2026-10-02).** Nothing in the set says which; the 2018 and 2022 amending regulations are a 3H gap. Left open.

**Suggested repair.** List the transferees in r. 19 expressly (see R-29).

### D-31 -- An offer for sale is a "transfer", so s. 24 requires notice of a purchaser who does not exist

- **Provision:** s. 3(1) "transfer" (a); s. 24
- **Category:** D
- **Status:** OPEN, severity low-medium
- **Found by:** TST
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** 'Transfer' includes 'offer for sale', and s. 24 requires the seller, within 7 days 'after the transfer', to notify the local government and the database company of 'the name and address of the purchaser'. An offer not taken up has no purchaser, so the duty arises and cannot be met. Including offers is what makes s. 23 bite at the advertisement, which is its point. Parliament enacted the deletion of 'offer for sale' in 2021 (Dog Amendment (Stop Puppy Farming) Act 2021 s. 50(4)), not yet commenced; commencing it would also take offers out of s. 23. ENCODING-NOTES N-39, surfaced by an assertion.

**Why it matters.** Every seller who advertises a registered or chipped cat is in breach of s. 24 seven days later if no buyer has appeared. Parliament has already enacted the fix; it has not been proclaimed.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 24 -- there is a purchaser to name in` `Ana offers Tess for sale` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 24 -- the seller in` `Ana offers Tess for sale` `contravenes the section, having given` (LIST `a notice naming the purchaser to` "City of Perth" `on` (`the date` 2026 12 21), `a notice naming the purchaser to` "PetBase Pty Ltd, trading as Petsafe" `on` (`the date` 2026 12 21)) `, on` (`the date` 2026 12 30) `given the holidays` `the holidays` ``
- scenario "Ana advertises Tess for sale" (console)
- text: Dog Amendment (Stop Puppy Farming) Act 2021, as passed, s. 50(4): "In section 3(1) in the definition of transfer paragraph (a) delete"

**Challenge (2026-10-02).** Section 3(1) opens 'unless the context otherwise requires', which a court would very likely use to read s. 24 as applying only to a completed transfer; that softens the defect but leaves the duty's start ambiguous (is the 'transfer' the offer or the sale?). The enacted but uncommenced repair confirms the problem was recognised. OPEN at low-medium.

**Suggested repair.** Keep 'offer for sale' for s. 23 and say in s. 24 that it applies to a transfer other than an offer for sale, running from the day the cat passes to the purchaser; or commence SPF Act s. 50(4) and add offers to s. 23 expressly.

### L-33 -- Sections 24 and 25 both require the seller to report the same change

- **Provision:** ss. 24, 25; Cat Regulations 2012 rr. 16(a), 17(g)
- **Category:** L
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** On a sale of a registered cat, the seller must notify the purchaser's name and address under s. 24. Because the seller remains the registered owner (D-01), the seller is also 'the owner' who must notify the same change to 'the cat owner's full name' under s. 25, on the same 7-day clock: two offences for one omission. The purchaser owes neither. ENCODING-NOTES N-41.

**Why it matters.** Two offences for one omission, both on the person who no longer has the cat.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 25(a) -- the duty applies to` `Ana` `for` `Tess, renewed and sold` `on a change to` `the cat owner's full name` `on` (`the date` 2026 12 18) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 25(a) -- the duty applies to` `Ben` `for` `Tess, renewed and sold` `on a change to` `the cat owner's full name` `on` (`the date` 2026 12 18) ``
- scenario "Ben buys Tess, then applies to register her in his own name" (console)
- simulation: seed 1, 365 days, default parameters (console)

**Challenge (2026-10-02).** Section 24(a)(ii) and (b)(ii) ('any other changes') show the drafter meant s. 24 to cover the change of owner, but s. 25 is not disapplied. Sentencing Act principles against double punishment would apply at sentence, not to liability. OPEN at low.

**Suggested repair.** Disapply s. 25 to a change notified, or required to be notified, under s. 24; repairing D-01 also removes the overlap.

### U-34 -- Is a cat growing older a "change" the owner must notify within 7 days?

- **Provision:** s. 25(b); Cat Regulations 2012 r. 17(m)
- **Category:** U; fork FORK-15
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The information prescribed under s. 15 includes 'the age' of the cat (r. 17(m)). Section 25(b) requires the owner to notify the database company within 7 days after 'a change to any of the information prescribed under section 15'. Read literally (reading B), every owner of a microchipped cat must notify every change of age, and is in breach almost always. Reading A (taken) treats the information as fixed at implanting. The drafter could have prescribed the date of birth, as r. 16(d) does for the owner. ENCODING-NOTES N-42.

**Why it matters.** On the literal reading every owner of a microchipped cat is perpetually in breach of s. 25(b).

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 25(b) -- the duty applies to` `Ana` `for` `Tess, renewed` `on a change to` `the cat's age` `on` (`the date` 2026 12 18) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 25(b), reading B -- the duty applies to` `Ana` `for` `Tess, renewed` `on a change to` `the cat's age` `on` (`the date` 2026 12 18) ``
- scenario "Chipped Tom turns one" (console)
- simulation: seed 1, 365 days, default parameters (console)
- text: Cat Regulations 2012 (02-b0-00), r. 17(m): "the age, breed (if known), colour, gender and sterilisation status of the cat"

**Challenge (2026-10-02).** Interpretation Act s. 18 and the presumption against absurdity favour reading A, but reading A also takes the owner's address, which plainly can change, out of 'change' only if the information is frozen at implanting -- which would defeat s. 25(b) itself. The provision cannot be read both ways consistently; left open.

**Suggested repair.** Replace 'the age' in r. 17(m) with 'the date of birth (or, if unknown, the estimated age at the date of implanting)'.

### T-35 -- Section 25's 7 days run from a change the owner may never learn of

- **Provision:** s. 25; Cat Regulations 2012 r. 16(g), r. 17(c)-(e)
- **Category:** T
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The owner must notify 'within 7 days after the change to the information'. Some prescribed items are about other people: the implanter's name, organisation and contact details (r. 17(c)-(e)), and the details of an alternative contact (r. 16(g)). If those change, the owner is in breach on the eighth day without having known of the change. Parliament enacted a repair in 2021 -- time to run from when the owner 'becomes aware of the change' (Dog Amendment (Stop Puppy Farming) Act 2021 s. 55) -- not yet commenced. ENCODING-NOTES N-43.

**Why it matters.** An owner can be in breach of s. 25 without knowing anything changed. Parliament has already enacted the fix; it has not been proclaimed.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 25 --` `Ana` `contravenes the section for` `Tess, renewed` `on a change to` `contact details for the microchip implanter's company or organisation` `on` (`the date` 2026 12 18) `, having given` EMPTY `, on` (`the date` 2026 12 30) `given the holidays` `the holidays` ``
- scenario "Dr Vu's practice changes its phone number and nobody tells Ana" (console)
- text: Dog Amendment (Stop Puppy Farming) Act 2021, as passed, s. 55 (new s. 25): "within 7 days after the day on which the owner becomes aware of the change"

**Challenge (2026-10-02).** Criminal Code s. 24 (mistake of fact), applied to Cat Act offences by s. 36, would very likely excuse an owner who honestly and reasonably believed nothing had changed, which lowers the severity. It does not answer the defect: the duty still runs from a change the owner cannot know of, the excuse must be raised at trial or against an infringement notice (Sch. 2 item 11), and Parliament has enacted the repair. OPEN at low-medium.

**Suggested repair.** Commence the Dog Amendment (Stop Puppy Farming) Act 2021 s. 55, or amend s. 25 to the same effect, and confine r. 17 to information about the cat and its owner.

### R-36 -- "Has effect from the period specified in the registration certificate", which specifies no period or start

- **Provision:** Cat Regulations 2012 r. 12(2)(a); r. 14, Sch. 1 Form 2
- **Category:** R (also F)
- **Status:** OPEN, severity low
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** A registration 'has effect from the period specified in the registration certificate'. A registration takes effect from a day, not a period ('for the period' or 'from the date' was probably meant), and the certificate prescribed by r. 14 (Form 2) has a field for the expiry date only. When a registration starts is therefore stated nowhere. Lead from 2A; ENCODING-NOTES N-44.

**Why it matters.** When a registration starts is stated nowhere; the regulation points at a field the prescribed certificate does not have.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `r 14 -- the fields of Form 2` EQUALS LIST `name of cat`, `description of cat: gender, age, sterilisation status, breed if known, colour`, `name and address of the person who registered it`, `name of the local government`, `registration number of cat`, `date the registration expires` ``
- scenario "A one-year registration granted on 25 October" (console)
- simulation: seed 1, 365 days, default parameters (console)
- text: Cat Regulations 2012 (02-b0-00), r. 12(2)(a): "has effect from the period specified in the registration certificate"
- text: Cat Regulations 2012 (02-b0-00), Sch. 1 Form 2: "This registration expires on"

**Challenge (2026-10-02).** Section 9(1) and (7): a grant has effect when made, for the period prescribed; that supplies a start in practice. The words remain a slip pointing at a field that does not exist. OPEN at low.

**Suggested repair.** 'has effect from the day on which it is granted or renewed (or a later day specified in the registration certificate) until ...', and add a start date to Form 2.

### U-38 -- A "3-year" registration can last two years and a day

- **Provision:** Cat Regulations 2012 r. 12(2)(a)(ii)
- **Category:** U (also T); fork FORK-06
- **Status:** OPEN, severity low-medium
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** A 3-year registration has effect until '31 October in the final year of that period'. On reading A (taken: the 31 October falling in the last 12 months of the 3-year period) one taking effect on 31 October lasts two years and a day, and one taking effect in March about two years and eight months, for the 3-year fee. Reading B (the calendar year in which the period ends) gives some registrations more than three years; reading C (the one-year rule three times) picks a 31 October outside the period. None gives three years. ENCODING-NOTES N-46 (found when an #EVAL returned 2028).

**Why it matters.** The 3-year fee buys anything from two years and a day to three years, depending on the day of grant, on the reading taken; no reading gives three years.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `r 12(2)(a)(ii) -- 31 October in the final year of the 3-year period beginning on` (`the date` 2026 10 31) EQUALS `the date` 2028 10 31 ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `r 12(2)(a)(ii) -- 31 October of the calendar year the period ends, reading B` (`the date` 2026 3 1) EQUALS `the date` 2029 10 31 ``
- scenario "A 3-year registration granted on 31 October" (console)

**Challenge (2026-10-02).** Interpretation Act ss. 5 ('year') and 62(3) fix how the period is reckoned, which is why reading A was taken; they do not make the result three years. Left open.

**Suggested repair.** Say 'until the third 31 October after the day on which it takes effect' (or 'until 31 October in the third year after the year in which it takes effect'), and align r. 12(2)(a)(i).

### T-39 -- Renewal outside the 21 days before 1 November, and an application after expiry, are not provided for

- **Provision:** Cat Regulations 2012 r. 12(2)(b); Sch. 3 item 1
- **Category:** T
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** A registration 'may be renewed to take effect as from 1 November in any year, within the preceding period of 21 days' (11 to 31 October, IA s. 61(1)(c)). The regulation does not say whether a renewal may be made at another time, from when it would then take effect, or whether an application after a registration has expired is a renewal or a fresh grant -- which changes the fee (a one-year grant from June to October costs $10, a renewal $20). ENCODING-NOTES N-47.

**Why it matters.** Owners renewing early or late do not know what they are buying, or what fee applies.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `r 12(2)(b) -- a renewal made on` (`the date` 2026 10 10) `may take effect from 1 November` 2026 ``
- scenario "Ana renews Tess in July, and again after she lapses" (console)
- simulation: seed 1, 365 days, default parameters (console)
- text: Cat Regulations 2012 (02-b0-00), r. 12(2)(b): "may be renewed to take effect as from 1 November in any year, within the preceding period of 21 days"

**Challenge (2026-10-02).** Section 9(1) obliges a local government to decide any application for renewal under s. 8, whenever made; nothing fixes its effect outside r. 12(2)(b). Not answered.

**Suggested repair.** Provide that a renewal takes effect on the day after the registration it renews expires, whenever applied for, and that an application after expiry is for a grant.

### D-41 -- The pensioner rate turns on "the owner", who may be several people

- **Provision:** Cat Regulations 2012 Sch. 3 cl. 1(3)
- **Category:** D
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The fee is halved 'if the owner of a cat is a pensioner'. A cat may have several owners (a child keeper and the parent, the owners of a business that keeps it), and the applicant may not be the owner whose status is in question. The clause does not say whether one pensioner owner suffices, or whether the applicant's status governs. (The encoding applies the test to the applicant: ENCODING-NOTES N-49.)

**Why it matters.** Small: the fee concession may be given or withheld depending on which owner applies.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `Sch 3 cl 1 -- the fee payable` (`an application by` `Pat, pensioner` `Max, taken in on 1 March` `for the grant of registration` (`the date` 2026 11 15) `one year` 10 (`the date` 2026 11 20)) EQUALS 10 ``
- scenario "Pat, a pensioner, registers his cat" (console)
- text: Cat Regulations 2012 (02-b0-00), Sch. 3 cl. 1(3): "if the owner of a cat is a pensioner"

**Challenge (2026-10-02).** Interpretation Act s. 10(c) makes 'the owner' include 'the owners', which, if anything, suggests all owners must be pensioners. Cl. 1(4) lets the local government reduce any fee, which softens the effect. OPEN at low.

**Suggested repair.** 'if the applicant is a pensioner'.

### U-44 -- Does IA s. 71(2) make a continuing failure to "ensure" registration, microchipping or sterilisation a daily offence?

- **Provision:** ss. 5(1), 14(1), 18(1); Interpretation Act 1984 s. 71(2)
- **Category:** U; fork FORK-12
- **Status:** OPEN, severity low
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Interpretation Act s. 71(2) makes each day after conviction a further $50 offence where 'an act or thing is required or directed to be done but no period ... is specified'. Sections 5(1), 14(1) and 18(1) impose duties to 'ensure' a state of affairs. Reading A (taken; the reference register REF-41) treats them as acts required to be done; reading B does not, and s. 71 adds nothing. The Act could have said, and s. 78(c) shows the drafter knew how to provide daily penalties for regulations. ENCODING-NOTES N-54.

**Why it matters.** Whether continued non-compliance after conviction is a daily offence turns on a reading of the Interpretation Act the Cat Act could have settled.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 71 -- the subsection that applies to` `s 71 -- s 5(1) is` EQUALS "s 71(2)" ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 71, reading B of FORK-12 -- s 71 reaches the duty to ensure` ``
- scenario "Ana takes in Max; the 14-day grace ends" (console)
- text: Interpretation Act 1984, s. 71(2)(a): "by or under a written law an act or thing is required or directed to be done but no period within which or time by which that act or thing is to be done is specified"

**Challenge (2026-10-02).** No authority in the set decides whether a duty to ensure is a duty 'to do an act or thing'. Left open; the consequence is modest ($50 a day after conviction).

**Suggested repair.** State in Part 2 whether a failure under ss. 5(1), 14(1) and 18(1) is a continuing offence, and the daily penalty.

### T-46 -- A one-year registration granted in late October lasts days

- **Provision:** Cat Regulations 2012 r. 12(2)(a)(i); Sch. 3 item 1(a)
- **Category:** T
- **Status:** OPEN, severity low
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Every one-year registration ends on 'the next 31 October', however late in the year it is granted. One granted on 25 October lasts six days; it costs $10 (Sch. 3 item 1(a)), the same as one granted on 1 June that lasts five months, and must be renewed at once for $20. An owner whose cat reaches 6 months in late October cannot wait for 1 November without breaching s. 5(1). Found setting r. 12(2)(a)(i) beside Sch. 3; a generated year shows it.

**Why it matters.** Small, but it falls on owners who comply on time: a cat that reaches 6 months in late October costs two fees within a fortnight.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `r 12(2)(a)(i) -- the next 31 October after` (`the date` 2026 10 25) EQUALS `the date` 2026 10 31 ``
- scenario "A one-year registration granted on 25 October" (console)
- simulation: seed 1, 365 days, default parameters (console)

**Challenge (2026-10-02).** The half fee for grants from June shows the drafter saw short first registrations, but it is flat. The owner may choose a 3-year or lifetime registration instead. OPEN at low.

**Suggested repair.** Run a one-year registration granted after a set day (say 1 August) to the second 31 October, or allow a grant in October to take effect from 1 November.

### X-47 -- The explanatory memorandum says s. 7 deals mainly with forged tags; its words do not reach them

- **Provision:** s. 7; s. 3(1) "registration tag"
- **Category:** X
- **Status:** OPEN, severity low
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The Cat Bill 2011 explanatory memorandum (cl. 7 note) presents s. 7 as mainly concerned with forged tags and with tags put on unregistered cats. Section 7 forbids removing or interfering with 'a registration tag worn by a cat', and a registration tag is 'the registration tag given to the owner ... under section 11(1)(c)'. A forged or home-made tag is not one, and fastening a council's tag to another cat is not 'interfering with a registration tag worn by a cat'. No other provision of the Act creates an offence of forging or misusing a tag.

**Why it matters.** A reader relying on the memorandum would think forging tags is an offence under s. 7. It is not an offence under the Act at all.

**Evidence.**

- scenario "Ben puts a home-made tag on unregistered Tom" (console)
- text: Cat Act 2011 (00-l0-01), s. 7: "remove or interfere with a registration tag worn by a cat"
- text: Cat Act 2011 (00-l0-01), s. 3(1) "registration tag": "means the registration tag given to the owner of the cat under section 11(1)(c)"

**Challenge (2026-10-02).** Interpretation Act s. 19 allows the memorandum to be used only to confirm the ordinary meaning or resolve ambiguity, so it cannot extend s. 7; that is why the gap is real. Section 85 covers false information to an authorised person or in an application, not a forged tag on a cat. OPEN at low.

**Suggested repair.** Add an offence of making, possessing or placing on a cat a tag that purports to be a registration tag and is not the cat's own.

### X-51 -- Form 1 tells applicants the council "may refuse an application"; the Act's power is to refuse to consider it

- **Provision:** Cat Regulations 2012 Sch. 1 Form 1 Part G; s. 9(6)
- **Category:** X (also P)
- **Status:** OPEN, severity low
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The declaration in Form 1 Part G states that the local government may refuse an application if information is not provided within the time specified. The Act's power (s. 9(6)) is to refuse to consider it -- which, unlike a refusal, carries no s. 13 notice and no review (P-15). An applicant or a local government reading the form is led to the wrong consequence.

**Why it matters.** Applicants and local governments are told the wrong consequence, and the difference matters (P-15).

**Evidence.**

- scenario "The council refuses to consider Ana's application for Tom" (console)
- text: Cat Regulations 2012 (02-b0-00), Sch. 1 Form 1 Part G: "The local government may refuse an application if any or all of the required information is not provided within the time period specified in the legislation."
- text: Cat Act 2011 (00-l0-01), s. 9(6): "The local government may refuse to consider an application if the applicant does not comply"

**Challenge (2026-10-02).** The form is part of the regulations, but an explanatory statement in it cannot enlarge s. 9(6) (Interpretation Act s. 43(1)). It remains misleading. OPEN at low.

**Suggested repair.** 'The local government may refuse to consider an application if ...' (or repair P-15 and keep the form).

### F-52 -- Regulation 12(1) repeats "for": "may be for — ... (b) for the life of the cat"

- **Provision:** Cat Regulations 2012 r. 12(1)
- **Category:** F
- **Status:** OPEN, severity low
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The chapeau ends 'may be for —' and paragraph (b) begins 'for the life of the cat'. Grammar only.

**Why it matters.** Form only.

**Evidence.**

- text: Cat Regulations 2012 (02-b0-00), r. 12(1): "Registration of a cat may be for —"
- text: Cat Regulations 2012 (02-b0-00), r. 12(1)(b): "for the life of the cat."

**Challenge (2026-10-02).** Nothing to answer: the print was confirmed current.

**Suggested repair.** Delete 'for' in r. 12(1)(b).

### F-53 -- Regulation 4: "each of the following bodies are prescribed"

- **Provision:** Cat Regulations 2012 r. 4
- **Category:** F
- **Status:** OPEN, severity low
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** 'Each ... are'; r. 6 has 'each of the following bodies is'. Grammar only.

**Why it matters.** Form only.

**Evidence.**

- text: Cat Regulations 2012 (02-b0-00), r. 4: "each of the following bodies are prescribed as operators of a facility for keeping cats"

**Challenge (2026-10-02).** Nothing to answer: the print was confirmed current.

**Suggested repair.** 'each of the following bodies is prescribed'.

### F-54 -- Form 1 labels dates of birth "Age (dd/mm/yy)"

- **Provision:** Cat Regulations 2012 Sch. 1 Form 1 Parts A and B
- **Category:** F
- **Status:** OPEN, severity low
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The owner's, the alternative contact's and the cat's dates of birth are asked for under the label 'Age', in a two-digit-year format; r. 16(d) records the owner's 'date of birth'. Formatting only, but it feeds FORK-15 (U-34): the database records an 'age'.

**Why it matters.** Form only, but it is the source of the 'age' field that U-34 turns on.

**Evidence.**

- text: Cat Regulations 2012 (02-b0-00), Sch. 1 Form 1 Parts A, B: "Age (dd/mm/yy)"
- text: Cat Regulations 2012 (02-b0-00), r. 16(d): "the cat owner's date of birth"

**Challenge (2026-10-02).** Nothing to answer: the print was confirmed current.

**Suggested repair.** 'Date of birth (dd/mm/yyyy)'.

---

## Findings verified sound

### D-02 -- The s. 4(2) presumption gives no day on which keeping began, for s. 5(2)(a)

- **Provision:** s. 4(2); s. 5(2)(a)
- **Category:** D
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** A person named in a microchip database is taken to keep and care for an unregistered cat, but s. 5(2)(a) asks how long 'the person' has kept it. ENCODING-NOTES N-10. The encoding treats such a person as outside s. 5(2)(a).

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `the person` `Ben` `is an owner of` `Max, recorded to Ben` `on` (`the date` 2026 10 1) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 5(2)(a) -- the cat` `Max, recorded to Ben` `has been kept by` `Ben` `for less than 14 days on` (`the date` 2026 10 1) ``
- scenario "Dr Vu chips and desexes Tom; Ana applies; the council registers him" (console)

**Challenge (2026-10-02).** The presumption is evidentiary and operates only 'in the absence of evidence to the contrary': evidence of when the keeping began is such evidence, and decides s. 5(2)(a).
 Answered by: Cat Act 2011 s. 4(2) ('in the absence of evidence to the contrary') [cat-act-2011-text].

### U-03 -- On which day does a cat reach 6 months of age?

- **Provision:** ss. 4(1)(c), 5(1), 9(2)(a), 14, 18; Interpretation Act 1984 s. 62
- **Category:** U; fork FORK-01
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The Act does not say how age is reckoned (ENCODING-NOTES N-08). The readings differ by a day.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT (`the date` 2025 8 15) `has reached` 6 `months of age on` (`the date` 2026 2 15) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `reading B --` (`the date` 2025 8 15) `has reached` 6 `months of age on` (`the date` 2026 2 15) ``
- scenario "Tom reaches 6 months unchipped, entire and unregistered" (console)

**Challenge (2026-10-02).** Interpretation Act s. 62 reckons a period of months to the numerically corresponding date less one; age is reached the next day, matching ordinary usage. The fork is closed.
 Answered by: Interpretation Act 1984 s. 62(1), (3) [wa-interpretation-act-1984].

### U-04 -- Is a child who keeps a cat still an owner beside the parent?

- **Provision:** s. 4(1)(b), (c)
- **Category:** U; fork FORK-02
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-09. Consequential: a child aged 14-17 would be liable for the owner's offences.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 4 -- the owners of` `Mo` `on` (`the date` 2026 10 1) EQUALS LIST "Kit", "Ana" ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 4, reading B -- the owners of` `Mo` `on` (`the date` 2026 10 1) EQUALS LIST "Ana" ``
- scenario "Kit, a child, takes in Mo and applies to register him" (console)

**Challenge (2026-10-02).** The chapeau 'means any of these persons' is cumulative: (c) adds the parent, it does not substitute. Criminal Code s. 29 limits the responsibility of children under 14. The fork is closed on the text.
 Answered by: Cat Act 2011 s. 4(1) ('owner ... means any of these persons') [cat-act-2011-text].

### U-07 -- Counting "less than 14 days" in s. 5(2)

- **Provision:** s. 5(2)(a), (b); Interpretation Act 1984 s. 61
- **Category:** U; fork FORK-04
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-15. The readings differ by a day at the end of the grace period.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 5(2)(a) -- the cat` `Max, taken in on 1 March` `has been kept by` `Ana` `for less than 14 days on` (`the date` 2026 3 14) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 5(2)(a), reading B of FORK-04 -- the cat` `Max, taken in on 1 March` `has been kept by` `Ana` `for less than 14 days on` (`the date` 2026 3 14) ``
- scenario "Ana takes in Max; the 14-day grace ends" (console)

**Challenge (2026-10-02).** Interpretation Act s. 61(1)(b) and (g) both exclude the first day; nothing in s. 5(2) points to inclusive counting. The fork is closed.
 Answered by: Interpretation Act 1984 s. 61(1)(b), (g) [wa-interpretation-act-1984].

### U-08 -- Does s. 5(2)(b) exempt a person never resident in the State?

- **Provision:** s. 5(2)(b)
- **Category:** U; fork FORK-09
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-16. Read literally, a non-resident has been resident for less than 14 days for ever.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 5(2)(b) --` `Vic, not resident` `has been resident in the State for less than 14 days on` (`the date` 2026 10 1) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 5(2)(b), reading B --` `Vic, not resident` `has been resident in the State for less than 14 days on` (`the date` 2030 10 1) ``
- scenario "Vic, who lives in Darwin, keeps Vito in Perth" (console)

**Challenge (2026-10-02).** The paragraph is a period of grace for newcomers; a construction promoting the Act's purpose (control of cats, s. 5(1)) is to be preferred. The fork is closed.
 Answered by: Interpretation Act 1984 s. 18 [wa-interpretation-act-1984].

### L-11 -- An unsterilised kitten under 6 months must be refused registration

- **Provision:** s. 9(2)(d), (4); s. 18(3)
- **Category:** L
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** TST
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 9(4) saves an unsterilised cat only if exempt under s. 18(2), and no certificate can apply under 6 months (s. 18(3)); an owner who registers early must be refused. ENCODING-NOTES N-18 (surfaced by the case 'Kitty').

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9 -- the decision required on` (`an application by` `Ana` `Kitty` `for the grant of registration` (`the date` 2026 9 1) `one year` 10 (`the date` 2026 9 3)) EQUALS `must refuse` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 5(1) -- the duty to ensure the cat is registered applies to` `Ana` `for` `Kitty` `on` (`the date` 2026 9 3) ``
- scenario "Ana applies to register Tom as he is; the council must refuse" (console)

**Challenge (2026-10-02).** No duty to register arises before 6 months (s. 5(1)), so the refusal costs the owner nothing and is consistent with the scheme (registration proves sterilisation: Cat Bill 2011 EM, cl. 5).
 Answered by: Cat Act 2011 s. 5(1) ('a cat that has reached 6 months of age') [cat-act-2011-text].

### U-12 -- "2 or more offences against any of the following": counted together across the three Acts?

- **Provision:** s. 9(2)(e); s. 10(b)
- **Category:** U; fork FORK-10
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-20. Consequential: refusal is mandatory.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9(2)(e) --` `Rex, one Dog Act and one AWA conviction` `has been convicted within the previous 3 years of 2 or more offences, as at` (`the date` 2026 11 20) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 9(2)(e), reading B of FORK-10 --` `Rex, one Dog Act and one AWA conviction` `has been convicted within the previous 3 years of 2 or more offences, as at` (`the date` 2026 11 20) ``
- scenario "Ben, with two recent convictions, applies to register his cat" (console)
- text: Legislative Council Supplementary Notice Paper 197-2 (internal copy), amendment 13/9 (checked against the pinned copy; not reproduced)

**Challenge (2026-10-02).** The words come from the Legislative Council's amendment, which replaced a single offence 'against' any of the Acts with '2 or more offences against any of the following': the list describes the offences counted, not separate counts. The fork is closed.
 Answered by: Legislative Council Supplementary Notice Paper 197-2, amendments 13/9 and 14/10 (Cat Bill 2011 cll. 9, 10) [lc-snp-197-2].

### P-14 -- A s. 9(5) requirement allowing more than 21 days

- **Provision:** s. 9(5), (6)
- **Category:** P
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-22: the Act does not say what follows if a local government specifies more than 21 days.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 9(6) -- the local government may refuse to consider` (`Ana's application, required to answer within` 22) `given the holidays` `the holidays` ``
- scenario "The council allows 30 days to answer" (console)

**Challenge (2026-10-02).** The limit is express: a requirement allowing more is not one 'under subsection (5)', so s. 9(6) cannot rest on it and the application must be decided.
 Answered by: Cat Act 2011 s. 9(5) ('within a specified time of not more than 21 days'), (6) ('a requirement under subsection (5)') [cat-act-2011-text].

### L-16 -- "If, and only if": must an application without the fee be granted?

- **Provision:** s. 8(2); s. 9(1), (2)
- **Category:** L
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 9(2) permits refusal only on its five grounds, and a missing fee or form is not one; the encoding's s. 9 decision does not consult s. 8(2).

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 8(2) -- the application is made as required` `Ana's application, no fee` ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 9 -- the decision required on` `Ana's application, no fee` EQUALS `must grant or renew` ``
- scenario "Ana applies for Max without paying the fee" (console)

**Challenge (2026-10-02).** Section 9 operates 'on receiving an application ... under section 8', and an application 'is to ... be accompanied by the fee' (s. 8(2)(b)): one without it is not an application under s. 8, and s. 9(2) is not reached.
 Answered by: Cat Act 2011 s. 9(1) ('an application ... under section 8') with s. 8(2) [cat-act-2011-text].

### T-23 -- Section 21 fixes no time for the certificate of sterilisation

- **Provision:** s. 21
- **Category:** T
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-31: when the duty is broken is not stated.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 71 -- the subsection that applies to` `s 71 -- s 21 is` EQUALS "s 71(2)" ``
- scenario "Dr Vu chips and desexes Tom; Ana applies; the council registers him" (console)
- text: Interpretation Act 1984, s. 63: "such act or thing shall be done with all convenient speed"

**Challenge (2026-10-02).** Where no time is fixed, the act is to be done with all convenient speed (IA s. 63). The reference register did not name s. 63; it is in the 0H set.
 Answered by: Interpretation Act 1984 s. 63 [wa-interpretation-act-1984].

### D-25 -- Section 18(2)(b) where a cat has several owners, only one an approved breeder

- **Provision:** s. 18(2)(b)
- **Category:** D
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-33: the encoding judges (b) by the owner whose duty is in question.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 18(2) --` `Queen` `is exempt from sterilisation on` (`the date` 2026 10 1) `, owned by` `Bree, approved breeder` ``
- scenario "Bree's breeding queen reaches 6 months entire" (console)

**Challenge (2026-10-02).** 'A cat is exempt from sterilisation if ... the cat is owned, for the purpose of breeding, by an approved cat breeder': the exemption attaches to the cat, so every owner has it. The law is clear; the encoding's per-owner test is narrower for co-owned cats (a corpus limitation, reported to the human, not a finding).
 Answered by: Cat Act 2011 s. 18(2) ('A cat is exempt from sterilisation if any of the following apply') [cat-act-2011-text].

### L-26 -- Sections 18(2)(c) and 23(2)(a)(iii) depend on a class no regulation prescribes

- **Provision:** s. 18(2)(c); s. 23(2)(a)(iii)
- **Category:** L
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** No regulation prescribes a class of cats exempt from sterilisation, so both limbs are unreachable, and a seller 'satisfied' that a cat belongs to such a class is satisfied of nothing. Lead from 2A; ENCODING-NOTES N-37.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `no regulation -- belongs to a class of cats prescribed as exempt from sterilisation` `Tom` ``
- scenario "Ana sells Tom unchipped and entire, with no voucher" (console)
- text: Cat Act 2011 (00-l0-01), s. 76(1): "all matters that are required or permitted by this Act to be prescribed"

**Challenge (2026-10-02).** The Act permits a class to be prescribed; it does not require one. An unused power leaves an empty limb, which harms no one and can be filled by regulation. Not a defect.
 Answered by: Cat Act 2011 s. 76(1) (matters 'required or permitted' to be prescribed) [cat-act-2011-text].

### L-28 -- An unchipped kitten under 6 months cannot lawfully be transferred

- **Provision:** s. 23(1); s. 14(3)
- **Category:** L
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 23(1) allows transfer of an unchipped cat only if a s. 14(2) certificate applies, and none can under 6 months; s. 23(2) has a voucher route for sterilisation, s. 23(1) none for microchipping. ENCODING-NOTES N-36.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 23(1) -- contravened by the transfer` (`a transfer of` `Kit-kat, 10 weeks, unchipped, with a certificate` `give away` (`the date` 2026 10 1) "Ana" (JUST "Ben") (`anyone else` "Ben") TRUE) ``
- scenario "Ana sells Tom unchipped and entire, with no voucher" (console)

**Challenge (2026-10-02).** That is the scheme Parliament was told of: all cats microchipped (and sterilised) before transfer (Cat Bill 2011 EM, overview, key feature (b); cl. 23); kittens can be chipped young, and transfers to r. 9 bodies are excepted (r. 19).
 Answered by: Explanatory Memorandum, Cat Bill 2011, overview (key feature (b)) and cl. 23 note [em-cat-bill-2011].

### R-32 -- Section 24 for a cat that is neither registered nor recorded with a database company

- **Provision:** s. 24(a), (b)
- **Category:** R
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-40: s. 24(a) has no addressee for an unregistered cat, s. 24(b) none for a cat with no company.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 24(a) -- notice to a local government is required for` (`a transfer of` `Tom` `give away` (`the date` 2026 10 1) "Ana" (JUST "Ben") (`anyone else` "Ben") TRUE) ``
- scenario "Ana sells Tom unchipped and entire, with no voucher" (console)

**Challenge (2026-10-02).** Each paragraph names its addressee by the registration or the record ('the local government with which the cat is registered'; 'the microchip database company for that cat'): with neither, there is nothing to correct and nothing to notify. Sound.
 Answered by: Cat Act 2011 s. 24(a), (b) [cat-act-2011-text].

### U-37 -- "The next 31 October" for a one-year registration taking effect on 31 October

- **Provision:** Cat Regulations 2012 r. 12(2)(a)(i)
- **Category:** U; fork FORK-05
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-45: read as the same day, a one-year registration would last a day.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `r 12(2)(a)(i) -- the next 31 October after` (`the date` 2026 10 31) EQUALS `the date` 2027 10 31 ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `r 12(2)(a)(i) -- the next 31 October, reading B` (`the date` 2026 10 31) EQUALS `the date` 2026 10 31 ``
- scenario "A one-year registration granted on 31 October" (console)

**Challenge (2026-10-02).** Registration may be 'for ... one year' (r. 12(1)(a)); 'the next 31 October' said on 31 October means a year away. The fork is closed.
 Answered by: Cat Regulations 2012 r. 12(1)(a) ('either one year or 3 years') [cat-regulations-2012].

### U-40 -- The $10 fee for an application "made after 31 May": after which 31 May?

- **Provision:** Cat Regulations 2012 Sch. 3 Table item 1(a)
- **Category:** U; fork FORK-07
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-48: every day is after some 31 May.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `Sch 3 item 1(a) -- made after 31 May for registration until the next 31 October` (`the date` 2026 11 15) ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `Sch 3 item 1(a) -- made after 31 May, reading B` (`the date` 2026 11 15) ``
- scenario "A one-year registration granted in November" (console)

**Challenge (2026-10-02).** The item ties the date to the registration year: 'made after 31 May for registration until the next 31 October'. A November application is for registration until the 31 October eleven months on, after a 31 May that has not yet come. The fork is closed.
 Answered by: Cat Regulations 2012 Sch. 3 Table item 1(a) ('made after 31 May for registration until the next 31 October') [cat-regulations-2012].

### T-42 -- Foster care for "a total of 12 weeks": whose placements count?

- **Provision:** Cat Regulations 2012 r. 9(3)(b)
- **Category:** T
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** ENCODING-NOTES N-50: whether placements by different bodies are added together is not said.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 5(2)(c), 9(2)(b) -- belongs to a class of cats prescribed as exempt from registration` (`a stray fostered for SAFE for` 85) ``
- scenario "A SAFE group places a stray in foster care for 13 weeks" (console)

**Challenge (2026-10-02).** The proviso counts the cat's time: 'provided that the cat has not been in foster care for more than a total of 12 weeks' -- all foster care, by whomever placed. Clear.
 Answered by: Cat Regulations 2012 r. 9(3)(b) [cat-regulations-2012].

### P-43 -- Regulation 10 exempts an owner, where s. 6(2) authorises exempting a class of cats

- **Provision:** s. 6(2); Cat Regulations 2012 r. 10
- **Category:** P
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** RD
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 6(2) speaks of 'a class of cats prescribed as exempt'; r. 10(2) exempts 'the owner of a cat that is being exhibited ... but only while that cat is being exhibited'. ENCODING-NOTES N-52.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT NOT `s 6(1) --` `Ana` `contravenes the subsection for` `Tess, renewed` `on` (`an outing on` (`the date` 2026 12 1) TRUE FALSE (JUST `Cats United WA Incorporated`)) ``
- scenario "Tess is exhibited untagged at a Cats United show" (console)
- text: Cat Regulations 2012 (02-b0-00), r. 10(2): "The owner of a cat that is being exhibited is exempt"

**Challenge (2026-10-02).** The exemption is defined entirely by a class of cats -- those 'being exhibited' as r. 10(1) defines it -- so in substance it prescribes the s. 6(2) class; and regulations may be made for anything 'necessary or convenient' for the Act (s. 76(1)). Within power.
 Answered by: Cat Regulations 2012 r. 10(1), (2), made under Cat Act 2011 ss. 6(2), 76(1) [cat-regulations-2012].

### T-45 -- Sections 14(2)-(3) and 18(2)-(3) commenced a year before the duties they qualify

- **Provision:** s. 2(b), (c)
- **Category:** T
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** ENC
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** Section 2(c) lists '14(1)' and '18(1)' for 1 November 2013, so the exemptions commenced on 1 November 2012. ENCODING-NOTES N-55.

**Evidence.**

- assertion in `lqa-evidence.l4`: `` #ASSERT `s 2 -- the day` `s 14(2)-(3)` `comes into operation, assent being on` (`the date` 2011 11 9) EQUALS `the date` 2012 11 1 ``
- assertion in `lqa-evidence.l4`: `` #ASSERT `s 2 -- the day` `s 9` `comes into operation, assent being on` (`the date` 2011 11 9) EQUALS `the date` 2012 11 1 ``
- scenario "Dr Vu certifies that chipping may harm 2-month-old Tom" (console)

**Challenge (2026-10-02).** Registration (s. 9) began on 1 November 2012, and s. 9(3)-(4) refer to the exemptions in ss. 14(2) and 18(2): they had to be in force then. Deliberate.
 Answered by: Cat Act 2011 s. 2(b), (c), with s. 9(3), (4) [cat-act-2011-text].

### X-48 -- The explanatory memorandum describes refusal of registration for a single conviction

- **Provision:** s. 9(2)(e)
- **Category:** X
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The Cat Bill 2011 explanatory memorandum (cl. 9 note) describes refusal where the applicant has been convicted of an offence in the last 3 years; the Act requires 2 or more.

**Evidence.**

- scenario "Ben, with two recent convictions, applies to register his cat" (console)
- text: Legislative Council Supplementary Notice Paper 197-2 (internal copy), amendment 13/9 (checked against the pinned copy; not reproduced)

**Challenge (2026-10-02).** The memorandum describes the Bill as introduced; the Legislative Council amended cl. 9 to '2 or more offences'. A reader using the memorandum must take account of the amendment; no one is misled about the enacted words.
 Answered by: Legislative Council Supplementary Notice Paper 197-2, amendment 13/9 [lc-snp-197-2].

### X-49 -- The explanatory memorandum limits the sterilisation voucher to cats too young to be sterilised; s. 23(2)(b) does not

- **Provision:** s. 23(2)(b)
- **Category:** X
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The Cat Bill 2011 explanatory memorandum (cl. 23 note) says the voucher is intended only for cats too young to be sterilised. Section 23(2)(b) allows a voucher for any cat; an amendment to limit it in that way was proposed in the Council (SNP 197-2, 7/23) and is not in the Act.

**Evidence.**

- scenario "Ana sells adult Max entire, with a sterilisation voucher" (console)
- text: Legislative Council Supplementary Notice Paper 197-2 (internal copy), amendment 7/23 (checked against the pinned copy; not reproduced)
- text: Cat Act 2011 (00-l0-01), s. 23(2)(b): "a voucher is given to the purchaser by the person to enable the purchaser to have the cat sterilised at a later date by a veterinarian at no cost to the purchaser"

**Challenge (2026-10-02).** The words are clear; extrinsic material may only confirm the ordinary meaning or resolve ambiguity or absurdity, so the memorandum cannot narrow s. 23(2)(b). The rejected amendment confirms the words were meant.
 Answered by: Interpretation Act 1984 s. 19(1) [wa-interpretation-act-1984].

### X-50 -- The explanatory memorandum says s. 8 requires the owner to apply; s. 8 permits

- **Provision:** s. 8(1)
- **Category:** X
- **Status:** VERIFIED-NO-DEFECT
- **Found by:** CMP
- **Print:** 00-l0-01, currency start 25 Sep 2025; checked against the current print 2026-10-02

**What.** The Cat Bill 2011 explanatory memorandum (cl. 8 note) says the clause requires the owner to apply for registration; s. 8(1) says the owner 'may apply'.

**Evidence.**

- scenario "Ana applies to register Tom as he is; the council must refuse" (console)
- text: Cat Act 2011 (00-l0-01), s. 8(1): "may apply to that local government for the grant or renewal of the registration of the cat"

**Challenge (2026-10-02).** The duty the memorandum describes is imposed by s. 5(1); read with it, s. 8 is the means. No outcome differs.
 Answered by: Cat Act 2011 s. 5(1) [cat-act-2011-text].
