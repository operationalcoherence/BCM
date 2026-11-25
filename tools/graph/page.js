/* The simple Pattern Synthesis page (first build, 2026-11-24).
 *
 * Graph (tools/graph/graph.js) and shapes (tools/graph/shapes.js) in, two blocks out:
 *   WHAT CHANGED WHAT        the strongest single relationship
 *   WHAT KEEPS ITSELF GOING  the strongest shape (or WHAT HOLDS IT IN PLACE, WHERE IT IS HEADING)
 * Each block: one sentence of meaning, a short explanation, one line of evidence (note numbers
 * and how sure the reading is, in plain words). Design: claude/pattern_synthesis_minimal_page_2026-11-24.md.
 *
 * The question block is not built (Gregory, 24 Nov: the question engine waits until the
 * discovered parts are tested). Where a shape rests on an inferred step, the page says that the
 * step needs the person's answer, and nothing more.
 *
 * Rules kept here:
 *   - A note is never named by a fragment of its text in a narrative line. It is described by
 *     what it is and where it stands (its emotion, its side of the line, its stretch of the way);
 *     note numbers go in the evidence line. Only a cue word the graph matched is quoted there.
 *   - "Emotion", never "feeling". Serial comma in every list.
 *   - Stays empty-handed honestly: with nothing related, it says so in one line.
 *
 * gsmPSRead(data, lexicon) -> { blocks: [...], empty: bool }   (no DOM; testable in node)
 * gsmPSPage(Rt, data, lexicon)  inserts the page after the Pattern Synthesis part header.
 */
(function (root) {
  "use strict";
  var G = root.gsmGraph || (typeof require !== "undefined" ? require("./graph.js") : null);
  var S = root.gsmShapes || (typeof require !== "undefined" ? require("./shapes.js") : null);

  var EMO = ["aggression", "acceptance", "distrust", "indifference", "defiance"];
  var RANK = { inferred: 1, placed: 2, stated: 3 };
  var ANSWER = {
    1: "your account of why the goal has not taken root",
    2: "your account of the opposition",
    3: "your account of the support",
    4: "the conditions you named",
    5: "your account of what needs to be designed",
    6: "your account of what needs to be redesigned",
    7: "your account of what needs to be reinforced",
  };
  var DESIGN = { 5: "something you would design", 6: "something you would redesign", 7: "something you would reinforce" };
  var STRETCH = ["near the present", "midway", "near the goal"];
  var NUM = ["", "one", "two", "three", "four", "five", "six", "seven", "eight"];

  function list(a) {
    if (a.length < 2) return a[0] || "";
    if (a.length === 2) return a[0] + " and " + a[1];
    return a.slice(0, -1).join(", ") + ", and " + a[a.length - 1];
  }
  function cap(s) {
    return s ? s.charAt(0).toUpperCase() + s.slice(1) : s;
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function reader(g, data) {
    var byId = {};
    g.nodes.forEach(function (n) {
      byId[n.id] = n;
    });
    var placeIdx = {};
    ((data.p && data.p.m) || []).forEach(function (r, i) {
      if (r && r[8]) placeIdx[r[8]] = i + 1;
    });
    // how the page's link pass writes a note: "note 5" (line map) or "P5" (place map)
    function ref(id) {
      var n = byId[id];
      if (!n) return id;
      if (n.kind === "answer") return n.label;
      if (n.kind === "goal") return "the goal";
      if (g.view === "place") return placeIdx[n.id] ? "P" + placeIdx[n.id] : n.label;
      return "note " + String(n.label).replace(/^N/, "");
    }
    // what a part is and where it stands, never its words
    function say(id) {
      var n = byId[id];
      if (!n) return "a part of the map";
      if (n.kind === "goal") return "the goal";
      if (n.kind === "answer") return ANSWER[n.q] || "one of your answers";
      var what;
      if (n.role === "design") what = DESIGN[n.q];
      else what = n.emo != null ? EMO[n.emo] : "a note";
      if (g.view === "place") return n.role === "design" ? what : n.emo != null ? "a note of " + what : what;
      var where = [];
      if (n.role !== "design") where.push(n.side === "help" ? "on the help side" : n.side === "hinder" ? "on the hinder side" : "on the line");
      if (n.stretch != null) where.push(STRETCH[n.stretch]);
      return what + (where.length ? " " + where.join(", ") : "");
    }
    var text = {};
    ((g.view === "place" ? data.p && data.p.m : data.m) || []).forEach(function (r, i) {
      var id = g.view === "place" ? r[8] : "N" + (i + 1);
      text[g.byLabel[id] || id] = text[g.byLabel[id] || id] || r[3] || "";
    });
    (data.a || []).forEach(function (t, i) {
      text["Q." + (i + 1)] = t || "";
    });
    return { byId: byId, ref: ref, say: say, text: text, view: g.view };
  }

  function sure(arrows) {
    // the plainest truthful line for the weakest kind of evidence among these arrows
    var ev = [];
    arrows.forEach(function (a) {
      ev = ev.concat(a.evidence || []);
    });
    var g = Math.min.apply(
      null,
      arrows.map(function (a) {
        return RANK[a.grade];
      }),
    );
    if (g === 1) return "One step rests on a single shared word, so it needs your answer.";
    var cues = [];
    ev.forEach(function (e) {
      if (e.type === "cue" && e.cue && cues.indexOf(e.cue) < 0) cues.push(e.cue);
    });
    if (ev.some((e) => e.type === "user-link") && arrows.every((a) => (a.evidence || []).some((e) => e.type === "user-link"))) return "You drew this yourself.";
    if (g === 3) return "The workbook says this directly" + (cues.length ? ": " + list(cues.slice(0, 3).map((c) => "“" + c + "”")) + "." : ".");
    if (ev.some((e) => e.type === "names-each-other")) return "Shown by whom the notes are aimed at.";
    return "Shown by the order and wording of the notes" + (cues.length ? ", with " + list(cues.slice(0, 2).map((c) => "“" + c + "”")) : "") + ".";
  }

  /* ---------- what a relationship rests on, in the person's own shared words ---------- */
  // A shared phrase or shared words between two differently worded parts may be named (the
  // theme rule). Emotion words are left out: they tie notes that are only about the same emotion.
  var EMO_STEMS = { aggres: 1, accept: 1, distru: 1, indiff: 1, defian: 1, emotio: 1 };
  // the longest runs of wanted words that sit together in one text (at most one short word
  // between them, as in "command and control"), recovered as the person wrote them
  function surface(stemsWanted, texts) {
    var want = {};
    stemsWanted.forEach(function (w) {
      w.split(" ").forEach(function (p) {
        if (!EMO_STEMS[p]) want[p] = 1;
      });
    });
    var found = {}, out = [];
    texts.forEach(function (t) {
      G._clauses(t).forEach(function (c) {
        var run = [];
        function flush() {
          if (!run.length) return;
          var a = run[0], z = run[run.length - 1];
          var endw = c.raw.slice(z.at).match(/^[a-z-]+/)[0];
          var span = c.raw.slice(a.at, z.at + endw.length).replace(/\s+/g, " ").replace(/-+$/, "");
          var key = run.map((k) => k.s).join(" ");
          if (!found[key]) {
            found[key] = 1;
            out.push({ s: span, n: run.length, key: key });
          }
          run = [];
        }
        c.toks.forEach(function (k, i) {
          if (!want[k.s]) return flush();
          var prev = run[run.length - 1];
          if (prev) {
            var pw = c.raw.slice(prev.at).match(/^[a-z-]+/)[0];
            var gapTxt = c.raw.slice(prev.at + pw.length, k.at);
            if (!/^\s*([a-z]{1,4}\s+)?$/.test(gapTxt) || prev === k) flush();
          }
          if (run.length && run[run.length - 1].at === k.at) return; // two halves of one hyphenated word
          run.push(k);
        });
        flush();
      });
    });
    // keep the fullest wording of each word: a run inside a longer run is dropped
    out.sort((x, y) => y.n - x.n);
    var kept = [];
    out.forEach(function (o) {
      var parts = o.key.split(" ");
      if (kept.some((k) => parts.every((p) => k.key.split(" ").indexOf(p) >= 0))) return;
      kept.push(o);
    });
    return kept.map((o) => o.s.replace(/s$/, function (m) { return /ships$|s's$/.test(o.s) ? "" : m; }));
  }
  function topic(a, R) {
    var ph = [], ws = [];
    (a.evidence || []).forEach(function (e) {
      (e.phrases || []).forEach((p) => ph.indexOf(p) < 0 && ph.push(p));
      (e.words || []).forEach((w) => ws.indexOf(w) < 0 && ws.push(w));
    });
    var texts = [a.to, a.from].map((id) => (R.byId[id] && R.text[id]) || "");
    var got = surface(ph.concat(ws), texts);
    return got.slice(0, 3);
  }
  function quoteList(ws) {
    return list(ws.map((w) => "“" + w + "”"));
  }
  // two parts said together, without repeating what they share
  function pair(aid, bid, R) {
    var a = R.byId[aid], b = R.byId[bid];
    if (a && b && a.kind === "note" && b.kind === "note" && a.role === b.role && a.emo === b.emo && a.side === b.side && R.view !== "place") {
      var what = a.role === "design" ? DESIGN[a.q] === DESIGN[b.q] ? "two things you would " + DESIGN[a.q].replace("something you would ", "") : "two things you would do" : a.emo != null ? "two notes of " + EMO[a.emo] : "two notes";
      var side = a.role === "design" ? "" : a.side === "help" ? " on the help side" : a.side === "hinder" ? " on the hinder side" : "";
      var st = a.stretch === b.stretch ? ", both " + STRETCH[a.stretch] : a.stretch != null && b.stretch != null ? ", one " + STRETCH[a.stretch] + " and one " + STRETCH[b.stretch] : "";
      return what + side + st;
    }
    return null;
  }

  /* ---------- block 1: the strongest single relationship ---------- */
  function strongestRelationship(g, avoid) {
    var deg = {};
    g.arrows.forEach(function (a) {
      if (a.from === a.to) return;
      deg[a.from] = (deg[a.from] || 0) + 1;
      deg[a.to] = (deg[a.to] || 0) + 1;
    });
    var inShape = {};
    (avoid ? avoid.arrows : []).forEach(function (a) {
      inShape[a.from + "|" + a.to + "|" + a.kind] = 1;
    });
    var order = {};
    g.nodes.forEach(function (n, i) {
      order[n.id] = i;
    });
    var cand = g.arrows.filter(function (a) {
      return a.from !== a.to && a.grade !== "inferred";
    });
    cand.sort(function (a, b) {
      return (
        RANK[b.grade] - RANK[a.grade] ||
        (inShape[a.from + "|" + a.to + "|" + a.kind] ? 1 : 0) - (inShape[b.from + "|" + b.to + "|" + b.kind] ? 1 : 0) ||
        deg[b.from] + deg[b.to] - (deg[a.from] + deg[a.to]) ||
        Math.min(order[a.from], order[a.to]) - Math.min(order[b.from], order[b.to])
      );
    });
    return cand[0] || null;
  }

  /* ---------- prose ---------- */
  // what each emotion means as ground (claude/emotion_definitions_redline.md, approved 11-24);
  // read toward what the note is about, on either side of the line; never legitimacy outside acceptance
  function ground(n) {
    if (!n || n.emo == null) return "";
    var hinder = n.side === "hinder";
    return [
      "Aggression sits next to defiance, and the slide between them runs both ways.",
      hinder
        ? "Acceptance below the line is the firmest ground the present way stands on: settled rather than argued, and so the hardest to move."
        : "Acceptance is the ground where an idea takes root and spreads, and it has to be tended to stay that way.",
      "Distrust is low ground: it climbs toward acceptance only with real effort, and it slides toward something harsher more easily.",
      "Indifference is a precarious place, neither for nor against: most change passes through it, and some people stay there.",
      "Defiance is the lowest ground, and the most resistant to any strategy.",
    ][n.emo];
  }
  var ANS_NOUN = {
    1: "the reasons the goal has not taken root",
    2: "the opposition you describe",
    3: "the support you describe",
    4: "the conditions you named",
    5: "your answer on what to design",
    6: "your answer on what to redesign",
    7: "your answer on what to reinforce",
  };
  var ANS_SHORT = { 1: "those reasons", 2: "the opposition", 3: "the support", 4: "the conditions", 5: "the design", 6: "the redesign", 7: "the reinforcing" };
  var DES_NOUN = { 5: "something you would design", 6: "something you would redesign", 7: "something you would reinforce" };
  // a second mention, short; falls back to the full name where two parts would sound alike
  function shorts(ids, R) {
    var sh = ids.map(function (id) {
      var n = R.byId[id];
      if (!n) return np(id, R);
      if (n.kind === "answer") return ANS_SHORT[n.q] || np(id, R);
      if (n.role === "design") return "that " + DES_NOUN[n.q].replace("something you would ", "") ;
      return n.emo != null ? "the " + EMO[n.emo] : np(id, R);
    });
    var full = sh.map((x, i) => (sh.indexOf(x) !== i || sh.lastIndexOf(x) !== i ? np(ids[i], R) : x));
    return dedupe(full);
  }
  // the same name twice in one ring: "one acceptance", "another acceptance"
  function dedupe(a) {
    var seen = {};
    return a.map(function (x) {
      if (a.indexOf(x) === a.lastIndexOf(x)) return x;
      var bare = x.replace(/^the /, "");
      seen[x] = (seen[x] || 0) + 1;
      return (seen[x] === 1 ? "one " : "another ") + bare;
    });
  }
  // a part as a noun phrase, optionally with what it is about
  function np(id, R, about) {
    var n = R.byId[id];
    if (!n) return "one part of the map";
    if (n.kind === "goal") return "the goal";
    if (n.kind === "answer") return ANS_NOUN[n.q] || "one of your answers";
    if (n.role === "design") return DES_NOUN[n.q] || "something you would do";
    var e = n.emo != null ? EMO[n.emo] : "concern";
    var side = R.view === "place" ? "" : n.side === "hinder" ? "below the line" : n.side === "help" ? "above the line" : "";
    return "the " + e + (about ? " around " + about : "") + (side ? " " + side : "");
  }
  function when(id, R) {
    var n = R.byId[id];
    return n && n.stretch != null && R.view !== "place" ? ["near the start", "partway along", "near the goal"][n.stretch] : "";
  }
  function topicOf(arrows, R, anyWord) {
    var c = {}, order = [];
    arrows.forEach(function (a) {
      topic(a, R).forEach(function (t) {
        if (!c[t]) order.push(t);
        c[t] = (c[t] || 0) + 1;
      });
    });
    order.sort((x, y) => (y.indexOf(" ") > 0) - (x.indexOf(" ") > 0) || c[y] - c[x] || y.length - x.length);
    var t = order[0] || "";
    return anyWord || t.indexOf(" ") > 0 ? t : "";
  }

  function relBlock(a, R) {
    var ev = a.evidence || [],
      na = R.byId[a.from],
      nb = R.byId[a.to],
      T = topicOf([a], R),
      head,
      body = [];
    var mutual = ev.some((e) => e.type === "names-each-other");
    var user = ev.some((e) => e.type === "user-link");
    var sameEmo = na && nb && na.emo != null && na.emo === nb.emo;
    if (mutual) {
      var two = na.side && nb.side && na.side !== nb.side;
      head = two ? "The two sides are locked in one exchange of " + (sameEmo ? EMO[na.emo] : "hostility") + "." : "Two groups are answering each other in kind.";
      body.push(cap(np(a.from, R)) + " is aimed at the very people " + np(a.to, R) + " belongs to, and " + np(a.to, R) + " is aimed straight back.");
      body.push("Each side’s stance has become the other side’s reason, so neither needs anything new to keep going.");
      if (sameEmo) body.push(ground(na));
      body.push("Pressing on either side feeds the other. The exchange loosens only when one side is met with something other than what it expects.");
    } else if (user) {
      head = "You tied " + np(a.from, R) + " to " + np(a.to, R) + ".";
      body.push("This is a relationship you drew yourself, so it outranks anything BCM finds in the wording.");
      if (ground(nb)) body.push(ground(nb));
      body.push("Whatever moves the first should be expected to reach the second.");
    } else if (a.kind === "carry") {
      head = sameEmo
        ? cap(EMO[na.emo]) + (topicOf([a], R, true) ? " of " + topicOf([a], R, true) : "") + " does not fade as the change moves on; it travels with it."
        : cap(np(a.from, R, T)) + " " + when(a.from, R) + " turns into " + EMO[nb.emo != null ? nb.emo : 0] + " further along.";
      body.push("It shows up " + when(a.from, R) + " and again " + when(a.to, R) + ", and the later one rests on the earlier" + (RANK[a.grade] === 3 ? ": the workbook says as much." : "."));
      if (ground(nb)) body.push(ground(nb));
      body.push("Carried this far, it is no longer a mood the change can wait out; it is part of the ground every later step has to cross, and each move will be read through it.");
      body.push("It loses its hold only when something done early gives it nothing to carry forward.");
    } else if (a.kind === "reachback") {
      head = "What people expect to happen later is already deciding where they stand now.";
      body.push(cap(np(a.to, R, T)) + " " + when(a.to, R) + " is looking ahead to " + np(a.from, R) + " " + when(a.from, R) + ".");
      if (ground(nb)) body.push(ground(nb));
      body.push("So the later stretch is partly being settled early: the first visible moves will be read as signs of how it ends.");
    } else if (a.kind === "recoil") {
      head = cap(np(a.from, R)) + " will change the ground it is meant for.";
      body.push("It is aimed at " + np(a.to, R, T) + ", and ground does not hold still once something lands on it.");
      if (ground(nb)) body.push(ground(nb));
      body.push("Expect an answer, and plan the next step for the ground as it will be, not as it was mapped.");
    } else if (a.kind === "coupling") {
      head = (sameEmo ? "Two places of " + EMO[na.emo] : cap(np(a.from, R)) + " and " + np(a.to, R)) + (when(a.from, R) ? " " + when(a.from, R) : "") + " move together" + (T ? ", both turning on " + T : "") + ".";
      body.push("They stand on the same stretch and turn on the same thing, so a move in one is likely to show up in the other.");
      if (ground(na)) body.push(ground(na));
      body.push("Neither changes alone: work on one and watch the other.");
    } else {
      head = cap(np(a.from, R)) + " and " + np(a.to, R) + (T ? " both turn on " + T : " are tied") + ".";
      body.push("The map gives no order to say which acts on which, only that they turn on the same thing.");
      if (ground(nb)) body.push(ground(nb));
    }
    return { key: "rel", title: "WHAT CHANGED WHAT", head: head, body: body.join(" "), refs: [R.ref(a.from), R.ref(a.to)], arrow: a.undirected ? " and " : " → ", sure: sure([a]) };
  }

  function shapeBlock(s, R) {
    var refs = s.parts.map(R.ref),
      head,
      body = [],
      title;
    var T = topicOf(s.arrows, R);
    var inferred = s.arrows.filter((a) => a.grade === "inferred")[0];
    var weak = inferred || s.burden;
    var shAll = shorts(s.parts, R), shOf = function (id) { var i = s.parts.indexOf(id); return i >= 0 ? shAll[i] : np(id, R); };
    var weakTxt = "between " + shOf(weak.from) + " and " + shOf(weak.to);
    if (s.type === "loop" && s.given) {
      title = "WHAT KEEPS ITSELF GOING";
      head = "You described a loop yourself: more of it makes the need for more of it.";
      body.push(cap(np(s.parts[0], R, T)) + " feeds itself, so it needs no outside push to continue.");
      if (ground(R.byId[s.parts[0]])) body.push(ground(R.byId[s.parts[0]]));
      body.push(
        s.joins && s.joins.length
          ? "It does not stay inside the one note: BCM finds " + s.joins.length + (s.joins.length === 1 ? " other part" : " other parts") + " tied into it, so the loop reaches further than you wrote it."
          : "Nothing else on the map ties into it yet, which is worth asking about: a loop this strong rarely stands alone.",
      );
      refs = refs.concat((s.joins || []).map((a) => R.ref(a.from === s.parts[0] ? a.to : a.from)));
    } else if (s.type === "loop" && s.mutual) {
      var b = relBlock(s.arrows[0], R);
      title = "WHAT KEEPS ITSELF GOING";
      head = b.head;
      body = [b.body];
    } else if (s.type === "loop") {
      title = "WHAT KEEPS ITSELF GOING";
      var k = NUM[s.parts.length] || String(s.parts.length);
      head = cap(k) + " parts of the situation hold each other in place" + (T ? ", all turning on " + T : "") + ".";
      var names = s.parts.map((id) => np(id, R)), sn = shorts(s.parts, R);
      body.push("They are " + list(dedupe(names)) + ".");
      body.push("Each gives the next its reason: " + list(sn.map((n, i) => "from " + n + (i === sn.length - 1 ? " back to " + sn[0] : " to " + sn[i + 1]))) + ".");
      body.push("A loop like this needs no one to defend it. It renews itself every time one of its parts is touched, so pressing on one part alone tends to be absorbed by the others.");
      body.push("It is thinnest " + weakTxt + ". Change what passes there, and the rest lose a reason to hold.");
    } else if (s.type === "settlement") {
      title = "WHAT HOLDS IT IN PLACE";
      head = cap(NUM[s.sources.length] || String(s.sources.length)) + " different reasons all end in the same place" + (T ? ", around " + T : "") + ".";
      body.push(cap(list(s.sources.map((id) => np(id, R)))) + " each lead to " + np(s.target, R) + ".");
      if (ground(R.byId[s.target])) body.push(ground(R.byId[s.target]));
      body.push("Because the reasons are separate, taking one away leaves the others still holding. This is what a settled situation looks like: nothing is pushing, and nothing has to.");
      body.push("It moves only when each reason is met, or when the place they end in is changed directly.");
    } else {
      title = "WHERE IT IS HEADING";
      var last = s.parts[s.parts.length - 1];
      head = cap(np(s.parts[0], R)) + " leads, step by step, to " + np(last, R) + ".";
      body.push("The way runs " + [np(s.parts[0], R)].concat(shAll.slice(1)).join(", then ") + (T ? ", turning on " + T : "") + ".");
      if (ground(R.byId[last])) body.push(ground(R.byId[last]));
      body.push("Left as it is, this is where the situation goes, one step making the next likely.");
      body.push("The cheapest place to turn it is its weakest link, " + weakTxt + ".");
    }
    if (inferred) body.push("That link rests on a single shared word, so treat it as open until you say whether it holds.");
    return { key: "shape", title: title, head: head, body: body.join(" "), refs: refs, arrow: s.type === "settlement" ? ", " : " → ", sure: sure(s.arrows) };
  }

  function gsmPSRead(data, lex) {
    if (lex && !root.gsmLexicon) root.gsmLexicon = lex;
    if (!G || !S) return { blocks: [], empty: true, unavailable: true };
    var g = G.buildGraph(data || {});
    var R = reader(g, data || {});
    var sh = S.detectShapes(g);
    var top = sh.strongest && !sh.strongest.yields ? sh.strongest : sh.strongest;
    var rel = strongestRelationship(g, top);
    var blocks = [];
    if (rel) blocks.push(relBlock(rel, R));
    if (top) blocks.push(shapeBlock(top, R));
    // the same thing twice says nothing new
    if (blocks.length === 2 && blocks[0].head === blocks[1].head) blocks.splice(1, 1);
    return { blocks: blocks, empty: !blocks.length, graph: g, shapes: sh, rel: rel, top: top };
  }

  function html(r) {
    if (r.unavailable) return "";
    var h = '<div class="psy-sec">';
    if (r.empty) return h + '<div class="psy-head">Nothing in this workbook changes anything else yet.</div></div>';
    r.blocks.forEach(function (b) {
      h +=
        '<div class="psy-blk" data-psy="' +
        b.key +
        '"><div class="psy-t">' +
        esc(b.title) +
        '</div><div class="psy-head">' +
        esc(b.head) +
        '</div><p class="psy-body">' +
        esc(b.body) +
        '</p><div class="psy-ev">' +
        esc(b.refs.filter((x, i, a) => a.indexOf(x) === i).join(b.arrow)) +
        " · " +
        esc(b.sure) +
        "</div></div>";
    });
    return h + "</div>";
  }

  var CSS =
    ".psy-sec{margin:6px 0 22px}.psy-blk{border-left:3px solid #222;padding:2px 0 2px 14px;margin:0 0 18px}" +
    ".psy-t{font-size:11px;letter-spacing:1.6px;color:#555;margin:0 0 4px}.psy-head{font-size:19px;font-weight:700;line-height:1.3;margin:0 0 6px}" +
    ".psy-body{margin:0 0 6px;line-height:1.55}.psy-ev{font-size:12px;color:#777}";

  function gsmPSPage(Rt, data, lex) {
    if (!Rt || Rt.querySelector(".psy-sec")) return;
    var part = [].filter.call(Rt.children, function (k) {
      return k.classList.contains("part") && /LOOKING OUT/.test(k.textContent);
    })[0];
    if (!part) return;
    var r;
    try {
      r = gsmPSRead(data, lex);
    } catch (e) {
      return;
    }
    var out = html(r);
    if (!out) return;
    if (!document.getElementById("psy-css")) {
      var st = document.createElement("style");
      st.id = "psy-css";
      st.textContent = CSS;
      document.head.appendChild(st);
    }
    var box = document.createElement("div");
    box.innerHTML = out;
    var el = box.firstChild;
    el.setAttribute("data-pv", "3");
    if (part.classList.contains("tabhide")) el.classList.add("tabhide");
    Rt.insertBefore(el, part.nextSibling);
  }

  var api = { gsmPSRead: gsmPSRead, gsmPSPage: gsmPSPage, _html: html };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else {
    root.gsmPSRead = gsmPSRead;
    root.gsmPSPage = gsmPSPage;
  }
})(typeof window !== "undefined" ? window : globalThis);
