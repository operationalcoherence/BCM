# v269: Pattern Synthesis retired (his decision 11-25, claude/pattern_synthesis_retired_2026-11-25.md).
# Ackoff: synthesis explains a thing by its role in a larger containing system. Nothing the engine reads without
# reading meaning is outside the situation, so the engine cannot do synthesis. The page's sections were analysis.
#  - What was under 2 · LOOKING OUT now reads at the end of Pattern Analysis: THE LAY OF THE LAND (3D, WHAT THE GROUND
#    SAYS, the tour, the patterns row), CAUSE AND EFFECT, NOW AND LATER, SCALE, ONE JUDGEMENT TWICE,
#    IN YOUR ANSWERS, NOT ON THE MAP, OPEN QUESTIONS, WHAT IT RESTS ON, WHAT YOU LINKED.
#  - DOES THIS SERVE THE GOAL? moves to Taking Action, before MORE INFORMATION NEEDED.
#  - Dropped: HOW THIS MAP IS MADE, the graph blocks (WHAT CHANGED WHAT ...), ABOUT WHAT YOU COLLECTED (its text; the
#    hidden old figure In Parallel reads stays), WHAT IT MIGHT MEAN, WHAT TO PAY ATTENTION TO, "Put the two pictures together".
#  - No Pattern Synthesis tab; a saved tab 3 opens Analysis. Parts renumbered: 2 · THE TWO PICTURES TOGETHER, 3 · COURSES
#    OF ACTION (the PDF's part 2 heading now says In Parallel; its part 3 heading was already Taking Action).
#  - WHAT THE GROUND SAYS reads as a story; the numbered readings fold under it (his note 08:46).
import re
p = "gsm-readable.js"
s = open(p, encoding="utf-8").read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:90])
    s = s.replace(old, new)

# 1. the part header becomes a hidden marker; the post-pass sorts what follows it
rep("""'<div class="part">2 · LOOKING OUT<span>Synthesis: the puzzle, all together.</span></div>' + ye""",
    """'<div class="synmark" style="display:none"></div>' + ye""")
rep("""(function () { try { window.gsmPSPage && window.gsmPSPage(Rt, C); } catch (e) {} })(),""",
    """(function () { try { gsmRetireSyn(Rt); } catch (e) {} })(),""")
rep("""  function gsmTAPass(Rt, tries) {""", r"""  /* v269: Pattern Synthesis retired. What was under LOOKING OUT stays where it is, now the end of Pattern Analysis;
     dropped sections go; DOES THIS SERVE THE GOAL? moves to Taking Action. */
  function gsmRetireSyn(Rt) {
    var mk = Rt.querySelector(".synmark");
    if (!mk) return;
    var kids = [],
      e = mk.nextElementSibling;
    while (e && !e.classList.contains("part")) {
      kids.push(e);
      e = e.nextElementSibling;
    }
    var lab = function (x) {
        var sp = x.querySelector("span");
        return (sp ? sp.textContent : x.textContent).trim();
      },
      DROP = { "WHAT IT MIGHT MEAN": 1, "WHAT TO PAY ATTENTION TO": 1 },
      move = [];
    kids.forEach(function (k) {
      if (k.classList.contains("psy-sec")) return void k.remove();
      if (!k.classList.contains("plab")) return;
      var t = lab(k),
        nx = k.nextElementSibling,
        sb = nx && nx.classList.contains("secb") ? nx : null;
      if ("ABOUT WHAT YOU COLLECTED" === t) {
        /* its text goes; its fold now heads the ground (THE LAY OF THE LAND) and the hidden old figure it holds */
        var sp0 = k.querySelector("span");
        sp0 ? (sp0.textContent = "THE LAY OF THE LAND") : (k.textContent = "THE LAY OF THE LAND");
        for (var c = k.nextElementSibling; c && !c.classList.contains("plab") && !c.classList.contains("part"); ) {
          var c2 = c.nextElementSibling;
          /^(meta|msub|metal)$/.test(String(c.getAttribute("class") || "")) && c.remove();
          c = c2;
        }
        sb && sb.classList.remove("closed");
      } else if (DROP[t]) {
        k.remove();
        sb && sb.remove();
      } else if ("DOES THIS SERVE THE GOAL?" === t) {
        move.push(k);
        sb && move.push(sb);
      }
    });
    mk.remove();
    if (!move.length) return;
    var pa = [].slice.call(Rt.children).filter(function (x) {
      return x.classList.contains("part") && /COURSES OF ACTION/.test(x.textContent);
    })[0];
    if (!pa) return;
    var at = pa.nextElementSibling;
    while (at && !at.classList.contains("part") && !(at.classList.contains("plab") && /MORE INFORMATION NEEDED/.test(at.textContent)))
      at = at.nextElementSibling;
    move.forEach(function (m) {
      Rt.insertBefore(m, at || null);
    });
  }
  function gsmTAPass(Rt, tries) {""")

# 2. no Synthesis tab
rep("""<button type="button" data-v="3">Pattern Synthesis</button>""", "")
rep("""      function O(i) {
""", """      function O(i) {
        3 === i && (i = 2);
""")
rep("""Analysis + Synthesis together""", """Analysis + the ground together""")

# 3. parts renumbered, and the PDF heading for part 2
rep('"3 · THE TWO PICTURES TOGETHER<span>What Analysis and Synthesis say when you read them side by side.</span>"',
    '"2 · THE TWO PICTURES TOGETHER<span>What your words and your ground say when you read them side by side.</span>"')
rep("""'<div class="part">4 · COURSES OF ACTION<span>""", """'<div class="part">3 · COURSES OF ACTION<span>""")
s, k = re.subn(r'z\("Pattern Synthesis"\),\s*P\("How the inputs make sense together\.", 10, "normal", 10, 100\),', 'z("In Parallel"),', s)
assert k == 1

# 4. HOW THIS MAP IS MADE: with no LOOKING OUT part it stays hidden
rep("""        part.parentNode.insertBefore(how, part.nextSibling);
      }
    })();""", """        part.parentNode.insertBefore(how, part.nextSibling);
      } else how.style.display = "none";
    })();""")

# 4b. the ground's own heading is now the fold's (above), so the template's copy hides on the main map
rep("""    host.className += " gterr";
    host.innerHTML = TPL;
""", """    host.className += " gterr";
    host.innerHTML = TPL;
    if (!(data && (data.card || data.an || data.par))) {
      var pl0 = host.querySelector(".plab");
      pl0 && /LAY OF THE LAND/.test(pl0.textContent) && (pl0.style.display = "none");
    }
""")

# 5. what the page says about itself
rep("""<li><b>Pattern Analysis.</b> Looking in: what patterns your answers and notes hold when analyzed together.</li><li><b>Pattern Synthesis.</b> Looking out: how questions and notes hang together, what their basis is, what intricacies are formed and the insights they yield, and what to pay attention to.</li>""",
    """<li><b>Pattern Analysis.</b> Looking in: what patterns your answers and notes hold when analyzed together, and the ground they make.</li>""")
rep("""On the line map, Pattern Synthesis shows it as ground.""", """On the line map, Pattern Analysis shows it as ground.""")
rep("""part of the larger pattern your answers and notes form, shown in Pattern Synthesis.""", """part of the larger pattern your answers and notes form, shown in Pattern Analysis.""")
rep("""Navigate to Pattern Analysis and Pattern Synthesis to see how your answers and notes interact.""", """Navigate to Pattern Analysis to see how your answers and notes interact.""")
rep("""Pattern Analysis and Pattern Synthesis open once you have answered all seven questions""", """Pattern Analysis opens once you have answered all seven questions""")
# the Synthesis instruction fold goes; its paragraph on working with others joins the Analysis one
m = re.search(r'<details class="fold pinst pisy"><summary>PATTERN SYNTHESIS: INSTRUCTION</summary><div class="mtext"><p>In Pattern Synthesis.*?</p>(<p>To work with others.*?</p>)</div></details>', s)
assert m
s = s.replace(m.group(0), "")
rep("""and their relationship and proximity to the goal.</p></div></details>""", """and their relationship and proximity to the goal.</p>""" + m.group(1) + """</div></details>""")
for a, b in [
    ("Then read Pattern Synthesis again.", "Then read Pattern Analysis again."),
    ("then read Pattern Synthesis again.", "then read Pattern Analysis again."),
    ("read Pattern Synthesis again.", "read Pattern Analysis again."),
    ("every note on the Synthesis ground that carries it", "every note on the ground that carries it"),
    ("Tap a word to follow it here and on the Pattern Synthesis 3D map.", "Tap a word to follow it here and on the 3D map in Pattern Analysis, under THE LAY OF THE LAND."),
    ("joined by hoses to their notes on the Pattern Synthesis ground", "joined by lines to their notes on the ground"),
    ('t1.textContent = "PATTERN SYNTHESIS";', 't1.textContent = "THE GROUND";'),
    ('"See it on the Pattern Synthesis 3D map"', '"See it on the 3D map in Pattern Analysis"'),
    ("its lines also go onto the Pattern Synthesis 3D map.", "its lines also go onto the 3D map in Pattern Analysis."),
    ("The sentences are under CAUSE AND EFFECT on Pattern Synthesis.", "The sentences are under CAUSE AND EFFECT on Pattern Analysis."),
    ("NOT ON THE MAP on Pattern Synthesis.", "NOT ON THE MAP on Pattern Analysis."),
    ("The order of the crossings on the ground of Pattern Synthesis:", "The order of the crossings on the ground (THE LAY OF THE LAND, Pattern Analysis):"),
    ("The numbers are what the ground says, read on Pattern Synthesis (Synthesis).", "The numbers are what the ground says, read under THE LAY OF THE LAND on Pattern Analysis."),
    ("What you change here is saved and described in Pattern Synthesis, under WHAT YOU LINKED, and in Mapping Landscape.", "What you change here is saved and described in Pattern Analysis, under WHAT YOU LINKED, and in Mapping Landscape."),
    (' Pattern Synthesis reads this ground in full."', ' THE LAY OF THE LAND, below, reads this ground in full."'),
]:
    c = s.count(a)
    assert c >= 1, a
    s = s.replace(a, b)

rep("""    function fillReadings() {
      var el = $("readings");
      el.innerHTML = "";
""", """    function fillReadings() {
      var el = $("readings");
      el.innerHTML = "";
      host._read = READ;
""")
# 6. WHAT THE GROUND SAYS as a story (his note 08:46: "worth keeping, as a story, not a list").
#    Written from the same readings, act by act, with no note numbers; the numbered readings fold under it,
#    because the numbers on the 3D map point to them. Main map only (not Analysis's question map, cards, or In Parallel).
rep("""    function fillReadings() {
      var el = $("readings");
      el.innerHTML = "";
      host._read = READ;
""", """    function groundStory(RD) {
      var qs = function (t) {
          var m = String(t || "").match(/“[^”]+”/);
          return m ? m[0] : "";
        },
        lst = function (a) {
          return a.length < 2 ? a[0] || "" : a.slice(0, -1).join(", ") + (a.length > 2 ? ", and " : " and ") + a[a.length - 1];
        },
        clean = function (x) {
          x = String(x || "")
            .replace(/\\s*\\((?:[NP]\\d+(?:,\\s*(?:and\\s+)?|\\s+and\\s+)?)+(?:,?\\s*and \\d+ more)?\\)/g, "")
            .replace(/\\b[NP]\\d+ \\(([a-z]+)\\)/g, "$1")
            .replace(/\\s+(?:around|at|near)\\s+[NP]\\d+(?:(?:,\\s*(?:and\\s+)?|\\s+and\\s+)[NP]\\d+)*(?:,?\\s*and \\d+ more)?/g, "");
          return /\\b[NP]\\d+\\b/.test(x) ? "" : x;
        },
        emo = function (x) {
          var m = String(x || "").match(/(?:hollow|ground|ridge) of ((?:aggression|acceptance|distrust|indifference|defiance)(?:(?:, and |, | and )(?:aggression|acceptance|distrust|indifference|defiance))*)/);
          return m ? m[1] : "";
        },
        by = { 0: [], 1: [], 2: [], 3: [] },
        out = [];
      RD.forEach(function (r) {
        (by[r.grp] || (by[r.grp] = [])).push(r);
      });
      if (PLACE) {
        Object.keys(by).forEach(function (g) {
          var t = by[g]
            .map(function (r) {
              return clean(r.short);
            })
            .filter(Boolean)
            .join(" ");
          t && out.push(t);
        });
        return out;
      }
      /* the high ground */
      var p = [],
        foot = by[0].filter(function (r) {
          return /has footing$/.test(r.title);
        }).map(function (r) {
          return qs(r.title);
        }).filter(Boolean),
        hill = by[0].filter(function (r) {
          return /^High ground/.test(r.title);
        })[0],
        fall = by[0].filter(function (r) {
          return /easiest to fall from/.test(r.title);
        })[0];
      if (hill) {
        var he = emo(hill.short) || "acceptance",
          from = (hill.short.match(/\\(([a-z][^)]*)\\)/g) || []).map(function (z) {
            return z.slice(1, -1);
          });
        p.push(
          "The ground holds up where " + he + " gathers" +
            (/off to the side/.test(hill.title)
              ? ", but off to the side of the line to the goal, so the way there cannot lean on it."
              : " near the line to the goal, so the way there can lean on it.") +
            (from.length ? " It is built mostly from your notes on " + lst(from) + "." : ""),
        );
      }
      foot.length && p.push(lst(foot) + (foot.length > 1 ? " stand" : " stands") + " on firm ground.");
      if (fall) {
        var fm = fall.short.match(/\\(([a-z]+)\\) sits closest to [NP]\\d+ \\(([a-z]+)\\)/);
        fm && p.push((p.length ? "Its edge is where " : "The high ground's edge is where ") + fm[1] + " comes closest to " + fm[2] + ": there the high ground drops away fastest.");
      }
      by[0].forEach(function (r) {
        if (r === hill || r === fall || /has footing$/.test(r.title)) return;
        var c = clean(r.short);
        c && p.push(c);
      });
      p.length && out.push(p.join(" "));
      /* the low ground */
      p = [];
      var stuck = by[1].filter(function (r) {
          return /get stuck$/.test(r.title);
        }),
        down = by[1].filter(function (r) {
          return /holds the ground down$/.test(r.title);
        }).map(function (r) {
          return qs(r.title);
        }).filter(Boolean),
        back = by[1].filter(function (r) {
          return /longest way back/.test(r.title);
        })[0];
      if (stuck.length) {
        var pc = stuck.map(function (r) {
            var m = r.short.match(/^(\\d+)%/);
            return m ? +m[1] : 0;
          }),
          em = [];
        stuck.forEach(function (r) {
          emo(r.short).split(/, and |, | and /).forEach(function (e) {
            e && em.indexOf(e) < 0 && em.push(e);
          });
        });
        var big = Math.max.apply(null, pc);
        p.push(
          (out.length ? "Below it, " : "") +
            (stuck.length > 1
              ? (out.length ? "the" : "The") + " ground falls into " + ["", "one", "two", "three", "four", "five"][stuck.length] + " hollows of " + lst(em) + "; the largest draws in " + big + "% of the ground. These are the places where it is easiest to get stuck."
              : (out.length ? "" : "") + big + "% of the ground slopes into a hollow of " + lst(em) + ", the place where it is easiest to get stuck."),
        );
        p[0] = p[0].charAt(0).toUpperCase() + p[0].slice(1);
      }
      down.length && p.push(lst(down) + (down.length > 1 ? " hold" : " holds") + " the ground down: " + (down.length > 1 ? "their" : "its") + " notes sit in sunk ground.");
      if (back) {
        var bm = back.short.match(/is ([a-z]+), the deepest ground on the map\\. The way from there up to ([a-z]+)[^.]* climbs (\\d+%)/);
        bm && p.push(bm[1].charAt(0).toUpperCase() + bm[1].slice(1) + " is the deepest ground. The climb from it to " + bm[2] + " takes " + bm[3] + " of the map's height, the longest way back. Start elsewhere, and come back here once acceptance is moving on its own.");
      }
      by[1].forEach(function (r) {
        if (r === back || stuck.indexOf(r) >= 0 || /holds the ground down$/.test(r.title)) return;
        var c = clean(r.short);
        c && p.push(c);
      });
      p.length && out.push(p.join(" "));
      /* between them */
      p = [];
      var ridge = by[2].filter(function (r) {
          return /ridge between/.test(r.title);
        })[0],
        easy = by[2].filter(function (r) {
          return /easiest to get to/.test(r.title);
        })[0],
        rock = by[2].filter(function (r) {
          return /^Bare rock/.test(r.title);
        });
      ridge && p.push("Between them runs a narrow ridge of indifference, climbing from the low ground up into acceptance.");
      if (easy)
        p.push(
          /by way of the indifference/.test(easy.short)
            ? (ridge ? "It is" : "A ridge of indifference is") + " the least costly way up from the largest low ground: most moves go through indifference."
            : "The least costly way up from the largest low ground reaches acceptance without crossing indifference.",
        );
      if (rock.length) {
        var pr = [];
        rock.forEach(function (r) {
          var m = r.short.match(/Here ([a-z]+) \\([NP]\\d+\\) meets ([a-z]+)/);
          m && pr.indexOf(m[1] + " meets " + m[2]) < 0 && pr.push(m[1] + " meets " + m[2]);
        });
        pr.length && p.push("Where " + lst(pr) + " with no indifference between them, the ground turns to bare rock: the steepest crossing on the map, the one a big move pays for in energy either way.");
      }
      by[2].forEach(function (r) {
        if (r === ridge || r === easy || rock.indexOf(r) >= 0) return;
        var c = clean(r.short);
        c && p.push(c);
      });
      p.length && out.push(p.join(" "));
      /* what keeps it this way */
      p = [];
      var both = by[3].filter(function (r) {
        return /both kinds of ground$/.test(r.title);
      }).map(function (r) {
        return qs(r.title);
      }).filter(Boolean);
      both.length && p.push("What keeps it this way: " + lst(both) + (both.length > 1 ? " stand" : " stands") + " on both kinds of ground, raised in one place and sunk in another, so the same words carry the change and the resistance to it.");
      by[3].forEach(function (r) {
        if (/both kinds of ground$/.test(r.title)) return;
        var c = clean(r.short);
        c && p.push(c);
      });
      p.length && out.push(p.join(" "));
      return out;
    }
    function fillReadings() {
      var el = $("readings");
      el.innerHTML = "";
      host._read = READ;
      if (!(ANH || CARDH || PAR) && el.parentNode) {
        var sw = host.querySelector(".gstory");
        if (!sw) {
          sw = document.createElement("div");
          sw.className = "gstory";
          sw.style.cssText = "font-size:15px;line-height:1.6;margin:4px 0 10px";
          var fd = document.createElement("details");
          fd.className = "fold gstoryl";
          fd.style.margin = "4px 0 12px";
          fd.innerHTML = "<summary>THE READINGS, ONE BY ONE (THE NUMBERS ON THE MAP)</summary>";
          el.parentNode.insertBefore(sw, el);
          el.parentNode.insertBefore(fd, el);
          fd.appendChild(el);
        }
        var ps = [];
        try {
          ps = READ.length ? groundStory(READ) : [];
        } catch (e) {}
        sw.innerHTML = ps.map(function (t) {
          return "<p style=\\"margin:0 0 10px\\">" + String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</p>";
        }).join("");
        sw.style.display = ps.length ? "" : "none";
      }
""")
# 7. In Parallel's "See it on the 3D map" scrolls to the main ground even before its 3D has loaded (it now sits low on Analysis)
rep("""      PAR = !!data.par,
      AQ = 0;
""", """      PAR = !!data.par,
      AQ = 0;
    !ANH && !PAR && !CARDH && (window.gsmSynHost = host);
""")
rep("Each number on the ground is explained here first; hover or tap a number on the map to read it there.", "The numbered readings fold under the story; hover or tap a number on the map to read it there.")
rep('t.textContent = "v268"', 't.textContent = "v269"')
open(p, "w", encoding="utf-8").write(s)
print("ok")
