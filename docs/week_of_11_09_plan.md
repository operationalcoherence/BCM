# Week of 2026-11-09 — what to build, in order, with estimates

Written 2026-11-08, updated 2026-11-10 after v111. Supersedes the ordering in
`v99_plan.md`, which still holds for anything not listed here. All wording in
this document is Claude's.

**The build started 2026-11-10.** Three rows have shipped and are struck from
the table below; see "Shipped" directly under this.

Read `handoff_v111.md` first.

## Shipped since the handoff

- **v100** — the map hover heading ends with the note's author, falling back to
  the workbook owner's name. Both maps. `v100_update.md`.
- **v101** — the place map's note hover appears at all. A document-level
  listener had been wiping it a millisecond after the marker set it; place-map
  note hovers had never worked. `v101_update.md`. Also adds
  `tests/placehover.py`, which serves Leaflet from a local copy so the place
  map can be tested at all.
- **v102** (2026-11-09) — the stopword list cleaned: 362 entries to 352, eight
  duplicates and two entries the tokenizer can never match. No behavior change,
  proved by rendering all three reading pages on both workbooks before and
  after. `v102_update.md`.
- **v103** (2026-11-09) — In Parallel's "Where to start" no longer names the
  same word twice. It nominates a contested word, an unreached cause and a
  bridging thread with no check that they differ; on his workbook `fire` won
  two of the three. `v103_update.md`.
- **v104** (2026-11-10) — the hang figure is no longer cut off at the bottom.
  The finished drawing is measured and the frame grows to hold it, never
  shrinking below the old size. Page text byte-identical. **Completes item 1.**
  `v104_update.md`.

- **v105 to v111** (2026-11-10) — the clutter pass, done on his instruction
  ("if it doesn't add value to a meaningful synthesis or analysis and just makes
  the page longer, cut it"). Pages on his workbook, every fold open: Analysis
  1,860 → 1,077 words, Synthesis 1,957 → 1,310, In Parallel 1,008 → 760.
  **Completes item 1, the safe cuts, and goes well past it.** Details in
  `v105_update.md` through `v111_update.md`; the checklist history is in
  `keep_or_cut_table.md`.

v102 and v103 were taken from the queue on 2026-11-09 with very little usage
left, on the principle of running the lowest-impact thing available: the first
because it cannot change behavior, the second because it is logic rather than
wording and so needed no pass from him.

**Next up is Layer 1 scoring, slice 1** (see "Layer 1 in slices" below). Start
it in a fresh session: it costs far less there than at the end of a long one.

## Decisions Gregory made on 2026-11-08

**One screen, by minimizing the existing menus, on all three reading pages.**
Not Pattern Synthesis alone. The existing folds collapse by default and hold
whatever comes off the top. His first framing was that nothing is deleted; he
reopened that himself later the same day ("if it's minimized why does it
exist?"), so see the standard below — folding is the default, cutting is now on
the table where a section earns nothing. Current weights:

| Page | Words today |
| --- | --- |
| Pattern Synthesis | 1,957 |
| Pattern Analysis | 1,860 |
| In Parallel | 1,013 |

**The six subject words are going in, but not yet.** He wants `community`,
`communities`, `people`, `person`, `area`, `areas` read by the engine — decided
2026-11-08 — and chose to wait rather than ship it that day. It is batched with
item 2, after the Layer 1 scoring (6a), for the reason in the next section.
This is no longer an open question; it is a queued change with a known cost
(below).

Why after the ranking: surprise scoring is what demotes a word behaving exactly
as its overall frequency predicts — the same machinery that correctly demotes
`wildfire` in a wildfire workbook. With it in place, the ranking decides
whether these six earn a named place on the page. Without it, nothing does.

**Already measured on 2026-11-08, so do not re-derive it.** A test build with
the six removed from the stopword list was rendered against both workbooks:

- No flooding. Pattern Analysis 1,860 → 1,859 words on his workbook, Synthesis
  1,957 → 1,957. Broadview 1,607 → 1,609 and 1,771 → 1,779. The recurring list
  goes 111 → 114 on his and 30 → 32 on Broadview.
- Real findings appear. `community` enters two on his workbook: the trio "burn,
  fire and community are used together in Q.1, Q.4, Q.6" and the one-voice-only
  line. For-and-against goes 19 → 21. On Broadview `areas` enters four,
  including a new for-and-against finding and second place in "Where to look
  first"; threads tying back to the goal go 3 → 4.
- A phrase becomes reachable that could not exist before: **`vegetated
  areas`**, which needs `areas` unsuppressed to form as a bigram.
- One hand-drawn link stops being counted as "only you see" on Broadview
  (5 → 4). That count is links whose two ends share no word the engine
  recognizes, so the engine gained the word basis for a connection he had
  already drawn.
- The cost is displacement, and it is small but real. Four words stop being
  *named* on the page: `eradicated` and `media` on his workbook, `fire` and
  `cutting` on Broadview. They are still counted — they move into the trailing
  "and N more", which is a hard `slice` with no expander, so an unnamed term is
  not reachable anywhere in the interface. Broadview also loses the
  OPPOSITION NOT YET ENGAGED finding for `landscape`, and its help-side trio
  shifts from "education, emotional and mitigation" to "change, wildfire and
  mitigation", which reads weaker.

That displacement is the whole reason to do this after the ranking rather than
before: nothing currently decides which four terms earn a named slot except
where they happen to sort.

## Why item 6 comes before item 2 (decided 2026-11-08)

He reached this himself. Item 2 admits the largest number of new terms of any
change here — 28 distinct names on his workbook — into the same fixed set of
named slots. The six subject words added three terms and cost four names their
place on the page; proper nouns are roughly nine times that influx. **This part
is reasoning, not measurement:** item 2's displacement cannot be measured until
it is built, unlike the six words, which were rendered from a test build.

A second reason. Layer 1 scores a term by how far it strays from what its
frequency predicts, so admitting 28 new names afterwards shifts that landscape
and the ranking needs rechecking either way. The two orders fail differently:
item 2 first leaves the reading pages flooded until item 6 lands, which is a
state he would be reading; item 6 first costs only a verification pass he never
sees.

So items 2 and 3 move together into one batch after the ranking. Once item 6
was split (see "What comes first"), what gates them is 6a, the scoring, not 6b,
the page rewrite — so the wait is about two hours of work, not the whole long
item.

## The standard item 6 is judged against (set 2026-11-08)

He set this from Gelernter's definition of elegance: power and simplicity. For
an interface, functional minimalism — offer the appropriate core functions
(power) and nothing else (simplicity), as against "the exceeding amount of
less-than-powerful features found in many mainstream applications."

Applied here, that has three consequences.

**The reading pages are the mainstream application in that analogy.** Not in
their menus, in their findings. Pattern Analysis prints a line about names that
recur, a line about numbers appearing in notes, a line about words that signal
necessity, a line about notes using "but". None is wrong. Together they are the
poor layout tools and the worse drawing tools.

**Folding is not minimizing.** His rule has been that nothing is deleted and
everything goes behind a fold. That preserves power and simulates simplicity.
He raised the harder question himself on 2026-11-08: if it is minimized, why
does it exist? So **the Layer 1 ranking must be allowed to drop a finding, not
only fold it.** A page that is merely shorter is not the same as a page that is
elegant. Deciding this in advance is what separates the two.

A preliminary screening of every section on all three reading pages is in
`elegance_screening.md`, for him to rule on. He will go through it in the week
of 2026-11-09.

**It also settles the ceiling, which was open.** Claim extraction or a language
model would buy power by spending all of the simplicity: no longer
self-contained, no longer deterministic, no longer private. By this standard
that is not an upgrade to the artifact, it is a different artifact. The
standard argues for staying under the ceiling and getting more out of what is
already computed. His call still, but he now has a principle to decide it with.

## What comes first (set 2026-11-08)

He asked which things come first judged by the two goals he has set — elegance,
and the engine asking better questions. Four, in this order, about six hours
together.

**0. Figure clipping — shipped as v104 on 2026-11-10.** It served neither
goal; it was a bug fix, placed first at his instruction because it is the one
thing he sees the moment it ships.

**1. The safe cuts, about an hour.** `keep_or_cut_table.md` is the checklist to
work from; `elegance_screening.md` carries the reasoning. Screening sections 1,
2 and 5, plus item 5a. Duplicated findings, the two "meaning of the meaning"
blocks that do not earn their heading, the paragraph describing the drawing,
and the action card giving the same reason twice. 350–450 words off three pages, no finding lost,
no ranking needed, nothing deferred. The only pure elegance work available
before anything else is built.

**2. Layer 1 scoring, split out of item 6 and built alone, about 2 hr.** This
is a change to the plan as first written, where the ranking sat inside a 4.5–8
hour page rewrite. It should not. Scoring gates nearly everything else: cut
versus fold, which terms earn a named slot, whether items 2 and 3 can come in,
which questions are worth asking, whether the funnel can choose its five to
eight pairs, whether `costly` and `deadly` ever surface.

Built alone it is testable alone: score every finding, change nothing on
screen, dump the scores, and check across all four workbooks that the top three
or four are the ones a person would have picked. A wrong ranking is then found
in two hours rather than six, and everything downstream unblocks at once.

**Layer 1 in slices (decided 2026-11-10).** He wants this built but cannot
spend two hours of usage on it at once. Usage comes mostly from reading the
large page file and rendering pages repeatedly, so it is split into four
slices, each worth having on its own, each shippable or checkable alone:

1. **Score WHAT STANDS OUT only.** Its findings already carry what the score
   needs: dot count, voices, whether the goal is touched, help and hinder
   sides. Score them, print the new top seven beside today's for his workbook
   and Broadview, change nothing on screen. He reads the two lists and says
   which is better. About a quarter of the job. **Start here.**
2. **Order WHAT STANDS OUT by that score.** Small, and the first thing he sees.
3. **Score words**, so capped lists name the telling terms rather than the
   most frequent. The larger half; this is what surfaces `costly` and
   `deadly`, and what items 2 + 3 need.
4. **Let low scorers drop.** Small once 1–3 exist.

The score is never shown. His rule "counts only, no scores" stands; the score
only decides order and what gets named.

**3. The question mechanism, with one question, about 2 hr.** The first
question carries the whole cost: answers need somewhere to live (`C.decisions`
is taken by Keep/Change/Drop on the course-of-action cards) and they have to
survive a combine. Every question after it is cheap. Build it once with the
strongest candidate — class 1 in `asking_questions.md`, the contradiction the
engine already finds and already prints: *you put N20 on the hinder side, but
two of the three notes it shares words with sit on the help side. Which is
right?* Per-note, already computed, and the answer corrects the data rather
than merely acknowledging a remark.

## Build order

Estimates are wall-clock build time at Opus medium, including testing and the
update doc, excluding his review. Ranges, not promises — see the caveat below.
The four that came first are, in this table: item 1 (shipped), the safe cuts,
6a and 6c.

| # | Item | Estimate | Note |
| --- | --- | --- | --- |
| — | The safe cuts — checklist in `keep_or_cut_table.md`, reasoning in `elegance_screening.md` | ~45 min | Duplicated findings, the two blocks that do not earn their heading, the figure describing itself. No ranking needed. Pair with 5a, which is the same bug class. |
| — | Update `tests/tok.js` to the shipped engine, re-baseline both workbooks | 20–30 min | Must precede item 2. See corrections below. |
| ~~1~~ | ~~Figure clipping~~ — **shipped as v104, 2026-11-10** | — | The frame is now measured from the finished drawing. See `v104_update.md`. |
| 5a | Duplicate reason in course-of-action cards | 30–45 min | `unanswered === e.c` and `!e.R.act` both fire for any Q.1–Q.4 item whose word is unanswered. Self-contained; the classifier itself is sound and stays as it is. |
| 4 | PRESENT–FUTURE axis produces findings | 60–90 min | Data already there; the x coordinate is read in exactly one place today. New wording, needs his pass. |
| — | In Parallel line into Start Here | 10 min | **Blocked on his copy.** |
| 6a | Layer 1 scoring, built alone | ~2 hr | Score every finding on surprise, reach, consequence and corroboration, with 5b's correlation discount. Change nothing on screen; dump the scores and check the top three or four against human judgement on all four workbooks. Gates everything below. |
| 6b | One screen, all three reading pages | 3–6 hr | What remains of item 6 once 6a is done: selection, ordering, folding, cutting, the heavy-overlap-opposite-emotion finding family, and the new wording for his pass. Split across sessions. |
| 6c | The question mechanism, with one question | ~2 hr | Somewhere for answers to live on `C` that survives combine, plus class 1 from `asking_questions.md`. The first question carries the cost; the rest are cheap. Can run before or after 6b once 6a exists. |
| 2 + 3 | Proper nouns, and the six subject words, together | 1.75–2.75 hr | Gated by 6a, not by 6b — the ranking is what arbitrates, so these can follow the scoring without waiting for the page rewrite. Do them as one batch, sharing a single verification pass. Both add terms competing for the same named slots. Re-measure the clinic and place-map workbooks alongside his. |
| — | Degenerate workbook says nothing | 20–30 min | Edge case. Low value. Can go anywhere. |
| — | The Outliers line claims more than its test supports | 20–30 min | Synthesis says "6 dots share no thread yet (N5, N7, N18, N20, N22, N24). **They use words nothing else uses.**" That second sentence is false for N20, whose word `social` also appears in N4 and N23 — the page says so elsewhere. In Parallel says the same note "shares words with 3 places". The test is presumably about the 8 threads drawn in the figure; the prose claims something larger. Fix the sentence, or the test. Found 2026-11-08. |

Roughly **8 to 13.5 hours** for what is left, of which the three still ahead of
the rest are about five.

Deliberately not scheduled:

- A better `-ly` rule — 45–90 min and genuinely uncertain. A suffix test cannot
  tell an adjective from an adverb, so it may not converge.
- The stem-collision guard — 45–75 min. Latent; all 41 collisions on his
  workbook and the clinic one are legitimate variants.
- `costly` and `deadly` — no separate work. 6a's scoring is what surfaces them.

`asking_questions.md` is a design note, not a scheduled item: the classes of
question the engine could ask from structure it already computes, and the rule
that governs which findings become questions. It generalizes the vocabulary
feature and shares its cap. Not estimated.

The vocabulary feature remains its own version: **4–8 hr** across sessions,
with the mockup's counts needing a 20-minute refresh against the live engine
first. He has said it is what he most cares about, so whether it jumps ahead of
item 6 is worth asking before item 6 starts.

## Corrections found on 2026-11-08, by running the code

**Item 2's measurement is off, and the harness is why.** `tests/tok.js` still
carries the pre-v99 lowercasing rule, so it drops `Good` as a proper noun when
the shipped engine does not. With the live rule the count is **28 distinct
names, 45 occurrences** — not 29 and 46 as the handoff and the audit state. Its
`-ly` exception list is also still 13 entries where the engine has 31, so those
figures are pre-v99 too. Fix the harness before measuring item 2's before and
after.

**"The engine reads none of it" overstates the proper-noun gap.** Pattern
Analysis already prints an observation headed A NAME THAT RECURS, which on his
workbook reads: Mitigate (2 places), Wildfire Design Industry (2 places), Fire
Adapted Colorado (2 places). Capitalized names are therefore detected for that
one line. What they cannot do is become threads or feed any other finding. The
gap is real but narrower than written.

**`good fire` is not split and needs no work.** It reads as a thread on 10 dots
— GOAL, Q.1, Q.2, Q.5, Q.7, N3, N4, N6, N11, N15 — confirmed by rendering
Pattern Analysis, not from the documents. v98's descriptive-word list keeps
`good` holding the chain open without becoming a thread itself, and v99's quote
tolerance recovered `"Good fire"` at the start of a paragraph in Q.1. Only
multi-word *names* still break.

## Still open for him

Unchanged from the handoff unless noted:

- The In Parallel line for Start Here, in his words.
- Does the figure now close properly on his screen? v104 was verified headless.
- Whose figure position wins when two people move the same dot on combine?
- Does the place map's full screen need a note sheet?
- Change the two older "the problem" sentences to question-number wording?
- Cut `/gsmlive` over to the hosted file?
- `keep_or_cut_table.md`: which of the screened sections get cut, which get
  folded, which stay. It is the per-section checklist; `elegance_screening.md`
  carries the reasoning and the confidence marks. The five rows marked
  Duplicate are the only ones Claude would act on with a simple yes. Its section 2 was corrected on 2026-11-08
  after he asked whether the "meaning of the meaning" heading is earned: block
  1 on Synthesis holds up and is now marked keep.
- Does the vocabulary feature jump ahead of item 6? Note that its step 2 —
  asking only about terms that carry a finding — needs 6a, so it leans on the
  scoring whichever way this is answered.

**The PDF workbook is uncoupled from the website** (2026-11-10). It is a
simple workbook in its own right, does not track the reading pages, and is not
expected to match them. So the cuts have no PDF prerequisite, and the older
rule about the export matching the online version no longer applies.

No longer open: the six subject words (decided, batched with item 2 behind item
6), whether the one-screen work covers all three reading pages (yes), and
whether item 6 precedes item 2 (yes).

## On the estimates

Treat them as ranges. Every item shipped so far came in under what a first
guess would have been, and v101 only exists because serving Leaflet from a
local copy took ten minutes and exposed a bug that had been invisible for every
prior version. Item 2 is the least trustworthy number here.

The handoff's standing lesson applies to estimating as much as to findings:
offer the cheap version first and give an honest number. **The cheapest useful
start is now the safe cuts — about 45 minutes, low-risk, and nothing stands in
front of them.** See "What comes first" above.
