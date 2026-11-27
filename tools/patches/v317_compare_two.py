"""v317: F8 step 7, part 1 - COMPARE TWO under READING THEM TOGETHER. The lead picks two people, or two voices,
and sees where those two split, where they agree, what only one of them names, and how each leans.
Shown only when there are three or more people, or two or more voices (with two people, WHERE THEY SPLIT and
WHERE THEY AGREE already are the comparison). Phrases of two or three words only, as in v313. No extra reads.
Run from the repository root:  python3 tools/patches/v317_compare_two.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:80]); s = s.replace(old, new)

rep('t && (t.textContent = "v316");', 't && (t.textContent = "v317");')

# a group (a voice) holds several people under one id: never pair a person with someone in their own group
rep('          if (X[i].r === X[j].r) continue;', '          if (X[i].r.uid === X[j].r.uid) continue;')

# agreeItem can say "Both" / "Both voices" in a comparison
rep('''  function agreeItem(a) {
    var who = a.xs.length + " people",''', '''  function agreeItem(a, both) {
    var who = typeof both === "string" ? both : a.xs.length + " people",''')

rep('''  /* one combined copy of everyone's work (in the voice chosen), in the workbook's own format */''',
'''  /* v317: COMPARE TWO. Options are each person, and each voice when no voice filter is on. A voice is its people,
     each copied under the voice's id, so shared() treats the voice as one side. */
  function cmpOpts(rows) {
    var O = rows.map(function (r) {
      return { id: "p:" + r.uid, label: r.name + (r.voice ? " · " + r.voice : ""), name: r.name, who: r.name, rs: [r] };
    });
    if (!dash.voice) {
      var V = {};
      rows.forEach(function (r) {
        var v = r.voice || "No voice";
        (V[v] = V[v] || []).push(r);
      });
      var vk = Object.keys(V);
      vk.length >= 2 &&
        vk.forEach(function (v) {
          O.push({ id: "v:" + v, label: "Voice: " + v + " (" + V[v].length + (V[v].length === 1 ? " person)" : " people)"), name: v, who: "the " + v + " voice", voice: true, rs: V[v] });
        });
    }
    return O;
  }
  function cmpSide(o) {
    return o.rs.map(function (r) {
      return Object.assign({}, r, { uid: o.id });
    });
  }
  function only(A, B) {
    var goal = phrases(st.cur && st.cur.goal),
      vn = phrases(((st.cur && st.cur.voices) || []).concat(dash.rows.map(function (r) { return r.voice; })).join(". ")),
      inB = {},
      by = {};
    B.forEach(function (r) {
      spots(r).forEach(function (x) {
        Object.keys(phrases(x.t)).forEach(function (k) { inB[k] = 1; });
      });
    });
    A.forEach(function (r) {
      spots(r).forEach(function (x, i) {
        Object.keys(phrases(x.t)).forEach(function (k) {
          if (inB[k] || goal[k] || vn[k]) return;
          var b = by[k] || (by[k] = { k: k, w: phrases(x.t)[k], xs: [] });
          b.xs.some(function (y) { return y.t === x.t; }) || b.xs.push(x);
        });
      });
    });
    var L = Object.keys(by)
      .map(function (k) { return by[k]; })
      .filter(function (b) { return b.xs.length >= 2; });
    L = L.filter(function (b) {
      return !L.some(function (o) {
        return o !== b && o.k.length > b.k.length && (" " + o.k + " ").indexOf(" " + b.k + " ") >= 0 && o.xs.length >= b.xs.length;
      });
    });
    return L.sort(function (a, c) { return c.xs.length - a.xs.length || c.k.length - a.k.length; });
  }
  function leanOf(o) {
    var c = [0, 0, 0, 0, 0],
      n = 0,
      sd = { help: 0, hinder: 0 };
    o.rs.forEach(function (r) {
      spots(r).forEach(function (x) {
        x.q < 0 && x.e != null && (c[x.e]++, n++);
        x.q < 0 && x.side && sd[x.side]++;
      });
    });
    var order = [1, 3, 2, 0, 4],
      top = n ? c.indexOf(Math.max.apply(null, c)) : -1,
      h = '<div class="evr"><b>' + esc(o.name) + '</b> <span class="lh">' + sd.help + " on the help side, " + sd.hinder + " on the hinder side" + (n ? "; mostly " + EMOS[top][0].toLowerCase() : "; no emotion marked yet") + "</span>";
    n &&
      (h += '<div class="ebar" aria-hidden="true">' + order.map(function (i) { return c[i] ? '<span style="width:' + (100 * c[i]) / n + "%;background:" + EMOS[i][1] + '"></span>' : ""; }).join("") + "</div>" +
        '<div class="lh">' + order.filter(function (i) { return c[i]; }).map(function (i) { return EMOS[i][0] + " " + Math.round((100 * c[i]) / n) + "%"; }).join(", ") + "</div>");
    return { h: h + "</div>", top: top, help: sd.help, hinder: sd.hinder };
  }
  function cmpHtml(rows) {
    var O = cmpOpts(rows);
    if (rows.length < 3) return "";
    var ids = O.map(function (o) { return o.id; });
    ids.indexOf(dash.ca) < 0 && (dash.ca = ids[0]);
    (ids.indexOf(dash.cb) < 0 || dash.cb === dash.ca) && (dash.cb = ids.filter(function (i) { return i !== dash.ca; })[0]);
    var sel = function (k, v) {
        return '<select data-l="cmp" data-k="' + k + '" aria-label="' + (k === "ca" ? "First to compare" : "Second to compare") + '">' +
          O.map(function (o) { return '<option value="' + esc(o.id) + '"' + (o.id === v ? " selected" : "") + ">" + esc(o.label) + "</option>"; }).join("") + "</select>";
      },
      a = O[ids.indexOf(dash.ca)],
      b = O[ids.indexOf(dash.cb)],
      h = '<div class="rh">COMPARE TWO</div><div class="crow">' + sel("ca", dash.ca) + "<span>with</span>" + sel("cb", dash.cb) + "</div>";
    if (a.id === b.id) return h + '<div class="lh">Choose two different ones.</div>';
    var au = {};
    a.rs.forEach(function (r) { au[r.uid] = 1; });
    if (b.rs.some(function (r) { return au[r.uid]; }))
      return h + '<div class="lh">' + esc((a.voice ? b.name : a.name) + " answers as " + (a.voice ? a.name : b.name) + ". Choose two that don’t share anyone.") + "</div>";
    var A = cmpSide(a),
      B = cmpSide(b),
      S = shared(A.concat(B)),
      both = a.voice && b.voice ? "Both voices" : "Both",
      oa = only(A, B),
      ob = only(B, A),
      la = leanOf(a),
      lb = leanOf(b),
      cap = function (t) { return t.charAt(0).toUpperCase() + t.slice(1); },
      A1 = cap(a.who),
      gist =
        S.split.length || S.agree.length
          ? (S.split.length ? "they read " + S.split.length + (S.split.length === 1 ? " thing" : " things") + " two ways" : "they read nothing two ways") +
            (S.agree.length ? " and share " + S.agree.length + "." : ", and share nothing yet.")
          : "they don’t yet name the same things.";
    var lean =
      la.top >= 0 && lb.top >= 0
        ? la.top === lb.top
          ? " Both lean toward " + EMOS[la.top][0].toLowerCase() + "."
          : FAR(la.top, lb.top)
            ? " " + A1 + " leans toward " + EMOS[la.top][0].toLowerCase() + " and " + b.who + " toward " + EMOS[lb.top][0].toLowerCase() + ", with no ridge of indifference between them: bringing them together takes real effort."
            : " " + A1 + " leans toward " + EMOS[la.top][0].toLowerCase() + " and " + b.who + " toward " + EMOS[lb.top][0].toLowerCase() + "."
        : "";
    h += '<div class="rm">' + esc(A1 + " and " + b.who + ": " + gist + lean) + "</div>";
    S.split.length && (h += '<div class="rsh">WHERE THE TWO SPLIT</div>' + S.split.slice(0, 3).map(splitItem).join("") + (S.split.length > 3 ? '<div class="lh">…and ' + (S.split.length - 3) + " more.</div>" : ""));
    S.agree.length && (h += '<div class="rsh">WHERE THE TWO AGREE</div>' + S.agree.slice(0, 3).map(function (x) { return agreeItem(x, both); }).join("") + (S.agree.length > 3 ? '<div class="lh">…and ' + (S.agree.length - 3) + " more.</div>" : ""));
    var onlyItem = function (x, me, other) {
      return '<div class="rit"><div class="rm">' + esc("Only " + me + " names “" + x.w + "”, in " + x.xs.length + " places. " + cap(other) + " never does.") + "</div>" + x.xs.slice(0, 2).map(said).join("") + "</div>";
    };
    (oa.length || ob.length) &&
      (h += '<div class="rsh">WHAT ONLY ONE OF THEM NAMES</div><div class="lh">Each sees part of the situation the other has not put into words. Here each could fill in the other’s picture.</div>' +
        oa.slice(0, 2).map(function (x) { return onlyItem(x, a.who, b.who); }).join("") +
        ob.slice(0, 2).map(function (x) { return onlyItem(x, b.who, a.who); }).join(""));
    !S.split.length && !S.agree.length && !oa.length && !ob.length && (h += '<div class="lh">They don’t yet name the same things, and neither names anything twice. There is not enough written to compare.</div>');
    h += '<div class="rsh">HOW EACH LEANS</div>' + la.h + lb.h;
    return h;
  }
  /* one combined copy of everyone's work (in the voice chosen), in the workbook's own format */''')

rep('''    h += '<div class="rh">WHAT NOBODY HAS SAID YET</div>' + gapsHtml(rows);
    return h + "</div>";''', '''    h += '<div class="rh">WHAT NOBODY HAS SAID YET</div>' + gapsHtml(rows);
    h += cmpHtml(rows);
    return h + "</div>";''')

rep('''    "#gsm-lead .evr{margin:8px 0}''', '''    "#gsm-lead .crow{display:flex;flex-wrap:wrap;gap:6px 8px;align-items:center;margin:6px 0 8px}#gsm-lead .crow select{font:inherit;font-size:13.5px;border:1px solid #999;border-radius:2px;padding:5px 7px;background:#fff;color:#222;max-width:100%;min-height:34px}" +
    "#gsm-lead .rdg .rsh{font-weight:700;letter-spacing:.1em;font-size:10.5px;color:#444;margin:12px 0 2px}#gsm-lead .rdg>.rm{margin:4px 0}" +
    "#gsm-lead .evr{margin:8px 0}''')

rep('''    box.addEventListener("click", onClick);
    box.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.target && e.target.id === "gsm-lpv") {''', '''    box.addEventListener("click", onClick);
    box.addEventListener("change", function (e) {
      var t = e.target;
      t && t.matches && t.matches('select[data-l="cmp"]') && ((dash[t.getAttribute("data-k")] = t.value), drawDash());
    });
    box.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.target && e.target.id === "gsm-lpv") {''')

open(P, 'w', encoding='utf-8').write(s)
print('ok')
