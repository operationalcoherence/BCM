# How the method reads words: the general case

Written 2026-11-07, at v97. Companion to the analytics evaluation. All wording
is Claude's. (Spelling normalized to American English for this repository; the
original sits in the Claude project as
`claude/groundsmith_vocabulary_architecture.md`.)

His question: fixing the lexicon strengthens the wildfire case, but what about
every other use that comes after it? This document answers that by testing,
not arguing. Experiments were run on the live engine.

## Experiment 1: what the wildfire lexicon does to a workbook that is not about wildfire

A rural clinic workbook was written - seven answers, eight notes, about keeping
a clinic open and getting residents to primary care. Nothing to do with land,
fuel or fire.

The engine reported its single most pressing pattern as:

> **homeowner: in 10 places, on both the help and hinder sides, for and
> against, in the goal.**

The word "homeowner" appears **nowhere** in that workbook. The lexicon maps
*resident, residents, owner, owners, property, properties* all to `homeowner`,
so "residents", "the strip mall owners" and "the property lease" are counted as
one idea and given a name nobody wrote. "homeowner" appears 57 times across the
output. `trust` similarly absorbs *relationship*, merging "the school nurse
relationship works" with "residents need to trust the clinic".

This is the answer to his question in its sharpest form. **A built-in domain
lexicon does not merely fail to help other domains - it corrupts them,
confidently and invisibly.** Every workbook that follows inherits wildfire's
vocabulary.

## Experiment 2: removing the fire entries from the lexicon

Three variants were built and run on his real workbook:

| Variant | Lexicon change | Did "good fire" appear? |
| --- | --- | --- |
| A | "fire" feeds `wildfire` only | No |
| B | "fire" feeds neither | No |
| C | whole domain lexicon removed | No |

Useful but not sufficient. In B and C the terms do separate properly -
"fire", "wildfire", "suppression" and "burn" become distinct threads instead of
one blob - so the merge damage stops. But his central term still never appears.
Something else was suppressing it.

## Experiment 3: the second suppressor

The engine carries a fixed list of **362 English stopwords**. "good" is one of
them. So are *bad, new, old, right, wrong, big, small, whole, real*.

Worse than dropping the word: in the tokenizer, hitting a stopword **breaks the
phrase chain** - the code resets the adjacency pointer and pushes a null. A
two-word phrase therefore can never span a stopword. "good fire" is
structurally impossible to detect, however many times it is written.

Removing "good" from the list, with the fire entries already out of the
lexicon, produced this immediately:

> Thread: fire - Thread: wildfire - Thread: suppression - **Thread: good fire**
> - Thread: aggressive - Thread: landscape - Thread: force

"Good fire" becomes one of the eight strongest threads and is reported as tying
back to the goal. He wrote it 13 times; the engine needed only to be allowed to
notice.

**This is the deeper general problem, and it is worse than the lexicon one.**
The lexicon damages non-wildfire workbooks. The stopword list damages *every*
workbook, because every field turns some ordinary word into a technical term.
In his field "good fire" is the term of art. In forestry: "old growth", "new
growth", "right conditions", "small diameter" - *old, new, right, small* are
all on the list. Each of those is undetectable today.

## What the engine does well, and should do more of

It already finds phrases from repetition alone, with no vocabulary at all. On
his workbook it found "aggressive suppression", "urban sprawl", "unplanned
ignitions", "managing unplanned". On the clinic workbook, with no medical
vocabulary anywhere in the code, it found "hospital board", "school nurse",
"lease", "clinic".

**That mechanism is domain-free and it works.** It learns the person's terms
from the fact that they repeat them. It is the right foundation for the general
case, and it is currently being undercut by the two hand-written lists sitting
in front of it.

## The principle: split by default, never merge

The two directions are not symmetrical.

- **Splitting** two things the person treats as one: they see two threads, they
  recognize them, the findings are slightly less concentrated. Recoverable, and
  visible.
- **Merging** two things the person treats as different: the distinction is
  destroyed, and the engine reports confident nonsense in its place. Not
  recoverable, and invisible - nothing on screen says a merge happened.

His own workbook is the proof. Its stated goal is **to visualize a distinction**
between two kinds of fire, and the lexicon merged both sides of that
distinction before the analysis began.

So the default must be: **the person's words are the person's words.** Merge
only where the person says to merge.

This is also the method's own rule. "Patterns suggests; you decide." Before
v98 the code decided - silently - that a resident is a homeowner and that fire
means prescribed burning. That is the engine deciding, not suggesting.

## What to do instead

**1. Take the domain lexicon out of the code.** Default to no synonymy. Terms
separate; nothing is invented. *(Shipped as v98.)*

**2. Strengthen phrase detection, which is already the strongest mechanism.**
Let a pair form across a stopword when the pair itself recurs. Frequency of the
*pair* is a domain-free signal that the person has a term of art. "Good fire"
written 13 times is the person telling the engine it is one idea. No word list
can know that in advance; repetition can. *(v98 shipped the narrower form: a
19-word descriptive set that keeps the chain pointer.)*

**3. Let the person declare their own synonyms, in their workbook.** After the
seven answers, show the terms that recur and ask whether any of them mean the
same thing here. He would group wildfire with unplanned ignition, and
prescribed fire with planned burn and RX fire. A clinic would group nothing of
the sort. The domain knowledge comes from the domain expert, lives in their
saved state, and travels with their workbook instead of with the code.
*(Designed in the five-screen mockup; not built.)*

**4. Optionally, ship starter packs.** A wildfire pack he can load in one
click, holding exactly what he described: *fire = wildfire = unplanned
ignition*; *prescribed fire = RX fire = planned burn = planned ignition*. He
loses nothing he has now, and nobody else inherits it. Later packs can be
written for other fields without touching the engine.

Together these invert the earlier design. The engine used to ship a theory of
what words mean and apply it to everyone. Instead it learns each person's
vocabulary from their own repetition, and asks them when it needs to know more.

## Addendum: why the engine cannot work the synonyms out for itself

His follow-up question. Short answer: it already tries, it is right to be weak
at it, and the weakness is a data problem rather than a code problem.

### It already has a synonym detector

Inside In Parallel there is a rule that looks for two terms with the same count
that appear in exactly the same dots and never apart, sharing no words with
each other. It reports them as **ONE IDEA UNDER TWO NAMES**. On the stand-in
workbook it fired: *"'wildfire day' and 'school' appear in the same 4 places
and never apart. They may be one idea under two names, or two things you cannot
separate."*

That is distributional synonym detection - the standard method, in miniature.
There is a mirror rule too, **NEVER IN THE SAME PLACE**, for two frequent terms
that never co-occur. Both are the right shape. Both report at most one pair,
and report it as a curiosity rather than asking about it.

### Why it cannot get much better: there is almost no text

His entire workbook - goal, seven answers, 24 notes - is **1,533 words**. Of
559 distinct words, **365 appear exactly once**.

The term he most wants recognized as a synonym, "unplanned ignition", appears
**twice**. "Planned ignition" appears twice.

Distributional methods work on the principle that words appearing in similar
contexts mean similar things. To compare two terms' contexts you need each one
many times over, in varied surroundings. Word embedding models are trained on
billions of words; even narrow domain models need millions. A workbook is short
by about six orders of magnitude. Comparing the two contexts of "unplanned
ignition" against the twenty-nine of "wildfire" is not a weak algorithm finding
little - there is nothing there to find.

And "RX fire", which he named as a synonym, appears **zero** times in the
workbook. No amount of analysis can recover a term the person never wrote. Only
he can supply it.

### The three ways to get real synonymy, and what each costs

**Ship a pre-learned model.** An embedding table is tens of megabytes against a
319KB hosted file, loaded on every page view. And general-English embeddings do
not contain "unplanned ignition" or "RX fire" as units - the domain terms are
exactly what general corpora lack. It would be a hand-written list again, only
larger and harder to inspect.

**Call a language model.** This would work, immediately and well. It also ends
the current design: the file stops being self-contained, the workbook leaves
the browser (people write community conflict into these, and the privacy
promise changes), the readings stop being deterministic so the same workbook
could read differently next week, and there is a key and a bill to manage.
Those are real costs, not objections - his call, but a different product.

**Learn from the person's own text.** Limited by the word count above, but not
worthless. Three signals cost nothing:

- *Same distribution* - already built, described above.
- *Shared head noun* - "unplanned ignition" and "planned ignition" share
  "ignition". Worth noting that a shared head with a **different** modifier
  usually marks a deliberate contrast rather than a synonym. His whole workbook
  is built on exactly that pattern, so this signal is at least as useful for
  finding distinctions as for finding sameness.
- *Author glosses* - people define their own terms in passing. His text
  contains "the massive wildfire complex- or apparatus, as some call it". But
  the same pattern also produced "the fire is out, or it's not", which is a
  plain disjunction, and "(prescribed fire) or letting unplanned ignitions
  burn", which is a contrast. So glosses yield candidates, never conclusions.

### What this settles

None of these signals is strong enough to justify the engine **deciding**. All
of them are strong enough to justify it **asking**.

That is the same conclusion this document reached from the other direction, and
the data volume makes it firmer rather than weaker. The engine should surface
candidate pairs - "you have used these two in much the same places; are they
the same thing here?" - one tap, answer stored, asked once.

It also means the weak detector is good enough. It does not have to be right.
It has to raise a question worth a second of the person's attention. With 1,533
words to go on, that is the most any method could honestly claim, and it is
what "Patterns suggests; you decide" asks for anyway.
