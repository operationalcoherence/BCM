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

## Verified

Real, Broadview (place map) and clinic workbooks, across Pattern Analysis,
Pattern Synthesis, In Parallel and Taking Action, every fold open: no page
errors, no remaining "feeling" in any case, no remaining British spelling.
`gsm-readable.js` regenerated from the new build.

## Not in v99

The figure clipping fix, proper nouns, the stopword decisions, the
PRESENT–FUTURE findings, the emotion/placement redundancy finding, and the
Pattern Synthesis rewrite to one screen. All still in `v99_plan.md`, and all
approved by him in scope — only the timing changed.
