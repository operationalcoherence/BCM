# F8 build plan: live projects for leaders

Written 26 Nov 2026, after v303. Based on BCM_ARCHITECTURE.md §12a, the F8 mockup, and Gregory's 11-17 direction.
Estimate: 6 to 9 versions over several desktop sessions.

## Already done (26 Nov)

- **Security rules:** `firebase/firestore.rules`. They're drafted and tested but not deployed; the live database stays fully locked.
  34 tests in `firebase/rules.test.mjs` run on GitHub on every change to `firebase/` ("Firebase rules tests"). All pass.
- **Key check:** `sh tools/keycheck.sh` replaces the manual `grep -c 'AAPK\|AIza'`. Esri keys always fail. One Google
  key is allowed only if it is listed in `tools/allowed_keys.txt`, which is empty until the build.
- **Privacy note for the solo version:** the "BCM privacy note (draft)" doc artifact.

## How the data is laid out

| Path | Who reads | Who writes |
| --- | --- | --- |
| `projects/{pid}` | the lead | the lead (Google sign-in); can't be handed to another lead |
| `projects/{pid}/keys/{key}` | anyone holding the link (one key, never the list) | the lead; `open: false` stops saving |
| `projects/{pid}/workbooks/{uid}` | that person, and the lead | that person only, while their key is open |

- **Leads:** sign in with Google.
- **People answering:** Firebase signs them in anonymously in the background, with nothing to type and no account. The link
  carries the key, a random string of at least 20 characters.
- **Workbook fields:** `uid, key, name, voice, data, saved`. `data` is BCM's own workbook format (schema §11), so moving off
  Firebase later stays easy.

## Build order

1. **v1, the opening page:** On my own · Combine workbooks · Lead a project. Only the first two work yet; Lead a project shows "coming soon". **Done in v306** (top of Start Here).
2. **v2, Firebase wired in:** the web key goes in `tools/allowed_keys.txt`; Google sign-in for leads; anonymous sign-in for
   people answering. Use test data only.
3. **v3, Lead a project:** name, shared goal (lead-only), voices plus **Other** write-in, due date, map, invite link (copy,
   email, QR).
4. **v4, invited person:** the link opens the workbook with the lead's goal and map; they add a name and a voice. Saving is live,
   about every 30 seconds: "Sharing with <lead> · saved N ago", with Pause sharing. If the free daily write cap is hit, work
   stays on the device and is sent later.
5. **v5, dashboard core:** "Open a project I lead" shows EVERY WORKBOOK as a table: voice, questions answered, notes, main emotion, last
   change, Open, and Remind. It also counts people started and working now.
6. **v6, dashboard reading:** everyone's ground on one 3D relief with a voice filter; WHERE THEY AGREE / WHERE THEY SPLIT;
   emotion by voice; WHAT NOBODY HAS SAID YET; "Patterns suggests; you decide." said once.
7. **v7, wrap-up:** compare two people or voices; take everyone to Taking Action; a file route kept as a fallback ("Add it" link);
   the full privacy page; App Check; deploy the rules.
8. **v8 to v9, test and fix:** with one real team.

## Needed from Gregory

**Before v2:**

- **The Firebase web key and config.** Paste it in chat on purpose during v2, never before. Restrict the key to the BCM sites in Google Cloud.
- **Turn on Anonymous sign-in.** Firebase console → Authentication → Sign-in method. Google is already on.

**Choices, before v3 (one decided):**

1. ~~Who may lead a project?~~ **Decided 26 Nov: anyone who signs in with Google.** The rules already allow this.
2. How long answers are kept, and who can delete them? The rules already let a person delete their own workbook, and a lead delete any workbook in their project.
3. Does the file route stay for people who don't want to share live?
4. Which account owns the Firebase project long term?

**Before real answers go in:** the full privacy page, with a short legal look.

## Rules for every F8 version

- Stay on the free Spark plan. Never move to Blaze without Gregory's yes.
- Run `sh tools/keycheck.sh` before every push.
- Rule changes ship only with passing tests.
- The solo version must keep working with no sign-in at all.
