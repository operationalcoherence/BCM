# Bear Canyon Method v110 (preview) - update

Written 2026-11-10. Follows v109. One comprehensive pass over all three pattern
pages, on his instruction to clear the clutter "for once and for all" rather
than a few sections at a time. Every line on each page was read and judged in
one go.

## What changed

**Pattern Analysis**

- IN THE WORDS no longer shows five findings that repeat what is said
  elsewhere: RESTING ON WHAT WAS SAID and HEARD FROM ONE PERSON ONLY (both in
  WHAT IT RESTS ON and "One voice only" on Synthesis), ONE EMOTION THROUGHOUT,
  ONE SIDE OF THE LINE ONLY (Synthesis's "Help and hinder"), and ANSWERED, WITH
  NOTHING ON THE MAP (STILL OPEN). They are still computed, because POSSIBLE
  PATTERNS is built from them; those lines are unchanged. IN THE WORDS now holds
  A NAME THAT RECURS, MOST OF THE MAP ON ONE QUESTION and POSSIBLE PATTERNS.
- WHAT REPEATS removed: a word-by-dot lookup table. The figure itself is
  tappable and shows the same.
- "Program or strategy" under the Around the goal figure removed. Taking
  Action makes that call.

**Pattern Synthesis**

- "Who you heard from" removed. WHAT IT RESTS ON gives the voice counts, and
  In Parallel's "Voices" draws the conclusion.
- "Most of what recurs appears in Q.5-Q.7..." removed. Its opposite, which
  warns when more is missing than present, stays.

**In Parallel**

- "Words used here" and "What each picture asks" removed. They explained the
  method, not the workbook. "Read together", the finding, stays.

## Size, his workbook, every fold open

| Page | v104 | v109 | v110 |
| --- | --- | --- | --- |
| Pattern Analysis | 1,860 | 1,425 | 1,075 |
| Pattern Synthesis | 1,957 | 1,453 | 1,395 |
| In Parallel | 1,008 | 904 | 791 |

Counts include about 150 words of fixed page chrome each.
About 1,560 words off since v104.

## Deliberately kept

AT A GLANCE, WHAT STANDS OUT, A NAME THAT RECURS, MOST OF THE MAP ON ONE
QUESTION, POSSIBLE PATTERNS, STILL OPEN, both figures and their captions,
ABOUT WHAT YOU COLLECTED, the "What this suggests" paragraphs on Synthesis,
WHAT IT MIGHT MEAN (its buckets hold "patterns that reach the goal" and
"patterns needed to reach the goal"), WHAT IT RESTS ON, WHAT YOU LINKED
(including its line about unthreaded notes, which carries the "+ Link" call to
action), EMERGING, and all of In Parallel's findings, patterns and "Where to
start".

Outliers on Synthesis still makes the false "words nothing else uses" claim;
its rewording is his.

## Verified

- Syntax check (one edit left a broken expression on the first try; caught
  before rendering).
- All three reading pages rendered with every fold open, v109 against v110, on
  his workbook, Broadview and the clinic workbook. Every difference is one of
  the cuts above. POSSIBLE PATTERNS unchanged.
- tests/matrix.py over ten workbooks: no page errors. tests/hover.py: line-map
  hovers work, no errors.
- Key check 0. `gsm-readable.js` regenerated.

## Wording

No new wording.
