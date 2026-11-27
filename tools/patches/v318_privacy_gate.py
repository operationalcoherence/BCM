"""v318: the privacy screen (F8 step 7, part 2). Nobody can work until they have pressed "I understand".
- Solo: a short screen the first time the page is opened (and again when the privacy text changes).
- Live (an invite link, or Lead a project): a fuller screen saying what is stored online, who can see it
  (the person, the lead, and the BCM administrator), and how to delete it.
- The screen covers the workbook and has no close button; Escape and clicks outside do nothing.
- Recorded on this device; on a live project also in the workbook record (data.privacy) and, for a lead,
  on the project record (privacy). No rule change: data is a map, and project fields are not restricted.
- The full privacy page opens from a Privacy link at the bottom of the workbook, any time.
Run from the repository root:  python3 tools/patches/v318_privacy_gate.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:80]); s = s.replace(old, new)

rep('t && (t.textContent = "v317");', 't && (t.textContent = "v318");')

# footer link
rep('''<a href="mailto:greg@operationalcoherence.com?subject=Bear%20Canyon%20Method%20feedback">Send feedback</a>''',
    '''<a href="mailto:greg@operationalcoherence.com?subject=Bear%20Canyon%20Method%20feedback">Send feedback</a><span class="fbsep"> \\u00b7 </span><a href="#" id="gsm-privlink">Privacy</a>''')

# the invited person's saves carry their acknowledgement
rep('''data: { fmt: "bcm-workbook", sv: (w && w.sv) || 2, json: s }, saved: M.serverTimestamp() };''',
    '''data: { fmt: "bcm-workbook", sv: (w && w.sv) || 2, json: s, privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("live") : null }, saved: M.serverTimestamp() };''')

# the lead's project record carries theirs (the project record only, not the invite key)
rep('''          return M.setDoc(ref, Object.assign({ lead: u.uid, key: key, created: M.serverTimestamp() }, shared))''',
    '''          return M.setDoc(ref, Object.assign({ lead: u.uid, key: key, created: M.serverTimestamp(), privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("live") : null }, shared))''')
rep('''        return M.updateDoc(M.doc(S.db, "projects", p.id), shared)''',
    '''        return M.updateDoc(M.doc(S.db, "projects", p.id), Object.assign({ privacy: window.gsmPrivacy ? window.gsmPrivacy.rec("live") : null }, shared))''')

# Lead a project: the live screen first
rep('''        btn.addEventListener("click", function () {
          box.classList.add("on");''', '''        btn.addEventListener("click", function () {
          if (window.gsmPrivacy && window.gsmPrivacy.need("live"))
            return window.gsmPrivacy.show("live", function () {
              btn.click();
            });
          box.classList.add("on");''')

s += r'''
/* v318: the privacy screen. Nobody works until they have pressed "I understand". Solo and live have their own
   text; each is asked again only when its version (a date) changes. Recorded in groundsmith-web-privacy. */
!(function () {
  var V = "2026-11-26",
    KEY = "groundsmith-web-privacy",
    ADMIN = /[?&#]bcmadmin\b/.test(location.search + location.hash),
    gate = null,
    lastFocus = null;
  function get() {
    try {
      return JSON.parse(localStorage.getItem(KEY) || "null") || {};
    } catch (e) {
      return {};
    }
  }
  function need(kind) {
    var r = get()[kind];
    return !(r && String(r.v) >= V);
  }
  function rec(kind) {
    var r = get()[kind];
    return r && r.v ? { v: String(r.v), at: r.at || null } : null;
  }
  function mark(kind) {
    var all = get();
    all[kind] = { v: V, at: new Date().toISOString() };
    try {
      localStorage.setItem(KEY, JSON.stringify(all));
    } catch (e) {}
  }
  var SERVICES =
      "Place search, maps, terrain, fonts, and code come from outside services: Esri, OpenStreetMap, Photon, Amazon Web Services, Google Fonts, cdnjs, and jsDelivr. They see your device’s internet address, as any website does, and a place search sends the words you type. None of them receive your goal, answers, or notes.",
    SOLO = [
      ["Your workbook stays on this device.", "Your goal, answers, notes, and maps are saved only in this browser. They are never sent to Operational Coherence or anyone else. We cannot see them."],
      ["You choose where it goes.", "Save workbook downloads a file. You decide whether to keep it, send it to someone, or combine it with theirs. Clearing your browser’s data erases the copy kept here, so save a file to keep your work."],
      ["Some outside services are used.", SERVICES],
      ["What we don’t do.", "This version has no accounts, collects no personal information, and keeps no record of your work."]
    ],
    LIVE = [
      ["This is a shared project. What you write is saved online.", "Your answers, notes, and maps are sent as you work and kept in Google Firebase, a database service, in the United States."],
      ["Who can see it.", "You, the project’s lead, and the BCM administrator at Operational Coherence, who can read project records and workbooks to look after the service. Nobody else."],
      ["What is kept.", "The name and voice you give, your answers, notes, and maps, and when you last saved. People answering need no account. A lead signs in with Google; the lead’s Google name (or email, if there is no name) is shown to the people they invite."],
      ["How long, and how to delete it.", "Until the lead deletes the project. You can delete your own workbook at any time with Delete my workbook, and Pause sharing stops sending. A lead can delete any workbook in their project."],
      ["Your own workbook stays apart.", "If you have a workbook of your own on this device, it is not sent. It stays on this device and comes back when you open the page without the invite link."],
      ["Some outside services are used.", SERVICES]
    ];
  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function list(L) {
    return L.map(function (x) {
      return "<p><b>" + esc(x[0]) + "</b> " + esc(x[1]) + "</p>";
    }).join("");
  }
  function full() {
    return (
      '<div class="pvh">THE BEAR CANYON METHOD · PRIVACY</div><div class="pvd">Last changed ' + esc(new Date(V + "T12:00:00").toLocaleDateString(undefined, { month: "long", day: "numeric", year: "numeric" })) + ".</div>" +
      '<div class="pvs">WORKING ON YOUR OWN</div>' + list(SOLO.slice(0, 2)) +
      '<div class="pvs">SHARED PROJECTS</div>' + list(LIVE.slice(0, 5)) + "<p>Don’t write anything in a shared project that you wouldn’t want the lead to read.</p>" +
      '<div class="pvs">OUTSIDE SERVICES</div><p>' + esc(SERVICES) + "</p>" +
      '<div class="pvs">WHAT WE DON’T DO</div><p>We don’t sell or share what you write, show advertising, or use what you write for anything but running BCM. Working on your own needs no account and keeps no record of your work.</p>' +
      '<div class="pvs">WHEN THIS CHANGES</div><p>You are asked to read it again before you can carry on.</p>' +
      '<div class="pvs">QUESTIONS</div><p>Write to <a href="mailto:greg@operationalcoherence.com">greg@operationalcoherence.com</a>.</p>'
    );
  }
  var CSS =
    "#gsm-priv{position:fixed;inset:0;z-index:2147483600;background:rgba(20,20,20,.55);display:flex;align-items:center;justify-content:center;padding:14px;box-sizing:border-box;font-family:'Questrial',sans-serif;color:#222}" +
    "#gsm-priv .pvb{background:#fff;border:1.5px solid #222;max-width:600px;width:100%;max-height:100%;overflow:auto;padding:18px 20px 16px;box-sizing:border-box;font-size:15px;line-height:1.5;-webkit-overflow-scrolling:touch}" +
    "#gsm-priv .pvh{font-weight:700;letter-spacing:.14em;font-size:12.5px;margin:0 0 4px}#gsm-priv .pvd{font-size:12.5px;color:#666;margin:0 0 10px}" +
    "#gsm-priv .pvs{font-weight:700;letter-spacing:.12em;font-size:11.5px;margin:16px 0 4px}#gsm-priv p{margin:0 0 10px}#gsm-priv a{color:#222}" +
    "#gsm-priv .pvr{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin:14px 0 0}" +
    "#gsm-priv .pvok{border:1px solid #111;background:#111;color:#fff;font:16px 'Questrial',sans-serif;padding:12px 22px;min-height:44px;cursor:pointer;letter-spacing:.03em}" +
    "#gsm-priv .pvlnk{background:none;border:0;padding:0;font:13.5px 'Questrial',sans-serif;color:#222;text-decoration:underline;cursor:pointer}" +
    "html.gsm-privon,html.gsm-privon body{overflow:hidden!important}@media print{#gsm-priv{display:none}}";
  function ensureCss() {
    if (document.getElementById("gsm-privcss")) return;
    var c = document.createElement("style");
    c.id = "gsm-privcss";
    c.textContent = CSS;
    document.head.appendChild(c);
  }
  function close() {
    if (!gate) return;
    gate.remove();
    gate = null;
    document.documentElement.classList.remove("gsm-privon");
    var w = document.getElementById("gsm");
    w && (w.inert = false);
    lastFocus && lastFocus.focus && lastFocus.focus();
  }
  function trap(e) {
    if (!gate) return;
    if (e.key === "Escape") return void (e.preventDefault(), e.stopPropagation());
    if (e.key !== "Tab") return;
    var f = gate.querySelectorAll("button,a[href]");
    if (!f.length) return;
    var a = f[0],
      z = f[f.length - 1];
    if (e.shiftKey && document.activeElement === a) (e.preventDefault(), z.focus());
    else if (!e.shiftKey && document.activeElement === z) (e.preventDefault(), a.focus());
    else if (!gate.contains(document.activeElement)) (e.preventDefault(), a.focus());
  }
  /* kind: "solo" or "live" asks for "I understand"; "full" is the full page, closed with Close */
  function show(kind, done) {
    ensureCss();
    close();
    lastFocus = document.activeElement;
    gate = document.createElement("div");
    gate.id = "gsm-priv";
    gate.setAttribute("role", "dialog");
    gate.setAttribute("aria-modal", "true");
    gate.setAttribute("aria-labelledby", "gsm-privh");
    var ask = kind !== "full",
      body = ask
        ? '<div class="pvh" id="gsm-privh">BEFORE YOU START: YOUR PRIVACY</div><div class="pvd">' +
          (kind === "live" ? "You are about to work in a shared project." : "Please read this before you work in the Bear Canyon Method.") +
          "</div>" + list(kind === "live" ? LIVE : SOLO) +
          (kind === "live" ? "<p>Don’t write anything you wouldn’t want the lead to read.</p>" : "") +
          '<div class="pvr"><button type="button" class="pvok" data-pv="ok">I understand</button><button type="button" class="pvlnk" data-pv="full">Read the full privacy page</button></div>'
        : full().replace('class="pvh"', 'class="pvh" id="gsm-privh"') + '<div class="pvr"><button type="button" class="pvok" data-pv="close">Close</button></div>';
    gate.innerHTML = '<div class="pvb">' + body + "</div>";
    gate.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("[data-pv]");
      if (!b) return;
      var k = b.getAttribute("data-pv");
      if (k === "ok") {
        mark(kind);
        close();
        done && done();
      } else if (k === "full") {
        var bx = gate.querySelector(".pvb");
        bx.innerHTML = full().replace('class="pvh"', 'class="pvh" id="gsm-privh"') + '<div class="pvr"><button type="button" class="pvok" data-pv="ok">I understand</button></div>';
        bx.scrollTop = 0;
        bx.querySelector("[data-pv=ok]").focus();
      } else if (k === "close") close();
    });
    document.body.appendChild(gate);
    document.documentElement.classList.add("gsm-privon");
    var w = document.getElementById("gsm");
    w && (w.inert = true);
    var ok = gate.querySelector(".pvok");
    ok && ok.focus();
  }
  document.addEventListener("keydown", trap, true);
  window.gsmPrivacy = { V: V, need: need, rec: rec, show: show };
  function start() {
    var w = document.getElementById("gsm");
    if (!w) return false;
    var a = document.getElementById("gsm-privlink");
    a &&
      a.addEventListener("click", function (e) {
        e.preventDefault();
        gate || show("full");
      });
    if (ADMIN) return true;
    var kind = window.gsmJoin || window.gsmRead ? "live" : "solo";
    need(kind) && show(kind);
    return true;
  }
  var n = 0,
    t = setInterval(function () {
      (start() || ++n > 120) && clearInterval(t);
    }, 100);
})();
'''

open(P, 'w', encoding='utf-8').write(s)
print('ok')
