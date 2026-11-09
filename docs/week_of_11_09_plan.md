# Week of 2026-11-09 — what to build, in order, with estimates

Written 2026-11-08. Supersedes the ordering in `v99_plan.md`, which still holds
for anything not listed here. All wording in this document is Claude's.

Read `handoff_v99.md` first. Its "Latest shipped: v99" line predates v100 and
v101, both of which shipped on 2026-11-08 outside this plan.

## Shipped since the handoff

- **v100** — the map hover heading ends with the note's author, falling back to
  the workbook owner's name. Both maps. `v100_update.md`.
- **v101** — the place map's note hover appears at all. A document-level
  listener had been wiping it a millisecond after the marker set it; place-map
  note hovers had never worked. `v101_update.md`. Also adds
  `tests/placehover.py`, which serves Leaflet from a local copy so the place
  map can be tested at all.

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
item 2, after item 6, for the reason in the next section. This is no longer an
open question; it is a queued change with a known cost (below).

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

So items 2 and 3 move together into one batch after item 6. The cost of this
order, stated plainly: nothing from either ships until item 6 is finished, and
item 6 is the long one.

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

## Build order

Estimates are wall-clock build time at Opus medium, including testing and the
update doc, excluding his review. Ranges, not promises — see the caveat below.

| # | Item | Estimate | Note |
| --- | --- | --- | --- |
| — | Stopword cleanup, the free parts | 10–15 min | 8 duplicates, plus `place's` and `time's`, which the tokenizer can never match. No behavior change. |
| — | Update `tests/tok.js` to the shipped engine, re-baseline both workbooks | 20–30 min | Must precede item 2. See corrections below. |
| 1 | Figure clipping | 45–75 min | Most visible payoff. Compute the viewBox from the union of drawn geometry plus a margin. Verify on all three workbooks, line and place map, full screen at more than one window size. |
| 5a | Duplicate reason in course-of-action cards | 30–45 min | `unanswered === e.c` and `!e.R.act` both fire for any Q.1–Q.4 item whose word is unanswered. Self-contained; the classifier itself is sound and stays as it is. |
| 4 | PRESENT–FUTURE axis produces findings | 60–90 min | Data already there; the x coordinate is read in exactly one place today. New wording, needs his pass. |
| — | In Parallel line into Start Here | 10 min | **Blocked on his copy.** |
| 6 | One screen, all three reading pages | 4.5–8 hr | Split across sessions. Includes Layer 1 scoring, the heavy-overlap-opposite-emotion finding family, and 5b (the correlation discount). Synthesis alone is 3–5 hr; the ranking machinery is shared, so Analysis and In Parallel are mostly selection and folding after that. |
| 2 + 3 | Proper nouns, and the six subject words, together | 1.75–2.75 hr | Do these as one batch after item 6, so they share a single verification pass. Both add terms competing for the same named slots, and the ranking is what arbitrates. Re-measure the clinic and place-map workbooks alongside his. |
| — | Degenerate workbook says nothing | 20–30 min | Edge case. Low value. Can go anywhere. |
| — | "Where to start" can nominate the same word twice | 15–25 min | In Parallel reads: *Start with the contested word "fire", then the unreached cause "tradition", then the bridging thread "fire".* Three roles, no check that they differ. Found 2026-11-08 while screening. |

Roughly **8.5 to 14 hours** for everything above.

Deliberately not scheduled:

- A better `-ly` rule — 45–90 min and genuinely uncertain. A suffix test cannot
  tell an adjective from an adverb, so it may not converge.
- The stem-collision guard — 45–75 min. Latent; all 41 collisions on his
  workbook and the clinic one are legitimate variants.
- `costly` and `deadly` — no separate work. Item 6's ranking is what surfaces
  them.

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
- Does the bottom clipping he sees match the 16 units measured here?
- Whose figure position wins when two people move the same dot on combine?
- Does the place map's full screen need a note sheet?
- Change the two older "the problem" sentences to question-number wording?
- Should the PDF include the new sections, and the version number?
- Cut `/gsmlive` over to the hosted file?
- `elegance_screening.md`: which of the screened sections get cut, which get
  folded, which stay. The duplicates in its section 1 are the only ones Claude
  would act on with a simple yes. Its section 2 was corrected on 2026-11-08
  after he asked whether the "meaning of the meaning" heading is earned: block
  1 on Synthesis holds up and is now marked keep.
- Does the vocabulary feature jump ahead of item 6? Note that its step 2 —
  asking only about terms that carry a finding — needs Layer 1, so it leans on
  item 6 whichever way this is answered.

No longer open: the six subject words (decided, batched with item 2 behind item
6), whether the one-screen work covers all three reading pages (yes), and
whether item 6 precedes item 2 (yes).

## On the estimates

Treat them as ranges. Both items shipped on 2026-11-08 came in under what a
first guess would have been, and v101 only exists because serving Leaflet from
a local copy took ten minutes and exposed a bug that had been invisible for
every prior version. Item 2 is the least trustworthy number here.

The handoff's standing lesson applies to estimating as much as to findings:
offer the cheap version first and give an honest number. **The cheap bundle is
the first three rows — about an hour, all low-risk, and item 1 is the one he
sees the moment it ships.**
