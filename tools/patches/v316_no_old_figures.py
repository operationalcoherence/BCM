"""v316: the old figures never show on Pattern Analysis again (Gregory, 26 Nov 19:04, after the live test).
AROUND THE GOAL and HOW IT HANGS TOGETHER stay in the page, hidden, for any code that still looks for them,
whatever the workbook holds (before: shown when no line-map note had words, so place-only workbooks and workbooks
with only symbols got them). When no note has words yet, Pattern Analysis opens with NO GROUND YET instead,
saying how many symbols are waiting for words, with a button to Mapping Landscape.
Run from the repository root:  python3 tools/patches/v316_no_old_figures.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:80]); s = s.replace(old, new)
rep('t && (t.textContent = "v315");', 't && (t.textContent = "v316");')
rep('''  function gsmGoalQ(Rt) {''', r'''  /* v316: no old figures, ever; NO GROUND YET when no note has words */
  function gsmNoOldFigs(Rt) {
    Rt.querySelectorAll("summary, .plab").forEach(function (s) {
      var t = (s.textContent || "").trim().toUpperCase();
      if (t.indexOf("AROUND THE GOAL") !== 0 && t.indexOf("HOW IT HANGS TOGETHER") !== 0) return;
      if (s.closest(".gsm-oldfig")) return;
      var head = s.tagName === "SUMMARY" ? s.closest("details") : s;
      if (!head || head === Rt || !head.parentNode) return;
      /* the heading and what follows it, up to the next section, go into one hidden box */
      var wrap = document.createElement("div");
      /* "part" makes it a section boundary, so the fold-maker never pulls it into the section before */
      wrap.className = "part gsm-oldfig";
      wrap.style.display = "none";
      wrap.setAttribute("aria-hidden", "true");
      head.parentNode.insertBefore(wrap, head);
      var n = head;
      do {
        var nx = n.nextElementSibling;
        wrap.appendChild(n);
        n = nx;
      } while (n && !n.matches(".plab, .part"));
    });
    var old = Rt.querySelector(".gsm-noground");
    old && old.remove();
    var d = window.gsmData ? window.gsmData() : null;
    if (!d) return;
    var all = (d.m || []).concat((d.p && d.p.m) || []),
      worded = all.filter(function (n) { return String(n[3] || "").trim(); }).length;
    if (worded) return;
    var bare = all.length,
      el = document.createElement("div");
    el.className = "gsm-noground";
    el.style.cssText = "border:1.5px solid #222;padding:12px 14px;margin:6px 0 14px;font-size:15px;line-height:1.5;background:#fff";
    el.innerHTML =
      '<div style="font-weight:700;letter-spacing:.14em;font-size:12px;margin:0 0 6px">NO GROUND YET</div>' +
      "<div>Pattern Analysis reads the ground your notes make, and no note has words yet." +
      (bare
        ? " " + bare + (bare === 1 ? " symbol is" : " symbols are") + " placed on the map without words. Write what each one is, and the ground builds from them."
        : " Place a symbol on Mapping Landscape and write what it is, and the ground builds from it.") +
      " Until then, what follows reads your answers only.</div>" +
      '<button type="button" class="btn" style="width:auto;margin-top:10px">Go to Mapping Landscape</button>';
    el.querySelector("button").addEventListener("click", function () {
      try { window.gsmTab(1); window.scrollTo(0, 0); } catch (e) {}
    });
    Rt.insertBefore(el, Rt.firstChild);
  }
  function gsmGoalQ(Rt) {''')
rep('''          (function () { try { gsmGoalQ(Rt); } catch (e) {} })(),''',
'''          (function () { try { gsmGoalQ(Rt); } catch (e) {} })(),
          (function () { try { gsmNoOldFigs(Rt); } catch (e) {} })(),''')
open(P, 'w', encoding='utf-8').write(s)
print('ok')
