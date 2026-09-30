# Independent test report: Carriage by Air Act 1988

File: `tests-independent.l4` (343 assertions). Result of `l4 run`: 343 satisfied, 0 failed, 0 error diagnostics.
Expected values were fixed from `source/CAA1988.txt` and `BRIEF.md` before any `.l4` file was opened. A deliberate wrong assertion in a scratch file was confirmed to print `assertion failed`, so the harness does detect failures.

Covered, per Convention text: Art 22 limits and unit (WS 125,000; HG/MT 250,000 francs; 250 francs/kg; MT cargo 17 SDR/kg; 5,000 francs), amounts with special contract, declared value, part-loss weight; Art 22(4) costs and the "later of six months / commencement" edge; Art 26 periods on both sides of each day (3/7/14 vs 7/14/21/21) and forthwith, writing, fraud; s 7; forfeiture under Arts 3, 4, 9 (each text); Arts 18, 20, 21, 23, 24, 25, 25A, 32; Art 29 and s 8(1)-(3) edges; Art 13(3) edge; Arts 37-39 timing and 40A; ss 2-13; Arts 1, 2, 34 scope; Art 30; REFUSE where a text is silent.

Not tested: Arts 1(3), 12, 14, 15(2), 16, 17 detail, 27, 28, 31, 36, 40, 41; Art 6/8 content checks; Art 3(1)/4(3)/8 particulars functions; Article 29(2) and month-end/leap-day counting (fork F6, law of the forum); Montreal Art 2(2)/(3) postal carriage; Art 22(5)/(6) conversion rules; s 6(5); the deontic duties in the scope module.
