# v287: tidy, second pass (his "keep searching", 25 Nov 2026 18:59). Engine fixes; his rule that a single
# word is never stated as a finding (emotion names excepted) applied where it was still broken.
# 1. FOR AND AGAINST, ROOT CONDITION, READY TO REINFORCE, REDESIGN THE RESISTANCE, BUILD OR REBUILD:
#    phrases only, never single shared words ("emergent, organization, leadership").
# 2. WHERE THESE MEET: no "The word ..." entries (single words).
# 3. POSSIBLE PATTERNS: no "“command” sits behind two findings" for a single word.
# 4. WHERE THE CARDS MEET: a name that is a piece of another on the same line is said once.
# 5. DOES THIS SERVE THE GOAL?: its questions now sit under its own heading on Taking Action, not inside
#    IN YOUR ANSWERS, NOT ON THE MAP on Pattern Analysis (the heading had moved in v269; its body had not).
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

rep('''    function fo(t, e) {
      return co(
        Object.keys(i[t].k).filter(function (t) {
          return i[e].k[t];
        }),''', '''    function fo(t, e) {
      return co(
        Object.keys(i[t].k).filter(function (t) {
          /* v287: a single word is not stated as a finding */
          return i[e].k[t] && (t.indexOf(" ") > 0 || GSM_EMOW.test(t));
        }),''')

rep('''          out.sort(function (a, b) {
            return b.n - a.n || b.f - a.f;
          });
          out = out.slice(0, 6);''', '''          out.sort(function (a, b) {
            return b.n - a.n || b.f - a.f;
          });
          /* v287: no single words here */
          out = out.filter(function (o) {
            return !o.w || o.k.slice(2).indexOf(" ") > 0 || GSM_EMOW.test(o.k.slice(2));
          });
          out = out.slice(0, 6);''')

rep('''                    if (
                      (n.forEach(function (n) {
                        ((n[0] === t.lab && n[1] === e.lab) || (n[0] === e.lab && n[1] === t.lab)) &&
                          (l = n[2]);
                      }),''', '''                    if (a.length && String(a[0]).indexOf(" ") < 0 && !GSM_EMOW.test(String(a[0]).toLowerCase())) return;
                    if (
                      (n.forEach(function (n) {
                        ((n[0] === t.lab && n[1] === e.lab) || (n[0] === e.lab && n[1] === t.lab)) &&
                          (l = n[2]);
                      }),''')

rep('''                    o.push(
                      s.map(n).join(", ") +
                        " all rest on each other's notes. They may be one argument under " +
                        s.length +
                        " names rather than " +
                        s.length +
                        " courses of action.",
                    ));''', '''                    (function () {
                      /* v287: "complex adaptive" and "complex adaptive system" are one name */
                      var nm = s.map(n),
                        f = function (x) {
                          return " " + String(x).replace(/<[^>]*>/g, "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim() + " ";
                        },
                        kp = nm.filter(function (x, i) {
                          return !nm.some(function (y, j) {
                            return j !== i && f(y).length > f(x).length && f(y).indexOf(f(x)) >= 0;
                          });
                        });
                      kp.length >= 2 &&
                        o.push(
                          kp.join(", ") +
                            " all rest on each other's notes. They may be one argument under " +
                            kp.length +
                            " names rather than " +
                            kp.length +
                            " courses of action.",
                        );
                    })());''')

rep("""          (function () { try { gsmRetireSyn(Rt); } catch (e) {} })(),""", """          (function () { try { gsmRetireSyn(Rt); } catch (e) {} })(),
          (function () { try { gsmGoalQ(Rt); } catch (e) {} })(),""")
rep("""  function gsmRetireSyn(Rt) {""", """  /* v287: DOES THIS SERVE THE GOAL? keeps its own questions, on Taking Action (they were left inside
     IN YOUR ANSWERS, NOT ON THE MAP on Pattern Analysis) */
  function gsmGoalQ(Rt) {
    var ds = [].slice.call(Rt.querySelectorAll(".plab")).filter(function (x) {
      return /^DOES THIS SERVE THE GOAL\\?/.test(x.textContent.trim());
    })[0];
    if (!ds) return;
    var gl = [];
    [].slice.call(Rt.querySelectorAll('[onclick^="gsmAskG"]')).forEach(function (b) {
      var d = b.closest(".emo");
      d = d && d.parentElement;
      if (!d || gl.indexOf(d) >= 0) return;
      var pv = d.previousElementSibling;
      while (pv && "P" !== pv.tagName && pv.querySelector && pv.querySelector('[onclick^="gsmAskG"]')) pv = pv.previousElementSibling;
      pv && "P" === pv.tagName && /no word with your goal/.test(pv.textContent) && gl.indexOf(pv) < 0 && gl.push(pv);
      gl.push(d);
    });
    [].slice.call(Rt.querySelectorAll(".csl")).forEach(function (x) {
      if (!/YOU SAID THESE DO NOT SERVE THE GOAL/.test(x.textContent)) return;
      var nx = x.nextElementSibling;
      gl.push(x);
      nx && nx.classList.contains("cq") && gl.push(nx);
    });
    if (!gl.length) return;
    var gw = document.createElement("div");
    gw.className = "mean";
    gl.forEach(function (x) {
      gw.appendChild(x);
    });
    var pa = [].slice.call(Rt.children).filter(function (x) {
      return x.classList.contains("part") && /COURSES OF ACTION/.test(x.textContent);
    })[0];
    if (pa && ds.parentNode === Rt && ds.compareDocumentPosition(pa) & Node.DOCUMENT_POSITION_FOLLOWING) {
      var at = pa.nextElementSibling;
      while (at && !at.classList.contains("part") && !(at.classList.contains("plab") && /MORE INFORMATION NEEDED/.test(at.textContent)))
        at = at.nextElementSibling;
      Rt.insertBefore(ds, at || null);
    }
    var sb = ds.nextElementSibling && ds.nextElementSibling.classList.contains("secb") ? ds.nextElementSibling : null;
    sb ? sb.appendChild(gw) : ds.parentNode.insertBefore(gw, ds.nextSibling);
  }
  function gsmRetireSyn(Rt) {""")
rep('t.textContent = "v286"', 't.textContent = "v287"')
open(p, 'w', encoding='utf-8').write(s); print('ok')
