# mississippi/

Mississippi (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Mississippi Code of 1972 Annotated - 'Mississippi Code Public Access', hosted on LexisNexis Advance for the Joint Legislative Committee on Compilation, Revision and Publication of Legislation (linked as the code source by both the Mississippi Legislature and the Secretary of State); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Mississippi has no state-run consolidated code website. The Legislature's own site (https://www.legislature.ms.gov/) carries only bill/measure search; its single code link points off-site to http://www.lexisnexis.com/hottopics/mscode/, which redirects to the LexisNexis Advance 'Mississippi Code Public Access' container. Scripted access is impossible: curl of the redirect target returns a JavaScript 'cookiesrequired' bounce, and https://www.sos.ms.gov/publications-external-affairs/mississippi-law returns HTTP 403 to curl (it was readable through the Claude WebFetch tool). Verification was therefore done in a real interactive Chrome browser on the public-access platform, with no sign-in: about 4 page loads plus 2 searches. IMPORTANT: when I clicked through from the search-results list to a full document view, the platform served a 'Captcha Validation' page ('We use CAPTCHA on this site to prevent automated software from overburdening the system...'). I stopped there and did not attempt, solve or work around the CAPTCHA, so no full document page was opened and no per-document 'current through <session>' currency statement could be captured. Everything recorded below comes from the code's own live table of contents and search-result headers on that platform, seen before the challenge.

## Topics with no legislation here

- **Termination/severance**: No Mississippi statute. Employment is at will and there is no state wrongful-discharge, notice or severance-pay statute; mass-layoff notice is federal (WARN Act, 29 U.S.C. ch. 23). The consequences of termination for pay purposes fall under Title 71, ch. 1 (listed under Payroll/wages).
- **Passenger compensation**: No state statute. Air passenger rights are federal (49 U.S.C. 41712; DOT denied-boarding rules, 14 C.F.R. pt. 250); intercity rail is Amtrak under federal law. Title 77 regulates carriers but confers no passenger compensation.
- **Customs/duties**: Federal matter, not state: Tariff Act of 1930 and the Harmonized Tariff Schedule, 19 U.S.C.
- **Work permits/immigration**: Federal matter, not state: Immigration and Nationality Act, 8 U.S.C. ch. 12; employment authorisation and verification at 8 U.S.C. 1324a. Mississippi's own contribution is an E-Verify mandate (Mississippi Employment Protection Act, Title 71, ch. 11), which enforces federal status rules rather than conferring work permits; it was not separately verified before the CAPTCHA stopped further checks.
