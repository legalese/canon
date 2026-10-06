# Policy defect records: home, property, fire, engineering, construction, liability

Rows: VN-05, VN-07, VN-08, VN-09, VN-20, VN-21, VN-22.
Source of every record: the row's `NOTES.md` section 4 (Findings) and its findings test module, read only.
"src:N" is the encoder's citation into the row's source text.
Any legal statement is "on the literal reading", as the encoder framed it.

---

## VN-05 Liberty HomeCare

Directory: `vn-liberty-homecare/encodings/legalese-2026-10-vn-05`.
Findings module: `homecare-findings.l4`.

### VN-05 X-negligence — Personal liability cover excludes the insured's own negligence
- **Class**: T6 / T2
- **Scenario**: Part 2 exclusion 1 removes liability from an "intentional or negligent act" with reasonably foreseeable consequences. A guest trips on a rug the insured left loose; damages 300,000,000 and costs 20,000,000 are claimed, and the claim pays 0 on exclusion 1 alone.
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: LITERAL ("read as written").
- **Evidence**: `homecare-findings.l4:35-36` (grounds EQUALS exclusion 1; amount payable EQUALS 0). src:532-535.
- **Plain-English test of surprise**: a buyer of personal liability cover expects carelessness to be the main thing covered; the wording pays almost only for liability without fault.

### VN-05 X-visitors — Every injured guest counts as a household resident
- **Class**: T5 / T6
- **Scenario**: Exclusion 3 treats a person as "usually residing with the Insured" if that person "has used the Home". Every guest injured at the Home has used it, so on the literal words every visitor injury falls in the household exclusion.
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: CONTESTED (F-excl3: the encoder reads "used" as used as a place to live).
- **Evidence**: `homecare-findings.l4:45` (`on its literal words, exclusion 3 treats as usually residing` `a visitor` is TRUE). src:541-543.
- **Plain-English test of surprise**: a householder expects injured guests to be the classic liability claim; the literal deeming rule makes every guest a household member.

### VN-05 X-home-c — Definition of the Home excludes houses and apartments
- **Class**: T7 / T6
- **Scenario**: The Home is a house or apartment (src:74), yet exclusion (c) removes "các loại nhà và căn hộ" (the kinds of houses and apartments): literally, no Home is ever insured. It also excludes strata-title apartments, which most owned Vietnamese apartments are (encoder: outside knowledge, unverified).
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: CONTESTED. Literal reading empties the definition; the encoder adopts reading (ii), establishments of those kinds (F-home-c).
- **Evidence**: `homecare-findings.l4:53-54` (both literal predicates TRUE for a house and for an apartment). src:74, 93-94.
- **Plain-English test of surprise**: a homeowner expects a home policy to cover the home; the literal definition excludes every home.

### VN-05 X-flood — Flood cover granted then removed by water exclusions
- **Class**: T6 / T7
- **Scenario**: Flood includes overflow of the public water main, but Peril 5 limbs (g) "by water or rain" and (h) escape of water from any pipe exclude it. A burst-main flood is excluded on the literal words, covered on the encoder's reading.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (F-flood: the encoder reads (g) and (h) as not reaching defined flood).
- **Evidence**: `homecare-findings.l4:70` (literal exclusion TRUE), `:72` (grounds EQUALS EMPTY on the reading taken). src:218-220, 232-234.
- **Plain-English test of surprise**: a buyer told flood is covered expects a burst water main to be covered; the same clause takes water damage back.

### VN-05 X-claim-time — Liability claim deadline can expire before any claim
- **Class**: T1 / T3
- **Scenario**: GC4(g) requires a written claim within 30 days "from the day of the event", a condition precedent under GC1, though a third party may first demand compensation months later. A dog-bite claim delivered 46 days after the bite fails; the trace shows breach on day 31.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW. Law art 30(1) allows one year; art 30(3) runs a liability claim from the third party's demand (F-gc4g).
- **Evidence**: `homecare-findings.l4:85` (grounds EQUALS GC1 with GC4(g)); trace in `homecare-tests-part3-conditions.l4:466-469`. src:848-852.
- **Plain-English test of surprise**: an insured expects the clock to start when the victim claims; the wording starts it at the incident.

### VN-05 X-precedent — Any breach of any duty defeats every claim
- **Class**: T12 / T3
- **Scenario**: GC1 makes every term a condition precedent to any payment. Without kept purchase receipts (src:339-341), a fire claim on the house itself pays 0, though no receipt is needed to prove its value.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("as written"). The encoder notes Law art 46 and art 19(3) narrow this for late notice only.
- **Evidence**: `homecare-findings.l4:101` (amount payable EQUALS 0 with `kept receipts or proof of value` FALSE). src:802-807, 339-341.
- **Plain-English test of surprise**: a homeowner expects a lost receipt to matter only where value is in doubt; the wording forfeits an undisputed fire claim.

### VN-05 X-award — Arbitration win forfeited after twelve months
- **Class**: T12 / T7
- **Scenario**: GC10 makes an arbitral award final. GC7(b)(ii) forfeits benefit for claims decided by arbitration "không có kháng nghị" (without the insured's challenge) within 12 months. A final award cannot be challenged, so every arbitrated claim, won or lost, is forfeited a year after the award: an award of 1 August 2026, asked on 2 August 2027, is a forfeiture ground.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `homecare-findings.l4:113` (grounds EQUALS GC7(b)(ii)). src:913-915, 945-946.
- **Plain-English test of surprise**: an insured who wins at arbitration expects to be paid; the wording forfeits the win unless the insured challenges it.

### VN-05 X-war — War exclusion worded as a terrorism exclusion
- **Class**: T5
- **Scenario**: General Exclusion 1's chapeau excludes loss connected with "any act of terrorism", then lists war, terrorism and rebellion. On reading (i), war damage with no terrorism is not excluded by GE1, and fire is covered whatever the cause (src:166).
- **Who bears it**: insurer. **Money direction**: against the insurer (on reading (i)).
- **Standing**: CONTESTED. The encoder takes reading (ii), each limb excluded (F-ge1), and says reading (i) is open to the insured under Law art 24.
- **Evidence**: `homecare-findings.l4:126` (reading (i) excludes war is FALSE), `:127` (reading taken excludes). src:687-697, 166.
- **Plain-English test of surprise**: an insurer expects war to be excluded; the clause as drafted can be read to exclude only terrorism.

### VN-05 X-debris — Demolition and shoring cover deleted for typical buyers
- **Class**: T6 / T7
- **Scenario**: Extension 5 deletes limbs (b) and (c) when the Home OR the Renovation Costs OR the Contents is uninsured. Renovation Costs exist only for a tenant, so the usual owner (Home and Contents) and the usual tenant (Renovation Costs and Contents) both lose demolition and shoring cover.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `homecare-findings.l4:137-138` (deleted under both the owner's and the tenant's fixture Summary). src:383-384, 106-108.
- **Plain-English test of surprise**: a buyer expects a listed extension to be available; the deletion trigger is met by almost every ordinary policy.

### VN-05 X-rent — Rent benefit for a landlord the definitions exclude
- **Class**: T7 / T6
- **Scenario**: Part 3 limb 1 pays rent "as landlord not occupying the Insured Location", but that Location and the Home are defined as the insured's own residence. Literally, the limb never applies to a let house (test: fire, 2 months unfit, rent lost 50,000,000).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (F-p3-rent: the encoder does not apply the residence requirements to limb 1).
- **Evidence**: `homecare-findings.l4:150` (NOT `the rent limb can apply`). src:632-633, 69-72, 76.
- **Plain-English test of surprise**: a landlord sold a loss-of-rent benefit expects it to work for a let house; the definitions make the let house uninsurable.

### VN-05 X-personal-effects — Contents include personal effects, then exclude them
- **Class**: T6 / T7
- **Scenario**: Contents include personal effects "normally carried or worn on the person"; exclusion (j) removes items "normally carried out of the insured location". A handbag or watch is both, so not Contents; literally, (j) also removes the photographic and sports equipment limb (a) admits.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL for personal effects; CONTESTED for equipment (encoder reads (j) as reaching portable items only, F-contents-j).
- **Evidence**: `homecare-findings.l4:180` (NOT `the property is Contents`), `:182` (literal (j) reaches the equipment). src:115-119, 155-157.
- **Plain-English test of surprise**: a buyer told personal effects are covered expects a watch at home to be covered; the exclusion catches it.

### VN-05 X-vacancy — Three vacancy rules, a weekend away voids water cover
- **Class**: T7 / T5
- **Scenario**: Escape of water is excluded for a Home "vacant or unused" with no minimum period; theft only after more than 30 consecutive days unattended; GC3(d) ends cover after more than 30 days vacant. A three-day vacancy defeats an escape-of-water claim on Peril 6(b) and nothing else.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `homecare-findings.l4:190` (3 days vacant; grounds EQUALS Peril 6(b)). src:243, 275, 829.
- **Plain-English test of surprise**: a family away for a weekend expects to stay covered; a pipe leak while away is excluded.

### VN-05 X-atmosphere — Storm loss excludable as atmospheric conditions
- **Class**: T2 / T7
- **Scenario**: Peril 5(i) excludes atmospheric conditions except storm and flood, but Part 1 exclusion 2 excludes "the action of light or atmospheric conditions" with no storm exception. A typhoon loss recorded with atmospheric conditions fails on Part 1 exclusion 2.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (the encoder says an insurer "can read" it onto any storm loss).
- **Evidence**: `homecare-findings.l4:198` (typhoon; grounds EQUALS Part 1 exclusion 2). src:235-236, 410-411.
- **Plain-English test of surprise**: a buyer sold storm cover expects a typhoon to be covered; a general exclusion can swallow it.

### VN-05 X-appeal — Liability cover does not answer appeal judgments
- **Class**: T2 / T6
- **Scenario**: The Part 2 indemnity does not apply to judgments "không phải là phán quyết sơ thẩm" (that are not first-instance judgments) of a competent Vietnamese court. A judgment on appeal is not first-instance, so liability fixed on appeal fails on the Jurisdiction clause.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (F-jurisdiction reads the qualifier as reaching judgments only).
- **Evidence**: `homecare-findings.l4:207` (appellate judgment; grounds EQUALS Jurisdiction). src:464-469.
- **Plain-English test of surprise**: an insured expects cover to follow the final judgment; the wording covers only the first one.

### VN-05 X-fence — Theft cover requires a fenced home, apartments fail
- **Class**: T6 / T7
- **Scenario**: Peril 9 covers theft only "tại Ngôi Nhà có tường rào" (at a Home with a perimeter wall or fence). An apartment in a block usually has none of its own, so apartments the Home definition admits may have no theft cover: a forcible theft from an unenclosed apartment fails on Peril 9.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (encoder hedges "may have no theft cover").
- **Evidence**: `homecare-findings.l4:214` (grounds include Peril 9: not enclosed). src:263.
- **Plain-English test of surprise**: an apartment owner sold theft cover expects a break-in to be covered; the fence requirement removes it.

### VN-05 X-sublimit — Printed tenant sub-limit above the schedule limit
- **Class**: T6 / T7
- **Scenario**: The tenant's Extension prints a limit of 160,000,000 per Occurrence, but the Part 2 limit comes from the Summary. With a hypothetical Summary limit of 100,000,000, a 200,000,000 claim pays 100,000,000 and the printed 160,000,000 never binds.
- **Who bears it**: insured (tenant). **Money direction**: against the claimant.
- **Standing**: LITERAL (figures hypothetical).
- **Evidence**: `homecare-findings.l4:221` (amount payable EQUALS 100,000,000). src:514.
- **Plain-English test of surprise**: a tenant reading "160,000,000 per Occurrence" expects that much; the schedule limit can sit lower and govern.

### VN-05 X-discretion — Discretion without criteria across several clauses
- **Class**: T11 / T5
- **Scenario**: GC2 says the policy "may become void" with no decider or test; GC12(e) makes "all reasonable recommendations of the Insurer" a condition precedent; depreciation for Actual Value has no rate; "reasonable dispatch" and "seriously injured" are undefined; the death benefit states a limit and no amount.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL, reading only. LAW noted on GC2: art 22(2) requires intent (F-gc2).
- **Evidence**: reading only. src:809-810, 971, 288, 317, 658, 661.
- **Plain-English test of surprise**: a policyholder expects conditions with a test; these let the insurer decide outcomes on undefined standards.

### VN-05 X-translation — Translation errors that change meaning
- **Class**: T13 (translation defects in a Vietnamese-only text) / T5
- **Scenario**: "luật hôn nhân" (marriage law) appears twice where martial law is meant; GE8 is a prohibition placed under "the Insurer shall not be liable for"; "aircraft that cannot be piloted" is likely meant as a drone; GE1(d) "an excluded risk" is circular; the helper proviso 2 is likely inert.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only; the encoder hedges "likely meant".
- **Evidence**: reading only. src:696-697, 790-791, 135, 703, 679-681.
- **Plain-English test of surprise**: a reader expects the published text to say what was meant; several clauses say something else.

### VN-05 X-undefined — Capitalised terms that are never defined
- **Class**: T5
- **Scenario**: "Sự Kiện Bảo Hiểm" (Insured Event) carries Peril 4(iii) and GC4 but is defined nowhere; "Bên Mua Bảo Hiểm" (the policyholder) appears once; "Tài sản được Bảo hiểm", two names for the limit, and "Personal Accident" (whose existence removes the death benefit) are used and undefined.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:213, 833, 51, 426, 773, 897, 636, 653, 665.
- **Plain-English test of surprise**: a reader expects capitalised terms to be defined; outcomes turn on terms with no definition.

### VN-05 X-payment-time — The insurer has no deadline to pay
- **Class**: T1 / T3
- **Scenario**: The document gives the insured 30 days to claim and 12 months to challenge, and gives the insurer no time to assess or pay. A claim delivered on day 10 leaves the insurer's duty to pay still standing, undischarged, on day 400.
- **Who bears it**: insured. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL (document silent). The encoder notes Law art 31(1) supplies 15 days (LAW-31); not encoded.
- **Evidence**: trace in `homecare-tests-part3-conditions.l4:472-477`. GC4; Comparables.
- **Plain-English test of surprise**: an insured expects both sides to have deadlines; only the insured has one.

### VN-05 X-cancel — Insurer may cancel without cause on notice
- **Class**: T3 / T11
- **Scenario**: GC11 lets the insurer cancel without cause on 30 days' notice, counted from sending. The encoder notes Law art 26 lists the grounds for unilateral termination.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW, as flagged by the encoder (LAW-26: encoded "as written"; art 26 lists grounds). Reading only.
- **Evidence**: reading only. src:947-949.
- **Plain-English test of surprise**: a policyholder expects a one-year policy to last the year; the insurer can end it at will.

#### VN-05 row summary
- Findings in section 4: 21 (X-negligence to X-cancel); 21 records above.
- Three most counterintuitive: X-award (winning an arbitration forfeits the claim after a year); X-home-c (the definition of Home, read literally, excludes all houses and apartments); X-negligence (personal liability cover excludes negligence).
- Matches in this group: X-cancel = VN-07 F14, VN-08 F20, VN-09 X13, VN-20 X16 (cancel at will, Law art 26). X-payment-time = VN-07 F20, VN-08 F22, VN-09 X21, VN-20 X19 (no insurer payment deadline, Law art 31). X-precedent = VN-08 F2, VN-09 X8, VN-20 X14, VN-21 F3, VN-22 X6 (any breach defeats any claim). X-vacancy = VN-07 F10, VN-08 F6, VN-20 X8. X-award = VN-20 X18 (an arbitral win must still be followed up within 12 months). X-fence ~ VN-07 F19 (theft needs force at a building). X-claim-time ~ VN-21 F1 (notice clock runs from the event, not from when the claim can be made). X-undefined = VN-07 F17, VN-08 F12, VN-21 F12, VN-22 X20. X-translation ~ VN-21 F19, VN-22 X21. X-war ~ VN-20 X2 (terrorism wording narrower or broader than meant).

---

## VN-07 UIC property all risks

Directory: `vn-uic-property-all-risks/encodings/legalese-2026-10-vn-07`.
Findings module: `uic-par-findings.l4`. The encoder numbers findings 1 to 21; ids below are "F-n" for finding n (not the fork ids F1-F37 of section 3, which are cited as "fork F-").

### VN-07 Finding 1 — Riot damage saved by one clause, excluded by another
- **Class**: T7 / T6
- **Scenario**: B1's carve-back saves loss by "nổi loạn" (riot); A3(b) excludes "nổi loạn" (rebellion). Rioters break a shopfront's fixed glass: saved from B1, excluded by A3(b). With one word, one meaning, riot damage is never covered; strike damage is.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F7: one meaning taken; splitting riot from rebellion, as the English market wording does, is listed).
- **Evidence**: `uic-par-findings.l4:27-28` (exclusions EQUALS `LIST "A3(b)"`), `:30-31` (riot excluded, strike not). src:123-124, 202-203.
- **Plain-English test of surprise**: a shop owner reading "riot" in the list of saved perils expects riot damage paid; another clause takes it back.

### VN-07 Finding 2 — Three conflicting rules for property insured elsewhere
- **Class**: T7 / T4
- **Scenario**: B3(i) excludes property insured separately; B4, garbled, pays only the excess over other insurance; GC 6 caps at an undefined "rateable proportion". Loss 100, other policy paying 60: B4 leaves 40, which GC 6 makes uncomputable. If the other policy pays rateably (37.5), the insured recovers 77.5.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (rests on forks F12 and F13; F20 not answered; Law:588-591 favours F12 (i)).
- **Evidence**: `uic-par-findings.l4:36`, `:39` (40,000,000), `:40` (REFUSED), `:45-46` (77,500,000). src:240, 242-245, 331-336.
- **Plain-English test of surprise**: a business with two policies expects full recovery between them; the wording can leave 22.5% unpaid.

### VN-07 Finding 3 — Twelve-month bar cuts short a three-month suit window
- **Class**: T1 / T7
- **Scenario**: Loss 15 June 2026, claim 1 July, rejected 1 May 2027, suit 15 July 2027: inside GC 4(b)'s three months (to 1 August). But GC 12 ends liability twelve months after the loss unless the claim is pending or in arbitration, and on 15 June 2027 it was neither: the insurer owes 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, on fork F25 reading (i) (a rejected claim is not pending).
- **Evidence**: `uic-par-findings.l4:55-58` (owes 0). src:309-312, 481-483.
- **Plain-English test of surprise**: an insured given three months to sue expects to be in time; a different clause has already ended liability.

### VN-07 Finding 4 — Arbitration default counted from two different days
- **Class**: T1 / T7
- **Scenario**: The party asked is late two months from the request, but the other may appoint a sole arbitrator only two months from receipt. A request made 31 July 2026, received 30 August, leaves 30 days of default without remedy. GC 7 also lacks an umpire mechanism and reaches only disputes on amount.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL (fork F32 keeps both as written).
- **Evidence**: `uic-par-findings.l4:64` (EQUALS 30). src:344-347.
- **Plain-English test of surprise**: a party expects a default to be remediable once it occurs; the wording leaves a month-long gap.

### VN-07 Finding 5 — Unlimited insurer powers after loss; any non-compliance forfeits
- **Class**: T11 / T12
- **Scenario**: After a loss the insurer may take possession of "bất kỳ tài sản nào của Người được bảo hiểm" (ANY property of the Insured) on the premises until final settlement, without liability. Non-compliance with "the Insurer's requirements", which have no criteria, forfeits all benefit under the Policy.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only (the encoding takes non-compliance as an input).
- **Evidence**: reading only. src:418-445.
- **Plain-English test of surprise**: an insured expects the insurer to handle damaged property only; the wording reaches any property and forfeits on undefined demands.

### VN-07 Finding 6 — Insurer's opinion alone shifts the terrorism burden
- **Class**: T11 / T5
- **Scenario**: Terrorism is defined "including but not limited to", and reaches force by an individual "for similar purposes"; one person wrecking machinery in protest could fall in it, though B1's carve-back saves "malicious persons". Once the insurer "considers" A3(c) applies, with no proceedings, the insured must prove the loss is covered.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL for the burden shift; whether an act was terrorism is reading only.
- **Evidence**: `uic-par-findings.l4:68` (EQUALS `the Insured bears it`). src:134-140, 147-150, 168-171.
- **Plain-English test of surprise**: an insured expects the insurer to prove an exclusion; the insurer's opinion reverses that.

### VN-07 Finding 7 — Innocent misdescription takes property out of cover
- **Class**: T3 / T12
- **Scenario**: GC 2 removes cover for a misdescription of the property, building or business, with no intent and no materiality required. Stock burnt but affected by a misdescription pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork L5: Law:543-553 lets the insurer cancel only for INTENTIONAL incomplete or false information).
- **Evidence**: `uic-par-findings.l4:72` (EQUALS 0). src:281-288.
- **Plain-English test of surprise**: an insured who made an honest slip expects the slip to matter only if it mattered; the wording forfeits cover regardless.

### VN-07 Finding 8 — Any change of trade ends cover, even safer
- **Class**: T2 / T12
- **Scenario**: GC 8(a) ends cover on a change of trade or manufacture without endorsement, and on fork F21 the "increasing the risk" qualifier does not reach this limb. A fireworks warehouse becomes a bottled-water warehouse; a later fire pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F21 reading (i); reading (ii) applies the risk-increase qualifier to both limbs).
- **Evidence**: `uic-par-findings.l4:76` (EQUALS 0). src:365-367.
- **Plain-English test of surprise**: a business that moves to a safer trade expects cover to continue; the wording ends it.

### VN-07 Finding 9 — Four duties with no stated consequence for breach
- **Class**: T5 / T12
- **Scenario**: GC 9 (notice "at once"; written claim in 30 days), GC 5, GC 13 and the deductible undertaking state no consequence of breach; terms are conditions precedent only "so far as their nature permits". A written claim on day 31 leaves the outcome undecidable.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL (fork F4 not answered); LAW L2 suggests late notice carries no reduction.
- **Evidence**: `uic-par-findings.l4:80` (REFUSED, "the wording does not say whether that defeats the claim"). src:3-7, 380-414, 314-327, 485-488, 267-269.
- **Plain-English test of surprise**: a policyholder one day late expects to know whether the claim survives; the document does not say.

### VN-07 Finding 10 — Two vacancy rules that do not line up
- **Class**: T7 / T2
- **Scenario**: A1(c)(vi) excludes escaping water "while" a building is empty, from day one; GC 8(b) ends all cover only after more than 30 days unoccupied. On day 5, burst-pipe damage is excluded but a fire is covered; from day 31, nothing is covered for any cause.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F22: 30 days is not more than 30).
- **Evidence**: `uic-par-findings.l4:85` (water excluded), `:87` (cover not ended at 5 days), `:89` (day 31 pays 0). src:84-85, 369-370.
- **Plain-English test of surprise**: an owner expects one vacancy rule; the water rule bites from the first day.

### VN-07 Finding 11 — Insuring clause names no first day of cover
- **Class**: T5 / T7
- **Scenario**: The insuring clause runs cover from payment of the first premium and names no first day. Premium paid 20 December 2025, Period from 1 January 2026, fire on 25 December 2025: on the clause's own words the loss is covered; on the reading taken, it is not.
- **Who bears it**: insurer. **Money direction**: against the insurer (on the clause's own words).
- **Standing**: CONTESTED (fork F1: reading (ii), the Schedule's period, taken).
- **Evidence**: `uic-par-findings.l4:94` (own words reach the loss), `:95` (cover not running). src:7-11.
- **Plain-English test of surprise**: an insurer expects cover to start on the Schedule date; the clause starts it at payment.

### VN-07 Finding 12 — Deductible taken after the limit, never full limit
- **Class**: T4
- **Scenario**: The deductible applies "after applying all the other terms", so after the cap. Covered loss 3,952m, limit 3,000m, deductible 50m: the insured receives 2,950m and never the full limit however large the loss; the other order gives 3,000m.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F19 reading (i); LAW: Law:588-591 favours reading (ii), deductible before caps).
- **Evidence**: `uic-par-findings.l4:101` (EQUALS 2,950,000,000), `:102` (other order 3,000,000,000). src:22-28, 263-265.
- **Plain-English test of surprise**: an insured with a 3,000m limit and a total loss expects 3,000m; the wording pays 50m less.

### VN-07 Finding 13 — Sum insured, once paid, is gone for the Period
- **Class**: T4 / T6
- **Scenario**: Each cap applies "for each loss and for the whole Period", and nothing restores the sum insured. Stock insured for 2,000m is destroyed in March and paid in full; restocked, it burns in June and nothing is paid, with no premium returned.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F15: "the words say both"; reading (ii), per loss only, recorded).
- **Evidence**: `uic-par-findings.l4:107` (June loss after 2,000m paid EQUALS 0). src:22-23.
- **Plain-English test of surprise**: an insured who restocks expects the new stock covered; the year's cover was used up in March.

### VN-07 Finding 14 — Insured's refund unknowable; insurer cancels at will
- **Class**: T8 / T11
- **Scenario**: An insured who cancels gets a refund at "customary short-period rates", which the document does not state, so the refund cannot be computed. The insurer may cancel on 30 days' notice with no reason.
- **Who bears it**: policyholder. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL; LAW L6 (Law:623-635 lists termination grounds; whether exhaustive is outside knowledge, unverified).
- **Evidence**: `uic-par-findings.l4:111` (REFUSED: rates "not stated in the wording"). src:292-298.
- **Plain-English test of surprise**: a policyholder expects to know the refund before cancelling; the rate table is not in the document.

### VN-07 Finding 15 — One fraudulent claim forfeits every honest claim
- **Class**: T12
- **Scenario**: GC 4(a) forfeits "mọi quyền lợi" (all benefit) under the Policy if "any claim" is fraudulent. An honest June fire claim is followed by a fraudulent claim on another loss; the June fire then pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F30 reading (i), all benefit; reading (ii), only the tainted claim).
- **Evidence**: `uic-par-findings.l4:117` (EQUALS 0). src:302-307.
- **Plain-English test of surprise**: a reasonable reader expects fraud to forfeit the fraudulent claim; the wording also forfeits an earlier honest one.

### VN-07 Finding 16 — Rust-started fire excluded, wear-started fire paid
- **Class**: T7 / T2
- **Scenario**: A1(a) and A1(c) save subsequent loss from a non-excluded cause; A1(b) and A1(d) do not. Corroded wiring starts a fire: excluded, pays 0. A landslip ruptures a gas main and the fire burns stock: excluded. The same fire started by wear and tear is paid.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (on fork F5's chain-of-causation reading, which the A1(a) and A1(c) exceptions presuppose).
- **Evidence**: `uic-par-findings.l4:125` (wear and tear not excluded), `:127`, `:129`, `:130` (EQUALS 0). src:51-53, 55-67, 89-91, 97-107.
- **Plain-English test of surprise**: an insured with fire cover expects a fire paid whatever started it; the trigger decides.

### VN-07 Finding 17 — Weight-bearing terms never defined; nouns drift
- **Class**: T5 / T8
- **Scenario**: "Tài sản được bảo hiểm", "Địa điểm được bảo hiểm" and "Thời hạn bảo hiểm" are capitalised and never defined; GC 1 imports definitions from a Schedule not in the document. Synonyms drift ("Đơn bảo hiểm" for "Hợp đồng bảo hiểm", "căn nhà" beside "tòa nhà", undefined loss terms beside "Tổn thất").
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:8, 10, 48-49, 148, 217, 85, 276-279.
- **Plain-English test of surprise**: a reader expects key terms defined in the document; they depend on a missing Schedule.

### VN-07 Finding 18 — A forecast typhoon is not a covered loss
- **Class**: T6 / T5
- **Scenario**: "Tổn thất" is defined as physical, accidental, sudden and "không lường trước được" (unforeseen). A typhoon forecast days ahead damages a building insured for 9,000m: no exclusion applies, but the loss is not unforeseen, so the storm B1's carve-back names pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F3 reading (i); reading (ii) requires only accidental and sudden).
- **Evidence**: `uic-par-findings.l4:146` (no exclusion), `:147` (EQUALS 0). src:16-19, 206.
- **Plain-English test of surprise**: a building owner expects storm damage covered; a forecast makes it not a "Loss".

### VN-07 Finding 19 — Theft covered only with force at a building
- **Class**: T2 / T6
- **Scenario**: Theft is covered only with forcible entry or exit at a building. Theft from a yard, from a vehicle, by deception or through an unlocked door is excluded, as is disappearance. Stock stolen without force pays 0; with force, 50m after the deductible.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `uic-par-findings.l4:151` (EQUALS 0), `:152` (EQUALS 50,000,000). src:69-70, 74.
- **Plain-English test of surprise**: a buyer of "all risks" expects theft covered; most thefts are excluded.

### VN-07 Finding 20 — No deadline binds the insurer; insurer picks remedy
- **Class**: T1 / T11
- **Scenario**: The document states no period for the insurer to assess, decide or pay, and the insurer alone chooses to pay or reinstate, "not bound to reinstate exactly or completely".
- **Who bears it**: insured. **Money direction**: against the claimant (timing).
- **Standing**: LITERAL, reading only; LAW L4 (Law:718-729, 15 days where none agreed) and L12 (Law:997-1006, money failing agreement) noted.
- **Evidence**: reading only. src:459-460.
- **Plain-English test of surprise**: an insured expects a payment deadline and a say in repair or cash; the wording gives neither.

### VN-07 Finding 21 — Premium paid by a lender does not start cover
- **Class**: T13 (who must pay the premium) / T5
- **Scenario**: Cover starts on premium "đã được Người được bảo hiểm thanh toán" (paid by the Insured). On the words, a premium paid by a parent company or a lender does not start the cover.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:7-8.
- **Plain-English test of surprise**: an insured whose lender paid the premium expects to be covered; the words require the insured to pay.

#### VN-07 row summary
- Findings in section 4: 21 (numbered 1 to 21); 21 records above.
- Three most counterintuitive: Finding 3 (suing inside the three months GC 4(b) gives is still too late); Finding 18 (a forecast typhoon is not a "Loss"); Finding 1 (riot saved and excluded, so riot damage is never paid).
- Matches in this group: F1 = VN-20 X3 (riot given back then excluded). F2 ~ VN-08 F1, VN-21 F18, VN-22 X12 (other insurance clauses conflict or have no basis). F5 = VN-08 F23 (unlimited insurer powers over property; forfeiture on any requirement). F6 ~ VN-09 X10 (insurer's say-so shifts burden). F7 = VN-08 F17, VN-20 X15 (innocent misdescription, Law art 22(2)). F8 ~ VN-08 F6 (change of business ends cover). F10 = VN-05 X-vacancy, VN-08 F6, VN-20 X8. F12 ~ VN-20 X5 (order of operations). F13 = VN-08 F18 (sum insured eroded, never reinstated). F14 = VN-09 X18 (short-period rates missing) and VN-05 X-cancel. F15 = VN-08 F21, VN-21 F16 (one fraud forfeits all). F17 = VN-05 X-undefined. F18 ~ VN-08 F19 ("all risks" fails on foreseen or unknown cause). F19 ~ VN-05 X-fence. F20 = VN-05 X-payment-time.

---

## VN-08 Bảo Minh property all risks

Directory: `vn-baominh-property-all-risks/encodings/legalese-2026-10-vn-08`.
Findings module: `baominh-par-findings.l4`. Findings numbered 1 to 23; "fork F-n" is the section 3 fork register.

### VN-08 Finding 1 — Other-insurance exclusion makes contribution clause dead text
- **Class**: T7 / T6
- **Scenario**: Exclusion 8(i) excludes property "đã được thu xếp bảo hiểm theo cách khác" (otherwise insured); GC 6 pays a rateable share of a loss other insurance also covers. Stock worth 500,000,000, insured here and elsewhere for 500,000,000, suffers 100,000,000 of fire damage: GC 6 would pay 50,000,000; the claim pays nothing under exclusion 8.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("whichever governs, the other is dead text").
- **Evidence**: `baominh-par-findings.l4:38` (GC 6 EQUALS 50,000,000), `:40` (nothing payable, "exclusion 8"). src:168, 298-306.
- **Plain-English test of surprise**: a business with two policies expects each to pay its share; this one pays nothing.

### VN-08 Finding 2 — One late notice or missed precaution voids claim
- **Class**: T12 / T3
- **Scenario**: Every condition is a condition precedent; GC 9(a) wants notice "ngay lập tức" (immediately), unquantified, and GC 12 "mọi biện pháp" (every measure) against loss. A covered 100,000,000 fire pays 90,000,000; with notice judged not immediate, or one unrelated precaution missed, nothing.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW for the late-notice limb (fork F28: art 46, art 19(3)); LITERAL for the precaution limb.
- **Evidence**: `baominh-par-findings.l4:52` (90,000,000), `:54` (GC 9(a) reasons), `:56` (GC 12). src:9-11, 337-340, 401-402.
- **Plain-English test of surprise**: an insured expects a missed precaution unrelated to the fire to cost nothing; it costs the whole claim.

### VN-08 Finding 3 — Second arbitrator appointable on one day only
- **Class**: T7 / T1
- **Scenario**: GC 7: appoint "sau 2 tháng" (after two months) from the request, or lose the choice if not done "trong vòng 2 tháng" (within two months). Month 1 is a nullity, month 2 complies, month 3 lets the other side appoint a sole arbitrator; read strictly, no day complies. Disagreeing with an award also reopens it (reading only).
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: CONTESTED (fork F21: inclusive reading taken; strict and slip readings listed).
- **Evidence**: three `#TRACE` directives, `baominh-par-tests-conditions.l4:92-98`. src:310-314.
- **Plain-English test of surprise**: a party expects a window of weeks to appoint; the wording gives one day or none.

### VN-08 Finding 4 — Premium warranty circular for policies under 30 days
- **Class**: T5 / T7
- **Scenario**: GC 15 1(a) covers a period of insurance of 30 days or more; 1(c) speaks of "thời hạn thanh toán phí bảo hiểm dưới 30 ngày" (a premium payment period under 30 days), the very period the clause defines. For a 20-day policy, the wording as written gives no rule.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F26 reads 1(c) as a slip for the period of insurance).
- **Evidence**: reading only; fork F26's result is tested at `baominh-par-tests-conditions.l4:228-231`. src:423, 443-444.
- **Plain-English test of surprise**: a short-policy buyer expects to know when premium is due; the clause defines the term by itself.

### VN-08 Finding 5 — Mitigation required at once; nobody pays for it
- **Class**: T13 (cost of a required duty unallocated) / T5
- **Scenario**: GC 9(a)(i) requires "all necessary measures to minimise the loss" immediately. Other clauses say who pays for subrogation, documents and plans, but the mitigation clause is silent, and the insuring clause pays only the value of Damage.
- **Who bears it**: insured. **Money direction**: against the claimant (inferred).
- **Standing**: LITERAL, reading only; LAW art 51(3) makes the insurer pay reasonable mitigation costs "as the contract agrees", and none is recorded.
- **Evidence**: reading only. src:338, 292, 349, 390-391.
- **Plain-English test of surprise**: an insured ordered to limit the damage expects the cost reimbursed; the wording does not say.

### VN-08 Finding 6 — Cover ends with no link to the loss
- **Class**: T2 / T7
- **Scenario**: GC 8 ends cover if the building is unattended 30 days or more, the business changes, or the interest passes, unless endorsed first, with no causal connection to the loss. A building unattended 30 days is damaged by earthquake: nothing paid; at 29 days cover stands. GC 8(b)'s "unattended" also differs from exclusion 1(c)(vi)'s "empty or not in use".
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (the test mismatch is reading only).
- **Evidence**: `baominh-par-findings.l4:77` (nothing payable, GC 8); `baominh-par-tests-conditions.l4:123` (29 days). src:320-333, 57-58.
- **Plain-English test of surprise**: an owner expects an earthquake covered regardless of a guard; absence of a guard voids cover.

### VN-08 Finding 7 — Pollution exclusion garbled; excluded and saved unclear
- **Class**: T5 / T13 (garbled sentence)
- **Scenario**: The pollution clause is the standard clause with its words out of order ("ô nhiễm hoặc nhiễm bẩn loại trừ ..."); read as it stands it does not say what is excluded and what is written back. One literal reading would exclude Damage by an insured peril.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F8: the standard clause taken; reading (ii) treats the write-backs as further exclusions).
- **Evidence**: reading only. src:120-123.
- **Plain-English test of surprise**: a reader expects a pollution exclusion to say what it excludes; this one cannot be parsed.

### VN-08 Finding 8 — Short-period refund rows overlap at 3 and 6 months
- **Class**: T4 / T5
- **Scenario**: The short-period scale prints "Đến 3 tháng" (up to 3 months) and "Từ 3 đến 6 tháng" (from 3 to 6 months), and likewise at 6. A cover ended at exactly 3 months is charged either 30% or 60%.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F20 takes the first row, the lower charge, which LAW art 24 also favours).
- **Evidence**: `baominh-par-findings.l4:90-91` (each row's upper edge equals the next row's lower edge). src:277-281.
- **Plain-English test of surprise**: a policyholder cancelling at 3 months expects one price; the scale gives two.

### VN-08 Finding 9 — Two write-back peril lists that do not match
- **Class**: T7
- **Scenario**: Exclusion 6's and exclusion 11's lists of written-back perils render overlapping perils in different words and each lacks perils the other has; exclusion 10's has fire and explosion alone. A computer damaged by riot or by hail is excluded by exclusion 6; the same computer damaged in a demonstration is not.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `baominh-par-findings.l4:98-99` (riot, hail: excluded by exclusion 6), `:101` (demonstration: no exclusion). src:135-139, 233-237.
- **Plain-English test of surprise**: an insured expects riot and demonstration treated alike; one is covered and one is not.

### VN-08 Finding 10 — Defective numbering makes citations ambiguous
- **Class**: T5 / T13 (defective numbering)
- **Scenario**: Two exclusions are numbered "10."; exclusion 3 has "d)" without its parenthesis; exclusion 11 has both "Phần 1-3" and letters; GC 15 restarts at "1."; 1(c)'s write-back limbs reuse "(i)" and "(ii)", so "trừ khi (i)" can be read as a reference to theft.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:173, 177, 90, 216, 238, 245, 418, 60, 62.
- **Plain-English test of surprise**: a reader expects "exclusion 10" to name one clause; it names two.

### VN-08 Finding 11 — Date-change exclusion can remove any computer replacement
- **Class**: T2 / T6
- **Scenario**: Exclusion 11 Part 2, "notwithstanding Part 1", excludes costs "relating to changing or supplementing any computer system", with no link to a date change. Read literally, replacing office computers destroyed by fire is excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F12: the encoding takes the narrow reading, since (ii) would empty Part 1's write-back).
- **Evidence**: reading only. src:239-244.
- **Plain-English test of surprise**: an insured expects burnt computers replaced; a millennium-bug clause can be read to exclude it.

### VN-08 Finding 12 — Key terms undefined or used inconsistently
- **Class**: T5
- **Scenario**: "sự kiện" (event) in exclusion 11 Part 3 has no other use, so Part 3 switches off nothing; "tổn thất" (loss), the deductible's unit, is undefined, so grouping of damage into one loss is unstated; "Tổn hại" alternates with other words; the Schedule, the insurer and the document itself each go by several names.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:247, 405, 167, 413, 361, 420, 453, 257-259.
- **Plain-English test of surprise**: a reader expects the deductible's unit defined; how many deductibles apply cannot be read off.

### VN-08 Finding 13 — Data exclusion lost its causal link in translation
- **Class**: T2 / T13 (translation)
- **Scenario**: Exclusion 10(a)(i) excludes data loss "or loss of use, reduction in functionality, costs of any kind" with nothing tying those to the data; the standard clause's "resulting therefrom" is missing. Read literally, any loss of use or cost, whatever its cause, is excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (the encoding ties them to a data matter in the chain).
- **Evidence**: reading only. src:183-184.
- **Plain-English test of surprise**: an insured expects a data exclusion to cover data problems; the literal words exclude all loss of use.

### VN-08 Finding 14 — Insured money not covered against burglary
- **Class**: T6 / T7
- **Scenario**: Exclusion 6(a) covers money and valuables confirmed as insured only for listed perils, and theft is not one, though exclusion 1(c)(i) allows burglary with force from the insured building. A safe broken open inside the insured building is excluded by exclusion 6.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `baominh-par-findings.l4:110` (`excluded by` "exclusion 6"). src:127-130, 48-49.
- **Plain-English test of surprise**: a business that insured its cash expects a safe-cracking covered; it is not.

### VN-08 Finding 15 — Same fire covered after defect, excluded after breakdown
- **Class**: T7 / T2
- **Scenario**: Exclusion 1(a) writes back the part from a non-excluded cause; 1(c) also requires "và" (and) that the excluded loss itself resulted from such a cause. A machine damaged by a latent defect and fire has the fire part covered; damaged by breakdown and fire, it is wholly excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F5 reads "và" as both limbs required; LAW art 24 would favour reading (ii), either).
- **Evidence**: `baominh-par-findings.l4:116` (apportioned under 1(a)), `:117` (excluded by 1(c)). src:34-36, 59-63.
- **Plain-English test of surprise**: an insured expects fire damage paid whatever else went wrong; the companion cause decides.

### VN-08 Finding 16 — Tanks and pipes are themselves excluded property
- **Class**: T5 / T7
- **Scenario**: Exclusion 8(d) excludes Damage to "bể chứa" and "đường ống" (reservoirs, pipelines), the same words as the tanks and pipes whose bursting exclusion 6 writes back. A factory pipe or water tank damaged by fire is excluded by exclusion 8.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (encoder: "translation-dependent").
- **Evidence**: `baominh-par-findings.l4:124-125` (pipelines, reservoirs excluded by exclusion 8). src:156-159, 138-139, 57.
- **Plain-English test of surprise**: a factory owner expects ordinary tanks and pipes covered against fire; the words exclude them.

### VN-08 Finding 17 — Innocent unconnected omission takes property out of cover
- **Class**: T3 / T12
- **Scenario**: GC 2 removes cover for property "bị ảnh hưởng bởi" (affected by) a false statement or omission of a fact the risk was assessed on, with no intent and no link to the cause. A fact about the building was omitted; lightning strikes it; nothing is payable.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F18: art 22(2) gives avoidance only for intentional withholding or falsification).
- **Evidence**: `baominh-par-findings.l4:142` (nothing payable, GC 2). src:262-268.
- **Plain-English test of surprise**: an insured who forgot a detail expects lightning damage paid; the omission voids it.

### VN-08 Finding 18 — Average uses full sum insured after erosion
- **Class**: T4
- **Scenario**: The aggregate cap is eroded by earlier payments with no reinstatement, yet GC 14's average still compares value with the full sum insured. A building insured for 1,000,000,000 has had 900,000,000 paid; a second fire of 500,000,000 hits it, now worth 1,200,000,000. Average gives over 416,666,666; 100,000,000 is paid.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (encoder: penalised "for under-insurance on cover it no longer has").
- **Evidence**: `baominh-par-findings.l4:160` (GREATER THAN 416,666,666), `:161` (EQUALS 100,000,000). src:20-23, 412-416.
- **Plain-English test of surprise**: an insured expects a used-up limit and an average penalty not to stack; the wording runs both.

### VN-08 Finding 19 — All-risks policy excludes damage of unknown cause
- **Class**: T6 / T2
- **Scenario**: Exclusion 1(c)(iii) lists "không rõ nguyên nhân" (unknown cause), and the write-back needs a cause not excluded, which an unknown cause cannot supply. Stock found damaged with cause unknown is excluded; the insured must prove the cause to recover under "all risks".
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `baominh-par-findings.l4:167` (`excluded by` "exclusion 1(c)"). src:51.
- **Plain-English test of surprise**: a buyer of "all risks" expects unexplained damage covered; it is excluded.

### VN-08 Finding 20 — Insurer may cancel at will on seven days
- **Class**: T3 / T11
- **Scenario**: GC 3 lets the insurer cancel at any time on 7 days' notice by registered letter.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (art 26 lists the grounds for unilateral termination and this is not one; art 20(1)(c) limits insurer termination to art 26).
- **Evidence**: reading only. src:270-272.
- **Plain-English test of surprise**: a policyholder expects a year's cover; the insurer can end it in a week.

### VN-08 Finding 21 — One fraudulent claim forfeits every policy benefit
- **Class**: T12
- **Scenario**: GC 4(a): "Tất cả quyền lợi bảo hiểm theo hợp đồng bảo hiểm này sẽ bị bãi bỏ" (all benefits under the policy are forfeited), not only the fraudulent claim.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only (the encoding models one loss at a time).
- **Evidence**: reading only. src:283-286.
- **Plain-English test of surprise**: a reader expects fraud to cost the fraudulent claim; it costs all of them.

### VN-08 Finding 22 — Short insured deadlines; insurer has no deadline
- **Class**: T1 / T3
- **Scenario**: GC 9(b) gives 30 days to file a claim and GC 4(b) three months to sue after rejection; the insurer has no deadline to decide or pay.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (art 30 gives one year to file; art 31 gives 15 days to pay; neither applied; forks F24, F34).
- **Evidence**: reading only. src:343, 287-288.
- **Plain-English test of surprise**: an insured expects deadlines on both sides; only the insured's exist, and they are shorter than the statute's.

### VN-08 Finding 23 — Insurer powers over property with no standard
- **Class**: T11 / T12
- **Scenario**: GC 10 lets the insurer take possession of, sell or dispose of the property "without incurring liability", and forfeits every benefit if the insured does not comply with "các yêu cầu của Bảo Minh" (the insurer's requirements), with no reasonableness test, while the insured may not abandon the property.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only (the forfeiture is asserted in the conditions tests).
- **Evidence**: `baominh-par-tests-conditions.l4` §§ General Conditions 5, 10, 11, 12, 13 (from line 180). src:361-381.
- **Plain-English test of surprise**: an insured expects insurer demands to be reasonable; any unmet demand forfeits everything.

#### VN-08 row summary
- Findings in section 4: 23 (numbered 1 to 23); 23 records above.
- Three most counterintuitive: Finding 19 (an "all risks" policy excludes damage of unknown cause); Finding 1 (insurance elsewhere excludes the property entirely, so the contribution clause never runs); Finding 2 (one unrelated missed precaution forfeits a 90,000,000 fire claim).
- Matches in this group: F1 ~ VN-07 F2. F2 = VN-05 X-precedent, VN-20 X14, VN-21 F3, VN-22 X5. F3 ~ VN-07 F4, VN-21 F7, VN-22 X8 (arbitrator appointment broken). F4 = VN-20 X17: the same words "thời hạn thanh toán phí bảo hiểm dưới 30 ngày" in both Bảo Minh forms, which the VN-08 encoder read as a slip (fork F26) and the VN-20 encoder read literally (fork F34). F6 = VN-07 F8, F10; VN-05 X-vacancy; VN-20 X8. F8 = VN-20 X12 (short-period rows overlap at 3 and 6 months). F9 ~ VN-07 F1, VN-20 X3 (riot/demonstration lists differ). F11, F13 ~ VN-20 X11 (date-change and data exclusions). F12 = VN-07 F17. F17 = VN-07 F7, VN-20 X15. F18 = VN-07 F13. F20 = VN-05 X-cancel, VN-20 X16. F21 = VN-07 F15, VN-21 F16. F22 = VN-20 X19. F23 = VN-07 F5.

---

## VN-09 MSIG commercial general liability (English source)

Directory: `vn-msig-general-liability-2015/encodings/legalese-2026-10-vn-09`.
Findings module: `msig-cgl-tests-findings.l4`. Findings X1 to X23. The source is English only, so T9 does not arise.

### VN-09 X1 — Claims-made plus occurrence trigger leaves a gap between policies
- **Class**: T6 / T1
- **Scenario**: The P&CO part requires both injury and claim inside the period. An injury on 31 December 2026, claimed 1 January 2027, fails under this policy (claim late) and the 2027 renewal (injury early). An injury in November 2025, claimed February 2026, also fails: the 2020 Retroactive Date never operates.
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F20 takes the literal reading; a true claims-made reading is listed, with LAW art 24).
- **Evidence**: `msig-cgl-tests-findings.l4:38-42` (`not covered`). src:59-60, 164-166, 731-736.
- **Plain-English test of surprise**: a renewing buyer expects no gap; a year-end injury falls between two policies.

### VN-09 X2 — "Anywhere in the world" products cover cut to Vietnam
- **Class**: T2 / T6
- **Scenario**: Products sold for use in Vietnam are covered for harm anywhere, but a proviso requires suit under the Jurisdiction clause, which removes foreign judgements. A buyer injured abroad who sues there is not covered, though the place is within limb (3); so too an injury in Vietnam sued on abroad.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F2 reading (i): the proviso governs all limbs; (ii) limb (3) only).
- **Evidence**: `msig-cgl-tests-findings.l4:51` (not covered), `:52` (place inside the territory). src:153-157, 46-49.
- **Plain-English test of surprise**: a buyer told "anywhere in the world" expects a foreign suit covered; it is not.

### VN-09 X3 — CGL products aggregates apply to nothing
- **Class**: T6 / T7
- **Scenario**: Section III gives the CGL part aggregates for products and completed operations, but a Special Condition removes both hazards from the CGL part. A products claim falls under the aggregate test and is not covered.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL.
- **Evidence**: `msig-cgl-tests-findings.l4:56` (aggregate test TRUE), `:57` (not covered, products hazard exclusion). src:512-514, 535-536, 710-713.
- **Plain-English test of surprise**: a buyer reading a products aggregate expects products cover under that part; there is none.

### VN-09 X4 — Two foreign-currency caps that disagree, no conversion rule
- **Class**: T7 / T4
- **Scenario**: Supplementary Payments cap bail bonds at US$250 and daily earnings at US$25; the Ultimate Net Loss Clause says S$250.00 and S$25.00. No rate, date or source converts either to dong. At hypothetical rates the same sums give 90,550,000 under one clause, 89,100,000 under the other.
- **Who bears it**: insured. **Money direction**: unclear (the reading taken gives the smaller figure).
- **Standing**: CONTESTED (fork F4 takes the Ultimate Net Loss Clause; LAW art 24 would favour the larger cap).
- **Evidence**: `msig-cgl-tests-findings.l4:63` (90,550,000), `:64` (89,100,000). src:28, 34, 942, 949.
- **Plain-English test of surprise**: an insured expects one cap in the policy currency; the policy states two in other currencies.

### VN-09 X5 — No rule for which limit absorbs defence costs
- **Class**: T5 / T4
- **Scenario**: Defence and other supplementary sums are "inclusive in the applicable limit", but with separate bodily injury and property damage limits, one occurrence causing both (1,000,000,000 and 500,000,000 of damages) has two applicable limits, and nothing says which absorbs the sums. The encoding refuses.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F11: declined by name).
- **Evidence**: `msig-cgl-tests-findings.l4:68` (REFUSED). src:18, 504-540, 923-924.
- **Plain-English test of surprise**: an insured expects defence costs to be charged to a known limit; the wording does not say which.

### VN-09 X6 — Knowledge proviso lets a foreseeable claim through
- **Class**: T5
- **Scenario**: The claims-made proviso holds if at inception an insured "did not know or could not reasonably have foreseen". Joined by "or", it fails only if an insured both knew and could have foreseen. A claim no insured knew of but which was foreseeable passes as written and fails on the "neither knew nor could have foreseen" reading.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F22 takes the words; the "neither ... nor" reading is encoded beside it).
- **Evidence**: `msig-cgl-tests-findings.l4:75` (holds), `:76` (NOT on the other reading). src:734-736.
- **Plain-English test of surprise**: an insurer expects foreseeable prior problems excluded; "or" lets them in.

### VN-09 X7 — Notice of circumstances saves products, not completed operations
- **Class**: T7 / T6
- **Scenario**: Claims Made clause 4 deems a later claim made in the period if circumstances were notified, but only circumstances "by reason of the named insured's products", although the part covers both hazards. Same facts, injury November 2026, notice 5 November, claim February 2027: products covered; completed operations not.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F25: every word of the clause).
- **Evidence**: `msig-cgl-tests-findings.l4:95` (covered), `:96` (not covered). src:746-750.
- **Plain-English test of surprise**: an insured who gave notice expects either hazard saved; only one is.

### VN-09 X8 — Any departure from any term bars the action
- **Class**: T12 / T3
- **Scenario**: Condition 4 makes "full compliance with all of the terms" a condition precedent to any action, so late notice bars it entirely, however little it cost the insurer; and a default or consent judgement is not "after actual trial". A judgement after trial, with late notice: no action.
- **Who bears it**: insured / third party. **Money direction**: against the claimant.
- **Standing**: LAW (fork F14: art 46 and art 19(3) point the other way; conflict left open).
- **Evidence**: `msig-cgl-tests-findings.l4:101` (NOT an action lies). src:231-234, 209-227.
- **Plain-English test of surprise**: an insured expects slightly late notice to cost only what it harmed; it costs everything.

### VN-09 X9 — Clause names coverages "Y" and "Z" that do not exist
- **Class**: T5 / T8
- **Scenario**: The Ultimate Net Loss Clause names coverages "Y" and "Z", which no part of the document defines. No rule can reach them.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL, reading only ("inert").
- **Evidence**: reading only. src:923.
- **Plain-English test of surprise**: a reader expects named coverages to exist; template placeholders were left in.

### VN-09 X10 — War exclusion applies on the insurer's allegation alone
- **Class**: T11
- **Scenario**: Once the insurer alleges the War and Terrorism Exclusion, the loss is excluded unless the insured proves otherwise, and the allegation needs no stated ground. A bodily injury claim with no war or terrorism found at all is excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F26 reading (i), "as written").
- **Evidence**: `msig-cgl-tests-findings.l4:107` (not covered, WAR AND TERRORISM EXCLUSION). src:976-977.
- **Plain-English test of surprise**: an insured expects the insurer to show war was involved; an allegation suffices.

### VN-09 X11 — Cyber exclusion reaches any business done by email
- **Class**: T2 / T6
- **Scenario**: The Cyber Liability Exclusion removes "any claim or loss arising out of any activities and/or business conducted ... via" email or online. On a literal reading, a product ordered by email that injures its buyer is excluded under both parts.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("on a literal reading"; illusory "for most businesses ... to that extent").
- **Evidence**: `msig-cgl-tests-findings.l4:112` (P&CO not covered), `:113` (CGL not covered). src:819-821.
- **Plain-English test of surprise**: a business expects a cyber exclusion to cover hacking; it removes products sold by email.

### VN-09 X12 — Three different notice standards for one event
- **Class**: T5 / T7
- **Scenario**: Condition 3(a) asks for notice "as soon as practicable", 3(b) "immediately", and the Claims Made endorsement "immediate notice ... in accordance with the Conditions", which the Conditions do not define.
- **Who bears it**: insured. **Money direction**: unclear.
- **Standing**: LITERAL, reading only (fork F12 takes each as a finding of fact).
- **Evidence**: reading only. src:212, 214, 734.
- **Plain-English test of surprise**: an insured expects one notice deadline; there are three standards.

### VN-09 X13 — Insurer cancels for any reason; notice need not arrive
- **Class**: T3 / T11
- **Scenario**: The insurer may cancel for any reason on ten days' notice, and mailing is "sufficient proof of notice", so the ten days run from posting whether or not the notice arrives.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (fork F35: art 26 lists termination grounds; not resolved, exhaustiveness outside knowledge, unverified).
- **Evidence**: grounds reading only; ten days tested in `msig-cgl-tests-amounts.l4:258` (A14). src:290-295.
- **Plain-English test of surprise**: a policyholder expects to learn of cancellation before it bites; posting is enough.

### VN-09 X14 — Defence costs eat the limit, leaving damages unpaid
- **Class**: T4
- **Scenario**: Defence and supplementary sums come out of the limit. Damages of 4,950,000,000 plus other sums of 89,100,000 against a 5,000,000,000 limit: the insurer pays 5,000,000,000 and 39,100,000 of the damages fall on the insured, because defence was paid from the same limit.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `msig-cgl-tests-findings.l4:120` (EQUALS 5,000,000,000). src:18, 923-924.
- **Plain-English test of surprise**: an insured with a 5,000,000,000 limit and lower damages expects them paid in full; defence costs consume the margin.

### VN-09 X15 — Named insured's employees are not insureds
- **Class**: T13 (persons insured omit employees) / T6
- **Scenario**: Only CGL paragraph (e), operators of registered mobile equipment on a highway, reaches an employee; the P&CO part has no (e). An employee sued personally for injuring a visitor at work, on foot, is not covered under either part.
- **Who bears it**: insured (employee). **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `msig-cgl-tests-findings.l4:126` (not covered, PERSONS INSURED). src:462-499, 643-657.
- **Plain-English test of surprise**: an employer expects staff sued for workplace accidents covered; they are not insureds.

### VN-09 X16 — Combined single limit leaves CGL without an aggregate
- **Class**: T4 / T7
- **Scenario**: Under the combined single limit endorsement the aggregate reaches only products and completed operations, which the CGL part excludes. With the whole 10,000,000,000 aggregate already paid, a premises occurrence is still paid in full (1,089,100,000): every premises occurrence gets a fresh 5,000,000,000.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL ("a finding for the insurer").
- **Evidence**: `msig-cgl-tests-findings.l4:133` (EQUALS 1,089,100,000). src:808-810, 710-713.
- **Plain-English test of surprise**: an insurer expects an annual aggregate to cap total exposure; for premises claims there is none.

### VN-09 X17 — Defined term used in a form it does not define
- **Class**: T5
- **Scenario**: "named insured products" is defined, but "named insured's products" is used in the definition itself and everywhere else.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only (fork F3 treats them as one term).
- **Evidence**: reading only. src:135-137.
- **Plain-English test of surprise**: a reader expects the defined term to be the one used; a different form is used throughout.

### VN-09 X18 — Premium and own-cancellation refund cannot be computed
- **Class**: T8
- **Scenario**: The named insured's refund on cancelling, and the premium itself, depend on a "customary short rate table and procedure" and rules not in the document. A premium of 100,000,000 for 2026, cancelled on 1 July, gives no computable earned premium.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `msig-cgl-tests-findings.l4:137` (REFUSED); `msig-cgl-tests-amounts.l4:169` (A8). src:182-183, 297.
- **Plain-English test of surprise**: a policyholder expects to know the refund; the table is missing.

### VN-09 X19 — Aggregate limit's period never stated
- **Class**: T5 / T8
- **Scenario**: "aggregate" is never tied to the policy period or to a year; the encoding takes the caller's figure for what has already been paid out of it.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:514, 522, 675, 683, 809.
- **Plain-English test of surprise**: a buyer expects an annual aggregate; the period it covers is not stated.

### VN-09 X20 — Recall at own cost on expectation, or lose cover
- **Class**: T11 / T12
- **Scenario**: The Sistership clause obliges a recall where harm "is expected to occur", refuses the recall cost, and excludes later harm unless the failure to recall had a "justifiable reason", which is undefined.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL; the mechanism is tested, the missing criteria are reading only.
- **Evidence**: `msig-cgl-tests-cover.l4:450` (C10, Sistership). src:904-916.
- **Plain-English test of surprise**: an insured expects recall to be required only on known defects, with criteria; an expectation triggers it.

### VN-09 X21 — No deadlines; statute's year may run out before trial
- **Class**: T1 / T3
- **Scenario**: The policy states no deadline for claim documents, the insurer's assessment or payment, or suit. The Law's one year to submit runs from the third party's demand, while Condition 4 withholds any action until liability is fixed after actual trial. An insured who waits for trial before filing may be out of time under the Law.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F36: art 30, art 31; recorded, not encoded). Reading only.
- **Evidence**: reading only. src:207-241.
- **Plain-English test of surprise**: an insured who follows the policy's own sequence expects to stay in time; the statute's clock may expire first.

### VN-09 X22 — CGL war exclusion (g) does no work
- **Class**: T7 / T13 (surplus clause)
- **Scenario**: The War and Terrorism Exclusion removes all war loss in every part, so CGL exclusion (g)'s limit to incidental contracts and first aid does nothing.
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:378-383, 952-977.
- **Plain-English test of surprise**: a reader expects each exclusion to matter; this one is overridden.

### VN-09 X23 — Insurer settles as it deems expedient; insured bears excess
- **Class**: T11
- **Scenario**: The insurer may investigate and settle "as it deems expedient", with no criteria, while the excess over the limit stays with the insured. Read with X14, the insurer controls a settlement paid from a limit that also pays its own defence costs.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:334, 572-573.
- **Plain-English test of surprise**: an insured expects settlement control to come with responsibility for the result; the excess stays with the insured.

#### VN-09 row summary
- Findings in section 4: 23 (X1 to X23); 23 records above.
- Three most counterintuitive: X1 (a year-end product injury falls between two consecutive policies, and the Retroactive Date never operates); X11 (the cyber exclusion removes products ordered by email); X14 (defence costs paid from the limit leave part of the damages with the insured).
- Matches in this group: X8 = VN-05 X-precedent, VN-21 F3 (any breach bars recovery). X10 ~ VN-07 F6 (insurer's allegation shifts burden). X13 = VN-05 X-cancel, VN-08 F20, VN-20 X16. X18 = VN-07 F14 (short-period table missing). X21 = VN-05 X-payment-time, VN-08 F22. X23 ~ VN-21 F17, VN-22 X19 (insurer controls settlement, insured bears the rest). X12 ~ VN-22 X5 (several notice standards for one event). X5 ~ VN-21 F18, VN-22 X12 (an allocation with no stated basis). X1, X2, X11 have no match in this group (the other rows are not claims-made or products forms).

---

## VN-20 Bảo Minh fire and special perils

Directory: `vn-baominh-fire-special-perils/encodings/legalese-2026-10-vn-20`.
Findings module: `bmfire-findings.l4`. Findings X1 to X19 (a table in section 4).

### VN-20 X1 — Insured's own vehicles covered for impact damage
- **Class**: T13 (cover wider than the market wording) / T5
- **Scenario**: Risk J's only sentence about the insured's own vehicles and animals is a deductible sentence; the usual market exclusion of own vehicles is absent. The insured's own lorry reverses into its warehouse: 200,000,000 damage, deductible 10,000,000, and 190,000,000 is payable.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F8 reading (i), a deductible sentence; reading (ii), the market exclusion).
- **Evidence**: `bmfire-findings.l4:27` (reasons EMPTY), `:28` (EQUALS 190,000,000). src:150-155.
- **Plain-English test of surprise**: an insurer expects its own-vehicle exclusion to be there; the text only sets a deductible.

### VN-20 X2 — Lone or state terrorism not excluded from explosion or riot
- **Class**: T5 / T7
- **Scenario**: Terrorism is defined to cover a person acting alone or for a government, but exclusions in B and D add "nhân danh hoặc có liên quan đến bất kỳ tổ chức nào" (on behalf of or connected with any organisation). A lone bomber with a political aim destroys the building: it is Terrorism, yet B and D claims have no exclusion.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL.
- **Evidence**: `bmfire-findings.l4:33` (Terrorism holds), `:34-35` (B, D reasons EMPTY). src:24-27, 53-54, 69-70.
- **Plain-English test of surprise**: an insurer expects terrorism excluded whoever commits it; the exclusion needs an organisation.

### VN-20 X3 — Riot cover given back, then excluded outright
- **Class**: T6 / T7
- **Scenario**: III.1(a)(i) gives "Nổi loạn" (riot) back where risk D is insured; III.1(a)(iii) excludes "Nổi loạn" and "bạo động" with no carve-back, and D uses different words. A riot damages an insured shop: called "civil commotion", paid; called "Nổi loạn", excluded.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED ("illusory on a literal reading"; fork F36 leaves the choice of word to the adjuster).
- **Evidence**: `bmfire-findings.l4:43` (commotion: EMPTY), `:44`, `:45` (riot: III.1(a)(iii)). src:57, 160-166.
- **Plain-English test of surprise**: a shop owner who bought riot cover expects a riot paid; the label decides.

### VN-20 X4 — Thirty-day claim period, far shorter than statute
- **Class**: T1 / T3
- **Scenario**: VII.1(b) requires particulars within 30 days, and the preamble makes conditions precedent, so a late particular takes away the whole claim. Fire damage of 200,000,000 on 1 June 2026: a written claim on 1 July is in time, on 2 July (day 31) the claim fails; the Law gives one year.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (art 30(1), aid 707-710; fork F37, not encoded).
- **Evidence**: `bmfire-tests-conditions.l4:75` (1 July: EMPTY), `:76` (2 July: VII.1(b)). src:275-280, 6-8.
- **Plain-English test of surprise**: an insured expects a late form to delay payment; it forfeits the claim.

### VN-20 X5 — Average and contribution cut an over-insured claim twice
- **Class**: T4
- **Scenario**: Average is measured against this policy's sum insured alone, then contribution takes a rateable share again. A building worth 1,000 is insured for 600 here and 600 elsewhere (1,200 in all); damage 200. Average gives 120, contribution halves it to 60; each insurer pays 60, so 120 of a 200 loss though over-insured.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F18: a loss adjuster's order of steps, others possible).
- **Evidence**: `bmfire-findings.l4:57` (EQUALS 60,000,000). src:330-334, 339-347.
- **Plain-English test of surprise**: an owner insured for more than the value expects full recovery; 40% goes unpaid.

### VN-20 X6 — Warranty breach bites only in a renewal period
- **Class**: T7 / T5
- **Scenario**: VI.5 takes away a claim for warranty breach "nếu có TỔN HẠI xảy ra trong thời gian tái tục hợp đồng" (if damage occurs in a renewal period). First-year policy, sprinkler warranty broken, deductible insured, fire: 200,000,000 is payable.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F25 reading (i), as written; reading (ii), a slip for any period).
- **Evidence**: `bmfire-findings.l4:67` (breach recorded), `:68` (EQUALS 200,000,000). src:255-261, 203-204.
- **Plain-English test of surprise**: an insurer expects warranties to bind from day one; the text binds only renewals.

### VN-20 X7 — Twelve months to sue run during arbitration formation
- **Class**: T1 / T7
- **Scenario**: Rejection and request to arbitrate on 15 March 2026; two two-month appointment periods, no period for the umpire or the award. No suit by 16 March 2027: the benefit is lost, whether or not an award has come.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL ("either bar suffices").
- **Evidence**: `bmfire-findings.l4:76` (first period ends 2026-07-15), `:77` (benefit lost). src:294-300, 357-367.
- **Plain-English test of surprise**: an insured in arbitration expects the suit clock paused; it runs out regardless.

### VN-20 X8 — Empty-building water damage excluded from day one
- **Class**: T7
- **Scenario**: Risk I(ii) excludes water damage to a building left empty, with no period; VI.3 ends cover only after 30 days empty. Building empty since 31 May, pipe bursts 1 June: the policy has not ceased, but I(ii) excludes the loss.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F7: any time empty).
- **Evidence**: `bmfire-findings.l4:89` (VI.3 not triggered), `:90` (reasons EQUALS II.I(ii)). src:142, 233.
- **Plain-English test of surprise**: an owner told cover lapses after 30 days empty expects day one covered; water damage is not.

### VN-20 X9 — Three answers to whether premium must come first
- **Class**: T7 / T5
- **Scenario**: The preamble covers only "sau khi đã đóng phí" (after the premium is paid); VIII.3.1 alone denies liability unless paid in 30 days; VIII.3.2 keeps the insurer liable for the period in force. Fire 15 January, premium paid 20 January or never: the preamble says no, clause 1 says no, the encoded answer pays 200,000,000.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F27 reading (iii) taken; LAW art 27(1)(c) agrees for property insurance).
- **Evidence**: `bmfire-findings.l4:100`, `:102`, `:109`, `:110`. src:11, 446-484.
- **Plain-English test of surprise**: either party expects one rule on unpaid premium; the document gives three.

### VN-20 X10 — Electrical exclusion removes direct lightning damage
- **Class**: T2 / T6
- **Scenario**: Risk A covers direct lightning, but III.1(c) excludes electrical machinery damaged by its own electrical fault "do bất kỳ nguyên nhân nào (kể cả sét đánh)" (from any cause, including lightning). Direct lightning burns out a printing press (150,000,000 damage): excluded under III.1(c).
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bmfire-findings.l4:118` (reasons EQUALS III.1(c)). src:38-40, 175-181.
- **Plain-English test of surprise**: a business sold lightning cover expects a struck machine paid; the electrical exclusion takes it.

### VN-20 X11 — Date-change write-back omits flood and water perils
- **Class**: T7 / T6
- **Scenario**: The date-change write-back omits flood, water from tanks, sprinklers, animals and subsidence, and lists perils the policy does not insure. A date fault in a pump controller lets a river flood the site: excluded under H; the same fault with a storm: covered.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F15 maps the perils).
- **Evidence**: `bmfire-findings.l4:125` (flood: VIII.2), `:126` (storm: EMPTY). src:428-432, 116, 128.
- **Plain-English test of surprise**: an insured with flood cover expects a flood paid; a computer fault upstream removes it.

### VN-20 X12 — Short-period scale lists three months twice
- **Class**: T4 / T5
- **Scenario**: "Đến 3 tháng" (up to 3 months) and "Từ 3 đến 6 tháng" (from 3 to 6 months) both describe a termination exactly 3 months in: the short-period rate is 30% or 60%.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: CONTESTED (fork F24 takes the lower row, favouring the insured).
- **Evidence**: `bmfire-findings.l4:132` (EQUALS 30%). src:251-253.
- **Plain-English test of surprise**: a policyholder cancelling at 3 months expects one rate; the scale gives two.

### VN-20 X13 — Cancellation refund ignores the seven notice days
- **Class**: T4 / T1
- **Scenario**: When the insurer cancels, cover runs 7 days after notice but the refund counts from the notice day. Notice 2 July, cover to 9 July: refund of 6,000,000 for 182 of 364 days, though the policy ran 189.
- **Who bears it**: insurer. **Money direction**: against the insurer (inferred: 7 days covered and refunded).
- **Standing**: LITERAL (fork F23: refund "from the day the notice is issued").
- **Evidence**: `bmfire-findings.l4:138` (effective 2026-07-09), `:139` (EQUALS 6,000,000). src:241-244.
- **Plain-English test of surprise**: either party expects the refund to match the days not covered; seven days are both covered and refunded.

### VN-20 X14 — Any breached condition defeats any claim
- **Class**: T12 / T2
- **Scenario**: The preamble makes all conditions conditions precedent, and VI.6 is open-ended ("mọi biện pháp thích hợp", every proper measure). A storm blows the roof off; the insured had neglected the gutters, unconnected to the roof: nothing is payable on a 200,000,000 loss.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL; LAW for late notice only (art 46, fork F29).
- **Evidence**: `bmfire-findings.l4:150` (EQUALS 0). src:6-8, 262-265.
- **Plain-English test of surprise**: an owner expects neglected gutters to matter only for water damage; they forfeit a storm claim.

### VN-20 X15 — Innocent misstatement voids the policy at insurer's option
- **Class**: T3 / T11
- **Scenario**: VI.2 lets the insurer treat the policy as void for a misstatement with no intent and, for misstatement, no materiality. A wrong construction year given in good faith suffices.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (art 22(2), aid 543-553; fork F31). Reading only.
- **Evidence**: reading only. src:220-223.
- **Plain-English test of surprise**: a policyholder expects an honest mistake to be corrected; it can void the policy.

### VN-20 X16 — Insurer cancels on seven days, any reason
- **Class**: T3 / T11
- **Scenario**: The insurer may cancel on 7 days' notice for any reason, by registered letter to the last known address, without proof of receipt. Cancellation could be sent as a typhoon approaches.
- **Who bears it**: policyholder. **Money direction**: against the claimant.
- **Standing**: LAW (art 26, aid 623-635; fork F38). Reading only.
- **Evidence**: reading only. src:240-244.
- **Plain-English test of surprise**: a policyholder expects cover through storm season; it can be withdrawn on a week's notice.

### VN-20 X17 — Short agreed payment term extends time to pay
- **Class**: T7 / T5
- **Scenario**: VIII.3.1(c) applies "khi thời hạn thanh toán phí bảo hiểm dưới 30 ngày" (when the premium payment term is under 30 days). With an agreed 15-day term, payment is due by the end of the period (31 December 2026); with no term, by 31 January 2026.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F34 reading (i), as written; reading (ii), a period of insurance under 30 days).
- **Evidence**: `bmfire-findings.l4:156` (2026-12-31), `:157` (2026-01-31). src:476-478.
- **Plain-English test of surprise**: an insurer expects a shorter agreed term to mean earlier payment; it means later.

### VN-20 X18 — Winning arbitration still requires suit within twelve months
- **Class**: T12 / T1
- **Scenario**: After an arbitral award on the amount in the insured's favour, if the insurer does not pay and the insured does not sue within 12 months, the benefit is lost.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:298-300.
- **Plain-English test of surprise**: an insured holding an award expects it to be enforceable; it lapses unless followed by suit.

### VN-20 X19 — Insurer has no deadline; reinstatement choice has no criteria
- **Class**: T1 / T11
- **Scenario**: The insurer has no period to assess or pay and may choose to reinstate with no criteria, while the insured's periods are "at once", 30 days and 12 months.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (art 31(1), aid 719-724; fork F37). Reading only.
- **Evidence**: reading only. src:9-10, 301-314.
- **Plain-English test of surprise**: an insured expects reciprocal deadlines; only the insured has them.

#### VN-20 row summary
- Findings in section 4: 19 (X1 to X19); 19 records above.
- Three most counterintuitive (the encoder names X3, X14 and X9 as most likely to matter): X3 (riot cover given and taken back by a label); X14 (neglected gutters forfeit a storm claim on the roof); X10 (direct lightning on a machine is excluded under a lightning policy).
- Matches in this group: X3 = VN-07 F1. X5 ~ VN-07 F12 (order of operations cuts the payout). X8 = VN-05 X-vacancy, VN-07 F10, VN-08 F6. X11 ~ VN-08 F11, F13. X12 = VN-08 F8. X14 = VN-05 X-precedent, VN-08 F2, VN-21 F3. X15 = VN-07 F7, VN-08 F17, VN-22 X18. X16 = VN-05 X-cancel, VN-08 F20, VN-09 X13. X17 = VN-08 F4 (same words, opposite fork). X18 = VN-05 X-award. X7 ~ VN-07 F3 (two clocks for one dispute). X19 = VN-05 X-payment-time, VN-07 F20, VN-08 F22.

---

## VN-21 Bảo Minh installation all risks

Directory: `vn-baominh-installation-all-risks/encodings/legalese-2026-10-vn-21`.
Findings module: `bm-ear-tests-findings.l4`. Findings numbered 1 to 21; "fork F0n" is the section 3 register.

### VN-21 Finding 1 — Fourteen-day notice bar defeats hidden damage
- **Class**: T1 / T12
- **Scenario**: Unless notice is received within 14 days of the occurrence (not discovery), Bao Minh is not liable "Trong mọi trường hợp" (in any case). Hidden damage on 1 June 2026, found 20 June, notified 21 June: nothing payable under either Part.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (Law 46 and 19(3) allow only a proportionate reduction and exclude force majeure; fork F02). The policy as written gives nothing.
- **Evidence**: `bm-ear-tests-findings.l4:24` (ground GC5), `:25-26` (Part I 0, Part II 0). src:109-111, 94.
- **Plain-English test of surprise**: an insured expects the notice clock to start on discovery; hidden damage is time-barred before it is found.

### VN-21 Finding 2 — One innocent questionnaire slip defeats every claim
- **Class**: T12 / T3
- **Scenario**: GC1 makes true and complete answers a condition precedent, with no test of intent, materiality or connection. One incomplete answer, however trivial, leaves Part I and Part II at 0 where the same claim otherwise pays 900,000,000 and 330,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F04 reading (ii), answers true; reading (i), answered, which Điều 24 would favour); LAW (Law 22(2) requires intent; see Finding 21).
- **Evidence**: `bm-ear-tests-findings.l4:34-35` (0, 0), `:37-38` (900,000,000, 330,000,000). src:62-65, 5-8.
- **Plain-English test of surprise**: an insured who made an honest slip expects it ignored if irrelevant; it forfeits everything.

### VN-21 Finding 3 — Any unconnected breach defeats the claim
- **Class**: T12 / T2
- **Scenario**: Every duty is a condition precedent with no connection test. Not following a manufacturer's recommendation about another machine defeats a Part I crane-collapse claim; a late police report of an unrelated theft defeats a Part II injury claim.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F02 reading (i), "the words"; Điều 24 would favour (ii), a connection test; LAW art 46 and 19(3) for notice).
- **Evidence**: `bm-ear-tests-findings.l4:44` (Part I 0), `:46` (Part II 0). src:62-65.
- **Plain-English test of surprise**: an insured expects only a breach that caused the loss to matter; any breach suffices.

### VN-21 Finding 4 — Forfeiture condition overrides the average remedy
- **Class**: T4 / T7
- **Scenario**: Article 1 asks the insured to adjust sums insured when prices change, with average as its remedy. Because the undertaking is a duty, GC1 makes it a condition precedent: an item underinsured at 80% pays 0 instead of the average figure 710,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (on fork F02 reading (i)).
- **Evidence**: `bm-ear-tests-findings.l4:59` (710,000,000), `:60` (0). src:193-203, 62-65.
- **Plain-English test of surprise**: an underinsured owner expects a proportionate cut; the wording pays nothing.

### VN-21 Finding 5 — Burden-of-proof clause names the wrong party
- **Class**: T5 / T7
- **Scenario**: The clause shifts the burden when THE INSURED contends exclusion (a) applies, which an insured never does, and is silent when Bao Minh does. As written it never helps the insurer.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F03 reading (i), the words; reading (ii), the evident purpose; "a Vietnamese court may read it purposively").
- **Evidence**: `bm-ear-tests-findings.l4:64-65` (REFUSED for an allegation by Bao Minh). src:34-37.
- **Plain-English test of surprise**: an insurer expects its war and riot exclusion to carry a burden shift; the clause shifts nothing.

### VN-21 Finding 6 — Suit bar never starts for an outright rejection
- **Class**: T13 (translation omission) / T1
- **Scenario**: GC8's three-month bar runs only "from when the arbitrators made their award", and arbitration takes only disputes on amount with liability admitted. A claim rejected outright on 1 July 2026 cannot be arbitrated, so no bar starts: still not barred on 1 January 2030. The evident source wording also ran from the rejection.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F19 reading (i), the words; Điều 24 agrees).
- **Evidence**: `bm-ear-tests-findings.l4:71` (NOT barred). src:143-146, 131-132.
- **Plain-English test of surprise**: an insurer expects rejected claims to be time-barred quickly; as translated they never are.

### VN-21 Finding 7 — No award, no action; nothing forces an appointment
- **Class**: T11 / T12
- **Scenario**: An arbitral award is a condition precedent to any action on the amount, but a party who ignores a written request to appoint an arbitrator suffers nothing: no consequence, no default appointment. If Bao Minh never appoints, there is no award and no action lies.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bm-ear-tests-findings.l4:78`; traces at `bm-ear-tests-duties.l4:69-74` end in a breach by Bao Minh with no consequence. src:131-139.
- **Plain-English test of surprise**: an insured expects the insurer's refusal to appoint to open the courts; it closes them.

### VN-21 Finding 8 — Average applies to items with no stated measure
- **Class**: T4 / T8
- **Scenario**: "Every item ... separately" is subject to average, but the amount that ought to have been insured is stated only for items 1 and 2 (and, on fork F23, item 4). For item 3 the proportion cannot be computed.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F23).
- **Evidence**: `bm-ear-tests-findings.l4:82-83` (REFUSED for item 3). src:193-203.
- **Plain-English test of surprise**: an insured expects average to have a formula; for most items it has none.

### VN-21 Finding 9 — Total loss pays nothing until insured self-funds replacement
- **Class**: T6 / T7
- **Scenario**: The insuring clause promises cash, repair or replacement at Bao Minh's option, but Article 2 pays only "costs actually incurred" after invoices. Item 1, worth 8,000,000,000, is destroyed (salvage 500,000,000); the insured has not yet spent anything, and no ground of non-liability applies, yet 0 is payable.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F16: the option conflicts with Article 2).
- **Evidence**: `bm-ear-tests-findings.l4:92` (no ground), `:93` (EQUALS 0). src:155-160, 211-222.
- **Plain-English test of surprise**: an insured with a total loss expects money to rebuild; it must rebuild first.

### VN-21 Finding 10 — Neighbouring property damaged by civil works falls between Parts
- **Class**: T6 / T7
- **Scenario**: Article 4 covers surrounding property only for damage directly connected with ERECTION OR TESTING; Part II names construction but exclusion 3(b) excludes the principal's property. The principal's building next to the site is damaged by civil works (300,000,000 damages): Part I 0, Part II 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bm-ear-tests-findings.l4:107-109`. src:237-242, 255, 287-290.
- **Plain-English test of surprise**: a contractor with both material damage and liability cover expects one Part to respond; neither does.

### VN-21 Finding 11 — Repair required before payment and to keep cover
- **Class**: T12 / T6
- **Scenario**: Bao Minh pays only after repair invoices, and its liability for an item ends if the item is not repaired "promptly and properly". An insured short of cash loses the payment for the first loss and the cover for the next.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only (second limb on fork F12).
- **Evidence**: reading only; the second limb tested at `bm-ear-tests-part1.l4:80`. src:119-120, 218-222.
- **Plain-English test of surprise**: an insured waiting for money to repair expects to stay covered; the delay ends cover.

### VN-21 Finding 12 — Weight-bearing words never defined
- **Class**: T5
- **Scenario**: GC2 says defined words keep their meaning, but only the insurer's short name is defined. "sự cố" (occurrence), by which every deductible and limit counts, "material change", "minor damage", "reasonable time", "representative" and "third party" are undefined; the two deductibles use two different words.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only.
- **Plain-English test of surprise**: a reader expects the unit of the deductible defined; it is not.

### VN-21 Finding 13 — Weekend stoppage counts as cessation of work
- **Class**: T2
- **Scenario**: A general exclusion removes loss during "cessation of work, whole or partial", with no minimum duration. A theft from the site over a weekend when work had stopped pays 0.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bm-ear-tests-findings.l4:114` (EQUALS 0). src:32.
- **Plain-English test of surprise**: a contractor expects ordinary weekend breaks covered; they trigger the exclusion.

### VN-21 Finding 14 — Notices must be sent by telegram
- **Class**: T12 / T13 (obsolete notice channel)
- **Scenario**: Notices must go by telegram and in writing (src:81-82), or by telephone or telegram as well as in writing (src:94-95). If no telegram service is available, a question of fact outside the document, GC4(b) cannot be complied with, and GC1 then defeats every claim.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only (fork F32 not decided).
- **Evidence**: reading only. src:81-82, 94-95.
- **Plain-English test of surprise**: an insured expects email or letter to suffice; the text requires a telegram.

### VN-21 Finding 15 — Insurer adjusts cover after material change without criteria
- **Class**: T11
- **Scenario**: After a material change Bao Minh may adjust cover or premium, with no criterion; the adjusted premium cannot be computed.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `bm-ear-tests-general.l4:83-84` (REFUSED). src:84-85.
- **Plain-English test of surprise**: a policyholder expects a stated basis for re-pricing; the insurer decides freely.

### VN-21 Finding 16 — False declaration in one claim forfeits all claims
- **Class**: T12
- **Scenario**: "All benefits under this Policy" lose their value on a false declaration. An honest claim made after a false declaration in an earlier claim pays 0 under both Parts.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bm-ear-tests-findings.l4:119-120` (0, 0). src:141-146.
- **Plain-English test of surprise**: a reader expects fraud to forfeit the tainted claim; a later honest one is lost too.

### VN-21 Finding 17 — Insurer pays settlement value, then walks away
- **Class**: T11
- **Scenario**: Part II condition 2 lets Bao Minh pay what the claim "can be settled" for, without saying who judges that, after which the insured's further defence costs are its own. After a condition 2 payment, a passer-by injury suit defended with consent pays 0 more.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bm-ear-tests-findings.l4:126` (EQUALS 0). src:310-314.
- **Plain-English test of surprise**: an insured expects defence funded until the case ends; the insurer can pay out and leave.

### VN-21 Finding 18 — Other-insurance clause gives no basis for proportion
- **Class**: T5 / T4
- **Scenario**: GC9 limits Bao Minh to its proportion where other insurance exists, but says nothing about how that proportion is computed. A Part II claim with other insurance and no agreed share cannot be computed.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F20 "not stated"; LAW Law 49 fixes a sum-insured basis for double insurance in some cases).
- **Evidence**: `bm-ear-tests-findings.l4:130-131` (REFUSED). src:148-150.
- **Plain-English test of surprise**: an insured with two policies expects a formula; there is none.

### VN-21 Finding 19 — Translation and typesetting defects
- **Class**: T13 (translation and typesetting defects) / T5
- **Scenario**: Misspellings ("khôngg", "băng văn bản", "vật liệu vật liệu", "khởi nghiã"), an unclosed parenthesis in the preamble, "hạn mức trách nhiệm bồi thường đó" (that limit) with no antecedent, the burden clause's subject (Finding 5) and GC8's missing anchor (Finding 6).
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:144, 133, 187, 22, 7-8, 162.
- **Plain-English test of surprise**: a reader expects a published policy to be proofread; several defects change meaning.

### VN-21 Finding 20 — Notice bar stricter than statute allows
- **Class**: T3 / T1
- **Scenario**: The absolute 14-day notice bar conflicts with Law 46, which allows only a proportionate reduction for late notice, and Law 19(3), which excludes force majeure delay.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F02). Reading only; the Law is not encoded.
- **Evidence**: reading only. src:109-111.
- **Plain-English test of surprise**: an insured expects the statute's softer rule to apply; the policy's text says otherwise.

### VN-21 Finding 21 — Disclosure condition stricter than statute allows
- **Class**: T3 / T12
- **Scenario**: GC1 defeats cover for any untrue or incomplete answer; Law 22(2) lets the insurer avoid only for intentional non-disclosure or falsehood.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F04). Reading only.
- **Evidence**: reading only. src:62-65.
- **Plain-English test of surprise**: an insured expects honest mistakes forgiven, as the statute does; the policy does not.

#### VN-21 row summary
- Findings in section 4: 21 (numbered 1 to 21); 21 records above.
- Three most counterintuitive (the encoder names 1, 2-3 and 9 as most likely to matter): Finding 9 (a total loss pays 0 until the insured funds replacement); Finding 1 (hidden damage is time-barred before discovery); Finding 10 (neighbouring property damaged by civil works falls between both Parts).
- Matches in this group: VN-21 and VN-22 are sibling Bảo Minh forms (installation and construction) and share most defects: F5 = VN-22 X2 (burden clause names the insured); F6 = VN-22 X10 (suit bar never starts on outright rejection); F7 = VN-22 X8 (non-appointment stalls arbitration); F9, F11 = VN-22 X17, X7 (pay only after repair; repair promptly or lose cover); F12 = VN-22 X20; F13 = VN-22 X24 (cessation of work); F14 = VN-22 X6 (telegram); F15 = VN-22 X23; F17 = VN-22 X19; F18 = VN-22 X12; F19 = VN-22 X21, X13 (same typos, same antecedent-less "hạn mức ... đó"). Beyond VN-22: F3 = VN-05 X-precedent, VN-08 F2, VN-20 X14; F16 = VN-07 F15, VN-08 F21; F21 = VN-07 F7, VN-08 F17, VN-20 X15.

---

## VN-22 Bảo Minh construction all risks

Directory: `vn-baominh-construction-all-risks/encodings/legalese-2026-10-vn-22`.
Findings module: `bmcar-findings.l4`; some evidence is in `bmcar-tests.l4`. Findings X1 to X24.

### VN-22 X1 — The recital never finishes its sentence
- **Class**: T5 / T13 (unfinished sentence)
- **Scenario**: The recital's "(giấy yêu cầu bảo hiểm này được xem như)" (this proposal is deemed to be) names nothing, and the next parenthesis never closes. An insured could argue a proposal statement is not a term because the deeming is incomplete.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only (fork F1 calls it inert: GC1 gives the answers effect anyway).
- **Evidence**: reading only. src:6-9.
- **Plain-English test of surprise**: a reader expects the policy's opening sentence to be complete; it is not.

### VN-22 X2 — Burden-of-proof clause names the wrong party
- **Class**: T5 / T7
- **Scenario**: The clause shifts the burden of proving cover to the insured where the insured ("Người được bảo hiểm cho là") contends exclusion (a) applies. An insured never contends its own loss is excluded, so the clause never operates, and the case that matters, Bảo Minh alleging riot or strike, is not addressed.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F4 reading (i), as written; reading (ii) treats it as the insurer contending).
- **Evidence**: `bmcar-tests.l4:82` (REFUSED where Bảo Minh contends); §§ General Exclusions from line 60. src:36-39.
- **Plain-English test of surprise**: an insurer expects its burden shift to work; it names the wrong side.

### VN-22 X3 — Cover can begin before the Schedule's start date
- **Class**: T5 / T7
- **Scenario**: Liability starts on the site events "dù ngày quy định trong phụ lục có thể khác" (though the date in the Schedule may differ). Schedule from 1 March 2026, work began 15 February: a loss on 20 February is in the period.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: CONTESTED (fork F6 reading (i), as the Vietnamese reads; reading (ii), never before the Schedule date; an English original "only after" is outside knowledge, unverified).
- **Evidence**: `bmcar-findings.l4:25` (in the period). src:44-45.
- **Plain-English test of surprise**: an insurer expects cover to start on the Schedule date; site activity can start it earlier.

### VN-22 X4 — Handed over or in use, but not both, stays covered
- **Class**: T5 / T7
- **Scenario**: Cover on a part ends only when it is "bàn giao và đưa vào sử dụng" (handed over AND put into use). A floor occupied by the owner for months without formal handover remains at the contractor's insurer's risk: 350,000,000 payable for a loss to a part in use but not handed over, and likewise the reverse.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F7: "và").
- **Evidence**: `bmcar-findings.l4:31-32` (payable 350,000,000 in both cases). src:47-48.
- **Plain-English test of surprise**: an insurer expects cover to end once the owner moves in; it continues.

### VN-22 X5 — Timely notice can still defeat the claim
- **Class**: T7 / T12
- **Scenario**: GC5(a) requires notice "lập tức" (immediately); lines 102-104 allow 14 days before the bar; GC1 makes every duty a condition precedent. Occurrence 10 June 2026, notice received on day 2 but found not immediate: within the 14 days, yet nothing is payable.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (forks F9, F11); the encoder records LAW art 46 and 19(3) on late notice (fork F38), not resolved.
- **Evidence**: `bmcar-findings.l4:40` (received within 14 days), `:41` (nothing payable, GC1). src:89, 102-104, 57-60.
- **Plain-English test of surprise**: an insured who meets the 14-day deadline expects to be in time; a second standard defeats it.

### VN-22 X6 — Telegram required; unrelated claim fails without one
- **Class**: T12 / T13 (obsolete notice channel)
- **Scenario**: GC4(b) requires notice of a material change "bằng điện tín và bằng văn bản" (by telegram and in writing); GC5(a), phone or telegram plus writing. A change notified promptly in writing only, then an unconnected storm loss: nothing payable under GC1. A written-only loss notice fails likewise.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL (fork F10: "và"); whether telegram service still exists is outside knowledge, unverified.
- **Evidence**: `bmcar-findings.l4:49` (4(b) case), `:51` (5(a) case). src:76-77, 89-90.
- **Plain-English test of surprise**: an insured who notified in writing expects to be covered; the missing telegram voids an unrelated claim.

### VN-22 X7 — Must wait for inspection, yet repair without delay
- **Class**: T11 / T7
- **Scenario**: Non-minor damage may not be repaired before inspection or before a period "được xem là hợp lý" (considered reasonable) passes, with no criteria; liability on an item ends if it is not repaired "kịp thời" (promptly). An early repair breaches a condition precedent; a late one loses the item's cover; Bảo Minh controls the first clock.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only; the period is an input to traces at `bmcar-tests.l4:130-133`. src:106-112, 114-115.
- **Plain-English test of surprise**: an insured expects a clear time to start repairs; both early and late are breaches.

### VN-22 X8 — Arbitration can be stalled indefinitely by non-appointment
- **Class**: T11 / T12
- **Scenario**: Each party has one month to appoint an arbitrator, with no consequence for failing and no default mechanism; the award is a condition precedent to any action. Bảo Minh does not appoint: 400 days later the duty is breached and the action is still barred, with no date when that stops.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bmcar-findings.l4:60-62` (trace ends in breach by Bảo Minh; bar TRUE). src:128-134.
- **Plain-English test of surprise**: an insured expects the insurer's refusal to engage to open the courts; it closes them.

### VN-22 X9 — "Trọng tài chung" means two different people
- **Class**: T5 / T7
- **Scenario**: "Trọng tài chung" is the agreed sole arbitrator at line 128 and the umpire appointed by two arbitrators at lines 131-132; the condition precedent is the award "của cuộc họp" (of the meeting), presupposing three; GC8's clock starts on an award of "hai Trọng tài viên hay Trọng tài chung". GC2 says a term keeps one meaning.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only (fork F16 takes an award by any of the three).
- **Evidence**: reading only. src:128, 131-133, 140.
- **Plain-English test of surprise**: a reader expects one term, one meaning; this one has two.

### VN-22 X10 — Suit time-bar never reaches an outright rejection
- **Class**: T13 (missing limb) / T1
- **Scenario**: GC8, as the Vietnamese has it, bars suit three months after an award only; an outright rejection is a liability dispute that GC7 does not send to arbitration, so there is never an award and never a bar. Rejected in 2026, no proceedings by 2031: not forfeited.
- **Who bears it**: insurer. **Money direction**: against the insurer.
- **Standing**: LITERAL (fork F16 reading (i): "the Vietnamese has no clock from the rejection").
- **Evidence**: `bmcar-findings.l4:70` (not arbitrable), `:71` (NOT forfeited). src:138-141.
- **Plain-English test of surprise**: an insurer expects rejected claims to go stale; as written they never do.

### VN-22 X11 — Liability disputes have no forum in the document
- **Class**: T13 (no forum for liability disputes) / T5
- **Scenario**: GC7 sends only disputes about the amount to arbitration; nothing says where a dispute about liability goes.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only; LAW art 32 noted (fork F41: negotiation, mediation, arbitration or court).
- **Evidence**: reading only. src:126-127.
- **Plain-English test of surprise**: a policyholder whose claim is denied expects the policy to say where to go; it is silent.

### VN-22 X12 — "Rateable proportion" undefined
- **Class**: T5 / T4
- **Scenario**: GC9 limits Bảo Minh to "tỷ lệ của họ" (its proportion) where other insurance exists, with no basis. A Section I claim with other insurance cannot be computed.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL (fork F17: not answered; LAW art 49 fills it only where the total exceeds market value).
- **Evidence**: `bmcar-tests.l4:177` (REFUSED). src:143-145.
- **Plain-English test of surprise**: an insured with two policies expects a formula; there is none.

### VN-22 X13 — A limit called "that" with no antecedent
- **Class**: T5
- **Scenario**: Section I says each occurrence "sẽ không vượt quá hạn mức trách nhiệm bồi thường đó" (shall not exceed that limit of liability), and nothing before it names a limit.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only (fork F18 makes it an optional Schedule figure).
- **Evidence**: reading only. src:158-159.
- **Plain-English test of surprise**: a reader expects a cap to be identified; this one refers to nothing.

### VN-22 X14 — Defect exclusion can swallow the whole works
- **Class**: T2 / T5
- **Scenario**: Exclusion (d) for defective material or workmanship is limited to "những hạng mục bị ảnh hưởng trực tiếp" (the items directly affected), and "hạng mục" elsewhere means a Schedule item. A 20,000,000 defective beam brings down 400,000,000 of works: 380,000,000 on the component reading taken; nothing on the Schedule-item reading.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F22: component reading taken; Schedule-item reading demonstrated).
- **Evidence**: `bmcar-findings.l4:94` (380,000,000), `:95` (whole loss excluded on the other reading). src:153-154, 181-184, 64-66.
- **Plain-English test of surprise**: a contractor expects only the defective beam excluded; the words can exclude the collapse.

### VN-22 X15 — Insured at new price, paid at depreciated value
- **Class**: T4 / T6
- **Scenario**: Article I requires plant insured at replacement value new; Article 2(b) pays a total loss at actual value before the loss. Plant worth 1,200,000,000, 2,000,000,000 new, destroyed and replaced new: 1,200,000,000 paid on a premium charged on 2,000,000,000. Insured at 1,200,000,000 instead, average cuts it to 720,000,000.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bmcar-findings.l4:105` (1,200,000,000), `:108` (720,000,000). src:210-211, 231-232.
- **Plain-English test of surprise**: a contractor paying premium on new value expects new value back; it gets depreciated value.

### VN-22 X16 — Average cuts a small early loss
- **Class**: T4
- **Scenario**: Item 1 must be insured at full contract value at completion, and average compares the sum insured with that, whatever was at risk at the loss. Works insured for 10,000,000,000, completion value 12,500,000,000; with 1,000,000,000 built, 400,000,000 is damaged and 320,000,000 is paid.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL; LAW art 48 measures at contracting "or as the contract agrees"; whether a future-date basis is permitted is open (fork F42).
- **Evidence**: `bmcar-findings.l4:117` (EQUALS 320,000,000). src:206-208, 217-220.
- **Plain-English test of surprise**: an insured covered ten times over the value at risk expects full payment; average still cuts it.

### VN-22 X17 — Nothing paid until insured funds repair or replacement
- **Class**: T6 / T12
- **Scenario**: Section I pays only costs "thực tế phải gánh chịu" (actually incurred), after invoices, and cover on an item ends if it is not repaired promptly. Plant destroyed and not yet replaced pays 0, as does an unpaid repair; a contractor unable to fund the work may also lose the item's cover.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED for replacement (fork F27 applies the clause to both bases; contra proferentem would favour repairs only); LITERAL for repairs.
- **Evidence**: `bmcar-findings.l4:125-128`. src:234-240, 114-115.
- **Plain-English test of surprise**: a contractor expects the insurer to fund the rebuild; it must fund it first.

### VN-22 X18 — Innocent false declaration forfeits all benefit
- **Class**: T12 / T3
- **Scenario**: GC8 forfeits "tất cả các quyền lợi" (all benefits) on a "khai báo sai" (false declaration) made or used in support of a claim, with no intent stated. An innocent mistake in a supporting document reads as a forfeiture.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LAW (fork F46: art 22.2 needs an intentional untruth).
- **Evidence**: `bmcar-tests.l4:163` (`a history with a false declaration` forfeits). src:136, 141.
- **Plain-English test of surprise**: an insured who made an honest error expects it corrected; it forfeits everything.

### VN-22 X19 — Insurer may pay settlement value and walk away
- **Class**: T11
- **Scenario**: Section II gives Bảo Minh "toàn quyền" (full discretion) over defence and settlement, and lets it pay "a lesser sum for which the claims can be settled" and be discharged. With 4,000,000,000 of limit left, Bảo Minh pays 2,500,000,000 and owes nothing further; a higher recovery or further defence cost is the insured's.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: LITERAL.
- **Evidence**: `bmcar-findings.l4:136` (2,500,000,000 discharges), `:137` (further liability 0). src:314-317, 321-325.
- **Plain-English test of surprise**: an insured expects defence through to judgement within the limit; the insurer can pay its own estimate and leave.

### VN-22 X20 — Weight-bearing terms never defined
- **Class**: T5
- **Scenario**: GC2 presupposes definitions but the document defines nothing. "sự cố" (occurrence, the unit of deductibles and limits), "material change", "minor damage", "third party" and "công trường" (site) are undefined; "hạng mục" and "Trọng tài chung" are used in two senses.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:64-66.
- **Plain-English test of surprise**: a reader expects the deductible's unit defined; it is not.

### VN-22 X21 — Drafting slips, one changing an exclusion
- **Class**: T13 (drafting slips) / T5
- **Scenario**: "Điều I" is followed by "Điều 2" and "Điều 3"; several misspellings ("dđòi hỏi", "luơng bổng", "băng", "khôngg", "khoảnmục", "thoả thận", "khởi nghiã"); line 302 omits a word, leaving exclusion 4(b)'s qualifier unclear.
- **Who bears it**: unclear. **Money direction**: unclear.
- **Standing**: LITERAL, reading only.
- **Evidence**: reading only. src:202, 204, 207, 128, 211, 139, 220, 306, 23, 302.
- **Plain-English test of surprise**: a reader expects a published policy proofread; one slip changes an exclusion.

### VN-22 X22 — Borrowed wording from the installation form
- **Class**: T13 (borrowed wording)
- **Scenario**: Section II's insuring clause speaks of "xây dựng hay lắp đặt" (construction or erection), erection being the installation wording's subject; every page footer reads "(Munich Re)_03.06".
- **Who bears it**: unclear. **Money direction**: no money.
- **Standing**: LITERAL, reading only ("harmless to the Insured").
- **Evidence**: reading only. src:266.
- **Plain-English test of surprise**: a reader expects a construction form to speak of construction; it carries over installation wording.

### VN-22 X23 — Insurer adjusts cover or premium without criteria
- **Class**: T11
- **Scenario**: After a material change "phạm vi bảo hiểm và/hoặc phí bảo hiểm sẽ được điều chỉnh một cách thích hợp" (cover and/or premium will be adjusted appropriately), with no criteria; the adjustment cannot be computed.
- **Who bears it**: policyholder. **Money direction**: unclear.
- **Standing**: LITERAL.
- **Evidence**: `bmcar-tests.l4:109` (REFUSED). src:79-80.
- **Plain-English test of surprise**: a policyholder expects a stated basis for re-pricing; the insurer decides.

### VN-22 X24 — Work stoppage anywhere in the chain excludes storm loss
- **Class**: T2
- **Scenario**: General Exclusion (d) (cessation of work) applies to loss "trực tiếp hay gián tiếp" (directly or indirectly) caused. A storm damages a site idle during a suspension of work: excluded, because the stoppage is among the causes.
- **Who bears it**: insured. **Money direction**: against the claimant.
- **Standing**: CONTESTED (fork F3 reading (i), any listed cause; contra proferentem would favour (ii), dominant cause).
- **Evidence**: `bmcar-findings.l4:145` (nothing payable). src:19-20, 34.
- **Plain-English test of surprise**: a contractor expects storm damage covered; the site being idle removes it.

#### VN-22 row summary
- Findings in section 4: 24 (X1 to X24); 24 records above.
- Three most counterintuitive: X15 (premium charged on new value, payout at depreciated value); X16 (works insured at ten times the value at risk still suffer average); X5 (notice inside the 14-day deadline still defeats the claim).
- Matches in this group: sibling of VN-21 (see the VN-21 summary for the one-to-one list: X2, X6, X7, X8, X10, X12, X13, X17, X19, X20, X21, X23, X24). X5, X6 = VN-05 X-precedent, VN-08 F2, VN-20 X14 (condition precedent with no causal test). X18 = VN-07 F7, VN-08 F17, VN-20 X15 (no intent required, Law art 22(2)). X15, X16 ~ VN-08 F18, VN-21 F4 (average produces a payout below what was insured). X3 ~ VN-07 F11 (start of cover not tied to the Schedule date). X14 has no match in the group.

---
