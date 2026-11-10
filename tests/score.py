"""Layer 1 slice 1: score the WHAT STANDS OUT findings and print the new
top seven beside today's. Nothing on screen changes; this is a measurement.

Four parts, each from data the findings already carry:
  surprise      - how rare the finding's own terms are in this workbook
  reach         - how many distinct questions and notes it spans
  consequence   - whether it reaches the action side (Q.5-Q.7) or the goal
  corroboration - how many distinct voices stand behind it, both sides counted
Then a repetition penalty: a finding that rests on the same terms and places
as one already picked is discounted, so the list stops saying one thing
three times.
"""
import json, re, sys, math

WB, SSO, LABEL = sys.argv[1], sys.argv[2], sys.argv[3]
wb = json.load(open(WB))['data']
sso = json.load(open(SSO))
findings = sso['full']['findings']
today = [f['head'] for f in sso['capped']['findings']]

# ---- corpus text, for how rare a term is -------------------------------
notes = wb.get('m') or []
pnotes = (wb.get('p') or {}).get('m') or []
corpus = ' '.join([wb.get('goal') or ''] + [a or '' for a in wb.get('a') or []] +
                  [(n[3] or '') for n in notes] + [(n[3] or '') for n in pnotes]).lower()
words = re.findall(r"[a-z0-9]+", corpus)
total = max(len(words), 1)

def occurrences(term):
    t = term.lower().strip()
    if ' ' in t:
        return corpus.count(t)
    stem = t[:6]
    return sum(1 for w in words if w.startswith(stem))

def voice_of(ref):
    m = re.match(r'note (\d+)$', ref)
    if m:
        i = int(m.group(1)) - 1
        if 0 <= i < len(notes):
            n = notes[i]
            return (n[7] if len(n) > 7 and n[7] else '') or '(unattributed)'
    m = re.match(r'P(\d+)$', ref)
    if m:
        i = int(m.group(1)) - 1
        if 0 <= i < len(pnotes):
            n = pnotes[i]
            return (n[7] if len(n) > 7 and n[7] else '') or '(unattributed)'
    return None

LEAD = {'Q.1', 'Q.2', 'Q.3', 'Q.4'}
ACT = {'Q.5', 'Q.6', 'Q.7'}

rows = []
for f in findings:
    refs = [r for r in f['refs'] if r]
    bold = [b for b in f['bold'] if b]
    text = f['text']

    # surprise: rare terms score high. A term used once in 500 words is
    # far more telling than `fire` in a workbook about fire.
    if bold:
        rates = [max(occurrences(b), 1) / total for b in bold]
        surprise = sum(-math.log(r) for r in rates) / len(rates)
    else:
        surprise = 0.0

    # reach: distinct places, plus a bonus for carrying across the two groups
    qs = set(r for r in refs if r.startswith('Q.'))
    ns = set(r for r in refs if not r.startswith('Q.'))
    reach = math.log(1 + len(qs) + len(ns))
    if qs & LEAD and qs & ACT:
        reach += 0.7

    # consequence: does it bear on action, or on the goal
    consequence = 0.0
    if qs & ACT:
        consequence += 1.0
    if 'goal' in text.lower():
        consequence += 1.0
    if re.search(r'\bnot yet\b|\bnothing\b|\bstill\b', text.lower()):
        consequence += 0.5   # an unmet condition is actionable

    # corroboration: distinct voices behind it, and both sides of the line
    vs = set(v for v in (voice_of(r) for r in refs) if v)
    corroboration = float(len(vs))
    if re.search(r'both sides|for and against', text.lower()):
        corroboration += 0.7

    rows.append({'head': f['head'], 'bold': bold, 'refs': refs, 'text': text,
                 'surprise': surprise, 'reach': reach,
                 'consequence': consequence, 'corroboration': corroboration})

def norm(key):
    vals = [r[key] for r in rows]
    lo, hi = min(vals), max(vals)
    for r in rows:
        r['n_' + key] = 0.5 if hi == lo else (r[key] - lo) / (hi - lo)

for k in ('surprise', 'reach', 'consequence', 'corroboration'):
    norm(k)

W = {'surprise': 0.35, 'reach': 0.25, 'consequence': 0.20, 'corroboration': 0.20}
for r in rows:
    r['base'] = sum(W[k] * r['n_' + k] for k in W)

def overlap(a, b):
    """How much two findings say the same thing: shared terms and places."""
    ta, tb = set(x.lower() for x in a['bold']), set(x.lower() for x in b['bold'])
    ra, rb = set(a['refs']), set(b['refs'])
    def j(x, y):
        return len(x & y) / len(x | y) if (x | y) else 0.0
    return 0.65 * j(ta, tb) + 0.35 * j(ra, rb)

# greedy selection with the repetition penalty
pool = sorted(rows, key=lambda r: -r['base'])
picked = []
while pool:
    best, bestv = None, -1
    for r in pool:
        pen = max([overlap(r, p) for p in picked] or [0.0])
        v = r['base'] * (1 - 0.75 * pen)
        if v > bestv:
            best, bestv, bestpen = r, v, pen
    best['final'] = bestv
    best['pen'] = bestpen
    picked.append(best)
    pool.remove(best)

print('#' * 62)
print('##', LABEL)
print('#' * 62)
print('\nTODAY (what the page shows, in the order it shows them)')
for i, h in enumerate(today, 1):
    print('  %d. %s' % (i, h))
print('\nSCORED (new order)')
for i, r in enumerate(picked[:7], 1):
    print('  %d. %-34s  terms: %s' % (i, r['head'], ', '.join(r['bold'][:4])))
print('\n  -- below the cut --')
for i, r in enumerate(picked[7:], 8):
    print('  %d. %-34s  terms: %s' % (i, r['head'], ', '.join(r['bold'][:4])))
print('\nWHY, in numbers (sur/reach/cons/corr -> base, repetition penalty, final)')
for i, r in enumerate(picked, 1):
    print('  %2d %-34s %.2f %.2f %.2f %.2f -> %.3f  pen %.2f  final %.3f'
          % (i, r['head'][:34], r['n_surprise'], r['n_reach'], r['n_consequence'],
             r['n_corroboration'], r['base'], r['pen'], r['final']))

print('\nFULL TEXT OF THE NEW TOP SEVEN')
for i, r in enumerate(picked[:7], 1):
    print('\n  %d. %s\n     %s' % (i, r['head'], r['text']))
print('\nDROPPED FROM TODAY\'S SEVEN (same page, now below the cut)')
seen = {}
for r in picked[7:]:
    if r['head'] in today and not seen.get(r['head']):
        seen[r['head']] = 1
        print('\n  - %s\n     %s' % (r['head'], r['text']))
