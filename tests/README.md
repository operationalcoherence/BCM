# Test harness

Playwright Chromium. The page is served at `http://t.local/`, the hosted file
is fulfilled from a local path, and every non-local request is aborted, so no
fonts, tiles or Esri calls go out. The workbook under test is injected into
`localStorage` before the page loads.

Kept here because every previous harness lived in a sandbox that was lost.

    pip install playwright && playwright install chromium

| Script | What it does |
| --- | --- |
| `dump2.py JSFILE WORKBOOK.json 2,3,6,4` | Renders the named tabs to plain text with every fold open. The way to actually read what the engine says. Tabs: 5 Start Here, 0 Mapping Context, 1 Mapping Change, 2 Pattern Analysis, 3 Pattern Synthesis, 6 In Parallel, 4 Taking Action. |
| `matrix.py WORKBOOK.json …` | Runs every tab of every workbook given. Reports boot time, per-tab time and word count, any uncaught page error, and whether either script-injection probe fired. |
| `coa.py WORKBOOK.json …` | Counts STRATEGY against PROGRAM in Taking Action and prints the reasons each card gives. |
| `mkwb.py` | Writes the synthetic test workbooks: empty, goal-only, single-note, a non-wildfire clinic workbook, a legacy 9-element-note one and its 10-element twin, hostile text, 200 notes, 12 identical notes, and one carrying both maps. |
| `tok.js WORKBOOK.json` | A faithful copy of the tokenizer, run outside the page. Reports what survives, stem collisions, proper nouns dropped, stopwords hit, and -ly words dropped. Uses `stop.txt`. |
| `stop.txt` | The 362-entry stopword list, lifted from the engine so `tok.js` matches it exactly. Regenerate it if the list changes. |

## Workbooks the scripts expect

`mkwb.py` writes everything it needs except two real ones it reads to build the
both-maps case: `real.json` and `broadview.json`. Those are Gregory's own
workbooks and are **not** kept in this repository — ask him for them, and take
the `data` key of a saved workbook file.

Run a non-wildfire workbook every time. It is what exposed the domain lexicon
corrupting other subjects, and place-map bugs have hidden behind line-map
assumptions more than once.
