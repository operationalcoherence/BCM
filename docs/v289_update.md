# v289 — a plural word after a preposition counts as a thing

His concern, 25 Nov 2026 19:28: asking about every doubtful word "bothers the user with our shortcomings". So no new questions; the v288 test is widened instead. Change in gsm-readable.js (diff: `tools/patches/v289_plural_after_preposition.diff`).

`gsmThing` also accepts a word that ends its phrase, is plural (ends in s, not ss/us/is/ys), is at least five letters, and follows a preposition (to, for, of, in, on, with, about, from, by, into, toward, over, against, among, between, without): "a threat to referrals". A short list of -s adverbs (always, sometimes, perhaps, afterwards…) never counts. The other two checks (two places, always shown with its context) are unchanged.

Results: clinic gains "residents" (with its sentence); "referrals" now qualifies (on the clinic test its place in WHERE THESE MEET is taken by N1, which carries the same sentence). 11-20 unchanged. matrix.py, vague_titles.py, ta_flow.py pass.
