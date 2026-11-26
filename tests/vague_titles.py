"""v284: no vague Taking Action titles. Every card title must name its object in the user's words: a phrase of two
or more words, an emotion, a short clause from a note with its id, note ids, or the user's own instruction. Prints FAIL for any title
that names only a single word (not an emotion) or nothing at all.
Usage (from tests/): python3 vague_titles.py WORKBOOK.json ..."""
import json, sys, re
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
EMO = re.compile(r'^(accept|indiffer|distrust|aggress|defian)', re.I)
VAGUE = re.compile(r'^(Build on what already helps|Scale the alternative that already exists|Reinforce the support you have not backed yet|Change what holds the situation in place|Carry out what you designed)\s*$')
bad = 0
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    for f in sys.argv[1:]:
        wb = json.load(open(f))['data']
        pg = b.new_page()
        def route(r):
            u = r.request.url
            if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
            elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
            else: r.abort()
        pg.route('**/*', route)
        pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
        pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1200)
        pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(4000)
        ts = pg.evaluate("[].slice.call(document.querySelectorAll('#gsm .coa .taact')).map(e=>e.textContent)")
        for t in ts:
            q = re.findall(r'“([^”]+)”', t)
            why = ''
            if VAGUE.match(t): why = 'names nothing'
            goal = ' ' + re.sub(r'[^a-z0-9 -]', ' ', str(wb.get('goal', '')).lower()) + ' '
            for x in q:
                if ' ' not in x.strip() and not EMO.match(x): why = 'single word: ' + x
                elif ' ' + x.lower() + ' ' in re.sub(r'\s+', ' ', goal): why = "only the goal's own words: " + x
            print(('FAIL ' if why else 'ok   ') + f.split('/')[-1] + ': ' + t + (' (' + why + ')' if why else ''))
            bad += bool(why)
        pg.close()
    b.close()
print('ALL PASS' if not bad else '%d VAGUE' % bad)
