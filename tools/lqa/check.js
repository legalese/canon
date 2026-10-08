/* ===========================================================================
   The LQA checker: reads one subject's files and reports the status of every
   step of the LQA pipeline (LQA-PIPELINE.md), 0H to 13A. Every status is a
   function of files on disk; nothing here takes anyone's word for anything.

     node tools/lqa/check.js <subject-dir>                 report every step
     node tools/lqa/check.js <subject-dir> --l4            also run `l4 check` and `l4 run`
     node tools/lqa/check.js <subject-dir> --digest 6H     print the digest a human signs
     node tools/lqa/check.js <subject-dir> --sign 6H --by "Full Name" [--decision waived --reason "..."]
                                                       record a human's approval, given in the conversation
     node tools/lqa/check.js --jurisdiction <dir> --sign 0H --by "Full Name" --statement "..." [--missing m.json]

   Steps run strictly in order: a step whose predecessor is not complete is WAITING, whatever its
   files say. A human step is approved in the conversation: the agent shows the human what the
   step covers, the human types their full name, and --sign records the name, the date and the
   digest of what they approved.

   Exit 0 when every step is DONE (or 6H WAIVED), 1 otherwise, 2 on bad usage.

   The checker cannot tell who wrote a gate entry. That an H step was done by a
   human is a matter of honesty, not of this program.
   =========================================================================== */
var fs = require("fs"), path = require("path"), crypto = require("crypto"), vm = require("vm"),
    cp = require("child_process");

var CATS = ["D", "R", "L", "T", "U", "P", "E", "M", "I", "X", "W", "F", "S"];
var MAX_HEADLINES = 10;                          /* 9A: headline findings at most; the rest are drafting notes */
var STEPS = [
  ["0H", "Jurisdiction"], ["1A", "Pin"], ["2A", "Gather"], ["3H", "Confirm"], ["4A", "Encode"],
  ["5A", "Fork"], ["6H", "Fidelity"], ["7A", "Probe"], ["8A", "Demonstrate"], ["9A", "Challenge"],
  ["10A", "Re-pin"], ["11A", "Report"], ["12H", "Release"], ["13A", "Publish"]
];
var L4 = process.env.L4_BIN || "C:\\Users\\micha\\AppData\\Local\\Programs\\l4\\l4.exe";

/* ------------------------------------------------------------------ args */
var args = process.argv.slice(2), subjectDir = null, runL4 = false, digestFor = null, jurOnly = null, SIGN = null;
for (var i = 0; i < args.length; i++) {
  if (args[i] === "--l4") runL4 = true;
  else if (args[i] === "--jurisdiction") jurOnly = args[++i];
  else if (args[i] === "--sign") (SIGN = SIGN || {}).step = args[++i];
  else if (/^--(by|decision|statement|reason|recipient|missing)$/.test(args[i])) (SIGN = SIGN || {})[args[i].slice(2)] = args[++i];
  else if (args[i] === "--digest") digestFor = args[++i];
  else if (!subjectDir) subjectDir = args[i];
}
if (!subjectDir && !jurOnly) { console.error("usage: node tools/lqa/check.js <subject-dir> [--l4] [--digest 0H|3H|6H|12H]\n       node tools/lqa/check.js --jurisdiction <_jurisdiction-dir> [--digest 0H]"); process.exit(2); }
/* --jurisdiction checks 0H alone, before any subject in the jurisdiction exists */
var SUB = jurOnly ? path.resolve(jurOnly, "..", "__none__") : path.resolve(subjectDir),
    JUR = jurOnly ? path.resolve(jurOnly) : path.resolve(SUB, "..", "_jurisdiction");
var ROOT = (function () {                       /* the repository root, for paths written relative to it */
  var d = SUB;
  while (d !== path.dirname(d)) {
    if (fs.existsSync(path.join(d, "LQA-PIPELINE.md"))) return d;
    d = path.dirname(d);
  }
  return SUB;
})();

/* --------------------------------------------------------------- helpers */
function sha(buf) { return crypto.createHash("sha256").update(buf).digest("hex"); }
function exists(p) { try { return fs.statSync(p).isFile(); } catch (e) { return false; } }
function readJSON(p) {
  if (!exists(p)) return { missing: true };
  try { return { data: JSON.parse(fs.readFileSync(p, "utf8")) }; }
  catch (e) { return { error: path.basename(p) + " is not valid JSON: " + e.message }; }
}
/* a path in a register may be relative to the subject, to the jurisdiction folder
   ("_jurisdiction/..."), or to the repository root ("subjects/...") */
function resolve(p) {
  if (!p) return null;
  if (/^_jurisdiction[\/\\]/.test(p)) return path.join(path.dirname(JUR), p);
  var a = path.join(SUB, p);
  if (exists(a)) return a;
  var b = path.join(ROOT, p);
  return exists(b) ? b : a;
}
/* the digest a gate signs: every covered file's name and bytes, in a fixed order. Names are
   relative to the subject, so a signature binds to content, not to where the repository sits. */
function digestFiles(files) {
  var h = crypto.createHash("sha256");
  files.forEach(function (f) {
    h.update(path.relative(SUB, f).replace(/\\/g, "/") + "\0");
    h.update(exists(f) ? fs.readFileSync(f) : "<missing>");
    h.update("\0");
  });
  return h.digest("hex");
}
function norm(s) { return String(s).replace(/[\u2018\u2019]/g, "'").replace(/[\u201C\u201D]/g, '"').replace(/\s+/g, " ").trim(); }

/* --------------------------------------------- a small JSON Schema subset */
var SCHEMAS = path.join(__dirname, "schemas");
function schema(name) { return JSON.parse(fs.readFileSync(path.join(SCHEMAS, name + ".schema.json"), "utf8")); }
function validate(name, data) {
  var root = schema(name), errs = [];
  function walk(s, v, at) {
    if (s.$ref) s = root.$defs[s.$ref.replace("#/$defs/", "")];
    if ("const" in s && v !== s.const) { errs.push(at + ": must be " + JSON.stringify(s.const)); return; }
    if (s.enum && s.enum.indexOf(v) < 0) { errs.push(at + ": " + JSON.stringify(v) + " is not one of " + s.enum.join(", ")); return; }
    var t = s.type;
    if (t === "object") {
      if (!v || typeof v !== "object" || Array.isArray(v)) { errs.push(at + ": must be an object"); return; }
      (s.required || []).forEach(function (k) { if (!(k in v)) errs.push(at + ": missing " + k); });
      Object.keys(s.properties || {}).forEach(function (k) { if (k in v) walk(s.properties[k], v[k], at + "." + k); });
    } else if (t === "array") {
      if (!Array.isArray(v)) { errs.push(at + ": must be an array"); return; }
      if (s.minItems && v.length < s.minItems) errs.push(at + ": needs at least " + s.minItems);
      if (s.items) v.forEach(function (x, i) { walk(s.items, x, at + "[" + i + "]"); });
    } else if (t === "string") {
      if (typeof v !== "string") { errs.push(at + ": must be a string"); return; }
      if (s.minLength && v.length < s.minLength) errs.push(at + ": must not be empty");
      if (s.pattern && !new RegExp(s.pattern).test(v)) errs.push(at + ": " + JSON.stringify(v) + " does not match " + s.pattern);
    } else if (t === "integer") {
      if (typeof v !== "number" || v % 1) { errs.push(at + ": must be an integer"); return; }
      if ("minimum" in s && v < s.minimum) errs.push(at + ": below " + s.minimum);
    } else if (t === "boolean" && typeof v !== "boolean") errs.push(at + ": must be true or false");
  }
  walk(root, data, name);
  return errs;
}
function load(name, file, problems) {
  var r = readJSON(file);
  if (r.missing) return null;
  if (r.error) { problems.push(r.error); return null; }
  validate(name, r.data).forEach(function (e) { problems.push(e); });
  return r.data;
}

/* -------------------------------------------------------- the console engine */
var engineCache = {};
function loadScheme(file, id) {
  var key = file + "#" + id;
  if (key in engineCache) return engineCache[key];
  var box = { window: {}, console: { log: function () {}, warn: function () {}, error: function () {} } };
  box.window.window = box.window;
  vm.createContext(box);
  var out = { error: null };
  try {
    vm.runInContext(fs.readFileSync(path.join(__dirname, "..", "scheme-console", "engine.js"), "utf8"), box, { filename: "engine.js" });
    vm.runInContext(fs.readFileSync(file, "utf8"), box, { filename: path.basename(file) });
    out.Engine = box.window.Engine;
    out.scheme = (box.window.SCHEMES || []).filter(function (s) { return s.id === id; })[0];
    if (!out.scheme) out.error = "no scheme with id \"" + id + "\" in " + path.basename(file);
  } catch (e) { out.error = path.basename(file) + " does not load: " + e.message; }
  return (engineCache[key] = out);
}
function refsFired(S, eng) {             /* the finding ids whose observations fired in a run */
  var byObs = {};
  (S.scheme.observations || []).forEach(function (o) { if (o.ref) byObs[o.id] = o.ref; });
  return Object.keys(eng.counts).filter(function (k) { return eng.counts[k] && byObs[k]; })
    .map(function (k) { return byObs[k]; });
}
function playScenario(S, label) {
  var sc = (S.scheme.scenarios || []).filter(function (x) { return x.label === label; })[0];
  if (!sc) return null;
  var eng = new S.Engine(S.scheme), errs = [];
  eng.play(sc, function (e) { errs.push(e.message); })(sc.focus);
  return { refs: refsFired(S, eng), errs: errs };
}
function simulate(S, ev) {
  var sim = S.scheme.simulation, param = {};
  (sim.params || []).forEach(function (p) { param[p.key] = p.def; });
  Object.keys(ev.params || {}).forEach(function (k) { param[k] = ev.params[k]; });
  var eng = new S.Engine(S.scheme);
  eng.seed(ev.seed);
  eng.startRun(sim, param);
  for (var d = 0; d < (ev.days || 365); d++) { eng.tick(); eng.generate(sim); }
  return refsFired(S, eng);
}

/* ------------------------------------------------------------ the subject */
var R = {};                                     /* step id -> { status, problems, notes } */
function step(id) { return (R[id] = R[id] || { status: "DONE", problems: [], notes: [] }); }
function fail(id, msg) { step(id).problems.push(msg); }
function note(id, msg) { step(id).notes.push(msg); }
function notStarted(id, why) { var s = step(id); s.status = "NOT STARTED"; s.problems.push(why); }

var mp = [], manifest = jurOnly ? { subject: "(none)", legal_engineer: "", instrument: { title: "reference set only", print: path.relative(process.cwd(), JUR), document: "" } }
                                : load("lqa-subject", path.join(SUB, "lqa.json"), mp);
if (!manifest) {
  console.error(mp.length ? "lqa.json: " + mp.join("; ") : "No lqa.json in " + SUB + ": this is not an LQA subject.");
  process.exit(2);
}
var reg = function (f) { return path.join(SUB, "registers", f); };
var P = {};                                     /* parse problems, by step */
function loadFor(stepId, name, file) { var pr = []; var d = load(name, file, pr); pr.forEach(function (m) { fail(stepId, m); }); return d; }

var refSet = loadFor("0H", "reference-set", path.join(JUR, "reference-set.json"));
var bundleR = readJSON(reg("source-bundle.json")), bundle = bundleR.data;
var searchLog = loadFor("2A", "search-log", reg("search-log.json"));
var refReg = loadFor("2A", "reference-register", reg("reference-register.json"));
var coverage = loadFor("4A", "coverage", path.join(SUB, "coverage.json"));
var forksR = readJSON(reg("fork-register.json")), forks = forksR.data;
var gates = loadFor("6H", "gates", reg("gates.json"));
var probe = loadFor("7A", "probe-record", reg("probe-record.json"));
var incidents = loadFor("7A", "incidents", path.join(SUB, "incidents.json"));
var releases = loadFor("13A", "release-log", reg("release-log.json"));
var findings = (incidents && incidents.findings) || [];
var schemeFile = coverage && coverage.scheme ? resolve(coverage.scheme.file) : null;
var S = schemeFile ? loadScheme(schemeFile, coverage.scheme.id) : null;

/* --------------------------------------------------------------- digests */
function libFiles() { return ((refSet && refSet.library) || []).map(function (m) { return path.join(JUR, m.file); }); }
function moduleFiles() {
  var seen = {}, out = [];
  ((coverage && coverage.parts) || []).forEach(function (p) {
    p.modules.forEach(function (m) { var f = resolve(m); if (!seen[f]) { seen[f] = 1; out.push(f); } });
  });
  ((refReg && refReg.entries) || []).forEach(function (e) {
    if (e.disposition === "encoded" && e.module) { var f = resolve(e.module); if (!seen[f]) { seen[f] = 1; out.push(f); } }
  });
  return out.sort();
}
var DIGEST = {
  "0H": function () {
    var h = crypto.createHash("sha256");
    h.update(JSON.stringify({ items: refSet && refSet.items, library: refSet && refSet.library }));
    h.update(digestFiles(libFiles()));
    return h.digest("hex");
  },
  "3H": function () { return digestFiles([reg("source-bundle.json"), reg("search-log.json"), reg("reference-register.json")]); },
  /* 6H vouches for the encoding: the L4 and the forks. The console scheme gains its findings and
     scenarios after 6H (8A, 11A), so it is covered at 12H, not here. */
  "6H": function () { return digestFiles(moduleFiles().concat([reg("fork-register.json")])); },
  "12H": function () { return digestFiles([path.join(SUB, "incidents.json"), path.join(SUB, "REPORT.md"), schemeFile || ""]); }
};
if (digestFor) {
  if (!DIGEST[digestFor]) { console.error("--digest takes 0H, 3H, 6H or 12H"); process.exit(2); }
  console.log(DIGEST[digestFor]());
  process.exit(0);
}
function gate(id) {
  return ((gates && gates.entries) || []).filter(function (e) { return e.step === id; }).sort(function (a, b) {
    return a.date < b.date ? -1 : 1; }).pop();
}
function checkGate(id, decisions) {
  var g = gate(id);
  if (!gates) { notStarted(id, "no registers/gates.json"); return null; }
  if (!g) { notStarted(id, "no " + id + " entry in registers/gates.json"); return null; }
  if (decisions.indexOf(g.decision) < 0) fail(id, id + " decision \"" + g.decision + "\" is not one of " + decisions.join(", "));
  if (g.digest !== DIGEST[id]()) { step(id).status = "STALE"; fail(id, "what " + id + " covers has changed since " + g.by + " signed on " + g.date + "; it must be signed again"); }
  return g;
}

/* ------------------------------------------------------------------- 0H */
(function () {
  if (!refSet) { if (!R["0H"]) notStarted("0H", "no " + path.relative(ROOT, path.join(JUR, "reference-set.json"))); return; }
  var kinds = {};
  refSet.items.forEach(function (it) {
    kinds[it.kind] = 1;
    if (!it.sha256 && !it.no_copy_reason) fail("0H", it.id + ": neither a sha256 nor a no_copy_reason");
    if (it.sha256 && it.local_path) {
      var f = path.join(JUR, it.local_path);
      if (!exists(f)) fail("0H", it.id + ": " + it.local_path + " is missing");
      else if (sha(fs.readFileSync(f)) !== it.sha256) fail("0H", it.id + ": " + it.local_path + " does not match its sha256");
    }
  });
  if (!kinds.interpretation) fail("0H", "no interpretation legislation in the set");
  if (!kinds["drafting-manual"] && !kinds["style-guide"]) note("0H", "no drafting manual or style guide in the set: Style (S) cannot run unless 0H names a stand-in");
  refSet.library.forEach(function (m) { if (!exists(path.join(JUR, m.file))) fail("0H", "library module " + m.file + " is missing"); });
  if (!refSet.confirmed) { if (!step("0H").problems.length) step("0H").status = "OPEN"; fail("0H", "not confirmed: a human signs reference-set.json's \"confirmed\""); return; }
  if (refSet.confirmed.digest !== DIGEST["0H"]()) { step("0H").status = "STALE"; fail("0H", "the reference set has changed since " + refSet.confirmed.by + " confirmed it on " + refSet.confirmed.date); }
  (refSet.confirmed.missing || []).forEach(function (m) { note("0H", "knowingly missing: " + m.what + " (" + m.why + ")"); });
})();

/* ------------------------------------------------------------------- 1A */
var docIds = {};
(function () {
  if (bundleR.missing) { notStarted("1A", "no registers/source-bundle.json"); return; }
  if (bundleR.error) { fail("1A", bundleR.error); return; }
  (bundle.documents || []).forEach(function (d) { docIds[d.id] = d; });
  var doc = docIds[manifest.instrument.document];
  if (!doc) { fail("1A", "the instrument \"" + manifest.instrument.document + "\" is not in source-bundle.json"); return; }
  (bundle.documents || []).forEach(function (d) {
    var integ = d.integrity || {};
    if (!integ.sha256) { if (d === doc) fail("1A", d.id + ": no sha256"); return; }
    if (integ.local_path) {
      var f = resolve(integ.local_path);
      if (!exists(f)) fail("1A", d.id + ": " + integ.local_path + " is missing");
      else if (sha(fs.readFileSync(f)) !== integ.sha256) fail("1A", d.id + ": " + integ.local_path + " does not match its sha256");
    } else if (d === doc) fail("1A", d.id + ": no local copy, so its fingerprint cannot be rechecked");
  });
  if (!doc.licence) note("1A", "the instrument's licence is not recorded");
  note("1A", manifest.instrument.title + ", " + manifest.instrument.print);
})();

/* ------------------------------------------------------------------- 2A */
(function () {
  if (!searchLog && !R["2A"]) notStarted("2A", "no registers/search-log.json");
  if (!refReg && step("2A").status !== "NOT STARTED") fail("2A", "no registers/reference-register.json");
  if (searchLog) searchLog.searches.forEach(function (s) {
    (s.found || []).forEach(function (id) { if (!docIds[id]) fail("2A", s.id + " found " + id + ", which is not in source-bundle.json"); });
    if (s.outcome === "refused" || s.outcome === "not-found") note("2A", s.id + ": " + s.outcome + " (" + s.route + ")");
  });
  if (refReg) refReg.entries.forEach(function (e) {
    if (e.disposition === "encoded") {
      if (!e.module) fail("2A", e.id + ": encoded, but names no module");
    } else if (!e.reason) fail("2A", e.id + ": " + e.disposition + " needs a reason");
    if (e.depth > 1 && !e.deeper_because) fail("2A", e.id + ": depth " + e.depth + " needs deeper_because, naming the finding");
    if (e.deeper_because && !findings.some(function (f) { return f.id === e.deeper_because || (f.aliases || []).indexOf(e.deeper_because) >= 0; }))
      fail("2A", e.id + ": deeper_because names " + e.deeper_because + ", which is not a finding");
  });
})();

/* ------------------------------------------------------------------- 3H */
(function () {
  var g = checkGate("3H", ["confirmed"]);
  if (g) (g.missing || []).forEach(function (m) { note("3H", "knowingly missing: " + m.what + " (" + m.why + ")"); });
})();

/* ------------------------------------------------------------------- 4A */
(function () {
  if (!coverage) { if (!R["4A"]) notStarted("4A", "no coverage.json"); return; }
  moduleFiles().forEach(function (f) { if (!exists(f)) fail("4A", path.relative(SUB, f) + " is missing"); });
  if (S && S.error) fail("4A", "scheme: " + S.error);
  coverage.not_encoded.forEach(function (n) { note("4A", "not encoded: " + n.provisions + " (" + n.reason + ")"); });
  if (runL4) {
    if (!exists(L4)) { fail("4A", "--l4: no l4 binary at " + L4 + " (set L4_BIN)"); return; }
    moduleFiles().filter(exists).forEach(function (f) {
      var r = cp.spawnSync(L4, ["check", path.basename(f)], { cwd: path.dirname(f), encoding: "utf8" });
      var out = (r.stdout || "") + (r.stderr || "");
      /* "Check succeeded" can sit beside an import error (H-03), so read the output, not the banner */
      if (r.status !== 0 || /\berror\b/i.test(out.replace(/0 errors?/gi, ""))) fail("4A", "l4 check " + path.basename(f) + ": " + out.trim().split("\n").slice(0, 3).join(" | "));
    });
    note("4A", "l4 check ran over " + moduleFiles().length + " module(s)");
    /* and every module holding #ASSERTs is run: 4A is not done while a case fails */
    moduleFiles().filter(exists).filter(function (f) { return /^#ASSERT/m.test(fs.readFileSync(f, "utf8")); }).forEach(function (f) {
      var r = cp.spawnSync(L4, ["run", path.basename(f)], { cwd: path.dirname(f), encoding: "utf8", maxBuffer: 64 * 1024 * 1024 });
      var out = (r.stdout || "") + (r.stderr || "");
      var ok = (out.match(/Message:\s+assertion satisfied/gi) || []).length, bad = (out.match(/Message:\s+assertion failed/gi) || []).length;
      if (bad || (r.status !== 0 && !ok)) fail("4A", "l4 run " + path.basename(f) + ": " + (bad ? bad + " failed assertion(s)" : "exited " + r.status));
      else note("4A", "l4 run " + path.basename(f) + ": " + ok + " assertion(s) satisfied");
    });
  }
})();

/* ------------------------------------------------------------------- 5A */
var forkIds = {};
(function () {
  if (forksR.missing) { notStarted("5A", "no registers/fork-register.json (an empty register with a note is a result)"); return; }
  if (forksR.error) { fail("5A", forksR.error); return; }
  if (forks.kind !== "fork-register") fail("5A", "fork-register.json: kind is not \"fork-register\"");
  (forks.entries || []).forEach(function (e) {
    forkIds[e.id] = 1;
    if ((e.readings || []).length < 2) fail("5A", e.id + ": a fork needs at least two readings");
    if (!("taken" in e) && !(e.readings || []).some(function (r) { return r.taken; })) fail("5A", e.id + ": says which reading is taken nowhere");
  });
  if (!(forks.entries || []).length && !forks.note) fail("5A", "no forks and no note saying none were found");
})();

/* ------------------------------------------------------------------- 6H */
(function () {
  var g = checkGate("6H", ["certified", "waived"]);
  if (!g) return;
  if (g.decision === "waived") {
    if (!g.reason) fail("6H", "a waiver needs a reason");
    if (step("6H").status === "DONE") step("6H").status = "WAIVED";
    note("6H", "waived by " + g.by + ": " + (g.reason || "no reason"));
  }
  if (g.by === manifest.legal_engineer) note("6H", "signed by the legal engineer who ran the encoding; whether 6H must be someone else is not yet decided");
})();

/* ------------------------------------------------------------------- 7A */
var byId = {};
(function () {
  if (!incidents) { if (!R["7A"] || !R["7A"].problems.length) notStarted("7A", "no incidents.json"); return; }
  var nums = {};
  findings.forEach(function (f) {
    byId[f.id] = f; (f.aliases || []).forEach(function (a) { byId[a] = f; });
    var m = /^([A-Z])-(\d+)$/.exec(f.id);
    if (m && m[1] !== f.category) fail("7A", f.id + ": its letter is not its category (" + f.category + ")");
    if (m && +m[2] !== f.number) fail("7A", f.id + ": its number is not " + f.number);
    if (nums[f.number]) fail("7A", f.id + ": number " + f.number + " is also " + nums[f.number]);
    nums[f.number] = f.id;
  });
  if (!probe) { fail("7A", "no registers/probe-record.json"); return; }
  var parts = ((coverage && coverage.parts) || []).map(function (p) { return p.part; }), done = {};
  probe.runs.forEach(function (r) {
    r.parts.forEach(function (p) {
      if (parts.indexOf(p) < 0) fail("7A", "probe run " + r.category + " names Part \"" + p + "\", which coverage.json does not");
      done[r.category + "\0" + p] = 1;
    });
    r.candidates.forEach(function (c) { if (!byId[c]) fail("7A", "probe run " + r.category + " produced " + c + ", which is not in incidents.json"); });
  });
  var gaps = [];
  CATS.forEach(function (c) { parts.forEach(function (p) { if (!done[c + "\0" + p]) gaps.push(c + " over " + p); }); });
  if (gaps.length) fail("7A", "not yet probed: " + gaps.join("; "));
  var probed = {};
  probe.runs.forEach(function (r) { r.candidates.forEach(function (c) { probed[c] = 1; }); });
  findings.forEach(function (f) {
    if (f.found_by !== "EXT" && !probed[f.id] && !(f.aliases || []).some(function (a) { return probed[a]; }))
      fail("7A", f.id + " is in no probe run's candidates");
  });
})();

/* ------------------------------------------------------------------- 8A */
var scenarioRefs = null;   /* finding id -> labels of scenarios in which it fires, for 11A */
(function () {
  if (!incidents) { notStarted("8A", "no incidents.json"); return; }
  var schemeOK = S && !S.error;
  findings.forEach(function (f) {
    var ids = [f.id].concat(f.aliases || []);
    if (!f.evidence.length && !f.opinion) fail("8A", f.id + ": no evidence, and not labelled opinion");
    if (f.opinion && !f.evidence.length) note("8A", f.id + " is opinion");
    if (f.category === "U" && (!f.fork || !forkIds[f.fork])) fail("8A", f.id + ": an Uncertainty finding must name its fork-register entry");
    f.evidence.forEach(function (ev, i) {
      var at = f.id + " evidence " + (i + 1) + " (" + ev.kind + ")";
      if (ev.kind === "assert") {
        var file = resolve(ev.file);
        if (!ev.file || !exists(file)) { fail("8A", at + ": file " + ev.file + " is missing"); return; }
        if (!ev.text || norm(fs.readFileSync(file, "utf8")).indexOf(norm(ev.text)) < 0) fail("8A", at + ": the assertion is not in " + ev.file);
        else if (!/^#ASSERT/.test(norm(ev.text))) fail("8A", at + ": the text is not an #ASSERT");
      } else if (ev.kind === "quote") {
        var src = docIds[ev.document] || null, f2 = null;
        if (src && src.integrity && src.integrity.local_path) f2 = resolve(src.integrity.local_path);
        var item = refSet && refSet.items.filter(function (x) { return x.id === ev.document; })[0];
        if (item && item.local_path) f2 = path.join(JUR, item.local_path);
        if (!f2 || !exists(f2)) { fail("8A", at + ": no pinned copy of \"" + ev.document + "\" to quote from"); return; }
        if (!ev.quote || norm(fs.readFileSync(f2, "utf8")).indexOf(norm(ev.quote)) < 0) fail("8A", at + ": the quoted words are not in " + ev.document);
      } else if (!schemeOK) fail("8A", at + ": the scheme does not load");
      else if (ev.kind === "scenario") {
        var r = playScenario(S, ev.label);
        if (!r) fail("8A", at + ": no scenario labelled \"" + ev.label + "\"");
        else {
          r.errs.forEach(function (e) { fail("8A", at + ": " + e); });
          if (!r.refs.some(function (x) { return ids.indexOf(x) >= 0; })) fail("8A", at + ": \"" + ev.label + "\" does not record " + f.id);
        }
      } else if (ev.kind === "simulation") {
        if (!S.scheme.simulation) fail("8A", at + ": the scheme has no simulation section");
        else if (typeof ev.seed !== "number") fail("8A", at + ": a simulation needs its seed");
        else if (!simulate(S, ev).some(function (x) { return ids.indexOf(x) >= 0; }))
          fail("8A", at + ": seed " + ev.seed + " over " + (ev.days || 365) + " days does not record " + f.id);
      }
    });
  });
  if (runL4) {
    var cases = {};
    findings.forEach(function (f) { f.evidence.forEach(function (ev) { if (ev.kind === "assert" && ev.file) cases[resolve(ev.file)] = 1; }); });
    Object.keys(cases).filter(exists).forEach(function (file) {
      var r = cp.spawnSync(L4, ["run", path.basename(file)], { cwd: path.dirname(file), encoding: "utf8" });
      var out = (r.stdout || "") + (r.stderr || "");
      /* each result prints twice; the "Message:" line is counted once per directive */
      var ok = (out.match(/Message:\s+assertion satisfied/gi) || []).length, bad = out.match(/Message:\s+assertion failed/gi);
      if (r.status !== 0 && !bad && !ok) bad = ["l4 run exited " + r.status];
      if (bad) fail("8A", "l4 run " + path.basename(file) + ": " + bad.length + " failed assertion(s)");
      else note("8A", "l4 run " + path.basename(file) + ": " + ok + " assertion(s) satisfied");
    });
  }
})();

/* ------------------------------------------------------------------- 9A */
(function () {
  if (!incidents) { notStarted("9A", "no incidents.json"); return; }
  var setIds = {};
  ((refSet && refSet.items) || []).forEach(function (x) { setIds[x.id] = "0H"; });
  Object.keys(docIds).forEach(function (k) { setIds[k] = "3H"; });
  findings.forEach(function (f) {
    if (f.status === "CANDIDATE") { fail("9A", f.id + " is still a CANDIDATE"); return; }
    if (!f.challenged) fail("9A", f.id + ": no record of its challenge");
    if (f.status === "OPEN" && /^none/.test(f.severity)) fail("9A", f.id + ": OPEN with severity none");
    if (f.status === "VERIFIED-NO-DEFECT") {
      if (!f.answered_by) fail("9A", f.id + ": verified sound, but names nothing that answered it");
      else if (!setIds[f.answered_by.source])
        fail("9A", f.id + ": answered by \"" + f.answered_by.source + "\", which is in neither the 0H nor the 3H set; add it there");
    }
    if (f.found_by === "EXT" && !f.external_source) fail("9A", f.id + ": found externally, but whose finding it was is not recorded");
  });
  /* triage: every OPEN finding is a headline, a drafting note, or merged into another finding. Runs made
     before triage was added carry no tiers at all and are not held to it. */
  if (!findings.some(function (f) { return f.tier; })) return;
  var heads = [];
  findings.forEach(function (f) {
    if (f.status !== "OPEN") {
      if (f.tier) fail("9A", f.id + ": only OPEN findings are triaged, but it has tier " + f.tier);
      return;
    }
    if (["headline", "note", "merged"].indexOf(f.tier) < 0) { fail("9A", f.id + ": OPEN but not triaged (headline, note or merged)"); return; }
    if (f.tier === "headline") {
      heads.push(f);
      if (!f.plain_title) fail("9A", f.id + ": a headline needs a plain title");
      if (!f.story) fail("9A", f.id + ": a headline needs a story");
      if (!(f.rank >= 1)) fail("9A", f.id + ": a headline needs a rank");
    }
    if (f.tier === "merged") {
      var into = byId[f.merged_into];
      if (!into) fail("9A", f.id + ": merged into " + f.merged_into + ", which is not in the register");
      else if (into.status !== "OPEN" || into.tier === "merged") fail("9A", f.id + ": merged into " + f.merged_into + ", which is not an OPEN headline or note");
    } else if (f.merged_into) fail("9A", f.id + ": has merged_into but is not tier merged");
  });
  if (heads.length > MAX_HEADLINES) fail("9A", heads.length + " headlines; at most " + MAX_HEADLINES + ": move the weakest to drafting notes");
  var ranks = heads.map(function (f) { return f.rank; }).sort(function (a, b) { return a - b; });
  ranks.forEach(function (r, i) { if (r !== i + 1) { fail("9A", "headline ranks must run 1 to " + heads.length + " without gaps or repeats"); ranks.length = 0; } });
})();

/* ------------------------------------------------------------------ 10A */
(function () {
  if (!incidents) { notStarted("10A", "no incidents.json"); return; }
  findings.forEach(function (f) {
    if (!f.checked_print) { fail("10A", f.id + ": not yet checked against the current print"); return; }
    if (f.checked_print.print !== manifest.instrument.print)
      fail("10A", f.id + ": checked against " + f.checked_print.print + ", but the current print is " + manifest.instrument.print);
    if (f.challenged && f.checked_print.date < f.challenged.date) fail("10A", f.id + ": checked against the print before it was challenged");
  });
})();

/* ------------------------------------------------------------------ 11A */
(function () {
  var report = path.join(SUB, "REPORT.md");
  if (!exists(report)) { notStarted("11A", "no REPORT.md"); }
  else {
    var txt = fs.readFileSync(report, "utf8");
    findings.forEach(function (f) { if (txt.indexOf(f.id) < 0) fail("11A", "REPORT.md does not mention " + f.id); });
  }
  if (!S || S.error) { fail("11A", "the console scheme does not load"); return; }
  var obsRefs = {};
  (S.scheme.observations || []).forEach(function (o) {
    if (!o.ref) return;
    obsRefs[o.ref] = o;
    if (/^[A-Z]-\d{2,}$/.test(o.ref) && !byId[o.ref]) fail("11A", "the scheme shows " + o.ref + ", which is not in incidents.json");
  });
  var shown = {};
  (S.scheme.scenarios || []).forEach(function (sc) {
    var r = playScenario(S, sc.label);
    r.refs.forEach(function (x) { shown[x] = 1; });
  });
  findings.forEach(function (f) {
    var ids = [f.id].concat(f.aliases || []);
    var o = ids.map(function (x) { return obsRefs[x]; }).filter(Boolean)[0];
    if (!o) { fail("11A", f.id + " is not in the console scheme"); return; }
    if (o.ref !== f.id) fail("11A", "the scheme shows " + f.id + " under its old ID " + o.ref);
    if (o.foundBy && o.foundBy !== f.found_by) fail("11A", f.id + ": the scheme says found by " + o.foundBy + ", the register " + f.found_by);
    if (!o.foundBy) fail("11A", f.id + ": the scheme does not say how it was found");
    if (o.static && ["F", "S"].indexOf(f.category) < 0) fail("11A", f.id + ": only Form and Style findings may be static in the scheme");
    if (f.status === "OPEN" && !o.static && !ids.some(function (x) { return shown[x]; }))
      fail("11A", f.id + " is OPEN but no scenario in the scheme shows it");
  });
  if (!S.scheme.simulation) fail("11A", "the scheme has no simulation section");
  /* triage travels with the finding: same tier in the scheme, and a headline under its plain title */
  findings.forEach(function (f) {
    var o = obsRefs[f.id];
    if (!o || !f.tier) return;
    if (o.tier !== f.tier) fail("11A", f.id + ": the register says " + f.tier + ", the scheme " + (o.tier || "nothing"));
    if (f.tier === "headline" && o.label !== f.plain_title) fail("11A", f.id + ": the scheme does not show the headline's plain title");
    if (f.tier === "headline" && o.rank !== f.rank) fail("11A", f.id + ": the scheme ranks it " + o.rank + ", the register " + f.rank);
    if (f.tier === "merged" && o.mergedInto !== f.merged_into) fail("11A", f.id + ": the scheme does not show it merged into " + f.merged_into);
  });
  if (exists(report)) {
    var rtxt = fs.readFileSync(report, "utf8");
    findings.forEach(function (f) {
      if (f.tier === "headline" && rtxt.indexOf(f.plain_title) < 0) fail("11A", "REPORT.md does not give " + f.id + " under its plain title");
    });
  }
})();

/* ------------------------------------------------------------------ 12H */
(function () {
  var g = checkGate("12H", ["released"]);
  if (g && !g.recipient) fail("12H", "a release needs a recipient");
  if (g) note("12H", "released to " + (g.recipient || "?") + " by " + g.by + " on " + g.date);
  /* agent steps may run ahead of an unsigned gate, provisionally; nothing may be released on them */
  if (g) STEPS.slice(0, 12).forEach(function (s) {
    var r = step(s[0]), ok = (r.status === "DONE" || r.status === "WAIVED") && !r.problems.length;
    if (!ok) fail("12H", "released while " + s[0] + " " + s[1] + " is not complete");
  });
})();

/* ------------------------------------------------------------------ 13A */
(function () {
  if (!releases) { if (!R["13A"]) notStarted("13A", "no registers/release-log.json"); return; }
  var g = gate("12H");
  if (!releases.releases.length) { fail("13A", "the release log is empty"); return; }
  releases.releases.forEach(function (r) {
    if (!g || r.gate_digest !== g.digest) fail("13A", "release on " + r.date + " to " + r.recipient + " is not under the current 12H signature");
    if (r.print !== manifest.instrument.print) fail("13A", "release on " + r.date + " was against " + r.print + ", not the current print");
  });
})();

/* ----------------------------------------------------------------- sign */
if (SIGN) {
  var st = SIGN.step, idx = STEPS.map(function (s) { return s[0]; }).indexOf(st);
  if (["0H", "3H", "6H", "12H"].indexOf(st) < 0) { console.error("--sign takes 0H, 3H, 6H or 12H"); process.exit(2); }
  if (!SIGN.by || SIGN.by.trim().split(/\s+/).length < 2) { console.error("--by needs the signer's full name, as they typed it"); process.exit(2); }
  if (jurOnly && st !== "0H") { console.error("--jurisdiction signs 0H only"); process.exit(2); }
  /* a step may be approved only when every step before it is complete, and its own files are */
  var before = STEPS.slice(0, idx).filter(function (s) {
    var r = step(s[0]); return !((r.status === "DONE" || r.status === "WAIVED") && !r.problems.length); });
  if (before.length) { console.error("Cannot sign " + st + ": " + before.map(function (s) { return s[0]; }).join(", ") + " not complete."); process.exit(1); }
  var mine = step(st).problems.filter(function (p) { return !/^no .*gates\.json|^no \w+ entry|^not confirmed|has changed since|must be signed again/.test(p); });
  if (mine.length) { console.error("Cannot sign " + st + ":\n  - " + mine.join("\n  - ")); process.exit(1); }
  var _d = new Date(), today = _d.getFullYear() + "-" + String(_d.getMonth() + 1).padStart(2, "0") + "-" + String(_d.getDate()).padStart(2, "0"), missingList = [];
  if (SIGN.missing) missingList = JSON.parse(fs.readFileSync(SIGN.missing, "utf8"));
  if (st === "0H") {
    var rf = path.join(JUR, "reference-set.json"), rs = JSON.parse(fs.readFileSync(rf, "utf8"));
    if (!SIGN.statement) { console.error("0H needs --statement"); process.exit(2); }
    rs.confirmed = { by: SIGN.by.trim(), date: today, digest: DIGEST["0H"](), how: "full name typed in the conversation",
                     statement: SIGN.statement, missing: missingList };
    fs.writeFileSync(rf, JSON.stringify(rs, null, 2) + "\n");
  } else {
    var gf = reg("gates.json"), gd = exists(gf) ? JSON.parse(fs.readFileSync(gf, "utf8"))
      : { kind: "gates", version: 1, subject: manifest.subject, entries: [] };
    var dec = SIGN.decision || { "3H": "confirmed", "6H": "certified", "12H": "released" }[st];
    if (dec === "waived" && !SIGN.reason) { console.error("a waiver needs --reason"); process.exit(2); }
    if (st === "12H" && !SIGN.recipient) { console.error("12H needs --recipient"); process.exit(2); }
    var e = { step: st, decision: dec, by: SIGN.by.trim(), date: today, digest: DIGEST[st](), how: "full name typed in the conversation" };
    ["statement", "reason", "recipient"].forEach(function (k) { if (SIGN[k]) e[k] = SIGN[k]; });
    if (missingList.length) e.missing = missingList;
    gd.entries.push(e);
    fs.writeFileSync(gf, JSON.stringify(gd, null, 2) + "\n");
  }
  console.log(st + " signed by " + SIGN.by.trim() + " on " + today + ". Run the check again to see the next step.");
  process.exit(0);
}

/* --------------------------------------------------------------- report */
if (jurOnly) {
  var r0 = step("0H");
  if (r0.status === "DONE" && r0.problems.length) r0.status = "OPEN";
  console.log("LQA check: reference set at " + JUR + "\n\n0H   Jurisdiction " + r0.status);
  r0.problems.forEach(function (p) { console.log("       - " + p); });
  r0.notes.forEach(function (n) { console.log("       \u00b7 " + n); });
  process.exit(r0.status === "DONE" ? 0 : 1);
}
var blocked = false, allDone = true;
console.log("LQA check: " + manifest.subject + " (" + manifest.instrument.title + ", " + manifest.instrument.print + ")\n");
/* steps run strictly in order: once one is incomplete, every later step waits for it */
STEPS.forEach(function (s) {
  var r = step(s[0]);
  if ((r.status === "DONE" || r.status === "WAIVED") && r.problems.length) r.status = "OPEN";
  if (blocked) { console.log((s[0] + "     ").slice(0, 5) + (s[1] + "            ").slice(0, 13) + "WAITING for " + blocked); return; }
  console.log((s[0] + "     ").slice(0, 5) + (s[1] + "            ").slice(0, 13) + r.status);
  r.problems.forEach(function (p) { console.log("       - " + p); });
  r.notes.forEach(function (n) { console.log("       · " + n); });
  if (r.status !== "DONE" && r.status !== "WAIVED") { blocked = s[0]; allDone = false; }
});
var counts = {};
findings.forEach(function (f) { var k = f.status; counts[k] = (counts[k] || 0) + 1; });
var methods = {};
findings.forEach(function (f) { methods[f.found_by] = (methods[f.found_by] || 0) + 1; });
console.log("\nFindings: " + (findings.length ? Object.keys(counts).map(function (k) { return counts[k] + " " + k; }).join(", ") : "none") +
  (findings.length ? "\nFound by: " + Object.keys(methods).map(function (k) { return k + " " + methods[k]; }).join(", ") : ""));
process.exit(allDone ? 0 : 1);
