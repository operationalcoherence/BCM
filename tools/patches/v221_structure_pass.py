"""v221: the structure pass on Pattern Analysis (his 11-18 18:34 note, "go ahead" 18:48).
"Does this page explain why the observed system behaves the way it does?" A new section opens Pattern Analysis,
WHY IT BEHAVES THIS WAY, with up to five readings built by rules from anyone's workbook (no AI). Each reading
stays silent when the workbook doesn't meet its test, and each folds its notes under it.
1. THE SYSTEM THAT HOLDS: the hindering notes tied by shared words, named by their opening words; called
   self-supporting when its notes say they reinforce, feed, drive, or freeze one another. Its ground (the emotions
   most of it carries) explains why it holds.
2. THE KEY TENSION: what the goal asks for more of, against the hindering notes that fear it (fear, liability,
   escape, vilify, eradicate, deadly, …).
3. THE LOOP: a word written in two or more sentences that say it feeds itself (reinforce, accumulate, itself,
   feedback, …), read with now and later.
4. THE OPPORTUNITY: help that already exists (support and reinforce notes on acceptance or indifference) against what
   still has to be designed new.
5. WHERE IT CAN CROSS: the indifference notes, the ridge between the low ground that holds and the high ground.
All sentence wording is Claude's, for his redlines (claude/structure_pass_plan.md).
Usage: python3 v221_structure_pass.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

JS = r'''
  function gsmStName(n) {
    var t = String(n.txt || "")
        .replace(/\([^)]*\)/g, " ")
        .split(/[.,;:!?\n]/)[0]
        .replace(/\s+/g, " ")
        .trim(),
      w = t.split(" "),
      out = [],
      VERB = /^(that|which|who|whose|contributes?|presents?|promotes?|enables?|leads?|forces?|turns?|drives?|supports?|freezes?|haunts?|may|could|will|would|has|have|had|is|are|was|were|engage|engages|like|such|including|put|continues?|remains?|solves?|takes?|makes?)$/i,
      PREP = /^(to|within|over|as|where|when|in|by|for|from|on|at|into|among|across|through)$/i;
    while (w.length && /^(the|a|an|as|so|and)$/i.test(w[0])) w.shift();
    for (var i = 0; i < w.length && out.length < 6; i++) {
      if (VERB.test(w[i]) && out.length >= 1) break;
      if (PREP.test(w[i]) && out.length >= 2) break;
      out.push(w[i]);
    }
    while (out.length > 1 && /^(and|or|of|the|a|an|to|in|its|their|with)$/i.test(out[out.length - 1])) out.pop();
    var r = out.join(" ").replace(/[^\w)’'/-]+$/, "");
    return r && !/^[A-Z]{2,}/.test(r) && !/^[A-Z]\w*\s+[A-Z]/.test(r) ? r.charAt(0).toLowerCase() + r.slice(1) : r;
  }
  function gsmStRef(n) {
    return '<a class="ref" data-ref="' + Gt(n.ref) + '">' + Gt(n.lab) + "</a>";
  }
  function gsmStQ(n, txt, key) {
    var w = String(txt || n.txt).replace(/\s+/g, " ").trim().replace(/[.!?]+$/, "").split(" "),
      a = 0;
    if (w.length > 16 && key)
      for (var i = 0; i < w.length; i++)
        if (0 === w[i].toLowerCase().replace(/^\W+/, "").indexOf(key)) {
          a = Math.max(0, Math.min(i - 3, w.length - 15));
          break;
        }
    var t = w.slice(a, a + 15).join(" ");
    return "“" + Gt((a > 0 ? "…" : "") + t + (a + 15 < w.length ? "…" : "")) + "” (" + gsmStRef(n) + ")";
  }
  function gsmStList(a, k) {
    k = k || 6;
    var b = a.slice(0, k);
    a.length > k && b.push("and " + (a.length - k) + " more");
    return b.length < 3 && a.length <= k ? b.join(" and ") : b.slice(0, -1).join(", ") + ", " + (a.length > k ? "" : "and ") + b[b.length - 1];
  }
  function gsmStSent(t) {
    return String(t || "")
      .replace(/\s+/g, " ")
      .split(/(?<=[.!?])\s+/)
      .filter(function (x) {
        return x.trim().length > 12;
      });
  }
  function gsmStEm(list) {
    var c = [0, 0, 0, 0, 0];
    list.forEach(function (n) {
      null != n.em && n.em >= 0 && n.em < 5 && c[n.em]++;
    });
    var o = [0, 1, 2, 3, 4]
      .filter(function (i) {
        return c[i] > 0;
      })
      .sort(function (a, b) {
        return c[b] - c[a];
      });
    return { c: c, o: o };
  }
  function gsmStruct() {
    try {
      return phKeep(gsmStructBuild) || "";
    } catch (e) {
      return "";
    }
  }
  window.gsmStruct = gsmStruct;
  function gsmStructBuild() {
    gsmMeanCss();
    var E = GSMEMO,
      src = gsmMeanSrc(),
      notes = src.filter(function (n) {
        return n.note;
      }),
      K = function (t) {
        return Ht(t).k;
      };
    notes.forEach(function (n) {
      n.keys = K(n.txt);
      n.name = gsmStName(n);
    });
    var R = [],
      CAUSE = /\b(reinforc\w*|feed\w*|fuel\w*|drive\w*|leads? to|haunt\w*|entrench\w*|freez\w*|ingrain\w*|built up|turns? to|forces? the|sustain\w*|perpetuat\w*|lock\w* in|continuance|itself)\b/i;
    function card(lab, html, ev) {
      R.push(
        '<div class="sread"><div class="srl">' +
          lab +
          '</div><div class="srm">' +
          html +
          "</div>" +
          (ev ? '<details class="more"><summary>The notes behind it</summary><div class="srev">' + ev + "</div></details>" : "") +
          "</div>",
      );
    }
    // 1. the system that holds
    var hind = notes.filter(function (n) {
        return n.side < 0;
      }),
      comp = [],
      sysNames = [];
    if (hind.length >= 3) {
      var adj = hind.map(function (a) {
          return hind.filter(function (b) {
            if (a === b) return !1;
            for (var k in a.keys) if (b.keys[k]) return !0;
            return !1;
          });
        }),
        seen = {};
      hind.forEach(function (n, i) {
        if (seen[i]) return;
        var q = [i],
          c = [];
        seen[i] = 1;
        while (q.length) {
          var j = q.shift();
          c.push(j);
          adj[j].forEach(function (b) {
            var bi = hind.indexOf(b);
            seen[bi] || ((seen[bi] = 1), q.push(bi));
          });
        }
        c.length > comp.length && (comp = c);
      });
      comp = comp
        .map(function (i) {
          return { n: hind[i], d: adj[i].length + (CAUSE.test(hind[i].txt) ? 100 : 0) - (hind[i].name.split(" ").length > 4 ? 50 : 0) };
        })
        .sort(function (a, b) {
          return b.d - a.d;
        })
        .map(function (x) {
          return x.n;
        });
      var nm = {};
      comp.forEach(function (n) {
        var k = n.name.toLowerCase();
        n.name && !nm[k] && ((nm[k] = 1), sysNames.push(n.name));
      });
    }
    if (sysNames.length >= 3) {
      var tied = comp.filter(function (n) {
          return CAUSE.test(n.txt);
        }),
        self = tied.length >= 2,
        em = gsmStEm(comp),
        o = em.o,
        g = "";
      o.length &&
        ([0, 4].indexOf(o[0]) >= 0 && [0, 4].indexOf(o[1]) >= 0
          ? (g = "Most of it sits on aggression and defiance, the lowest ground, which is why it holds: from there, change is unlikely in the short or medium term.")
          : 4 === o[0]
            ? (g = "Most of it sits on defiance, the lowest ground and the longest road to acceptance, which is why it holds.")
            : 0 === o[0]
              ? (g = "Most of it sits on aggression, low ground that can slide into defiance, which is why it holds: from there, change is unlikely in the short or medium term.")
              : 2 === o[0]
                ? (g = "Most of it sits on distrust, low ground where trust has to come before anything moves, which is why it holds.")
                : 3 === o[0]
                  ? (g = "Most of it sits on indifference, so it holds loosely: what you do next can tip it either way.")
                  : (g = "Most of it carries acceptance: the people inside it are content with it, which is its own kind of hold."));
      card(
        "THE SYSTEM THAT HOLDS",
        Gt(gsmStList(sysNames, 8)).replace(/^./, function (c) {
          return c.toUpperCase();
        }) +
          (self
            ? " reinforce one another into a self-supporting system against the goal. "
            : " hang together against the goal, each sharing ground with the others. ") +
          g,
        comp
          .slice(0, 8)
          .map(function (n) {
            return "<div>" + gsmStRef(n) + " <i>" + (null != n.em ? E[n.em] : "no emotion marked") + "</i>: " + Gt(n.name) + "</div>";
          })
          .join("") +
          (tied.length
            ? '<div class="srq">Where your notes say the parts hold each other up:</div>' +
              tied
                .slice(0, 3)
                .map(function (n) {
                  var se =
                    gsmStSent(n.txt).filter(function (x) {
                      return CAUSE.test(x);
                    })[0] || n.txt;
                  return "<div>" + gsmStQ(n, se) + "</div>";
                })
                .join("")
            : ""),
      );
    }
    // 2. the key tension
    var MORE = /\b(more|add\w*|increas\w*|grow\w*|reintroduc\w*|introduc\w*|putting|put|restor\w*|expand\w*|scal\w*|build\w*|adopt\w*)\b/i,
      FEAR = /\b(fear\w*|afraid|liabilit\w*|escap\w*|danger\w*|deadly|costly|disast\w*|mistake\w*|vilif\w*|enem\w*|eradicat\w*|threat\w*|catastroph\w*|harm\w*|blame\w*|unsafe)\b/i,
      parts = String(C.goal || "")
        .split(/[.;]|,|\bwhereas\b|\bbut\b|\band\b(?= [a-z]+ing\b)/i)
        .map(function (x) {
          return x.trim();
        })
        .filter(function (x) {
          return x.split(" ").length >= 3 && MORE.test(x);
        }),
      gc = parts[0];
    if (gc) {
      var gk = K(gc),
        fears = hind
          .map(function (n) {
            var hit = 0;
            for (var k in gk) n.keys[k] && hit++;
            var f = (n.txt.match(new RegExp(FEAR.source, "gi")) || []).length;
            return { n: n, s: hit && f ? hit + 2 * f : 0 };
          })
          .filter(function (x) {
            return x.s > 0;
          })
          .sort(function (a, b) {
            return b.s - a.s;
          }),
        helpHas = notes.some(function (n) {
          if (n.side <= 0) return !1;
          for (var k in gk) if (n.keys[k]) return !0;
          return !1;
        });
      if (fears.length && helpHas) {
        var f0 = fears[0].n,
          fs =
            gsmStSent(f0.txt).filter(function (x) {
              return FEAR.test(x);
            })[0] || f0.txt,
          fe = f0.em,
          gl =
            2 === fe
              ? " That fear sits on distrust, low ground where trust has to come before anything moves."
              : 4 === fe
                ? " That fear sits on defiance, the ground most resistant to any strategy."
                : 0 === fe
                  ? " That fear sits on aggression, which can harden into defiance."
                  : 3 === fe
                    ? " That fear sits on indifference, so it can still be moved either way."
                    : "";
        card(
          "THE KEY TENSION",
          "What the goal asks for more of, “" +
            Gt(gc.replace(/^(to|and|whereas)\s+/i, "")) +
            "” (the goal), is what the other side has learned to fear: " +
            gsmStQ(f0, fs) +
            ". The force the work needs is the force people resist, so asking for more of it isn’t enough; the work has to change what people expect it to do." +
            gl,
          fears
            .slice(0, 4)
            .map(function (x) {
              return "<div>" + gsmStRef(x.n) + " <i>" + (null != x.n.em ? E[x.n.em] : "no emotion marked") + "</i>: " + gsmStQ(x.n).replace(/ \(<a[^)]*<\/a>\)$/, "") + "</div>";
            })
            .join(""),
        );
      }
    }
    // 3. the loop
    var LOOP = /\b(reinforc\w*|accumulat\w*|feedback|itself|in turn|each passing|more and more|ever more|cycle|spiral|thicker|compound\w*|need for more)\b/i,
      ls = [];
    src.forEach(function (s0) {
      gsmStSent(s0.txt).forEach(function (x) {
        LOOP.test(x) && ls.push({ s: s0, t: x, k: K(x) });
      });
    });
    var kc = {},
      df = {};
    src.forEach(function (s0) {
      var kk = K(s0.txt);
      for (var k in kk) df[k] = (df[k] || 0) + 1;
    });
    ls.forEach(function (l) {
      for (var k in l.k) {
        var twice = (l.t.toLowerCase().match(new RegExp("\\b" + k, "g")) || []).length > 1;
        kc[k] = (kc[k] || 0) + 1 + (twice ? 2 : 0);
      }
    });
    var lk = Object.keys(kc)
      .filter(function (k) {
        return (
          ls.filter(function (l) {
            return l.k[k];
          }).length >= 2 && k.length > 3 && (df[k] || 0) <= 0.5 * src.length
        );
      })
      .sort(function (a, b) {
        return kc[b] - kc[a];
      })[0];
    if (lk) {
      var lsk = ls.filter(function (l) {
          return l.k[lk];
        }),
        best = lsk.slice().sort(function (a, b) {
          var ta = (a.t.toLowerCase().match(new RegExp("\\b" + lk, "g")) || []).length,
            tb = (b.t.toLowerCase().match(new RegExp("\\b" + lk, "g")) || []).length;
          return tb - ta || (b.s.note ? 1 : 0) - (a.s.note ? 1 : 0) || a.t.length - b.t.length;
        })[0],
        all = lsk
          .map(function (l) {
            return l.t;
          })
          .join(" "),
        nl = /\b(present|now|today|quickly|immediate\w*|soon as)\b/i.test(all) && /\b(future|later|years?|generations?|over time|eventually|each passing)\b/i.test(all),
        le = gsmStEm(
          lsk
            .map(function (l) {
              return l.s;
            })
            .filter(function (n) {
              return n.note;
            }),
        ).o[0],
        lg =
          0 === le
            ? " It runs on aggression, which can harden into defiance."
            : 4 === le
              ? " It runs on defiance, the ground most resistant to any strategy."
              : 2 === le
                ? " It runs on distrust, which can slide further down as easily as it climbs."
                : 3 === le
                  ? " It runs through indifference, so it could still be turned."
                  : 1 === le
                    ? " It runs on acceptance: people are content with it, which keeps it turning."
                    : "";
      card(
        "THE LOOP",
        gsmStQ(best.s, best.t, lk) +
          (nl
            ? ". What it settles in the present builds the conditions that call for more of it later, so each success makes the next round harder."
            : ". Each round of it makes the next round more likely.") +
          lg,
        lsk
          .slice(0, 4)
          .map(function (l) {
            return "<div>" + gsmStQ(l.s, l.t, lk) + "</div>";
          })
          .join(""),
      );
    }
    // 4. the opportunity
    var EXIST = /\b(already|existing|exists?|emerg\w*|growing|continu\w*|there are|in place|visible|underway)\b/i,
      okEm = function (n) {
        return null == n.em || 1 === n.em || 3 === n.em;
      },
      ex = notes.filter(function (n) {
        return n.side > 0 && okEm(n) && (3 === n.k || 7 === n.k);
      }),
      nw = notes.filter(function (n) {
        return n.side > 0 && okEm(n) && (5 === n.k || 6 === n.k) && !EXIST.test(n.txt);
      }),
      exNames = [],
      en = {};
    ex.forEach(function (n) {
      var nmx = gsmStName({ txt: n.txt.replace(/^\s*(reinforce|continue to|support|scale|grow|keep)\s+/i, "") });
      nmx && !en[nmx.toLowerCase()] && ((en[nmx.toLowerCase()] = 1), exNames.push(nmx));
    });
    if (exNames.length >= 2) {
      var oe = gsmStEm(ex).o[0];
      card(
        "THE OPPORTUNITY",
        (ex.length >= nw.length ? "Most" : "Part") +
          " of the alternative already exists: " +
          Gt(gsmStList(exNames, 6)) +
          ". The work is scaling and reinforcing it more than inventing it." +
          (1 === oe
            ? " It stands on the high ground of acceptance, the ground with the most promise, but acceptance doesn’t hold on its own: what isn’t reinforced can slip."
            : 3 === oe
              ? " Much of it sits on indifference, so it can tip either way until it is reinforced."
              : ""),
        ex
          .slice(0, 6)
          .map(function (n) {
            return "<div>" + gsmStQ(n) + "</div>";
          })
          .join("") +
          (nw.length
            ? '<div class="srq">Still to be designed new: ' +
              nw
                .slice(0, 6)
                .map(gsmStRef)
                .join(", ") +
              "</div>"
            : ""),
      );
    }
    // 5. where it can cross
    var ind = notes.filter(function (n) {
      return 3 === n.em;
    });
    if (ind.length && sysNames.length >= 3) {
      card(
        "WHERE IT CAN CROSS",
        gsmStList(ind.map(gsmStRef), 5).replace(/>place note/, ">Place note") +
          (1 === ind.length ? " carries" : " carry") +
          " indifference: the ridge between the low ground that holds and the high ground of acceptance. People there are for nothing yet, so they can be moved either way, and most crossings go through ground like this.",
        ind
          .slice(0, 5)
          .map(function (n) {
            return "<div>" + gsmStQ(n) + "</div>";
          })
          .join(""),
      );
    }
    return R.length >= 1 ? '<div class="plab">WHY IT BEHAVES THIS WAY</div><div class="sreads">' + R.join("") + "</div>" : "";
  }
'''

rep("""  window.gsmSaveP = P;
  function P() {""", JS + """  window.gsmSaveP = P;
  function P() {""")
rep('''#gsm .metal li .rmean2{font-size:15px;margin:0}";''',
    '''#gsm .metal li .rmean2{font-size:15px;margin:0}#gsm .sread{border-left:3px solid #111;padding:6px 0 6px 12px;margin:0 0 14px}#gsm .sread .srl{font-size:11px;font-weight:700;letter-spacing:.16em;color:#444;margin-bottom:3px}#gsm .sread .srm{font-size:16px;line-height:1.55;color:#111}#gsm .sread .srev{font-size:13.5px;line-height:1.45;color:#444;padding-left:9px;border-left:2px solid #ddd}#gsm .sread .srev div{margin:0 0 4px}#gsm .sread .srev i{font-style:normal;color:#777;font-size:12.5px}#gsm .sread .srq{margin:8px 0 4px;color:#222}";''')
rep("""            window.gsmSameAsk = "";
            return x;
          })() +
          we +""", """            window.gsmSameAsk = "";
            return x;
          })() +
          (window.gsmStruct ? window.gsmStruct() : "") +
          we +""")
rep('''                          "WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED" === r ||''',
    '''                          "WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED" === r ||
                          "WHY IT BEHAVES THIS WAY" === r ||''')
rep('t && (t.textContent = "v220");', 't && (t.textContent = "v221");')
open(P, "w").write(s)
print("ok")
