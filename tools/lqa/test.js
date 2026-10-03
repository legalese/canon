/* ===========================================================================
   Proves the LQA checker can go red. Copies the worked example to a temporary
   folder, breaks it one way at a time, and checks that the step that should
   fail does, and says why.

     node tools/lqa/test.js

   A checker that has never been seen to fail licenses nothing.
   =========================================================================== */
var fs = require("fs"), path = require("path"), os = require("os"), cp = require("child_process");
var EX = path.join(__dirname, "example", "exampleland");
var CHECK = path.join(__dirname, "check.js");

function copyDir(a, b) {
  fs.mkdirSync(b, { recursive: true });
  fs.readdirSync(a).forEach(function (f) {
    var s = path.join(a, f), d = path.join(b, f);
    if (fs.statSync(s).isDirectory()) copyDir(s, d); else fs.copyFileSync(s, d);
  });
}
function run(sub) {
  var r = cp.spawnSync(process.execPath, [CHECK, sub], { encoding: "utf8" });
  return { code: r.status, out: r.stdout + r.stderr };
}
/* the lines of one step's block in the checker's output */
function block(out, stepId) {
  var lines = out.split("\n"), i = lines.findIndex(function (l) { return l.indexOf(stepId + " ") === 0; });
  if (i < 0) return "";
  var b = [lines[i]];
  for (var j = i + 1; j < lines.length && /^\s{7}/.test(lines[j]); j++) b.push(lines[j]);
  return b.join("\n");
}
function edit(file, fn) { fs.writeFileSync(file, fn(fs.readFileSync(file, "utf8"))); }
function editJSON(file, fn) { var o = JSON.parse(fs.readFileSync(file, "utf8")); fn(o); fs.writeFileSync(file, JSON.stringify(o, null, 2)); }
function finding(o, id) { return o.findings.filter(function (f) { return f.id === id; })[0]; }

var CASES = [
  ["the instrument's text changes after pinning", "1A", /does not match its sha256/,
    function (s) { edit(path.join(s, "sources", "bill-print-1.txt"), function (t) { return t.replace("14 days", "21 days"); }); }],
  ["the gathered set changes after 3H", "3H", /STALE/,
    function (s) { editJSON(path.join(s, "registers", "search-log.json"), function (o) { o.searches.pop(); }); }],
  ["a cross-reference supplied as a fact gives no reason", "2A", /needs a reason/,
    function (s) { editJSON(path.join(s, "registers", "reference-register.json"), function (o) { delete o.entries[0].reason; }); }],
  ["the encoding changes after 6H", "6H", /STALE/,
    function (s) { edit(path.join(s, "pet-bill.l4"), function (t) { return t + "\n-- an edit after certification\n"; }); }],
  ["6H is waived with no reason", "6H", /needs a reason/,
    function (s) { editJSON(path.join(s, "registers", "gates.json"), function (o) {
      o.entries.forEach(function (e) { if (e.step === "6H") e.decision = "waived"; }); }); }],
  ["a fork names no reading taken", "5A", /which reading is taken/,
    function (s) { editJSON(path.join(s, "registers", "fork-register.json"), function (o) { delete o.entries[0].taken; }); }],
  ["one category is never probed", "7A", /not yet probed: W over Whole Bill/,
    function (s) { editJSON(path.join(s, "registers", "probe-record.json"), function (o) {
      o.runs = o.runs.filter(function (r) { return r.category !== "W"; }); }); }],
  ["an ID's letter is not its category", "7A", /its letter is not its category/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "P-03").category = "E"; }); }],
  ["a finding has no evidence and is not called opinion", "8A", /P-03: no evidence/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "P-03").evidence = []; }); }],
  ["an assertion cited as evidence is not in the file", "8A", /the assertion is not in/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "R-01").evidence[0].text = "#ASSERT `something else`"; }); }],
  ["a scenario does not show the finding it is cited for", "8A", /does not record T-02/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "T-02").evidence[1].label = "Ben minds Rex for a week"; }); }],
  ["a simulation seed does not reproduce the finding", "8A", /does not record T-02/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "T-02").evidence[0].days = 30; }); }],
  ["a quotation is not in the pinned text", "8A", /quoted words are not in/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "S-05").evidence[0].quote = "A registration shall last a year"; }); }],
  ["a candidate is left unchallenged", "9A", /still a CANDIDATE/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "R-01").status = "CANDIDATE"; }); }],
  ["a finding is answered from outside the reference set", "9A", /neither the 0H nor the 3H set/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "T-04").answered_by.source = "some-textbook"; }); }],
  ["the print moves on and findings are not re-checked", "10A", /current print is print 2/,
    function (s) { editJSON(path.join(s, "lqa.json"), function (o) { o.instrument.print = "print 2"; }); }],
  ["the report leaves a finding out", "11A", /does not mention R-01/,
    function (s) { edit(path.join(s, "REPORT.md"), function (t) { return t.split("R-01").join("R-1"); }); }],
  ["the scheme and the register disagree on how it was found", "11A", /the scheme says found by/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "T-02").found_by = "RD"; }); }],
  ["the scheme changes after release was signed", "12H", /STALE/,
    function (s) { edit(path.join(s, "scheme.js"), function (t) { return t + "\n/* an edit after release */\n"; }); }],
  ["the findings change after release was signed", "12H", /STALE/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { finding(o, "S-05").severity = "medium"; }); }],
  ["a release is signed while an earlier step is open", "12H", /WAITING for 9A/,
    function (s) { editJSON(path.join(s, "incidents.json"), function (o) { delete finding(o, "T-02").challenged; }); }],
  ["the reference set changes after 0H", "0H", /STALE/,
    function (s) { editJSON(path.join(s, "..", "_jurisdiction", "reference-set.json"), function (o) { o.items[0].version = "as at 1 July 2026"; }); }]
];

var extra = 0;
var tmp = fs.mkdtempSync(path.join(os.tmpdir(), "lqa-test-")), failures = 0;
var base = path.join(tmp, "base");
copyDir(EX, base);
var clean = run(path.join(base, "pet-registration-bill-2026"));
if (clean.code !== 0) { console.log("FAIL  the unbroken example is not green:\n" + clean.out); failures++; }
else console.log("ok    the unbroken example is green");

CASES.forEach(function (c, i) {
  var dir = path.join(tmp, "case" + i);
  copyDir(EX, dir);
  var sub = path.join(dir, "pet-registration-bill-2026");
  c[3](sub);
  var r = run(sub), b = block(r.out, c[1]);
  var good = r.code === 1 && !/^\S+\s+\S+\s+DONE\b/.test(b) && c[2].test(b);
  if (!good) failures++;
  console.log((good ? "ok    " : "FAIL  ") + c[1] + ": " + c[0] + (good ? "" : "\n" + (b || r.out)));
});

/* --sign: refuses out of order, refuses a single name, and records a typed full name */
(function () {
  var dir = path.join(tmp, "sign"); copyDir(EX, dir);
  var sub = path.join(dir, "pet-registration-bill-2026");
  fs.unlinkSync(path.join(sub, "registers", "gates.json"));
  function sign(argv) { return cp.spawnSync(process.execPath, [CHECK, sub, "--sign"].concat(argv), { encoding: "utf8" }); }
  var t = [
    ["--sign refuses a step whose predecessors are incomplete", sign(["6H", "--by", "Ann Example"]), 1, /3H not complete/],
    ["--sign refuses a single name", sign(["3H", "--by", "Ann"]), 2, /full name/],
    ["--sign records a typed full name", sign(["3H", "--by", "Ann Example"]), 0, /3H signed by Ann Example/]
  ];
  t.forEach(function (c) {
    var good = c[1].status === c[2] && c[3].test(c[1].stdout + c[1].stderr);
    if (!good) failures++;
    console.log((good ? "ok    " : "FAIL  ") + c[0] + (good ? "" : "\n" + c[1].stdout + c[1].stderr));
  });
  var after = run(sub);
  var good = /3H   Confirm      DONE/.test(after.out) && /6H   Fidelity     NOT STARTED/.test(after.out);
  if (!good) failures++;
  console.log((good ? "ok    " : "FAIL  ") + "after --sign 3H, 3H is DONE and 6H is next" + (good ? "" : "\n" + after.out));
  extra += 4;
})();

fs.rmSync(tmp, { recursive: true, force: true });
console.log("\n" + (failures ? failures + " failure(s)" : "all " + (CASES.length + 1 + extra) + " passed"));
process.exit(failures ? 1 : 0);
