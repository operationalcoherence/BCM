// Tests for firestore.rules, run against the Firestore emulator with fake data only.
//   cd firebase && npm install && npx firebase emulators:exec --only firestore --project demo-bcm "node --test rules.test.mjs"
import { test, before, after, beforeEach } from 'node:test';
import { readFileSync } from 'node:fs';
import { initializeTestEnvironment, assertSucceeds, assertFails } from '@firebase/rules-unit-testing';
import { doc, getDoc, setDoc, updateDoc, deleteDoc, collection, collectionGroup, getDocs, query, where, increment } from 'firebase/firestore';

const KEY = 'k'.repeat(24), CLOSED = 'c'.repeat(24), OTHERKEY = 'o'.repeat(24);
let env;
const lead = () => env.authenticatedContext('lead1', { firebase: { sign_in_provider: 'google.com' } }).firestore();
const lead2 = () => env.authenticatedContext('lead2', { firebase: { sign_in_provider: 'google.com' } }).firestore();
const person = (u = 'p1') => env.authenticatedContext(u, { firebase: { sign_in_provider: 'anonymous' } }).firestore();
const admin = (email = 'operationalcoherence@gmail.com', verified = true, provider = 'google.com') =>
  env.authenticatedContext('admin1', { email, email_verified: verified, firebase: { sign_in_provider: provider } }).firestore();
const anon = () => env.unauthenticatedContext().firestore();
const wb = (uid, key = KEY, extra = {}) => ({ uid, key, name: 'Sam', voice: 'Residents', data: { goal: 'x', m: [] }, saved: 1, ...extra });

before(async () => {
  env = await initializeTestEnvironment({ projectId: 'demo-bcm', firestore: { rules: readFileSync('firestore.rules', 'utf8') } });
});
after(async () => env.cleanup());
beforeEach(async () => {
  await env.clearFirestore();
  await env.withSecurityRulesDisabled(async (c) => {
    const db = c.firestore();
    await setDoc(doc(db, 'projects/P1'), { lead: 'lead1', name: 'Test', goal: 'g' });
    await setDoc(doc(db, 'projects/P2'), { lead: 'lead2', name: 'Other', goal: 'g2' });
    await setDoc(doc(db, `projects/P1/keys/${KEY}`), { open: true, goal: 'g' });
    await setDoc(doc(db, `projects/P1/keys/${CLOSED}`), { open: false, goal: 'g' });
    await setDoc(doc(db, `projects/P2/keys/${OTHERKEY}`), { open: true, goal: 'g2' });
    await setDoc(doc(db, 'projects/P1/workbooks/p2'), wb('p2'));
  });
});

// projects
test('a lead creates a project in their own name', () => assertSucceeds(setDoc(doc(lead(), 'projects/P9'), { lead: 'lead1', name: 'n' })));
test('a lead cannot create a project in someone else\'s name', () => assertFails(setDoc(doc(lead(), 'projects/P9'), { lead: 'lead2' })));
test('an anonymous person cannot create a project', () => assertFails(setDoc(doc(person(), 'projects/P9'), { lead: 'p1' })));
test('a lead reads their own project', () => assertSucceeds(getDoc(doc(lead(), 'projects/P1'))));
test('a lead cannot read another lead\'s project', () => assertFails(getDoc(doc(lead(), 'projects/P2'))));
test('a lead lists only their own projects', () => assertSucceeds(getDocs(query(collection(lead(), 'projects'), where('lead', '==', 'lead1')))));
test('a lead cannot list every project', () => assertFails(getDocs(collection(lead(), 'projects'))));
test('a lead cannot hand the project to someone else', () => assertFails(updateDoc(doc(lead(), 'projects/P1'), { lead: 'lead2' })));
test('a lead changes the goal', () => assertSucceeds(updateDoc(doc(lead(), 'projects/P1'), { goal: 'new' })));
test('an invited person cannot change the goal', () => assertFails(updateDoc(doc(person(), 'projects/P1'), { goal: 'new' })));
test('nobody signed out reads a project', () => assertFails(getDoc(doc(anon(), 'projects/P1'))));

// invite keys
test('a person with the link reads that invite', () => assertSucceeds(getDoc(doc(person(), `projects/P1/keys/${KEY}`))));
test('a person cannot list the invites', () => assertFails(getDocs(collection(person(), 'projects/P1/keys'))));
test('a person cannot make their own invite', () => assertFails(setDoc(doc(person(), `projects/P1/keys/${'z'.repeat(24)}`), { open: true })));
test('a lead closes an invite', () => assertSucceeds(updateDoc(doc(lead(), `projects/P1/keys/${KEY}`), { open: false })));
test('another lead cannot touch this project\'s invites', () => assertFails(updateDoc(doc(lead2(), `projects/P1/keys/${KEY}`), { open: false })));
test('a short, guessable key is refused', () => assertFails(setDoc(doc(lead(), 'projects/P1/keys/abc'), { open: true })));

// workbooks
test('a person saves their own workbook with a live key', () => assertSucceeds(setDoc(doc(person(), 'projects/P1/workbooks/p1'), wb('p1'))));
test('a person cannot save into someone else\'s workbook', () => assertFails(setDoc(doc(person(), 'projects/P1/workbooks/p2'), wb('p2'))));
test('a person cannot save with a closed key', () => assertFails(setDoc(doc(person(), 'projects/P1/workbooks/p1'), wb('p1', CLOSED))));
test('a person cannot save with a made-up key', () => assertFails(setDoc(doc(person(), 'projects/P1/workbooks/p1'), wb('p1', 'x'.repeat(24)))));
test('a person cannot use another project\'s key', () => assertFails(setDoc(doc(person(), 'projects/P1/workbooks/p1'), wb('p1', OTHERKEY))));
test('a signed-out visitor cannot save', () => assertFails(setDoc(doc(anon(), 'projects/P1/workbooks/p1'), wb('p1'))));
test('unexpected fields are refused', () => assertFails(setDoc(doc(person(), 'projects/P1/workbooks/p1'), wb('p1', KEY, { admin: true }))));
test('a person reads their own workbook', () => assertSucceeds(getDoc(doc(person('p2'), 'projects/P1/workbooks/p2'))));
test('a person cannot read someone else\'s workbook', () => assertFails(getDoc(doc(person('p1'), 'projects/P1/workbooks/p2'))));
test('a person cannot list the workbooks', () => assertFails(getDocs(collection(person(), 'projects/P1/workbooks'))));
test('the lead reads every workbook in their project', () => assertSucceeds(getDocs(collection(lead(), 'projects/P1/workbooks'))));
test('another lead cannot read them', () => assertFails(getDocs(collection(lead2(), 'projects/P1/workbooks'))));
test('the lead cannot write into a person\'s workbook', () => assertFails(updateDoc(doc(lead(), 'projects/P1/workbooks/p2'), { name: 'x' })));
test('a person deletes their own workbook', () => assertSucceeds(deleteDoc(doc(person('p2'), 'projects/P1/workbooks/p2'))));
test('the lead deletes a workbook in their project', () => assertSucceeds(deleteDoc(doc(lead(), 'projects/P1/workbooks/p2'))));
test('saving stops once the lead closes the invite', async () => {
  await env.withSecurityRulesDisabled((c) => updateDoc(doc(c.firestore(), `projects/P1/keys/${KEY}`), { open: false }));
  await assertFails(updateDoc(doc(person('p2'), 'projects/P1/workbooks/p2'), { saved: 2 }));
});

// everything else
test('nothing outside projects can be written', () => assertFails(setDoc(doc(lead(), 'other/x'), { a: 1 })));

// admin (v314)
test('the admin lists every project', () => assertSucceeds(getDocs(collection(admin(), 'projects'))));
test('the admin reads any project', () => assertSucceeds(getDoc(doc(admin(), 'projects/P2'))));
test('the admin reads every workbook at once', () => assertSucceeds(getDocs(collectionGroup(admin(), 'workbooks'))));
test('the admin cannot change a project', () => assertFails(updateDoc(doc(admin(), 'projects/P1'), { goal: 'x' })));
test('the admin cannot write someone else\'s workbook', () => assertFails(setDoc(doc(admin(), 'projects/P1/workbooks/p2'), wb('p2'))));
test('the admin cannot delete a workbook', () => assertFails(deleteDoc(doc(admin(), 'projects/P1/workbooks/p2'))));
test('the admin cannot list invite keys', () => assertFails(getDocs(collection(admin(), 'projects/P1/keys'))));
test('an unverified admin email is refused', () => assertFails(getDocs(collection(admin('operationalcoherence@gmail.com', false), 'projects'))));
test('the admin email without Google sign-in is refused', () => assertFails(getDocs(collection(admin('operationalcoherence@gmail.com', true, 'password'), 'projects'))));
test('another Google account cannot read every workbook', () => assertFails(getDocs(collectionGroup(admin('someone@gmail.com'), 'workbooks'))));
test('a lead cannot read every workbook', () => assertFails(getDocs(collectionGroup(lead(), 'workbooks'))));
test('an invited person cannot read every workbook', () => assertFails(getDocs(collectionGroup(person(), 'workbooks'))));
test('a lead counts an export on their own project', () => assertSucceeds(updateDoc(doc(lead(), 'projects/P1'), { exports: increment(1) })));
