# arkansas/

Arkansas (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Arkansas Code Annotated - Code of Arkansas Public Access (LexisNexis, for the Arkansas Bureau of Legislative Research / Arkansas Code Revision Commission); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Arkansas publishes no code text of its own: arkleg.state.ar.us links out to a LexisNexis-hosted 'Code of Arkansas Public Access' site, and www.lexisnexis.com/hottopics/arcode/Default.asp 301-redirects to advance.lexis.com. https://arkleg.state.ar.us/Home/ArkansasCode returned HTTP 500 and advance.lexis.com is a JavaScript application, so I opened the public-access container in a real browser (Claude's browser pane, ordinary Chrome, no user-agent spoofing) and expanded the official table of contents there - about 10 node expansions, each several seconds apart. IMPORTANT: when I clicked through from the table of contents to an individual section document, the site served a 'Captcha Validation' page. I stopped immediately, did not attempt the challenge, and made no further document requests. Consequence: every Arkansas entry below is verified at table-of-contents level on the official public-access edition (chapter and subchapter captions, and Lexis's '[Repealed.]' markers), and I could not read the 'current through' currency statement or any individual section.

## Topics with no legislation here

- **Leave/holiday pay**: No state statute. Arkansas mandates no paid or unpaid annual leave, holiday pay or sick leave for private employers; the Title 11 chapter list on the register shows no leave chapter. Job-protected family and medical leave is federal (FMLA, 29 U.S.C. s 2601 et seq.).
- **Termination/severance**: Employment is at will by common law; there is no statutory notice period, severance entitlement or state mini-WARN Act (plant-closing notice is federal, 29 U.S.C. s 2101 et seq.). The only termination-adjacent statute is the final-wages rule inside Title 11, ch. 4, subch. 4 (Payment of Wages), already listed under Payroll/wages.
- **Passenger compensation**: Federal. Air passenger rights come from US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Arkansas's carrier chapters (Title 23, subtit. 1, ch. 10 'Transportation Of Passengers And Freight Generally', ch. 13 Motor Carriers) regulate carriage but provide no passenger compensation scheme.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.
- **Work permits/immigration**: Federal. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. (employer verification at 8 U.S.C. s 1324a). Arkansas imposes no general E-Verify duty on private employers; its verification requirements are procurement conditions on state contractors (Title 19, Public Finance), not a work-permit regime.
