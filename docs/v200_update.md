# v200 update (2026-11-18)

Phase 1, step 4 of the review plan, first half: the phrase-and-meaning layer (P1) on Taking Action. Patch: `tools/patches/v200_phrases_cards.py` (engine only, for every workbook).

## 1. Card titles are phrases, never a lone word
- A card that grows from a recurring word is titled with the phrase around that word that the workbook uses most: two to five words, taken from the goal, the answers, and the notes. Ties go to the goal's wording, then to the phrase whose other words recur most. Names stay whole and are never split for a phrase ("Fire Adapted Colorado" doesn't feed "fire"). Words such as "including", "throughout", and "toward" never glue onto a phrase.
- A card built from Q.3, Q.5, Q.6, or Q.7 is titled with the clause it came from, starting at its phrase. A clause that is only a list item takes the rest of its list.
- Hovering a title shows the whole sentence it came from.
- Two cards never share a title. WHERE THE CARDS MEET and Where to start use the same titles as the cards.

On his 11-13 workbook (before → after): landscape → restoring landscapes; management → wildfire management; media → social media; promoting policy efforts → promoting policy efforts that enable and reinforce the capacity to put fire on the landscape; instead places significant responsibility → places significant responsibility for fire outcomes on the shoulders of home and property owners; combined ideology → combined ideology of suppressing fires that are indeed bad and threaten resources; organizations reinforcement → political, social, and organizational reinforcement. Good fire and aggressive suppression were already phrases and stay.

## 2. IN SERVICE OF THE GOAL on every card
Up to three short sentences, built from the workbook:
- what the goal names about it, quoted ("The goal names 'aggressive wildfire suppression.'");
- what you would design, redesign, or reinforce about it, quoted from Q.5–Q.7 or their notes, with the whole sentence on hover; a card that is itself from Q.5–Q.7 says so ("It is what you would redesign (Q.6)."), and one from Q.3 says it is already working; with nothing to quote it says "Nothing you would design, redesign, or reinforce names it yet.";
- where the context you've grasped (the Q.1–Q.4 notes) has it helping or holding the goal back. For cards from a clause, those are the Q.1–Q.4 notes that share at least two of its words.

## Wording that is Claude's (flagged)
IN SERVICE OF THE GOAL; "The goal names …"; "What you would design (redesign, reinforce) says …"; "It is what you would design"; "It is already working"; "Nothing you would design, redesign, or reinforce names it yet"; "In the context you've grasped, it helps in … and holds the goal back in …"; "answers what holds the goal back in … / builds on what helps in …".

## Known limits
- On Broadview a few thread phrases stay thin ("right place", "mitigated risk"), because the workbook uses those words in only one or two ways. The purpose lines carry the meaning there.
- A Q.5 note that describes how things are designed today (N16 on 11-13) is still quoted as "what you would design," because it was written under Q.5.
- Program or strategy is unchanged here (P3, v202).

## Tests
- `tests/dump2.py` on 11-13, Broadview, clinic, and hostile: every card has a phrase title and the purpose lines; Pattern Analysis, Synthesis, and In Parallel read exactly as in v199.
- `tests/matrix.py` on 11-13, Broadview, and every mkwb workbook: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-13, Broadview, clinic, and 200 notes.
- `grep -c 'AAPK\|AIza'` = 0.
