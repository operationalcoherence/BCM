# Bear Canyon Method web workbook: HANDOFF at v99 (preview, not live)

Written 2026-11-08. Supersedes `groundsmith_web_handoff_v98.md`. Read this
first, then `engine_audit_v98.md` (the evidence behind most of the work
below), then `v99_plan.md`, `v99_update.md`, `vocabulary_architecture.md` and
`vocabulary_funnel.md`.

**All wording in these documents is Claude's.** Gregory edits his own text;
do not "fix" his.

## What it is

Gregory Vigneaux (Operational Coherence / WDI, gvigneaux.nps@gmail.com) builds
"The Bear Canyon Method" (earlier names Groundsmith, SenseCraft): a web
workbook of seven questions plus a map, with pattern readings and courses of
action. He is not a coder: explain simply.

## What changed since the v98 handoff, and why this one is different

The v98 handoff warned that the readable source was four versions stale and
the project depended on a sandbox that was already gone. **That is fixed.**

- `gsm-readable.js` is in the repository: the hosted file prettified to about
  12,700 lines, verified to render identical page text on his real workbook
  across Pattern Analysis, Pattern Synthesis, In Parallel and Taking Action.
- `docs/` holds the design and audit documents.
- `tests/` holds the Playwright harness and the stopword list, so nobody
  rebuilds a harness from a description again.
- The README says to regenerate `gsm-readable.js` whenever `gsm-preview.js`
  changes. **Do that, every time, or the two drift and the next person reads a
  version that is not running.**

`gsm-preview.js` is still the only thing the page loads, and it is still
minified. v99 was made by exact-string replacement on it, the same method as
v95–v98, and `gsm-readable.js` was regenerated afterwards.

**Untested idea, worth trying first next week:** edit `gsm-readable.js` and
minify it back to `gsm-preview.js` with esbuild. If the unchanged readable
file minifies to something that renders identically, all later work gets much
easier. If it does not, fall back to exact-string patching. This was set up
but never run.

## Hosting (unchanged)

- Repository: `operationalcoherence/BCM` — https://github.com/operationalcoherence/BCM
- Served at https://operationalcoherence.github.io/BCM/ — Pages deploys from
  `main`, folder `/` (root)
- Preview page: https://www.operationalcoherence.com/bcm loads `gsm-preview.js`
- Live page: https://www.operationalcoherence.com/gsmlive — **still on the old
  pasted v92 file.** Not cut over. Do not touch without his say-so.
- To ship: patch `gsm-preview.js`, regenerate `gsm-readable.js`, commit, push.
  The loader appends a number that changes every minute, so a push shows within
  a minute.
- `gsm.js` — the live file — deliberately does not exist in the repository.
  Promoting a version is what creates it.

## Standing rules (from him)

- **PREVIEWS ONLY.** Nothing goes live without his explicit go-ahead.
- One numbered version per batch of his edits. **Latest shipped: v99.**
- "Patterns suggests; you decide." Counts only, no scores.
- Flag any wording Claude wrote. He edits his own text.
- Keep all features; UI obvious, even, clean, one screen at a time.
- **NEVER write the Esri API key into project docs or replies.**
- After each batch: write the update doc.
- American spelling. He called British spelling in the workbook "the biggest
  error."
- The exported PDF and print should always match the online version.
- Do not use his own material as a public example or demo in the workbook.

### Wording rules (carried from v80, still in force)

- "The method" = the WHOLE thing: the questions, the map, Pattern Analysis,
  Pattern Synthesis, Taking Action programs and strategies. Never use "the
  method" for only part of it.
- Parts may be named: the questions, the map, Pattern Analysis, Pattern
  Synthesis, actions/programs/strategies, In Parallel.
- The code groups Q.1–Q.4 (not already, opposition, support, conditions)
  against Q.5–Q.7 (design, redesign, reinforce). This grouping is silent. On
  screen it is only ever written as question numbers, "in Q.1–Q.4" or "in
  Q.5–Q.7". Do NOT invent group names. Use an en dash: Q.1–Q.4.
- **"Emotion", never "feeling".** Changed throughout in v99.

## The Esri key

Not in the source and not in the repository. It lives only in the small block
pasted on the Webador page, which sets `window.GSM_ESRI_KEY`. The source reads
`(window.GSM_ESRI_KEY || "")`. Check any build before pushing:
`grep -c 'AAPK\|AIza' gsm-preview.js` must be 0. He restricted it on 5 Nov
2026: referrers locked to operationalcoherence.com, Geocode-not-stored only,
pay-as-you-go disabled, **expires 2027-11-05**.

## The Webador block

Unchanged and never needs changing again. Webador silently rejects a script
wrapped in an immediately-invoked function containing HTML tags inside
JavaScript strings. Keep the block to plain top-level statements: no function
wrapper, no markup inside JavaScript strings. See
`webador_stub_tiny_PREVIEW.html`.

---

# What v99 already shipped (2026-11-07)

Seven changes, all verified on the real, Broadview (place map) and clinic
workbooks with no page errors. Details in `v99_update.md`.

1. **"feeling" → "emotion"**, 24 places, including the all-caps titles THE
   FEELING CHANGES and ONE FEELING THROUGHOUT. The ordering array `D` holds
   the label too and was changed in step.
2. **"colouring" → "coloring."** The only British spelling in the file.
3. **A sentence may open with a quotation mark.** The lowercasing rule now
   tolerates an opening quote, bracket or dash before the capital. It was
   costing `"Good fire"` at the start of a paragraph in Q.1.
4. **The -ly exception list, 13 entries to 31.** Recurring list 109 → 111.
5. **"Voices." no longer appears twice in a row.** Three sections shared the
   label and sorted to the same rank. Now "Who you heard from.", "One voice
   only.", "A voice not carried through." — all added to `D` in the old
   label's place.
6. **"What these lines read." → "Beyond the picture."** It echoed the section
   label above it.
7. **Full screen names the figure**, from the nearest preceding `.plab`,
   cleared on close. Escape already closed full screen and still does.

Items 5, 6 and 7 use Claude's wording and need his pass.

---

# What we are going to do next week

He approved the whole list on 2026-11-07 and set one hard constraint on the
synthesis page: **one screen, no scrolling.** The work waits for his usage to
reset Wednesday morning.

Build order: 1 first because he will see it immediately; then 2–5, which
change what the reading pages say; then 6, which is the largest.

## 1. Fix the figure clipping

The `hang` figure's viewBox is hardcoded `-24 -14 388 348` (x −24→364,
y −14→334) for every workbook, while the loops are drawn from where the dots
sit. Measured at v98:

| Workbook | Drawn extent (x0,y0,x1,y1) | Result |
| --- | --- | --- |
| His real (line map) | 12, −1, 352, **350** | 16 units cut off the bottom |
| Broadview (place map) | 13, 15, 347, 333 | fits by 1 unit |
| Synthetic 24-note | 1, **−22**, **375**, 315 | cut at top and right |

Full screen does not help: `#gsm .pnet.fs svg{height:100%}` scales the
already-clipped viewBox. **Broadview missing it by one unit is the point** —
every workbook is exposed, and which edge gets cut depends only on where the
dots land.

**Fix:** compute the viewBox from the union of the drawn geometry plus a
margin. Correct for any workbook and any note count. It also removes the
asymmetric dead space on the left, since content starts at x=12 inside a frame
starting at −24. Verify on all three workbooks, line map and place map, and in
full screen at more than one window size.

Still unknown: whether the bottom clipping he sees on screen matches the 16
units measured here, or whether his screen shows more.

## 2. Let the engine see proper nouns

Any word capitalised mid-sentence is dropped **and breaks the phrase chain**.
There is no exception list and no recovery.

Measured on his workbook: **29 distinct proper nouns, 46 occurrences** —
Smokey, Bear, Fire Adapted Colorado, The Ember Alliance, The Nature
Conservancy, BurnBot, Incident Management Teams, Wildfire Design Industry,
FiSci's Mitigate, Operational Coherence, Colorado. His Q.3 answer — what
support already exists — is almost entirely named organizations and the engine
reads none of it.

This is the largest category of unread content, and it is general: for a
method about communities and the actors in them, every person, organization,
place and product is structurally invisible. A clinic workbook loses "Broad
Street"; a county workbook loses the council's name.

**Approach to try:** admit a capitalised word as a thread when it recurs
across two or more dots, which is the same bar every other word meets. Keep
the chain unbroken through it. The risk is noise from sentence-initial words
that the lowercasing rule misses; v99 fixed the quote case, so that risk is
already lower. Watch what it does to the clinic workbook as well as his.

## 3. Decide the stopword list

362 entries, **354 unique**. Three separate things to do:

- **Remove the 8 duplicates** (could, get, got, much, other, same, way,
  taken). No behavior change.
- **Remove `place's` and `time's`.** The tokenizer strips apostrophes before
  the lookup, so neither entry can ever match. No behavior change.
- **His call: `community`, `communities`, `people`, `person`, `area`,
  `areas`.** These are often the subject rather than the scaffolding, and a
  method applied to community problems can never surface either word as a
  pattern. Suppressing the method's own question words — design, redesign,
  reinforce, support, oppose, condition — is defensible, because every answer
  contains them; these are different. **Ask him before changing it.**

Context for the decision: only **44% of his tokens** survive to the analysis
(670 of 1,535), and 54% on the clinic workbook.

## 4. Make the PRESENT–FUTURE axis produce findings

The x coordinate is read in **exactly one place**, to order the path figure in
Taking Action. Half the change map is drawn, labelled and explained to the
person and contributes to no finding.

It carries a real pattern. His map in thirds:

| | helps | hinders |
| --- | --- | --- |
| present third | 3 | 8 |
| middle third | 6 | 3 |
| future third | 3 | 1 |

What hinders sits in the present; what helps sits ahead. That is a readable
statement about where his difficulty lives in time, and no other signal
answers it. Zero new interface and the data is already there.

## 5. Handle redundant signals, and report the redundancy

Measured on his real workbook:

| | acceptance | aggression | distrust | indifference | defiance |
| --- | --- | --- | --- | --- | --- |
| **helps** (above the line) | **11** | 0 | 0 | 0 | 0 |
| **hinders** (below the line) | 0 | **7** | 2 | 2 | 1 |

A perfect separation. Every note he placed above the line he also marked
acceptance; not one below it. The engine treats emotion and help/hinder as
independent, so "this helps *and* carries acceptance" is one judgement
reported as two agreeing ones, and the Layer 1 corroboration score would
inflate it further.

Two things follow:

- **The ranking must discount correlated signals.** Measure the agreement
  between signals in the workbook at hand and weight corroboration by how
  independent they actually are.
- **The correlation is itself a finding.** "Your emotion marks and your
  placement are the same judgement made twice; one of them is adding nothing."
  Costs one cross-tab and reads as a deep observation.

### Related: the same reason given twice in a course-of-action card

The strategy/program call tests six conditions and names the ones that hold.
Two overlap: `"unanswered" === e.c` ("nothing in Q.5–Q.7 answers it") and
`!e.R.act` ("Q.5–Q.7 do not reach it", set by `act: e >= 4`, so the item sits
in Q.1–Q.4). For any card anchored on a Q.1–Q.4 item whose word is unanswered,
both fire and the card says "and 1 other thing points the same way". The
fourth and sixth conditions — strong emotion, more hindering than helping —
are correlated for the same reason as above. Observed on the clinic workbook:
"A strategy, because nothing in Q.5–Q.7 answers it, and 2 other things point
the same way."

The classifier itself is sound and does not need changing: the split measured
5/4, 3/5, 3/6 and 3/2 across four workbooks. Only the reason-counting is wrong.

## 6. Rewrite Pattern Synthesis to one screen

**His constraint: one screen, no scrolling.** Roughly 150–250 words at full
weight, three or four blocks, everything else behind folds. Nothing is deleted.

Today the page renders to **1,947 words**. "What this suggests" is **478
words** across 12 labelled paragraphs; "WHAT IT MIGHT MEAN" is **347 words**
across 18 items. Everything sits at equal weight, so nothing reads as
important.

### What he asked for, in his words

Key points; takeaways; theories of patterns; **patterns needed to reach the
goal**; **patterns that reach the goal**; "make it important, surprisingly
deep insights."

### Both of his named sections already exist, buried

- *Patterns that reach the goal* — the existing line "18 of them tie back to
  the goal (managing unplanned, unplanned fire, aggressive suppression, good
  fire)", near the bottom of WHAT IT MIGHT MEAN.
- *Patterns needed to reach the goal* — the existing buckets "Not in Q.5–Q.7
  yet (13)", "Condition (1)" and "Unused support (8)". The page already
  concludes "those 14 are where Q.5–Q.7 are thinnest" and then buries it.

So the rewrite is mostly selection and ordering, not new computation.

### Proposed shape

1. What reaches the goal.
2. What the goal needs and does not have.
3. One or two deep readings.
4. Where to look first.

### The finding family that produces the depth he asked for

**Heavy overlap, opposite emotion.** Two threads running through many of the
same dots but leading with different emotions. Domain-free; no word list.
Measured from the engine's own thread data:

| Thread | Dots | Leading emotion |
| --- | --- | --- |
| fire | 19 | acceptance |
| good fire | 10 — a complete subset of *fire* | acceptance |
| wildfire | 16 | aggression |
| suppression | 13 | aggression |
| aggressive | 8 | aggression |
| force | 7 | aggression |

*fire* and *wildfire* share 11 dots — **69% of everywhere *wildfire*
appears** — and lead with opposite emotions. His stated goal is the
distinction between a suppression vocabulary and an ecological one. That
distinction is measurable in his own writing and the page does not say it.

The rule generalizes: in any workbook it finds a subject the person feels two
ways about depending on which word they reach for. Rank it alongside the
existing THE EMOTION CHANGES (same word, different emotion across Q.1–Q.4 vs
Q.5–Q.7) and ONE IDEA UNDER TWO NAMES.

### Ranking (Layer 1 from the evaluation document)

Score every finding on **surprise** (distance from what the word's overall
frequency predicts — this is what correctly demotes "wildfire" in a wildfire
workbook), **reach**, **consequence** (does it bear on Q.5–Q.7 or the goal),
and **corroboration** (how many independent signals agree; disagreement ranks
highest), with the correlation discount from item 5. Show three or four at
full weight; fold the rest.

Keep computing all ~130 findings. Nothing is removed, only ranked.

### Open on this one

- Whether the folded remainder keeps all 12 paragraphs or drops some.
- All new wording will be Claude's and needs his pass.
- The same length problem exists on Pattern Analysis and In Parallel. He has
  only ruled on Synthesis.

---

# Also queued, smaller

- **In Parallel is missing from the instructions.** Start Here says "THE FIVE
  PAGES" and lists five; there are seven tabs, and In Parallel appears in
  neither that list nor the glossary. A reader never learns the page exists.
  **His copy, so his line to write** — ask him for it.
- **A workbook with nothing to distinguish produces no courses of action and
  says nothing.** Reproduced with a deliberately degenerate workbook (12
  identical notes, 7 identical answers): zero cards, no message. An edge, but
  the page should say there is nothing to suggest yet.
- **The -ly exception list is a stopgap.** v99 grew it from 13 to 31, but a
  suffix test cannot tell an adjective from an adverb, so it will keep needing
  additions — the same shape of problem as the domain lexicon v98 removed.
  A better rule is wanted.
- **Six-character stem truncation can merge unrelated words.** Latent: it does
  no harm on his workbook or the clinic one, where all 41 collisions are
  legitimate variants (burn/burning/burned). But conservation + conservative →
  `conser`, contract + contrast → `contra`, continue + continent → `contin`,
  transport + transparent → `transp`, construction + constraint → `constr`,
  compliance + complication → `compli`, integration + integrity → `integr`,
  personal + personnel → `person`, information + informal → `inform`,
  relative + relationship → `relati`, sustain + sustainable → `sustai`,
  interior + interim → `interi`. A governance or procurement workbook would hit
  several, and nothing on screen would show that a merge happened.
- **costly and deadly are counted but invisible.** v99 made them eligible and
  they are in the 111 recurring terms, but they sit below what the page prints.
  Layer 1 scoring is what would surface them.

---

# The vocabulary feature

Designed, not built. Five screens:
https://claude.ai/artifact/Vk5rTHDvugvbXGzZ72uG7V — Entry, Your words, Naming,
Opening a vocabulary, How it shows afterwards.

He treats this as the thing he most cares about. It is its own version, not
part of the work above, because it adds interface rather than changing
readings.

**What the mockup settles**, against the open questions in
`vocabulary_architecture.md`:

- **Where the question lives:** Mapping Change step 2, "describe your notes",
  as a dismissible card above the note list. Not Start Here, not Pattern
  Analysis.
- **Whether a grouping shows on screen:** yes. A grouped term keeps the dotted
  underline the page already uses for note and question references, with a
  tooltip reading "Counted as one" and the member words. No new kind of mark.
- **Whose vocabulary wins:** resolved per group, not per file — groups that
  come in cleanly, groups that need a decision because a word is claimed on
  both sides, and groups that wait because the words have not been written yet.
- **Naming a group:** the most-used member is proposed, the others stay
  visible, the person may type their own name.

**What the mockup needs before it is built:**

- Its counts are placeholders from before v98 (fire 29 / wildfire 29, and
  elsewhere 24 / 18 / 2). The engine at v98 reports fire 19 dots, wildfire 16,
  suppression 13, good fire 10. Take real counts.
- Its "too faint to be reported at all" line needs checking against the live
  threshold, which reports anything at two dots or more.
- The Entry screen labels the emotion chips "Feeling". v99 retired that word.
- The After screen says "The centre." British; the live page says "The center."

**The narrowing problem he raised**, and the answer, in
`vocabulary_funnel.md`: nobody can be asked about 559 words. Drop what appears
once (365 of 559 on his workbook); the recurring list is the pool (**109 terms
on his workbook, 111 after v99**); ask only about terms that carry a top
finding; build pairs from the three free signals (same distribution, shared
head word with a different modifier, author glosses); cap at five to eight
pairs, one tap each, stored in the workbook.

Both halves are wanted: the funnel handles what he wrote, a loadable starter
pack handles what he did not — "RX fire" appears zero times in his workbook.

**The principle, unchanged: split by default, never merge.** A wrong merge
destroys a distinction invisibly; a wrong split is visible and recoverable.

---

# Architecture notes

- State `C` in localStorage `groundsmith-web-v1`: goal, `a[7]`, `m[]` line
  notes, `p{m[],loc,c,name}`, `links[]`, voices, decisions, who, `others[]`,
  fig, lastCombine, `log[]`. Other keys: `groundsmith-web-name`,
  `groundsmith-web-vnames`, `groundsmith-web-tab`, `groundsmith-web-welcomed`.
- Note array: `[type,x,y,text,area,emo,source,voice,id,author,extraVoices]`.
  His saved workbooks have 9 elements (no author/extraVoices) — **both work
  identically; verified at v98 on a 9-element file and its 10-element twin.**
  Place notes use `[type,lat,lng,text,...]` in `C.p.m`.
- **Emotion index order: 0 aggression, 1 acceptance, 2 distrust,
  3 indifference, 4 defiance.** Not alphabetical; easy to get wrong.
- Tabs (`data-v`): 5 Start Here, 0 Mapping Context, 1 Mapping Change,
  2 Pattern Analysis, 3 Pattern Synthesis, 6 In Parallel, 4 Taking Action.
  `window.gsmTab(n)`. Mapping Change is two steps; step 2 is "describe your
  notes".
- Change map coordinates: viewBox `0 0 340 230`; **y<118 helps, y>=118
  hinders**; x runs PRESENT (left) to FUTURE (right); GOAL at (305,156).
- Readings: `INTB`/`INTGO` (combined reading), `TXR()` with
  `put(t,e,kw,kp)`, `Ft`/`XTB`, `MIR()`, `CPATH(st,notes)`, `CBODY(...)`.
- `D` is the ordering array for the tangle reading's `§...§` labels.
  `H.split("\n").concat(T)` is sorted by position in `D`. **Any new or renamed
  label must be added to `D`, or it sorts to the front.**
- Full screen: the live handler is the delegated click listener on `Rt`, not
  the restore path in `Ut()`. Both exist and both need patching. Escape closes
  it.
- Strategy versus program is measurable on the path figure: strategies cross
  the line 4–12 times at 2.0–4.6x, programs cross once at 1.0–1.4x.
  Test-asserted.

## The word pipeline

`Ht(text)` tokenizes: strips apostrophes, lowercases sentence-initial capitals
(**since v99, through an opening quote, bracket or dash**), splits, then per
token — a capitalised word, a word under 3 letters, a stopword in `Ot`, a
number, an `Ft` word or an -ly word not in `At` breaks the chain; otherwise the
token is stemmed by `Nt` (truncates to 6 characters), recorded in `e.k`, and
joined to the previous token as a bigram in `e.b`.

- `Dsc` (v98) holds 19 descriptive words that keep the chain pointer without
  becoming threads: good, bad, new, old, right, wrong, big, small, great,
  true, real, whole, full, general, specific, particular, different, certain,
  first.
- `Ot` is a 362-entry English stopword list; 354 unique. Anything on it is
  invisible unless it is in `Dsc`.
- `At` is the -ly exception list, **31 entries since v99**.
- `Mt` records each stem's original surface forms; `jt(token)` returns the most
  common one for display, splitting bigrams on the space.
- `g` = per-dot counts for single words, `p` = for bigrams. A word or phrase
  enters the recurring list only at **count > 1** (two or more dots). A single
  word is dropped when its count equals a phrase it always sits inside, so a
  phrase suppresses its own parts.

# Tests

`tests/` in the repository. Playwright Chromium, page served at
`http://t.local/`, non-local requests aborted, workbook injected into
localStorage. See `tests/README.md`.

| Script | Covers |
| --- | --- |
| `dump2.py` | renders named tabs to plain text with every fold open — the way to actually read what the engine says |
| `matrix.py` | every tab of every workbook: boot time, per-tab time and words, page errors, script-injection probes |
| `coa.py` | strategy vs program counts and the reasons each card gives |
| `mkwb.py` | writes the synthetic workbooks |
| `tok.js` | a faithful copy of the tokenizer run outside the page: what survives, stem collisions, proper nouns dropped, stopwords hit, -ly words dropped |

**Test data:** ask him for `bear-canyon-workbook-2026-11-07.json` (the real
one, line map, 24 notes) and `bear-canyon-workbook-2026-11-05.json`
(Broadview, place map). The `data` key goes straight into localStorage. They
are not kept in the repository. `mkwb.py` writes everything else.

**Run a non-wildfire workbook every time.** It is what exposed the domain
lexicon corrupting other subjects. **Run a place-map workbook every time.**
Place-map bugs have hidden behind line-map assumptions more than once.

# Unverified

iPad and touch; the live page `/gsmlive`; the PDF export (does not include IN
THE WORDS, WHO DID WHAT, or the combined reading, and v95–v99 are untested
against it); Leaflet place-map rendering, since the harness blocks tiles;
combine/merge across workbooks.

# Known limits

Readings are templates driven by word matches and do not understand meaning.
Figure positions and hidden links are not merged on combine. Place-map full
screen has no note sheet. Names are self-declared. Pop-ups show static clones.

# The ceiling, which he has not decided on

The engine reads vocabulary, not claims. It can say "tradition is a gap"; it
cannot say "your Q.5 designs tools and media while your Q.2 says the obstacle
is an occupational complex." Going past that needs claim extraction or a
language model, which ends the self-contained, deterministic, private design.
His call, not yet made.

# Open questions for him

- `community` / `communities` / `people` / `person` in the stopword list —
  keep suppressing, or let them become patterns? (See item 3.)
- The In Parallel line for Start Here, in his words.
- Should the length work extend to Pattern Analysis and In Parallel, or only
  Pattern Synthesis?
- Does the bottom clipping he sees match the 16 units measured?
- Whose figure position wins when two people move the same dot on combine?
- Does the place map's full screen need a note sheet?
- Change the two older "the problem" sentences to question-number wording?
- Should the PDF include the new sections, and the version number?
- Cut `/gsmlive` over to the hosted file?

# Deferred (offered, not requested)

The v93 spatial strip for place-map workbooks; deleting WHAT REPEATS and
cutting EACH QUESTION; which section owns the for-and-against finding; the
Why-line overlap with the decision sentence; card titles that read as
fragments; declutter the hang figure; PDF additions; Keep/Change/Drop "Switch
to (other strategy)" button; mobile optimization; **Esri key renewal before
2027-11-05**.

# Lessons, carried forward and re-earned

- **Do not state a guess as a finding.** This session said the -ly fix would
  surface "costly" and "deadly" on screen. It did not — they are counted but
  rank too low to print. Caught by looking, not by reasoning.
- **Run the code before describing it.** Everything in the audit came from
  rendering pages to text and reading them, and from running a copy of the
  tokenizer over his actual words.
- **Verify the thing you changed, not the thing you meant to change.** The
  "feeling" replacement missed two all-caps section titles, and the
  full-screen title first attached to the wrong code path. Both were found by
  checking the rendered page, not the diff.
- **Ask him for the artefact.** His saved workbook turns a general evaluation
  into a specific one in one step.
- **Test on a workbook that is not about wildfire, and on a place map.**
- **Quote him his own cost.** He stopped a two-hour build at 75% usage and
  asked for the light subset instead. Offer the cheap version first and give
  an honest estimate; tonight's first estimate was three times too high.
