  /* v298: YOUR STORY SO FAR for a place map (his go-ahead, 25 Nov 2026 22:50: "In the engine first").
     The line-map story reads hollows in the emotion ground; on a place map the hills are real land, so
     this one reads the notes and answers instead, with no terrain words. One story, the same four
     summary paragraphs, and the same seven moves in the fold. Each reason needs two places (notes that
     hinder, or the answers to Q.1 and Q.2). Silent unless the workbook holds enough to say something. */
  var GSM_PHOLD = [
    ["risk", /risk (?:is|as) low|low risk|risk[^.;]{0,50}\b(?:low|elsewhere|limited to|not concern|does not apply|doesn'?t apply)|perceptions? of (?:wildfire |the )?(?:risk|danger|threat)|not (?:directly )?experienc|underestimat|won'?t happen (?:here|to)|not at risk|believes? (?:it is |they are )?safe/i],
    ["look", /\bnatural\b|\bhistoric\b|\bthe look of\b|(?:look|storefronts?|facades?|street|character|view)\b[^.;]{0,40}\b(?:changed|altered|modified)|\baesthetic|\bscenery|\bscenic|\bbeauty|\bcharm|repulsive|\bcharacter of\b|(?:change|changing|modify\w*|cutting|alter\w*)\b[^.;]{0,40}\b(?:landscape|environment|roofing|siding|look|trees|yard|view)|landscapes?\b[^.;]{0,30}\b(?:undesirable|as they are|conserve|preserve)|(?:conserve|preserve)\b[^.;]{0,30}\blandscape/i],
    ["cost", /financ|econom|afford|\bcosts?\b|costly|expens|\bmoney\b|budget|\bprices?\b|\bpay for\b/i],
    ["worth", /anyway|regardless|no difference|not worth|pointless|futil|insurance|one-and-done|one and done|won'?t (?:help|matter|work)/i],
    ["trad", /\btradition|\bcentur(?:y|ies)\b|hundred years|\bdecades\b|always been|always ha(?:s|ve)|as it always|\blegacy\b|entrench|\bhabits?\b|ingrained|cultural norm|not broken/i],
    ["fear", /\bfears?\b|\bfeared\b|afraid|liabilit|danger(?!ous)|deadly|\bblame|worried/i],
    ["expect", /expectation|\bpublic\b|politic|\bmedia\b|televis|community reaction/i],
  ];
  function gsmPlaceStory(mt) {
    var PM = (C && C.p && C.p.m) || [],
      A = (C && C.a) || [],
      E = GSMEMO;
    if (!mt || mt.querySelector(".stories")) return;
    var P = [];
    PM.forEach(function (t, i) {
      if (!t || !String(t[3] || "").trim()) return;
      var e = "number" == typeof t[5] && t[5] >= 0 && t[5] < 5 ? t[5] : null,
        k = +t[0] || 0;
      P.push({
        k: k,
        e: e,
        em: e,
        txt: String(t[3]),
        lab: "N" + (i + 1),
        ref: "place note " + (i + 1),
        pts: [[t[1], t[2]]].concat(Array.isArray(t[4]) ? t[4] : []),
        hin: (1 === k || 2 === k) && null != e && 1 !== e,
        help: 3 === k && 1 === e,
      });
    });
    var HIN = P.filter(function (p) {
        return p.hin;
      }),
      HELP = P.filter(function (p) {
        return p.help;
      });
    if (P.length < 8 || HIN.length < 3) return;
    /* reasons, each from two places */
    var TX = P.filter(function (p) {
      return 1 === p.k || 2 === p.k || ((3 === p.k || 4 === p.k) && null != p.e && 1 !== p.e);
    })
      .map(function (p) {
        return p.txt;
      })
      .concat(String(A[0] || "").split(/(?<=[.!?;])\s+|\n+/), String(A[1] || "").split(/(?<=[.!?;])\s+|\n+/))
      .filter(function (x) {
        return x && x.trim();
      });
    var HD = {};
    TX.forEach(function (t) {
      t = t.replace(/(\b(?:protect|safeguard|defend|sav)\w*\b[^.;]{0,60}?)\blivelihoods?\b/gi, "$1");
      GSM_PHOLD.forEach(function (h) {
        h[1].test(t) && (HD[h[0]] = (HD[h[0]] || 0) + 1);
      });
    });
    var ALL = TX.join(" \n "),
      HAS = function (k) {
        return (HD[k] || 0) >= 2;
      },
      KEYS = ["look", "risk", "cost", "worth", "trad", "fear", "expect"].filter(HAS);
    if (!KEYS.length) return;
    var absent = /seasonal|part-time|second homes?|vacation homes?|secluded|\bremote\b|away from|miss (?:the )?(?:fire )?season/i.test(ALL),
      supply = /market|contractor|service providers?|\bservices\b|no one (?:to|who)|vendors?|\blabor\b/i.test(ALL),
      GA = (String((C && C.goal) || "") + " " + A.join(" ")).toLowerCase(),
      unit = /homeowner|household|\bresidents?\b|\bhomes?\b|property owner/.test(GA) ? "household" : "person",
      fire = /\bfire|wildfire/.test(GA),
      its = "household" === unit ? "its" : "their",
      inside = "household" === unit ? "from inside a single household" : "from where each person stands",
      quiet = fire ? "every season without a fire" : "every year that nothing goes wrong",
      Q1 = String(A[0] || "").toLowerCase(),
      saidInfo = /knowledge|information|understand|aware|educat|learn|familiar/.test(Q1 + " " + String(A[3] || "").toLowerCase());
    /* how far the people already doing the work are from those who hold back */
    function dm(a, b) {
      var R = 6371e3,
        r = Math.PI / 180,
        x = (b[1] - a[1]) * r * Math.cos(((a[0] + b[0]) / 2) * r),
        y = (b[0] - a[0]) * r;
      return R * Math.sqrt(x * x + y * y);
    }
    var near = 1e12;
    HIN.forEach(function (h) {
      HELP.forEach(function (g) {
        h.pts.forEach(function (a) {
          g.pts.forEach(function (b) {
            "number" == typeof a[0] && "number" == typeof b[0] && (near = Math.min(near, dm(a, b)));
          });
        });
      });
    });
    var walk = near < 400 ? "a few minutes' walk" : near < 1500 ? "a short walk" : near < 5000 ? "a short drive" : "";
    /* emotions on the side that holds back, most first */
    var cnt = [0, 0, 0, 0, 0];
    HIN.forEach(function (p) {
      cnt[p.e]++;
    });
    var ord = [0, 4, 2, 3]
        .filter(function (e) {
          return cnt[e] > 0;
        })
        .sort(function (a, b) {
          return cnt[b] - cnt[a];
        }),
      emoL = gsmMeanList(
        ord.map(function (e) {
          return E[e];
        }),
      ),
      hasDef = cnt[4] > 0,
      hasAgg = cnt[0] > 0,
      hasDis = cnt[2] > 0,
      hasInd = cnt[3] > 0;
    /* worth, in the user's own reasons */
    var WP = [];
    /anyway|regardless/i.test(ALL) && WP.push("household" === unit ? "it may not save the house anyway" : "it may not pay off anyway");
    /insurance/i.test(ALL) && WP.push("insurance seems to carry the loss");
    /one-and-done|one and done/i.test(ALL) && WP.push("one round of it seems to be enough");
    /no difference|not worth|pointless|futil|won'?t (?:help|matter|work)/i.test(ALL) && WP.push("it may make no difference");
    var SH = {
        look: "how the place would look",
        risk: "a danger people do not feel",
        cost: "what it costs",
        worth: "doubt that it is worth doing",
        trad: "the weight of habit",
        fear: "fear of what goes wrong",
        expect: "what others expect",
      },
      MC = {
        look: "the work would change how the place looks, and how it looks is much of why people are there",
        risk: "the risk looks low, or like someone else's" + (absent ? ", and many are not there in the season when it would show itself" : ""),
        cost: "the cost falls on each " + unit + (supply ? ", and there are not yet enough people offering to do the work" : ""),
        worth: "the work does not look worth it" + (WP.length ? ": " + gsmMeanList(WP.slice(0, 3)).replace(/, and /, ", or ").replace(/^([^,]*) and /, "$1, or ") : ""),
        trad: "a long habit makes the present way look like the only sensible one",
        fear: "fear of what happens when something goes wrong, and of who will be blamed, makes holding back the safer choice",
        expect: "what others expect to see keeps rewarding the present way",
      };
    var EP = [];
    /* 1. the pattern */
    EP.push(
      (KEYS.length >= 2
        ? "Here the goal does not meet one argument against it but several private reasons, held one " + unit + " at a time: " + gsmMeanList(KEYS.slice(0, 4).map(function (k) { return SH[k]; })) + "."
        : "Here the goal meets one reason above the others, held one " + unit + " at a time: " + SH[KEYS[0]] + ".") +
        (HELP.length
          ? " Alongside them, others are already doing the work" + (walk ? ", some of them " + walk + " from those who hold back" : "") + "."
          : " No one on the map is yet doing the work, so nothing nearby shows what it would look like."),
    );
    /* 2. what keeps it going */
    var M = KEYS.slice(0, 4).map(function (k) {
      return MC[k];
    });
    EP.push(
      (saidInfo ? "A lack of information is among the reasons you gave, but the notes point more strongly elsewhere: " : "What keeps it going is that ") +
        (M.length > 2 ? M.slice(0, -1).join("; ") + "; and " + M[M.length - 1] : M.join("; and ")) +
        ". Each of these is reasonable " + inside + ", and together they make waiting the sensible choice for each one, which is how a whole place stays as it is without anyone deciding it should.",
    );
    /* 3. what it protects */
    var K = KEYS[0],
      INV = {
        look: ("household" === unit ? "home as people know it: a place that looks the way they chose it for" : "the place as people know it: the way it looks, and what that means to them") + (HAS("risk") ? ", and that feels safe enough as it is" : ""),
        risk: "the sense that home is safe enough as it is",
        cost: "each " + unit + "'s own means, and the right to decide what they are spent on",
        worth: "the judgment that effort should go where it makes a difference",
        trad: "a way of doing things that has stood for a long time and that people take for granted",
        fear: "safety from blame: no one wants to answer for the one time things go wrong",
        expect: "what others expect to see, and the standing of those who deliver it",
      }[K],
      WHY = {
        look: ("household" === unit ? "People chose the place for what it is" : "People value the place for what it is") + ", and a change that asks them to give some of that up" + (HAS("risk") ? ", against a danger they do not feel," : "") + " asks a great deal.",
        risk: "No one can live braced for every danger, and a risk that has never touched them is easy to set aside.",
        cost: "Money spent on the work is money not spent on something they can see.",
        worth: "No one wants to spend effort on something that may not count.",
        trad: "Without it, people would have to rebuild, all at once, what they rely on without thinking.",
        fear: "Without it, each person would carry the risk of every failure alone.",
        expect: "Without it, those in charge would answer for every outcome that looks like failure.",
      }[K];
    EP.push("Underneath, one thing stays the same. The system protects " + INV + ". That is not unreasonable. " + WHY);
    /* 4. what would have to change, and what the user's own design already reaches */
    var DS = A.slice(4, 7)
        .concat(
          PM.filter(function (t) {
            return t && t[0] >= 5;
          }).map(function (t) {
            return t[3] || "";
          }),
        )
        .join(" \n ")
        .toLowerCase(),
      LV = [],
      NO = [];
    function lever(on, re, txt, gap) {
      on && (re.test(DS) ? LV.push(txt) : NO.push(gap));
    }
    lever(HAS("risk"), /percept|frame|framing|aware|educat|\bshow|\bsee\b/, "changing how people see where the risk is", "how people will come to see the risk for themselves");
    lever(HAS("look"), /aesthetic|understood|landscape|\blook|beaut|\bplace\b/, "changing how the place is understood once the work is done", "how the work can keep the place looking like itself");
    lever(HAS("cost"), /market|incentiv|fund|grant|financ|\bcost|service|provider/, "building the services and support that make the work possible", "who helps carry the cost and the labor");
    lever(HAS("worth"), /already|reinforc|demonstrat|evidence|example|neighbo/, "letting the work already being done show what it changes", "how people will see the work make a difference");
    lever(HAS("trad"), /narrativ|frame|story|stories|campaign|educat|messag|perspective/, "giving people a new story to see the work through", "what new story replaces the one people see the work through now");
    lever(HAS("fear"), /liabil|\brisk|safe|protect|insur|small|experiment|pilot/, "lowering the risk people carry when they try it", "who carries the risk, and the blame, when something goes wrong");
    lever(HAS("expect"), /media|public|messag|campaign|communit|narrativ|frame/, "changing what others expect to see", "what others will expect instead");
    lever(HELP.length > 0, /reinforc|already|existing|neighbo|\bask\b|peer/, "building on the people already doing it", "how the people already doing it are drawn in");
    var GIVE = {
      look: "work that keeps the place looking like itself",
      risk: "a risk people can see for themselves",
      cost: "help with the cost and the labor",
      worth: "proof, close to home, that the work counts",
      trad: "a new way people can come to take for granted",
      fear: "a way to try it that does not leave people to carry the blame alone",
      expect: "results others can see and come to expect",
    };
    EP.push(
      "Change succeeds here not when people are argued out of their reasons but when the work stops costing them what they protect: " +
        gsmMeanList(KEYS.slice(0, 3).map(function (k) { return GIVE[k]; })) +
        "." +
        (LV.length ? " Your own answers already reach part of this: " + gsmMeanList(LV) + "." : "") +
        (NO.length ? " Nothing you would design yet answers " + gsmMeanList(NO) + "." : "") +
        (saidInfo ? " Information on its own will not do it, because each of these reasons answers a real cost, not a gap in what people know." : ""),
    );
    /* the story in greater detail: the seven moves */
    var S = [];
    S.push("Where the goal reaches the people it depends on, it meets " + emoL + ", and each comes with a reason of its own rather than a shared position.");
    S.push(
      HAS("cost") || HAS("look")
        ? "It emerges because the goal asks each " + unit + " to change what is " + its + " own, at " + its + " own cost" + (HAS("risk") ? ", against a danger " + ("its" === its ? "it does" : "they do") + " not feel" : "") + ", so every reason to wait is a private one that no one has to argue out with anyone else."
        : HAS("risk")
          ? "It emerges where the danger is not felt, so the work answers a question no one is asking."
          : HAS("trad")
            ? "It emerges where long habit has made the present way seem like the only sensible one, so the change has to argue against what people take for granted."
            : HAS("fear")
              ? "It emerges where fear of what happens when something goes wrong makes holding back the safer choice."
              : "It emerges where what others expect to see keeps rewarding the present way.",
    );
    S.push(
      HAS("worth") && !HAS("risk")
        ? "What keeps recreating it is that the benefit is hard to see before it arrives, so the work has to be paid for on faith, while waiting asks for nothing."
        : HAS("risk")
        ? "What keeps recreating it is that waiting shows no cost. Until something goes wrong, the place that did nothing looks no different from the one that did the work, so " + quiet + " confirms the choice to wait."
        : HAS("look")
          ? "What keeps recreating it is that the work shows and its benefit does not: the change to the place is seen at once, while what it prevents may never be seen at all."
          : "What keeps recreating it is that each round of the change arrives without changing the reasons it meets, so each round is met the way the last one was.",
    );
    S.push("It reveals that the resistance is less a stand against the goal than a set of reasonable private calculations, and that the goal so far gives people little to put on the other side of them.");
    var NOT = [];
    HAS("cost") && NOT.push("lower the cost");
    HAS("look") && NOT.push("keep the place looking as it does");
    HAS("worth") && NOT.push("prove the work will count");
    S.push(
      NOT.length
        ? "It matters because reasons like these do not give way to information alone. Telling people " + (HAS("risk") ? "the risk is real" : "the change is worth it") + " does not " + gsmMeanList(NOT).replace(/, and /, ", or ").replace(/^([^,]*) and /, "$1 or ") + "."
        : "It matters because reasons like these are held one " + unit + " at a time, so no single conversation can settle them.",
    );
    S.push(
      hasDef
        ? "Left as it is, the defiance stays where it is: those least interested have the least reason to look again, and " + quiet + " gives them one more." + (hasAgg ? " The aggression can harden into defiance too, the furthest of the emotions from taking up the work." : "")
        : hasAgg
          ? "Left as it is, aggression can harden into defiance, the furthest of the emotions from taking up the work."
          : hasDis
            ? "Left as it is, distrust spreads from the work to those asking for it, and whatever comes next inherits that distrust before it begins."
            : "Left as it is, indifference can settle in for good: not opposed, and not moving either.",
    );
    S.push(
      hasInd
        ? "For it to lose its influence, people do not have to move straight to acceptance. The nearer step is indifference: some already hold it, unsure the work helps but not set against it, and most change passes through there."
        : "For it to lose its influence, indifference has to be reached first. No one holding back is there yet, so a move straight to acceptance would take the most energy.",
    );
    HELP.length &&
      S.push(
        "Acceptance is already close at hand: " +
          (walk ? "some of the people already doing the work are " + walk + " from those who hold back, and " : "people are already doing the work, and ") +
          "what they did, seen up close, answers " +
          (HAS("worth") ? "the doubt about whether it is worth it" : "the reasons to wait") +
          " better than anything said about it.",
      );
    var NB = HIN.concat(HELP);
    var box = document.createElement("div");
    box.className = "stories";
    box.innerHTML =
      '<p class="stsn">Your workbook holds one story, read from your place map. It shows what the system is doing and why.</p>' +
      '<div class="csl" style="margin-top:10px">YOUR STORY, SUMMARIZED</div>' +
      '<div class="evo">' +
      EP.map(function (p) {
        return "<p>" + Gt(p) + "</p>";
      }).join("") +
      '</div><details class="more evst"><summary>Your story in greater detail</summary>' +
      '<div class="story1"><div class="s1h">STORY 1 · ON THE PLACE MAP</div><div class="s1p"><p>' +
      Gt(S.slice(0, 3).join(" ")) +
      "</p><p>" +
      Gt(S.slice(3).join(" ")) +
      '</p></div><details class="more"><summary>The notes behind this reading</summary><div class="srev">' +
      NB.map(function (p) {
        return "<div>" + gsmStRef(p) + " <i>" + E[p.em] + "</i>: " + gsmStQ(p).replace(/ \(<a[^)]*<\/a>\)$/, "") + "</div>";
      }).join("") +
      "</div></details></div></details>";
    /* AT A GLANCE says what the system is doing */
    try {
      var groot = mt.closest("#gsm"),
        gp = groot && groot.querySelector(".glance");
      if (gp && !gp.querySelector(".glsys")) {
        var grow = document.createElement("div");
        grow.className = "gl glsys";
        grow.innerHTML = '<span class="gk">WHAT THE SYSTEM IS DOING</span><span class="gt"></span>';
        grow.querySelector(".gt").textContent =
          "The system isn’t resisting the change itself. It is protecting " + INV + "." +
          (KEYS.length >= 2 ? " The protection takes several forms at once: " + gsmMeanList(KEYS.slice(0, 4).map(function (k) { return SH[k]; })) + "." : "") +
          " It gives way only where the change provides the same thing another way.";
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
