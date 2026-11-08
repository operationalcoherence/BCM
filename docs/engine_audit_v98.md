# The engine room: an audit of v98

Written 2026-11-07 against `gsm-preview.js` at v98. All wording below is
Claude's. Everything is measured by running the engine, not by reading the
source and guessing — the two are separated below, and where a defect is latent
rather than observed on real data, it says so.

Method: `gsm-preview.js` was prettified to 12,730 readable lines
(`gsm-pretty.js`) and confirmed to render **identical output** to the minified
file across Pattern Analysis, Pattern Synthesis, In Parallel and Taking Action
on the real workbook. All tests below ran against the prettified file in
headless Chromium with the page served locally and outside requests blocked.

Eleven workbooks were used: his real one (2026-11-07, line map, 24 notes), the
Broadview place-map one (2026-11-05), a synthetic clinic workbook, a 200-note
workbook, an empty one, goal-only, single-note, a 12-identical-note one, a
legacy 9-element-note one, a 10-element twin of it, and one carrying both a
line map and a place map.

---

## What is sound

Worth saying plainly, because it narrows where the work should go.

- **No crashes.** No uncaught page errors on any of the eleven workbooks,
  including empty, goal-only and 200 notes.
- **No injection.** Note and answer text containing `<script>`, `<img
  onerror=…>` and raw SVG tags rendered as text; neither probe fired.
- **Legacy notes are safe.** A 9-element note array and its 10-element twin
  produced byte-identical page text (782 / 772 / 896 / 1,929 words across the
  four reading tabs). His older saved workbooks are not at risk.
- **Performance is not a problem.** Boot 96–197 ms for normal workbooks, 357 ms
  at 200 notes. Tab switches are flat. There is no scaling work to do.
- **Strategy versus program is balanced, not lopsided.** Despite a single
  condition out of six being enough to call a strategy, the split measured
  5/4, 3/5, 3/6 and 3/2 across four workbooks. The classifier is not
  trigger-happy.
- **Stemming does no harm on real data.** All 41 stem collisions on his
  workbook are legitimate morphological variants (burn/burning/burned,
  suppression/suppressed, policy/policies). The clinic workbook had 2, both
  benign.

---

## Defects

### 1. A sentence that opens with a quotation mark loses its first word

The tokeniser lowercases a sentence-initial capital so it is not mistaken for a
proper noun. The rule is `([.!?;:]\s+|^\s*|\n\s*)([A-Z])` — it requires the
capital to come **immediately** after the boundary. When a sentence opens with
a quote mark, bracket or dash, the capital survives, is read as a proper noun,
is dropped, and **breaks the phrase chain**.

Measured on his workbook: one hit, and it is `"Good fire" is an opposing idea…`
at the start of a paragraph in Q.1. His flagship term, lost in the one place he
sets it against its opposite. v98 went to some trouble to let "good fire" form;
this is a residual suppressor of the same phrase.

General, not his: any workbook that opens a sentence with a quotation loses that
word.

### 2. Proper nouns are invisible to the whole analysis

Any word capitalised mid-sentence is dropped and breaks the chain. There is no
exception list and no recovery.

Measured on his workbook: **29 distinct proper nouns, 46 occurrences** — Smokey,
Bear, Fire Adapted Colorado, The Ember Alliance, The Nature Conservancy,
BurnBot, Incident Management Teams, Wildfire Design Industry, FiSci's Mitigate,
Operational Coherence, Colorado, U, S.

His Q.3 answer — what support already exists — is almost entirely a list of
named organizations, and the engine sees none of it. This is the single largest
category of content the engine cannot read, and it is general: for a method
about communities and the actors in them, every person, organization, place and
product is structurally invisible. A clinic workbook loses "Broad Street"; a
county workbook loses the council's name.

### 3. Adjectives ending in -ly are discarded as adverbs

The rule drops any token matching `/ly$/` unless it is one of 13 hard-coded
exceptions (family, supply, apply, rely, early, assembly, ally, july, italy,
anomaly, butterfly, firefly, monopoly).

Measured on his workbook: 14 distinct -ly words dropped, and two of them are
adjectives carrying the core of his Q.2 — **costly ×2** and **deadly ×2**, in
"Prescribed fires … have been costly, deadly, and destructive". Those are the
words that name why the opposition exists, and they are not adverbs.

The exception list is a closed set of 13; English has many more adjectives in
-ly (likely, friendly, timely, orderly, elderly, lovely, daily, weekly). A
suffix test cannot tell an adjective from an adverb, so the exception list will
keep needing additions — the same shape of problem as the domain lexicon v98
removed.

### 4. Six-character truncation can merge unrelated words (latent)

`Nt` truncates every stem to six characters. **This causes no harm on his
workbook or the clinic one** — stated plainly because it would be easy to call
it a bug on theory alone.

It is nonetheless capable of merging unrelated ideas, silently, which is the
failure mode v98 was built to eliminate. Demonstrated colliding pairs:

conservation + conservative → `conser` · contract + contrast → `contra` ·
continue + continent → `contin` · transport + transparent → `transp` ·
construction + constraint → `constr` · compliance + complication → `compli` ·
integration + integrity → `integr` · personal + personnel → `person` ·
information + informal → `inform` · relative + relationship → `relati` ·
sustain + sustainable → `sustai` · interior + interim → `interi`

A workbook about procurement or governance would hit several of these. When it
happens there is nothing on screen to show that a merge occurred — the thread
is simply named after whichever surface form is more common.

### 5. The stopword list has not been audited

362 entries, **354 unique** — 8 duplicates (could, get, got, much, other, same,
way, taken). Two entries, `place's` and `time's`, carry apostrophes, but the
tokeniser strips apostrophes before the lookup, so **neither entry can ever
match**. Harmless in themselves; they indicate the list has never been checked.

More consequential: the list suppresses words that are often the subject rather
than the scaffolding — **community, communities, people, person, area, areas,
support, condition, design, opposition**. Suppressing the method's own question
words (design, redesign, reinforce, support, oppose, condition) is defensible,
since every answer contains them. Suppressing *community* and *people* is a
different matter: a method applied to community problems can never surface
either as a pattern. On his workbook 114 distinct stopwords were hit; overall
**only 44% of his tokens survive to the analysis** (670 of 1,535), and 54% on
the clinic workbook.

### 6. Emotion and map position are the same signal, counted twice

Measured on his real workbook:

| | acceptance | aggression | distrust | indifference | defiance |
|---|---|---|---|---|---|
| **helps** (above the line) | **11** | 0 | 0 | 0 | 0 |
| **hinders** (below the line) | 0 | **7** | 2 | 2 | 1 |

A perfect separation. Every note he placed above the line he also marked
acceptance; not one below it. The engine treats emotion and help/hinder as two
independent signals, so a finding that says "this helps *and* carries
acceptance" is one judgement reported as two agreeing ones — and the planned
Layer 1 "corroboration" score would inflate it further.

Two things follow. The scoring needs to discount signals that are correlated in
a given workbook. And the correlation is itself a finding worth stating: *your
emotion marks and your placement are the same judgement made twice; one of them
is adding nothing.* That reads as a deep observation and costs one cross-tab.

### 7. The same reason is given twice in a course-of-action card

The strategy/program call tests six conditions and names the ones that hold.
Two of them overlap: `"unanswered" === e.c` ("nothing in Q.5–Q.7 answers it")
and `!e.R.act` ("Q.5–Q.7 do not reach it", which is set by `act: e >= 4`, i.e.
the item sits in Q.1–Q.4). For any card anchored on a Q.1–Q.4 item whose word
is unanswered, both fire, and the card reports "…and 1 other thing points the
same way". A fourth and sixth condition — strong emotion, and more hindering
than helping — are correlated for the same reason as defect 6.

Observed on the clinic workbook: "A strategy, because nothing in Q.5–Q.7
answers it, and 2 other things point the same way."

### 8. The PRESENT → FUTURE axis feeds nothing

Confirmed: the x coordinate is read in exactly one place, to order the path
figure in Taking Action. Half of the change map is drawn, labelled and
explained to the person, and contributes to no finding.

It carries a real pattern on his workbook. Splitting the map into thirds:

| | helps | hinders |
|---|---|---|
| present third | 3 | 8 |
| middle third | 6 | 3 |
| future third | 3 | 1 |

What hinders sits in the present; what helps sits ahead. That is a readable
statement about where his difficulty lives in time, and the engine does not
make it.

### 9. A degenerate workbook produces no courses of action at all

Twelve identical notes and seven identical answers yielded **zero** cards in
Taking Action, with no message explaining why. Not a crash, and not a realistic
workbook, but the page goes silent rather than saying there is nothing to
suggest yet.

---

## Where the advancements are, in order of return

1. **Rank and select (Layer 1), with a correlation discount.** Already the
   agreed next piece; defect 6 adds a requirement to it. Fixes the "too long,
   everything at equal weight" complaint on all three reading pages at once.
2. **Let the engine see proper nouns.** The largest body of unread content.
   A capitalised word that recurs across two or more dots is a thread as much
   as any other word; the risk of admitting them is far smaller than the cost
   of dropping every actor in the workbook.
3. **Make the PRESENT–FUTURE axis produce findings.** Zero new interface, the
   data is already there, and it answers a question no other signal answers:
   *when* the difficulty sits.
4. **The quote-start and -ly fixes.** Small, contained, and each recovers words
   the person plainly meant.
5. **New finding families** (Layer 2), including the two named this session:
   heavy overlap with opposite emotion, and signal redundancy.
6. **Narrative synthesis (Layer 3).**

## Housekeeping now resolved

`gsm-pretty.js` exists and is verified identical in behavior to the hosted
file. The standing risk named in the v98 handoff — the project depending on a
lost sandbox with no readable source — can be closed by committing it. Not
done: this session has read-only access to the repository and he has not asked
for it.

## Not covered by this audit

The PDF export, iPad and touch, the live page `/gsmlive`, Leaflet place-map
rendering (the harness blocks tiles), and combine/merge across workbooks.
