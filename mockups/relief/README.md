# Relief-model mock-up (approved look, 2026-11-12)

Not part of the engine yet. See project doc claude/relief_mockups_2026_11_12.md for the recipe Gregory approved (60% emotion color over a rock/grass/soil substrate, rock face between distant emotions).

Build:
1. Make a copy of gsm-preview.js with a hook at the top of `render(st)` that stores terr (hn, col, notes, qpos, START, GOAL, ROUTES, EMO) on window.__GTC / window.__GTR (see dump.py).
2. `python3 -I dump.py hooked.js WORKBOOK.json data.json`, then compact it into the page as `window.DATA`.
3. `npm i three esbuild && npx esbuild main.js --bundle --minify --format=iife --outfile=bundle.js`, inline bundle.js and the data into page.html (__JS__, __DATA__).
4. `shot.py page.html out.png '?style=field&alpha=60'` renders a screenshot.
