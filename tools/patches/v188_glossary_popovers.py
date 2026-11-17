"""v188 (G1): the first use of each major term in every Patterns section and Taking Action card is dotted;
hover or tap shows what it means. Definitions reuse wording already on screen (WORDS USED HERE, the map legend,
the cards, the Vigneaux passage)."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("#gsm .copy a{color:#555}", "#gsm .copy a{color:#555}#gsm .gsg{border-bottom:1px dotted #8a8a8a;cursor:help}#gsm .gsg:hover,#gsm .gsg.on{border-bottom-color:#222}.glpop{position:fixed;z-index:2147483600;max-width:300px;background:#fff;border:1px solid #222;padding:8px 10px;font:13px/1.45 'Questrial',Helvetica,Arial,sans-serif;color:#222;box-shadow:0 2px 10px rgba(0,0,0,.15);display:none}.glpop b{display:block;font-size:11px;letter-spacing:.12em;margin-bottom:3px}")

rep("""  function gsmSame(t) {""", """  var GSMGL = [
    [/\\bthreads?\\b/i, "THREAD", "A word or phrase that runs through and relates several answers or notes. A dashed ring on a dot means it is not associated with other answers or notes by a thread."],
    [/\\bpatterns?\\b/i, "PATTERN", "A unique to you entanglement of answers and notes formed by words and symbols related by BCM. It suggests; you decide."],
    [/\\bvoices?\\b/i, "EMOTION, SOURCE, VOICE", "How a note feels, how you know it, and whose view it carries."],
    [/\\blinks?\\b/i, "LINK", "A connection you draw from a note to an answer, the goal, or another note."],
    [/\\bbare rock(?: face)?\\b/i, "BARE ROCK FACE", "Two distant emotions meet with no ridge of indifference between them, so getting across is a climb. A big move takes energy either way; most moves go through indifference."],
    [/\\bridges?\\b/i, "RIDGE", "Indifference: a ridge, where most moves between emotions cross."],
    [/\\b(?:high|higher|highest) ground\\b/i, "HIGH GROUND", "On the map, emotion sets the height of the ground. Acceptance: the highest ground. Indifference: a ridge. Distrust: low ground. Aggression: lower ground. Defiance: the lowest ground."],
    [/\\b(?:low|lower|lowest) ground\\b/i, "LOW GROUND", "On the map, emotion sets the height of the ground. Acceptance: the highest ground. Indifference: a ridge. Distrust: low ground. Aggression: lower ground. Defiance: the lowest ground."],
    [/\\bstrateg(?:y|ies)\\b/i, "STRATEGY", "A strategy is held loosely and revised as people respond."],
    [/\\bprograms?\\b/i, "PROGRAM", "A program runs to completion."],
    [/\\bemotions first\\b/i, "EMOTIONS FIRST", "Emotions first suits acceptance and indifference: connect people to acceptance, or something close to it, then tie that acceptance to what needs doing (Vigneaux, 2026)."],
    [/\\bbehaviors first\\b/i, "BEHAVIORS FIRST", "Behaviors first suits aggression, distrust and defiance: introduce the behavior itself, without its label, in a form that fits the emotions already there, and let a small shift in emotion follow over time (Vigneaux, 2026)."],
  ];
  var GSMGLSKIP = "a,button,textarea,input,select,option,label,summary,svg,script,style,h1,h2,h3,h4,.gsg,.glance,.csl,.plab,.rl,.wh,.cqm,.mode,.stage,.grel,.grleg,.legbox,.bar,.gtrb,.tip,.part,.lnk,.morebtn,[data-ref],[data-hid]";
  function gsmGloss() {
    var pat = document.getElementById("gsm-pat");
    if (!pat) return;
    pat.querySelectorAll(".secb:not([data-gl]),.coa:not([data-gl]),.gterr:not([data-gl])").forEach(function (box) {
      if (box.parentNode && box.parentNode.closest && box.parentNode.closest(".coa:not([data-gl]),.secb:not([data-gl]),.gterr:not([data-gl])")) return;
      box.setAttribute("data-gl", "1");
      var used = {},
        tw = document.createTreeWalker(box, NodeFilter.SHOW_TEXT, null),
        list = [],
        n;
      while ((n = tw.nextNode())) n.nodeValue.trim() && !(n.parentNode.closest && n.parentNode.closest(GSMGLSKIP)) && list.push(n);
      list.forEach(function (node) {
        for (var guard = 0; guard < 12 && node; guard++) {
          var best = null;
          GSMGL.forEach(function (g, gi) {
            if (used[g[1]]) return;
            var m = g[0].exec(node.nodeValue);
            m && (!best || m.index < best.i) && (best = { i: m.index, l: m[0].length, g: g });
          });
          if (!best) break;
          var mid = node.splitText(best.i),
            rest = mid.splitText(best.l),
            sp = document.createElement("span");
          sp.className = "gsg";
          sp.setAttribute("tabindex", "0");
          sp.setAttribute("data-gl", best.g[1]);
          mid.parentNode.insertBefore(sp, mid);
          sp.appendChild(mid);
          used[best.g[1]] = 1;
          node = rest;
        }
      });
    });
  }
  (function () {
    var pop = null,
      pin = null,
      tm = 0;
    function show(el) {
      var g = null;
      GSMGL.forEach(function (x) {
        x[1] === el.getAttribute("data-gl") && (g = x);
      });
      if (!g) return;
      pop || ((pop = document.createElement("div")), (pop.className = "glpop"), pop.setAttribute("role", "tooltip"), document.body.appendChild(pop));
      pop.innerHTML = "<b>" + g[1] + "</b>" + g[2];
      pop.style.display = "block";
      var r = el.getBoundingClientRect(),
        w = pop.offsetWidth,
        h = pop.offsetHeight,
        x = Math.max(6, Math.min(window.innerWidth - w - 6, r.left)),
        y = r.bottom + 6 + h > window.innerHeight ? r.top - h - 6 : r.bottom + 6;
      pop.style.left = x + "px";
      pop.style.top = Math.max(6, y) + "px";
      document.querySelectorAll("#gsm .gsg.on").forEach(function (o) {
        o.classList.remove("on");
      });
      el.classList.add("on");
    }
    function hide() {
      pop && (pop.style.display = "none");
      pin = null;
      document.querySelectorAll("#gsm .gsg.on").forEach(function (o) {
        o.classList.remove("on");
      });
    }
    document.addEventListener("mouseover", function (e) {
      var el = e.target && e.target.closest && e.target.closest("#gsm .gsg");
      el && !pin && show(el);
    });
    document.addEventListener("mouseout", function (e) {
      var el = e.target && e.target.closest && e.target.closest("#gsm .gsg");
      el && !pin && hide();
    });
    document.addEventListener("click", function (e) {
      var el = e.target && e.target.closest && e.target.closest("#gsm .gsg");
      if (el) return pin === el ? hide() : (show(el), (pin = el));
      pin && !(pop && pop.contains(e.target)) && hide();
    });
    document.addEventListener("keydown", function (e) {
      if ("Escape" === e.key) return hide();
      var el = document.activeElement;
      ("Enter" === e.key || " " === e.key) && el && el.classList && el.classList.contains("gsg") && (e.preventDefault(), show(el), (pin = el));
    });
    window.addEventListener("scroll", function () {
      pin || hide();
    }, true);
    function arm() {
      new MutationObserver(function () {
        clearTimeout(tm);
        tm = setTimeout(gsmGloss, 250);
      }).observe(document.body, { childList: !0, subtree: !0 });
      gsmGloss();
    }
    document.body ? arm() : document.addEventListener("DOMContentLoaded", arm);
  })();
  function gsmSame(t) {""")
rep('t.textContent = "v187"', 't.textContent = "v188"')
open(P, "w").write(s)
