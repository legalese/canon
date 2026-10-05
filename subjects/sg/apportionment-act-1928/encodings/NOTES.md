# Apportionment Act 1928 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act, ss 1–7**, as printed by SSO, current version as at 05 Oct 2026 (2020 Revised Edition).
The Legislative History lists no amending Act since Ordinance 25 of 1928, only revised editions, so no date is gated.
Nothing in the Act is left out.

The encoding answers four questions about a periodical payment and a cut-off day — a death, a re-entry, a sale:

| question | rule | module |
| --- | --- | --- |
| is it apportionable at all? | `apportionable under the Act`, and `the apportionment of` … `at` …, which names the exclusion | `aa-act.l4` |
| how much has accrued by the cut-off day? | `the part of` … `accrued at` … (s 3, s 2 for dividends), less a share of just allowances (s 5(1)) | `aa-act.l4` |
| when is it payable? | `the s 4 limb for` …, `the apportioned part of` … `is payable on` … | `aa-act.l4` |
| from whom is it recovered? | `s 5(1) gives remedies to` …, `the route for recovering the apportioned part of` … | `aa-act.l4` |

## 2. Coverage table

| s | heading | disposition |
| --- | --- | --- |
| long title | "An Act for the better apportionment of rents and other periodical payments." | inert |
| 1 | Short title | inert |
| 2 | Interpretation | encoded: "rents", "annuities" (incl. salaries and pensions) and "dividends" are the `Kind of payment`; the dividend exclusion of a return of capital and the deemed daily accrual over the declared period are both encoded |
| 3 | Rents, etc., to accrue from day to day | encoded |
| 4 | Apportioned part payable when next entire portion due | encoded, (a) and (b) |
| 5 | Remedies for recovering apportioned parts | encoded, (1) (who, and the proportionate allowances) and (2) (rent charged on land) |
| 6 | Exclusion of policies of assurance | encoded |
| 7 | Exclusion by express stipulation | encoded |

## 3. Fork register

| id | provision | the question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 3 "accruing from day to day" | how are days counted? | whole days elapsed since the period began: the first day not counted, the cut-off day counted. 1 Jan – 1 Apr is 90 days, and a cut-off on 1 Feb is 31 of them | The Act does not say. This is the reading under which the whole period adds up to exactly the entire portion and nothing has accrued on day 0. Another reading (counting both ends) gives a slightly larger share. |
| F2 | s 5(2) "an entire or continuing rent" | does (2) reach rent on land whose payment has determined (s 4(b))? | **yes** — any rent reserved out of or charged on land | "entire or continuing" is disjunctive. "Entire" does its work in the s 4(b) case: a life-tenant landlord dies mid-period, the next entire rent is received by the successor, and the executors recover the apportioned part from that person by suit. **Revised 2026-10-05:** the first reading (continuing rent only) was challenged by the independent test pass, which pointed out that it left "entire" with nothing to do; on re-reading the text the challenge was accepted. |

The rest of the Act is plain on its face. Looked for and not found: no money threshold, no time limit and no discretion anywhere in the Act.

## 4. Tests

`aa-tests.l4`, 26 assertions written from the text, with the arithmetic shown beside each: quarterly rent ($9,000 over 90 days; 31 days → $3,100), a salary, a dividend declared for a year (182 of 365 days → $18,200), each exclusion in ss 2, 6 and 7, both limbs of s 4, both routes of s 5, and the proportionate allowances (31/90 of $900 = $310 off).
`tests-independent.l4` (37 assertions) and `INDEPENDENT-TEST-REPORT.md` are the independent pass. A separate session wrote its expectations from the source before reading the encoding (`independent-expectations.md`). First run: 36 of 37. The one failure was fork F2, now revised (§3). Now 37 of 37.

## 5. Checks

See `encoding.json` → `checks` for the numbers `check.sh` printed.
