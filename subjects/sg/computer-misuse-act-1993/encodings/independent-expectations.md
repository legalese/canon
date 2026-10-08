# Independent expectations: Computer Misuse Act 1993 (2020 RevEd, as amended to Act 21 of 2025)

Written from `BRIEF.md` and `../source/CMA1993.txt` alone, before any `.l4` module was opened.
These values are fixed and are not changed after encoding modules were read.

Conventions: amounts in SGD, imprisonment in years, caning in strokes. "Conduct date" is the
date of the conduct; all scenarios use a conduct date of 2026-03-01 unless stated otherwise.

## A. Definitions (s 2; First Schedule)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| A1 | General-purpose server (data processing device, logical/storage functions), not excluded | is a computer | s 2(1) "computer" |
| A2 | Automated typewriter | not a computer | s 2(1) "computer" (a) |
| A3 | Portable hand-held calculator | not a computer | s 2(1) "computer" (b) |
| A4 | Similar device that is non-programmable | not a computer | s 2(1) "computer" (c) |
| A5 | Similar device with no data storage facility | not a computer | s 2(1) "computer" (c) |
| A6 | Device prescribed by Minister by Gazette notification | not a computer | s 2(1) "computer" (d) |
| A7 | Person causes computer to perform a function and thereby alters data | secures access | s 2(2)(a) |
| A8 | Copies data to a USB drive | secures access | s 2(2)(b) |
| A9 | Moves data to a different location in the same storage medium | secures access | s 2(2)(b) |
| A10 | Causes data to be displayed on screen | secures access | s 2(2)(d) |
| A11 | Function causes program to be executed | uses the program, so secures access | s 2(2)(c), 2(3)(a) |
| A12 | Function is itself a function of the program | uses the program | s 2(3)(b) |
| A13 | Causes a computer to perform a function but none of alter/copy/move/use/output occurs | does not secure access | s 2(2) |
| A14 | Not entitled to control access, and no consent from entitled person | unauthorised | s 2(5) |
| A15 | Not entitled, but has consent of an entitled person | authorised | s 2(5)(b) |
| A16 | Entitled to control access of the kind in question | authorised | s 2(5)(a) |
| A17 | Data in computer is erased by operation of a function | modification | s 2(7)(a) |
| A18 | Program added to the contents | modification | s 2(7)(b) |
| A19 | Act impairs normal operation of any computer | modification | s 2(7)(c) |
| A20 | Nothing altered, erased, added, or impaired | no modification | s 2(7) |
| A21 | Modifier not entitled to determine, no consent | modification unauthorised | s 2(8) |
| A22 | Modifier has consent of entitled person | modification authorised | s 2(8)(b) |
| A23 | Impairment causing loss of exactly $10,000 within a year | damage | s 2(1) "damage" (a) "at least $10,000" |
| A24 | Impairment causing loss of $9,999.99 only, no other limb | no damage | s 2(1) "damage" (a) |
| A25 | $6,000 loss within 1 year + $6,000 loss accrued more than 1 year after offence | no damage (only $6,000 counts) | s 2(1) "damage" (a) proviso |
| A26 | $4,000 + $7,000 both within the year (aggregating) | damage ($11,000) | s 2(1) "damage" (a) "aggregating" |
| A27 | Impairment potentially impairs medical treatment of a person, $0 loss | damage | s 2(1) "damage" (b) |
| A28 | Impairment threatens physical injury, $0 loss | damage | s 2(1) "damage" (c) |
| A29 | Impairment threatens public safety, $0 loss | damage | s 2(1) "damage" (d) |
| A30 | No impairment at all, though loss of $50,000 arises | no damage (damage requires an impairment) | s 2(1) "damage" chapeau |
| A31 | Minister prescribed threshold $20,000; loss $15,000 | no damage | s 2(1) "damage" (a) "or such other amount" |

## B. Offences (ss 3-10, 12)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| B1 | Knowingly causes computer to perform function to secure unauthorised access | s 3 offence made out | s 3(1) |
| B2 | Same, but not knowingly | no s 3 offence | s 3(1) "knowingly" |
| B3 | Same, but access authorised | no s 3 offence | s 3(1) |
| B4 | Access (authorised) with intent to commit fraud offence punishable by max 5 years | s 4 offence | s 4(1),(2),(4)(a) |
| B5 | s 4 intended offence: property offence, max imprisonment exactly 2 years | s 4 applies | s 4(2) "not less than 2 years" |
| B6 | s 4 intended offence: dishonesty, max 1 year | s 4 does not apply | s 4(2) |
| B7 | s 4 intended offence: max 10 years but not property/fraud/dishonesty/bodily harm (e.g. a regulatory offence) | s 4 does not apply | s 4(2) |
| B8 | s 4 intended offence: causes bodily harm, max 3 years | s 4 applies | s 4(2) |
| B9 | Act known to cause unauthorised modification | s 5 offence | s 5(1) |
| B10 | Modification is authorised | no s 5 offence | s 5(1), 2(8) |
| B11 | Knowingly secures unauthorised access to obtain computer service | s 6(1)(a) offence | s 6(1)(a) |
| B12 | Knowingly intercepts without authority a function via a device | s 6(1)(b) offence | s 6(1)(b) |
| B13 | Knowingly, without authority or lawful excuse, interrupts lawful use of computer | s 7 offence | s 7(1)(a) |
| B14 | Same but with lawful excuse | no s 7 offence | s 7(1) |
| B15 | Knowingly and without authority discloses password for wrongful gain | s 8 offence | s 8(1)(a) |
| B16 | Discloses knowingly without authority but no wrongful gain, no unlawful purpose, no knowledge of likely wrongful loss | no s 8 offence | s 8(1) |
| B17 | Singpass user discloses own password knowing purpose is to facilitate offence | s 8A offence | s 8A(1) |
| B18 | Non-user (no Singpass account) discloses | no s 8A offence | s 8A(1) "Any user" |
| B19 | User discloses for gain, no actual knowledge found, presumption not rebutted | s 8A offence (presumed reasonable grounds) | s 8A(3)(a) |
| B20 | User discloses for gain but presumption rebutted, no other knowledge | no s 8A offence | s 8A(3) "until the contrary is proved" |
| B21 | User fails reasonable steps to ascertain identity/location; not rebutted | s 8A offence | s 8A(3)(c) |
| B22 | Elements of 8A(1) met, but user had reasonable grounds to believe purpose was a lawful transaction in user's identity | no offence | s 8A(4) |
| B23 | Obtains credential of another for use in committing offence | s 8B(1)(a) offence | s 8B(1)(a), (2) |
| B24 | Obtains credential of another for an innocent purpose | no offence | s 8B(2) |
| B25 | Supplies credential, innocent purpose, and did not know/have reason to believe it would be used for offence | no offence | s 8B(3) |
| B26 | Supplies credential, innocent purpose, but had reason to believe likely use for an offence | s 8B(1)(b) offence | s 8B(3)(b) (both limbs needed) |
| B27 | Network/routing provider merely transmits a credential | no s 8B(1)(b) offence | s 8B(4) |
| B28 | Retains personal info knowing obtained by s 3 contravention, for use in committing offence | s 9(1)(a) offence | s 9(1)(a), (2) |
| B29 | s 9 Example 1: A downloads/retains card list to report to police | no s 9(1)(a) offence | s 9(2), Example 1 |
| B30 | s 9 Example 1: A transmits list to B to inform, no knowledge/reason to believe of misuse | no s 9(1)(b) offence | s 9(3), Example 1 |
| B31 | s 9 Example 2: C transmits to D for B's investigation, no knowledge | no s 9(1)(b) offence | s 9(3), Example 2 |
| B32 | Variant of Example 2: C had reason to believe D would misuse | s 9(1)(b) offence | s 9(3)(b) |
| B33 | Personal info obtained by contravention of s 7 (not 3/4/5/6) | no s 9 offence | s 9(1) "section 3, 4, 5 or 6" |
| B34 | Network provider merely routes personal information | no s 9(1)(b) offence | s 9(4) |
| B35 | Obtains a hacking program intending to commit s 3 offence | s 10(1)(a)(i) offence | s 10(1)(a), (2)(a) |
| B36 | Supplies a password intending it be used for s 8 offence (not 3-7) | no s 10 offence | s 10(1)(b) "3, 4, 5, 6 or 7" |
| B37 | Abets / attempts s 5 offence | guilty of s 5 offence, same punishment | s 12(1) |

## C. Punishment (ss 3-11; caning)

| # | Scenario | Expected max (fine / years / strokes) | Provision |
|---|---|---|---|
| C1 | s 3 first conviction, no damage | $5,000 / 2 / 0 | s 3(1)(a) |
| C2 | s 3 repeat conviction, no damage | $10,000 / 3 | s 3(1)(b) |
| C3 | s 3 first conviction with damage | $50,000 / 7 | s 3(2) |
| C4 | s 3 repeat with damage | $50,000 / 7 | s 3(2) |
| C5 | s 4 first | $50,000 / 10 | s 4(3) |
| C6 | s 4 repeat | $50,000 / 10 (no repeat limb) | s 4(3) |
| C7 | s 5 first | $10,000 / 3 | s 5(1)(a) |
| C8 | s 5 repeat | $20,000 / 5 | s 5(1)(b) |
| C9 | s 6 with damage | $50,000 / 7 | s 6(2) |
| C10 | s 7 repeat | $20,000 / 5 | s 7(1)(d) |
| C11 | s 8 repeat | $20,000 / 5 | s 8(2)(b) |
| C12 | s 8 with "damage" | $10,000 / 3 (first) - no damage limb | s 8(2) |
| C13 | s 8A first, no caning grounds | $10,000 / 3 / 0 | s 8A(1) |
| C14 | s 8A repeat | $10,000 / 3 (no repeat limb) | s 8A(1) |
| C15 | s 8B repeat | $20,000 / 5 | s 8B(5)(b) |
| C16 | s 9 first | $10,000 / 3 | s 9(5)(a) |
| C17 | s 10 repeat | $20,000 / 5 | s 10(3)(b) |
| C18 | s 3 + protected computer (access obtained) | $100,000 / 20 | s 11(1) |
| C19 | s 5 + protected computer, repeat with damage | $100,000 / 20 (in lieu) | s 11(1) |
| C20 | s 4 + protected computer | $50,000 / 10 (s 11 does not cover s 4) | s 11(1) "3, 5, 6 or 7" |
| C21 | s 8 + protected computer | s 8 punishment unchanged | s 11(1) |
| C22 | Protected: accused ought reasonably to have known computer used for banking services | protected | s 11(2)(c) |
| C23 | Computer used for banking but no knowledge found and no warning | not protected | s 11(2) |
| C24 | No knowledge found, but warning of enhanced penalty exhibited, not rebutted | protected (presumed) | s 11(3) |
| C25 | Warning exhibited, presumption rebutted, no knowledge otherwise | not protected | s 11(3) |
| C26 | Computer used for a retail shop only, accused knew | not protected | s 11(2) |
| C27 | s 8A, individual knew purpose was a scam offence | 12 strokes in addition | s 8A(5)(a) |
| C28 | s 8A, used for scam proved, individual cannot prove reasonable steps | 12 strokes | s 8A(5)(b) |
| C29 | s 8A, used for scam proved, individual proves reasonable steps | 0 strokes | s 8A(5)(b)(ii) |
| C30 | s 8A, offender is a company (not individual), knew scam | 0 strokes | s 8A(5) "individual" |
| C31 | s 8B(1)(a), obtained credential for use in scam | 12 strokes | s 8B(5A)(a) |
| C32 | s 8B(1)(a), obtained for use in non-scam offence | 0 strokes | s 8B(5A) |
| C33 | s 8B(1)(b), knew credential would be used for scam | 12 strokes | s 8B(5B)(a) |
| C34 | s 8B(1)(b), used for scam, no reasonable steps proved | 12 strokes | s 8B(5B)(b) |
| C35 | s 3 offence: no caning | 0 strokes | s 3 |

## D. Reach and procedure (ss 13-17)

| # | Scenario | Expected | Provision |
|---|---|---|---|
| D1 | Accused in Singapore at material time, any offence | Act applies | s 13(3)(a) |
| D2 | s 3, accused abroad, computer in Singapore | applies | s 13(3)(b) |
| D3 | s 8, accused abroad, computer in Singapore | applies | s 13(3)(b) |
| D4 | s 9, accused abroad, computer in Singapore, no serious harm | does not apply | s 13(3)(b) excludes s 9 |
| D5 | s 10, accused abroad, computer in Singapore, no serious harm | does not apply | s 13(3)(b) |
| D6 | s 9, accused abroad, serious harm in Singapore | applies | s 13(3)(c) |
| D7 | s 8A, accused abroad, nothing in Singapore | applies | s 13(3)(d) |
| D8 | s 8B, accused abroad | applies | s 13(3)(d) |
| D9 | s 5, accused abroad, computer abroad, no serious harm | does not apply | s 13(3) |
| D10 | Two s 3 acts, same computer, 6 months apart | can amalgamate | s 14(1) |
| D11 | Two s 3 acts, same computer, 1 Jan 2026 and 1 Jan 2027 (exactly 12 months) | can amalgamate ("does not exceed 12 months") | s 14(1)(c) |
| D12 | Two s 3 acts, same computer, 1 Jan 2026 and 2 Jan 2027 | cannot | s 14(1)(c) |
| D13 | One s 3 act and one s 5 act, same computer | cannot | s 14(1)(a) |
| D14 | Two s 3 acts, different computers | cannot | s 14(1)(b) |
| D15 | Only one act | cannot | s 14(1) "2 or more acts" |
| D16 | Amalgamated charge counts as | one offence | s 14(3) |
| D17 | Can a District Court hear s 11 offence and impose full $100,000 / 20 years | yes | s 15 |
| D18 | Magistrate's Court hear any CMA offence | yes, full penalty | s 15 |
| D19 | Compound prescribed offence for $3,000 | allowed | s 16(1) |
| D20 | Compound prescribed offence for $3,001 | not allowed | s 16(1) |
| D21 | Compound offence not prescribed | not allowed | s 16(1) |
| D22 | Civil claim $20,000; compensation paid $8,000 | claim deemed satisfied to $8,000; $12,000 remains recoverable | s 17(2) |
| D23 | Claim $5,000, compensation $8,000 | nothing remains (0) | s 17(2) |
| D24 | Arrest without warrant on reasonable suspicion | allowed | s 19 |

## E. Vintage gate

| # | Scenario | Expected | Provision |
|---|---|---|---|
| E1 | Conduct on 29 Dec 2025, any question | REFUSE | BRIEF vintage; Act 21 of 2025 wef 30/12/2025 |
| E2 | Conduct on 30 Dec 2025 | answered normally | same |
| E3 | Conduct in 2020 | REFUSE | same |
