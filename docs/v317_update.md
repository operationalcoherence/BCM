# v317: COMPARE TWO (F8 step 7, part 1)

Under READING THEM TOGETHER, after WHAT NOBODY HAS SAID YET. Pick two people, or two voices, from two menus.

- One line first: how many things the two read two ways, how many they share, and which emotion each leans toward
  (and whether there is a ridge of indifference between them).
- WHERE THE TWO SPLIT and WHERE THE TWO AGREE: the same reading as v313, for just these two ("Both put…").
- WHAT ONLY ONE OF THEM NAMES: a phrase one names in two or more places and the other never does. Goal phrases and
  voice names are left out.
- HOW EACH LEANS: help and hinder counts, and an emotion bar for each.
- Shown only with three or more people (with two, the sections above already are the comparison). Follows the voice
  filter. A person and the voice they answer as can't be compared ("Choose two that don't share anyone").
- Phrases of two or three words only. No extra database reads.
- Everything else on the dashboard is unchanged (f8read output identical to v316 outside COMPARE TWO).

Tests: tests/f8cmp.py at 1000 and 390 px; f8read, f8dash, f8lead, f8join, f8admin, matrix.py clean. Key check OK.
Patch: tools/patches/v317_compare_two.py.
