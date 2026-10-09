# Supreme Court of Judicature Act 1969 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation.

**Checks:** one case file, 81 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**38 of the 527 Singapore Acts** deposited here cite it: s 80 (the Rules of Court
power) by 25 and s 29C (which court hears an appeal) by 11. This row takes the
civil appeal routes -- whether an appeal lies, whether permission is needed, and
which court hears it -- because that is what s 29C's citers depend on and what a
litigant asks first. s 80 is a rule-making power and the Rules of Court were not
retrieved.

## What the Act turns out to say

### 1. Two mirrored pairs of orders get opposite treatment

Fourth Schedule para 1(i), (j): **no appeal** against an order **giving** permission
to amend a pleading, or **refusing** security for costs. Fifth Schedule para 3(h),
(i): an order **refusing** permission to amend, or **giving** security for costs, can
be appealed **with permission**. In each pair the order that lets the case go on is
final and the one that obstructs it is appealable. Asserted.

### 2. Routing follows the case's subject, not the issue on appeal

Sixth Schedule para 1(a) to (ea): an appeal goes to the Court of Appeal if it
"arises from a case relating to" constitutional or administrative law, contempt,
arbitration, corporate insolvency, patents, or admiralty and shipping, "**even if the
appeal does not raise any issue**" in that field. A costs-only appeal in an
arbitration-related case goes to the apex court. Asserted.

### 3. A parent's maintenance appeal goes to the apex court

Sixth Schedule para 1(i)(v): appeals under "section 18(5) of the Maintenance of
Parents Act 1995" go to the **Court of Appeal**. A contract appeal of any size goes to
the **Appellate Division** (s 29C(1)). Asserted.

### 4. The parties can sign away their appeal, before or after judgment

Fourth Schedule para 3: no appeal where the parties have agreed in writing that the
decision is final, and the agreement "may be made before or after the decision".
The only way back is to allege fraud, illegality or a fundamental breach of natural
justice, and then only with permission (Fifth Schedule para 5). Asserted.

### 5. Two money thresholds

s 21(1)(a): from a District or Magistrate's Court, permission is needed where the
amount in dispute is **$60,000 or less** (excluding interest and costs). s 29A(1)(b):
from the General Division, **$250,000 or less** -- unless the General Division was
exercising an original jurisdiction a written law gives it exclusively, or it is the
Family Division at first instance (Fifth Schedule para 2(2)). Asserted at the
boundaries.

### 6. Smaller things worth recording

- **s 21 and the Third Schedule:** a defendant ordered to pay into court as the price
  of defending, or of setting aside a default judgment, can appeal without
  permission; the other side needs it.
- **s 29C(3):** the routing section "does not create any right of appeal".
- **s 22(7):** on an appeal from a State Court, the General Division may vary any part
  of the decision in favour of a party who did not appeal.
- **ss 45, 60C:** an appeal is no stay of enforcement unless a court orders one.
- **Fourth Schedule para 1(b):** consent judgments are never appealable.

## What would need doing before this is worth anything

- **Retrieve the Rules of Court 2021**, which set the time limits and procedure for
  every appeal here.
- **No case law was searched.** "Arises from a case relating to" in the Sixth
  Schedule, and "amount in dispute" in s 29A, have both been litigated.
- Criminal appeals and the post-appeal capital-case procedure are not encoded.
