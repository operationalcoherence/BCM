# Test harness

Playwright Chromium. The page is served at `http://t.local/`, the hosted file
is fulfilled from a local path, and every non-local request is aborted, so no
fonts, tiles or Esri calls go out. The workbook under test is injected into
`localStorage` before the page loads.

Kept here because every previous harness lived in a sandbox that was lost.

    pip install playwright && playwright install chromium

| Script | What it does |
| --- | --- |
| `fulldump.py WORKBOOK.json ['JS']` | Pattern Analysis as text with every fold and `<details>` open and the 3D loaded (v275); dump2 leaves `<details>` closed. A second argument prints one JS expression instead. |
| `dump2.py JSFILE WORKBOOK.json 2,3,6,4` | Renders the named tabs to plain text with every fold open. The way to actually read what the engine says. Tabs: 5 Start Here, 0 Mapping Context, 1 Mapping Change, 2 Pattern Analysis, 6 In Parallel, 4 Taking Action (since v269 there is no Pattern Synthesis; 3 opens Analysis). |
| `matrix.py WORKBOOK.json …` | Runs every tab of every workbook given. Reports boot time, per-tab time and word count, any uncaught page error, and whether either script-injection probe fired. |
| `coa.py WORKBOOK.json …` | Counts STRATEGY against PROGRAM in Taking Action and prints the reasons each card gives. |
| `mkwb.py` | Writes the synthetic test workbooks: empty, goal-only, single-note, a non-wildfire clinic workbook, a legacy 9-element-note one and its 10-element twin, hostile text, 200 notes, 12 identical notes, and one carrying both maps. |
| `tok.js WORKBOOK.json` | A faithful copy of the tokenizer, run outside the page. Reports what survives, stem collisions, proper nouns dropped, stopwords hit, and -ly words dropped. Reads the stopword list, the -ly exceptions and the descriptive words straight from `gsm-preview.js`, so it cannot go stale. |
| `derive.py WORKBOOK.json [NOTE EMOTION]` | Boots without opening In Parallel, prints the derived action points, edits one note's emotion through the page's own save, and reports whether the points and MOVES, IN ORDER follow (v199). On a place map the edit doesn't reach the notes, so use a line map for the edit half. |
| `switch.py WORKBOOK.json` | The program/strategy switch on Taking Action cards (v202): switches the first program card, checks it stays and is saved, then undoes it. |
| `waymoves.py WORKBOOK.json` | FIRST MOVES follows the selected way (v203): with the 3D loaded, clicks every way on every card and prints the line under FIRST MOVES. |
| `qhover.py WORKBOOK.json` | Hovering a question above YOUR LANDSCAPE shows the question and its notes (v205). |
| `tour.py WORKBOOK.json [OUT] [slow]` | The guided tour on THE LAY OF THE LAND, now at the end of Pattern Analysis (v208, v269), with the 3D loaded: presses Play, prints each caption, screenshots three moments, checks a click stops it. `slow` runs it 8x slower for settled screenshots. |
| `tour_an.py WORKBOOK.json [OUT]` | The short tour on Pattern Analysis (v210), with the 3D loaded: plays it, prints each caption, screenshots one stop, checks End tour closes full screen. |
| `agree.py WORKBOOK.json [OUT]` | THE TWO PICTURES, SIDE BY SIDE on In Parallel (v213; since v269 its taps draw on the ground on Pattern Analysis), with the 3D loaded: lists the words and verdicts, taps one, checks its hoses are drawn on the 3D, screenshots both. |
| `vague_titles.py WORKBOOK.json …` | No vague Taking Action titles (v284): every card title names its object in the user's words. FAILs on a title that names a single non-emotion word or nothing at all. |
| `pagewalk.py JSFILE WORKBOOK.json OUTDIR [width]` | Start Here, Mapping Context steps 0 to 7, and Mapping Landscape steps 1 and 2, every fold open: prints each step's text and saves a full-page screenshot (v290; default width 420, a phone). |
| `f8join.py JSFILE WORKBOOK.json WIDTH OUTPREFIX` | F8 step 4, the invited person (v311), with fake Firebase kept in sessionStorage so it survives reloads: invite link, own workbook parked and restored, name and voice, live save, Pause, the daily limit, the lead changing the goal or closing the project, Delete my workbook, a bad link, a place-map project. Prints PASS/FAIL lines. |
| `privacy.py JSFILE WORKBOOK.json WIDTH OUTPREFIX` | The privacy screen (v318): solo screen on first open, can't be got past, full page, footer link, asked again on a new version, live screen on an invite link, acknowledgement in the workbook record. `privacy_lead.py` (same arguments) checks Lead a project asks first and the project record. Every other script sets the acknowledgement at start-up. |
| `f8cmp.py JSFILE WORKBOOK.json WIDTH OUTPREFIX` | COMPARE TWO (v317): people, voices, an overlap, the voice filter. |
| `ev.py JSFILE WORKBOOK.json TAB 'JS'` | Opens a tab and prints the JSON of one JavaScript expression evaluated in the page (v249). |
| `stop.txt` | Obsolete (pre-v102, 362 entries). `tok.js` no longer reads it. |

## Workbooks the scripts expect

`mkwb.py` writes everything it needs except two real ones it reads to build the
both-maps case: `real.json` and `broadview.json`. Those are Gregory's own
workbooks and are **not** kept in this repository — ask him for them, and take
the `data` key of a saved workbook file.

Run a non-wildfire workbook every time. It is what exposed the domain lexicon
corrupting other subjects, and place-map bugs have hidden behind line-map
assumptions more than once.

## placehover.py - the place map

The page loads Leaflet from a CDN, which this harness blocks, so the place map
never rendered in testing and place-map bugs hid behind that. `placehover.py`
serves Leaflet from a local copy and hovers every marker:

    npm install leaflet@1.9.4
    python3 placehover.py ../gsm-preview.js bear-canyon-workbook-2026-11-05.json Greg

The third argument is optional and is written into the workbook's `who` field,
which is what a note with no author falls back to in the hover heading. Map
tiles stay blocked; markers do not need them. `hover.py` is the line-map
equivalent and needs no Leaflet.
