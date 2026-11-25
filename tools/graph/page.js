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

  function relBlock(a, R) {
    var A = R.say(a.from),
      B = R.say(a.to),
      P = pair(a.from, a.to, R),
      T = topic(a, R),
      about = T.length ? quoteList(T) : "",
      ev = a.evidence || [],
      head,
      body;
    var mutual = ev.some((e) => e.type === "names-each-other");
    var user = ev.some((e) => e.type === "user-link");
    var na = R.byId[a.from],
      nb = R.byId[a.to];
    if (mutual) {
      var same = na && nb && na.emo != null && na.emo === nb.emo;
      var twoSides = na && nb && na.side && nb.side && na.side !== nb.side && na.side !== "line" && nb.side !== "line";
      head = (twoSides ? "The two sides’ " : "These two groups’ ") + (same ? EMO[na.emo] : "stances") + " are one exchange.";
      body = cap(A) + " is aimed at the people " + B + " describes, and " + B + " is aimed back. Each side’s stance is becoming the other side’s reason, so expect a move against either one to be answered by the other.";
    } else if (user) {
      head = "You tied these two together.";
      body = "You drew a link from " + A + " to " + B + ". BCM reads it as a relationship of your own, and nothing it finds on its own outranks it.";
    } else if (a.kind === "carry") {
      head = "What comes earlier is carried into what comes later.";
      body = (P ? cap(P) + "," : cap(A) + ", and later " + B + ",") + (about ? " are both about " + about + "," : "") + " and the later one rests on the earlier. Unless something changes the first, expect the second to keep following from it.";
    } else if (a.kind === "reachback") {
      head = "What is expected later already acts on the present.";
      body = cap(B) + " looks ahead to " + A + (about ? ", through " + about : "") + ". What people expect further along is shaping where they stand now, so the later stretch is partly being decided early.";
    } else if (a.kind === "recoil") {
      head = "What you would design will change the ground it is meant for.";
      body = cap(A) + " is aimed at " + B + (about ? ", through " + about : "") + ". Expect it to answer back: the ground will not stay as it was mapped once the design reaches it.";
    } else if (a.kind === "coupling") {
      head = "Two parts on the same stretch move together.";
      body = (P ? cap(P) + "," : cap(A) + " and " + B) + (about ? " share " + about : " are tied") + ", so a change in one is likely to show up in the other.";
    } else {
      head = "Two parts are tied, with no order to read.";
      body = cap(A) + " and " + B + (about ? " share " + about : " are tied") + ", though the map gives no order to say which acts on which.";
    }
    return { key: "rel", title: "WHAT CHANGED WHAT", head: head, body: body, refs: [R.ref(a.from), R.ref(a.to)], arrow: a.undirected ? " and " : " → ", sure: sure([a]) };
  }

  /* ---------- block 2: the strongest shape ---------- */
  function shapeBlock(s, R) {
    var refs = s.parts.map(R.ref),
      head,
      body,
      title;
    var inferred = s.arrows.filter((a) => a.grade === "inferred")[0];
    var gap = inferred
      ? " One step, from " + R.say(inferred.from) + " to " + R.say(inferred.to) + ", rests only on a single shared word. Read the rest as shown, and treat that step as open until you say whether it holds."
      : "";
    function leg(a, from) {
      var to = a.from === from ? a.to : a.from, T = topic(a, R);
      return { to: to, txt: (T.length ? "through " + quoteList(T) + " " : "") + (to === s.parts[0] ? "back to the first" : (a.undirected ? "together with " : "to ") + R.say(to)) };
    }
    if (s.type === "loop" && s.given) {
      title = "WHAT KEEPS ITSELF GOING";
      head = "You described a loop yourself.";
      body = cap(R.say(s.parts[0])) + " keeps itself going: more of it makes the need for more of it. " +
        (s.joins && s.joins.length ? "BCM finds " + s.joins.length + (s.joins.length === 1 ? " other part" : " other parts") + " tied into it, so the loop reaches further than the one note." : "Nothing else on the map ties into it yet.");
      refs = refs.concat((s.joins || []).map((a) => R.ref(a.from === s.parts[0] ? a.to : a.from)));
    } else if (s.type === "loop" && s.mutual) {
      var b = relBlock(s.arrows[0], R);
      title = "WHAT KEEPS ITSELF GOING";
      head = b.head;
      body = b.body;
    } else if (s.type === "loop") {
      title = "WHAT KEEPS ITSELF GOING";
      head = cap(NUM[s.parts.length] || String(s.parts.length)) + " parts of the situation hold each other in place.";
      var at = s.parts[0], legs = [];
      s.arrows.forEach(function (a, i) {
        var l = leg(a, at);
        legs.push(l.txt);
        at = l.to;
      });
      body = "Round it goes: " + R.say(s.parts[0]) + " leads " + legs.join("; then ") + ". Each keeps the next going, so a push on any one alone is likely to be pushed back by the rest." + (gap || " The place to start is the step that holds least firmly, from " + R.say(s.burden.from) + " to " + R.say(s.burden.to) + ".");
    } else if (s.type === "settlement") {
      title = "WHAT HOLDS IT IN PLACE";
      head = cap(NUM[s.sources.length] || String(s.sources.length)) + " different reasons end in the same place.";
      body = cap(list(s.sources.map(R.say))) + " each lead to " + R.say(s.target) + ". Because the reasons are different, taking one away leaves the others still holding it; it changes only when each reason is met, or when that place itself is changed." + gap;
    } else {
      title = "WHERE IT IS HEADING";
      head = "One thing leads to the next, in " + (NUM[s.arrows.length] || s.arrows.length) + " steps.";
      var at2 = s.parts[0], legs2 = [];
      s.arrows.forEach(function (a) {
        var l = leg(a, at2);
        legs2.push(l.txt);
        at2 = l.to;
      });
      body = cap(R.say(s.parts[0])) + " leads " + legs2.join("; then ") + ". Left as it is, this is where the situation goes." + (gap || " The step that holds least firmly, from " + R.say(s.burden.from) + " to " + R.say(s.burden.to) + ", is the cheapest place to turn it.");
    }
    return { key: "shape", title: title, head: head, body: body, refs: refs, arrow: s.type === "settlement" ? ", " : " → ", sure: sure(s.arrows) };
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
