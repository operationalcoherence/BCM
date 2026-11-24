"""v251: Pattern Analysis read as a reader (his go-ahead 11-24 09:03 on the before/after image).

- AT A GLANCE opens with WHAT THE SYSTEM IS DOING: three sentences from the system story (what the
  system protects, how the protection moves as the change advances, where it gives way). The BIGGEST
  GAP count leaves AT A GLANCE; the same gap is already on Taking Action (NOTHING YOU WOULD DO).
  Only when the workbook holds several stories; otherwise AT A GLANCE is unchanged.
- WHAT HOLDS THE SITUATION IN PLACE: when acceptance sits inside what stands against the goal, the
  reading rests on it (the present arrangement still taken as the right one), with the low emotions
  growing on that footing. Note numbers go behind, small and gray.
- THE OPPORTUNITY: when what you would reinforce feeds support and support answers resistance in kind
  (aggression on the side that helps), it says so: support is fed where it already stands, and the work
  is to let it reach across the line.
- WHERE IT CAN CROSS: no definition first; no note numbers first; only notes about people (Q.1-Q.4)
  count as the middle, not what you would do. Says who the middle is when the notes say it (waiting to
  see what happens, expecting it to fail, out of their hands, not invested), and points to a plan to ask
  for participation when one exists. WHERE THIS LEAVES THE WORK uses the same notes.
- WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED is no longer built.
"""
import sys
F = "gsm-readable.js"
s = open(F).read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit("expected %d, found %d: %r" % (n, c, old[:90]))
    s = s.replace(old, new)


# numbers behind, small and gray
rep('''  function gsmStRef(n) {
    return '<a class="ref" data-ref="' + Gt(n.ref) + '">' + Gt(n.lab) + "</a>";
  }''', '''  function gsmStRef(n) {
    return '<a class="ref" data-ref="' + Gt(n.ref) + '">' + Gt(n.lab) + "</a>";
  }
  function gsmStNB(list) {
    var seen = {},
      u = (list || []).filter(function (n) {
        return n && n.ref && !seen[n.ref] && (seen[n.ref] = 1);
      });
    return u.length ? ' <span class="srnb">' + u.slice(0, 8).map(gsmStRef).join(", ") + (u.length > 8 ? ", and " + (u.length - 8) + " more" : "") + "</span>" : "";
  }''')
rep('''#gsm .intframe{font-size:15px;line-height:1.5;color:#222;margin:4px 0 10px}";''',
    '''#gsm .intframe{font-size:15px;line-height:1.5;color:#222;margin:4px 0 10px}#gsm .srnb{color:#999;font-size:11.5px}#gsm .srnb a.ref{color:#999}#gsm .glance .gl.glsys{cursor:default}";''')

# WHERE IT CAN CROSS: no definition first
rep('''      "WHERE IT CAN CROSS": "Crossing is a move from one emotion\\u2019s ground to another\\u2019s, such as from distrust toward acceptance. Distant emotions take the most energy to cross between, in either direction.",
    };
    function card(''', '''    };
    function card(''')

# WHAT HOLDS: rests on acceptance when acceptance is inside it
rep('''      card(
        "WHAT HOLDS THE SITUATION IN PLACE",
        "What stands against the goal is one connected body" +''', '''      /* v251: acceptance of the present inside what stands against the goal is what the rest grows on */
      var accH = comp.filter(function (n) {
          return 1 === n.em;
        }),
        lowO = o.filter(function (e) {
          return [0, 2, 4].indexOf(e) >= 0;
        }),
        lowN = lowO.map(function (e) {
          return E[e];
        });
      card(
        "WHAT HOLDS THE SITUATION IN PLACE",
        accH.length && lowO.length
          ? "What stands against the goal " +
              (sysTh.length ? "gathers around " + gsmStQL(sysTh) + " and " : "") +
              "rests less on " +
              E[lowO[0]] +
              " than on acceptance: the present arrangement is still taken as the right one, so any alternative has to argue against common sense. " +
              gsmMeanList(lowN).replace(/^./, function (c) {
                return c.toUpperCase();
              }) +
              (1 === lowN.length ? " grows" : " grow") +
              " on that footing" +
              (tied.length ? ", and the parts hold each other up" : "") +
              ". That is why it holds." +
              gsmStNB(accH.concat(tied))
          : "What stands against the goal is one connected body" +''')

# THE OPPORTUNITY: support fed where it already stands, answering resistance in kind
rep('''      card(
        "THE OPPORTUNITY",
        (ex.length >= nw.length ? "Most" : "Part") +''', '''      var fedN = ex.filter(function (n) {
          return 7 === n.k;
        }),
        hAgg = notes.filter(function (n) {
          return n.side > 0 && 0 === n.em;
        });
      card(
        "THE OPPORTUNITY",
        fedN.length && hAgg.length
          ? "Support for the goal already exists" +
              (exTh.length ? ", around " + gsmStQL(exTh) : "") +
              ", and what you would reinforce already feeds it. But it is fed where it already stands, and here support tends to answer resistance in kind: each side hardens the other. The work is to let support reach across the line, not just grow stronger on its own side." +
              gsmStNB(fedN.concat(hAgg))
          : (ex.length >= nw.length ? "Most" : "Part") +''')

# WHERE IT CAN CROSS: who the middle is; the people, not the plans
rep('''    SS.D.ind = ind;
    if (ind.length && sysNames.length >= 3) {
      SS.cross = ind.slice(0, 4).map(gsmStRef);
      card(
        "WHERE IT CAN CROSS",
        gsmStList(ind.map(gsmStRef), 5).replace(/>place note/, ">Place note") +
          (1 === ind.length ? " carries" : " carry") +
          " indifference: the ridge between the low ground that holds and the high ground of acceptance. People there are not yet for or against, so they can be moved either way, and most crossings go through ground like this.",''', '''    SS.D.ind = ind;
    /* v251: the middle is the people in it (Q.1-Q.4), not what you would do about them */
    var indP = ind.filter(function (n) {
        return n.k >= 1 && n.k <= 4;
      }),
      MID = [
        [/\\b(see what happens|wait\\w* (and|to) see)\\b/i, "waiting to see what happens"],
        [/\\b(likely to fail|bound to fail|will fail|going to fail|just another)\\b/i, "expecting it to fail"],
        [/\\b(out of (their|our|my|his|her) hands|no say|no voice|no influence|powerless|nothing (they|we|i) can do)\\b/i, "feeling it is out of their hands"],
        [/\\b(not invested|do(es)?n'?t care|do(es)? not care|disinterested|uninterested)\\b/i, "not invested in it"],
        [/\\b(uncertain|unsure|undecided|don'?t know how they feel)\\b/i, "unsure how they feel"],
      ],
      midD = [],
      midN = [];
    MID.forEach(function (m) {
      var h = indP.filter(function (n) {
        return m[0].test(n.txt);
      });
      h.length && (midD.push(m[1]), (midN = midN.concat(h)));
    });
    var noSay = indP.some(function (n) {
        return MID[2][0].test(n.txt);
      }),
      partN = notes.filter(function (n) {
        return n.k >= 5 && /\\b(particip\\w*|co-?design\\w*|involv\\w*|have a say|give (them|people) a (say|voice))\\b/i.test(n.txt);
      });
    if (ind.length && sysNames.length >= 3) {
      SS.cross = (indP.length ? indP : ind).slice(0, 4).map(gsmStRef);
      card(
        "WHERE IT CAN CROSS",
        indP.length
          ? (indP.length >= 4 ? "A wide middle" : "A small middle") +
              " is neither for nor against the goal" +
              (midD.length >= 2 ? ": people " + gsmMeanList(midD) + "." : ".") +
              " It is the nearest crossing; most moves between emotions go through ground like this." +
              (noSay ? " What holds people there is less doubt about the goal than a sense of having no say in it." : "") +
              (partN.length
                ? noSay
                  ? " Asking for their participation, as you already plan, is the move that fits."
                  : " What you would do already asks for participation, which reaches it."
                : noSay
                  ? " Nothing you would do yet gives them a say."
                  : "") +
              gsmStNB(indP.concat(partN))
          : gsmStList(ind.map(gsmStRef), 5).replace(/>place note/, ">Place note") +
            (1 === ind.length ? " carries" : " carry") +
            " indifference: the ridge between the low ground that holds and the high ground of acceptance. People there are not yet for or against, so they can be moved either way, and most crossings go through ground like this.",''')
rep('''        ind
          .slice(0, 5)
          .map(function (n) {
            return "<div>" + gsmStQ(n) + "</div>";
          })
          .join(""),
      );
    }
    return R.length >= 1''', '''        (indP.length ? indP : ind)
          .slice(0, 6)
          .map(function (n) {
            return "<div>" + gsmStQ(n) + "</div>";
          })
          .join(""),
      );
    }
    return R.length >= 1''')

# WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED: no longer built
rep('''            PARA.length > 1 &&
              (we =
                '<div class="plab">WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED</div>''',
    '''            /* v251: retired; it described the method, not the situation */
            0 &&
              PARA.length > 1 &&
              (we =
                '<div class="plab">WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED</div>''')

# AT A GLANCE: the system story first, in place of the gap count
rep('''    var more = Y.low.length > 3 ? " These are the three largest; "''', '''    /* v251: AT A GLANCE opens with what the system is doing; the gap count is on Taking Action */
    try {
      var GI = {
          legit: "what the present arrangement gives it: a shared sense of what is right and of who belongs",
          ident: "its present identity: people remaining recognizable to themselves and to one another",
          order: "the present order of control: knowing who decides, what counts as good work, and who is safe",
        }[K],
        FS = CH.map(function (c) {
          return SHORT[c.key];
        }),
        FP = [];
      /* chapters at the start at the same time join; later ones follow in order */
      CH.forEach(function (c, i) {
        i && "start" === c.wh && "start" === CH[i - 1].wh ? (FP[FP.length - 1] += " and " + FS[i]) : FP.push(FS[i]);
      });
      var
        gist =
          "The system isn\\u2019t resisting the change itself. It is protecting " +
          GI +
          "." +
          (FP.length >= 2
            ? " As the change advances, the protection moves from " + (2 === FP.length ? FP.join(" to ") : FP.join(", to ")) + "."
            : FS.length >= 2
              ? " The protection takes several forms at once: " + gsmMeanList(FS) + "."
              : "") +
          " It gives way only where the change provides the same thing another way.",
        groot = mt.closest("#gsm"),
        gp = groot && groot.querySelector(".glance");
      if (gp && !gp.querySelector(".glsys")) {
        var grow = document.createElement("div");
        grow.className = "gl glsys";
        grow.innerHTML = '<span class="gk">WHAT THE SYSTEM IS DOING</span><span class="gt"></span>';
        grow.querySelector(".gt").textContent = gist;
        [].slice.call(gp.querySelectorAll(".gl")).forEach(function (g) {
          var k = g.querySelector(".gk");
          if (k && "BIGGEST GAP" === k.textContent.trim()) {
            var x = g.nextElementSibling;
            x && !x.classList.contains("gl") && x.parentNode.removeChild(x);
            g.parentNode.removeChild(g);
          }
        });
        var gh = gp.querySelector("h4");
        gh ? gh.after(grow) : gp.prepend(grow);
      }
    } catch (e) {}
    var more = Y.low.length > 3 ? " These are the three largest; "''')

rep('t && (t.textContent = "v250");', 't && (t.textContent = "v251");')
open(F, "w").write(s)
print("v251 applied")
