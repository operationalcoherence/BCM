# Bear Canyon Method v108 (preview) - update

Written 2026-11-10. Follows v107. One larger batch, on his instruction to take a
big swing rather than small groups, under his standing rule: if a section does
not add value to a meaningful synthesis or analysis and only makes the page
longer, cut it.

## What changed

**Pattern Analysis**

- **A WORD THAT RETURNS, A WORD THAT CROSSES QUESTIONS, SAID, BUT NOT ANSWERED**
  no longer appear. They are still computed, because the POSSIBLE PATTERNS
  lines are built from them (v105 and v107 showed that removing them outright
  loses those). They are now hidden from IN THE WORDS instead. The generic
  "X turns up in two findings at once: A and B" line is also suppressed when A
  or B is one of these three, so the page never names a finding it no longer
  shows. The specific POSSIBLE PATTERNS lines are unchanged.
- **EACH QUESTION** removed. Nothing else read from it.

**Pattern Synthesis**

- **PRESSING NOW** column under WHAT TO PAY ATTENTION TO is hidden. It was
  identical to PRESSING NOW in AT A GLANCE on Pattern Analysis, which reads its
  text from this column, so the column stays on the page invisibly. EMERGING,
  the other half of the block, stays visible; it is said nowhere else. The fold
  count now counts only what shows.

**In Parallel**

- **"The meaning of that meaning"** removed. It recapped the findings directly
  above it, and "Where to start" says the same thing a line later.

## Size, his workbook, every fold open

| Page | v104 | v108 |
| --- | --- | --- |
| Pattern Analysis | 1,860 | 1,425 |
| Pattern Synthesis | 1,957 | 1,492 |
| In Parallel | 1,008 | 904 |

About 1,000 words off across v105 to v108. Counts include the page's fixed
chrome (tabs, buttons, footer), roughly 150 words per page.

## Kept, and why

- **WHAT REPEATS:** each word is a button that lights its dots on the figure.
- **STILL OPEN:** holds findings that appear nowhere else (EMOTION NOT YET READ
  on Broadview).
- **Where to look first** (Synthesis) and **Where to start** (In Parallel):
  they overlap, but merging them is a wording job, not a cut.
- **Words used here / What each picture asks / Read together** (In Parallel):
  they explain how to read the two pictures side by side. Arguable; left for
  him.
- Everything section 6 of `elegance_screening.md` marks as the method working.

## Verified

- Every edit syntax-checked before rendering (one cut in this batch broke the
  page on the first try and was fixed before anything else ran).
- Pattern Analysis, Pattern Synthesis and In Parallel rendered as text with
  every fold open, v107 against v108, on his workbook, Broadview and the clinic
  workbook. Every difference is one of the sections above. POSSIBLE PATTERNS,
  EMERGING and AT A GLANCE are unchanged.
- tests/matrix.py over ten workbooks including both-maps: no page errors.
- Key check 0. `gsm-readable.js` regenerated.

## Wording

No new wording.
