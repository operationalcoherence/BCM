# v294 part 3: the forms keep their article; a lever for a finding appears only when the story names it
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
rep('''            forms.replace(/^the /, "") +''', '''            forms +''')
rep('''    ["trad", "liv", "fear", "expect", "loop"].forEach(function (k) {
      HAS(k) && M.length < 4 && M.push(MC[k]);
    });''', '''    var MK = {};
    MK[K] = 1;
    ["trad", "liv", "fear", "expect", "loop"].forEach(function (k) {
      HAS(k) && M.length < 4 && (M.push(MC[k]), (MK[k] = 1));
    });''')
for k in ['trad', 'liv', 'fear', 'expect']:
    rep('lever(HAS("%s"),' % k, 'lever(MK.%s,' % k)
open(p, 'w', encoding='utf-8').write(s)
print('v294 part 3 applied')
