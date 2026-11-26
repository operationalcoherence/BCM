# v291: Pattern Analysis and Taking Action, third tidy pass

His go-ahead, 25 Nov 2026 21:22. Patch: tools/patches/v291_no_asks_single_words.py.

## His rule: no one-tap questions to cover what the engine can't tell (19:28)
Removed, each finding now says what it can without asking:
- IN YOUR ANSWERS, NOT ON THE MAP: "A phrase can be a theme or just wording, and Patterns cannot tell which, so it asks. … Is it a theme?" (both kinds). Now: the phrase appears in one note at most, "so the map has not caught up with it yet."
- DOES THIS SERVE THE GOAL? (Taking Action): "Patterns cannot tell which, so it asks. … Does it serve the goal?" Now: "It may be off the goal, or the goal may only be worded differently," with the notes listed. The notes still move to Taking Action (gsmGoalQ now finds them by class `.gq`).
- A LOOP BETWEEN GROUPS: "Does the aggression in N38 come from …?" Now: "Whose it is decides whether this is a loop: worth finding out before acting on either side."
- TWO WAYS OF RUNNING: "Is the goal two ways of running …?" dropped; the "If both are meant to stay" reading stays.
Kept, flagged to him: THE SAME THING? (his own rule: never merge words unless he says) and DOES THIS ANSWER THE GOAL? (he renamed it on 25 Nov). Answers already saved under the removed questions still count.

## His single-word rule, where it still leaked
- WHAT STANDS OUT word lists (`uo`): single words that are not things are dropped; a finding left with no statable words is removed (e.g. "command; control; act", "organization; working; adaptive"). The "For <word>:" clauses in CROSSES THE GROUND LINE and CONDITION IN THE WAY follow the same test.
- WHAT YOU WOULD DO: "deals yet with yet (N3), strong (N7), and philosophy" now "deals yet with science (Q.1, Q.2, and Q.4)".
- `gsmThing`: "that/this/these/those" after a noun is a relative word, not a determiner, so "constraints that permit" no longer makes "permit" a thing. New helper `gsmOkW`.

## Repeats and one first move
- ONE EMOTION, SEVERAL TARGETS: the people-versus-ideas sentence is said once, not once per emotion.
- POSSIBLE PATTERNS: the generic "“x” sits behind two findings at once" lines are dropped.
- THE CHEAPEST FIRST MOVE no longer has "Decide organizational transformation first" under it (a second, vaguer first). WHERE TO START on Pattern Analysis now says the same first move as Taking Action, with the cards' final titles.

## Side effect to know
Because fewer words count as things, the set of WHAT STANDS OUT findings on 11-20 changed: two RUNS TOGETHER built only on loose words are gone, BUILD ON WHAT IS HAPPENING (keyed on "organization; change") no longer shows, and CONDITION IN THE WAY now does.

## Checks
- matrix.py on 11-20 (full text, tests/w20full.json), 11-13, Broadview and every mkwb workbook: no page errors, no injection.
- fulldump on 11-20, 11-13, Broadview, clinic: no question buttons left of the removed kinds, no empty findings.
- ta_flow.py: ALL PASS. vague_titles.py: one FAIL on 11-13 ("Redesign “aggressive suppression” with those who oppose it"), already present in v290; next.
