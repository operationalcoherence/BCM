"""v313: F8 step 6, the dashboard reading. Under EVERY WORKBOOK, the lead gets READING THEM TOGETHER:
a voice filter; See everyone's ground together (opens one combined copy of everyone's answers and notes, so
Pattern Analysis shows everyone's ground on the 3D relief, and Taking Action works from all of it; the lead's own
workbook is parked and comes back, like an invite link); WHERE THEY AGREE; WHERE THEY SPLIT; EMOTION BY VOICE;
WHAT NOBODY HAS SAID YET. "Patterns suggests; you decide." said once, at the top of the reading.
Run from the repository root:  python3 tools/patches/v313_dashboard_reading.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:80])
    s = s.replace(old, new)

rep('t && (t.textContent = "v312");', 't && (t.textContent = "v313");')

# ---------- boot: a read-together copy (#bcmread=pid) parks the lead's own workbook, like an invite link
rep('''      m = /[#&]bcmjoin=([A-Za-z0-9]{1,40})\\.([A-Za-z0-9]{20,64})/.exec(location.hash || ""),
      cur = null;''',
'''      m = /[#&]bcmjoin=([A-Za-z0-9]{1,40})\\.([A-Za-z0-9]{20,64})/.exec(location.hash || ""),
      m2 = /[#&]bcmread=([A-Za-z0-9]{1,40})/.exec(location.hash || ""),
      RD = "groundsmith-web-f8read",
      RDM = "groundsmith-web-f8readmeta",
      cur = null;''')
rep('''      if (!cur) {
        var own = ls.getItem(S);
        put(SOLO, own);
      } else if (cur.pid !== pid) put(PK(cur.pid), ls.getItem(S));
      if (!cur || cur.pid !== pid) put(S, ls.getItem(PK(pid)));
      ls.setItem(CUR, JSON.stringify({ pid: pid, key: m[2] }));
      window.gsmJoin = { pid: pid, key: m[2] };
    } else if (cur && cur.pid) {
      put(PK(cur.pid), ls.getItem(S));
      put(S, ls.getItem(SOLO));
      ls.removeItem(SOLO);
      ls.removeItem(CUR);
    }''',
'''      if (!cur) {
        var own = ls.getItem(S);
        put(SOLO, own);
      } else if (!cur.read && cur.pid !== pid) put(PK(cur.pid), ls.getItem(S));
      if (!cur || cur.read || cur.pid !== pid) put(S, ls.getItem(PK(pid)));
      ls.setItem(CUR, JSON.stringify({ pid: pid, key: m[2] }));
      window.gsmJoin = { pid: pid, key: m[2] };
    } else if (m2 && ls.getItem(RD)) {
      /* v313: the lead reads everyone together. The copy is for reading only: it is never sent, and it is
         dropped when the page is opened without the link. */
      if (!cur) put(SOLO, ls.getItem(S));
      else if (!cur.read) put(PK(cur.pid), ls.getItem(S));
      put(S, ls.getItem(RD));
      ls.setItem(CUR, JSON.stringify({ pid: m2[1], read: 1 }));
      var meta = null;
      try {
        meta = JSON.parse(ls.getItem(RDM) || "null");
      } catch (e) {}
      window.gsmRead = { pid: m2[1], meta: meta || {} };
    } else if (cur && cur.pid) {
      cur.read ? (ls.removeItem(RD), ls.removeItem(RDM)) : put(PK(cur.pid), ls.getItem(S));
      put(S, ls.getItem(SOLO));
      ls.removeItem(SOLO);
      ls.removeItem(CUR);
    }''')
rep('''    var had = !!window.gsmJoin,
      has = /[#&]bcmjoin=/.test(location.hash || "");
    if (had !== has || (has && location.hash.indexOf(window.gsmJoin.pid + "." + window.gsmJoin.key) < 0)) location.reload();''',
'''    var had = !!window.gsmJoin,
      has = /[#&]bcmjoin=/.test(location.hash || ""),
      rhad = !!window.gsmRead,
      rhas = /[#&]bcmread=/.test(location.hash || "");
    if (had !== has || (has && location.hash.indexOf(window.gsmJoin.pid + "." + window.gsmJoin.key) < 0) || (!has && rhad !== rhas)) location.reload();''')

# ---------- CSS for the reading
rep('''    "#gsm-lead .ewv .ewh{font-weight:700;letter-spacing:.12em;font-size:11px;margin:10px 0 2px}" +''',
'''    "#gsm-lead .ewv .ewh{font-weight:700;letter-spacing:.12em;font-size:11px;margin:10px 0 2px}" +
    "#gsm-lead .rdg{border-top:1.5px solid #222;margin:16px 0 0;padding:10px 0 0}#gsm-lead .rdg .rh{font-weight:700;letter-spacing:.12em;font-size:11.5px;margin:14px 0 4px}" +
    "#gsm-lead .rdg .rh:first-child{margin-top:0}#gsm-lead .rdg .rpsd{font-style:italic;color:#444;margin:2px 0 8px}" +
    "#gsm-lead .vfl{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 10px}#gsm-lead .vfl button{border:1px solid #222;border-radius:14px;padding:4px 11px;font:13px 'Questrial',sans-serif;background:#fff;color:#222;cursor:pointer;min-height:32px}" +
    "#gsm-lead .vfl button.on{background:#222;color:#fff}" +
    "#gsm-lead .rit{border-left:3px solid #222;padding:4px 0 4px 10px;margin:8px 0}#gsm-lead .rit.rsp{border-left-color:#c8352e}" +
    "#gsm-lead .rit .rm{margin:0 0 4px}#gsm-lead .rit .rq{font-size:13px;color:#333;margin:3px 0;overflow-wrap:anywhere}#gsm-lead .rit .rq i{color:#777;font-style:normal}" +
    "#gsm-lead .ebar{display:flex;height:12px;border:1px solid #bbb;margin:3px 0 2px;max-width:420px}#gsm-lead .ebar span{display:block;height:100%}" +
    "#gsm-lead .evr{margin:8px 0}#gsm-lead .rgap li{margin:3px 0}#gsm-lead .rgap{margin:4px 0;padding-left:20px}" +''')

# ---------- the reading functions, before draw()
rep('''  function draw() {
    if (!box) return;
    var b = st.view === "signin" ? viewSignin()''',
r'''  /* v313: F8 step 6 - the dashboard reading. Worked out on this device from the workbooks already read for the
     table; no extra reads. "Things" are two- and three-word phrases (stop words skipped, words stemmed) that two or
     more people use; single words are never stated on their own here. Each is shown with each person's own sentence
     and where it is. */
  var STOPW = {};
  "a an the and or but if then than so of to in on at by for with from into onto over under about as is are was were be been being it its this that these those there here they them their we our us you your i me my he she his her not no nor do does did done has have had will would can could should may might must just also very more most much many some any all each every other such only own same too out up down off again once what which who whom whose when where why how because while until both few s t yet still even ever get gets got make makes made way ways thing things lot".split(" ").forEach(function (w) {
    STOPW[w] = 1;
  });
  var QSIDE = { 1: "hinder", 2: "help" },
    QWHAT = ["why the goal has not taken root", "the opposition", "the support", "Q.4", "Q.5", "Q.6", "Q.7"],
    SRCW = ["seen", "told", "documented", "assumed"];
  function stem(t) {
    var e = t;
    if (/ies$/.test(e) && e.length > 5) e = e.slice(0, -3) + "y";
    else if (/ing$/.test(e) && e.length > 5) e = e.slice(0, -3);
    else if ((/ed$/.test(e) && e.length > 5) || (/es$/.test(e) && e.length > 6)) e = e.slice(0, -2);
    else if (/s$/.test(e) && !/(ss|us|is)$/.test(e) && e.length > 3) e = e.slice(0, -1);
    return e.length > 6 ? e.slice(0, 6) : e;
  }
  function phrases(text) {
    var out = {};
    String(text || "")
      .replace(/[’']/g, "")
      .split(/[.!?;:,()\n"“”]+/)
      .forEach(function (sen) {
        var ws = sen.toLowerCase().match(/[a-z][a-z-]*/g) || [],
          run = [];
        ws.forEach(function (w, i) {
          var c = !STOPW[w] && w.length > 2;
          run.push(c ? { s: stem(w), w: w } : null);
        });
        for (var i = 0; i < run.length; i++) {
          if (!run[i]) continue;
          for (var n = 2; n <= 3; n++) {
            var sl = run.slice(i, i + n);
            if (sl.length < n || sl.some(function (x) { return !x; })) break;
            var k = sl.map(function (x) { return x.s; }).join(" ");
            out[k] || (out[k] = sl.map(function (x) { return x.w; }).join(" "));
          }
        }
      });
    return out;
  }
  function trim(t, n) {
    t = String(t || "").replace(/\s+/g, " ").trim();
    return t.length > n ? t.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : t;
  }
  function vrows() {
    return dash.rows.filter(function (r) {
      return r.ok && (!dash.voice || (r.voice || "No voice") === dash.voice);
    });
  }
  /* every place a person wrote: answers (Q.n) and notes (side, emotion, source) */
  function spots(r) {
    var L = [],
      a = Array.isArray(r.w.a) ? r.w.a : [];
    for (var i = 0; i < 7; i++) String(a[i] || "").trim() && L.push({ r: r, q: i, t: String(a[i]), side: QSIDE[i] || "", e: null });
    var line = Array.isArray(r.w.m) ? r.w.m : [];
    r.list.forEach(function (n) {
      var onLine = line.indexOf(n) >= 0;
      L.push({ r: r, q: -1, t: String(n[3]), side: onLine && n[2] != null ? (n[2] < 118 ? "help" : n[2] > 118 ? "hinder" : "") : "", e: n[5] != null && EMOS[n[5]] ? n[5] : null, place: !onLine, src: n[6] });
    });
    return L;
  }
  function whereOf(x) {
    if (x.q >= 0) return "Q." + (x.q + 1);
    if (x.place) return "place map" + (x.e != null ? ", " + EMOS[x.e][0].toLowerCase() : "");
    return (x.side ? x.side + " side" : "on the line") + (x.e != null ? ", " + EMOS[x.e][0].toLowerCase() : "");
  }
  var FAR = function (a, b) {
    return (a === 1 && (b === 0 || b === 2 || b === 4)) || (b === 1 && (a === 0 || a === 2 || a === 4));
  };
  function shared(rows) {
    var goal = phrases(st.cur && st.cur.goal),
      by = {};
    rows.forEach(function (r) {
      spots(r).forEach(function (x) {
        var ph = phrases(x.t);
        Object.keys(ph).forEach(function (k) {
          var b = by[k] || (by[k] = { k: k, w: ph[k], who: {}, xs: [] });
          b.who[r.uid] = 1;
          b.xs.length < 40 && b.xs.push(x);
        });
      });
    });
    var L = Object.keys(by)
      .map(function (k) {
        var b = by[k];
        b.n = Object.keys(b.who).length;
        return b;
      })
      .filter(function (b) {
        return b.n >= 2;
      });
    /* a longer phrase used by the same people stands for its parts */
    L = L.filter(function (b) {
      return !L.some(function (o) {
        return o !== b && o.k.length > b.k.length && (" " + o.k + " ").indexOf(" " + b.k + " ") >= 0 && o.n >= b.n;
      });
    });
    var agree = [],
      split = [];
    L.forEach(function (b) {
      var sides = {},
        emos = {};
      b.xs.forEach(function (x) {
        x.side && ((sides[x.side] = sides[x.side] || {}), (sides[x.side][x.r.uid] = x));
        x.e != null && ((emos[x.e] = emos[x.e] || {}), (emos[x.e][x.r.uid] = x));
      });
      var ek = Object.keys(emos).map(Number),
        far = null,
        cross = null,
        X = b.xs;
      for (var i = 0; i < X.length; i++)
        for (var j = 0; j < X.length; j++) {
          if (X[i].r === X[j].r) continue;
          !cross && X[i].side === "help" && X[j].side === "hinder" && (cross = [X[i], X[j]]);
          !far && X[i].e != null && X[j].e != null && X[i].e === 1 && FAR(X[i].e, X[j].e) && (far = [X[i], X[j]]);
        }
      var hu = sides.help ? Object.keys(sides.help) : [],
        nu = sides.hinder ? Object.keys(sides.hinder) : [];
      if (cross || far) {
        split.push({ b: b, pair: cross || far, how: cross ? "side" : "emo" });
        return;
      }
      if (goal[b.k]) return;
      var seen = {},
        xs = b.xs.filter(function (x) {
          return !seen[x.r.uid] && (seen[x.r.uid] = 1);
        }),
        side = hu.length >= 2 ? "help" : nu.length >= 2 ? "hinder" : "",
        sameQ = (function () {
          var c = {};
          b.xs.forEach(function (x) {
            x.q >= 0 && ((c[x.q] = c[x.q] || {}), (c[x.q][x.r.uid] = 1));
          });
          for (var q in c) if (Object.keys(c[q]).length >= 2) return +q;
          return -1;
        })(),
        emo = ek.filter(function (e) { return Object.keys(emos[e]).length >= 2; })[0];
      if (!(side || sameQ >= 0 || emo != null)) return;
      /* show the sentences that carry the agreement, one per person */
      side && emo != null && !b.xs.some(function (x) { return x.side === side && x.e === emo; }) && (emo = null);
      var fit = function (x) {
          return side ? x.side === side : sameQ >= 0 ? x.q === sameQ : x.e === emo;
        },
        sn = {};
      xs = b.xs
        .slice()
        .sort(function (x, y) {
          return (emo != null && y.e === emo) - (emo != null && x.e === emo);
        })
        .filter(function (x) {
          return fit(x) && !sn[x.r.uid] && (sn[x.r.uid] = 1);
        });
      agree.push({ b: b, xs: xs, side: side, q: sameQ, e: emo });
    });
    var rank = function (a, c) {
      return c.b.n - a.b.n || c.b.k.length - a.b.k.length;
    };
    return { agree: agree.sort(rank), split: split.sort(rank) };
  }
  function said(x) {
    return '<div class="rq"><b>' + esc(x.r.name) + "</b>" + (x.r.voice ? " · " + esc(x.r.voice) : "") + ": “" + esc(trim(x.t, 160)) + "” <i>(" + esc(whereOf(x)) + ")</i></div>";
  }
  function agreeItem(a) {
    var who = a.xs.length + " people",
      m = a.side
        ? who + " put “" + a.b.w + "” on the " + a.side + " side" + (a.e != null ? ", with " + EMOS[a.e][0].toLowerCase() : "") + ". On this, the project already stands on common ground."
        : a.q >= 0
          ? who + " name “" + a.b.w + "” when they write about " + QWHAT[a.q] + ". It is part of the situation as more than one person sees it."
          : who + " tie “" + a.b.w + "” to " + EMOS[a.e][0].toLowerCase() + ". The same emotion attached to the same thing tends to hold steady.";
    return '<div class="rit"><div class="rm">' + esc(m) + "</div>" + a.xs.slice(0, 4).map(said).join("") + (a.xs.length > 4 ? '<div class="rq"><i>…and ' + (a.xs.length - 4) + " more</i></div>" : "") + "</div>";
  }
  function splitItem(x) {
    var A = x.pair[0],
      B = x.pair[1],
      m =
        x.how === "side"
          ? A.r.name + " reads “" + x.b.w + "” as helping the goal; " + B.r.name + " reads it as hindering it. The same thing read two ways is where the project’s reading splits, and where a conversation would move it most."
          : A.r.name + " ties “" + x.b.w + "” to " + EMOS[A.e][0].toLowerCase() + "; " + B.r.name + " ties it to " + EMOS[B.e][0].toLowerCase() + ". Between them there is no ridge of indifference, so moving one toward the other takes real effort.";
    return '<div class="rit rsp"><div class="rm">' + esc(m) + "</div>" + said(A) + said(B) + (x.b.n > 2 ? '<div class="rq"><i>' + (x.b.n - 2) + " more " + (x.b.n === 3 ? "person uses" : "people use") + " it too.</i></div>" : "") + "</div>";
  }
  function byVoice(rows) {
    var V = {};
    rows.forEach(function (r) {
      var k = r.voice || "No voice",
        v = V[k] || (V[k] = { k: k, ppl: 0, c: [0, 0, 0, 0, 0], n: 0 });
      v.ppl++;
      r.list.forEach(function (n) {
        n[5] != null && EMOS[n[5]] && (v.c[n[5]]++, v.n++);
      });
    });
    return Object.keys(V)
      .map(function (k) { return V[k]; })
      .sort(function (a, b) { return b.ppl - a.ppl || b.n - a.n; });
  }
  function voiceHtml(rows) {
    var V = byVoice(rows).filter(function (v) { return v.n; });
    if (!V.length) return '<div class="lh">Nobody has marked an emotion on a note yet.</div>';
    var lean = function (v) {
      var i = v.c.indexOf(Math.max.apply(null, v.c));
      return i;
    };
    var h = V.map(function (v) {
      var order = [1, 3, 2, 0, 4];
      return (
        '<div class="evr"><b>' + esc(v.k) + '</b> <span class="lh">' + v.ppl + (v.ppl === 1 ? " person" : " people") + ", " + v.n + (v.n === 1 ? " note" : " notes") + " with an emotion</span>" +
        '<div class="ebar" aria-hidden="true">' + order.map(function (i) { return v.c[i] ? '<span style="width:' + (100 * v.c[i]) / v.n + "%;background:" + EMOS[i][1] + '"></span>' : ""; }).join("") + "</div>" +
        '<div class="lh">' + order.filter(function (i) { return v.c[i]; }).map(function (i) { return EMOS[i][0] + " " + Math.round((100 * v.c[i]) / v.n) + "%"; }).join(", ") + "</div></div>"
      );
    }).join("");
    if (V.length >= 2) {
      var l = V.map(lean),
        diff = l.some(function (x) { return x !== l[0]; });
      h += '<div class="lh" style="margin-top:6px">' + esc(
        diff
          ? "The voices lean different ways: " + V.slice(0, 4).map(function (v, i) { return v.k + " toward " + EMOS[l[i]][0].toLowerCase(); }).join(", ") + ". Where a voice stands is where change with that voice starts from."
          : "Every voice leans toward " + EMOS[l[0]][0].toLowerCase() + ". On emotion, the voices are not far apart."
      ) + "</div>";
    }
    return h;
  }
  function gapsHtml(rows) {
    var G = [],
      p = st.cur,
      ans = [0, 0, 0, 0, 0, 0, 0],
      sides = { help: 0, hinder: 0 },
      emo = [0, 0, 0, 0, 0],
      src = [0, 0, 0, 0],
      nsrc = 0,
      notes = 0,
      line = 0;
    rows.forEach(function (r) {
      spots(r).forEach(function (x) {
        if (x.q >= 0) return void ans[x.q]++;
        notes++;
        x.place || line++;
        x.side && sides[x.side]++;
        x.e != null && emo[x.e]++;
        x.src != null && SRCW[x.src] && (src[x.src]++, nsrc++);
      });
    });
    var noQ = [];
    ans.forEach(function (c, i) { c || noQ.push("Q." + (i + 1)); });
    noQ.length && G.push(noQ.length === 7 ? "Nobody has answered any of the seven questions yet." : "Nobody has answered " + noQ.join(", ").replace(/, (Q\.\d)$/, ", or $1") + " yet." + (noQ.some(function (q) { return +q.slice(2) <= 4; }) ? " Until someone does, part of the context goes ungrasped." : " Until someone does, there is less to design from."));
    var have = {};
    dash.rows.forEach(function (r) { r.voice && (have[r.voice.replace(/^Other:\s*/i, "").toLowerCase()] = 1); });
    var missing = (p.voices || []).filter(function (v) { return !have[String(v).toLowerCase()]; });
    !dash.voice && missing.length && G.push("No one has answered as " + missing.join(", ").replace(/, ([^,]+)$/, ", or $1") + ". The reading below has nothing from " + (missing.length === 1 ? "that voice." : "those voices."));
    var silent = rows.filter(function (r) { return !r.notes; });
    silent.length && silent.length < rows.length && G.push(silent.map(function (r) { return r.name; }).join(", ").replace(/, ([^,]+)$/, ", and $1") + (silent.length === 1 ? " has" : " have") + " not written a note yet.");
    if (line >= 4) {
      !sides.help && G.push("Nobody has put anything on the help side of the line. What already moves toward the goal is not on the map yet.");
      !sides.hinder && G.push("Nobody has put anything on the hinder side of the line. What holds the situation in place is not on the map yet.");
    }
    if (notes >= 6) {
      var none = [];
      emo.forEach(function (c, i) { c || none.push(EMOS[i][0].toLowerCase()); });
      none.length && none.length < 5 && G.push("Nobody has marked " + none.join(", ").replace(/, ([^,]+)$/, ", or $1") + ". Either it is not in the situation, or nobody has said so yet.");
    }
    if (nsrc >= 6) {
      !src[0] && G.push("Nobody has marked a note as something they saw themselves. Everything on the map is told, documented, or assumed.");
      src[3] / nsrc >= 0.5 && G.push(Math.round((100 * src[3]) / nsrc) + "% of the notes with a source are assumed. Much of the ground rests on what people expect rather than what they know.");
    }
    return G.length ? '<ul class="rgap">' + G.map(function (g) { return "<li>" + esc(g) + "</li>"; }).join("") + "</ul>" : '<div class="lh">Nothing stands out as missing.</div>';
  }
  /* one combined copy of everyone's work (in the voice chosen), in the workbook's own format */
  function together(rows) {
    var p = st.cur,
      W = { goal: p.goal || "", a: ["", "", "", "", "", "", ""], m: [], p: { m: [] }, voices: [], links: [], others: [], who: "Everyone", log: [], decisions: {} };
    if (p.map && p.map.kind === "place" && p.map.p)
      try {
        var pl = JSON.parse(p.map.p);
        pl && typeof pl === "object" && ((W.p = pl), (W.p.m = []));
      } catch (e) {}
    var A = [[], [], [], [], [], [], []];
    rows.forEach(function (r, ri) {
      var w = r.w,
        ids = {},
        tag = "w" + ri + "-";
      for (var i = 0; i < 7; i++) String((w.a || [])[i] || "").trim() && A[i].push(String(w.a[i]).trim());
      [[w.m, W.m], [w.p && w.p.m, W.p.m]].forEach(function (pr) {
        (Array.isArray(pr[0]) ? pr[0] : []).forEach(function (n, j) {
          if (!Array.isArray(n)) return;
          var c = n.slice();
          for (; c.length < 10; ) c.push(null);
          var id = tag + (c[8] || (pr[1] === W.m ? "L" : "P") + j);
          c[8] && (ids[c[8]] = id);
          c[8] = id;
          c[9] = r.name;
          c[7] || (c[7] = r.voice || null);
          pr[1].push(c);
        });
      });
      !W.p.loc && w.p && w.p.loc && ((W.p.loc = w.p.loc), (W.p.c = w.p.c), (W.p.name = w.p.name));
      (w.links || []).forEach(function (l) {
        if (!l || typeof l !== "object") return;
        var c = Object.assign({}, l);
        ids[c.f] && (c.f = ids[c.f]);
        ids[c.t] && (c.t = ids[c.t]);
        W.links.push(c);
      });
      [r.voice].concat(w.voices || []).forEach(function (v) {
        v && W.voices.indexOf(v) < 0 && W.voices.push(v);
      });
    });
    W.a = A.map(function (L) { return L.join("\n\n"); });
    W.view = W.p.loc && W.p.m.length && !W.m.length ? "place" : "line";
    return W;
  }
  function openTogether() {
    var rows = vrows(),
      p = st.cur;
    if (!rows.length) return;
    try {
      localStorage.setItem("groundsmith-web-f8read", JSON.stringify(together(rows)));
      localStorage.setItem("groundsmith-web-f8readmeta", JSON.stringify({ name: p.name, voice: dash.voice || "", n: rows.length, at: Date.now() }));
    } catch (e) {
      dash.err = "This device has no room to open everyone together.";
      return drawDash();
    }
    location.hash = "bcmread=" + p.id;
    location.reload();
  }
  function readHtml() {
    var all = dash.rows.filter(function (r) { return r.ok; });
    if (!all.length) return "";
    var rows = vrows(),
      vs = [];
    all.forEach(function (r) {
      var v = r.voice || "No voice";
      vs.indexOf(v) < 0 && vs.push(v);
    });
    dash.voice && vs.indexOf(dash.voice) < 0 && (dash.voice = "");
    rows = vrows();
    var ans = [0, 0, 0, 0, 0, 0, 0];
    rows.forEach(function (r) {
      for (var i = 0; i < 7; i++) String((r.w.a || [])[i] || "").trim() && (ans[i] = 1);
    });
    var nq = ans.reduce(function (a, b) { return a + b; }, 0),
      h = '<div class="rdg"><div class="rh">READING THEM TOGETHER</div><div class="rpsd">Patterns suggests; you decide.</div>';
    vs.length > 1 &&
      (h += '<div class="vfl" role="group" aria-label="Voice"><button type="button" data-l="rvoice" data-v=""' + (dash.voice ? "" : ' class="on" aria-pressed="true"') + ">Every voice</button>" +
        vs.map(function (v) { return '<button type="button" data-l="rvoice" data-v="' + esc(v) + '"' + (dash.voice === v ? ' class="on" aria-pressed="true"' : "") + ">" + esc(v) + "</button>"; }).join("") + "</div>");
    h +=
      '<div class="lrow"><button type="button" class="btn" style="width:auto;flex:none" data-l="rtog">See ' + (dash.voice ? esc(dash.voice) + " together" : "everyone’s ground together") + " →</button></div>" +
      '<div class="lh">Opens one workbook that holds the answers and notes of ' + rows.length + (rows.length === 1 ? " person" : " people") +
      ", so Pattern Analysis shows the ground they make together, in 3D, and Taking Action reads all of it. It is a copy for reading: nothing there is sent or kept. Your own workbook comes back with Back to my own workbook." +
      (nq < 7 ? " Pattern Analysis opens once each of the seven questions has an answer from someone; so far " + nq + " of 7 do." : "") + "</div>";
    if (rows.length < 2) h += '<div class="lh" style="margin-top:8px">WHERE THEY AGREE and WHERE THEY SPLIT need at least two people' + (dash.voice ? " in this voice" : "") + ".</div>";
    else {
      var S = shared(rows);
      h += '<div class="rh">WHERE THEY SPLIT</div>' + (S.split.length ? S.split.slice(0, 4).map(splitItem).join("") + (S.split.length > 4 ? '<div class="lh">…and ' + (S.split.length - 4) + " more.</div>" : "") : '<div class="lh">Nobody yet reads the same thing two ways.</div>');
      h += '<div class="rh">WHERE THEY AGREE</div>' + (S.agree.length ? S.agree.slice(0, 4).map(agreeItem).join("") + (S.agree.length > 4 ? '<div class="lh">…and ' + (S.agree.length - 4) + " more.</div>" : "") : '<div class="lh">No two people name the same thing in the same way yet.</div>');
    }
    h += '<div class="rh">EMOTION BY VOICE</div>' + voiceHtml(rows);
    h += '<div class="rh">WHAT NOBODY HAS SAID YET</div>' + gapsHtml(rows);
    return h + "</div>";
  }
  function draw() {
    if (!box) return;
    var b = st.view === "signin" ? viewSignin()''')

rep('''    dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true };''',
    '''    dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "" };''')
rep('''    if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true };''',
    '''    if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "" };''')

# the reading sits inside the EVERY WORKBOOK box, after Stop / Start taking answers
rep('''      '<span class="lh">' + (dash.taking ? "Stops new saves from everyone. You can start again at any time." : "People’s work is sent again on their next save.") + "</span></div>";
    return h + "</div>";''',
'''      '<span class="lh">' + (dash.taking ? "Stops new saves from everyone. You can start again at any time." : "People’s work is sent again on their next save.") + "</span></div>";
    return h + readHtml() + "</div>";''')

rep('''    else if (k === "dtake") setTaking(!dash.taking);''',
'''    else if (k === "dtake") setTaking(!dash.taking);
    else if (k === "rvoice") ((dash.voice = b.getAttribute("data-v") || ""), drawDash());
    else if (k === "rtog") openTogether();''')

# ---------- the bar shown while reading everyone together
rep('''/* v311: F8 step 4 - the invited person.''',
r'''/* v313: F8 step 6 - reading everyone together (#bcmread=pid). The page holds a combined copy the lead's
   dashboard made; this bar says so, and Back to my own workbook brings the lead's own workbook back. */
!(function () {
  var R = window.gsmRead;
  if (!R) return;
  var M = R.meta || {};
  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function start() {
    var host = document.getElementById("gsm"),
      after = host && host.querySelector(".dsc");
    if (!after || !document.getElementById("gsm-ways")) return false;
    var css = document.createElement("style");
    css.textContent =
      "#gsm-rbar{border:1.5px solid #222;padding:12px 14px;margin:14px 0 4px;font-size:14.5px;line-height:1.45;background:#fff}" +
      "#gsm-rbar .jt{font-weight:700;letter-spacing:.14em;font-size:12px;margin:0 0 6px}#gsm-rbar .jh{font-size:12.5px;color:#666;margin:3px 0 0}" +
      "@media print{#gsm-rbar .lnk{display:none}}";
    document.head.appendChild(css);
    var bar = document.createElement("div");
    bar.id = "gsm-rbar";
    bar.innerHTML =
      '<div class="jt">' + esc(String(M.name || "A shared project").toUpperCase()) + " · EVERYONE TOGETHER</div>" +
      "<div>" + (M.n || 0) + ((M.n || 0) === 1 ? " person" : " people") + (M.voice ? ", " + esc(M.voice) + " only" : ", every voice") + ". Their answers and notes are read here as one workbook.</div>" +
      '<div class="jh">A copy for reading, made ' + (M.at ? new Date(M.at).toLocaleString([], { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" }) : "") + ". Nothing here is sent or kept. Pattern Analysis shows the ground they make together.</div>" +
      '<div style="margin-top:8px"><a class="lnk sm" href="' + esc(location.origin + location.pathname + location.search) + '">Back to my own workbook</a></div>';
    after.parentNode.insertBefore(bar, after.nextSibling);
    try {
      window.gsmTab && window.gsmTab(2);
    } catch (e) {}
    return true;
  }
  var n = 0,
    t = setInterval(function () {
      (start() || ++n > 120) && clearInterval(t);
    }, 250);
})();

/* v311: F8 step 4 - the invited person.''')

open(P, 'w', encoding='utf-8').write(s)
print('ok')
