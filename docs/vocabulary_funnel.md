# Vocabulary setting: narrowing the list before asking

Written 2026-11-07, after v98. Nothing here is built. All wording is Claude's.
Addendum to `vocabulary_architecture.md` (read that first). The interface it
describes is drawn in the five-screen mockup:
https://claude.ai/artifact/Vk5rTHDvugvbXGzZ72uG7V

## His point

The vocabulary field would be filled from the notes and answers, and the person
would say "this and this also mean this". It cannot be offered for every word.
Some narrowing has to be done before the person sees anything.

## The funnel (a design, not measured)

1. **Drop what appears once.** On his real workbook, 365 of 559 distinct words
   appear once, so at most 194 words can matter. The engine already keeps a
   recurring list (a word or phrase counts at 2 or more dots, and a phrase
   suppresses its own parts). On his workbook that list holds **109 words and
   phrases** - the figure the page already prints. That list is the pool.
2. **Ask only about terms that carry a finding.** Grouping two words matters
   only if it changes something on screen. Pairs are drawn from terms that
   appear in the top-ranked findings. This shares work with Layer 1 (score and
   select), so the two should be built together or in that order.
3. **Make pairs from free signals.**
   - Same distribution: same places, never apart (rule already exists in In
     Parallel, ONE IDEA UNDER TWO NAMES).
   - Shared head word with a different modifier ("planned ignition" and
     "unplanned ignition"). Usually a deliberate contrast, so ask "same or
     different?" and not "same?". The mockup's Your words screen already
     words this case exactly that way.
   - Author glosses ("as some call it", "or", parentheses). Candidates only:
     the same pattern also produced a plain disjunction and a contrast in his
     text.
4. **Cap and ask once.** Five to eight best pairs, one tap each, answer stored
   in the workbook. The number is a guess; tune it.

## Two readings of "like words or phrases work already done"

- **Narrowing done before the person sees anything.** The funnel above.
- **A ready-made set of like-word groups.** The starter pack (wildfire pack:
  fire = wildfire = unplanned ignition; prescribed fire = RX fire = planned
  burn = planned ignition). Covers terms never written, such as "RX fire"
  (zero mentions in his workbook). The mockup's Opening a vocabulary screen is
  this, as a named file rather than as code.

Both are wanted: the funnel handles what the person wrote, a pack handles what
they did not.

## What the mockup settles

Open questions from `vocabulary_architecture.md`, answered by the five screens:

- **Where the question belongs.** Mapping Change step 2, "describe your notes",
  as a dismissible card above the note list. Not Start Here, not Pattern
  Analysis.
- **Whether a grouping shows on screen.** Yes. A grouped term keeps the dotted
  underline the page already uses for note and question references, and the
  tooltip reads "Counted as one" with the member words and where they were
  grouped. No new kind of mark is introduced.
- **Whose vocabulary wins.** The Opening a vocabulary screen resolves it per
  group, not per file: groups that come in cleanly, groups that need a
  decision because a word is claimed on both sides, and groups that wait
  because the words have not been written yet.
- **Naming a group.** The most-used member is proposed; the others stay
  visible wherever the group appears; the person may type their own name.

## Still standing

- Default stays split, never merge. Nothing groups without the person's tap.
- A workbook carries its own vocabulary inside it, so it reads the same for
  whoever it is sent to. A vocabulary file is the separate thing that carries
  groups between workbooks.
- The mockup's counts are placeholders from before v98 (it shows fire 29 /
  wildfire 29, and elsewhere 24 / 18 / 2). The engine at v98 reports fire 19
  dots, wildfire 16, suppression 13, good fire 10. The built version must take
  real counts, and the "too faint to be reported" line needs checking against
  the live threshold, which reports anything at two dots or more.
- The Entry screen labels the emotion chips "Feeling"; his instruction is that
  this word is always "emotion".
