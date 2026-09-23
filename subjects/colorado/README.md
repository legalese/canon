# colorado/

Colorado (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Colorado Legal Resources - Colorado Revised Statutes Annotated (LexisNexis, under contract to the Committee on Legal Services of the Colorado General Assembly); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

The General Assembly hosts no statute text: https://leg.colorado.gov/colorado-revised-statutes (which redirects to /laws/colorado-revised-statutes) carries one line - 'Click here to access the Colorado Revised Statutes hosted by LexisNexis' - pointing to www.lexisnexis.com/hottopics/colorado/. The Office of Legislative Legal Services' own CRS page at content.leg.colorado.gov returned HTTP 403 Forbidden both to a plain fetch and to a real browser, so it could not be read. I loaded the Lexis 'Colorado Legal Resources' public-access container in a real browser (Claude's browser pane, ordinary Chrome, no user-agent spoofing) and expanded the official table of contents there - about 14 node expansions, several seconds apart; no CAPTCHA appeared on this container, but I had already hit one on the sibling Arkansas container when opening an individual section, so I stayed at table-of-contents level and opened no section documents. Consequence: Colorado entries are verified from the official CRS Annotated table of contents (title/article/part captions and the section ranges it prints), without a 'current through' date - the container shows none.

## Topics with no legislation here

- **Termination/severance**: Employment is at will by common law and Colorado has no severance entitlement and no state mini-WARN Act - plant-closing and mass-layoff notice is federal (WARN Act, 29 U.S.C. s 2101 et seq.). The termination-adjacent duties are inside the Colorado Wage Act already listed under Payroll/wages (final pay on separation, C.R.S. s 8-4-109), so no separate statute is recorded.
- **Passenger compensation**: Federal. Air passenger rights come from US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Colorado regulates motor carriers and transportation network companies under Title 40, arts. 10 - 17.5, but provides no passenger compensation scheme.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.
- **Work permits/immigration**: Federal. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. (employer verification at 8 U.S.C. s 1324a). Colorado repealed its own employment-verification affirmation requirement (former C.R.S. s 8-2-122) in 2016 and imposes no E-Verify duty. What remains in the Code is eligibility verification for public benefits (Title 24, 'Restrictions on Public Benefits (Arts. 76.5 - 76.7)'), which is not a work-permit regime.
