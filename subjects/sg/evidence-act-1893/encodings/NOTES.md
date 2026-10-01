# Evidence Act 1893 — encoding notes

Row `legalese-aswathy`. Status `draft`. **No domain expert has read this against the source, and no independent test pass has been run** (section 7).

## 1. What is encoded and what is not

The Evidence Act 1893 as printed in Singapore Statutes Online's PDF, current version as at 01 Oct 2026: Parts 1 to 4, section 177 and the First and Second Schedules. **Not encoded: ss 117 to 119 (estoppel)** — a gap in coverage, not a judgement that they are irrelevant. The Act has no single "goal per section"; the rules are organised by the evidentiary question they answer.

| module | the question | covers |
| --- | --- | --- |
| `ea-types.l4` | — | every noun (DECLARE only) |
| `ea-cpc-interface.l4` | — | the interface to the Criminal Procedure Code subject; **identical in both rows** (section 4) |
| `ea-relevancy.l4` | May evidence be given of this fact? | ss 2, 3(3) to (5), 5 to 16, 106, 138 |
| `ea-statements.l4` | Is this statement relevant, and so admissible? | ss 17 to 23, 31 to 33 (admissions, confessions, the s 32 hearsay framework, earlier testimony) |
| `ea-records-opinion-character.l4` | what else makes a fact, record, opinion or character relevant | ss 34 to 57 (records, judgments, convictions, opinion, character) |
| `ea-proof.l4` | What need not be proved; how are the contents of a document proved? | ss 58 to 80B, 67A, 68A |
| `ea-presumptions-burden.l4` | Does the court presume it? Who bears the burden? | ss 4, 81 to 92, 103 to 114, 116, 116A |
| `ea-parol-evidence.l4` | When does a document exclude oral evidence? | ss 93 to 102 |
| `ea-witnesses-privilege.l4` | Who may testify; what can a witness not be made to disclose? | ss 120 to 136 |
| `ea-examination.l4` | How is a witness examined; what do previous statements prove; what corroborates? | ss 137 to 169 |
| `ea-bankers-schedules.l4` | How are bankers' books proved; which offences are "child abuse" or "sexual"? | ss 170 to 177, both Schedules |
| `ea-goals.l4` | the principal questions, exported; the conclusions the Act hands the Code | assembles the above |
| `ea-tests-*.l4` (9 files) | — | 803 assertions, **generated** by `generators/ea_tests_*.py` from `ea-types.l4` |

**Shape.** Each rule is a `BOOLEAN` (or a `MAYBE`, an enumeration, or a named `REFUSE`) over a record of facts a witness could testify to; the Act's illustrations are the test cases. Where the Act says the court "may" or "is to" do something, the rule says whether the condition for the power or duty is met, never what the court decides in its discretion. Presumptions return the strength the Act gives them (`the court may presume`, `the court is to presume`, `conclusive proof`) or `NOTHING`.

## 2. Coverage table

Disposition: `encoded` (a rule in the module named), `inert` (read, adds no condition or answer; the reason is given), `refuse` (the Act delegates and nothing supplies the answer: a named `REFUSE`), `repealed`, `deferred` (not encoded; says so).

| provision | heading | disposition | where |
| --- | --- | --- | --- |
| 1 | Short title | inert | — |
| 2(1) | Application of Parts 1, 2 and 3 | encoded | relevancy |
| 2(2) | repeal of inconsistent common-law rules | inert: a repeal, not a rule of decision | relevancy (comment) |
| 3(1) "fact in issue", "relevant", "proved", "disproved", "not proved" ((2) to (5)) | Interpretation | encoded | relevancy |
| 3(1) "child abuse offence", "sexual offence" | | encoded with the First Schedule | bankers-schedules |
| 3(1) "document", "electronic record", "copy of a document", "evidence", "fact", "court" | | inert: used in field names; "copy of a document" and "document" feed s 64 and s 65 | proof |
| 3(6), 3(7) | "advocate or solicitor", "legal counsel" | inert: who counts is a fact | — |
| 4 | Presumptions | encoded | presumptions-burden |
| 5 to 16 | Relevancy of facts (same transaction, cause or effect, motive and conduct, explanation, conspiracy, inconsistent facts, damages, right or custom, state of mind, accident, course of business) | encoded | relevancy |
| 17 | Admission and confession defined | encoded | statements |
| 18 to 20 | Whose statements are admissions | encoded | statements |
| 21 to 23 | Proof of admissions; oral admissions as to documents; civil cases | encoded | statements |
| 24 to 30 | | repealed (Act 15 of 2010) | — |
| 31 | Admissions not conclusive proof | inert: weight and estoppel | statements (comment) |
| 32(1)(a) to (k), (2), (3), (4), (6), (7) | Statements of relevant facts by persons not called | encoded | statements |
| 32(5) | weight | inert | statements (comment) |
| 32A, 32B, 32C | utterances; opinion; credibility of the absent maker | encoded (32C(3), (4) stated as extensions) | statements |
| 33 | Earlier testimony | encoded (fork F4) | statements |
| 34, 37 to 40 | books of accounts, public records, maps, recitals, law books | encoded | records-opinion-character |
| 35, 36 | | repealed (Act 4 of 2012) | — |
| 36A | rules for electronic filing | inert: a rule-making power | — |
| 41 | How much of a statement is proved | encoded | records-opinion-character |
| 42 to 46 | Judgments, orders and decrees | encoded | records-opinion-character |
| 45A | Convictions and acquittals | encoded (fork F5) | records-opinion-character |
| 47 to 53 | Opinions | encoded | records-opinion-character |
| 54 to 57 | Character | encoded | records-opinion-character |
| 58 to 60 | Judicial notice; admitted facts | encoded | proof |
| 61, 62 | Oral evidence must be direct | encoded | proof |
| 62A | Video link | encoded; (6A) encoded; (9) rules inert | proof |
| 63 to 68 | Primary and secondary evidence; notice | encoded | proof |
| 67A, 68A | statements in documents; summaries | encoded | proof |
| 69 to 75 | Signatures, attestation, comparison | encoded (fork F8) | proof |
| 76 to 80A | Public documents; certified copies; film prints | encoded | proof |
| 80B | Apostille Act | inert: non-effect statement | — |
| 81 to 92 | Presumptions as to documents | encoded (fork F6) | presumptions-burden |
| 93 to 102 | Oral by documentary evidence | encoded | parol-evidence |
| 103 to 113 | Burden of proof | encoded (fork F7) | presumptions-burden |
| 114 | Paternity | encoded | presumptions-burden |
| 115 | | repealed (Act 8 of 1996) | — |
| 116 | Presumptions of fact | encoded; the nine illustrations are inert | presumptions-burden |
| 116A | Electronic records | encoded; (5) regulations and (7) affidavit inert | presumptions-burden |
| **117, 118, 119** | **Estoppel** | **deferred: not encoded** | — |
| 120, 121 | Who may testify; dumb witnesses | encoded | witnesses-privilege |
| 122 | Parties and spouses; the accused as a witness; cross-examination of the accused | encoded (fork F10) | witnesses-privilege |
| 123 to 133 | Privileges | encoded | witnesses-privilege |
| 134 | Self-incrimination | encoded | witnesses-privilege |
| 135, 136 | Accomplice; number of witnesses | encoded | witnesses-privilege |
| 137 | order of witnesses | inert: sent to other procedure law | — |
| 138 | Court decides admissibility | encoded ((1), (2)); (3) inert | relevancy |
| 139, 140(2), (3), 143 to 145 | Examination; leading questions | encoded | examination |
| 140(1), (4), 141, 142 | order, recall, document-producers, character witnesses | inert | — |
| 146, 147 | Matters in writing; previous statements | encoded; 147(6) weight inert | examination |
| 148 to 155 | Questions in cross-examination; 154A | encoded; 152 inert; 154A(2) refuse | examination |
| 156 | Own witness | inert: discretion | — |
| 157 to 163 | Credit; corroboration; refreshing memory | encoded | examination |
| 164 to 167 | Production; judge's power | encoded | examination |
| 168 | assessors | inert | — |
| 169 | Improper admission or rejection | encoded | examination |
| 170 to 174 | Bankers' books | encoded | bankers-schedules |
| 175, 176 | inspection order; costs | inert: discretion | — |
| 177 | Amendment of Schedules | inert: orders after 01 Oct 2026 are not applied | — |
| First Schedule | Child abuse and sexual offences | encoded as data | bankers-schedules |
| Second Schedule | Specified statutory bodies | encoded as data (23 rows) | bankers-schedules |

## 3. How a rule reads: the three kinds of answer

- a fact record in, `BOOLEAN` out: `the statement falls within section 32(1)(j)`;
- a strength out: `the presumption under section 116A(2)` is `JUST \`the court is to presume\`` or `NOTHING`;
- `REFUSE "…"` where the Act delegates or the facts contradict: `the question is permitted by the section 154A rules`; `the finding on the fact` where the same facts make it proved and disproved.

## 4. Relationship to the Criminal Procedure Code 2010

`l4` resolves an `IMPORT` only to a module in the importing file's own directory (or the project root, `JL4_LIBRARY_PATH` or the embedded library), so a rule in one subject cannot import a module from another. The two subjects therefore meet at **`ea-cpc-interface.l4`**, a DECLARE-only file carried **byte-identically** here and in `sg/criminal-procedure-code-2010/encodings/` (checked with `cmp`). Its records are the conclusions each Act hands the other, each field named for the provision that asks it. No rule of either Act is copied into the other.

**From the Evidence Act to the Code** (`Evidence Act Conclusions`, computed by `what the Evidence Act concludes for the Criminal Procedure Code` in `ea-goals.l4`):

| field | the Code asks it at | the Evidence Act answers it from |
| --- | --- | --- |
| admitted under s 147 | s 259(1)(a) (a witness's investigation statement) | s 147(1) to (5) |
| used to impeach under s 157 | s 259(1)(b) | s 157 |
| made admissible by another provision of the Act | s 259(1)(c) | ss 17 to 23, 32, 33, 147, 159 |
| within s 32(1)(a) | s 259(1)(e) | s 32(1)(a) |
| admissible as evidence of a fact stated | s 268 (hearsay in criminal proceedings) | ss 17 to 23, 32, 33, 147(3), (5) |
| opinion of an expert admissible | s 269(1) | s 47 |
| entitled to refuse to answer under s 122(4) | s 291(5)(a) | s 122(4) to (8), s 56 |

**From the Code to the Evidence Act** (`Code Conclusions`): s 32(4)(a) (the notice requirements prescribed under CPC s 428) and s 122(5) (evidence admissible by CPC s 265 or 266). Also pointing at the Code and not applied: s 32(7) (committal hearings before 17 September 2018) is a fact.

**Limitation to report.** The cross-reference is through a copied interface, not a cross-subject import. The Code's Part 14 is not yet encoded, so the Code side of each row above has no consumer yet. Where the Act or the Code distinguishes kinds of statement, the interface carries the distinction as an enumeration (`Kind of Report or Statement`): the fact that an offence was reported (relevant as conduct, s 8(2) illustrations (j) and (k), and as corroboration, s 159), the content of a first information report (CPC s 260), a witness's investigation statement (CPC s 259), an accused's statement (CPC s 258 and EA ss 17(2), 21), a conditioned statement (CPC s 264), a recorded statement (CPC s 264A), an affidavit (CPC s 262), a report of a qualified person (CPC s 263), a document produced as evidence (EA ss 63 to 68), and a deposition. The enumeration is declared and not yet used by a rule.

## 5. The Schedules

The First Schedule (child abuse offences, sexual offences) is encoded as four lists of section numbers and `the class of the offence under the First Schedule`, which also applies s 3(1)'s inclusion of attempts, abetments and conspiracies (the caller says the offence is ancillary; the class is the underlying offence's). The Second Schedule (23 statutory bodies) is `the specified statutory bodies`, used by s 80A. Both are as printed on 01 Oct 2026; s 177 lets the Minister amend them.

## 6. What `check.sh` prints

Run with `l4` build `unstable-20260926-c76e6b0` (win32-x64), 2026-10-01: 21 modules, 0 errors, 803 assertions satisfied, 0 failed.

```
ea-tests-examination.l4                      0       105       0
ea-tests-parol-evidence.l4                   0        26       0
ea-tests-presumptions-burden.l4              0        83       0
ea-tests-proof.l4                            0       149       0
ea-tests-records-opinion-character.l4        0        70       0
ea-tests-relevancy.l4                        0        50       0
ea-tests-schedules-goals.l4                  0       136       0
ea-tests-statements.l4                       0        89       0
ea-tests-witnesses-privilege.l4              0        95       0
TOTAL (21 modules)                           0       803       0
```

No assertion is expected to fail. A deliberately wrong assertion was run once, to check the harness reports it (it did), and not kept.

## 7. Fork register

| fork | the readings | taken | why |
| --- | --- | --- | --- |
| F1 | s 3(3) to (5): facts that make a fact both proved and disproved | `REFUSE` | the Act defines "not proved" as neither; it does not resolve a contradiction |
| F2 | s 8(2) Explanation 2: is the statement affecting relevant conduct itself "conduct"? | no: relevant on its own | Explanation 1 (statements are not conduct) would otherwise defeat Explanation 2; a test caught the first draft doing this |
| F3 | s 32(1)(b) "in particular ... (i) to (iv)" | illustrations, not conditions | "in particular" |
| F4 | s 33 Explanation "a criminal trial or inquiry is deemed to be a proceeding between the prosecutor and the accused" | the same-parties limb is met where both are criminal proceedings between the same prosecutor and accused | the deeming |
| F5 | s 45A(2) lists exceptions for "a conviction" | applied to a conviction only | the text; an acquittal that is under appeal is still admissible under (1) |
| F6 | s 83: "if such document is kept substantially in the form required by law and is produced from proper custody" | applies to the second class only | grammar; the Explanation to s 92 says it applies "also to section 83" for custody |
| F7 | ss 109 and 110 both made out | s 110 governs | "shifted" |
| F8 | ss 70 and 71 where no attesting witness is alive | s 71's proof is required | a first draft treated "none alive" as enough, and a test showed that contradicts s 71 |
| F9 | s 32B(2) | opinion is relevant under s 32(1) only if admissible as direct oral evidence | the text |
| F10 | s 122(5) refers to the Evidence Act, the CPC and "any other written law" | EA and other-law limbs are facts here; the CPC's limb is a field of `Code Conclusions` | one rule is not copied across subjects |
| F11 | s 62A(1) excludes "proceedings in a criminal matter" | encoded; the criminal equivalent is CPC s 281, not encoded | |
| F12 | s 124(2): "relevant in criminal proceedings in respect of a specified offence" | the rule takes the Boolean as a parameter; `the offence is a specified offence` is a separate rule over its own record | the definition has five limbs |
| F13 | s 128(1) and 128A(1): whether the "advice" limb survives the 128(2) exceptions | the exceptions subtract from every limb | 128(2) says "nothing in this section protects" |
| F14 | s 59(1)(a) to (n) | one field: the fourteen kinds of judicially noticed fact have one effect (s 58) | no difference in effect; the list is in a comment |

## 8. Open questions for a domain expert

- ss 117 to 119 (estoppel) are not encoded.
- s 32(1)(k) with s 32(6): is "the accused or any of the co-accused is represented by an advocate" tested when the agreement is made, as encoded, or at trial?
- s 116 illustrations (recent possession of stolen goods; the accomplice caution) are inert here; whether they should be encoded as conditions with CPC ss 265 and 266 is a modelling choice.
- the interface's `Kind of Report or Statement` enumeration has no rule yet; it belongs with the Code's Part 14.
