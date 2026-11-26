# F8 build plan: live projects for leaders

Written 26 Nov 2026, after v303. Based on BCM_ARCHITECTURE.md §12a, the F8 mockup, and Gregory's 11-17 direction.
Estimate: 7 to 10 versions over several desktop sessions.

## Already done (26 Nov)

- **Security rules:** `firebase/firestore.rules`. They're drafted and tested but not deployed; the live database stays fully locked.
  34 tests in `firebase/rules.test.mjs` run on GitHub on every change to `firebase/` ("Firebase rules tests"). All pass.
- **Key check:** `sh tools/keycheck.sh` replaces the manual `grep -c 'AAPK\|AIza'`. Esri keys always fail. One Google
  key is allowed only if it is listed in `tools/allowed_keys.txt`, which now holds the Firebase web key (added in v307).
- **Privacy note for the solo version:** the "BCM privacy note (draft)" doc artifact.
- **Firebase console set up (26 Nov, 11:20 to 11:30, done in Gregory's Chrome):**
  - The project lives under **operationalcoherence@gmail.com** (console URL `/u/1/`), project id `the-bear-canyon-method`. 2-step verification is on for that account.
  - Sign-in providers: **Google** and **Anonymous** both enabled. Anonymous **Auto clean-up is off** (it would delete anonymous accounts after 30 days; waits on the "how long answers are kept" choice).
  - Authorized domains: `www.operationalcoherence.com` and `operationalcoherence.com` added (plus Firebase's defaults). The workbook script loads from github.io but runs on the Webador page, so github.io isn't needed.
  - A web app **"BCM Preview"** exists; its config is on Project settings → General → Your apps. Copied into the build at v307 (Analytics left out).
  - Browser key (auto created by Firebase): restricted to websites `https://www.operationalcoherence.com/*`, `https://operationalcoherence.com/*`, and `https://the-bear-canyon-method.firebaseapp.com/*` (Firebase's own sign-in pop-up). API list unchanged (25 APIs).

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

## Risks to test (26 Nov)

- **Google sign-in from the Webador page:** use the pop-up sign-in, not the redirect one (some browsers, Safari on iPhone especially, block the redirect). *(Done: v307 uses the pop-up; Gregory confirmed Google sign-in works on his phone, 26 Nov 11:57.)*
- **Workbook size:** Firestore allows about 1 MB per record. *(Checked at v307: the four test workbooks are tens of KB each, and the change log inside a workbook is capped at 1,000 entries, so a record stays far under 1 MB. No split needed.)*
- **Free write cap:** 20,000 writes a day, about 80 person-hours at one save every 30 seconds. Over the cap, work stays on the device and is sent the next day (v4).

## Build order

1. **v1, the opening page:** On my own · Combine workbooks · Lead a project. Only the first two work yet; Lead a project shows "coming soon". **Done in v306** (top of Start Here; pushed as e51e4e2).
2. **v2, Firebase wired in:** the web key goes in `tools/allowed_keys.txt`; Google sign-in for leads (pop-up); anonymous sign-in for
   people answering. Use test data only. Check workbook sizes. **Done in v307–v308:** Firebase (13.4.0, from gstatic) loads only on demand,
   so the solo page never loads it or signs in. `window.gsmF8` offers load, user, onChange, signInLead, signInQuiet, and signOut. No Firestore reads or writes yet.
   Test panel: www.operationalcoherence.com/bcm?f8test=1 (or #f8test); v308 makes it open Start Here and scroll into view (phones opened on the last tab and hid it).
   Anonymous sign-in tested on the live page (one test anonymous user created). Google sign-in confirmed by Gregory on his phone.
3. **v3, Lead a project:** name, shared goal (lead-only), voices plus **Other** write-in, due date, map, invite link (copy,
   email, QR).
4. **v4, invited person:** the link opens the workbook with the lead's goal and map; they add a name and a voice. Saving is live,
   about every 30 seconds: "Sharing with <lead> · saved N ago", with Pause sharing. If the free daily write cap is hit, work
   stays on the device and is sent later.
5. **v5, dashboard core:** "Open a project I lead" shows EVERY WORKBOOK as a table: voice, questions answered, notes, main emotion, last
   change, Open, and Remind. It also counts people started and working now.
5b. **Admin page for Gregory (added 26 Nov, his ask):** a page only Gregory's Google account can open (his uid listed as admin in the
   rules, with tests). Reuses the v5 table. Shows, across all F8 projects: projects, people, saved workbooks, completions, and exports.
   For the solo version: an anonymous counter only (events such as "finished Pattern Analysis" or "exported", no names, no content;
   solo workbooks stay on each person's device and are never seen). Counter writes count toward the free cap, so keep them few
   (one per event, not per save). The privacy note must say exactly what is counted. Traffic itself can also come from Webador's own stats.
6. **v6, dashboard reading:** everyone's ground on one 3D relief with a voice filter; WHERE THEY AGREE / WHERE THEY SPLIT;
   emotion by voice; WHAT NOBODY HAS SAID YET; "Patterns suggests; you decide." said once.
7. **v7, wrap-up:** compare two people or voices; take everyone to Taking Action; a file route kept as a fallback ("Add it" link);
   the full privacy page; App Check; deploy the rules.
8. **v8 to v9, test and fix:** with one real team.

## Needed from Gregory

**Before v2:** nothing left; v2 is done.

**Choices, before v3 (two decided):**

1. ~~Who may lead a project?~~ **Decided 26 Nov: anyone who signs in with Google.** The rules already allow this.
2. ~~How long answers are kept, and who can delete them?~~ **Decided 26 Nov:** a project's answers are kept until the lead deletes the project; anyone can delete their own workbook at any time; a lead can delete any workbook in their project. The rules already allow this. Anonymous Auto clean-up stays **off** (it would delete people's work without warning). v3 needs a "Delete this project" for leads (deletes its keys and workbooks too) and v4 a "Delete my workbook" for people answering.
3. Does the file route stay for people who don't want to share live?
4. Which account owns the Firebase project long term? (Today: operationalcoherence@gmail.com.)

**Before 5b:** which Google account is the admin, and whether the solo version gets the anonymous counter.

**Before real answers go in:** the full privacy page, with a short legal look.

## Rules for every F8 version

- Stay on the free Spark plan. Never move to Blaze without Gregory's yes. (Google Cloud shows a "$300 free trial" banner: ignore it.)
- Run `sh tools/keycheck.sh` before every push.
- Rule changes ship only with passing tests.
- The solo version must keep working with no sign-in at all.
