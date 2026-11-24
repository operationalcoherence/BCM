# v249: Pattern Analysis no longer reads as gibberish

Queue item "Pattern Analysis reads as gibberish" (his screenshot, 11-20). Patch: tools/patches/v249_no_gibberish.py.

## What changed
The phrase layer never names a note by clipped first words any more:
- gsmStName: a note is named by its whole first sentence when that is short (2-9 words, not
  opening on a pronoun, preposition, or connective); else by its opening words only when they
  stop at a natural break and make sense alone (2+ words, not ending on a pronoun, article,
  or connective, not cut off by the word limit); otherwise it has no name and callers show
  its number once (N23, never "N23 (N23)" or "note 36 N36").
- gsmStThemes: a set of notes is named by the phrases at least two differently worded notes
  in it share (2 to 4 words, joined at most by "and", "of", or "to"; no emotion words, no lone
  words); a phrase another theme contains is dropped, and so is one that only repeats the
  goal's own words. WHAT HOLDS THE SITUATION IN PLACE and
  THE OPPORTUNITY lead with these themes, quoted; the evidence under them quotes the notes.
- AT A GLANCE names a gap only by a repeated phrase carried by two differently worded notes,
  never by one word or a stem.
- The phrase finder (phBest) counts a sentence written twice, as in repeated notes, once
  (same first 60 letters, as THE SAME THING? already does), so copies no longer make a
  fragment look like a repeated phrase.
- WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED: a phrase that another phrase contains is
  one theme, under the longer name; the same finding is never named twice in a sentence.
- Taking Action follows (it reads the same names): an unnamed note shows its number once, and a list that starts with a note number keeps it capitalized.

## Before and after, 11-20 workbook (Pattern Analysis)
- WHAT HOLDS THE SITUATION IN PLACE. Before: "Reinforcing aggression, among those, distrusting of subordinates, develop workarounds, there, …". After: "What stands against the goal is one connected body, gathered around “command and control”: 25 notes, each sharing ground with the others."
- THE OPPORTUNITY. Before: "allowing and even enabling free, providing those, for acceptance, …". After: "Most of the alternative already exists, in “Sending supporters of the transformation”, “Performing experiments”, and “Going along with the transition”."
- AT A GLANCE. Before: "The first is “strong”". After: the count only, because none of the five is a phrase two notes share.
- WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED. Before: "Complex adaptive and complex adaptive system turn up together" and N8 quoted twice. After: one theme under the longer name; N8 once.

## Other workbooks
- 11-13: WHAT HOLDS gathers around “wildfire management system” and “fire suppression”; THE OPPORTUNITY around “Fire Adapted Colorado”; AT A GLANCE names “unplanned ignitions”. Its two near-identical refusal notes (N9, N25) no longer make fragments look repeated.
- Broadview: WHAT HOLDS names its three notes, quoted, since they share no phrase. THE OPPORTUNITY quotes its notes whole.
- Clinic: THE OPPORTUNITY quotes “School nurse refers families already” and “Pharmacy owner offers space”.
- The 200-note synthetic workbook is word salad by design; its themes read as such.

## Tested
matrix.py on 11-13, 11-20, Broadview, and every mkwb workbook: no errors. ta_flow.py on 11-20 and 11-13: all pass. stories.py on 11-20: no errors. Before/after text of tabs 2, 3, 6, 4 diffed on 11-13, 11-20, Broadview, and clinic. Key check 0 on both built files. No 3D change. New helper: tests/ev.py (evaluate an expression in the page on a given tab).

## Waiting on him
The new card wording ("What stands against the goal is one connected body, gathered around …") is Claude's.
