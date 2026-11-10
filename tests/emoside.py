"""How far a workbook's emotion marks and its help/hinder side say the same thing.
Reads the workbook's notes directly. Side: line map = above/below the ground line (y<118 helps);
place map = Q.3 notes help, Q.2 notes hinder (others have no side). Emotion: acceptance vs the rest.
  python3 -I emoside.py wb1.json wb2.json ...
"""
import json, sys, math, collections
E = ['aggression', 'acceptance', 'distrust', 'indifference', 'defiance']
def phi(a, b, c, d):  # 2x2: rows help/hinder, cols accept/other
    n = a + b + c + d
    den = math.sqrt((a + b) * (c + d) * (a + c) * (b + d))
    return None if den == 0 else (a * d - b * c) / den
for f in sys.argv[1:]:
    d = json.load(open(f))['data']
    rows = []
    for r in d.get('m', []):
        if r[5] is None: continue
        rows.append(('help' if r[2] < 118 else 'hinder', E[r[5]]))
    for r in d.get('p', {}).get('m', []):
        if r[5] is None or r[0] not in (2, 3): continue
        rows.append(('help' if r[0] == 3 else 'hinder', E[r[5]]))
    n = len(rows)
    ha = sum(1 for s, e in rows if s == 'help' and e == 'acceptance')
    ho = sum(1 for s, e in rows if s == 'help' and e != 'acceptance')
    ra = sum(1 for s, e in rows if s == 'hinder' and e == 'acceptance')
    ro = sum(1 for s, e in rows if s == 'hinder' and e != 'acceptance')
    agree = ha + ro
    p = phi(ha, ho, ra, ro)
    print('%-18s notes with emotion and a side: %2d | help: accept %d other %d | hinder: accept %d other %d | agree %s | phi %s'
          % (f, n, ha, ho, ra, ro, ('%d%%' % round(100 * agree / n)) if n else '-', ('%.2f' % p) if p is not None else 'n/a (too few or one-sided)'))
