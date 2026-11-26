# v293: no goal-word card titles; the one-story fold follows the story rule

**Card titles (Taking Action).** A title made only of the goal's own words now names the note the card rests on instead, hindering notes first, with its id. On 11-13, 'Redesign "aggressive suppression" with those who oppose it' becomes 'Redesign "aggressive attack culture within the wildfire profession" (N17) with the people who hold it'. A card asked again keeps the note it got the first time. Applies to every workbook. Patch: tools/patches/v293_goal_word_titles.py.

**"The whole workbook read as one story" (Pattern Analysis).** Under his story rule (24 Nov), the base story no longer quotes Q.1 or notes and has no note ids. It reads the map by emotion and place ("In the present, close at hand, what holds the goal back carries aggression and indifference"). WHAT STANDS IN THE WAY, WHAT IS ALREADY HELPING, WHAT HAS TO BE TRUE, WHAT YOU WOULD DO, and WHERE TO START are now plain paragraphs with no labels. The WHAT HAS TO BE TRUE sentence that only restated the question is gone. The list of word fragments under WHAT YOU WOULD DO is now "most" or "some of what stands in the way". On workbooks with one story, YOUR STORY SO FAR gets the same change. Patch: tools/patches/v293_story_no_quotes.py.

Left as is, for him to call: the closing line about the word used on both sides ("you use "fire" on both sides…") still shows short phrases from his words.

Checks: vague_titles.py on 11-13 and clinic: ALL PASS. matrix.py on 11-13, w20, clinic, empty, one: no errors. Story fold on 11-13: 0 note ids. Broadview (place map) not rerun this session.
