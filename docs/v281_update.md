# v281 · TWO WAYS OF RUNNING

Item 7 in his order of the second generation of insight types (BCM_TASK_QUEUE.md, 11-20). Mockup approved, then "build it", 25 Nov 2026 16:46. Patch: tools/patches/v281_two_ways_of_running.py.

## What it does
**TWO WAYS OF RUNNING**, a card under WHY IT BEHAVES THIS WAY on Pattern Analysis, right after A LOOP BETWEEN GROUPS. It looks for an answer that describes two ways of running, each for its own conditions, rather than one way replacing another.

- **Asked first, always.** "Your answers describe two ways of running, not one. Q.2 sets one way when … and another during …" Then where else each condition comes up (support: Q.3 or help-side notes; opposition: Q.1, Q.2 or hinder-side notes; otherwise what you would design), then: "Is the goal two ways of running, each for its own conditions?" Stored in C.asks as `mode|Q<n>`.
- **After Yes:** neither way replaces the other, so the switch is what makes or breaks the goal (who decides that conditions have changed, and what tells them). If one condition ties only to opposition and the other only to support, it says each side already wants one of the two. The risk is an uneven switch, citing any answer or note that names instability or conflict. Then whether what you would design (Q.5–Q.7, design notes) says how the switch is made, reaches part of it, or says nothing.
- **After No:** the card is gone.

At most one card. `gsmStructSum.modes` keeps it (Taking Action not wired).

## How it reads (general words only)
- In each answer sentence that has a contrast word (but, while, whereas, yet, otherwise, instead, still, rather), find condition phrases: when/whenever/during/in times of + the words after it up to a comma or clause word, or "in/on … situations, conditions, times, periods, emergencies, crises, contexts, environments, events, days, weeks, months, seasons, shifts, hours".
- Two conditions with no shared word, and the contrast word between them, make the pair.
- A phrase that reads as a time, not a condition (has been, once, after, before, until, starts, begins), is skipped: "when a complex adaptive system has been officially adopted" (N10) is a time. Notes are not scanned for the pair.
- Ties use each condition's own words, minus generic heads (situations, environment, days…) and words in more than 40% of the workbook's items.

## Results
- His 11-20 workbook: Q.2, "when the environment is conducive to it" and "during emergent situations"; support tied to the second (Q.3, N33). After Yes: risk points to Q.4 (unstable and conflict-prone); design reaches part of it (Q.5, Q.6), nothing says who decides when to switch. Matches the mockup, without the mockup's hand-written summaries of each way.
- Clinic plus one test sentence ("On normal days the front desk runs by appointment only, but during flu season walk-ins are seen first"): asks about "on normal days" and "during flu season".
- Every other test workbook: word counts on every tab equal v280. After No, 11-20 equals v280. Taking Action unchanged everywhere.

## Limits
Words only. It names the conditions, not the two ways themselves ("orderly, as in a hierarchy" in the mockup was Claude's reading, which the engine cannot make). Two conditions in different sentences are missed. "In … times" style phrases can catch ordinary prepositions; the question is what keeps that safe.

## Checks
matrix.py (15 workbooks plus 11-20 with text, Yes and No): no page errors, no injection. The Yes tap was clicked in the page: saved and re-rendered as stated. No keys in the built file.

## Wording to flag (Claude's)
The title and every sentence of the card, including the question and "(you said the goal is two ways of running)".
