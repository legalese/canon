# Online Safety (Minimum Age and Child Safety Risk Assessment) Bill -- coverage register

**Run date:** 2026-09-11  
**Question answered:** which clauses of the Bill are modelled, and which are not.  
**Method:** every `@ref` citation in the eight rules modules was parsed for clause numbers and
matched against the Bill's own arrangement of clauses, taken from
`registers/source-bundle/LMS1592864.xml`. Subsection numbers in parentheses are stripped, so
`cll 15(2), 16(3)` reads as clauses 15 and 16. Schedule 1 clauses are counted separately,
because they restart at 1.

This register is mechanical. It records that a clause **is cited by the encoding**, not that
the rule is a correct or complete reading of it. Fidelity is a separate question and no
fidelity claim is made: the subject's status is `draft`.

Two limits of the method, stated because they matter here. A clause may be encoded without
carrying an `@ref` of its own -- a constant, or a rule reached through a cited neighbour --
and the third column names each such clause rather than counting it as uncovered. And a
clause cited jointly with another (`cll 45, 46, 47` on one rule) is counted for all of them,
so a single citation can cover three clauses; treat any clause whose only evidence is a joint
citation as worth checking rather than as proven.

---

## Body of the Bill, clauses 1 to 64

| Clause | Heading | Coverage |
| --- | --- | --- |
| 1 | Title | encoded, no own `@ref` -- Short title, encoded as a constant in part-1-preliminary.l4 |
| 2 | Commencement | encoded, no own `@ref` -- Commencement period, encoded as a constant in part-1-preliminary.l4 |
| 3 | Purpose | encoded, no own `@ref` -- Purpose, encoded as a constant in part-1-preliminary.l4 |
| 4 | Interpretation | encoded, no own `@ref` -- Interpretation; definitions encoded where they bear on a determination, otherwise taken as facts |
| 5 | Meaning of age-restricted platform | cited by `part-1-preliminary` |
| 6 | Meaning of operator | cited by `part-1-preliminary` |
| 7 | Regulator's power to designate operators | cited by `part-1-preliminary` |
| 8 | Territorial application | cited by `part-1-preliminary` |
| 9 | Transitional, savings, and related provisions | encoded, no own `@ref` -- Points at Schedule 1, which is encoded in schedule-1-transitional.l4 |
| 10 | Act binds the Crown | encoded, no own `@ref` -- Act binds the Crown, encoded as a constant in part-1-preliminary.l4 |
| 11 | Operators must take steps to prevent persons under 16 years from having accounts | cited by `part-2-duties` |
| 12 | Personal information collected for the purpose of complying with duty | cited by `part-2-duties` |
| 13 | Breach of restrictions relating to personal information | cited by `part-2-duties` |
| 14 | Operators must undertake child safety risk assessment | cited by `part-2-duties` |
| 15 | Provision of child safety risk assessment to regulator | cited by `part-2-duties` |
| 16 | Review of child safety risk assessment | cited by `part-2-duties` |
| 17 | Change-related child safety risk assessments | cited by `part-2-duties` |
| 18 | Individual responsible for confirming accuracy of risk assessments | cited by `part-2-duties` |
| 19 | Regulator's power to direct operator to repeat risk assessment | cited by `part-2-duties` |
| 20 | Regulator's functions | cited by `part-3-subpart-1-regulator` |
| 21 | Regulator's power to require information | cited by `part-3-subpart-1-regulator` |
| 22 | Sharing information with law enforcement or regulatory agencies and overseas regulators | cited by `part-3-subpart-1-regulator` |
| 23 | Restriction on disclosure of information acquired under sections 21 and 22 | cited by `part-3-subpart-1-regulator` |
| 24 | Regulator must issue warnings in certain manner | cited by `part-3-subpart-2-enforcement` |
| 25 | Regulator may require operator to disclose warning | cited by `part-3-subpart-2-enforcement` |
| 26 | Operator must comply with notice to disclose warning | cited by `part-3-subpart-2-enforcement` |
| 27 | Enforceable undertakings | encoded, no own `@ref` -- Undertaking record and lifecycle encoded in part-3-subpart-2-enforcement.l4 under the cl 29 citations |
| 28 | Notification requirements for undertakings | encoded, no own `@ref` -- Notification requirement carried as a field on the undertaking record |
| 29 | When undertaking becomes enforceable | cited by `part-3-subpart-2-enforcement` |
| 30 | Breach of undertaking | cited by `part-3-subpart-2-enforcement` |
| 31 | Corrective notices | cited by `part-3-subpart-2-enforcement` |
| 32 | Operator must comply with corrective notice | cited by `part-3-subpart-2-enforcement` |
| 33 | Procedural matters relating to corrective notice | cited by `part-3-subpart-2-enforcement` |
| 34 | Court-imposed remedies available under this subpart | encoded, no own `@ref` -- Remedy kinds and the specified liability act enum; the enum lives in types.l4 |
| 35 | Service restriction orders | cited by `part-3-subpart-3-remedies` |
| 36 | Interim service restriction orders | **not encoded** -- Interim service restriction order; granted on the court's opinion that it is desirable |
| 37 | Content of service restriction orders or interim service restriction orders | **not encoded** -- Content of a service restriction order; no condition on the outcome |
| 38 | Access restriction orders | cited by `part-3-subpart-3-remedies` |
| 39 | Interim access restriction orders | **not encoded** -- Interim access restriction order; granted on the court's opinion |
| 40 | Content of access restriction orders or interim access restriction orders | **not encoded** -- Content of an access restriction order; no condition on the outcome |
| 41 | Additional requirements relating to making of restriction orders | **not encoded** -- Court must consider named persons' rights (41(1)); regulator must inform the Minister (41(2)) |
| 42 | Application for renewal of restriction orders | **not encoded** -- Renewal procedure for restriction orders |
| 43 | Appeal to Court of Appeal on question of law | **not encoded** -- Appeal to the Court of Appeal on a question of law |
| 44 | Pecuniary penalty order | cited by `part-3-subpart-3-remedies` |
| 45 | Maximum penalty (Tier 1) | cited by `part-3-subpart-3-remedies` |
| 46 | Maximum penalty (Tier 2) | cited by `part-3-subpart-3-remedies` |
| 47 | Maximum penalty (Tier 3) | cited by `part-3-subpart-3-remedies` |
| 48 | Considerations for court in determining pecuniary penalty | **not encoded** -- Matters the court must have regard to in fixing a penalty; constrains reasoning, not outcome |
| 49 | High Court may grant injunctions | **not encoded** -- High Court may grant injunctions; power, not test |
| 50 | When court may grant restraining injunctions | **not encoded** -- Restraining injunctions on the court's satisfaction or opinion |
| 51 | When court may grant performance injunctions | **not encoded** -- Performance injunctions on the court's satisfaction or opinion |
| 52 | Regulator's undertaking as to damages not required for interim measures | **not encoded** -- Removes the requirement for an undertaking as to damages |
| 53 | Rules of civil procedure and civil standard of proof apply | **not encoded** -- Applies the ordinary civil rules and standard of proof |
| 54 | More than 1 court-imposed remedy may be given for same conduct | cited by `part-3-subpart-3-remedies` |
| 55 | Only 1 pecuniary penalty order may be made for same conduct | cited by `part-3-subpart-3-remedies` |
| 56 | No pecuniary penalty and criminal penalty for same conduct | cited by `part-3-subpart-3-remedies` |
| 57 | Offence relating to false or misleading risk assessments | cited by `part-3-subpart-4-offences` |
| 58 | Offence relating to information requirements under section 21 | cited by `part-3-subpart-4-offences` |
| 59 | Offence relating to conditions imposed in relation to information | cited by `part-3-subpart-4-offences` |
| 60 | Offence relating to unauthorised disclosure of information | cited by `part-3-subpart-4-offences` |
| 61 | Exemption order | cited by `part-3-subpart-5-other` |
| 62 | Regulations relating to age-restricted platforms | cited by `part-3-subpart-5-other` |
| 63 | Regulations relating to other matters | cited by `part-3-subpart-5-other` |
| 64 | Review of this Act | encoded, no own `@ref` -- Review period encoded as a constant in part-3-subpart-5-other.l4 |

## Schedule 1

| Clause | Heading | Coverage |
| --- | --- | --- |
| 1 | Interpretation | encoded, no own `@ref` -- commencement date modelled as a fact, not a calendar date |
| 2 | Section 11 applies in respect of accounts created before, on, and after commencement date | cited by `schedule-1-transitional` |
| 3 | Existing operators must provide child safety risk assessment to regulator within 6 months after commencement date | cited by `schedule-1-transitional` |

## Counts

- Clauses in the body of the Bill: **64**
- Encoded (cited, or encoded without an own citation): **51**
- Deliberately not encoded, with the reason recorded in the module: **13**
- Unaccounted for: **0**
- Schedule 1 clauses: **3**, all accounted for

## `@ref` citations per module

| Module | `@ref` citations |
| --- | --- |
| `part-1-preliminary.l4` | 4 |
| `part-2-duties.l4` | 9 |
| `part-3-subpart-1-regulator.l4` | 4 |
| `part-3-subpart-2-enforcement.l4` | 7 |
| `part-3-subpart-3-remedies.l4` | 6 |
| `part-3-subpart-4-offences.l4` | 4 |
| `part-3-subpart-5-other.l4` | 3 |
| `schedule-1-transitional.l4` | 2 |
| `types.l4` | 0 |
| **Total** | **39** |
