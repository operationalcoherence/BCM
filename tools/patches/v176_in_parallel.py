"""v176: V2, In Parallel shows the landscape (questions and what the ground says on one map) instead of the
petal and tangle figures; its readings stop pointing at figures that are gone."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("""                      '<div class="int2"><div class="intfig"><div class="intcap">AROUND THE GOAL</div>' +
                      st(r) +
                      '<div class="intsub">How far each answer is from the goal</div></div><div class="intfig"><div class="intcap">HOW IT HANGS TOGETHER</div>' +
                      st(i) +
                      '<div class="intsub">How everything ties to everything</div></div></div>' +""",
"""                      ((window.gsmData ? window.gsmData().m || [] : []).some(function (z) {
                        return (z[3] || "").trim();
                      })
                        ? '<div class="intsub" style="margin:4px 0 8px">One map for both pictures: the buttons show each question’s notes on the ground (Analysis); the ground itself, its heights, colors and ridges, is what the notes say together (Synthesis).</div><div class="gterr-host" data-an="1" data-par="1"></div>'
                        : '<div class="int2"><div class="intfig"><div class="intcap">AROUND THE GOAL</div>' +
                          st(r) +
                          '<div class="intsub">How far each answer is from the goal</div></div><div class="intfig"><div class="intcap">HOW IT HANGS TOGETHER</div>' +
                          st(i) +
                          '<div class="intsub">How everything ties to everything</div></div></div>') +""")
rep("""        h.getAttribute("data-an") && (dd.an = 1);""", """        h.getAttribute("data-an") && (dd.an = 1);
        h.getAttribute("data-par") && (dd.par = 1);""")
rep("""        } else if (ANH) {
          D.read = [];
        } else {""", """        } else if (ANH && !data.par) {
          D.read = [];
        } else {""")
rep("""        if (ANH) {
          host._rel.focusQ && host._rel.focusQ(AQ);
          return;
        }""", """        if (ANH) {
          host._rel.focusQ && host._rel.focusQ(AQ);
          if (!data.par) return;
        }""")
rep("""      var stg0 = $("stage"),
        after = stg0.nextSibling;""", """      var stg0 = $("stage"),
        after = stg0.nextSibling;
      if (data.par) {
        sy.innerHTML = "";
        sy.style.display = "none";
      }""")
rep("""          var t = host.querySelector(".gtansay");
          t && (t.innerHTML = say(q));""", """          var t = host.querySelector(".gtansay");
          t && !data.par && (t.innerHTML = say(q));""")
rep("""      stg0.parentNode.insertBefore(hd, sy);""", """      data.par || stg0.parentNode.insertBefore(hd, sy);""")

# readings: no petals, no tangle
for a, b in [
    ('"The petals are even and the tangle is tight. Every answer speaks the goal\'s language, and your answers and notes keep returning to the same ideas.',
     '"Every answer shares words with the goal, and many threads tie your answers and notes to the same ideas.'),
    ('"The petals are even but the tangle is loose. Every answer speaks the goal\'s language, yet the answers and notes share few threads with each other.',
     '"Every answer shares words with the goal, yet the answers and notes share few threads with each other.'),
    ('"The petals are uneven but the tangle is tight. Some answers sit far from the goal (the farthest is "',
     '"Some answers share few words with the goal (the fewest: "'),
    ('"The petals are uneven and the tangle is loose. Some answers sit far from the goal (the farthest is "',
     '"Some answers share few words with the goal (the fewest: "'),
    ('" both resisted and supported, and the tangle shows "', '" both resisted and supported, and the landscape has "'),
    ('" on both sides of the line. This is where the work is decided."', '" notes on both sides of the line. This is where the work is decided."'),
    ('" among the causes or conditions Q.5–Q.7 do not reach, and the tangle keeps "', '" among the causes or conditions Q.5–Q.7 do not reach, and the threads keep "'),
    ('": support not yet used (Analysis) that sits only above the line (tangle). Support', '": support already at work that Q.5–Q.7 do not use yet, and whose notes sit only above the line. Support'),
    ('The tangle reads how it runs between dots.', 'The threads show how it runs between answers and notes.'),
    ('" as not reached by Q.5–Q.7, but the tangle does not keep "', '" as not reached by Q.5–Q.7, but the threads do not keep "'),
    ('" through dots that carry Q.5–Q.7 too, so "', '" through answers and notes in Q.5–Q.7 too, so "'),
    ('"The tangle keeps " +', '"The threads keep " +'),
    ('E.push(["Closest and farthest, in the tangle", L])', 'E.push(["Closest and farthest from the goal", L])'),
]:
    rep(a, b)
rep('" is the closest answer to the goal and it also sits on a thread', '" shares the most words with the goal and it also sits on a thread')
rep('" is the closest answer to the goal but it is not on a thread', '" shares the most words with the goal but it is not on a thread')
rep('", the farthest, still shares threads with other answers', '", which shares the fewest, still shares threads with other answers')
rep('", the farthest from the goal, also sits on no thread', '", which shares the fewest words with the goal, also sits on no thread')
a='''" both resisted and supported, and the landscape has " +
                        x(p, "them", "it") +
                        " notes on both sides of the line. This is where the work is decided.",'''
b='''" both resisted and supported, and on the landscape " +
                        x(p, "their notes sit", "its notes sit") +
                        " on both sides of the line. This is where the work is decided.",'''
assert s.count(a)==1; s=s.replace(a,b)
a="still shares threads with other answers, so it is distant from the goal but not cut off from your thinking."
assert s.count(a)==1; s=s.replace(a,"still shares threads with other answers, so it is far from the goal's wording but not cut off from your thinking.")
rep('t && (t.textContent = "v175");', 't && (t.textContent = "v176");')
open(P, "w").write(s); print("v176 ok")
