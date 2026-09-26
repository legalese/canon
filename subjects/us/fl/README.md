# florida/

Florida (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Online Sunshine — The Florida Legislature, The 2026 Florida Statutes; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Plain HTTP/HTTPS GETs with an honest UA, about 10 requests spaced ~1.8 s apart. No block, challenge or rate limit. The site is plain server-rendered ColdFusion; chapter pages are addressed as index.cfm?App_mode=Display_Statute&URL=<range>/<chapter>/<chapter>.html. Every chapter page is headed 'The 2026 Florida Statutes', which is the currency marker; the site offers a year selector back to 1997.

## Topics with no legislation here

- **Leave/holiday pay**: No general state statute. Florida mandates no annual leave, sick leave, family leave or holiday pay, and § 218.077 and § 448.077 preempt local ordinances on employment benefits. The only statutory leave mandate is three days of domestic-violence leave under Fla. Stat. § 741.313, which is too narrow to stand as the principal statute for the topic. Family and medical leave generally is federal (FMLA, 29 U.S.C. ch. 28).
- **Termination/severance**: No state statute. Florida is an at-will state with no severance entitlement and no mini-WARN Act. Mass-layoff notice is federal: WARN Act, 29 U.S.C. § 2101 et seq. The statutory consequence of job loss is reemployment assistance under Fla. Stat. ch. 443.
- **Personal tax/withholding**: No such tax exists. Florida levies no personal income tax and the state constitution forbids one without an amendment (Fla. Const. art. VII, § 5(a)), so there is no state withholding regime. Personal income tax and wage withholding are federal (26 U.S.C. §§ 1, 3401-3406).
- **Passenger compensation**: No state statute. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250).
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Florida's own immigration provisions (Fla. Stat. § 448.095, mandatory E-Verify) enforce the federal scheme rather than conferring permission to work.
