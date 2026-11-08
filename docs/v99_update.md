# v99 — wording and tokenizer fixes

Shipped 2026-11-07 to `gsm-preview.js`, preview only. All wording Claude's.

Chosen deliberately as the light subset of the agreed v99 scope, late on a
Saturday with usage running low. The rest of that scope is unbuilt and still
listed in `v99_plan.md`.

## What changed

**1. "feeling" becomes "emotion", 24 places.** Including the all-caps section
titles THE FEELING CHANGES and ONE FEELING THROUGHOUT, which a first pass on
mixed case missed. The page had been contradicting itself: the header already
said "23 with emotion" and one section already said "Emotional disposition".

**2. "colouring" to "coloring".** The only British spelling in the file.

**3. A sentence may now open with a quotation mark.** The rule that lowercases
a sentence-initial capital required the capital to sit immediately after the
boundary. A sentence opening with a quote, bracket or dash kept its capital,
was read as a proper noun, was dropped, and broke the phrase chain.

    before  /([.!?;:]\s+|^\s*|\n\s*)([A-Z])/g
    after   /((?:[.!?;:]\s+|^\s*|\n\s*)(?:["“”\(\-–—]\s*)*)([A-Z])/g

The opening punctuation moved inside the first capture group, so the two-group
callback is unchanged. On the real workbook this was costing `"Good fire"` at
the start of a paragraph in Q.1 — the one place he sets the term against its
opposite, and the same phrase v98 was built to surface.

**4. The -ly exception list grows from 13 to 31.** Any token ending in -ly was
discarded as an adverb unless listed. Added: costly, deadly, friendly, timely,
orderly, elderly, lovely, daily, weekly, monthly, yearly, lonely, lively,
silly, holy, ugly, chilly, prickly.

## Measured

Real workbook: the recurring list goes from **109 terms to 111**.

**costly and deadly are counted now but do not appear on screen.** They are in
the 111 and below the terms the page prints. The words that carry his Q.2 —
"Prescribed fires … have been costly, deadly, and destructive" — are visible
to the engine for the first time, but nothing yet ranks them high enough to
report. Layer 1 scoring is what would surface them.

An exception list is the same shape of problem as the domain lexicon v98
removed: it will keep needing additions, because a suffix test cannot tell an
adjective from an adverb. It was taken as the cheap move, not the right one.

## Second batch, same evening: three UI fixes

**5. "Voices." no longer appears twice in a row.** Three sections in the
tangle reading all carried the label `Voices.` and the ordering array `D`
holds that label once, so they sorted to the same rank and stacked. They are
now `Who you heard from.`, `One voice only.` and `A voice not carried
through.`, each added to `D` in the old label's place so the order is
unchanged. (Claude's wording — his to edit.) The separate `Voices.` in
Pattern Analysis is a different section and is untouched.

**6. "What this suggests. What these lines read." no longer doubles up.** The
first heading inside the block echoed the section label above it. Renamed to
`Beyond the picture.` It is not in `D`, so its position is unchanged.
(Claude's wording.)

**7. Full screen now names the figure.** A `.fsname` element is inserted when
a figure opens, reading the nearest preceding `.plab` — "HOW IT HANGS
TOGETHER", "AROUND THE GOAL" — and removed when it closes. It takes the
label's first `span` so the fold's item count and chevron do not come with it.

The real click handler is the delegated listener on `Rt`, not the re-render
path in `Ut()`; both were patched, because the re-render path restores full
screen after a redraw. Escape already closed full screen before this change,
and now clears the title too.

## Verified

Real, Broadview (place map) and clinic workbooks, across Pattern Analysis,
Pattern Synthesis, In Parallel and Taking Action, every fold open: no page
errors, no remaining "feeling" in any case, no remaining British spelling,
one `Voices.` heading rather than two, and the full-screen title correct on
both figures and cleared by Escape. `gsm-readable.js` regenerated.

## Noticed and not done — waiting on him

- **In Parallel is missing from the instructions.** Start Here says "THE FIVE
  PAGES" and lists five; there are seven tabs, and In Parallel appears in
  neither that list nor the glossary. A reader never learns the page exists.
  His copy, so his line to write.
- **A workbook with nothing to distinguish produces no courses of action and
  says nothing.** Reproduced with a deliberately degenerate workbook (12
  identical notes, 7 identical answers): zero cards, no message. An edge, but
  the page should say there is nothing to suggest yet.
- **The synonym mockup's After screen says "The centre."** The live page says
  "The center". Catch it before the screens are built.

## Not in v99

The figure clipping fix, proper nouns, the stopword decisions, the
PRESENT–FUTURE findings, the emotion/placement redundancy finding, and the
Pattern Synthesis rewrite to one screen. All still in `v99_plan.md`, and all
approved by him in scope — only the timing changed.
