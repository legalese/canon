# north-dakota/

North Dakota (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the North Dakota Legislative Branch - North Dakota Century Code (North Dakota Legislative Council); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fully accessible. Plain HTTPS GET with the honest user agent 'canon-index-builder/1.0 (+https://github.com/legalese/canon)' worked with no challenge, no rate limiting and no block. Structure discovered by probing: /cencode/tNN.html is a per-title chapter index (chapter number, chapter name, and a '[Repealed]' marker where applicable) and /cencode/tNNcCC.html is a per-chapter section index; the actual statute text is served only as /cencode/tNNcCC.pdf, which was deliberately never downloaded. Titles with a decimal use a hyphen in the path (Title 26.1 is /cencode/t26-1.html; /cencode/t261.html is a 404), and decimal chapters likewise (Chapter 54-52.4 is /cencode/t54c52-4.html). Note that /cencode/ itself returns a ~46 MB response; it was not retrieved beyond a HEAD-style size check. About 30 requests in total, spaced 2 s apart. Verification used only the register's own chapter and section index pages plus the Century Code landing page and the site's disclaimer page.

## Topics with no legislation here

- **Passenger compensation**: No state statute. Compensation for denied boarding, delay and cancellation is federal: 14 C.F.R. part 250 and 49 U.S.C. ch. 417 for air, 49 U.S.C. for rail. Title 49 of the Century Code regulates rail and pipeline carriers for safety and rates, and its motor carrier chapter 49-18 is marked [Repealed] on the register's own index; no chapter creates a passenger compensation entitlement.
- **Customs/duties**: Federal matter. Customs duties and tariffs are exclusively federal (Tariff Act of 1930, 19 U.S.C.); U.S. Const. art. I, sec. 10, cl. 2 bars states from laying imposts or duties on imports or exports.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C., and I-9 verification by 8 U.S.C. sec. 1324a. The Century Code has no immigration or work-permit chapter; the nearest state provision is ch. 34-15 (Directory of New Hires), which is a child-support reporting register, not a work-authorisation scheme.
