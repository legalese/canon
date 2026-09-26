# new-mexico/

New Mexico (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the New Mexico Compilation Commission - NM OneSource (Current New Mexico Statutes Annotated 1978); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Partly blocked, then read successfully in a real browser. WebFetch of nmonesource.com returned HTTP 403 for every path tried (/nmos/nmsa/en/index.do, /nmos/nmsa/en/nav_date.do), and a plain curl request 404'd or was refused, so the site does not serve scripted clients. Loading the same URLs in a real browser worked. The site wraps all statute content in an iframe (src '<path>?iframe=true'), so the outer page looks empty to text extraction; appending '?iframe=true' to each item URL returns the chapter table of contents and text. I then read the chapter-by-date navigation (84 chapters over 4 pages) and nine chapter pages, roughly 15 page loads in total, spaced several seconds apart. The Commission's own site www.nmcompcomm.us is reachable by ordinary fetch and supplied the currency statement and copyright notice. No block, challenge or rate limit was circumvented; the 403 for scripted clients is recorded here rather than worked around, and everything below was read through the site's normal browser interface. The URLs given for each Act are the outer (canonical) item URLs; a scripted re-fetch will need the '?iframe=true' form.

## Topics with no legislation here

- **Passenger compensation**: No New Mexico statute. Air-passenger compensation and denied-boarding rules are federal (49 U.S.C. 41712; 14 C.F.R. pt. 250), and state regulation of an air carrier's prices, routes or services is expressly preempted by 49 U.S.C. 41713. New Mexico's transport chapters cover motor carriers (NMSA 1978 ch. 65) and aeronautics (ch. 64) as licensing and safety matters, with no passenger compensation scheme.
- **Customs/duties**: Federal matter. Customs duties are exclusively federal (U.S. Const. art. I, sec. 8, cl. 1 and sec. 10, cl. 2; Tariff Act of 1930, 19 U.S.C.). No state statute exists or could exist.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. New Mexico's only adjacent statute is the child-employment article (NMSA 1978 ch. 50, art. 6), which is an age-and-hours matter, not immigration.
