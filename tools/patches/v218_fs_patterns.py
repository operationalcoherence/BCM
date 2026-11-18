"""v218: the patterns row stays in full screen (his note, 11-18 15:13: "they shouldn't disappear in full screen").
Full screen on the Synthesis 3D carries the row into the map, at the top left, clear of the legend drawer and the Play button; closing
full screen puts it back above the map. It hides while the tour plays, so it does not crowd the captions.
Usage: python3 v218_fs_patterns.py tools/relief/relief.js --relief   and   python3 v218_fs_patterns.py gsm-readable.js"""
import sys
P = sys.argv[1]
RELIEF = "--relief" in sys.argv
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
if RELIEF:
    rep("""  bFs.onclick = () => { const on = !wrap.classList.contains('fs'); if (on) fillFsl(); moved = false; wrap.classList.toggle('fs', on);""",
        """  bFs.onclick = () => { const on = !wrap.classList.contains('fs'); if (on) fillFsl(); moved = false; wrap.classList.toggle('fs', on); if (D.onFs) D.onFs(on, wrap);""")
    rep("""if (typeof tbar !== 'undefined') tbar.style.left = pad + vw / 2 + 'px';""",
        """if (typeof tbar !== 'undefined') tbar.style.left = pad + vw / 2 + 'px'; const fl = wrap.querySelector('.fslay'); if (fl) { fl.style.left = pad + 12 + 'px'; fl.style.maxWidth = Math.max(220, vw * 0.62) + 'px'; }""")
    rep("""TOUR = { legs, start: performance.now(), total: t0, cur: -2, paused: null };""",
        """wrap.classList.add('touring'); TOUR = { legs, start: performance.now(), total: t0, cur: -2, paused: null };""")
    rep("""  function stopTour() { if (!TOUR) return; TOUR = null;""",
        """  function stopTour() { if (!TOUR) return; TOUR = null; wrap.classList.remove('touring');""")
    rep(""".grel .tourbar{position:absolute;""",
        """.grel .fslay{position:absolute;top:46px;z-index:4;margin:0!important;padding:8px 10px;background:rgba(255,255,255,.88);border:1px solid #ccc;display:flex;flex-wrap:wrap;gap:6px;align-items:center}.grel .fslay .lhelp{display:none}.grel.touring .fslay{display:none!important}.grel .tourbar{position:absolute;""")
else:
    rep("""          D.onHL = function (i) {""",
        """          /* v218: the patterns row goes into the map in full screen and back out after */
          D.onFs = function (on, w) {
            var lb = $("laybar");
            if (!lb || !lb.childNodes.length) return;
            if (on) {
              lb._home || (lb._home = { p: lb.parentNode, n: lb.nextSibling });
              lb.classList.add("fslay");
              w.appendChild(lb);
            } else if (lb._home) {
              lb.classList.remove("fslay");
              lb.style.left = lb.style.maxWidth = "";
              lb._home.p.insertBefore(lb, lb._home.n);
            }
          };
          D.onHL = function (i) {""")
    rep("""    function fillLay() {
      var lb = $("laybar");""",
        """    function fillLay() {
      var lb = $("laybar") || (host.querySelector(".grel .laybar") || null);""")
    s = s.replace('t.textContent = "v217"', 't.textContent = "v218"'); assert 't.textContent = "v218"' in s
open(P, "w").write(s)
