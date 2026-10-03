/* Correctness pass over the console's engine + schemes. */
var fs = require("fs"), vm = require("vm"), path = require("path");
var dir = __dirname;   /* engine.js and schemes.js sit beside this file */
var sandbox = { window: {}, console: console };
sandbox.window.window = sandbox.window;
vm.createContext(sandbox);
["engine.js", "schemes.js"].forEach(function (f) {
  vm.runInContext(fs.readFileSync(path.join(dir, f), "utf8"), sandbox, { filename: f });
});
var Engine = sandbox.window.Engine, SCHEMES = sandbox.window.SCHEMES;
var problems = [];
function bad(m) { problems.push(m); }

function runScenario(eng, sc) {
  return eng.play(sc, function (e) { bad(sc.label + ": " + e.message); })(sc.focus);
}

/* ---------------------------------------------------------------- calendar */
console.log("=== calendar ===");
(function () {
  var eng = new Engine(SCHEMES[0]);            /* startDate 2026-01-01 */
  if (eng.formatDate(0) !== "1 Jan 2026") bad("day 0 is not the start date: " + eng.formatDate(0));
  if (eng.dayForDate("2026-01-01") !== 0) bad("dayForDate round trip failed");
  /* a pup whelped on day 0 is 3 months old on 1 April, day 90 - not day 60 */
  var pup = eng.spawn("dog", "T", { bornDate: "2026-01-01", restrictedBreed: true, sterilised: false }, { owner: "p1" });
  if (eng.monthsSince(pup.attrs.bornDay) !== 0) bad("newborn is not 0 months old");
  for (var i = 0; i < 89; i++) eng.tick();
  if (eng.monthsSince(pup.attrs.bornDay) !== 2) bad("at day 89 the pup should still be 2 months, got " + eng.monthsSince(pup.attrs.bornDay));
  eng.tick();
  if (eng.monthsSince(pup.attrs.bornDay) !== 3) bad("at day 90 (1 Apr) the pup should be 3 months, got " + eng.monthsSince(pup.attrs.bornDay));
  console.log("  day 89 -> " + eng.formatDate(89) + ", 2 months | day 90 -> " + eng.formatDate(90) + ", 3 months");
  /* age keeps moving without anyone touching it */
  var rex = eng.get("d1"), before = eng.monthsSince(rex.attrs.bornDay);
  for (i = 0; i < 365; i++) eng.tick();
  var after = eng.monthsSince(rex.attrs.bornDay);
  if (after !== before + 12) bad("a year of ticks did not add 12 months (" + before + " -> " + after + ")");
  console.log("  Rex ages " + before + " -> " + after + " months over a year of ticks");
  /* scenario-mode age entry round trips */
  var e2 = new Engine(SCHEMES[1]);
  var d = e2.dayForYearsAgo(17);
  if (e2.monthsSince(d) !== 17 * 12) bad("dayForYearsAgo(17) does not read back as 17");
  console.log("  scenario age 17 -> born " + e2.formatDate(d) + " -> reads back " +
    Math.floor(e2.monthsSince(d) / 12));
})();

/* --------------------------------------------------------------- scenarios */
SCHEMES.forEach(function (scheme) {
  console.log("\n=== " + scheme.title + " ===");
  (scheme.scenarios || []).forEach(function (sc) {
    var eng = new Engine(scheme);
    var focus = runScenario(eng, sc);
    if (sc.focus && !eng.get(focus)) bad(sc.label + ": focus resolves to nothing");
    var fired = Object.keys(eng.counts).filter(function (k) { return eng.counts[k]; })
      .map(function (k) { return k + "=" + eng.counts[k]; });
    eng.log.filter(function (l) {
      return /could not be applied|Could not apply|failed/.test(l.text); })
      .forEach(function (b) { bad(sc.label + ": " + b.text.replace(/<[^>]+>/g, "")); });
    /* every observation should carry the mode the scenario ran in */
    eng.observed.forEach(function (o) {
      if (o.context !== (sc.mode === "nature" ? "nature" : "god")) {
        bad(sc.label + ": observation " + o.id + " tagged " + o.context);
      }
    });
    console.log("  [" + (sc.mode || "god") + ", day " + eng.day + " = " +
      eng.formatDate(eng.day) + ", cast " + eng.order.length + "] " + sc.label);
    console.log("      " + (fired.length ? fired.join(", ") : "no observations"));
    eng.log.filter(function (l) { return l.sev === "stop"; }).forEach(function (l) {
      console.log("      STOP  " + l.text.replace(/<[^>]+>/g, "").slice(0, 92) + "…");
    });
  });
});

/* -------------------------------------- creation under both ways of working */
console.log("\n=== creating actors ===");
SCHEMES.forEach(function (s) {
  [false, true].forEach(function (sim) {
    var eng = new Engine(s);
    eng.setContext(sim ? "nature" : "god");
    eng.creatableTypes().forEach(function (t) {
      var fi = eng.settableAtBirth(t.id, sim), ri = eng.settableRels(t.id, sim), attrs = {}, rels = {};
      fi.fields.forEach(function (f) {
        attrs[f.key] = f.def !== undefined ? f.def
          : (f.type === "bool" ? false : (f.type === "number" ? 0 : "x"));
      });
      fi.locked.forEach(function (f) { if (f.type === "bool") attrs[f.key] = false; });
      if (fi.birth) {
        attrs.bornDay = sim ? eng.day
          : (fi.birth.unit === "years" ? eng.dayForYearsAgo(fi.birth.def)
                                       : eng.dayForMonthsAgo(fi.birth.def));
      }
      ri.rels.forEach(function (r) {
        var c = eng.ofType(r.target)[0];
        if (r.required && !c) bad(s.title + ": " + t.id + " needs a " + r.target + " and none exists");
        if (c) rels[r.key] = c.id;
      });
      var ent = eng.spawn(t.id, "Test " + t.id, attrs, rels);
      if (!eng.get(ent.id)) bad(s.title + ": spawn of " + t.id + " produced nothing");
      if (sim && fi.birth && eng.monthsSince(ent.attrs.bornDay) !== 0) {
        bad(s.title + ": " + t.id + " born in simulation mode is not 0 old");
      }
      if (sim) {
        fi.locked.forEach(function (f) {
          if (ent.attrs[f.key] === true) bad(s.title + ": " + t.id + "." + f.key + " was conferred at birth");
        });
        ri.locked.forEach(function (r) {
          if (ent.rels[r.key]) bad(s.title + ": " + t.id + "." + r.key + " was established at birth");
        });
      }
      for (var i = 0; i < 200; i++) eng.tick();
      eng.remove(ent.id, sim);
      if (eng.get(ent.id)) bad(s.title + ": remove left " + t.id + " behind");
    });
    eng.order.forEach(function (id) {
      var o = eng.get(id);
      Object.keys(o.rels || {}).forEach(function (k) {
        if (!eng.get(o.rels[k])) bad(s.title + ": dangling relationship " + k + " on " + o.label);
      });
    });
    console.log("  " + s.title + " · " + (sim ? "nature" : "god") + ": " +
      eng.creatableTypes().length + " type(s) created, aged 200 days, removed");
  });
});

/* ---- a conferred fact must have an act that confers it, and it must work ---- */
console.log("\n=== provenance ===");
SCHEMES.forEach(function (s) {
  var actionIds = (s.actions || []).map(function (a) { return a.id; });
  var typeIds = (s.types || []).map(function (t) { return t.id; });
  var obsIds = (s.observations || []).map(function (o) { return o.id; });
  var conferred = [];
  (s.types || []).forEach(function (t) {
    var cr = t.create || {};
    (cr.fields || []).concat(cr.rels || []).forEach(function (f) {
      if (f.origin !== "conferred") return;
      conferred.push(t.id + "." + f.key);
      if (!f.by) { bad(s.title + ": " + t.id + "." + f.key + " is conferred by nothing named"); return; }
      if (actionIds.indexOf(f.by) < 0) {
        bad(s.title + ": " + t.id + "." + f.key + " names a missing act " + f.by);
      }
      /* the named act must actually set it somewhere */
      var sets = (s.rules || []).some(function (r) {
        return r.on === "action:" + f.by && (r.then || []).some(function (e) {
          return e[0] === "set" && String(e[1]).indexOf("." + f.key) >= 0; });
      });
      if (!sets) bad(s.title + ": no rule on " + f.by + " ever sets " + f.key);
    });
    (cr.fields || []).forEach(function (f) {
      if (["birth", "innate", "conferred", "exogenous"].indexOf(f.origin || "innate") < 0) {
        bad(s.title + ": " + t.id + "." + f.key + " has an unknown origin " + f.origin);
      }
    });
  });
  (s.rules || []).forEach(function (r) {
    var on = r.on;
    if (on.indexOf("action:") === 0 && actionIds.indexOf(on.slice(7)) < 0) bad(s.title + ": rule " + r.id + " on missing action");
    if (on.indexOf("create:") === 0 && typeIds.indexOf(on.slice(7)) < 0) bad(s.title + ": rule " + r.id + " on missing type");
    if (on.indexOf("death:") === 0 && typeIds.indexOf(on.slice(6)) < 0) bad(s.title + ": rule " + r.id + " on missing type");
    if (on === "day" && r["for"] && typeIds.indexOf(r["for"]) < 0) bad(s.title + ": day rule " + r.id + " binds a missing type");
    (r.then || []).forEach(function (e) {
      if (e[0] === "observe" && obsIds.indexOf(e[1]) < 0) bad(s.title + ": rule " + r.id + " observes undeclared " + e[1]);
    });
  });
  (s.actions || []).forEach(function (a) {
    if (typeIds.indexOf(a.actor) < 0) bad(s.title + ": action " + a.id + " has unknown actor type");
    if (a.target && typeIds.indexOf(a.target) < 0) bad(s.title + ": action " + a.id + " has unknown target type");
  });
  /* the other direction: a declared observation nothing can ever record is dead weight,
     and usually means a rule was dropped */
  var observedBy = {};
  (s.rules || []).forEach(function (r) {
    (r.then || []).forEach(function (e) { if (e[0] === "observe") observedBy[e[1]] = true; });
  });
  /* a static observation is a finding no run can show (Style, Form): it is listed, never recorded */
  (s.observations || []).forEach(function (o) { if (o.static) observedBy[o.id] = true; });
  obsIds.forEach(function (id) {
    if (!observedBy[id]) bad(s.title + ": observation " + id + " is declared but no rule records it");
  });
  console.log("  " + s.title + ": " + conferred.length + " conferred fact(s) — " +
    (conferred.join(", ") || "none") + " — each traced to an act that sets it; " +
    obsIds.length + " observation(s), each reachable from a rule");
});

/* ------------------------------------------------ generated runs */
console.log("\n=== simulation: a year from the starting cast, default parameters, seed 1 ===");
function simulateYear(s, param) {
  var eng = new Engine(s), d;
  eng.seed(1);
  eng.startRun(s.simulation, param);
  for (d = 0; d < 365; d++) { eng.tick(); eng.generate(s.simulation); }
  return eng;
}
SCHEMES.forEach(function (s) {
  if (!s.simulation) { console.log("  " + s.title + ": no simulation section"); return; }
  var param = {};
  (s.simulation.params || []).forEach(function (p) { param[p.key] = p.def; });
  var eng = simulateYear(s, param);
  eng.log.filter(function (l) { return /failed|could not be applied|Could not apply/.test(l.text); })
    .slice(0, 5).forEach(function (l) { bad(s.title + " simulation: " + l.text.replace(/<[^>]+>/g, "")); });
  var fired = Object.keys(eng.counts).filter(function (k) { return eng.counts[k]; })
    .map(function (k) { return k + "=" + eng.counts[k]; });
  console.log("  " + s.title + ": cast " + eng.order.length + " at day 365, " + eng.log.length + " log lines");
  console.log("      " + (fired.join(", ") || "no observations"));
  if (simulateYear(s, param).log.length !== eng.log.length) bad(s.title + " simulation: seed 1 did not replay the same run");
  /* a generated run, saved as a scenario, must play back to the same place */
  var rec = new Engine(s); rec.seed(1); rec.startRecording(); rec.startRun(s.simulation, param);
  for (var d = 0; d < 120; d++) { rec.tick(); rec.generate(s.simulation); }
  var saved = { label: "saved run", mode: "nature", steps: rec.recorder.steps, empty: rec.recorder.empty };
  var back = new Engine(s); runScenario(back, saved);
  if (back.order.length !== rec.order.length || back.day !== rec.day) {
    bad(s.title + " simulation: a saved run plays back to cast " + back.order.length + " on day " + back.day +
        ", not " + rec.order.length + " on day " + rec.day);
  }
  console.log("      saved at day 120 as " + saved.steps.length + " steps; plays back to the same cast and day");
});

console.log("\n=== problems ===");
console.log(problems.length ? problems.join("\n") : "none");
