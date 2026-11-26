# v294 part 4: "if it continues" names only an emotion the story holds (11-13 story 2 was told distrust
# spreads, with no distrust in it)
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
old = '''            [!0, "f-dis", (gw ? "d" : "Left as it is, d")'''
rep(old, '''            [0 === e0 || 0 === e1, "f-agg2", (gw ? "t" : "Left as it is, t") + "his aggression can harden into defiance too, and resistance this close to the goal is the last to give way."],
            [2 === e0 || 2 === e1 || (4 !== e0 && 0 !== e0 && 0 !== e1), "f-dis", (gw ? "d" : "Left as it is, d")''')
open(p, 'w', encoding='utf-8').write(s)
print('v294 part 4 applied')
