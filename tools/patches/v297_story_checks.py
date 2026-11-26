# v297: two story checks, found running 11-13, 11-18, 11-20 and Broadview (his ask, 25 Nov 2026 22:38)
# 1. "Each side reads the other's response as proof" needed only any aggression on the help side.
#    In 11-18 that was aggression toward full suppression (a practice), not toward people who resist.
#    Now the help-side aggression has to be aimed at people: those who, supporters, opponents, ...
# 2. "livelihood" in "protect themselves, their livelihoods, and property from wildfire" is safety,
#    not jobs built on the present way. A livelihood that is being protected no longer counts.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
rep('''      helpAgg = Y.pts.filter(function (p) {
        return p.side > 0 && 0 === p.e;
      }).length,''', '''      helpAgg = Y.pts.filter(function (p) {
        return p.side > 0 && 0 === p.e && GSM_ATPEOPLE.test(String(p.txt || ""));
      }).length,''')
rep('''  function gsmHolds(texts) {
    var n = {};
    (texts || []).forEach(function (t) {
      var seen = {};
      GSM_HOLD.forEach(function (h) {
        h[1].test(String(t || "")) && !seen[h[0]] && ((seen[h[0]] = 1), (n[h[0]] = (n[h[0]] || 0) + 1));''', '''  /* v297: aggression aimed at people (those who resist), not at a practice */
  var GSM_ATPEOPLE = /\\b(?:those who|people who|anyone who|everyone who|supporters|opponents|resisters|the opposition|critics|skeptics|holdouts|defiant|distrustful)\\b/i;
  function gsmHolds(texts) {
    var n = {};
    (texts || []).forEach(function (t) {
      var seen = {};
      /* v297: a livelihood being protected (from fire, from harm) is safety, not jobs built on the present way */
      t = String(t || "").replace(/(\\b(?:protect|safeguard|defend|sav)\\w*\\b[^.;]{0,60}?)\\blivelihoods?\\b/gi, "$1");
      GSM_HOLD.forEach(function (h) {
        h[1].test(String(t || "")) && !seen[h[0]] && ((seen[h[0]] = 1), (n[h[0]] = (n[h[0]] || 0) + 1));''')
# 3. "catastrophic" (media coverage of catastrophic wildfires) is about how bad outcomes are, not fear of
#    blame; it no longer counts as fear. Fear still needs "fear", "liability", "deadly", "disaster", ...
rep('danger|deadly|\\bblame|disaster|worried|catastroph/i]', 'danger|deadly|\\bblame|disaster|worried/i]')
rep('t.textContent = "v296"', 't.textContent = "v297"')
open(p, 'w', encoding='utf-8').write(s)
print('v297 applied')
