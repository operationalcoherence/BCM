# Build a 20-person BCM test project in real sentences, with planted clusters, traps, early threads and loose notes.
import json, random, zipfile, datetime
random.seed(27)
AGG, ACC, DIS, IND, DEF = 0, 1, 2, 3, 4
EN = ['aggression', 'acceptance', 'distrust', 'indifference', 'defiance']
V = ['Residents', 'Fire crews', 'Land managers', 'Other: school board']
GOAL = ("Build a shaded fuel break along the upper canyon road, above the homes, by next fall, "
        "working with the people who live, work, and go to school in the canyon.")

# Planted clusters: id -> (emotion, about, centre x, centre y, question)
CL = {
 'C1': (ACC, 'protecting the homes above the road', 190, 45, 5),
 'C2': (DIS, 'who decides where the line runs', 70, 175, 2),
 'C3': (AGG, 'thinning near the houses', 95, 200, 2),
 'C4': (IND, 'the plan from last spring', 125, 130, 3),
 'C5': (ACC, 'the crews already doing the work', 115, 60, 3),
 'C6': (DIS, 'funding stopping halfway', 165, 185, 4),
 'C7': (DEF, 'outside agencies on our land', 55, 210, 2),
 'T1': (AGG, 'the evacuation route (early thread)', 150, 160, 4),
 'T2': (ACC, 'grazing as a tool (early thread)', 230, 70, 7),
 'C8': (DEF, 'landowners refusing access', 80, 195, 2),
 'T4': (ACC, 'chipper days (early thread)', 205, 55, 5),
 'T3': (DIS, 'smoke on school days (early thread)', 200, 170, 6),
}
# (person, question, emotion, group, how it should match, text). how: same / similar / placed / meaning / far
# 'far' = placed well away from its cluster, so only the words can find it.
P = [
 (1, 5, ACC, 'C1', 'same', 'Protecting the homes above the road is worth doing.'),
 (5, 5, ACC, 'C1', 'same', 'The break would protect the homes above the road.'),
 (2, 1, ACC, 'C1', 'similar', 'Glad the line would shield the houses up above the canyon road.'),
 (3, 5, ACC, 'C1', 'far', 'Protection for the houses above that road makes sense to me.'),
 (4, 5, ACC, 'C1', 'meaning', "If the hillside burns, the families up the hill need a buffer. I'm for it."),
 (1, 5, ACC, 'C1', 'placed', 'Worth it for our neighbours up the slope.'),
 (9, 2, DIS, 'C2', 'same', 'Who decides where the line runs? Not us, it seems.'),
 (13, 2, DIS, 'C2', 'same', 'Nobody has told us who decides where the line runs.'),
 (8, 2, DIS, 'C2', 'similar', "We don't trust how the route of the break gets decided."),
 (12, 2, DIS, 'C2', 'far', "Decisions about the line's route are made behind closed doors."),
 (17, 2, DIS, 'C2', 'meaning', 'I suspect the people drawing the map have already made up their minds.'),
 (9, 2, DIS, 'C2', 'placed', 'We were never asked where it should go.'),
 (5, 2, AGG, 'C3', 'same', 'Furious about the thinning near the houses.'),
 (17, 2, AGG, 'C3', 'same', 'Angry that thinning near the houses will strip our privacy.'),
 (9, 2, AGG, 'C3', 'similar', 'Thinning close to our houses makes my blood boil.'),
 (16, 2, AGG, 'C3', 'meaning', "Cutting trees right next to people's homes is outrageous."),
 (13, 2, AGG, 'C3', 'placed', 'The chainsaws by the houses have people up in arms.'),
 (3, 3, IND, 'C4', 'same', "Last spring's plan? Never read it, and don't much care."),
 (7, 3, IND, 'C4', 'same', "Indifferent to last spring's plan; plans come and go."),
 (11, 3, IND, 'C4', 'similar', "The plan from last spring doesn't change much for me."),
 (10, 3, IND, 'C4', 'far', 'That spring planning document sits on a shelf. Whatever.'),
 (14, 3, IND, 'C4', 'similar', 'Another plan from the spring meeting, another shrug.'),
 (19, 3, IND, 'C4', 'meaning', "I haven't looked at what they wrote up in April."),
 (2, 3, ACC, 'C5', 'same', 'The crews already doing the work are the best part of this.'),
 (6, 3, ACC, 'C5', 'same', 'Our crews are already doing the work on the lower road.'),
 (10, 3, ACC, 'C5', 'similar', 'Crews have already started the work, and it shows.'),
 (15, 3, ACC, 'C5', 'similar', 'The work the crews are doing already is solid.'),
 (14, 3, ACC, 'C5', 'meaning', 'The engine crew is out there every week clearing brush.'),
 (18, 3, ACC, 'C5', 'meaning', 'Seeing crew members on the ridge each morning gives me hope.'),
 (11, 4, DIS, 'C6', 'same', "I don't trust the funding to last; it'll stop halfway."),
 (15, 4, DIS, 'C6', 'same', 'Funding always stops halfway through these projects.'),
 (4, 4, DIS, 'C6', 'meaning', 'The grant runs out after one year, and then what?'),
 (20, 4, DIS, 'C6', 'meaning', "Money for the break will dry up before it's finished."),
 (1, 2, DEF, 'C7', 'same', 'No outside agencies on our land, period.'),
 (13, 2, DEF, 'C7', 'same', "Outside agencies don't get to tell us what to do on our land."),
 (17, 2, DEF, 'C7', 'meaning', "We'll block any federal crew that sets foot on our property."),
 (5, 4, AGG, 'T1', 'similar', 'The evacuation route makes me angry; one road out is not a plan.'),
 (9, 4, AGG, 'T1', 'similar', 'Angry that the only evacuation route is the canyon road.'),
 (19, 7, ACC, 'T2', 'similar', "Grazing goats under the trees is a tool I'd welcome."),
 (2, 7, ACC, 'T2', 'similar', 'Using grazing as a tool to keep the grass down would help.'),
 (8, 6, DIS, 'T3', 'similar', "We don't trust them to avoid burning piles on school days."),
 (12, 6, DIS, 'T3', 'meaning', "Smoke drifting into classrooms worries us; I doubt they'll check the school calendar."),
 # traps: must NOT join the cluster they look like
 (7, 2, ACC, 'X-C2', 'trap: same words, opposite emotion', "Glad the county forester decides where the line runs; that's their job."),
 (6, 2, AGG, 'X-C3', 'trap: same word, different object', 'Some neighbours are aggressive toward the crews doing the thinning.'),
]
# Loose notes: one topic each, so they should fall in no cluster.
L = {
 1: [(1, IND, 'I mostly hear about the fire plans from the mail carrier.'), (2, DIS, "The last survey crew left stakes in my garden and never came back."), (3, ACC, 'The volunteer fire department breakfast is the best meeting in town.'), (4, AGG, 'Insurance premiums doubled and nobody can say why.'), (6, ACC, 'A map at the post office would help people see the plan.'), (7, IND, "I'll go to a meeting if there's food."), (1, DIS, 'Our road association has its own ideas about the gate.')],
 2: [(1, ACC, 'Residents who cleared their own brush last year made our job easier.'), (2, AGG, "Some people park across the hydrant every weekend."), (4, IND, 'The weather window for this kind of work keeps shrinking.'), (5, ACC, 'A shaded break keeps the big trees and drops the ladder fuels.'), (6, ACC, 'We could run a ride-along so neighbours see what the work looks like.'), (7, DIS, 'Radio coverage in the upper canyon is spotty at best.'), (2, IND, 'Our seasonal staff turn over every summer.')],
 3: [(1, ACC, 'The soil survey shows the slope can take the equipment.'), (2, DIS, 'Easement records for the upper parcels are a mess.'), (4, AGG, 'Cheatgrass will come in fast if we open the canopy too much.'), (5, ACC, 'We can leave the old ponderosas standing.'), (6, IND, 'Monitoring plots could go in after the first season.'), (7, ACC, 'A youth corps crew could handle the piling.'), (2, DEF, 'One landowner has refused every request to survey since 2019.'), (4, IND, 'Bark beetle numbers are down this year.')],
 4: [(1, ACC, 'Teachers want a lesson on why the forest needs work.'), (2, IND, 'Bus routes might shift while the road work is going on.'), (3, ACC, 'The PTA could host a walk along the break.'), (6, ACC, 'Students could help plant the native grasses afterward.'), (7, DIS, 'We were burned once by a contractor who promised outreach and vanished.'), (1, IND, 'Most parents have not heard about the project yet.'), (3, ACC, 'The high school science club already tracks local weather.'), (6, AGG, 'Parents get loud at board meetings about anything that touches the bus schedule.')],
 5: [(1, IND, 'I moved here two years ago and still learning how things work.'), (3, ACC, 'My neighbour lent me his chipper; that kind of help is common here.'), (6, DIS, 'The county website is impossible to find anything on.'), (7, ACC, 'A phone tree would reach the older folks better than email.'), (1, AGG, 'Tourists leave campfires burning at the trailhead.'), (3, IND, 'The elk come through every evening, fire break or not.'), (5, ACC, 'I would pay for a chipping day if it came to my road.')],
 6: [(1, ACC, 'Residents on the east side wave us down to ask questions.'), (4, DIS, "Dispatch doesn't always know which side road is which."), (5, ACC, 'Hand crews can work the steep pitch where machines cannot.'), (6, IND, 'Training hours for chainsaw certification are hard to schedule.'), (7, ACC, 'A joint drill with the school would build trust both ways.'), (3, AGG, 'Fireworks on the Fourth are a real problem up here.'), (4, IND, 'Our engine is due for replacement in three years.'), (5, ACC, 'Pile burning in winter keeps smoke low.')],
 7: [(1, ACC, 'The watershed group has volunteers ready to help.'), (3, ACC, 'Past mitigation near the trailhead held up well in the last fire.'), (4, DIS, 'Contractor bids came in far above the estimate.'), (5, IND, 'Archaeological review may add a few weeks.'), (6, ACC, 'Shared equipment between agencies would cut the cost.'), (7, ACC, 'We can phase the work from the bottom of the road upward.'), (2, AGG, 'Off-road riders keep cutting new trails through the treated area.'), (4, IND, 'Snowpack will decide when we can start.')],
 8: [(1, ACC, 'The school is the evacuation point for the whole canyon.'), (3, ACC, 'Our facilities staff already mow a defensible space around the gym.'), (4, IND, 'Board elections in May could change who is involved.'), (5, ACC, "We can share the school's sign board for notices."), (7, ACC, 'A family night could explain the project to parents.'), (2, AGG, 'Some parents are hostile to any work near the playground.'), (6, IND, 'Liability paperwork takes our lawyer months.'), (1, DIS, 'The district office rarely answers our emails about safety.')],
 9: [(1, ACC, 'I grew up in this canyon and want my kids to stay.'), (3, IND, 'The road gets plowed late every winter anyway.'), (5, ACC, 'I can host a meeting in my barn.'), (6, DIS, "My well is near the planned access road and nobody has checked it."), (7, ACC, 'Neighbours share trucks for hauling slash.'), (1, AGG, 'The power company trimmed my trees badly last year.')],
 10: [(1, ACC, 'Fire behaviour modelling shows the break slows a run up the slope.'), (2, DEF, 'A few residents have said they will never let us on their land.'), (4, IND, 'Overtime budgets get tight by August.'), (5, ACC, 'Masticators can work the flatter sections fast.'), (6, ACC, 'We could post weekly progress photos online.'), (7, ACC, 'Cross-training with the land agency is overdue.'), (1, IND, 'Most calls up here are medical, not fire.'), (2, AGG, 'People yell at us when we close the road for an hour.')],
 11: [(1, ACC, 'The canyon has a good record of neighbours helping each other.'), (2, DEF, 'The ranch at the top will not sign any agreement.'), (5, ACC, 'Thinning prescriptions can follow the contour.'), (6, ACC, 'Seed mixes from local sources do best here.'), (7, IND, 'Permits move at their own pace.'), (2, AGG, 'Trespass grazing on the lower parcel causes fights every summer.'), (5, ACC, 'Slash can go to the biomass plant down valley.'), (7, ACC, 'A shared calendar between agencies would avoid clashes.')],
 12: [(1, IND, 'Enrollment is dropping, so the school has other worries.'), (3, ACC, 'Our counsellor runs a wildfire anxiety group for students.'), (4, AGG, 'The teachers union is angry about after-hours duties.'), (5, ACC, 'We can lend classrooms for evening meetings.'), (7, ACC, 'Older students could earn credit by volunteering.'), (1, DIS, 'Families who rent rarely hear about anything.'), (3, IND, 'The cafeteria would need notice for any big event.'), (6, ACC, 'A school newsletter reaches almost every household.')],
 13: [(1, IND, 'I only come up on weekends in summer.'), (3, ACC, 'The fire chief came to our potluck and answered every question.'), (5, ACC, 'Clearing around my propane tank was easy once someone showed me how.'), (6, DIS, 'Last time a crew came through, they left the gate open and my horses got out.'), (7, IND, 'I would read a one-page update; anything longer I skip.'), (1, ACC, 'The church hall is free for community meetings.'), (4, AGG, 'Speeders on the canyon road scare everyone.')],
 14: [(1, ACC, 'The volunteer roster grew by six people this year.'), (2, IND, 'Night shifts are hard to staff in winter.'), (4, DIS, 'The new radios have not been programmed yet.'), (5, ACC, 'The new saw chains last longer than the old ones.'), (6, ACC, 'A ride-along for the school board could open doors.'), (7, ACC, 'Mutual aid agreements are already in place.'), (2, AGG, 'Someone keeps stealing our trail signs.'), (4, IND, 'Fuel moisture readings are taken only once a week.')],
 15: [(1, ACC, 'The canyon was treated once in the 1990s and it helped.'), (2, DEF, 'One owner posted no trespassing signs along the whole ridge.'), (4, IND, 'Wildlife surveys are only done in spring.'), (5, ACC, 'We can leave islands of shrubs for the birds.'), (6, ACC, 'A demonstration plot near the road would show what the break looks like.'), (7, IND, 'Staff time is split across four other projects.'), (3, ACC, 'The prescribed burn crew has a good safety record.'), (1, AGG, 'Illegal dumping in the pull-outs is getting worse.')],
 16: [(1, ACC, 'The superintendent supports any project that makes the school safer.'), (2, IND, 'Board members mostly live in town, not the canyon.'), (3, ACC, 'Our drama club made a fire safety play last year.'), (4, DIS, 'Promises of road repair near the school were broken twice.'), (5, ACC, 'We could add the break to the evacuation drill map.'), (6, IND, 'Summer school uses the building in July.'), (7, ACC, 'The booster club could fundraise for signs.'), (1, IND, 'Few board members have walked the upper road.'), (3, ACC, 'The nurse keeps air purifiers for smoky days.')],
 17: [(1, ACC, 'My family has kept a firebreak behind the barn for decades.'), (3, IND, 'I mostly mind my own business up here.'), (5, ACC, 'A chipper day in October would get a good turnout.'), (6, DIS, 'The HOA newsletter twists every story.'), (7, ACC, 'Older neighbours need help moving firewood away from houses.'), (4, IND, 'Property taxes went up again.'), (2, AGG, 'Hunters ignore the closures every fall.')],
 18: [(1, ACC, 'The canyon residents fed us during the last incident.'), (2, IND, 'Equipment breakdowns slow every project.'), (3, ACC, 'Our captain grew up on the upper road.'), (4, DIS, 'Weather forecasts for the canyon are often wrong.'), (5, ACC, 'We can stage equipment at the school lot on weekends.'), (6, ACC, 'Short videos of the work would travel far on social media.'), (7, IND, 'The academy class graduates in June.'), (2, AGG, 'A neighbour threatened a crew member with a shovel last year.'), (5, ACC, 'Hand piling keeps soil disturbance low.')],
 19: [(1, ACC, 'Aspen stands on the north side act as a natural break.'), (2, DIS, 'The state map of parcel lines is out of date.'), (4, IND, 'Elk calving season limits work in May.'), (5, ACC, 'Leave trees can be marked with blue paint.'), (6, IND, 'Post-treatment monitoring needs a volunteer lead.'), (3, ACC, 'Landowners on the south side already signed on.'), (2, AGG, 'Firewood cutters keep taking trees from the plots.'), (6, ACC, 'Photo points every quarter mile would show change over time.')],
 20: [(1, IND, 'Most of our families commute to town for work.'), (2, AGG, "A board member called the project 'a waste' in public."), (3, ACC, 'Our bus drivers know every turnout on the road.'), (5, ACC, 'The school could be a cooling centre on smoky days.'), (6, ACC, 'A student art contest could design the project signs.'), (7, IND, "Next year's budget is still unsettled."), (1, DIS, 'Parents doubt the district will fix the potholes by the bus stop.'), (3, ACC, 'The library has fire history books for the canyon.'), (5, IND, 'The school roof replacement takes priority this year.')],
}
# Short answers: each person answers two questions, so all seven are covered many times.
ANS = [
 'Most neighbours worry about fire but have never been asked what they think.',
 'Residents on the upper road are the most worried and the most divided.',
 'Some people oppose any work they did not ask for, especially near their houses.',
 'The fire crews and some landowners already support the break.',
 'People would need to see the plan, know who decides, and trust the money will last.',
 'A clear map, a named decision maker, and a schedule people can follow.',
 'The school, the fire department breakfasts, and neighbour-to-neighbour help.',
]
SRC = lambda: random.choice([0, 1, 1, 2, 3])
def place(q, emo, help_side):
    x = 10 + (q - 1) * 38 + random.uniform(4, 34)
    y = random.uniform(20, 108) if help_side else random.uniform(128, 215)
    return round(x), round(y)
HELPS = {ACC}
RETAG = {
 'One landowner has refused every request to survey since 2019.': ('C8', 'similar'),
 'A few residents have said they will never let us on their land.': ('C8', 'meaning'),
 'The ranch at the top will not sign any agreement.': ('C8', 'meaning'),
 'One owner posted no trespassing signs along the whole ridge.': ('C8', 'meaning'),
 'I would pay for a chipping day if it came to my road.': ('T4', 'similar'),
 'A chipper day in October would get a good turnout.': ('T4', 'similar'),
}
NEAR = {'The power company trimmed my trees badly last year.': 'near-miss for C3 (trees cut, but not near the houses for the break)',
        'Firewood cutters keep taking trees from the plots.': 'near-miss for C3 (trees taken, different thing)',
        'A demonstration plot near the road would show what the break looks like.': 'near-miss for C1 (same emotion and words, different thing)'}
people = {i: [] for i in range(1, 21)}
key = []
for (who, q, emo, g, how, text) in P:
    if g in CL and how != 'far':
        e, _, cx, cy, _ = CL[g]
        x, y = round(cx + random.uniform(-9, 9)), round(cy + random.uniform(-7, 7))
    else:
        x, y = place(q, emo, emo in HELPS)
    people[who].append([q, x, y, text, None, emo, SRC()])
    key.append({'person': f'Person {who}', 'voice': V[(who - 1) % 4], 'question': f'Q.{q}', 'emotion': EN[emo],
                'group': g, 'about': CL[g][1] if g in CL else CL[g[2:]][1], 'should_match_by': how, 'note': text})
for who, rows in L.items():
    for q, emo, text in rows:
        g, how = RETAG.get(text, ('loose', 'none'))
        if g != 'loose':
            e, _, cx, cy, _ = CL[g]; x, y = round(cx + random.uniform(-9, 9)), round(cy + random.uniform(-7, 7))
        else:
            x, y = place(q, emo, emo in HELPS)
        people[who].append([q, x, y, text, None, emo, SRC()])
        key.append({'person': f'Person {who}', 'voice': V[(who - 1) % 4], 'question': f'Q.{q}', 'emotion': EN[emo],
                    'group': g, 'about': CL[g][1] if g in CL else NEAR.get(text, ''), 'should_match_by': how, 'note': text})
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
wrap = lambda d: {'app': 'groundsmith', 'v': 1, 'saved': now, 'data': d}
books = []
for who in range(1, 21):
    name, voice = f'Person {who}', V[(who - 1) % 4]
    assert len(people[who]) == 10, (who, len(people[who]))
    m = []
    for j, n in enumerate(people[who]):
        m.append(n + [voice, f'p{who}n{j}', name])
    a = [''] * 7
    for k in ((2 * who) % 7, (2 * who + 1) % 7): a[k] = ANS[k]
    w = {'goal': GOAL, 'a': a, 'm': m, 'p': {'m': []}, 'voices': [voice], 'links': [], 'decisions': {}, 'others': [], 'who': name, 'log': []}
    books.append((name, voice, w))
# combined copy, same rules as together() in gsm-readable.js
W = {'goal': GOAL, 'a': [''] * 7, 'm': [], 'p': {'m': []}, 'voices': [], 'links': [], 'others': [], 'who': 'Everyone', 'log': [], 'decisions': {}}
A = [[] for _ in range(7)]
for ri, (name, voice, w) in enumerate(books):
    for k in range(7):
        if w['a'][k].strip(): A[k].append(w['a'][k].strip())
    for n in w['m']:
        c = n[:]; c[8] = f'w{ri}-' + c[8]; c[9] = name; W['m'].append(c)
    if voice not in W['voices']: W['voices'].append(voice)
W['a'] = ['\n\n'.join(x) for x in A]; W['view'] = 'line'
json.dump(wrap(W), open('bcm-fuel-break-test-20-people-combined.json', 'w'), indent=1, ensure_ascii=False)
with zipfile.ZipFile('bcm-fuel-break-test-20-people-workbooks.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for name, voice, w in books:
        z.writestr(f"{name.replace(' ', '-').lower()}-{voice.split(':')[0].replace(' ', '-').lower()}.json", json.dumps(wrap(w), indent=1, ensure_ascii=False))
json.dump(key, open('answer_key.json', 'w'), indent=1, ensure_ascii=False)
print(len(W['m']), 'notes;', sum(1 for k in key if k['group'] in CL), 'planted;', sum(1 for k in key if k['group'].startswith('X')), 'traps')
