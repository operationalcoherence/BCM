"""v219: his two last notes (11-18 15:21).
1. "On both tours take (Vigneaux, 2026) out of the text everywhere": the tour openings (Pattern Synthesis) and the
   Pattern Analysis tour no longer cite the paper ("Height follows the order of the emotions", "the emotion of
   transition", "it is unlikely in the short or medium term"). As a guard, the tour also drops any "(Vigneaux, 2026)"
   or "in Vigneaux (2026)" a reading's caption picks up. The page text (WHAT THE GROUND SAYS, the legends) keeps its
   citations.
2. "Make the In Parallel image have a full screen option with supportive text": a Full screen button on THE TWO
   PICTURES, SIDE BY SIDE. Full screen shows the figure large, with a panel beside it (below it on a narrow screen):
   the title, HOW TO READ IT, the key, and the reading of the tapped word. Close full screen or Escape returns.
Usage: python3 v219_tour_cites_fig_fs.py tools/relief/relief.js --relief   and   python3 v219_tour_cites_fig_fs.py gsm-readable.js"""
import sys
P = sys.argv[1]
RELIEF = "--relief" in sys.argv
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
if RELIEF:
    rep("""cap.querySelector('.tx').textContent = r.cap || r.text || '';""",
        """cap.querySelector('.tx').textContent = String(r.cap || r.text || '').replace(/\\s*\\(\\s*(?:after\\s+)?Vigneaux,?\\s*2026\\s*\\)/g, '').replace(/\\s+in Vigneaux \\(2026\\)/g, '');""")
else:
    # 1: the tours' own text
    rep("""it is unlikely in the short or medium term (Vigneaux, 2026).";""", """it is unlikely in the short or medium term.";""")
    rep("""Height follows the order in Vigneaux (2026): acceptance is the high ground""", """Height follows the order of the emotions: acceptance is the high ground""")
    rep("""            " indifference, the emotion of transition (Vigneaux, 2026). No one here is for or against the goal yet.""",
        """            " indifference, the emotion of transition. No one here is for or against the goal yet.""")
    # 2: full screen for the figure
    rep("""    wrap.appendChild(ky);
    wrap.appendChild(rd);
    var st = document.createElement("style");""",
        """    var fb = document.createElement("button"),
      hp = document.createElement("div"),
      ft = document.createElement("div");
    fb.type = "button";
    fb.className = "agfsb";
    fb.textContent = "Full screen";
    ft.className = "agft";
    ft.textContent = "THE TWO PICTURES, SIDE BY SIDE";
    hp.className = "aghelp";
    hp.innerHTML =
      "<b>HOW TO READ IT</b><p>Each word on the left is something Pattern Analysis found in your answers and notes. Its lines run to every note on the ground that uses it, so you can see where that word stands: acceptance is the high ground, indifference the ridge, and distrust, aggression, and defiance the low ground. The dashed line across the map divides what helps (above) from what hinders (below); the goal is the black diamond.</p><p>A <b>solid black line</b> means the ground agrees with what Analysis found. A <b>dashed red line</b> means the ground tells a different story, so that word is worth a second look.</p><p>Tap a word to read what both pictures say about it; its lines also go onto the Pattern Synthesis 3D map.</p>";
    var svgEl = wrap.querySelector("svg"),
      fsOn = function (on) {
        wrap.classList.toggle("agfs", on);
        fb.textContent = on ? "Close full screen" : "Full screen";
        document.documentElement.style.overflow = on ? "hidden" : "";
      };
    fb.onclick = function () {
      fsOn(!wrap.classList.contains("agfs"));
    };
    document.addEventListener("keydown", function (e) {
      "Escape" === e.key && wrap.classList.contains("agfs") && fsOn(!1);
    });
    var side = document.createElement("div");
    side.className = "agside";
    wrap.insertBefore(fb, wrap.firstChild);
    side.appendChild(ft);
    side.appendChild(hp);
    side.appendChild(ky);
    side.appendChild(rd);
    var main = document.createElement("div");
    main.className = "agmain";
    svgEl.parentNode.insertBefore(main, svgEl);
    main.appendChild(svgEl);
    wrap.appendChild(side);
    var st = document.createElement("style");""")
    rep("""#gsm .agread .lnk{margin-left:4px}""",
        """#gsm .agread .lnk{margin-left:4px}#gsm .agfig{position:relative}#gsm .agfsb{display:block;margin:0 0 8px auto;background:#fff;border:1px solid #222;font:13px Questrial,Helvetica,Arial,sans-serif;padding:5px 11px;cursor:pointer}#gsm .agft,#gsm .aghelp{display:none}#gsm .agfig.agfs{position:fixed;inset:0;z-index:2147483000;background:#fff;margin:0;padding:52px 22px 20px;overflow:auto;display:flex;gap:26px;align-items:flex-start}#gsm .agfig.agfs .agsub{display:none}#gsm .agfig.agfs .agfsb{position:fixed;top:10px;right:14px;margin:0;font-size:14px;padding:6px 12px;z-index:2}#gsm .agfig.agfs .agmain{flex:1 1 auto;min-width:0}#gsm .agfig.agfs .agmain svg{width:100%;max-height:calc(100vh - 80px)}#gsm .agfig.agfs .agside{flex:0 0 360px}#gsm .agfig.agfs .agft{display:block;font-weight:700;font-size:13px;letter-spacing:.16em;margin:0 0 12px}#gsm .agfig.agfs .aghelp{display:block;font-size:14.5px;line-height:1.55;color:#222;margin:0 0 12px}#gsm .agfig.agfs .aghelp b{font-weight:700}#gsm .agfig.agfs .aghelp>b:first-child{display:block;font-size:11.5px;letter-spacing:.14em;margin-bottom:4px}#gsm .agfig.agfs .aghelp p{margin:0 0 8px}#gsm .agfig.agfs .agkey{flex-direction:column;gap:6px;margin:0 0 12px}@media(max-width:900px){#gsm .agfig.agfs{display:block}#gsm .agfig.agfs .agside{margin-top:14px}}""")
    s = s.replace('t.textContent = "v218"', 't.textContent = "v219"'); assert 't.textContent = "v219"' in s
open(P, "w").write(s)
