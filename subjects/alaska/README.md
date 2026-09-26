# alaska/

Alaska (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Alaska State Legislature, BASIS - Alaska Statutes (Legislative Affairs Agency); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Scripted fetching is blocked: a plain HTTP fetch of https://www.akleg.gov/basis/statutes.asp returns 403 Forbidden, and the old host www.legis.state.ak.us now fails TLS (certificate covers only akleg.gov). I did not try to defeat the 403; instead I opened the same public page in a real browser (Claude's browser pane, ordinary Chrome, no user-agent spoofing), where it loads normally with the page title 'Alaska Statutes 2025'. Title and chapter contents are delivered by the site's own endpoint statutes.asp?media=js&type=TOC&title=<n>, which the page itself calls; I requested about 16 of those from inside the loaded page, spaced ~1.7 seconds apart. One transient 522 (Cloudflare origin timeout) on http://akleg.gov/disclaimer.php; the https URL served it. No CAPTCHA was encountered. The statutes pages carry no copyright notice and no 'current through' line beyond the 'Alaska Statutes 2025' page title.

## Topics with no legislation here

- **Personal tax/withholding**: Alaska levies no individual income tax, so there is no personal tax or wage-withholding statute. Verified on the register: the Title 43 chapter table of contents for AS 43.20 ('Alaska Net Income Tax Act') shows 'Sec. 43.20.010. Tax on individuals, fiduciaries, and corporations. [Repealed, s 13 ch 70 SLA 1975.]', with the live charging section being 43.20.011 'Tax on corporations'; the individual credit and exemption provisions 43.20.015 and 43.20.017 are also flagged '[Repealed, s 10 ch 1 SSSLA 1980.]'. Personal income tax and wage withholding are therefore federal only (Internal Revenue Code, 26 U.S.C., withholding at 26 U.S.C. s 3402).
- **Passenger compensation**: Federal. Air passenger rights are US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Alaska regulates ferry and motor-carrier operations (AS 42.25 Alaska Ferry Transportation Act, AS 42.10) but has no passenger compensation scheme.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.
- **Work permits/immigration**: Federal. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. (employment verification at 8 U.S.C. s 1324a). Alaska has no E-Verify or work-authorisation statute; AS 23.05.125 establishes only an 'Office of citizenship assistance' within the labour department, which is assistance rather than regulation of work permits.
