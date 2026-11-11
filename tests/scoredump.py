"""Read the engine's own WHAT STANDS OUT scores, not a replica of them.

Patches a scratch copy of the engine so the scored array is stashed on the
page, renders a workbook, and prints every candidate in the engine's order
with the four parts behind it. Nothing is written back to the engine.

  python3 -I scoredump.py ../gsm-preview.js real.json
"""
import json, re, subprocess, sys, tempfile, os
from playwright.sync_api import sync_playwright

JS, WB = sys.argv[1], sys.argv[2]
CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 99

src = open(JS, encoding='utf-8').read()

TAIL = 'return window.gsmTLR=P.slice(0,7),P.map(function(x){return x.t})}'
DUMP = ('window.__SC=P.map(function(x){return{bs:x.bs,rs:x.rs,su:x.su,rc:x.rc,'
        'cq:x.cq,cr:x.cr,ct:x.ct,nsu:x.nsu,nrc:x.nrc,ncq:x.ncq,ncr:x.ncr,nct:x.nct,'
        'cv:x.cv,bse:x.bse,fam:x.fam,ap:x.ap,'
        'raw:String(x.t[1]),'
        'h:String(x.t[0]).replace(/<[^>]*>/g,"")}});') + TAIL
assert src.count(TAIL) == 1, 'selection tail: expected 1, got %d' % src.count(TAIL)
src = src.replace(TAIL, DUMP)

CAPS = 'X.slice(0,7)'
assert src.count(CAPS) == 1, 'cap: expected 1, got %d' % src.count(CAPS)
src = src.replace(CAPS, 'X.slice(0,%d)' % CAP)

fd, path = tempfile.mkstemp(suffix='.js')
os.write(fd, src.encode('utf-8'))
os.close(fd)
chk = subprocess.run(['node', '--check', path], capture_output=True, text=True)
if chk.returncode:
    sys.exit('node --check failed: ' + chk.stderr)

wb = json.load(open(WB))['data']
HTML = (b'<!doctype html><html><head><meta charset="utf-8"></head><body>'
        b'<div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";'
        b'var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";'
        b'document.body.appendChild(t);</script></body></html>')
SRC = src.encode('utf-8')

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',
                          args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1400, 'height': 900})
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))

    def route(r):
        u = r.request.url
        if u == 'http://t.local/':
            r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'):
            r.fulfill(status=200, content_type='application/javascript', body=SRC)
        else:
            r.abort()

    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);"
                       "localStorage.setItem('groundsmith-web-welcomed','1');"
                       % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/')
    pg.wait_for_selector('#gsm', timeout=20000)
    pg.wait_for_timeout(1200)
    pg.evaluate("window.gsmTab&&window.gsmTab(2)")
    pg.wait_for_timeout(1000)
    sc = pg.evaluate("window.__SC||null")
    b.close()

os.unlink(path)
if not sc:
    sys.exit('the engine did not stash a scored array (errors: %r)' % errs[:3])

print('%d candidates, in the engine\'s own order' % len(sc))
def pt(x, k):
    # a part the family does not rank, or that cannot apply, prints as a dash
    return '    -' if not x.get('ap', {}).get(k) else '%5.2f' % (x.get('n' + k) or 0)


print('%-4s %-30s %-14s %5s %5s %5s %5s %5s %5s %6s'
      % ('', 'finding', 'family', 'sur', 'reach', 'cons', 'corr', 'ct', 'cv', 'base'))
for i, x in enumerate(sc, 1):
    print('%-4s %-30s %-14s %s %s %s %s %s %5.2f %6.3f'
          % (('%d.' % i) + (' *' if i <= 7 else ''), x['h'][:30], x.get('fam', ''),
             pt(x, 'su'), pt(x, 'rc'), pt(x, 'cq'), pt(x, 'cr'), pt(x, 'ct'),
             x.get('cv') or 0, x['bse']))
print('\n* = survives the cap of 7 today\n')
print('raw values, and what each finding names as resting on')
for i, x in enumerate(sc, 1):
    print('%2d %s' % (i, x['h'][:60]))
    print('     terms %r' % (x['bs'],))
    print('     places %r' % (x['rs'],))
    print('     su=%.3f rc=%.3f cq=%.3f cr=%.3f ct=%.3f cv=%.2f'
          % (x['su'], x['rc'], x['cq'], x['cr'], x.get('ct') or 0, x.get('cv') or 0))
    if not x['rs']:
        print('     RAW HTML THE SCORER READ:')
        print('       %s' % x['raw'][:700].replace('\n', ' '))
if errs:
    print('\npage errors: %r' % errs[:3])
