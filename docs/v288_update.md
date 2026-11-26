# v288 — single words, with their context

His call, 25 Nov 2026 19:18–19:19: a halfway measure on the one-word rule ("Lease", "clinic", "referrals" should be included). Patch: `tools/patches/v288_words_with_context.py`.

## The rule now (every workbook)
A single word is stated as a finding again when all three hold (`gsmThing`):
1. **It reads as a thing in the user's own words.** Somewhere it follows a, an, the, this, that, these, those, their, our, its, his, her, my, your, each, every, no, or any, with at most one word between ("a stable lease"), and it ends that phrase (the next word is a small word, punctuation, or nothing). So "a strong attitude" does not make "strong" a thing. Very general nouns (thing, way, part, idea, kind, area, level, side, time…) never count.
2. **It comes up in at least two places** (the goal, answers, or notes).
3. **It is always shown with its context**: the user's own clause and where it is, e.g. **lease**: “A stable lease would let staff be hired” (N5).

Emotion names still always count. Anything else stays out, as in v285–v287.

## Where it applies
The Q.5–Q.7 lists (Not in Q.5–Q.7 yet, For and against, Unused support, Q.5–Q.7 only), the word-overlap findings (FOR AND AGAINST, ROOT CONDITION, READY TO REINFORCE, REDESIGN THE RESISTANCE, BUILD OR REBUILD, CONDITION IN THE WAY), WHERE THESE MEET (a word is left out there when its context is a note already listed), and POSSIBLE PATTERNS.

## Results
- Clinic test: clinic, lease, and intake are back, each with its sentence; WHERE THESE MEET is back (N5).
- 11-20: science, context, change, room, value, constraints, and behaviors appear with their sentences; strong, yet, and emergent stay out.

## Tests
matrix.py on 11-20 and the eleven mkwb workbooks (no errors; Analysis time unchanged within noise), vague_titles.py and ta_flow.py pass.

## For his eye
"referrals" (clinic) still does not qualify: it is never preceded by a, the, their, and so on in the test workbook ("a threat to referrals").
