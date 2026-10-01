# NOTES — AI-content labelling across the EU, Washington and California

Read this before relying on any module or any cell of `CENSUS.md`.
The brief the encoding was written to is `BRIEF.md`.

## 1. What is encoded, and what is not

Three regimes answer one question about one piece of content: must it be marked or disclosed, by whom, and is the marking it carries enough?

- **EU.** Regulation (EU) 2024/1689, Art. 50(2) (providers must ensure output is marked) and Art. 50(4) (deployers must disclose deep fakes and public-interest text), with Art. 3(3), 3(4) and 3(60), the application date in Art. 113, and the transitional period that Regulation (EU) 2026/1744 added as Art. 111(4).
  Beside it, Measure 1.1 of the voluntary Code of Practice (final, 10 June 2026): at least two layers, signed metadata and an imperceptible watermark, with two single-layer cases.
- **Washington.** E2SHB 1170, ch. 167, Laws of 2026: ss. 1, 2, 3(2), 5 and 9. Covered providers must include provenance data in AI-created or materially altered image, video or audio, from 1 February 2027; a C2PA manifest is deemed to meet the hard-to-remove requirement.
- **California.** Bus. & Prof. Code ch. 25 **as amended by SB 1000** (approved 30 September 2026): 22757.1, 22757.3(a), 22757.5, 22757.6, and 22757.3.1 (AB 853's text, which SB 1000 does not amend). Covered providers must include a latent disclosure conveying five items; from 1 January 2027 large platforms must show users what provenance data says.

Not encoded: EU Art. 50(1), (3), (5), (6), the rest of the Code (including Section 2's "AI" icon), and penalties; Washington ss. 3(1), 4, 6, 7, 8; California 22757.2, 22757.3(b)–(d), 22757.3.2, 22757.3.3, 22757.4 and 22757.4.1.
**The California text in force from 2 August to 29 September 2026** (SB 942 as amended by AB 853, with a 1,000,000-user threshold and a manifest-disclosure option) **is not encoded**: any question dated in that window refuses, naming it.

## 2. Coverage table

| provision | heading | disposition |
| --- | --- | --- |
| EU Art. 3(3) | "provider" | encoded as the `the provider of the AI system` record; not computed |
| EU Art. 3(4) | "deployer" | encoded: `the publisher is a deployer` |
| EU Art. 3(60) | "deep fake" | encoded: `the content is a deep fake`; "would falsely appear ... authentic" is an input |
| EU Art. 50(1) | AI interacting with persons | out-of-scope: a disclosure about interaction, not about content |
| EU Art. 50(2) | marking of synthetic output | encoded; both exceptions inputs; law-enforcement limb encoded |
| EU Art. 50(3) | emotion recognition, biometric categorisation | out-of-scope: not about generated content |
| EU Art. 50(4) 1st subpara | deep fakes | encoded, including the artistic limb's limited disclosure |
| EU Art. 50(4) 2nd subpara | public-interest text | encoded, including the review-and-responsibility exception |
| EU Art. 50(5) | manner and timing of disclosure | out-of-scope: governs how a disclosure is made, not whether one is owed |
| EU Art. 50(6) | relation to Chapter III | inert: a saving provision |
| EU Art. 50(7) as replaced by 2026/1744 | codes of practice, adequacy | inert: context for why the Code is encoded; no rule reads it |
| EU Art. 111(4) as added by 2026/1744 | transitional period for 50(2) | encoded; fork F1 |
| EU Art. 113 | application | encoded |
| Code, Measure 1.1 | at least two layers; single-layer cases | encoded; fork F4 |
| Code, Sub-measure 1.1.1 | signed metadata | encoded; a manifest with no time refuses (fork F11) |
| Code, Sub-measure 1.1.2 | imperceptible watermark | encoded |
| Code, 1.1.3, 1.2–1.4, Commitments 2–4, Section 2 | the rest of the Code | out-of-scope by the brief |
| WA s.1(1) | "artificial intelligence" | inert: no rule turns on it |
| WA s.1(2) | "covered provider" | encoded |
| WA s.1(3) | "generative artificial intelligence" | encoded as the image/audio/video scope |
| WA s.1(4) | "provenance data" | encoded, read as a C2PA manifest |
| WA s.2(1) | duty to include provenance data | encoded; "commercially and technically reasonable" is an input |
| WA s.2(2) | difficult to remove; C2PA safe harbour | encoded as "deemed compliant"; watermark-only refuses |
| WA s.2(3) | no personal information required | inert: relieves, never imposes; no answer here turns on it |
| WA s.2(4) | "materially altered"; the open list | encoded; the significant-change judgement is an input |
| WA s.3(1) | trade secrets | out-of-scope by the brief |
| WA s.3(2) | business-to-business | encoded |
| WA s.4 | enforcement | out-of-scope by the brief |
| WA s.5(1), (2) | video games and interactive experiences; upscaling, noise reduction, compression systems | encoded; fork F13 |
| WA s.6 | government agencies' AI disclosure | out-of-scope: a different duty |
| WA ss.7, 8 | codification | inert |
| WA s.9 | effective date | encoded |
| CA 22757.1(e) | "covered provider" | encoded; a government provider refuses (fork F15) |
| CA 22757.1(i) | "large online platform" | encoded |
| CA 22757.1(l) | "minor modification", closed list | encoded |
| CA 22757.1(n), (o) | "provenance data", "system provenance data" | encoded as a C2PA manifest; fork F7 |
| CA 22757.1, other definitions | AI, assistive technology, capture device, etc. | inert: no rule here reads them |
| CA 22757.2 | disclosure verification tool | out-of-scope by the brief; (a)(3) reads compatibility as an input |
| CA 22757.3(a) | latent disclosure, (1)(A)–(E), (2), (3), (4) | encoded; (F) refuses from 2029; (2) is an input; forks F6, F8 |
| CA 22757.3(b)–(d) | licensees; assistive-technology misrepresentation | out-of-scope by the brief |
| CA 22757.3.1(a)(1) | detect provenance data | encoded as implied by (a)(2): what is shown is what is detected |
| CA 22757.3.1(a)(2) | what the interface must make available | encoded; (iii) read as "present" (fork F16) |
| CA 22757.3.1(a)(3) | let users inspect | out-of-scope: a duty of means, not of what is shown |
| CA 22757.3.1(b) | must not strip | out-of-scope: a prohibition on platform conduct that no census fact engages |
| CA 22757.3.1(c) | operative 1 January 2027 | encoded |
| CA 22757.3.2, 22757.3.3 | hosting platforms; capture devices | out-of-scope by the brief |
| CA 22757.4, 22757.4.1 | penalties | out-of-scope by the brief |
| CA 22757.5 | videogames; assistive technology before 2029 | encoded |
| CA 22757.6 | operative 2 August 2026 | encoded |
| CA 22757.1/.3/.5, text of 2 Aug – 29 Sep 2026 | the superseded vintage | refuses, by the brief |

No row is `deferred`.

## 3. The judgements, and why they are inputs

Each of these is a place where an instrument hands the question to someone. The modules take each as a `BOOLEAN` named in the instrument's own words and never compute it.

| regime | input | source |
| --- | --- | --- |
| EU | the AI system performs an assistive function for standard editing | Art. 50(2) |
| EU | the AI system does not substantially alter the input data ... or the semantics thereof | Art. 50(2); the Guidelines, para 91: "requires a case-specific assessment" |
| EU | the content would falsely appear to a person to be authentic or truthful | Art. 3(60) |
| EU | the content forms part of an evidently artistic, creative, satirical, fictional or analogous work or programme | Art. 50(4) |
| WA | the alteration is a significant change that substantially alters the data in content | s.2(4), asked only of alterations off the list |
| WA | including provenance data is commercially and technically reasonable | s.2(1) |
| CA | including a latent disclosure is technically feasible | 22757.3(a) |
| CA | the disclosure is permanent or extraordinarily difficult to remove or tamper with | 22757.3(a)(2) |

**This is the census's most important structural finding.** California's minor-modification list is closed ("means any of the following"), so an AI alteration either is on it or triggers the duty, with no judgement anywhere.
Washington's is open ("Minor modifications include:"), and adds "applying filters" and "resampling".
The EU has no list at all: the Commission's Guidelines give examples on both sides and call the question case-specific.
So the same edit can be a bright-line yes in California, a listed no in Washington, and a judgement in the EU.

## 4. Fork register

| fork | where | readings | taken, and why |
| --- | --- | --- | --- |
| F1 | EU Art. 111(4) | (a) for a system on the market before 2 Aug 2026, 50(2) compliance is not owed before 2 Dec 2026; (b) 50(2) applies from 2 Aug 2026 and 111(4) only defers enforcement | (a): "shall take the necessary steps in order to comply with Article 50(2) by 2 December 2026" sets the date compliance is due; recital: "a transitional period of four months" |
| F2 | EU Art. 50(4) | the artistic limb ("the transparency obligations set out in this paragraph are limited ...") reaches (a) only deep fakes, or (b) public-interest text too | (a): the limb sits inside the first subparagraph and speaks of "the display or enjoyment of the work"; (b) is open on the words "this paragraph" |
| F3 | CA 22757.1(l)(4) and WA s.2(4) | California's "File resizing" means (a) changing an image's dimensions, as Washington's "resizing", or (b) changing a file's size in bytes | (a): both lists pair it with "scaling" and "cropping"; one domain constructor, `resizing`, serves both |
| F4 | Code, Sub-measure 1.1.2 | very short free-form text is excepted from watermarking and free-form text cannot carry metadata, so Measure 1.1 asks (a) nothing of it, or (b) something unstated | (a), the literal text; "very short" is undefined (the Code says watermarking still applies above 200 tokens), so it is an input |
| F5 | CA (l)(5) and WA s.5(2) | AI upscaling is (a) "scaling", or (b) generative super-resolution that creates new detail, so not on California's list | (a); no separate `upscaling` alteration exists in the domain. Washington's s.5(2) separately excludes systems "used solely for upscaling" |
| F6 | CA 22757.3(a) | SB 1000's 22757.1 no longer defines "latent" (SB 942's did), so "latent disclosure" takes (a) its ordinary meaning, or (b) the repealed definition | (a); a C2PA manifest is taken as a latent disclosure, and as "compliant or interoperable with widely recognized industry standards" under (a)(4) |
| F7 | CA 22757.3.1(a)(2) | (ii) "the name of the GenAI system or capture device that created or substantially altered the content": "substantially altered" here is a different test from 22757.3's "altered, except by minor modification" | the name is read off the manifest's generator where it declares a capture or a generative source type; a manifest declaring only "algorithmically enhanced" names nothing under (ii) |
| F8 | CA 22757.3(a)(1)(E) | a manifest declaring "algorithmically enhanced" (a) does not, or (b) does convey "whether the GenAI system created or altered the content" | (a): the IPTC term describes an algorithm, not a generative system; this decides scenario S04's (E) |
| F9 | CA 22757.3(a)(2) | whether a C2PA manifest alone is "permanent or extraordinarily difficult to remove" | an INPUT; the census supposes manifest only = removable (platforms strip metadata), manifest bound to a watermark = permanent. This decides the census's California "meets the section" column |
| F10 | WA s.1(2); CA 22757.1(i) | "over 1,000,000 monthly users" and "exceeded 2,000,000 unique monthly users during the preceding 12 months" do not say how users are counted, or over which month | taken as numbers the caller supplies; the encoding does not choose the measure |
| F11 | Code, Sub-measure 1.1.1 | "time-stamped (on systems where time information is available)": a manifest with no time | refuses: whether time was available is not a fact held. Every fixture is time-stamped, so no census cell reaches it |
| F12 | EU Art. 50(2) | "to the extent" the system performs standard editing suggests a partial answer for content edited in several ways | one judgement per piece of content |
| F13 | WA s.5(1) | "interactive experiences including ... the sale of goods or services directly to consumers through the internet" appears to exclude e-commerce sites from the whole chapter | encoded as written, as a provider fact; noted because the scope is wider than "video games" suggests |
| F14 | WA s.2(2) | a watermark alone, without C2PA metadata, may be "a commonly supported technical standard for watermarking" | refuses: whether a given watermark follows such a standard is not a fact held |
| F15 | CA 22757.1(e) | "Covered provider" means "a person that creates ..."; whether a state, local, or tribal government is a "person" | refuses: nothing in the sources encoded defines "person". Raised by the independent test pass (W-04 to W-06); the encoding first answered yes |
| F16 | CA 22757.3.1(a)(2)(B)(iii) | "Whether any digital signatures are available" means (a) a signature is present, or (b) a valid one is | (a), the literal word "available"; a C2PA manifest is always signed, so (iii) is yes whenever a manifest is present. The independent test author read (b); its assertion (P-19) is kept, failing, as the visible alternative |

## 5. The census

`CENSUS.md` is generated by `census.py` and lists twelve scenarios on two dates. On **1 February 2027**, when all three regimes are in force, they disagree on whether the provider must mark the content in five:

- **S03, a stylistic filter by a generative model:** EU yes (on the judgement that a style change is beyond standard editing), Washington no ("applying filters" is on its list), California yes (it is not on California's).
- **S04, red-eye removed by an AI system:** EU no (the Guidelines' own example of standard editing), Washington no (judged not a significant change), California yes (red-eye removal is not on the closed list).
- **S09, a provider with 500,000 monthly users:** EU yes, Washington no ("over 1,000,000"), California yes (SB 1000 removed the threshold).
- **S10, an AI-written news article:** EU yes (Art. 50(2) reaches text, and 50(4) requires disclosure of unreviewed public-interest text), Washington and California no (image, video and audio only).
- **S11, a business-to-business system:** EU yes, Washington no (s.3(2)), California yes.

**Where they agree that marking is owed, they disagree on whether the marking is enough.** For an AI-generated image carrying only a signed C2PA manifest (S06), the EU Code is not met (one layer of two), Washington deems it compliant (the safe harbour), and California's answer turns on the permanence judgement (fork F9).
Only S07, a manifest bound to a watermark, satisfies all three.

Every judgement each scenario supposes is set out in `census.l4`, beside the scenario.
Where the Commission's Guidelines give an example on point, the EU judgement follows it and says so; otherwise it is a supposition, and changing it changes the cell.

## 6. Independent test pass

A fresh session was given `BRIEF.md` and the sources, and nothing else.
It wrote its expected answers to 129 scenarios, with 36 ambiguities, before any module of this encoding existed to read.
Only then did it open the modules, for their names and record shapes, and write `tests-independent.l4`: 864 assertions over 127 scenarios.
It did not read `tests-*.l4`, `census.l4`, `CENSUS.md` or this file, and changed no expected value after seeing the encoding.

**First run: 852 passed, 12 did not.** Each was checked against the source:

| finding | scenarios | resolution |
| --- | --- | --- |
| In the 2 August – 29 September 2026 window, `the items in 22757.3(a)(1) the disclosure does not convey` answered with SB 1000's list, which added item (E); the duty question already refused there | ED-2, ED-5, ED-6, C-15, P-17, X-04 (6) | **encoding error**, fixed: the item list now refuses in the window. A number from the amended text was answering for the original. |
| A state agency, county or tribal government was treated as a California "covered provider" | W-04, W-05, W-06 (3) | **encoding error**, fixed: refuses, fork F15. My own `tests-ca.l4` had asserted yes; that was a test written from the code's reading, not the source's, and it now asserts the refusal. |
| From 1 January 2029 the item list refused outright because (F) is not modelled, so the brief's question about (A)–(E) could not be answered | C-03, C-17 (2) | **encoding error**, fixed: (A)–(E) are always answered; the (F) refusal moved to `the content's latent disclosure meets 22757.3(a)`. My test asserting the list refused was changed to match, and says so. |
| (iii) "whether any digital signatures are available" is yes for a manifest whose signature does not validate | P-19 (1) | **genuine ambiguity**, fork F16: kept failing, by design. The test author approximated unsigned metadata as a manifest whose signature fails; the domain has no way to say "unsigned". |

**Second run: 863 passed, 1 failed (P-19, expected), 0 refused.**

**The harness finding.** The test author also found that the skill's own `check.sh` undercounts.
A `#ASSERT REFUSED` whose expression produces a value prints "assertion failed: …" on the line *after* `Message:`, which the skill's grep misses, so 9 of the 12 showed as errors but not as failures.
An `#ASSERT` whose expression refuses prints "assertion refused" at Warning severity, which the skill's script counts nowhere at all, so a refusing assertion looks green.
This row's `check.sh` reads the line after every `Message:` and adds a `refused` column; section 8 has the positive control.
The skill's asset in `legalese/l4-ide` (`skills/encoding-a-subject/assets/check.sh`, mirrored in `legalese/l4-plugin`) still has the defect.

**What the test author could not express with this encoding's names**, each a limit of the domain rather than a wrong answer:

- a 22757.3(a)(1) item conveyed "through a link to a permanent internet website" (C-10, C-11);
- a manifest whose signing time and stated creation time differ: one field, `the time it records`, serves both the Code's 1.1.1 time-stamp and California's item (C) (M-05, M-06, C-06);
- a manifest that records the content is AI-generated without saying whether created or altered: California's (E) and the Code's 1.1.1 read the same fields (C-08);
- an image in a format that cannot carry metadata, for which the test author expected the Code to refuse (M-20);
- whether a watermark follows "a commonly supported technical standard" under Washington s.2(2); the module refuses (fork F14) where the test author would have taken it as a supplied fact (M-02, M-20, W-14, P-03);
- unsigned IPTC or XMP metadata, which California's "provenance data" may reach (22757.1(n) asks only for a format "compliant, or interoperable with, widely adopted specifications"); this domain models provenance data as a C2PA manifest only (M-04, P-19).

Every contested reading the encoding could express agreed with the test author's: Washington's listed items stay minor whatever the judgement; image denoising is minor in California; the artistic limit does not reach text (fork F2); a system put into service but not placed on the market gets no transition; very short text with no watermark meets Measure 1.1 (fork F4); before 2 August 2026 California answers no rather than refusing; and Washington, unlike California, exempts user-generated video games and virtual shopping.

## 7. Language findings

Three things about L4 this encoding ran into. All were measured on the binary named in section 8.

- **`JSONDECODE` and `§` headings (smucclaw/l4-ide#947, open).** An enum declared under a `§` heading decodes from JSON as a plain string, and the record that holds it then fails comparison ("assertion could not be evaluated"). `labelling-domain.l4` therefore has no `§` headings, and says so at its top: its records are what a caller sends as JSON over REST or MCP. Measured both ways on 2026-10-01: the same JSON decoded into the same record succeeds without the headings and fails with them.
- **An inline `JSONDECODE` silently returns `RIGHT OF NOTHING`.** `#EVAL JSONDECODE "<json>"`, or a `JSONDECODE` whose type is fixed only by comparing it to a typed value, decodes nothing and reports success. The same JSON in a definition with `GIVETH AN EITHER STRING <type>` decodes correctly. `fixture-manifests.l4` uses the typed form, and its seven round-trip assertions are the guard. No issue was found for this; it is a candidate to file.
- **An imported mixfix that ends in a keyword cannot be called.** A function defined as `` `the generator with` users `monthly users` `` works in its own module, but a call from an importing module fails with "expects 1 input, but here it is given 2". The test kit uses a prefix form instead.

Smaller syntax notes, all loud: in a one-line `GIVEN`, `x IS A LIST OF T, y IS A U` reads `T, y` as type arguments (put each input on its own line); a mixfix keyword may not share a name with the input it labels; `#ASSERT … BECAUSE` may continue onto a second line but `#ASSERT … EQUALS` may not.

## 8. What `check.sh` prints

Run on 2026-10-01 with `~/.local/bin/l4`, a build of l4-ide `unstable` installed on 2026-09-30, after the last change to the language (2026-09-28); `JL4_LIBRARY_PATH` unset. The exact commit of that build was not recorded.
Canon has no CI, so these numbers are a point-in-time record.

```
module                      errors satisfied  failed  refused  expected
ca-bpc-22757.l4                  0         0       0        0         0
census-cells.l4                  0         0       0        0         0
census.l4                        0         0       0        0         0
eu-ai-act-art50.l4               0         0       0        0         0
eu-code-of-practice.l4           0         0       0        0         0
fixture-manifests.l4             0         7       0        0         0
labelling-domain.l4              0         0       0        0         0
test-kit.l4                      0         0       0        0         0
tests-ca.l4                      0        54       0        0         0
tests-eu.l4                      0        37       0        0         0
tests-independent.l4             1       863       1        0         1
tests-wa.l4                      0        36       0        0         0
wa-e2shb-1170.l4                 0         0       0        0         0
TOTAL (13 modules)               1       997       1        0
(a failed assertion is also an error; any error that is not a failed assertion, or any refused assertion, makes the run red)
exit=0
```

The one failure is expected: `tests-independent.l4`, scenario P-19, fork F16.

**Positive controls, both run in a scratch copy, never in this row:**

- One expected value in `tests-wa.l4` flipped (applying a filter, "not required" to "required"): `check.sh` reported 1 failed and went red.
- One `#ASSERT REFUSED` over an expression that produces a value, and one `#ASSERT` over an expression that refuses, appended to `tests-wa.l4`: this row's `check.sh` reported `failed 1, refused 1` and went red; the skill's original `check.sh`, on the same files, reported `failed 0` for that module. It went red only because the first failure also raises an error. A refused assertion alone raises neither an error nor a counted failure, so by the original script's own exit test (zero errors and zero failed) it would pass; that is read from the script, not run separately.
