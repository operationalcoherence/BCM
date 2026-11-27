/* BCM project clusters (F8, lead's project copy only). Rule-based: no AI, nothing sent.
   A cluster = notes from 3+ people with the same emotion about the same thing, in their own words.
   Two people = an early thread. Matches, strongest first:
     1 same words      a shared phrase (two or three content words in a row, stemmed)
     2 similar words   shared uncommon words, any order (idf-weighted overlap)
     3 placed together same emotion and question, close on the ground to two of a cluster's notes,
                       sharing a word with each; it can join a cluster
                       of 3+ people (at most one such note for every two found by words), never make one
   Emotion names and the goal's own words never count as a match (they would pull everything together).
   Input notes: {id, t, e (0-4), q (1-7), x, y, who, voice}. Links: [{f, t}] between note ids. */
function gsmClusters(notes, goal, links, opt) {
  opt = opt || {};
  var STOPW = {};
  ("a an the and or but if then than so of to in on at by for with from into onto over under about as is are was were be been being it its this that these those there here they them their we our us you your i me my he she his her not no nor do does did done has have had will would can could should may might must just also very more most much many some any all each every other such only own same too out up down off again once what which who whom whose when where why how because while until both few s t yet still even ever get gets got make makes made way ways thing things lot " +
    "dont doesnt didnt wont cant isnt arent im ive id youre theyre thats whats whatever havent hasnt wasnt werent through across toward towards against upon another always never " +
    "last next year years week weeks day month months time times first new old good like looks see seen would one two three every part lot sure really well").split(" ").forEach(function (w) { STOPW[w] = 1; });
  var EMOW = /^(aggress|aggres|accept|distru|trust|defian|defiant|indiff|indifferen|angry|anger|furiou|glad|happy)/;
  function stem(t) {
    var e = t;
    if (/ies$/.test(e) && e.length > 5) e = e.slice(0, -3) + "y";
    else if (/ing$/.test(e) && e.length > 6) e = e.slice(0, -3).replace(/([b-df-hj-np-tv-z])\1$/, "$1");
    else if ((/ed$/.test(e) && e.length > 5) || (/es$/.test(e) && e.length > 6)) e = e.slice(0, -2);
    else if (/ers?$/.test(e) && e.length > 5) e = e.replace(/ers?$/, "");
    else if (/s$/.test(e) && !/(ss|us|is)$/.test(e) && e.length > 3) e = e.slice(0, -1);
    return e.length > 6 ? e.slice(0, 6) : e;
  }
  function toks(text) {
    var out = [];
    String(text || "").replace(/[’']/g, "").split(/[.!?;:,()\n"“”]+/).forEach(function (sen) {
      var run = [];
      (sen.toLowerCase().match(/[a-z][a-z-]*/g) || []).forEach(function (w) {
        var s = stem(w);
        run.push(!STOPW[w] && w.length > 2 && !EMOW.test(s) ? { s: s, w: w } : null);
      });
      out.push(run);
    });
    return out;
  }
  var goalW = {}, goalP = {};
  toks(goal).forEach(function (run) {
    run.forEach(function (x, i) {
      if (!x) return;
      goalW[x.s] = 1;
      run[i + 1] && (goalP[x.s + " " + run[i + 1].s] = 1);
    });
  });
  var N = notes.filter(function (n) { return n && String(n.t || "").trim() && n.e != null && n.who; });
  var df = {};
  N.forEach(function (n) {
    var runs = toks(n.t), W = {}, P = {};
    runs.forEach(function (run) {
      run.forEach(function (x, i) {
        if (!x) return;
        goalW[x.s] || (W[x.s] = x.w);
        for (var k = 2; k <= 3; k++) {
          var sl = run.slice(i, i + k);
          if (sl.length < k || sl.some(function (y) { return !y; })) break;
          var key = sl.map(function (y) { return y.s; }).join(" ");
          if (k === 2 && goalP[key]) continue;
          P[key] || (P[key] = sl.map(function (y) { return y.w; }).join(" "));
        }
      });
    });
    n._W = W; n._P = P;
    Object.keys(W).forEach(function (s) { df[s] = (df[s] || 0) + 1; });
  });
  var M = N.length || 1;
  function idf(s) { return Math.log((M + 1) / ((df[s] || 0) + 1)); }
  N.forEach(function (n) {
    var v = {}, z = 0;
    Object.keys(n._W).forEach(function (s) { v[s] = idf(s); z += v[s] * v[s]; });
    z = Math.sqrt(z) || 1;
    Object.keys(v).forEach(function (s) { v[s] /= z; });
    n._V = v;
  });
  var linked = {};
  (links || []).forEach(function (l) { l && l.f && l.t && ((linked[l.f + "|" + l.t] = 1), (linked[l.t + "|" + l.f] = 1)); });
  var SIM = opt.sim || 0.34, NEAR = opt.near || 10, MINP = opt.minp || 3, COMMON = Math.max(4, Math.round(M * 0.06));
  /* pair matches, same emotion and different people only */
  var E = N.map(function () { return []; });
  for (var i = 0; i < N.length; i++)
    for (var j = i + 1; j < N.length; j++) {
      var a = N[i], b = N[j];
      if (a.e !== b.e || a.who === b.who) continue;
      var kind = 0, why = "";
      Object.keys(a._P).some(function (k) {
        if (!b._P[k]) return false;
        why = a._P[k];
        return (kind = 1);
      });
      if (!kind) {
        var c = 0, rare = "";
        Object.keys(a._V).forEach(function (s) {
          if (b._V[s]) { c += a._V[s] * b._V[s]; df[s] <= COMMON && (!rare || df[s] < df[rare]) && (rare = s); }
        });
        if (c >= SIM && rare) { kind = 2; why = a._W[rare]; }
      }
      if (!kind && linked[a.id + "|" + b.id]) kind = 2;
      var close = a.q === b.q && a.x != null && b.x != null && Math.hypot(a.x - b.x, a.y - b.y) <= NEAR;
      if (kind) { E[i].push({ j: j, k: kind, w: why }); E[j].push({ j: i, k: kind, w: why }); }
      else if (close) { E[i].push({ j: j, k: 3 }); E[j].push({ j: i, k: 3 }); }
    }
  /* groups from word matches only: a note joins a group when it matches two of its notes, or one when the group
     is still a pair; this stops one shared word chaining unrelated notes together */
  var gid = N.map(function () { return -1; }), G = [];
  var order = N.map(function (n, i) { return i; }).sort(function (x, y) {
    return E[y].filter(function (m) { return m.k < 3; }).length - E[x].filter(function (m) { return m.k < 3; }).length;
  });
  order.forEach(function (i) {
    if (gid[i] >= 0) return;
    var g = { m: [i], how: {} };
    g.how[i] = 0;
    gid[i] = G.length;
    G.push(g);
    var grew = true;
    while (grew) {
      grew = false;
      for (var c = 0; c < N.length; c++) {
        if (gid[c] >= 0) continue;
        var hits = E[c].filter(function (m) { return m.k < 3 && gid[m.j] === gid[i]; });
        var strong = hits.some(function (m) { return m.k === 1; });
        if (hits.length >= 2 || (hits.length && (g.m.length < 3 || strong))) {
          g.m.push(c);
          gid[c] = gid[i];
          g.how[c] = Math.min.apply(null, hits.map(function (m) { return m.k; }));
          grew = true;
        }
      }
    }
  });
  /* two groups that match each other in two places (or once in the same words) become one */
  for (var again = true; again; ) {
    again = false;
    for (var g1 = 0; g1 < G.length && !again; g1++)
      for (var g2 = g1 + 1; g2 < G.length && !again; g2++) {
        if (!G[g1].m.length || !G[g2].m.length) continue;
        var x = 0, sx = 0;
        G[g2].m.forEach(function (c) { E[c].forEach(function (m) { m.k < 3 && gid[m.j] === g1 && (x++, m.k === 1 && sx++); }); });
        if (x >= 2 || sx >= 1) {
          G[g2].m.forEach(function (c) { gid[c] = g1; G[g1].m.push(c); G[g1].how[c] = G[g2].how[c] || 1; });
          G[g2].m = [];
          again = true;
        }
      }
  }
  /* placed together: a loose note joins a group of 2+ people when it sits close to two of its notes */
  G.forEach(function (g) {
    var ppl = {};
    g.m.forEach(function (i) { ppl[N[i].who] = 1; });
    if (Object.keys(ppl).length < MINP) return;
    var gi = G.indexOf(g), cap = Math.floor(g.m.length / 2), added = 0;
    N.forEach(function (n, c) {
      if (added >= cap || G[gid[c]].m.length > 1) return;
      var near = E[c].filter(function (m) {
        return m.k === 3 && gid[m.j] === gi && Object.keys(N[c]._W).some(function (s) { return N[m.j]._W[s]; });
      }).length;
      if (near >= 2) { G[gid[c]].m = []; gid[c] = gi; g.m.push(c); g.how[c] = 3; added++; }
    });
  });
  /* the group's name: the phrase most of its people share, in their own words; else the rare word they share */
  var EN = ["Aggression", "Acceptance", "Distrust", "Indifference", "Defiance"];
  function name(g) {
    var best = null;
    var cnt = {};
    g.m.forEach(function (i) {
      var seen = {};
      Object.keys(N[i]._P).forEach(function (k) {
        if (seen[k]) return;
        seen[k] = 1;
        (cnt[k] = cnt[k] || { w: N[i]._P[k], who: {} }).who[N[i].who] = 1;
      });
    });
    Object.keys(cnt).forEach(function (k) {
      var n = Object.keys(cnt[k].who).length;
      n >= 2 && (!best || n > best.n || (n === best.n && k.split(" ").length > best.k.split(" ").length)) && (best = { k: k, w: cnt[k].w, n: n });
    });
    if (best) {
      /* widen the phrase to a few of the writer's own words around it, from the shortest note that has it */
      var KEEP = { who: 1, how: 1, what: 1, where: 1, the: 1, "last": 1 };
      var src = g.m.map(function (i) { return N[i]; }).filter(function (n) { return n._P[best.k]; })
        .sort(function (a, b) { return a.t.length - b.t.length; })[0];
      var sens = String(src.t).replace(/[’]/g, "'").split(/[.!?;:,()\n"“”]+/);
      for (var si = 0; si < sens.length; si++) {
        var ws = sens[si].trim().split(/\s+/), low = ws.map(function (w) { return stem(w.toLowerCase().replace(/[^a-z-]/g, "")); });
        var first = best.k.split(" ");
        for (var wi = 0; wi + first.length <= low.length; wi++) {
          if (first.every(function (f, fi) { return low[wi + fi] === f; })) {
            var plain = function (w) { return w.toLowerCase().replace(/[^a-z]/g, ""); };
            var a0 = Math.max(0, wi - 3), a1 = wi + first.length;
            /* a question word just before the window ("who decides…") belongs to the name */
            a0 > 0 && KEEP[plain(ws[a0 - 1])] && !KEEP[plain(ws[a0])] && a0--;
            /* after the phrase: an article and the word it leads to, never a verb run like "would cut" */
            if ((ws[a1] && /^(the|a|an)$/i.test(ws[a1]) && ws[a1 + 1] && !STOPW[plain(ws[a1 + 1])])) a1 += 2;
            var cut = ws.slice(a0, a1), lead = cut.length - first.length - (a1 - wi - first.length);
            for (var moved = true; moved && lead > 0; ) {
              var w0 = plain(cut[0]);
              moved = (STOPW[w0] && !KEEP[w0]) || EMOW.test(stem(w0)) || /^(i|we|they|it|nobody|people)$/.test(w0);
              moved && (cut.shift(), lead--);
            }
            return cut.join(" ").replace(/^(the|a|an) /i, "the ").replace(/^./, function (c) { return c.toLowerCase(); });
          }
        }
      }
      return best.w;
    }
    /* no shared phrase: a single word is never the name (BCM rule); the page shows the people's own sentences */
    return "";
  }
  var out = { clusters: [], threads: [], loose: [], n: N.length };
  G.forEach(function (g) {
    if (!g.m.length) return;
    var ppl = {};
    g.m.forEach(function (i) { ppl[N[i].who] = 1; });
    var np = Object.keys(ppl).length;
    var item = {
      e: N[g.m[0]].e,
      emotion: EN[N[g.m[0]].e],
      about: name(g),
      people: np,
      notes: g.m.map(function (i) { return { id: N[i].id, who: N[i].who, voice: N[i].voice, q: N[i].q, t: N[i].t, how: g.how[i] }; }),
    };
    if (np >= 3) out.clusters.push(item);
    else if (np === 2) out.threads.push(item);
    else g.m.forEach(function (i) { out.loose.push(N[i].id); });
  });
  out.clusters.sort(function (a, b) { return b.people - a.people || b.notes.length - a.notes.length; });
  out.threads.sort(function (a, b) { return b.notes.length - a.notes.length; });
  return out;
}
typeof module !== "undefined" && (module.exports = gsmClusters);
