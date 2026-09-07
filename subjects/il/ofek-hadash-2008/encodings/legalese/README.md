# Ofek Hadash — an L4 encoding

What an Israeli teacher is paid, computed from the collective agreements that say so.

**Not reviewed. Draft.** See [NOTES.md](NOTES.md) §8 before relying on any answer, and
[SOURCE-LICENSE.md](SOURCE-LICENSE.md) before redistributing anything from it.

## Run it

```sh
./check.sh                      # 254 assertions across eight modules
OFEK_CORPUS=<corpus> ./source/run-catala.sh   # compile to Catala and RUN the cases
```

`check.sh` pins `JL4_LIBRARY_PATH` to the worktree the `l4` binary was built from. That is
not incidental: a binary pointed at a newer prelude fails in ways that look like errors in
this encoding.

`run-catala.sh` needs a checkout of the source corpus and `catala`/`clerk` 1.2.1.

## The files

| file | |
| --- | --- |
| `ofek-domain.l4` | the ontology every other module reads |
| `ofek-salary-table.l4` | both combined-salary tables, the frontier, and the steps that generate them |
| `ofek-placement.l4` | §§ 36–38 — placement, seniority, promotion, the rank quotas |
| `ofek-worktime.l4` | §§ 14–33 — the 36-hour week, the age reductions, § 31's hourly value |
| `ofek-supplements.l4` | § 39 supplements, the 2022 shekel floors, Tosefet Ofek 2022, § 22 units |
| `ofek-fiscal-2025.l4` | the 2025–2026 wage reduction |
| `ofek-pay.l4` | a month's pay, assembled |
| `ofek-cases.l4` | three teachers, end to end |
| `ofek-catala.l4` | **generated** — the above flattened to the Catala v1 fragment |
| `catala/` | the emitted Catala module, and hand-written case scopes that run it |
| `source/` | the corpus parser, the module generator, and the Catala harness. No source text |
| `registers/` | all 282 corpus documents, the source bundle, and 13 forks |

## Three things a reader should know

**Ofek Hadash is not legislation.** It is a collective agreement between the State and the
Teachers' Union, layered with later agreements, binding decisions of a joint follow-up
committee, and ministry circulars. Even the 2025 budget law works by referring back to an
approved collective agreement rather than setting a rate itself.

**Half a post is not half the pay.** The combined salary and Tosefet Ofek 2022 are pro-rated;
the role supplements and the school-role supplement are not. The running fixture takes 54.5%
of full pay for 50% of the work, and a teacher just below a third of a post drops *below* a
proportionate share. NOTES.md §5.2.

**The salary table generates itself.** The two percentages printed in the table's own margins
reproduce all 224 of its separately-printed cells, to half an agora. The encoding carries
both the numbers and the rates, and asserts that the second produces the first. NOTES.md
§5.1.
