# Bear Canyon Method web workbook: HANDOFF at v103 (preview, not live)

Written 2026-11-10. Supersedes `handoff_v99.md`. Read this first, then
`week_of_11_09_plan.md` (what to build and in what order), then
`keep_or_cut_table.md`, `engine_audit_v98.md`, `asking_questions.md`,
`vocabulary_architecture.md` and `vocabulary_funnel.md`.

All wording in these documents is Claude's. Gregory edits his own text; do not
"fix" his.

## What it is

Gregory Vigneaux (Operational Coherence / WDI) builds "The Bear Canyon Method"
(earlier names Groundsmith, SenseCraft): a web workbook of seven questions plus
a map, with pattern readings and courses of action. He is not a coder: explain
simply, in plain words, and keep code terms out of replies.

## Starting a session

**The repository is public. You do not need it attached to read it.**

    git clone --depth 1 https://github.com/operationalcoherence/bcm

Give that a generous timeout. An attach is only needed to push a finished
version; ask for it when there is something to push, not at the start. He has
pre-approved push access for this repository, so request it and push verified
preview work rather than handing him files to commit.

**Both of his workbooks are now in the Claude project** as
`bear-canyon-workbook-2026-11-07.json` (the real one, line map, 24 notes) and
`bear-canyon-workbook-2026-11-05.json` (Broadview, place map, 14 place notes).
Read them with the project tool; the `data` key goes straight into
localStorage. There is no need to ask him for either.

## Where things stand

`gsm-preview.js` is still the only thing the page loads, still minified, and
every version since v95 has been made by exact-string replacement on it.
`gsm-readable.js` is that file prettified to about 12,790 lines and must be
regenerated whenever the preview file changes, or the next person reads a
version that is not running.

Hosting is unchanged. Repository `operationalcoherence/BCM`, served at
`https://operationalcoherence.github.io/BCM/`, preview page
`https://www.operationalcoherence.com/bcm`. The live page
`https://www.operationalcoherence.com/gsmlive` is **still on the old pasted v92
file and has not been cut over. Do not touch it without his say-so.**

Untested idea, carried forward from v99 and still never run: edit
`gsm-readable.js` and minify back with esbuild. If the unchanged readable file
minifies to something that renders identically, all later work gets easier.

## Standing rules (from him)

- PREVIEWS ONLY. Nothing goes live without his explicit go-ahead.
- One numbered version per batch of his edits. **Latest shipped: v103.**
- "Patterns suggests; you decide." Counts only, no scores.
- Flag any wording Claude wrote. He edits his own text.
- Keep all features; UI obvious, even, clean, one screen at a time.
- NEVER write the Esri API key into project docs or replies.
- After each batch: write the update doc.
- American spelling. He called British spelling in the workbook "the biggest
  error."
- The exported PDF and print should always match the online version.
- Do not use his own material as a public example or demo in the workbook.

### Wording rules (carried from v80, still in force)

- "The method" = the WHOLE thing. Never use it for only part.
- Parts may be named: the questions, the map, Pattern Analysis, Pattern
  Synthesis, actions/programs/strategies, In Parallel.
- The code groups Q.1–Q.4 against Q.5–Q.7. This grouping is silent. On screen
  it is only ever written as question numbers, "in Q.1–Q.4" or "in Q.5–Q.7".
  Do NOT invent group names. Use an en dash.
- "Emotion", never "feeling".

## The Esri key

Not in the source and not in the repository. It lives only in the block pasted
on the Webador page, which sets `window.GSM_ESRI_KEY`. Check any build before
pushing: `grep -c 'AAPK\|AIza' gsm-preview.js` must be 0. Restricted 5 Nov
2026, expires 2027-11-05.

## The Webador block

Unchanged and never needs changing again. Webador silently rejects a script
wrapped in an immediately-invoked function containing HTML tags inside
JavaScript strings. Keep it to plain top-level statements. See
`webador_stub_tiny_PREVIEW.html`.

## What shipped since v99

- **v100** (2026-11-08) — the map hover heading ends with the note's author,
  falling back to the workbook owner's name. Both maps.
- **v101** (2026-11-08) — the place map's note hover appears at all. A
  document-level `mouseover` listener resolved its target with `at()`, which
  matches only note and question references, and called `Z(null)` for anything
  else — including every Leaflet marker. The marker's own handler fires first,
  so the place map built the heading and then wiped it. The line map escaped
  this only because its figure re-shows the tooltip on `pointermove`.
  Pre-existing: place-map note hovers had never worked. Also adds
  `tests/placehover.py`.
- **v102** (2026-11-09) — stopword list cleaned, 362 entries to 352: eight
  duplicates and two entries the tokenizer can never match because it strips
  apostrophes first. No behavior change, proved by rendering.
- **v103** (2026-11-09) — In Parallel's "Where to start" no longer names the
  same word twice. It nominates a contested word, an unreached cause and a
  bridging thread with no check that they differ; on his workbook `fire` won
  two of the three roles.

Items 5, 6 and 7 of v99 use Claude's wording and still need his pass.

## Decisions he made on 2026-11-08, which shape everything below

**Elegance is the standard: power and simplicity.** From Gelernter, via a
passage he sent. For an interface that means functional minimalism — the
appropriate core functions and nothing else. He applied it himself and drew the
harder conclusion: *if it's minimized, why does it exist?* So **the ranking
must be allowed to drop a finding, not only fold it.** His earlier rule that
nothing is deleted is superseded by this; folding remains the default, cutting
is on the table where a section earns nothing.

**One screen on all three reading pages**, by minimizing the existing menus.
Not Pattern Synthesis alone. Current weights: Synthesis 1,957 words, Analysis
1,860, In Parallel 1,013.

**The six subject words are going in**, but after the ranking exists.
`community`, `communities`, `people`, `person`, `area`, `areas`. Decided, not
open. The cost is already measured — see the plan; do not re-derive it.

**Item 6 before item 2**, because proper nouns admit the largest influx of new
terms into a fixed number of named slots, and nothing arbitrates them until the
ranking exists.

**He also wants the engine to ask better questions**, not only report. See
`asking_questions.md`: a finding becomes a question when the engine has found a
discrepancy it cannot resolve and the person can.

## What to build, in order

Full table with estimates in `week_of_11_09_plan.md`. The four that come first,
about six hours together:

1. **Figure clipping**, 45–75 min. Serves neither goal; it is a bug fix, and it
   is first only because he sees it immediately.
2. **The safe cuts**, ~45 min, working from `keep_or_cut_table.md`.
3. **Layer 1 scoring, built alone**, ~2 hr. Gates nearly everything else.
4. **The question mechanism with one question**, ~2 hr.

Then the rest: `tok.js`, 5a, item 4, 6b, 2+3, and the smaller queue.

### What is known about the figure clipping, measured 2026-11-09

The hang figure's viewBox is hardcoded `-24 -14 388 348` for every workbook
while the loops are drawn from where the dots sit.

- On his workbook the drawing reaches y=349.5 and the frame stops at 334:
  **15.5 units cut off the bottom**, which confirms the handoff's 16.
- Broadview reaches exactly 334.0. It fits by zero, not by one unit.
- **Sizing the frame to the dots will not work.** His lowest dot is at y=306.6
  and the drawing reaches 349.5 — loops and labels extend about 43 units past
  the dots. All dot positions are known before the viewBox is written, which
  makes that approach tempting and wrong.
- What does work is measuring the finished drawing with `getBBox()`. It returns
  real numbers in this context. One catch: the white background `<rect>` is
  itself drawn at the old frame size, so it must be excluded from the
  measurement or it reports the frame back.
- Unverified risk: In Parallel draws the same figure, and `getBBox()` returns
  zeros for an element in a hidden tab.

Still open for him: whether the clipping he sees on screen matches 15.5 units,
which was measured headless at one window size.

## Corrections to earlier documents, found by running the code

- **`tests/tok.js` is stale.** It carries the pre-v99 lowercasing rule and
  drops `Good` as a proper noun when the shipped engine does not. With the live
  rule, item 2's baseline is **28 distinct names, 45 occurrences** — not 29 and
  46 as `handoff_v99.md` and `engine_audit_v98.md` state. Its `-ly` list is
  also 13 entries where the engine has 31. Fix the harness before measuring
  item 2.
- **"The engine reads none of it" overstates the proper-noun gap.** Pattern
  Analysis already prints A NAME THAT RECURS: Mitigate, Wildfire Design
  Industry, Fire Adapted Colorado, two places each. Names are detected for that
  one line; what they cannot do is become threads or feed other findings.
- **`good fire` is not split and needs no work.** It reads as a thread on 10
  dots, confirmed by rendering. v98's descriptive-word list keeps `good`
  holding the chain open, and v99's quote tolerance recovered `"Good fire"` at
  the start of a paragraph. Only multi-word names still break.
- **Synthesis's Outliers line is false.** It says the six unconnected dots "use
  words nothing else uses", but N20's word `social` also appears in N4 and N23,
  and the same page says so elsewhere. The test is presumably about the eight
  threads drawn in the figure; the prose claims something larger. Queued; needs
  a wording decision from him.

## Architecture notes

- State `C` in localStorage `groundsmith-web-v1`: goal, a[7], m[] line notes,
  p{m[],loc,c,name}, links[], voices, decisions, who, others[], fig,
  lastCombine, log[]. Other keys: `groundsmith-web-name`,
  `groundsmith-web-vnames`, `groundsmith-web-tab`, `groundsmith-web-welcomed`.
- `C.decisions` is **taken**: it holds Keep/Change/Drop on course-of-action
  cards, keyed by `mode|heading`. Answers to engine questions need their own
  key, and it must survive combine.
- Note array: `[type,x,y,text,area,emo,source,voice,id,author,extraVoices]`.
  His saved workbooks have 9 elements (no author/extraVoices); both work. Place
  notes use `[type,lat,lng,text,...]` in `C.p.m`.
- Emotion index order: 0 aggression, 1 acceptance, 2 distrust, 3 indifference,
  4 defiance. Not alphabetical; easy to get wrong.
- Tabs (data-v): 5 Start Here, 0 Mapping Context, 1 Mapping Change, 2 Pattern
  Analysis, 3 Pattern Synthesis, 6 In Parallel, 4 Taking Action.
  `window.gsmTab(n)`.
- Change map coordinates: viewBox `0 0 340 230`; y<118 helps, y>=118 hinders; x
  runs PRESENT (left) to FUTURE (right); GOAL at (305,156).
- `D` is the ordering array for the tangle reading's labels. Any new or renamed
  label must be added to `D`, or it sorts to the front.
- Full screen: the live handler is the delegated click listener on `Rt`, not
  the restore path in `Ut()`. Both exist and both need patching.
- **Term lists in a sentence are hard-capped** by `slice` — 3 to 8 terms
  depending on the sentence, then "and N more". There is no expander: an
  unnamed term is not reachable anywhere in the interface. This is why ranking
  matters and why `costly` and `deadly` stay invisible.
- Leaflet loads from a CDN. The test harness blocks it, which is why place-map
  rendering went untested for so long. `tests/placehover.py` serves it from a
  local copy (`npm install leaflet@1.9.4`).

## The word pipeline

`Ht(text)` strips apostrophes, lowercases sentence-initial capitals — since
v99 through an opening quote, bracket or dash — splits, then per token: a
capitalized word, a word under 3 letters, a stopword in `Ot`, a number, an `Ft`
word or an `-ly` word not in `At` breaks the chain; otherwise it is stemmed by
`Nt` (6 characters), recorded in `e.k`, and joined to the previous token as a
bigram in `e.b`. `Dsc` holds 19 descriptive words that keep the chain pointer
without becoming threads. `Ot` is now 352 entries. `At` is 31.

## Tests

`tests/` in the repository. Playwright Chromium, page served at
`http://t.local/`, non-local requests aborted, workbook injected into
localStorage.

`dump2.py` renders named tabs to plain text with every fold open — the way to
actually read what the engine says. `matrix.py` covers every tab of every
workbook. `coa.py` covers strategy vs program. `mkwb.py` writes the synthetic
workbooks. `tok.js` is a copy of the tokenizer run outside the page, and is
stale. `hover.py` and `placehover.py` test the line-map and place-map hovers.

**Run a non-wildfire workbook every time.** It is what exposed the domain
lexicon corrupting other subjects. **Run a place-map workbook every time.**
Place-map bugs have hidden behind line-map assumptions more than once, and v101
is the newest example.

## Unverified

iPad and touch; the live page `/gsmlive`; the PDF export (does not include IN
THE WORDS, WHO DID WHAT, or the combined reading, and v95–v103 are untested
against it); Leaflet tiles, since the harness blocks them; combine/merge across
workbooks.

## Known limits

Readings are templates driven by word matches and do not understand meaning.
Figure positions and hidden links are not merged on combine. Place-map full
screen has no note sheet. Names are self-declared. Pop-ups show static clones.

## The ceiling

The engine reads vocabulary, not claims. Going past that needs claim extraction
or a language model, which ends the self-contained, deterministic, private
design. **The elegance standard he set now argues against it:** that trade buys
power by spending all of the simplicity, which by Gelernter's test is not an
upgrade but a different artifact. Still his call, but he now has a principle to
decide it with.

## Open questions for him

- The In Parallel line for Start Here, in his words. A reader never learns the
  page exists.
- Which rows in `keep_or_cut_table.md` get cut. The ones marked Duplicate are
  the only ones Claude would act on with a simple yes.
- Does the bottom clipping he sees match the 15.5 units measured here?
- How the Outliers sentence should read.
- Whose figure position wins when two people move the same dot on combine?
- Does the place map's full screen need a note sheet?
- Should the PDF include the new sections, and the version number?
- Cut `/gsmlive` over to the hosted file?
- Does the vocabulary feature jump ahead of item 6? Its second step needs the
  ranking either way.

## Lessons, carried forward and re-earned

- **Do not state a guess as a finding.** v99's session said the `-ly` fix would
  surface `costly` and `deadly`. It did not. This session assumed the figure
  frame could be sized from the dots; it cannot, by 43 units. Both were caught
  by looking.
- **Run the code before describing it.** Everything above came from rendering
  pages to text and from running the tokenizer over his actual words.
- **Verify the thing you changed, not the thing you meant to change.** v101's
  claim that the hover "works the same on both maps" was true of the code and
  false on screen.
- **Test on a workbook that is not about wildfire, and on a place map.**
- **Quote him his own cost.** Offer the cheap version first and give an honest
  estimate. On 2026-11-09, with 2% usage left, two real items shipped: the
  stopword cleanup because it cannot change behavior, and the "Where to start"
  fix because it is logic rather than wording and so needed no pass from him.
