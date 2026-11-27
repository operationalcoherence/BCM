# v320: the lead's dashboard in three levels

Gregory, 26 Nov 19:55: "a smooth, clear UI that can be very condensed (at a glance) or granular (each person)". He chose
mockup B, people as cards (design canvas "BCM lead dashboard mockups"; project doc claude/lead_dashboard_design_2026-11-26.md).

- **Two tabs** under the summary: **People** (opens first) and **Project at a glance**.
- **People:** the EVERY WORKBOOK table is now cards in WORKING NOW (saved in the last 5 minutes), STILL GOING, and
  FINISHED (all 7 answered). Each card: name, NOW, last change, voice, a seven-step bar (Q.1 to Q.4 dark, Q.5 to Q.7
  grey), questions answered and notes, main emotion, Open, Remind, Delete. A group past 9 people shows 9 and "Show all N".
- **One person** (Open, or the name): "← Everyone in …"; See their ground and their story (their workbook alone, opened
  as a copy for reading with Pattern Analysis and Taking Action; banner "PROJECT · NAME"); Save as a file; Remind;
  Delete; HOW FAR THEY HAVE GOT by question; NEXT TO THE PROJECT (their emotion mix against the whole project, and the
  splits and agreements they are part of); THEIR ANSWERS AND NOTES, folded.
- **Project at a glance:** what READING THEM TOGETHER held (heading dropped; the tab names it), with HOW FAR THE PROJECT
  HAS GOT added and EMOTION ACROSS THE PROJECT (a Whole project row above the voices, when there are two or more)
  moved up. "Patterns suggests; you decide." still once, at the top. Everything else in it reads word for word as v319.
- No new reads or writes.

Not yet: a written story for the whole project at the top of Project at a glance. The story engine runs on one
workbook; it is one click away through See everyone's ground together. To try next: run it on the combined copy.

Tests: tests/f8dash.py rewritten for cards, the person view, the glance tab, and one person's own copy; f8read.py and
f8cmp.py open the glance tab first. All F8 tests, privacy.py and privacy_lead.py clean at 390 and 1000 px; matrix
matches v319 on clinic, big, and w20.
Patch: tools/patches/v320_lead_three_levels.py.
