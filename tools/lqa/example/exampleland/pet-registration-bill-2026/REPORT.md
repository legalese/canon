# LQA report: Pet Registration Bill 2026 (Exampleland), print 1

**FICTIONAL.** A worked example for `tools/lqa/check.js`. Exampleland does not exist.

Five findings: four OPEN, one verified sound. Found by: encoding 3, simulation 1, comparison 1.
"Found by" uses the casual-reader test in `LQA-PIPELINE.md`.

| ID | Finding | Status | Severity | Found by |
|---|---|---|---|---|
| P-03 | The council may refuse to consider, without limit (s. 4(2)) | OPEN | high | encode |
| T-02 | A registration granted in June lasts days (s. 5) | OPEN | medium | simulate |
| R-01 | "The person" in s. 3(2) has no antecedent | OPEN | low-medium | encode |
| S-05 | Section 5 uses "shall" (Drafting Manual 3.1) | OPEN | low | compare |
| T-04 | "3 months of age" (s. 3(1)): answered by Interpretation Act s. 12 | VERIFIED-NO-DEFECT | none | encode |

Forks: FORK-1, "the person" in s. 3(2), reading A (the owner) taken; both readings asserted.

Not encoded: ss. 1 and 2. Reference set knowingly lacks the second-reading speech (Hansard refused
automated access).
