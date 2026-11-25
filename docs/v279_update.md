# v279 · Same Emotion, Different Targets, on Pattern Analysis

Item 5 in his order of the second generation of insight types (BCM_TASK_QUEUE.md, 11-20 20:06). His call: "Next in your order is #5, Same Emotion, Different Targets", 25 Nov 2026 16:04. Patch: tools/patches/v279_same_emotion_different_targets.py.

## What it does
**ONE EMOTION, SEVERAL TARGETS**, a card under WHY IT BEHAVES THIS WAY, after WHO STANDS WHERE. Where a note names its own emotion and what that emotion is aimed at ("distrust in leadership", "aggression toward supporters", "staff distrust the new system"), the target is read from the words that follow. When one emotion is aimed at two or more different targets across three or more notes, the card says the emotion is several things, each answered where it points. It also says whether the targets are people (a group word from v276, or "those who are …") or ideas and things, because each kind moves differently. Up to two emotions are shown, the one with the most targets first. The notes behind it are folded under the card.

`gsmStructSum.targets` keeps the reading for later use (Taking Action).

## How a target is read (general words only)
- The note must name its own marked emotion (aggression, hostile, anger; acceptance, accepting; distrust, distrustful, mistrust, suspicion; indifference, apathy; defiance, defiant, rebellion). Then one of toward, towards, against, in, of, at, over, or about must follow within three words. A verb form also takes its object directly ("distrust the …", "accept the …", "defy the …").
- The target is the words after that, up to a comma or a clause word (to, that, which, will, since, after, and so on), at most four words. Leading "the", "what", "its", etc. and generic heads ("the idea of", "the concept of") come off; a possessive stops it ("leadership's idea" → leadership). "Toward and rejection of …" reads from the second preposition.
- Two targets are one only when they share a word that is not generic. Words are never merged: "leaders" and "leadership" stay two.

## Second piece: an emotion word alone no longer pairs notes
NO RESPONSE YET and DOES THIS ANSWER IT? paired a hindrance with a response when they shared any word. A shared emotion word ("distrust" in N5 and in N14) made every distrust note look answered by N14. Now emotion words don't count for pairing, so a response has to name what the emotion is aimed at. On 11-20: N5 now pairs with Q.5 through "leadership", N38 with N31 through "supporters", and **N6, N19, and N23 now show under NO RESPONSE YET**. The 11-20 review said job security (N19) is its own system that nothing in the plan answers.

## Inactive unless it applies
Silent unless an emotion has three or more notes that name it with a target, and those targets are two or more different ones.

## Results
- His 11-20 workbook: distrust aimed at leadership (N5, N37), the transformation (N4), a complex adaptive system (N6), the organization (N19), and subordinates (N29): the review's five distrusts. Aggression aimed at change (N9), those who are defiant (N16), the complex adaptive system (N26), and supporters (N38).
- A clinic test workbook with six added notes: aggression at the waiting times, the old paper forms, and the receptionists; distrust at the front desk staff (2 notes) and the new booking system.
- Every other test workbook: unchanged (word counts on every tab equal v278).

## Limits
Words only. An emotion the note doesn't name in words, or a target written another way, is missed. "The organization" for N19 is what the words say; the evidence fold shows the full note (job security). People are recognized only from the v276 group words, so for other people ("receptionists") the card uses the neutral sentence.

## Checks
matrix.py (13 workbooks): no page errors, no injection. ta_flow.py on 11-20: pass. No keys in the built file.

## Wording to flag (Claude's)
The title and the whole card: "… here is not one thing. It is aimed at …", "… draws the most of it", the people/ideas sentence, "So no single answer to … will reach it: there are N things to answer, each where it points."
