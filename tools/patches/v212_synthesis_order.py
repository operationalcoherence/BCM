"""v212: review Phase 2 step 7, Pattern Synthesis.
1. (4f) A row of the patterns sits right above the figure: tap one to draw it on the map without scrolling to the
   list below. It and the list's tick boxes stay in step.
2. (4e) The questions that sat inside WHAT THE GROUND SAYS (Does N15 support "aggressive suppression"?) are asked
   only under PATTERNS THAT RUN THROUGH IT, where the phrase is. The reading says where to answer.
3. (4g) Under PATTERNS THAT RUN THROUGH IT, read more shows the sentence from each note or answer with the phrase in
   bold. CAUSE AND EFFECT bolds the word in its quoted sentences.
4. (4i) In WHAT IT MIGHT MEAN, a finding that no note carries now names the answers it comes from (Q.3, ...), and
   those link back to the answer, as note numbers already link back to the note.
(4d, the legend, is in place since v176; 4h, IN YOUR ANSWERS, NOT ON THE MAP in phrases, since v201.)
Usage: python3 v212_synthesis_order.py gsm-readable.js   (no relief change; --relief is a no-op)"""
import sys

P = sys.argv[1]
if "--relief" in sys.argv:
    sys.exit(0)
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# 1: the row above the figure
rep(
    '<div class="msg" data-gt="msg"></div>',
    '<div class="laybar" data-gt="laybar"></div>\\n  <div class="msg" data-gt="msg"></div>',
)
rep(
    ".gterr .bar{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin:8px 0 10px;font-size:13px}",
    ".gterr .bar{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin:8px 0 10px;font-size:13px}"
    ".gterr .laybar{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:10px 0 8px}.gterr .laybar:empty{display:none}"
    ".gterr .laybar .lbl{font-size:11px;font-weight:700;letter-spacing:.14em;margin-right:4px}"
    ".gterr .laybar .lchip{font:13px Questrial,Helvetica,Arial,sans-serif;padding:6px 11px;border:1px solid #222;border-radius:16px;background:#fff;color:#222;cursor:pointer}"
    ".gterr .laybar .lchip.on{background:#3a1f0c;border-color:#3a1f0c;color:#fff}"
    ".gterr .laybar .lhelp{flex:1 1 100%;font-size:12px;color:#666;margin-top:2px}"
    ".gterr .phq{margin:6px 0 2px;font-size:13.5px;line-height:1.45}.gterr .phq div{padding-left:9px;border-left:2px solid #ddd;margin:0 0 4px}",
)
rep(
    """    function fillThreads() {
      var el = $("threads");
      el.innerHTML = "";""",
    """    function fillLay() {
      var lb = $("laybar");
      if (!lb) return;
      lb.innerHTML = "";
      if (!terr || !terr.threads.length) return;
      var lt = document.createElement("span");
      lt.className = "lbl";
      lt.textContent = "PATTERNS";
      lb.appendChild(lt);
      terr.threads.forEach(function (th) {
        var c = document.createElement("button");
        c.type = "button";
        c.className = "lchip" + (thOn[th.w] ? " on" : "");
        c.setAttribute("aria-pressed", thOn[th.w] ? "true" : "false");
        c.textContent = "“" + th.w + "”";
        c.onclick = function () {
          if (thOn[th.w]) delete thOn[th.w];
          else thOn[th.w] = 1;
          syncLay();
          render();
        };
        lb.appendChild(c);
      });
      var h = document.createElement("span");
      h.className = "lhelp";
      h.textContent = "Tap a pattern to draw it on the map; tap again to clear it. What each one means is under PATTERNS THAT RUN THROUGH IT, below the map.";
      lb.appendChild(h);
    }
    function syncLay() {
      var lb = $("laybar"),
        el = $("threads");
      lb &&
        [].forEach.call(lb.querySelectorAll(".lchip"), function (c, i) {
          var on = !!(terr.threads[i] && thOn[terr.threads[i].w]);
          c.classList.toggle("on", on);
          c.setAttribute("aria-pressed", on ? "true" : "false");
        });
      el &&
        [].forEach.call(el.querySelectorAll("input[type=checkbox]"), function (cb, i) {
          cb.checked = !!(terr.threads[i] && thOn[terr.threads[i].w]);
        });
    }
    function fillThreads() {
      fillLay();
      var el = $("threads");
      el.innerHTML = "";""",
)
rep(
    """          if (cb.checked) thOn[th.w] = 1;
          else delete thOn[th.w];
          render();""",
    """          if (cb.checked) thOn[th.w] = 1;
          else delete thOn[th.w];
          syncLay();
          render();""",
)
rep(
    "Two words used together in more than one note or answer, with what each means. Tick one to draw its loop on the map above.",
    "Two words used together in more than one note or answer, with what each means. Tick one here, or tap it in the row above the map, to draw it on the map.",
)
# 2: the questions live under PATTERNS THAT RUN THROUGH IT
rep(
    """          extra.appendChild(document.createTextNode(r.more || ""));
          (r.ask || []).forEach(function (a) {
            askRow(extra, a, r.th);
          });""",
    """          extra.appendChild(document.createTextNode(r.more || ""));""",
)
rep(
    '''          "Until you answer the question below, " +''',
    '''          "Until you answer the question about it under PATTERNS THAT RUN THROUGH IT, " +''',
)
rep(
    """                  return z && !/question below/i.test(z);""",
    """                  return z && !/until you answer/i.test(z);""",
)
# 3: the phrase in bold, in its sentences
rep(
    """        md.appendChild(document.createTextNode(f[0]));
        if (f[1]) {
          var mm = document.createElement("span");
          mm.className = "more";
          mm.textContent = "read more…";
          var ex = document.createElement("span");
          ex.style.display = "none";
          ex.textContent = " " + f[1];""",
    """        md.appendChild(document.createTextNode(f[0]));
        var qs = document.createElement("div"),
          pre = phraseRe(th.w);
        qs.className = "phq";
        th.ms.slice(0, 8).forEach(function (m) {
          var sen = (String(m.t || "").match(/[^.!?]+[.!?]*/g) || [])
            .map(function (z) {
              return z.trim();
            })
            .filter(function (z) {
              return pre.test(z);
            })[0];
          if (!sen) return;
          var mt = pre.exec(sen);
          if (sen.length > 180) {
            var st = Math.max(0, mt.index - 70),
              en = Math.min(sen.length, st + 180);
            sen = (st ? "…" : "") + sen.slice(st, en) + (en < sen.length ? "…" : "");
            mt = pre.exec(sen);
          }
          var d = document.createElement("div"),
            bb = document.createElement("b");
          d.appendChild(document.createTextNode(m.id + ": “" + sen.slice(0, mt.index)));
          bb.textContent = mt[0];
          d.appendChild(bb);
          d.appendChild(document.createTextNode(sen.slice(mt.index + mt[0].length) + "”"));
          qs.appendChild(d);
        });
        if (f[1] || qs.childNodes.length) {
          var mm = document.createElement("span");
          mm.className = "more";
          mm.textContent = "read more…";
          var ex = document.createElement("span");
          ex.style.display = "none";
          ex.textContent = f[1] ? " " + f[1] : "";
          qs.childNodes.length && ex.appendChild(qs);""",
)
rep(
    """                return '<div class="cq">' + P[i].l + ": “" + Gt(P[i].s) + "”</div>";""",
    """                return (
                  '<div class="cq">' +
                  P[i].l +
                  ": “" +
                  Gt(P[i].s).replace(new RegExp("\\\\b(" + b.k + "[a-z]*)", "gi"), "<b>$1</b>") +
                  "”</div>"
                );""",
)
# 4: a finding no note carries names the answers it comes from
rep(
    """  function gsmPhNameH(key, ctx) {
    var m = gsmPhName(key, ctx);
    return Gt(m.ph) + (m.ids.length ? " (" + phList(m.ids.slice(0, 3)) + ")" : "");
  }""",
    """  function gsmPhNameH(key, ctx) {
    var m = gsmPhName(key, ctx),
      ids = m.ids;
    if (!ids.length) {
      var stems = String(key).split(" ");
      ids = phKeep(function () {
        return phAll()
          .filter(function (x) {
            return /^Q/.test(x.src) && (!ctx || x.q <= 4) && phIn(stems, x.t);
          })
          .map(function (x) {
            return x.src;
          });
      });
    }
    return Gt(m.ph) + (ids.length ? " (" + phList(ids.slice(0, 3)) + ")" : "");
  }""",
)
s = s.replace('t.textContent = "v211"', 't.textContent = "v212"')
assert 't.textContent = "v212"' in s
open(P, "w").write(s)
