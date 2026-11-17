"""v182: U7 tap-to-inspect on touch screens; U8 progressive disclosure (long lists fold into View details);
N3 each WHAT STANDS OUT finding says what it means."""
import sys, json
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

MEAN = {
 "OPPOSITION NOT YET ENGAGED": "Opposition nothing answers keeps working against the goal while you plan around it.",
 "FOR AND AGAINST ON THE MAP": "The same thing is a reason for and a reason against. Whoever settles what it means will tip the work, so settle it with the people involved, not for them.",
 "FOR AND AGAINST": "The same thing is a reason for and a reason against. Whoever settles what it means will tip the work.",
 "CONDITION NOT IN Q.5–Q.7": "A condition that nothing is designed to meet is a test the plan fails by default.",
 "RUNS TOGETHER": "These words travel together as one idea. Treat them as one, or say how they differ.",
 "SUPPORT NOT YET REINFORCED": "Support left alone fades. It is the cheapest thing to keep and the costliest to rebuild.",
 "REDESIGN THE RESISTANCE": "You already plan to redesign what resists you, which turns opposition into material to work with rather than a wall.",
 "CROSSES THE GROUND LINE": "It helps in one place and hinders in another, so where you act on it decides which.",
 "ROOTED IN OPPOSITION": "What you would do grows out of the opposition itself, so it will be judged first by the people who resist.",
 "BUILD ON WHAT IS HAPPENING": "Something is already moving; joining it costs less than starting anew.",
}

rep("""  function P() {""", """  var GSMMEAN = %s;
  function gsmPD(sec) {
    if (!sec || sec.getAttribute("data-pd")) return;
    sec.setAttribute("data-pd", "1");
    sec.querySelectorAll(".rule").forEach(function (r) {
      var l = r.querySelector(".rl"),
        m = l && GSMMEAN[l.textContent.trim()];
      if (m && !r.querySelector(".rmean")) {
        var d = document.createElement("div");
        d.className = "rmean";
        d.textContent = m;
        r.appendChild(d);
      }
    });
    function fold(list, kids, keep, wrapTag) {
      if (kids.length <= keep + 1) return;
      var dt = document.createElement("details");
      dt.className = "more pdx";
      var sm = document.createElement("summary");
      sm.textContent = "View details (" + (kids.length - keep) + " more)";
      dt.appendChild(sm);
      var box = document.createElement(wrapTag);
      wrapTag === "ul" && (box.className = "metal");
      kids.slice(keep).forEach(function (k) {
        box.appendChild(k);
      });
      dt.appendChild(box);
      list.parentNode.insertBefore(dt, list.nextSibling);
    }
    sec.querySelectorAll("ul.metal").forEach(function (u) {
      if (u.closest(".pdx")) return;
      fold(u, [].slice.call(u.children), 3, "ul");
    });
    sec.querySelectorAll(".mean").forEach(function (m) {
      if (m.closest(".pdx")) return;
      var ps = [].slice.call(m.children).filter(function (c) {
        return "P" === c.tagName;
      });
      ps.length > 4 && fold(ps[2], ps, 3, "div");
    });
  }
  function P() {""" % json.dumps(MEAN, ensure_ascii=False))
rep("""                  (t.classList.add("pfold"),""", """                  (gsmPD(e),
                  t.classList.add("pfold"),""")
rep("#gsm .copy a{color:#555}", "#gsm .copy a{color:#555}#gsm .rmean{margin-top:4px;color:#444;font-size:14px;font-style:italic}#gsm details.pdx summary{margin:6px 0 4px}")

# U7: on touch, the first tap on a note or question reference shows its details; a second tap follows it
rep("""  var dt = document.getElementById("gsm-sb"),
    ht = null;""", """  (function () {
    var lastPT = "mouse",
      shown = null;
    document.addEventListener(
      "pointerdown",
      function (t) {
        lastPT = t.pointerType || "mouse";
      },
      !0,
    );
    document.addEventListener(
      "click",
      function (t) {
        if ("mouse" === lastPT) return;
        var e = at(t);
        if (e && e[1]) {
          var el = t.target.closest ? t.target.closest("a,button,[data-ref],.ref") || t.target : t.target;
          if (shown !== el) {
            (t.preventDefault(), t.stopPropagation(), (shown = el), Z(e[1], t.clientX, t.clientY));
            return;
          }
          shown = null;
          return;
        }
        shown && ((shown = null), Z(null));
      },
      !0,
    );
  })();
  var dt = document.getElementById("gsm-sb"),
    ht = null;""")
rep('t && (t.textContent = "v181");', 't && (t.textContent = "v182");')
open(P, "w").write(s); print("v182 ok")
