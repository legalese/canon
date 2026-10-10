# Goods and Services Tax Act 1993 (Singapore) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (Parts 1-12 and the First to Tenth Schedules), as printed in SSO's informal consolidation of the version in force from 11 September 2026. It is encoded from the text already deposited in this repository.

**Inputs.** These are taken as given rather than worked out:
- the Comptroller's, the Minister's and the Board's discretions and satisfactions;
- regulations (accounting periods, prescribed supplies, input tax rules);
- the classification of a supply into the Fourth Schedule's exempt categories and s 21(3)'s international services;
- facts: values, dates, establishments.

### The top-level goal

`the GST position for` a `Supply case` (`gst-goal.l4`) answers: *for this supply, is GST charged on it, and how; when does it take place; at what rate; how much tax is in the price; and who accounts for it?*

It returns:
- the treatment (standard-rated, zero-rated, exempt or outside the scope);
- whether the supply is made in Singapore;
- the time of supply;
- the rate;
- the tax;
- whether the recipient accounts under the reverse charge, or the customer under s 38 or 38A.

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Is tax charged; where, when, at what rate and on what value; does the reverse charge apply; how is a supply spanning a rate rise split? | `the tax treatment of`, `the supply is made in Singapore`, `belongs in Singapore`, `the rate of tax per cent on`, `the tax within a consideration of…`, `the time of supply of`, `distantly taxable goods`, `the recipient accounts for tax under the reverse charge`, `the tax on a supply performed before an increase,…`, `the tax on a supply invoiced before an increase,` | Part 3, ss 21-23, Part 6A; Second, Third, Fourth, Seventh, Eighth Schedules | `gst-charge.l4` |
| 2 | Must the person register, by when must it notify, from when is it registered, and when may it leave? | `liable to be registered` and its four tests, `registered on the retrospective test from…`, `registered on the prospective test from…`, `a voluntary registration lasts at least until…`, ss 31-33 rules | First Schedule; ss 30-33 | `gst-registration.l4` |
| 3 | May input tax be credited, how much, must it be repaid; what is the net amount; what surcharge applies? | `the input tax may be credited`, `the person should have known of the arrangement`, `the creditable input tax…`, `the net tax due…`, `unpaid input tax must be repaid…`, `the surcharge on a tainted claim of` | ss 19, 20, 34A, 41(7), 45A | `gst-credit.l4` |
| 4 | May the Comptroller still assess; how long are records kept; when are objections and appeals due, and may the appeal be heard? | `the Comptroller may still assess…`, `records must be kept until…`, `the last day to object…`, `…notice of appeal…`, `…petition of appeal…`, `the Board may hear the appeal…`, `may appeal to the High Court…` | ss 45-57 | `gst-administration.l4` |
| 5 | Refund claims, agency notices, detention, advance rulings, service | `the last day to claim a refund…`, the s 79 dates, `the most an advance ruling costs…`, `the notice is served on…` | ss 79, 83E, 87, 90; Fifth Schedule | `gst-administration.l4` |
| 6 | What does late payment or a late return cost; what is each offence's maximum; composition, consent, notice to attend | `the late payment penalty on`, `the late return penalty…`, `the failure-to-register penalty on`, `the maximum penalty for`, `the Public Prosecutor's consent is needed for` | Part 9; ss 44(4), 46(6), 69, 73A, 74, 75, 81(4), 83I, 84, 86(1) | `gst-penalties.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-6 | carried as text (definitions read into the facts; s 2(1A) $400 in Goal 1) |
| ss 7, 8 | Goal 1 |
| ss 9-12A | Goal 1 (time of supply); the rest carried as text |
| ss 13-15 | Goal 1 |
| s 16 | Goal 1 |
| ss 17-18A | Goal 1 (s 17(2)); the rest carried as text |
| ss 19, 20 | Goal 3 |
| ss 21-27A | Goal 1 (zero-rating and exemption as inputs); the rest carried as text |
| ss 28-38A | Goal 2 (ss 30-33); Goal 3 (s 34A); s 38/38A in the top-level goal; the rest carried as text |
| ss 39-40 | Goal 1 (ss 39B, 39C, 39D(2), 40); the rest carried as text |
| ss 41-48 | Goal 3 (ss 41(7), 45A); Goal 4 (ss 45(5), 46(2), 47, 47A, 48) |
| ss 49-57 | Goal 4 |
| ss 58-67 | Goal 6 |
| ss 68-77 | Goal 6 (ss 69, 73A, 74, 75); the rest carried as text |
| ss 78-84A | Goal 5 (ss 79, 83E(7)); offences in Goal 6; the rest carried as text |
| ss 85-94 | Goal 5 (ss 87, 90); the rest carried as text |
| First Schedule | Goal 2 |
| Second, Third Schedules | Goal 1 (paras 5(2), 7(1); paras 1(2), 10, 14) |
| Fourth Schedule | an input (the exempt category) |
| Fifth Schedule | Goal 5 (fees, period) |
| Sixth, Ninth, Tenth Schedules | carried as text |
| Seventh, Eighth Schedules | Goal 1 (customer, marketplace operator; exclusions as an input) |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | First Schedule para 5(2)(a)(i) | Day X before 1 July 2025: "the day immediately after the end of the 30 days" | Day X + 31 | The 30 days run from day X and end on day X + 30 |
| F2 | s 39B | What happens without the election? | The time-of-supply rules apply: consideration received before the change is at the old rate, and the rest at the new | s 11(2), "to the extent covered" |
| F3 | s 60(1)(b) | When does the 2% a month start? | Only once the 60 days after the 5% penalty pass; it then counts completed months from the due date, capped at 50% | The text says "commencing from the date on which the tax became payable" |
| F4 | s 58 | "in default of payment to imprisonment for a term not exceeding 6 months" | Recorded as a 6-month term, but not as an alternative penalty (both = FALSE) | It is imprisonment in default of the fine |
| F5 | s 16 | The rate before 2003 | REFUSE | The consolidation no longer states it |
| F6 | Fifth Schedule para 6(b) | When does a 3-year ruling end? | The day before the third anniversary | "beginning on the date the ruling is made" |

## 4. Tests

- **`gst-tests.l4`: 180 assertions.** Expected values are worked from the source. They cover:
  - place, belonging and treatment;
  - every rate boundary (with a refusal before 2003);
  - the tax fraction and special values;
  - each time-of-supply rule;
  - distantly taxable goods and the reverse charge;
  - the s 39B and s 39C splits;
  - every registration test and date (including the 1 July 2025 change and month-end clamps);
  - input tax, the net amount and the surcharge;
  - assessment and appeal limits;
  - refunds, agents and ruling fees;
  - late payment and late return penalties, every offence maximum, consent and composition;
  - whole cases through the top-level goal.

  A deliberately wrong assertion was added to a copy to confirm that the harness fails.
- **The independent pass.** The files are `tests-independent.l4` (243 assertions), `independent-expectations.md` (E01-E195, written before the encoding was read) and `INDEPENDENT-TEST-REPORT.md`.
  - **First run:** 241 pass and 2 fail.
  - **After the fixes below:** 242 pass and 1 fails. The remaining failure, E166, expects an advance ruling made on 1 March 2025 to apply until 28 February 2028. By the report's own account this is its leap-year slip: the correct last day is 29 February 2028, which the encoding now gives. It is an **expected failure**, and its value is left as written.
- **Changed after the independent pass:**
  - **Reverse charge in the top-level goal (E38).** A reverse-charged supply is now standard-rated, valued at the whole consideration, with the tax added on top (ss 14(2), 17(3A), (2A)(a)). Before, the tax was taken out of the price and the supply reported as outside the scope. Encoder case C (an export with reverse-charge facts that could not both hold) was rewritten without the reverse-charge facts, and case D was added for the reverse charge.
  - **Advance rulings.** The function now returns the last day of the 3 years, the day before the anniversary. The encoder's own expected value had made the same off-by-one mistake and was corrected to the source.
  - **Notice to attend court (s 73A).** This now requires an offence punishable by a fine or imprisonment. Before, s 59(1)'s penalty-only offence counted.
  - **Deemed supplies.** The scope input now reads "for a consideration, or deemed a supply by the Second Schedule", so business-asset deemed supplies are in scope.
  - **Refund claims (s 90).** For periods before 2007 these now refuse (s 90(1A), (5)).

  The independent file was changed only in plumbing: the renamed input field.
- **Simplifications the report lists, kept as they are:**
  - one election flag covers both s 14(5) and s 14(6);
  - the time of supply is a single date, with no "to the extent" splits;
  - recipient belonging (s 15(4)-(5)) and Seventh Schedule status are inputs;
  - open market value for non-money consideration is carried as text;
  - the Second Schedule para 5(4) and 7(2) credit carve-outs, the margin-scheme exclusion and the s 39A(5)/39B(4) limits are carried as text;
  - the s 33(1B), s 47(2A) and s 79(4) 14/28/7-day steps are carried as text;
  - the s 6 secrecy offence falls under s 58;
  - the fines in ss 62A and 62B are recorded in the multiple-of-tax field, with the numbers right;
  - the caller adds the Seventh Schedule supplies to the prospective registration total.

## 5. Open questions

- F3: whether the 60 days are counted from the imposition of the 5% penalty or from the due date.

## 6. Checks

See `encoding.json` → `checks`.
