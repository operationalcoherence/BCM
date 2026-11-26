# v292: put back the A LOOP BETWEEN GROUPS and TWO WAYS OF RUNNING questions (his "We just added
# these! Nooko", 25 Nov 2026 21:41). v291 removed them by mistake: they are features he asked for,
# not questions covering the engine's limits. The rest of v291 stays.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
rep('''          " is the other side's evidence, so it grows on its own. Whose it is decides whether this is a loop: worth finding out before acting on either side."''',
    '''          " is the other side's evidence, so it grows on its own. Does the " + ey + " in " + gsmStRef(y) + " come from " + nm(b) + "?" +
          '<div class="emo"><button type="button" class="ech" onclick="gsmAskLoop(\\'' + ask + '\\',\\'y\\')">Yes</button><button type="button" class="ech" onclick="gsmAskLoop(\\'' + ask + "','n')\\">No</button></div>"''')
rep('''        "</p><p>If both are meant to stay, the goal is not to replace one way with the other. It is to move between the two as conditions change.</p>";''',
    '''        "</p><p>If both are meant to stay, the goal is not to replace one way with the other. It is to move between the two as conditions change.</p>" +
        "<p>Is the goal two ways of running, each for its own conditions?</p>" +
        '<div class="emo"><button type="button" class="ech" onclick="gsmAskMode(\\'' +
        key +
        "','y')\\">Yes</button><button type=\\"button\\" class=\\"ech\\" onclick=\\"gsmAskMode('" +
        key +
        "','n')\\">No</button></div>";''')
rep('t.textContent = "v291"', 't.textContent = "v292"')
open(p, 'w', encoding='utf-8').write(s)
print('v292 applied')
