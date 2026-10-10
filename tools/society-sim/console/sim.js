/* Sim One console — the world, the clock, the cast, the chapters. Law is read from the scenario's
   facts file (what each event engaged and what it should have produced); in the working console
   that comes from L4, live. No rule of law is written here. */
(function () {
  "use strict";
  var D = window.SIM_DATA, F = D.facts, LEDGER = D.ledger, ROWS = D.rows || {};
  var $ = function (id) { return document.getElementById(id); };
  var SV = "http://www.w3.org/2000/svg";
  var DAY = 86400000;

  /* ---------- dates ---------- */
  function parse(s) { var p = s.split("-"); while (p.length < 3) p.push("01"); return Date.UTC(+p[0], +p[1] - 1, +p[2]); }
  function fmt(t) { var d = new Date(t); return d.getUTCDate() + " " + ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][d.getUTCMonth()] + " " + d.getUTCFullYear(); }
  function iso(t) { return new Date(t).toISOString().slice(0, 10); }
  function ageAt(born, t) { var b = new Date(born), d = new Date(t); var a = d.getUTCFullYear() - b.getUTCFullYear(); if (d.getUTCMonth() < b.getUTCMonth() || (d.getUTCMonth() === b.getUTCMonth() && d.getUTCDate() < b.getUTCDate())) a--; return a; }

  /* ---------- the cast ---------- */
  var PEOPLE = {}; F.people.forEach(function (p) { PEOPLE[p.id] = p; p.bornT = parse(p.born); p.diesT = p.dies ? parse(p.dies) : null; });
  var ORGS = {}; F.organisations.forEach(function (o) { ORGS[o.id] = o; });
  var NAMES = { simone: "Simone", marcus: "Marcus", kaien: "Kai En", kaixin: "Kai Xin", boonkeng: "Boon Keng", siewlan: "Siew Lan", junhao: "Jun Hao", ahhuat: "Ah Huat", meifong: "Mei Fong", meridian: "Meridian", "bank-employer": "the bank", straits: "Straits Eng." };
  var CH_TITLES = ["Born", "Preschool and primary school", "Secondary school, JC and three birthdays", "University", "First job", "A flat and a marriage", "First child", "Keys, a second child, the long middle", "Mid-life", "Retirement, old age, two deaths"];

  /* what a person is, as life confers it: the event that confers each chip, read from the script */
  var CONFERS = { e000: { simone: ["citizen"] }, e020: { simone: ["NRIC"] }, e021: { marcus: ["NSman"] }, e025: { simone: ["elector", "may make a will", "presumed donor"] },
    e030: { simone: ["undergraduate"] }, e034: { simone: ["graduate"] }, e040: { simone: ["employee"] }, e042: { simone: ["cardholder"] },
    e053: { simone: ["married"], marcus: ["married"] }, e062: { kaien: ["citizen"], simone: ["parent"], marcus: ["parent"] }, e070: { simone: ["owner"], marcus: ["owner"] },
    e075: { kaixin: ["citizen"] }, e076: { boonkeng: ["retired"] }, e07a: { boonkeng: ["CPF LIFE"] }, e083: { simone: ["will", "CPF nominee named"], marcus: ["will", "CPF nominee named"] },
    e085: { kaien: ["registered for NS"] }, e086: { kaien: ["NSF"] }, e088: { simone: ["executor"] }, e090: { simone: ["LPA"] }, e091: { marcus: ["LPA"] },
    e092: { marcus: ["retired"] }, e093: { marcus: ["CPF LIFE"] }, e094: { simone: ["retired"] }, e095: { simone: ["CPF LIFE"] }, e097: { simone: ["AMD"] }, e098: { simone: ["widow"] } };
  var EMPLOY = [ { who: "simone", org: "meridian", from: "2026-08-03", to: "2034-01-31" }, { who: "simone", org: "bank-employer", from: "2034-02-01", to: "2066-03-14" }, { who: "marcus", org: "straits", from: "2023-08-01", to: "2062-07-22" } ];
  var THINGS = F.homes.map(function (h) { return { id: h.id, label: h.id === "tampines-parents" ? "Tampines flat (parents)" : h.id === "pphs" ? "PPHS rental" : h.id === "tampines-north-bto" ? "Tampines North 4-room" : h.id === "punggol-ec" ? "Punggol EC" : "2-room Flexi", from: parse(h.from || h.bought || h.keys || h.applied), to: (h.to || h.sold) ? parse(h.to || h.sold) : null, owners: h.owner || h.occupier || [], kind: "home" }; })
    .concat([{ id: "car", label: "the car", from: parse("2034-06-15"), to: parse("2044-06-15"), owners: ["marcus", "simone"], kind: "thing" }, { id: "mochi", label: "Mochi", from: parse("2035-03-08"), to: parse("2049-03-08"), owners: ["simone", "marcus"], kind: "thing" }]);
  var AGENCY = [ [/^central-provident/, "CPF Board"], [/^income-tax|^stamp-duties|^property-tax|^goods-and-services|^inland-revenue/, "IRAS"], [/^housing-and-dev|^executive-condo|^town-councils/, "HDB"], [/^registration-of-births|^national-registration|^passports|^immigration/, "ICA"], [/^womens-charter/, "ROM"], [/^parliamentary-elections|^presidential-elections/, "ELD"], [/^employment-act|^employment-claims|^workplace|^work-injury|^retirement-and|^skills-development|^national-servicemen/, "MOM"], [/^child-development|^child-support|^early-childhood|^adoption/, "MSF / ECDA"], [/^medishield|^careshield|^healthcare|^medical|^infectious|^advance-medical|^human-organ|^mental-capacity/, "MOH"], [/^enlistment|^singapore-armed/, "MINDEF"], [/^compulsory-education|^education/, "MOE"], [/^succession|^probate|^wills|^intestate|^public-trustee|^family-justice/, "Family Justice Courts"], [/^customs/, "Customs"], [/^banking|^credit-bureau|^deposit-insurance|^insurance|^financial-advisers|^payment/, "MAS"], [/^constitution/, "the Constitution"], [/^road-traffic|^motor-vehicles|^parking/, "LTA"], [/^personal-data|^spam/, "PDPC"], [/^statistics|^census/, "SingStat"], [/^silver-support/, "Silver Support"], [/^animals/, "NParks AVS"], [/^land-titles|^building-strata|^estate-agents|^conveyancing/, "SLA / CEA"], [/^building-control/, "BCA"], [/^consumer-protection|^small-claims|^hire-purchase|^electricity|^public-utilities/, "Consumers / utilities"], [/^estate-duty/, "IRAS"] ];
  function agencyOf(slug) { for (var i = 0; i < AGENCY.length; i++) if (AGENCY[i][0].test(slug)) return AGENCY[i][1]; return "Other"; }
  function shortAct(slug) { return slug.replace(/-act-\d{4}$/, "").replace(/-\d{4}$/, "").replace(/-/g, " ").replace(/\b\w/g, function (c) { return c.toUpperCase(); }).replace(/^Pdpa$/, "PDPA").replace("Womens Charter", "Women's Charter"); }

  /* ---------- events and chapters ---------- */
  var EVENTS = F.events.map(function (e) { e.t = parse(e.date); e.tainted = e.law.some(function (l) { return l.status !== "ENC"; }); e.reqs = LEDGER.filter(function (r) { return r.trigger && r.trigger.event === e.id; }); return e; }).sort(function (a, b) { return a.t - b.t || (a.id < b.id ? -1 : 1); });
  var CHAPTERS = CH_TITLES.map(function (t, i) { var evs = EVENTS.filter(function (e) { return e.chapter === i; }); var ts = evs.map(function (e) { return e.t; }); return { n: i, title: t, start: Math.min.apply(null, ts), end: Math.max.apply(null, ts), events: evs }; });
  var DAY0 = PEOPLE.simone.bornT, NOW = parse(F.now), END = parse(PEOPLE.simone.dies);
  var clock = DAY0, sel = null, filterBeats = false, filterTaint = false;

  function chapterAt(t) { var c = 0; CHAPTERS.forEach(function (ch) { if (ch.start <= t) c = ch.n; }); return c; }
  function past() { return EVENTS.filter(function (e) { return e.t <= clock; }); }
  function alive(p) { return p.bornT <= clock && !(p.diesT && p.diesT <= clock); }
  function dead(p) { return p.diesT && p.diesT <= clock; }
  function chipsFor(pid) { var out = []; past().forEach(function (e) { var c = CONFERS[e.id]; if (c && c[pid]) c[pid].forEach(function (x) { if (out.indexOf(x) < 0) out.push(x); }); }); if (dead(PEOPLE[pid])) out.push("deceased"); return out; }
  function employerOf(pid) { var t = iso(clock), r = null; EMPLOY.forEach(function (x) { if (x.who === pid && x.from <= t && t <= x.to) r = x.org; }); return r; }

  /* ---------- clock ---------- */
  function setClock(t) { clock = Math.max(DAY0, Math.min(END + 30 * DAY, t)); render(); }
  function step(n) { setClock(clock + n * DAY); }
  function nextEvent() { for (var i = 0; i < EVENTS.length; i++) if (EVENTS[i].t > clock) { setClock(EVENTS[i].t); flash("→ " + EVENTS[i].title); return; } flash("Nothing further is scripted."); }
  function nextChapter() { var c = chapterAt(clock); if (c + 1 < CHAPTERS.length) { setClock(CHAPTERS[c + 1].start); flash("Chapter " + (c + 1) + " — " + CHAPTERS[c + 1].title); } else flash("That is the last chapter."); }
  function prevChapter() { var c = chapterAt(clock); var target = clock > CHAPTERS[c].start ? c : Math.max(0, c - 1); setClock(CHAPTERS[target].start); flash("Chapter " + target + " — " + CHAPTERS[target].title); }
  function flash(s) { var f = $("flash"); f.textContent = s; clearTimeout(f._t); f._t = setTimeout(function () { f.textContent = ""; }, 3500); }

  /* ---------- canvas ---------- */
  function el(name, attrs, text) { var n = document.createElementNS(SV, name), k; for (k in attrs) n.setAttribute(k, attrs[k]); if (text != null) n.appendChild(document.createTextNode(text)); return n; }
  var W = 960, H = 440, BANDS = [70, 215, 360];
  function colorFor(kind) { return kind === "person" ? "#8fa2e0" : kind === "org" ? "#e0a45c" : "#6cc79a"; }
  function nodes() {
    var ns = [];
    var agencies = {}; past().forEach(function (e) { e.law.forEach(function (l) { if (l.subject) { var a = agencyOf(l.subject); agencies[a] = (agencies[a] || 0) + 1; } }); });
    Object.keys(agencies).sort(function (a, b) { return agencies[b] - agencies[a]; }).slice(0, 7).forEach(function (a) { ns.push({ id: "ag:" + a, label: a, note: agencies[a] + (agencies[a] === 1 ? " touch" : " touches"), band: 0, kind: "org", shape: "rect" }); });
    EMPLOY.forEach(function (x) { if (employerOf(x.who) === x.org && !ns.some(function (n) { return n.id === "org:" + x.org; })) ns.push({ id: "org:" + x.org, label: NAMES[x.org], note: "employer", band: 0, kind: "org", shape: "rect" }); });
    F.people.forEach(function (p) { if (p.bornT > clock) return; var gone = dead(p); ns.push({ id: p.id, label: NAMES[p.id] + (gone ? " †" : ""), note: gone ? "died " + fmt(p.diesT) : ageAt(p.bornT, clock) + (p.id === "simone" ? " · Simone" : ""), band: 1, kind: "person", shape: "round", gone: gone, p: p }); });
    THINGS.forEach(function (h) { if (h.from <= clock && (!h.to || h.to > clock)) ns.push({ id: "th:" + h.id, label: h.label, note: h.kind === "home" ? "home" : "thing", band: 2, kind: "thing", shape: "rect", th: h }); });
    return ns;
  }
  function layout(ns) { var pos = {}; [0, 1, 2].forEach(function (b) { var row = ns.filter(function (n) { return n.band === b; }); var gap = W / (row.length + 1); row.forEach(function (n, i) { pos[n.id] = { x: gap * (i + 1), y: BANDS[b], w: Math.max(92, Math.min(176, n.label.length * 7.6 + 28)) }; }); }); return pos; }
  function drawCanvas() {
    var svg = $("canvas"); while (svg.firstChild) svg.removeChild(svg.firstChild);
    for (var gy = 40; gy < H; gy += 40) svg.appendChild(el("line", { x1: 0, y1: gy, x2: W, y2: gy, stroke: "var(--cv-grid)", "stroke-width": 1 }));
    [["authorities engaged", BANDS[0] - 38], ["people", BANDS[1] - 38], ["homes and things", BANDS[2] - 38]].forEach(function (b) { svg.appendChild(el("text", { x: 14, y: b[1], fill: "var(--cv-ink-2)", "font-family": "var(--mono)", "font-size": 10, "letter-spacing": 1.5 }, b[0].toUpperCase())); });
    var ns = nodes(), pos = layout(ns);
    function edge(a, b, dash, label) { var A = pos[a], B = pos[b]; if (!A || !B) return; svg.appendChild(el("line", { x1: A.x, y1: A.y, x2: B.x, y2: B.y, stroke: "var(--cv-edge)", "stroke-width": 1.5, "stroke-dasharray": dash })); if (label) svg.appendChild(el("text", { x: (A.x + B.x) / 2, y: (A.y + B.y) / 2 - 5, "text-anchor": "middle", fill: "var(--cv-ink-2)", "font-family": "var(--mono)", "font-size": 9.5 }, label)); }
    if (parse(F.marriage.solemnised) <= clock && pos.simone && pos.marcus) edge("simone", "marcus", "none", "spouses");
    F.people.forEach(function (p) { (p.parents || []).forEach(function (par) { if (pos[p.id] && pos[par]) edge(par, p.id, "2 4"); }); });
    THINGS.forEach(function (h) { if (pos["th:" + h.id]) h.owners.forEach(function (o) { if (pos[o] && alive(PEOPLE[o])) edge(o, "th:" + h.id, "5 4"); }); });
    EMPLOY.forEach(function (x) { if (employerOf(x.who) === x.org && pos[x.who]) edge(x.who, "org:" + x.org, "5 4", "employee"); });
    ns.forEach(function (n) {
      var p = pos[n.id], h = 46, c = colorFor(n.kind), isSel = sel === n.id;
      var g = el("g", { "class": "node", tabindex: 0, role: "button", "aria-label": n.label, opacity: n.gone ? 0.55 : 1 });
      g.appendChild(el("rect", { "class": "shape", x: p.x - p.w / 2, y: p.y - h / 2, width: p.w, height: h, rx: n.shape === "round" ? 22 : 9, fill: isSel ? c : "var(--cv-bg)", "fill-opacity": isSel ? 0.22 : 1, stroke: isSel ? c : "var(--cv-edge)", "stroke-width": isSel ? 3 : 1.5 }));
      g.appendChild(el("text", { x: p.x, y: p.y - 2, "text-anchor": "middle", fill: "var(--cv-ink)", "font-family": "var(--sans)", "font-size": 13, "font-weight": 600 }, n.label));
      g.appendChild(el("text", { x: p.x, y: p.y + 14, "text-anchor": "middle", fill: "var(--cv-ink-2)", "font-family": "var(--mono)", "font-size": 10 }, n.note));
      if (n.kind === "person" && chipsFor(n.id).length) g.appendChild(el("circle", { cx: p.x + p.w / 2 - 9, cy: p.y - h / 2 + 9, r: 4.5, fill: c, stroke: "var(--cv-bg)", "stroke-width": 1.5 }));
      g.appendChild(el("title", {}, n.label + (n.kind === "person" ? ": " + chipsFor(n.id).join(", ") : "")));
      g.addEventListener("click", function () { sel = n.id; render(); });
      g.addEventListener("keydown", function (ev) { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); sel = n.id; render(); } });
      svg.appendChild(g);
    });
    var aliveN = F.people.filter(alive).length, deadN = F.people.filter(dead).length;
    $("cast").textContent = aliveN + " alive" + (deadN ? " · " + deadN + " died" : "");
    $("hint-text").innerHTML = sel ? "<b>" + (ns.filter(function (n) { return n.id === sel; })[0] || { label: sel }).label + "</b> selected" : "Click an actor.";
  }

  /* ---------- inspector ---------- */
  function lawChip(l) { var s = document.createElement("span"); s.className = "cite"; s.dataset.s = l.status; s.textContent = l.subject ? shortAct(l.subject) : "(no instrument)"; if (l.sections) s.title = l.sections + (l.note ? " — " + l.note : ""); var st = document.createElement("span"); st.className = "st"; st.textContent = l.status; s.appendChild(st); return s; }
  function renderInspector() {
    var box = $("inspector"); box.innerHTML = "";
    if (!sel) { box.innerHTML = "<h3>Nobody selected</h3><p class='who'>the inspector</p><p class='empty'>Click a person, an authority, a home or a thing on the canvas to see what the law has made of them so far, and what is next.</p>"; return; }
    var h3 = document.createElement("h3"), who = document.createElement("p"); who.className = "who";
    if (PEOPLE[sel]) {
      var p = PEOPLE[sel]; h3.textContent = p.name; who.textContent = (dead(p) ? "died " + fmt(p.diesT) + " · " : "") + "born " + fmt(p.bornT) + " · age " + ageAt(p.bornT, Math.min(clock, p.diesT || clock)) + (employerOf(sel) ? " · works at " + NAMES[employerOf(sel)] : "");
      box.appendChild(h3); box.appendChild(who);
      var attrs = document.createElement("div"); attrs.className = "attrs"; var ch = chipsFor(sel); if (!ch.length) { var e0 = document.createElement("p"); e0.className = "empty"; e0.textContent = "Nothing conferred yet."; attrs.appendChild(e0); } ch.forEach(function (c) { var s = document.createElement("span"); s.className = "chip on"; s.textContent = c; attrs.appendChild(s); }); box.appendChild(attrs);
      var mine = past().filter(function (e) { return e.who && e.who.indexOf(sel) >= 0; });
      var sect = document.createElement("div"); sect.className = "sect"; sect.innerHTML = "<p class='q'>Law that has touched " + NAMES[sel] + " so far</p>";
      var counts = {}; mine.forEach(function (e) { e.law.forEach(function (l) { if (!l.subject) return; counts[l.subject] = counts[l.subject] || { n: 0, worst: "ENC" }; counts[l.subject].n++; if (l.status !== "ENC") counts[l.subject].worst = l.status; }); });
      var keys = Object.keys(counts).sort(function (a, b) { return counts[b].n - counts[a].n; });
      if (!keys.length) sect.innerHTML += "<p class='empty'>None yet.</p>";
      keys.forEach(function (k) { var r = document.createElement("div"); r.className = "lawrow"; var l = document.createElement("span"); l.appendChild(lawChip({ subject: k, status: counts[k].worst })); var n = document.createElement("span"); n.className = "n"; n.textContent = counts[k].n + "×"; r.appendChild(l); r.appendChild(n); sect.appendChild(r); });
      box.appendChild(sect);
      var nxt = EVENTS.filter(function (e) { return e.t > clock && e.who && e.who.indexOf(sel) >= 0; })[0];
      var s2 = document.createElement("div"); s2.className = "sect"; s2.innerHTML = "<p class='q'>Next in the script</p>" + (nxt ? "<p style='margin:0 0 8px;font-size:13.5px'><b>" + fmt(nxt.t) + "</b> — " + nxt.title + (nxt.question ? "<br><i style='color:var(--ink-2)'>" + nxt.question + "</i>" : "") + "</p>" : "<p class='empty'>Nothing further is scripted for " + NAMES[sel] + ".</p>");
      if (nxt) { var b = document.createElement("button"); b.className = "go"; b.textContent = "Go to " + fmt(nxt.t); b.addEventListener("click", function () { setClock(nxt.t); }); s2.appendChild(b); }
      box.appendChild(s2);
    } else if (sel.indexOf("ag:") === 0) {
      var ag = sel.slice(3); h3.textContent = ag; who.textContent = "authority · as engaged by the life so far"; box.appendChild(h3); box.appendChild(who);
      var sectA = document.createElement("div"); sectA.className = "sect"; sectA.innerHTML = "<p class='q'>Rows engaged</p>"; var cA = {};
      past().forEach(function (e) { e.law.forEach(function (l) { if (l.subject && agencyOf(l.subject) === ag) { cA[l.subject] = cA[l.subject] || { n: 0, worst: "ENC" }; cA[l.subject].n++; if (l.status !== "ENC") cA[l.subject].worst = l.status; } }); });
      Object.keys(cA).forEach(function (k) { var r = document.createElement("div"); r.className = "lawrow"; var l = document.createElement("span"); l.appendChild(lawChip({ subject: k, status: cA[k].worst })); var n = document.createElement("span"); n.className = "n"; n.textContent = cA[k].n + "× · rows: " + ((ROWS[k] || []).join(", ") || "none"); r.appendChild(l); r.appendChild(n); sectA.appendChild(r); });
      box.appendChild(sectA);
    } else if (sel.indexOf("org:") === 0) {
      var org = ORGS[sel.slice(4)]; h3.textContent = org.name; who.textContent = org.role; box.appendChild(h3); box.appendChild(who);
    } else if (sel.indexOf("th:") === 0) {
      var th = THINGS.filter(function (t) { return "th:" + t.id === sel; })[0]; var home = F.homes.filter(function (h) { return h.id === th.id; })[0];
      h3.textContent = th.label; who.textContent = (home ? home.tenure : th.kind) + " · " + th.owners.map(function (o) { return NAMES[o]; }).join(" and "); box.appendChild(h3); box.appendChild(who);
      if (home) { var pre = document.createElement("pre"); pre.style.cssText = "font-family:var(--mono);font-size:11.5px;color:var(--ink-2);white-space:pre-wrap;margin:0"; pre.textContent = Object.keys(home).filter(function (k) { return ["owner", "occupier", "id"].indexOf(k) < 0; }).map(function (k) { return k + ": " + home[k]; }).join("\n"); box.appendChild(pre); }
    }
  }

  /* ---------- the log ---------- */
  function renderLog() {
    var log = $("log"); log.innerHTML = "";
    var evs = past().filter(function (e) { return (!filterBeats || e.abridged) && (!filterTaint || e.tainted); });
    $("log-n").textContent = evs.length + " of " + EVENTS.length + " events";
    if (!evs.length) { log.innerHTML = "<p class='pane-empty'>Nothing yet. Step the clock, or jump to the next event.</p>"; return; }
    var lastT = evs[evs.length - 1].t;
    evs.forEach(function (e) {
      var row = document.createElement("div"); row.className = "ev" + (e.abridged ? " beat" : "") + (e.tainted ? " tainted" : "") + (e.t === lastT ? " now" : "");
      var d = document.createElement("div"); d.className = "d"; d.innerHTML = fmt(e.t) + "<small>ch " + e.chapter + " · " + (e.ages && e.ages.simone != null ? "S " + e.ages.simone : "") + "</small>";
      var t = document.createElement("div"); t.className = "t";
      t.innerHTML = "<b>" + e.title + "</b>" + (e.who ? " <span style='color:var(--ink-3)'>— " + e.who.map(function (w) { return NAMES[w] || w; }).join(", ") + "</span>" : "");
      if (e.question) { var q = document.createElement("div"); q.className = "q"; q.textContent = e.question; t.appendChild(q); }
      var laws = document.createElement("div"); laws.className = "laws"; e.law.forEach(function (l) { laws.appendChild(lawChip(l)); }); if (!e.law.length) { var none = document.createElement("span"); none.className = "chip"; none.textContent = "no law engaged"; laws.appendChild(none); } t.appendChild(laws);
      if (e.expected) { var x = document.createElement("div"); x.className = "exp"; x.textContent = "expected: " + Object.keys(e.expected).map(function (k) { var v = e.expected[k]; return k + " = " + (typeof v === "object" ? JSON.stringify(v) : v); }).join(" · "); t.appendChild(x); }
      if (e.tainted) { var r = document.createElement("div"); r.className = "req"; r.textContent = "tainted: proceeded on an assumption" + (e.reqs.length ? "; emitted " + e.reqs.map(function (q) { return q.id; }).join(", ") : "; no ledger entry yet for this gap"); t.appendChild(r); }
      row.appendChild(d); row.appendChild(t); log.appendChild(row);
    });
    log.scrollTop = log.scrollHeight;
  }


  /* only entries this life raised: the scheduled tier lines are the encoder's queue, not the simulation's */
  function raisedByLife(r) { return (r.trigger && r.trigger.event) || (r.closes_when && r.closes_when.scenario === F.scenario); }
  function raisedAt(r) { var ev = r.trigger && r.trigger.event ? EVENTS.filter(function (e) { return e.id === r.trigger.event; })[0] : null; return ev ? ev.t : parse(r.trigger.date); }
  /* ---------- side panes ---------- */
  function renderChapters() {
    var strip = $("chapters"), pane = $("chapters-pane"); strip.innerHTML = ""; pane.innerHTML = ""; var cur = chapterAt(clock);
    CHAPTERS.forEach(function (ch) {
      var b = document.createElement("button"); b.type = "button"; b.innerHTML = "ch " + ch.n + " <span class='y'>" + new Date(ch.start).getUTCFullYear() + "–" + new Date(ch.end).getUTCFullYear() + "</span>"; b.title = ch.title; if (ch.n === cur) b.setAttribute("aria-current", "true"); if (ch.start < clock && ch.n !== cur) b.className = "past"; b.addEventListener("click", function () { setClock(ch.start); }); strip.appendChild(b);
      var r = document.createElement("button"); r.type = "button"; r.className = "chrow"; if (ch.n === cur) r.setAttribute("aria-current", "true");
      var done = ch.events.filter(function (e) { return e.t <= clock; }).length;
      r.innerHTML = "<span class='n'>" + ch.n + "</span><span class='tt'>" + ch.title + "</span><span class='yy'>" + new Date(ch.start).getUTCFullYear() + "–" + new Date(ch.end).getUTCFullYear() + "</span><span class='age'>Simone " + ageAt(DAY0, ch.start) + "–" + ageAt(DAY0, ch.end) + " · " + done + "/" + ch.events.length + " events · " + ch.events.filter(function (e) { return e.abridged; }).length + " beats</span>";
      r.addEventListener("click", function () { setClock(ch.start); }); pane.appendChild(r);
    });
    $("ch-count").textContent = "chapter " + cur + " of 9";
  }
  function renderReqs() {
    var box = $("reqs"); box.innerHTML = "";
    var emitted = LEDGER.filter(raisedByLife).filter(function (r) { return raisedAt(r) <= clock; }).sort(function (a, b) { return (a.priority || 99) - (b.priority || 99) || b.count - a.count; });
    $("req-count").textContent = emitted.length + " of " + LEDGER.filter(raisedByLife).length + " raised by this life · " + LEDGER.length + " in the ledger";
    if (!emitted.length) { box.innerHTML = "<p class='pane-empty'>None yet. A requirement is emitted the first time the life needs law the library does not hold.</p>"; return; }
    emitted.forEach(function (r) { var d = document.createElement("div"); d.className = "reqrow"; if (r.status !== "open") d.style.cssText = "border-left-color:var(--ok);opacity:.75"; d.innerHTML = "<div class='h'><span class='id'>" + r.id + "</span><span class='k'>" + r.kind + "</span><span class='k'>→ " + r.attach_to.how + "</span>" + (r.status !== "open" ? "<span class='k' style='color:var(--ok);border-color:var(--ok)'>" + r.status + (r.resolution && r.resolution.commit ? " · " + String(r.resolution.commit).slice(0, 8) : "") + "</span>" : "") + "<span class='p'>p" + (r.priority || "-") + " · ×" + r.count + "</span></div><p class='tt'>" + r.instrument.title + (r.instrument.provision ? " <span style='color:var(--ink-3)'>" + r.instrument.provision + "</span>" : "") + "</p><p class='qq'>" + r.question + "</p>"; box.appendChild(d); });
  }
  function renderObs() {
    var box = $("obs"); box.innerHTML = ""; var p = past(); var subj = {}; p.forEach(function (e) { e.law.forEach(function (l) { if (l.subject) subj[l.subject] = 1; }); });
    var clean = p.filter(function (e) { return !e.tainted; }).length, taint = p.length - clean; var satisfied = LEDGER.filter(raisedByLife).filter(function (r) { return raisedAt(r) <= clock && r.status !== "open"; }).length;
    var emitted = LEDGER.filter(raisedByLife).filter(function (r) { return raisedAt(r) <= clock; }).length;
    [["days since Simone's birth", Math.round((clock - DAY0) / DAY), ""], ["people alive", F.people.filter(alive).length, ""], ["events adjudicated", p.length, ""], ["Acts engaged (distinct)", Object.keys(subj).length, ""], ["clean traces", clean, "ok"], ["tainted traces", taint, taint ? "warn" : ""], ["requirements emitted", emitted, emitted ? "warn" : ""], ["of which already encoded", satisfied, satisfied ? "ok" : ""], ["rows in the library when built", Object.keys(ROWS).length, ""]].forEach(function (r) { var d = document.createElement("div"); d.className = "cnt-row"; if (r[2]) d.dataset.s = r[2]; d.innerHTML = "<span class='l'>" + r[0] + "</span><span class='n'>" + r[1] + "</span>"; box.appendChild(d); });
  }

  function render() {
    var c = chapterAt(clock);
    $("clock").innerHTML = "<b>" + fmt(clock) + "</b> · day " + Math.round((clock - DAY0) / DAY) + " · ch " + c + (clock >= NOW && clock - NOW < DAY ? " · now" : "");
    $("prevch").disabled = clock <= DAY0; $("nextch").disabled = c >= CHAPTERS.length - 1;
    drawCanvas(); renderInspector(); renderLog(); renderChapters(); renderReqs(); renderObs();
  }

  $("d1").addEventListener("click", function () { step(1); }); $("d7").addEventListener("click", function () { step(7); }); $("d30").addEventListener("click", function () { step(30); }); $("d365").addEventListener("click", function () { step(365); });
  $("nextev").addEventListener("click", nextEvent); $("nextch").addEventListener("click", nextChapter); $("prevch").addEventListener("click", prevChapter);
  $("now").addEventListener("click", function () { setClock(NOW); flash("Today: the demo's present."); }); $("reset").addEventListener("click", function () { sel = null; setClock(DAY0); flash("Back to the day Simone was born."); });
  $("beats-only").addEventListener("change", function (e) { filterBeats = e.target.checked; renderLog(); }); $("tainted-only").addEventListener("change", function (e) { filterTaint = e.target.checked; renderLog(); });
  document.addEventListener("keydown", function (e) { if (e.target.tagName === "INPUT") return; if (e.key === "ArrowRight") { e.shiftKey ? nextChapter() : nextEvent(); } if (e.key === "ArrowLeft") prevChapter(); });
  $("builtdate").textContent = D.built; $("libnote").textContent = Object.keys(ROWS).length + " subjects with rows on " + D.built;
  sel = "simone"; setClock(NOW);
})();
