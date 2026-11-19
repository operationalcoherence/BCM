"""v220: the meaning pass on Pattern Analysis (his 11-18 18:05 note).
"Analysis should tell me what the findings mean, not what exists." Each finding card on Pattern Analysis now opens
with one sentence on what it means for the work, from the draft patterns (claude/meaning_patterns_draft.md in the
Claude project, Claude's wording, awaiting his redlines). What the card used to say (the words, the questions, the
counts) moves into a closed THE WORDS AND NOTES section under it, together with the notes that carry those words:
each note's number, emotion, side of the line, and a short quote.
- The subject of each sentence is the shortest sentence from the workbook that carries the finding's words, quoted
  with its source, never a lone word (his 11-12 rule).
- Emotion readings follow the paper: far-apart emotions (acceptance against distrust, aggression, or defiance) take
  a big move and no single message carries people across; indifference is the ground people move through most easily;
  aggression and defiance are the slowest ground to change; acceptance doesn't hold on its own.
- Findings that already say what they mean (CONDITION NOT IN Q.5-Q.7, FOR AND AGAINST ON THE MAP, and the rest of
  GSMMEAN) keep their sentence; it moves to the top and the rest folds under it.
- ONE WORD, SEVERAL MEANINGS and WHICH WORDS, AND WHOSE VOICES, SHAPE THIS MAP are left as they are.
- Only Pattern Analysis ([data-pv="2"]). In Parallel is the next step.
Usage: python3 v220_meaning_pass_analysis.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

JS = r'''
  function gsmMeanPass(sec) {
    setTimeout(function () {
      try {
        if (!sec || !sec.closest || !sec.closest('[data-pv="2"]')) return;
        gsmMeanRun(sec);
      } catch (e) {}
    }, 0);
  }
  var GSMEMO = ["aggression", "acceptance", "distrust", "indifference", "defiance"];
  function gsmMeanCss() {
    if (document.getElementById("gsm-mean-css")) return;
    var st = document.createElement("style");
    st.id = "gsm-mean-css";
    st.textContent =
      "#gsm .rule .rmean2{font-size:15.5px;line-height:1.5;color:#111;margin:2px 0 2px}#gsm .rule details.rev summary{margin:6px 0 2px;font-size:12.5px}#gsm .rule .revb{font-size:14px;color:#444;line-height:1.45;margin:4px 0 2px}#gsm .rule .revn{font-size:13.5px;color:#444;line-height:1.45;margin:6px 0 0;padding-left:9px;border-left:2px solid #ddd}#gsm .rule .revn div{margin:0 0 4px}#gsm .rule .revn i{font-style:normal;color:#777;font-size:12.5px}#gsm .metal li .rmean2{font-size:15px;margin:0}";
    document.head.appendChild(st);
  }
  function gsmMeanList(a) {
    return a.length < 2 ? a.join("") : a.length < 3 ? a.join(" and ") : a.slice(0, -1).join(", ") + ", and " + a[a.length - 1];
  }
  function gsmMeanRx(w) {
    w = String(w || "").replace(/[“”"]/g, "").trim().toLowerCase();
    if (!w) return null;
    var p = w.split(/\s+/).map(function (x) {
      return x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    });
    return new RegExp("\\b" + p.join("\\W+") + "(?:s|es)?\\b", "i");
  }
  function gsmMeanSrc() {
    var out = [],
      A = (C && C.a) || [];
    (C.goal || "").trim() && out.push({ ref: "GOAL", lab: "the goal", txt: C.goal });
    A.forEach(function (t, i) {
      (t || "").trim() && out.push({ ref: "Q." + (i + 1), lab: "Q." + (i + 1), txt: t, q: i + 1 });
    });
    (C.m || []).forEach(function (t, i) {
      (t[3] || "").trim() &&
        out.push({
          ref: "note " + (i + 1),
          lab: "N" + (i + 1),
          txt: t[3],
          note: 1,
          k: t[0],
          em: "number" == typeof t[5] ? t[5] : null,
          side: null != t[2] ? (t[2] < 118 ? 1 : t[2] > 118 ? -1 : 0) : 0,
        });
    });
    ((C.p && C.p.m) || []).forEach(function (t, i) {
      (t[3] || "").trim() &&
        out.push({
          ref: "P" + (i + 1),
          lab: "place note " + (i + 1),
          txt: t[3],
          note: 1,
          k: t[0],
          em: "number" == typeof t[5] ? t[5] : null,
          side: 2 === t[0] ? -1 : 3 === t[0] || 7 === t[0] ? 1 : 0,
        });
    });
    return out;
  }
  var GSMQEM = -1,
    GSMUSED = {},
    GSMUSET = 0;
  function gsmMeanQuote(cands, rx) {
    cands.sort(function (a, b) {
      return b.sc - a.sc;
    });
    var best = null;
    for (var c = 0; c < cands.length; c++)
      if (!GSMUSED[cands[c].t]) {
        best = cands[c];
        break;
      }
    best = best || cands[0];
    if (!best) return "";
    GSMUSED[best.t] = 1;
    GSMQEM = best.s.note && null != best.s.em ? best.s.em : -1;
    var w = best.t
      .replace(/[.!?]+$/, "")
      .split(/\s+/)
      .map(function (x) {
        return x.length > 30 ? x.slice(0, 28) + "…" : x;
      });
    if (w.length > 16) {
      var at = 0;
      for (var i = 0; i < w.length; i++)
        if (
          rx.some(function (r) {
            return r.test(w[i]);
          })
        ) {
          at = i;
          break;
        }
      var a = Math.max(0, Math.min(at - 4, w.length - 14));
      w = (a > 0 ? ["…"] : []).concat(w.slice(a, a + 14), a + 14 < w.length ? ["…"] : []);
    }
    return (
      "“" +
      Gt(w.join(" ").replace(/^… /, "…").replace(/ …$/, "…")) +
      "” (" +
      '<a class="ref" data-ref="' +
      Gt(best.s.ref) +
      '">' +
      Gt(best.s.lab) +
      "</a>)"
    );
  }
  function gsmMeanData(words) {
    GSMUSET ||
      (GSMUSET = setTimeout(function () {
        ((GSMUSED = {}), (GSMUSET = 0));
      }, 300));
    var rx = words.map(gsmMeanRx).filter(Boolean),
      src = gsmMeanSrc(),
      all = [],
      hc = [],
      nc = [],
      notes = [];
    src.forEach(function (s) {
      var hit = rx.filter(function (r) {
        return r.test(s.txt);
      }).length;
      if (!hit) return;
      s.note && notes.push(s);
      s.txt
        .replace(/\s+/g, " ")
        .split(/(?<=[.!?])\s+/)
        .forEach(function (se) {
          var h = rx.filter(function (r) {
              return r.test(se);
            }).length,
            n = se.split(/\s+/).length;
          if (!h || n < 3) return;
          var o = { sc: h * 30 - n - (n > 16 ? 40 : 0) + (s.note ? 10 : 0), t: se.trim(), s: s };
          all.push(o);
          (s.note ? s.side > 0 : 3 === s.q || 7 === s.q) && hc.push(o);
          (s.note ? s.side < 0 : 2 === s.q) && nc.push(o);
        });
    });
    var q = gsmMeanQuote(all.slice(), rx),
      qem = GSMQEM;
    var qh = gsmMeanQuote(hc.slice(), rx),
      qhem = GSMQEM,
      qn = gsmMeanQuote(nc.slice(), rx),
      qnem = GSMQEM;
    var cnt = [0, 0, 0, 0, 0],
      help = [0, 0, 0, 0, 0],
      hind = [0, 0, 0, 0, 0];
    notes.forEach(function (n) {
      if (null == n.em || n.em < 0 || n.em > 4) return;
      cnt[n.em]++;
      n.side > 0 ? help[n.em]++ : n.side < 0 && hind[n.em]++;
    });
    function top(a) {
      var m = Math.max.apply(null, a);
      return m > 0 ? a.indexOf(m) : -1;
    }
    var hs = 0;
    notes.forEach(function (n) {
      hs += n.side;
    });
    return { q: q, qem: qem, qh: qh, qhem: qhem, qn: qn, qnem: qnem, side: hs, notes: notes, em: top(cnt), help: top(help), hind: top(hind) };
  }
  function gsmMeanEv(d) {
    if (!d.notes.length) return "";
    var ns = d.notes.slice(0, 4).map(function (n) {
      var w = n.txt.replace(/\s+/g, " ").trim().split(" "),
        t = w.slice(0, 16).join(" ") + (w.length > 16 ? "…" : "");
      return (
        '<div><a class="ref" data-ref="' +
        Gt(n.ref) +
        '">' +
        Gt(n.lab) +
        "</a> <i>" +
        (null != n.em && GSMEMO[n.em] ? GSMEMO[n.em] : "no emotion marked") +
        (n.side > 0 ? ", helps" : n.side < 0 ? ", hinders" : "") +
        "</i>: “" +
        Gt(t) +
        "”</div>"
      );
    });
    return (
      '<div class="revn">' +
      ns.join("") +
      (d.notes.length > 4 ? "<div><i>and " + (d.notes.length - 4) + " more</i></div>" : "") +
      "</div>"
    );
  }
  var GSMREAD = {
    1: "firm ground to build on",
    3: "people aren’t engaged either way and could tip",
    2: "trust has to come before anything here moves",
    0: "expect pushback that can harden into defiance",
    4: "people resist it, so this is the last ground to work, not the first",
  };
  function gsmMeanSay(lab, words, body, d) {
    var one = 1 === words.length && /\s/.test(words[0]) && /^(ONE EMOTION THROUGHOUT|ONE SIDE OF THE LINE ONLY|HEARD FROM ONE PERSON ONLY|RESTING ON WHAT WAS SAID)$/.test(lab),
      bw = gsmMeanList(
        words.map(function (w) {
          return "<b>" + Gt(w) + "</b>";
        }),
      ),
      sn = d.qn || d.q || bw,
      enn = d.qn ? d.qnem : d.qem,
      sh = d.qh || d.q || bw,
      ehh = d.qh ? d.qhem : d.qem,
      eq = d.qem >= 0 ? d.qem : d.em,
      subj = (one ? "<b>" + Gt(words[0]) + "</b>" : d.q) || gsmMeanList(words.map(function (w) {
        return "<b>" + Gt(w) + "</b>";
      })),
      E = GSMEMO,
      far = function (a, b) {
        return (1 === a && [0, 2, 4].indexOf(b) >= 0) || (1 === b && [0, 2, 4].indexOf(a) >= 0);
      };
    if (/^(OPPOSITION NOT YET ENGAGED|SAID, BUT NOT ANSWERED)$/.test(lab))
      return (
        sn +
        " is part of why the goal hasn’t taken root, and nothing you would design touches it, so it will keep working against the plan." +
        (0 === (enn >= 0 ? enn : d.em) || 4 === (enn >= 0 ? enn : d.em)
          ? " It sits on the ground slowest to change, which makes it the likeliest place for the plan to stall."
          : "")
      );
    if (/^FOR AND AGAINST(, AND ON THE REDESIGN LIST)?$/.test(lab) || "TWO PEOPLE, TWO SIDES" === lab) {
      var h = d.help,
        n = d.hind,
        s =
          (d.qh && d.qn
            ? d.qh + " helps and " + d.qn + " hinders: people use the same words to pull the work two ways"
            : "People use " + subj + " to pull the work two ways") +
          (h >= 0 && n >= 0 ? ", as " + E[h] + " where it helps and " + E[n] + " where it hinders" : "") +
          (d.qh && d.qn
            ? ", so any move on those words will push one side further off until you settle together what they mean."
            : ", so any move on it will push one side further off until you settle together what it means.");
      h >= 0 && n >= 0 && far(h, n)
        ? (s += " Those emotions are far apart, and no single message carries people across; start where there is indifference near them.")
        : (3 === h || 3 === n) &&
          h !== n &&
          (s += " One side is indifference, the ground people move through most easily, so that’s where to settle it first.");
      return s;
    }
    if (/^(SUPPORT NOT YET REINFORCED|BUILD ON WHAT IS HAPPENING|PARTLY ALREADY)$/.test(lab))
      return (
        sh +
        " already helps the goal, and nothing you would design builds on it, so it’s the cheapest place to start." +
        (1 === (ehh >= 0 ? ehh : d.em)
          ? " Acceptance doesn’t hold on its own, so leaving it alone is a risk too."
          : 3 === (ehh >= 0 ? ehh : d.em)
            ? " It sits in indifference, so what you do next can tip it either way."
            : "")
      );
    if ("ONE EMOTION THROUGHOUT" === lab && d.em >= 0)
      return "Wherever " + subj + " appears, it carries " + E[d.em] + ", so expect the work around it to be met the same way each time: " + GSMREAD[d.em] + ".";
    if ("ONE SIDE OF THE LINE ONLY" === lab)
      return "In your notes, " + subj + " only ever " + (/below/.test(body) && !/above/.test(body) ? "hinders" : "helps") + ", which may mean you haven’t yet heard from the people who see it the other way.";
    if ("HEARD FROM ONE PERSON ONLY" === lab)
      return "What you know about " + subj + " comes from one voice, so treat it as a lead to check before you build on it.";
    if ("RESTING ON WHAT WAS SAID" === lab)
      return "What you know about " + subj + " comes from what was said, not seen, so treat it as a lead to check before you build on it.";
    if (/^(ANSWERED, WITH NOTHING ON THE MAP|NOT ON THE MAP)$/.test(lab)) {
      var qq = (body.match(/\((why[^)]*|what[^)]*|whether[^)]*)\)/) || [])[1];
      return "What you wrote " + (qq ? "about " + Gt(qq) : "in this answer") + " rests on your answer alone, with no note on the map, so treat it as a lead to check before you build on it.";
    }
    if ("PLANNED LEAST" === lab)
      return subj + " comes up often, but nothing you would design touches it: what you talk about most may be what you have planned least.";
    if ("MOST OF THE MAP ON ONE QUESTION" === lab)
      return "Most of your map is about one question, so the rest may be thinner than it looks, and that’s where surprises will come from.";
    if (/^(RUNS TOGETHER|A WORD THAT RETURNS|A WORD THAT CROSSES QUESTIONS|AT THE CENTER|A NAME THAT RECURS)$/.test(lab)) {
      var qs = (body.match(/Q\.\d/g) || []).map(function (x) {
          return +x.slice(2);
        }),
        ctx = qs.some(function (x) {
          return x <= 4;
        }),
        des = qs.some(function (x) {
          return x >= 5;
        }),
        nq = qs.filter(function (x, i) {
          return qs.indexOf(x) === i;
        }).length,
        sp = ctx && des ? "the context you have grasped and what you would design" : nq > 1 ? nq + " of your answers" : "your answers and notes";
      return (
        subj +
        " runs through " +
        sp +
        ", so changing it moves all of them at once." +
        (1 === eq || 3 === eq
          ? " On this ground, that makes it your strongest lever."
          : 0 === eq || 2 === eq || 4 === eq
            ? " On this ground, that makes it your biggest single risk."
            : "")
      );
    }
    return "";
  }
  function gsmMeanWords(el) {
    return [].slice
      .call(el.querySelectorAll("b"))
      .map(function (b) {
        return b.textContent.replace(/[“”"]/g, "").trim();
      })
      .filter(function (w, i, a) {
        return w && a.indexOf(w) === i;
      })
      .slice(0, 4);
  }
  function gsmMeanFold(body, d, extra) {
    var dt = document.createElement("details");
    dt.className = "more rev";
    dt.innerHTML = "<summary>The words and notes</summary>";
    var b = document.createElement("div");
    b.className = "revb";
    while (body.firstChild) b.appendChild(body.firstChild);
    dt.appendChild(b);
    extra && dt.insertAdjacentHTML("beforeend", extra);
    return dt;
  }
  function gsmMeanRun(sec) {
    gsmMeanCss();
    sec.querySelectorAll(".rule").forEach(function (r) {
      if (r.getAttribute("data-mp")) return;
      r.setAttribute("data-mp", "1");
      var l = r.querySelector(".rl"),
        lab = l ? l.textContent.trim() : "";
      if (!l || /^(ONE WORD, SEVERAL MEANINGS|WHICH WORDS, AND WHOSE VOICES, SHAPE THIS MAP)$/.test(lab)) return;
      var body = l.nextElementSibling,
        old = r.querySelector(".rmean");
      if (!body || body === old) return;
      if ("POSSIBLE PATTERNS" === lab) {
        body.querySelectorAll("li").forEach(function (li) {
          var tx = li.textContent,
            w = gsmMeanWords(li),
            d = w.length ? gsmMeanData(w) : null,
            k = /one person/.test(tx)
              ? "HEARD FROM ONE PERSON ONLY"
              : /same emotion/.test(tx)
                ? "ONE EMOTION THROUGHOUT"
                : /nothing you would design/.test(tx) && d
                  ? d.side < 0
                    ? "SAID, BUT NOT ANSWERED"
                    : d.side > 0
                      ? "SUPPORT NOT YET REINFORCED"
                      : "PLANNED LEAST"
                  : "",
            m = k && d ? gsmMeanSay(k, w, tx, d) : "";
          if (!m) return;
          var hold = document.createElement("div");
          while (li.firstChild) hold.appendChild(li.firstChild);
          li.innerHTML = '<div class="rmean2">' + m + "</div>";
          li.appendChild(gsmMeanFold(hold, d, gsmMeanEv(d)));
        });
        return;
      }
      var w = gsmMeanWords(body),
        d = w.length ? gsmMeanData(w) : { q: "", notes: [], em: -1, help: -1, hind: -1 },
        m = gsmMeanSay(lab, w, body.textContent, d);
      if (!m && !old) return;
      var mm = document.createElement("div");
      mm.className = "rmean2";
      m ? (mm.innerHTML = m) : (mm.textContent = old.textContent);
      old && old.parentNode.removeChild(old);
      var fd = gsmMeanFold(body, d, gsmMeanEv(d));
      body.parentNode.replaceChild(mm, body);
      mm.parentNode.insertBefore(fd, mm.nextSibling);
    });
  }
'''

rep("""  window.gsmSaveP = P;
  function P() {""", JS + """  window.gsmSaveP = P;
  function P() {""")
rep("""    if (!sec || sec.getAttribute("data-pd")) return;
    sec.setAttribute("data-pd", "1");""", """    if (!sec || sec.getAttribute("data-pd")) return;
    sec.setAttribute("data-pd", "1");
    gsmMeanPass(sec);""")
rep('t && (t.textContent = "v219");', 't && (t.textContent = "v220");')
open(P, "w").write(s)
print("ok")
