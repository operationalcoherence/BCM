"""v248: Pattern Analysis, several stories (the Several Systems capability, first on Analysis).

Finds the separate low grounds on a line map from what the workbook already holds
(each note's place, side, and emotion, with the same height rule the terrain uses),
and when there is more than one, YOUR STORY SO FAR opens with one story for each
(cap 3): what holds it, what helps, and where it can cross. The one-line story is kept,
folded under it. A workbook with one structure, a place map, or fewer than 12 placed
notes is unchanged.
"""
import re, sys
F = "gsm-readable.js"
s = open(F).read()

JS = r'''
  /* v248: several systems. The low grounds are found the way the terrain makes them:
     height = acceptance - (1.5 x aggression + distrust + 3.4 x defiance), smoothed by each
     note's reach; hollows that meet at a shallow saddle are one hollow. Line maps only. */
  function gsmSystems() {
    var pts = [],
      E = GSMEMO;
    (C.m || []).forEach(function (t, i) {
      if (!t || !String(t[3] || "").trim() || "number" != typeof t[1] || "number" != typeof t[2]) return;
      pts.push({
        x: t[1],
        y: t[2],
        e: "number" == typeof t[5] && t[5] >= 0 && t[5] < 5 ? t[5] : null,
        em: "number" == typeof t[5] && t[5] >= 0 && t[5] < 5 ? t[5] : null,
        side: t[2] < 118 ? 1 : t[2] > 118 ? -1 : 0,
        ref: "note " + (i + 1),
        lab: "N" + (i + 1),
        txt: t[3],
        k: t[0],
      });
    });
    var res = { low: [], high: [], pts: pts };
    var ep = pts.filter(function (p) {
      return null != p.e;
    });
    if (pts.length < 12 || ep.length < 8) return res;
    var CX = 4,
      VX = 86,
      VY = 58,
      n = VX * VY,
      sig = 22;
    var nn = ep
      .map(function (p) {
        var m = 1e9;
        ep.forEach(function (q) {
          q !== p && (m = Math.min(m, Math.hypot(p.x - q.x, p.y - q.y)));
        });
        return m;
      })
      .sort(function (a, b) {
        return a - b;
      });
    sig = Math.max(13, Math.min(30, 0.9 * nn[Math.floor(nn.length / 2)]));
    var H = new Float32Array(n),
      s2 = 2 * sig * sig,
      cut = 16 * sig * sig,
      hmin = 1e9,
      hmax = -1e9;
    for (var j = 0; j < VY; j++)
      for (var i = 0; i < VX; i++) {
        var x = i * CX,
          y = j * CX,
          w = [0, 0, 0, 0, 0];
        ep.forEach(function (p) {
          var d2 = (x - p.x) * (x - p.x) + (y - p.y) * (y - p.y);
          d2 < cut && (w[p.e] += Math.exp(-d2 / s2));
        });
        var h = w[1] - (1.5 * w[0] + w[2] + 3.4 * w[4]);
        H[j * VX + i] = h;
        h < hmin && (hmin = h);
        h > hmax && (hmax = h);
      }
    var span = Math.max(1e-6, hmax - hmin);
    function cellOf(p) {
      var ci = Math.max(0, Math.min(VX - 1, Math.round(p.x / CX))),
        cj = Math.max(0, Math.min(VY - 1, Math.round(p.y / CX)));
      return cj * VX + ci;
    }
    /* merge-by-depth watershed: a hollow shallower than 12% of the map's height at its
       saddle joins its neighbor */
    function sheds(sign) {
      var ord = [],
        par = new Int32Array(n).fill(-1),
        floor = {};
      for (var q = 0; q < n; q++) ord.push(q);
      ord.sort(function (a, b) {
        return sign * H[a] - sign * H[b];
      });
      function find(a) {
        while (par[a] !== a) (par[a] = par[par[a]]), (a = par[a]);
        return a;
      }
      ord.forEach(function (c) {
        var ci = c % VX,
          cj = (c / VX) | 0,
          roots = [];
        for (var dj = -1; dj <= 1; dj++)
          for (var di = -1; di <= 1; di++) {
            if (!di && !dj) continue;
            var ni = ci + di,
              nj = cj + dj;
            if (ni < 0 || nj < 0 || ni >= VX || nj >= VY) continue;
            var u = nj * VX + ni;
            if (par[u] < 0) continue;
            var r = find(u);
            roots.indexOf(r) < 0 && roots.push(r);
          }
        if (!roots.length) {
          par[c] = c;
          floor[c] = sign * H[c];
          return;
        }
        roots.sort(function (a, b) {
          return floor[a] - floor[b];
        });
        var lv = sign * H[c],
          keep = roots[0];
        par[c] = keep;
        roots.slice(1).forEach(function (r) {
          if (lv - floor[r] < 0.12 * span) par[r] = keep;
        });
      });
      return find;
    }
    function groups(sign, ok) {
      var find = sheds(sign),
        G = {};
      pts.forEach(function (p) {
        if (!ok(p)) return;
        var r = find(cellOf(p));
        (G[r] = G[r] || []).push(p);
      });
      return Object.keys(G)
        .map(function (r) {
          var L = G[r],
            cx = 0,
            cy = 0;
          L.forEach(function (p) {
            cx += p.x;
            cy += p.y;
          });
          return { n: L, x: cx / L.length, y: cy / L.length, depth: sign * H[+r] };
        })
        .filter(function (g) {
          return g.n.length >= 3;
        });
    }
    res.low = groups(1, function (p) {
      return 3 !== p.e && (p.side < 0 || (null != p.e && [0, 2, 4].indexOf(p.e) >= 0 && p.side <= 0));
    })
      .filter(function (g) {
        var lowE = g.n.filter(function (p) {
          return [0, 2, 4].indexOf(p.e) >= 0;
        }).length;
        return g.y > 118 && lowE >= 2 && g.depth < -0.15 * span;
      })
      .sort(function (a, b) {
        return b.n.length - a.n.length || a.depth - b.depth;
      });
    res.high = groups(-1, function (p) {
      return p.side > 0;
    }).sort(function (a, b) {
      return b.n.length - a.n.length;
    });
    var tot = res.low.reduce(function (a, g) {
      return a + g.n.length;
    }, 0);
    res.several = res.low.length >= 2 && res.low[0].n.length < 0.75 * tot && res.low[1].n.length >= 3;
    return res;
  }
  window.gsmSystems = gsmSystems;
  function gsmStories(mt) {
    if (!mt || mt.querySelector(".stories")) return;
    var Y = gsmSystems();
    window.gsmSys = Y;
    if (!Y.several) return;
    var E = GSMEMO,
      ST = Y.low.slice(0, 3).sort(function (a, b) {
        return a.x - b.x;
      }),
      ind = Y.pts.filter(function (p) {
        return 3 === p.e;
      }),
      usedInd = {},
      usedHelp = {};
    function where(g) {
      return g.x < 115 ? "start" : g.x > 225 ? "goal" : "mid";
    }
    function lowEm(g) {
      return gsmStEm(
        g.n.filter(function (p) {
          return [0, 2, 4].indexOf(p.e) >= 0;
        }),
      ).o;
    }
    var GW = { 0: "the lower ground of aggression", 2: "the low ground of distrust", 4: "defiance, the lowest ground" };
    function dsq(a, b) {
      return Math.hypot(a.x - b.x, a.y - b.y);
    }
    function segD(p, a, b) {
      var vx = b.x - a.x,
        vy = b.y - a.y,
        L = vx * vx + vy * vy || 1,
        t = Math.max(0, Math.min(1, ((p.x - a.x) * vx + (p.y - a.y) * vy) / L));
      return Math.hypot(p.x - a.x - t * vx, p.y - a.y - t * vy);
    }
    /* v248b: each story is read, not listed. Seven moves (his brief, 11-24 07:19): the dynamic, why it
       emerges, what recreates it, what it reveals, why it matters, where it goes if it continues, and
       what would have to change. Each move is chosen from what the hollow holds: where it sits in time,
       its emotions, acceptance of the present inside it, aggression answering it from the side that
       helps, a ridge of indifference out of it, and its size. No note text and no note numbers in it. */
    var used = {},
      helpAgg = Y.pts.filter(function (p) {
        return p.side > 0 && 0 === p.e;
      }).length,
      allLow = ST.reduce(function (a, g) {
        return a + g.n.length;
      }, 0),
      seenWhere = {},
      chap = [],
      out = [];
    function pick(L) {
      for (var i = 0; i < L.length; i++) if (L[i][0] && !used[L[i][1]]) return (used[L[i][1]] = 1), L[i][2];
      for (i = 0; i < L.length; i++) if (L[i][0]) return L[i][2];
      return "";
    }
    ST.forEach(function (g, k) {
      var wh = where(g),
        o = lowEm(g),
        c = gsmStEm(g.n).c,
        e0 = o[0],
        e1 = o.length > 1 && c[o[1]] * 2 >= c[o[0]] ? o[1] : null,
        acc = g.n.some(function (p) {
          return 1 === p.e;
        }),
        hasAgg = c[0] > 0,
        hc = Y.high
          .slice()
          .sort(function (a, b) {
            return dsq(a, g) - dsq(b, g);
          })[0],
        tgt = hc || { x: g.x, y: 60 },
        cr = ind.filter(function (p) {
          return !usedInd[p.ref] && segD(p, g, tgt) < 40;
        }),
        big = 0 === k && g.n.length * 2 >= allLow,
        second = "start" === wh && seenWhere.start,
        EW = { 0: "aggression", 2: "distrust", 4: "defiance" },
        emo = EW[e0] + (null != e1 ? " and " + EW[e1] : "");
      cr.forEach(function (p) {
        usedInd[p.ref] = 1;
      });
      seenWhere[wh] = 1;
      var S = [];
      /* 1. the dynamic */
      S.push(
        "goal" === wh
          ? "Close to the goal, the ground drops again, into " +
              emo +
              ". This is the low ground that waits where the change is close to arriving, where a new arrangement can exist in name while the old one goes on underneath it."
          : "mid" === wh
            ? "Partway to the goal, a separate low ground of " +
              emo +
              " forms where the change stops being an idea and starts to reach what people stand to lose."
            : second
              ? "A second low ground lies at the start, apart from the first, and it is made of " + emo + "."
              : pick([
                  [4 === e0, "s1d", "At the start, the change meets defiance, the lowest ground: people are not weighing the goal and deciding against it so much as refusing to let it into the conversation at all."],
                  [0 === e0, "s1a", "At the start, the change is met with " + emo + ": the goal is treated less as a proposal to weigh than as a threat to push back."],
                  [!0, "s1t", "At the start, the change meets " + emo + ": before anyone weighs what the goal offers, they are weighing whether the change, and those carrying it, can be trusted."],
                ]),
      );
      /* 2. why it emerges */
      S.push(
        pick([
          [acc, "w-acc", "It emerges because the present arrangement is still accepted as legitimate. That acceptance is not neutral ground here: it is what the resistance stands on, and it gives the resistance the standing of common sense."],
          ["goal" === wh, "w-goal", "It emerges because a change can ask for new behavior without changing what people are rewarded, trusted, or protected for, and then the old behavior stays the safer one."],
          ["mid" === wh, "w-mid", "It emerges once the change becomes concrete enough to threaten people's place in what comes after it, so holding on becomes a way of protecting a future rather than a past."],
          [4 === e0, "w-def", "It emerges where the old way has become part of who people are, so giving it up would mean giving up part of themselves."],
          [0 === e0, "w-agg", "It emerges where the change is lived as an attack on how people already work, so pushing back feels like defending something, not blocking something."],
          [!0, "w-dis", "It emerges where people cannot yet see what the change will ask of them, so they hold to what they know until they can."],
        ]),
      );
      /* 3. what keeps recreating it */
      S.push(
        pick([
          [helpAgg && hasAgg, "r-loop", "What keeps recreating it is the reply it gets. Aggression on the side that helps, aimed at those who resist, confirms the resisters' reading of the change, and their resistance in turn confirms the supporters' reading of them. Each side's emotion becomes the other side's evidence."],
          ["goal" === wh, "r-goal", "What keeps recreating it is that adoption can be shown without being lived. As long as the change is judged by what is announced rather than by what is done, the old ways can go on in plain sight without being seen."],
          [null != e1, "r-mix", 2 === e0 || 2 === e1 ? "What keeps recreating it is that its emotions hold each other up: distrust gives " + EW[2 === e0 ? e1 : e0] + " its reasons, and " + EW[2 === e0 ? e1 : e0] + " gives distrust its proof." : "What keeps recreating it is that its emotions hold each other up: aggression keeps defiance in practice, and defiance keeps aggression justified."],
          [!0, "r-same", "What keeps recreating it is that each round of the change arrives without changing the ground it lands on, so each round is met the way the last one was."],
        ]),
      );
      /* 4. what it reveals */
      S.push(
        "goal" === wh
          ? "It reveals that in this system adoption and change may not be the same thing: the structure can move while the behavior stays."
          : "mid" === wh
            ? "It reveals that the resistance has moved from ideas to stakes. What is being defended here is not a view of the goal but a person's footing once the goal arrives."
            : pick([
                [acc, "v-acc", "It reveals that the system's coherence is still carried by the arrangement the goal would replace. Resisting is a way of keeping that coherence while familiar assumptions lose their standing."],
                [!0, "v-gen", "It reveals how much of the system's footing still rests on the way things are done now, and how little of it has yet been given anywhere else to stand."],
              ]),
      );
      /* 5. why it matters */
      S.push(
        big
          ? "It matters because most of the ground that hinders lies here: whatever is designed for the goal will land on this ground first, and will be read through it."
          : "goal" === wh
            ? "It matters because it can undo the work after the work looks finished, and because it is the hardest of these low grounds to see."
            : "It matters because it stands apart from the others. Work aimed at another low ground will not reach it, and it can hold even if the others give way.",
      );
      /* 6. if it continues */
      S.push(
        ("goal" === wh
          ? "If it continues, the system can look changed while behaving as before, and the gap between the two will be taken as proof that the change never worked. Meanwhile, "
          : "") +
          pick([
            [4 === e0, "f-def", ("goal" === wh ? "d" : "Left as it is, d") + "efiance deepens: the longer the old way is defended, the more of people's identity it carries, and the longer the road back to acceptance becomes."],
            [0 === e0 || 0 === e1, "f-agg", ("goal" === wh ? "a" : "Left as it is, a") + "ggression can harden into defiance, the lowest ground, from which change is unlikely in the short or medium term."],
            [!0, "f-dis", ("goal" === wh ? "d" : "Left as it is, d") + "istrust spreads from the change to those leading it, and whatever comes next inherits that distrust before it begins."],
          ]),
      );
      /* 7. what would have to change */
      S.push(
        (cr.length
          ? pick([
              [!0, "c1", "For it to lose its influence, people do not have to move straight to acceptance. The nearer step is indifference: a ridge of it already runs out of this low ground, and most crossings go through ground like that. The work is to make that ridge easier to reach, not to ask people to climb a cliff."],
              [!0, "c2", "Here too the nearer step is indifference, not acceptance. A ridge of it already leaves this low ground, and the work is to widen it, so that leaving does not mean taking a side all at once."],
              [!0, "c3", "As in the other stories, the way out runs through indifference before acceptance, along a ridge that already leaves this low ground, where people can rest without being asked to agree."],
            ])
          : "For it to lose its influence, a ridge has to be made first. Nothing between this low ground and the help yet carries indifference, so going straight across is a climb over bare rock, and it takes the most energy in either direction.") +
          (acc ? " The acceptance that holds the present in place has to loosen too: until the current arrangement stops looking like the only legitimate one, every case for the goal will be heard as an attack on it." : "") +
          ("goal" === wh ? " Near the goal, the way out also means judging the change by what people do, not by what has been declared." : ""),
      );
      chap.push({ x: g.x, wh: wh, e0: e0, acc: acc });
      var TL = { start: second ? "AT THE START, A SECOND LOW GROUND" : "AT THE START", mid: "PARTWAY TO THE GOAL", goal: "CLOSE TO THE GOAL" }[wh];
      out.push(
        '<div class="story1"><div class="s1h">STORY ' +
          (k + 1) +
          " · " +
          TL +
          '</div><div class="s1p"><p>' +
          S.slice(0, 3).join(" ") +
          "</p><p>" +
          S.slice(3).join(" ") +
          '</p></div><details class="more"><summary>The notes behind this reading</summary><div class="srev">' +
          g.n
            .map(function (p) {
              return "<div>" + gsmStRef(p) + " <i>" + (null != p.em ? E[p.em] : "no emotion marked") + "</i>: " + gsmStQ(p).replace(/ \(<a[^)]*<\/a>\)$/, "") + "</div>";
            })
            .join("") +
          "</div></details></div>",
      );
    });
    /* v248c: the movement underneath (his brief, 11-24 07:28). The stories read as chapters in time
       order: what each defends, what is threatened next, what changes, what stays the same, and the
       larger story. Identity, legitimacy, power, incentives, coherence, and adaptation; no emotional
       terrain words. Chosen from the same readings as the stories. */
    var DF = {
      legit: {
        what: "legitimacy: the present arrangement's claim to be the right way of doing things, and with it the identities built inside that arrangement",
        why: "Power here belongs to whoever can make the present look like common sense, and as long as it does, the change has to argue for its right to exist before it can argue for anything else.",
        verb: "denies the change its legitimacy",
        obj: "what is right",
      },
      ident: {
        what: "identity: who people are within the way things are done now",
        why: "When a way of working has become part of who someone is, any change to it is heard as a judgment of them, and keeping it intact becomes a matter of self-respect rather than preference.",
        verb: "guards who it is against it",
        obj: "who people are",
      },
      trust: {
        what: "the authority to decide how change happens: who gets to carry it, on whose terms, and with what promises",
        why: "The contest is over power before it is over content; until people trust the hands the change is in, they withhold the cooperation it needs.",
        verb: "questions who has the right to carry it",
        obj: "who decides",
      },
      work: {
        what: "how the work is done now and who controls it",
        why: "The existing routines carry the system's competence and its lines of control, so a challenge to them is a challenge to whoever those routines keep in charge.",
        verb: "defends how its work is done",
        obj: "how the work is controlled",
      },
      place: {
        what: "position: each person's place, role, and livelihood in whatever comes after",
        why: "Once the change is real enough to redistribute roles, its incentives become personal; people stop asking whether the goal is right and start asking what it will cost them.",
        verb: "defends each person's place against it",
        obj: "who each person will be",
      },
      practice: {
        what: "practice: the everyday ways of working that can keep the old order alive inside the new one",
        why: "Here power is exercised quietly. The form of the change can be adopted while practice stays loyal to the old incentives, so the system keeps its coherence by letting the two drift apart.",
        verb: "lets it in by name while keeping the old life underneath",
        obj: "how the work is actually done",
      },
    };
    var CH = chap
        .slice()
        .sort(function (a, b) {
          return a.x - b.x;
        }),
      usedD = {};
    CH.forEach(function (c) {
      var d =
        "goal" === c.wh
          ? "practice"
          : "mid" === c.wh
            ? "place"
            : c.acc && !usedD.legit
              ? "legit"
              : 4 === c.e0 && !usedD.ident
                ? "ident"
                : 2 === c.e0 && !usedD.trust
                  ? "trust"
                  : !usedD.work
                    ? "work"
                    : !usedD.ident
                      ? "ident"
                      : "trust";
      usedD[d] = 1;
      c.key = d;
      c.d = DF[d];
    });
    /* v248e: one chapter in six levels (his brief, 11-24 07:37): pattern, mechanism, invariant,
       necessity, development, theory. Continuous prose, no section labels, no note text or numbers. */
    var SHORT = {
        legit: "an argument about what is right",
        ident: "loyalty to who people already are",
        trust: "a dispute over who may decide",
        work: "a hold on the routines",
        place: "a defense of each person's place",
        practice: "quiet practice under a new name",
      },
      anyAcc = CH.some(function (c) {
        return c.acc;
      }),
      hasGoal = CH.some(function (c) {
        return "goal" === c.wh;
      }),
      hasMid = CH.some(function (c) {
        return "mid" === c.wh;
      }),
      allDef =
        CH.filter(function (c) {
          return 4 === c.e0;
        }).length *
          2 >=
        CH.length,
      wideMid = ind.length >= Math.max(4, 0.15 * Y.pts.length),
      K = anyAcc ? "legit" : allDef ? "ident" : "order",
      forms = gsmMeanList(
        CH.map(function (c) {
          return SHORT[c.key];
        }),
      ),
      EP = [];
    /* 1. pattern */
    EP.push(
      "The change does not meet resistance once. It meets it again and again, and each time the resistance takes the shape the change has reached: " +
        forms.replace(/, and /, ", and finally ").replace(/^([^,]*) and /, CH.length === 2 ? "$1, and then " : "$1 and ") +
        "." +
        (helpAgg ? " Around it a second pattern forms: support answers resistance in kind, and each side hardens the other." : "") +
        (wideMid ? " Between them lies a wide middle that is neither for nor against, waiting to see which way things go." : ""),
    );
    /* 2. mechanism */
    var M = [];
    anyAcc && M.push("the present arrangement is still taken for granted as the right one, so any alternative has to argue against common sense");
    helpAgg && M.push("each side reads the other's response as proof of its own fears");
    hasMid && M.push("the rewards people can count on are tied to the places they hold now");
    hasGoal && M.push("the change is judged by what is declared rather than by what is done, so compliance can be shown without being lived");
    M.length < 2 && M.push("nothing in the change yet alters what people are trusted, protected, or rewarded for");
    EP.push(
      "What produces this is not a lack of information. It is that " +
        (M.length > 2 ? M.slice(0, -1).join("; ") + "; and " + M[M.length - 1] : M.join(" and ")) +
        ". Each of these keeps recreating the same response, because the response works: it keeps the system able to act in the way it already knows.",
    );
    /* 3. invariant */
    var INV = {
      legit: ["the standing of the present arrangement as the legitimate one", "a shared sense of what is right and of who belongs"],
      ident: ["the system's present identity", "continuity of self: people remaining recognizable to themselves and to one another"],
      order: ["the present order of control", "predictability: knowing who decides, what counts as good work, and who is safe"],
    }[K];
    EP.push(
      "Beneath the emotions, the arguments, and the behaviors, which all change, one thing does not. From beginning to end the system protects " +
        INV[0] +
        ". The function it is preserving is " +
        INV[1] +
        ".",
    );
    /* 4. necessity */
    EP.push(
      "That protection is not unreasonable. A system that let go of it all at once would lose more than a habit. " +
        (K === "legit"
          ? "It would lose the ground on which its members agree about what is right, who may decide, and whose work counts, and without that agreement every decision has to be fought for again."
          : K === "ident"
            ? "It would lose the continuity that lets its members recognize themselves in their work, and with it the pride and competence that continuity carries."
            : "It would lose its ability to coordinate under pressure, because coordination rests on knowing who decides and what is expected.") +
        (hasMid ? " For the people inside it, the stakes are also plainly material: their places, their skills, and their livelihoods are built on the arrangement as it stands." : "") +
        " From the system's side, holding on is a way of staying able to function while the future is still unclear.",
    );
    /* 5. development */
    var D = CH.map(function (c, i) {
      return (
        (0 === i
          ? "It is defended first as "
          : "start" === c.wh && "start" === CH[i - 1].wh
            ? "at the same time as "
            : i === CH.length - 1
              ? "and last as "
              : "then as ") + SHORT[c.key]
      );
    });
    EP.push(
      "Across the stories the system does not change what it protects; it changes how. " +
        D.join(", ") +
        ". With each step the protection moves closer to each person and further out of sight." +
        (hasGoal
          ? " What becomes hardest to see is that the resistance has not ended: by the time the change looks adopted, the protection has moved inside the new form and goes on there."
          : " What becomes hardest to see is that the dispute was never only about the goal; it was about what the goal would take away."),
    );
    /* 6. theory */
    EP.push(
      "What this workbook reveals is that a system does not resist change as such. It resists the loss of the function the present arrangement performs, and it will keep finding new forms for that resistance for as long as the change offers nothing that performs the function better." +
        (hasGoal ? " Adoption is not transformation; a system can take on the shape of a change and keep its old purpose inside it." : "") +
        " The general principle is that change succeeds not when resistance is overcome, but when what the resistance protects is provided another way: " +
        (K === "legit"
          ? "a new arrangement that people can hold as legitimately as the old one."
          : K === "ident"
            ? "a new way of working that people can recognize themselves in."
            : "a new order that is as predictable as the old one.") +
        " This matters because it changes where the work is. Persuading, pressing, or outlasting the resistance only teaches it new forms. The work is to build what it is protecting into the place the goal is going.",
    );
    var more = Y.low.length > 3 ? " These are the three largest; " + (Y.low.length - 3) + (Y.low.length - 3 > 1 ? " smaller hollows are" : " smaller hollow is") + " left out." : "";
    var box = document.createElement("div");
    box.className = "stories";
    box.innerHTML =
      '<p class="stsn">Your workbook holds ' +
      ["", "one story", "two stories", "three stories"][ST.length] +
      ". Read together, they show what the system is doing and why." +
      more +
      "</p>" +
      '<div class="evo"><div class="s1h">WHAT THE SYSTEM IS DOING</div>' +
      EP.map(function (p) {
        return "<p>" + p + "</p>";
      }).join("") +
      '</div><details class="more evst"><summary>Each chapter read on its own</summary>' +
      out.join("") +
      "</details>";
    var rest = [].slice.call(mt.children).filter(function (c) {
        return !c.classList.contains("owm");
      }),
      fd = document.createElement("details");
    fd.className = "more onel";
    fd.innerHTML = "<summary>The whole workbook read as one story</summary>";
    rest.forEach(function (c) {
      fd.appendChild(c);
    });
    mt.prepend(fd);
    mt.prepend(box);
  }
'''

CSS = '#gsm .stories{margin:6px 0 10px}#gsm .stories .stsn{font-size:17.5px;line-height:1.6;color:#111}#gsm .story1{border-left:3px solid #111;padding:4px 0 6px 14px;margin:16px 0}#gsm .story1 .s1h{font-size:11px;font-weight:700;letter-spacing:.16em;color:#444;margin-bottom:6px}#gsm .story1 .s1v{font-size:18px;line-height:1.55;font-style:italic;color:#111;margin:0 0 10px}#gsm .story1 .s1p p{font-size:16.5px;line-height:1.65;color:#111;margin:0 0 10px}#gsm .story1 .s1p b{font-weight:700;color:#111}#gsm details.onel{margin-top:14px}#gsm .evo{border-left:3px solid #111;padding:4px 0 4px 14px;margin:14px 0}#gsm .evo p{font-size:16.5px;line-height:1.65;color:#111;margin:0 0 12px}#gsm details.evst{margin:6px 0 8px}'

a = "  window.gsmStruct = gsmStruct;\n"
assert s.count(a) == 1
s = s.replace(a, a + JS, 1)

b = """        p1 ? (p1.after(h), h.after(p)) : (mt.prepend(p), mt.prepend(h));
      }
    }
"""
assert s.count(b) == 1
s = s.replace(b, b + """    try {
      gsmStories(fd.querySelector(".mtext"));
    } catch (e) {}
""", 1)

c = '#gsm .stn{color:#888;font-size:13px}";'
assert s.count(c) == 1
s = s.replace(c, '#gsm .stn{color:#888;font-size:13px}' + CSS + '";', 1)

d = 't.textContent = "v247"'
assert s.count(d) == 1
s = s.replace(d, 't.textContent = "v248"', 1)
open(F, "w").write(s)
print("v248 applied")
