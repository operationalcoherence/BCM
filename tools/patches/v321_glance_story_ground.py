"""v321: Project at a glance opens first, with the ground in 3D and the story (Gregory, 26 Nov 20:16: "it should open on
"project at a glance" with graphics, and include a story like the one in Patttern Analysis").
- The dashboard opens on Project at a glance.
- At the top of it: AT A GLANCE, THE GROUND THEY MAKE TOGETHER (THE BARE LANDSCAPE in 3D, with WHAT THE GROUND SAYS),
  and THE STORY SO FAR, all read from everyone's workbooks together (or one voice's, with the voice filter).
- How: the dashboard opens the combined copy in a frame of its own (srcdoc) that keeps everything in memory
  (window.GSM_PEEK: Storage is swapped for a plain object in that frame only). Nothing there is saved or sent, and the
  lead's own workbook on this device is never touched. Pattern Analysis runs there exactly as it does on the page, so
  the story and the ground are the engine's own; the dashboard copies AT A GLANCE, the ground's reading and the story
  out, and shows only the 3D ground of the frame.
- The frame is read once, and again only on Read again or a change of voice, so the 3D doesn't reload every minute.
  The dashboard keeps the frame in place when it redraws (moving a frame reloads it).
Run from the repository root:  python3 tools/patches/v321_glance_story_ground.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

rep('t && (t.textContent = "v320");', 't && (t.textContent = "v321");')

# 1. the in-memory mode, before anything reads storage
rep('''/* Bear Canyon Method v150 - boot: fonts, styles and page, then the workbook. */
''', '''/* Bear Canyon Method v150 - boot: fonts, styles and page, then the workbook. */
/* v321: the lead's dashboard reads everyone together in a frame of its own (window.GSM_PEEK, set by the dashboard).
   In that frame every read and write of storage goes to a plain object, so nothing is saved on the device and the
   lead's own workbook is never touched. */
!(function () {
  var P = window.GSM_PEEK;
  if (!P) return;
  try {
    var mem = {},
      SP = Storage.prototype,
      has = function (k) {
        return Object.prototype.hasOwnProperty.call(mem, k);
      };
    Object.keys(P.store || {}).forEach(function (k) {
      mem[k] = String(P.store[k]);
    });
    SP.getItem = function (k) {
      return has(String(k)) ? mem[String(k)] : null;
    };
    SP.setItem = function (k, v) {
      mem[String(k)] = String(v);
    };
    SP.removeItem = function (k) {
      delete mem[String(k)];
    };
    SP.clear = function () {
      mem = {};
    };
    SP.key = function (i) {
      return Object.keys(mem)[i] || null;
    };
    /* the frame is never scrolled: THE BARE LANDSCAPE is built at once, and no other map is built at all */
    try {
      window.IntersectionObserver = function (cb) {
        this.observe = function (el) {
          var p = el;
          while (p && !(p.classList && p.classList.contains("gtbare"))) p = p.parentNode;
          p &&
            setTimeout(function () {
              cb([{ isIntersecting: true, target: el }]);
            }, 0);
        };
        this.unobserve = this.disconnect = function () {};
        this.takeRecords = function () {
          return [];
        };
      };
    } catch (e) {}
    window.gsmRead = { pid: P.pid || "peek", meta: P.meta || {} };
    window.gsmPeek = true;
  } catch (e) {
    window.gsmPeekFail = true;
  }
})();
''')

# 2. opens on Project at a glance; tab order follows
rep('dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "", tab: "people", who: "", more: {} };',
    'dash = { pid: "", rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "", tab: "glance", who: "", more: {} };')
rep('if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "", tab: "people", who: "", more: {} };',
    'if (dash.pid !== p.id) dash = { pid: p.id, rows: [], at: 0, busy: false, err: "", msg: "", open: "", ask: "", taking: true, voice: "", tab: "glance", who: "", more: {} };')
rep('''      [["people", "People"], ["glance", "Project at a glance"]]
        .map(function (t) {
          var on = (dash.tab || "people") === t[0];''', '''      [["glance", "Project at a glance"], ["people", "People"]]
        .map(function (t) {
          var on = (dash.tab || "glance") === t[0];''')
rep('''    else if (k === "dtab") ((dash.tab = b.getAttribute("data-v") || "people"), (dash.who = ""), (dash.ask = ""), drawDash());''',
    '''    else if (k === "dtab") ((dash.tab = b.getAttribute("data-v") || "glance"), (dash.who = ""), (dash.ask = ""), drawDash());
    else if (k === "pkre") ((peek.want = 1), drawDash());''')

# 3. the glance tab: filter, then the frame's slot, then the rest
rep('''    h +=
      '<div class="lrow"><button type="button" class="btn" style="width:auto;flex:none" data-l="rtog">See ' + (dash.voice ? esc(dash.voice) + " together" : "everyone’s ground together") + " →</button></div>" +''',
    '''    h +=
      "</div>" +
      (nq === 7
        ? '<div id="gsm-lpeek-slot"></div>'
        : '<div class="lh" style="margin:8px 0 0">The ground in 3D and the story show here once each of the seven questions has an answer from someone; so far ' + nq + " of 7 do.</div>") +
      '<div class="rdg rdg2">' +
      '<div class="lrow"><button type="button" class="btn alt" style="width:auto;flex:none" data-l="rtog">Open ' + (dash.voice ? esc(dash.voice) + " together" : "everyone’s workbooks together") + " in full →</button></div>" +''')

# 4. drawDash keeps the frame where it is
rep('''  function drawDash() {
    var el = box && document.getElementById("gsm-ldash");
    if (el) el.outerHTML = dashHtml();
  }''', '''  function drawDash() {
    var el = box && document.getElementById("gsm-ldash");
    if (!el) return;
    var t = document.createElement("div");
    t.innerHTML = dashHtml();
    var N = t.firstElementChild,
      K = peek.el && peek.pid === dash.pid ? peek.el : null,
      slot = N.querySelector("#gsm-lpeek-slot");
    if (K && K.parentNode === el) {
      /* the frame stays put: everything else is swapped around it */
      [].slice.call(el.childNodes).forEach(function (c) {
        c !== K && el.removeChild(c);
      });
      var before = true;
      [].slice.call(N.childNodes).forEach(function (c) {
        if (c === slot) return void (before = false);
        before ? el.insertBefore(c, K) : el.appendChild(c);
      });
      K.style.display = slot ? "" : "none";
    } else {
      el.parentNode.replaceChild(N, el);
      if (K) {
        slot ? slot.parentNode.replaceChild(K, slot) : N.appendChild(K);
        K.style.display = slot ? "" : "none";
        /* a frame that moves reloads, so it must be read again */
        peek.want = 1;
      }
    }
    slot && peekRun();
  }
  /* v321: AT A GLANCE, the ground in 3D and the story, read from the combined copy in a frame of its own. */
  var peek = { el: null, pid: "", voice: null, want: 0, at: 0, n: 0, timer: 0 };
  function peekSrc() {
    var sc = document.querySelector('script[src*="gsm-preview.js"]');
    return sc ? sc.src : "";
  }
  function peekRun() {
    var p = st.cur,
      slot = document.getElementById("gsm-lpeek-slot"),
      rows = vrows();
    if (!p || !rows.length) return;
    var fresh = !peek.el || peek.pid !== dash.pid || peek.voice !== (dash.voice || "") || peek.want;
    if (!fresh) return;
    var src = peekSrc();
    if (!src) return;
    var K = peek.el;
    if (!K || peek.pid !== dash.pid) {
      K = document.createElement("div");
      K.id = "gsm-lpeek";
      slot && slot.parentNode.replaceChild(K, slot);
      K.addEventListener("click", function (e) {
        var g = e.target.closest(".gl");
        if (g && K.contains(g)) {
          var x = g.nextElementSibling;
          x && x.classList.contains("gx") && x.classList.toggle("on");
        }
      });
    } else if (slot) slot.parentNode.replaceChild(K, slot);
    peek.el = K;
    peek.pid = dash.pid;
    peek.voice = dash.voice || "";
    peek.want = 0;
    peek.n = rows.length;
    clearInterval(peek.timer);
    var priv = {};
    ["solo", "join", "lead", "live"].forEach(function (k) {
      priv[k] = { v: "9999", at: null };
    });
    window.__gsmPeekData = {
      pid: p.id,
      meta: { name: p.name, voice: dash.voice || "", n: rows.length, at: Date.now() },
      store: { "groundsmith-web-v1": JSON.stringify(together(rows)), "groundsmith-web-welcomed": "1", "groundsmith-web-privacy": JSON.stringify(priv) },
    };
    K.innerHTML =
      '<div class="pkst lh" role="status">Reading ' + (dash.voice ? esc(dash.voice) : "everyone") + "’s workbooks together…</div>" +
      '<div class="pkgl"></div><div class="rh pkgh" style="display:none">THE GROUND THEY MAKE TOGETHER</div>' +
      '<iframe class="pkfr" title="The ground they make together, in 3D" style="display:block;width:100%;height:0;border:0" tabindex="0"></iframe>' +
      '<div class="pkstory"></div>';
    var fr = K.querySelector("iframe");
    fr.srcdoc =
      '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0;background:#fff}</style></head><body><div id="gsm-mount"></div>' +
      "<script>window.GSM_ESRI_KEY=" + JSON.stringify(String(window.GSM_ESRI_KEY || "")).replace(/</g, "\\\\u003c") + ";window.GSM_PEEK=parent.__gsmPeekData;<\\/script>" +
      '<script src="' + esc(src) + '"><\\/script></body></html>';
    var tries = 0;
    peek.timer = setInterval(function () {
      tries++;
      if (!K.isConnected) return void clearInterval(peek.timer);
      var d = null;
      try {
        d = fr.contentDocument;
      } catch (e) {}
      var pat = d && d.getElementById("gsm-pat"),
        gl = pat && pat.querySelector(".glance"),
        bare = pat && pat.querySelector(".gtbare"),
        rel = bare && bare.querySelector(".grel"),
        cv = rel && rel.querySelector("canvas"),
        story = pat && pat.querySelector(".storylead details");
      if (!(gl && (cv || tries > 40) && (story || tries > 40)) && tries < 80) return;
      clearInterval(peek.timer);
      peekShow(K, fr, d, gl, bare, rel, story);
    }, 500);
  }
  function peekShow(K, fr, d, gl, bare, rel, story) {
    var st0 = K.querySelector(".pkst"),
      when = new Date().toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
    if (!gl) {
      st0.innerHTML = "The ground and the story couldn’t be read here. Open everyone’s workbooks together in full to see them. " + '<button type="button" class="lnk sm" data-l="pkre">Try again</button>';
      fr.style.display = "none";
      return;
    }
    st0.innerHTML = "Read from " + peek.n + (peek.n === 1 ? " workbook" : " workbooks") + (peek.voice ? " (" + esc(peek.voice) + ")" : "") + " at " + esc(when) + '. <button type="button" class="lnk sm" data-l="pkre">Read again</button>';
    /* AT A GLANCE, as Pattern Analysis has it */
    var g = gl.cloneNode(true);
    g.querySelectorAll("[id]").forEach(function (x) { x.removeAttribute("id"); });
    K.querySelector(".pkgl").appendChild(g);
    /* the 3D ground and its own reading (WHAT THIS GROUND IS DOING, which answers taps on the ground): only they show
       in the frame */
    var relBox = rel && rel.parentNode,
      box = bare;
    if (relBox && rel.querySelector("canvas")) {
      [].forEach.call(bare.children, function (c) {
        c !== relBox && c !== bare.lastElementChild && (c.style.display = "none");
      });
      for (var n = box; n && n !== d.body; n = n.parentElement)
        n.parentElement &&
          [].forEach.call(n.parentElement.children, function (c) {
            c !== n && !/^(SCRIPT|STYLE|LINK)$/.test(c.tagName) && (c.style.display = "none");
          });
      var gs = d.getElementById("gsm");
      gs && (gs.style.padding = "0", gs.style.maxWidth = "none");
      var fit = function () {
        fr.style.height = Math.ceil(box.getBoundingClientRect().height) + 4 + "px";
      };
      fit();
      try {
        new fr.contentWindow.ResizeObserver(fit).observe(box);
      } catch (e) {
        setTimeout(fit, 1500);
      }
      K.querySelector(".pkgh").style.display = "";
    } else fr.style.display = "none";
    /* the story */
    if (story) {
      var sc = story.cloneNode(true);
      sc.setAttribute("open", "");
      var sm = sc.querySelector("summary");
      sm && (sm.textContent = "THE STORY SO FAR");
      sc.querySelectorAll("[id]").forEach(function (x) { x.removeAttribute("id"); });
      K.querySelector(".pkstory").appendChild(sc);
    }
  }''')

# styles
rep('''    "#gsm-lead .evr{margin:8px 0}''', '''    "#gsm-lead #gsm-lpeek{margin:8px 0 4px}#gsm-lead #gsm-lpeek .pkst{margin:0 0 6px}#gsm-lead #gsm-lpeek .glance{margin:6px 0 10px}" +
    "#gsm-lead #gsm-lpeek .rh{font-weight:700;letter-spacing:.12em;font-size:11.5px;margin:14px 0 6px}#gsm-lead #gsm-lpeek .pkfr{border:1px solid #ddd!important}" +
    "#gsm-lead #gsm-lpeek .pkstory{margin:14px 0 0}#gsm-lead #gsm-lpeek .pkstory details{margin-bottom:8px}" +
    "#gsm-lead .rdg2{border-top:0;margin-top:6px;padding-top:0}" +
    "#gsm-lead .evr{margin:8px 0}''')

open(P, 'w', encoding='utf-8').write(s)
print('v321 patched')
