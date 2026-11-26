# v286: cut the repeats (his "Cut", 25 Nov 2026 18:52).
# 1. YOUR STORY SO FAR: when AT A GLANCE already names the forms the protection takes, the story's opening
#    no longer repeats them; "support answers resistance in kind" is said once, in THE OPPORTUNITY.
# 2. Taking Action: WHAT STILL STANDS IN THE WAY is left off a card when it repeats THE TEST word for word.
# 3. Start Here: THE FIVE PAGES (listing four) reads THE PAGES.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

rep('''    EP.push(
      "The change meets resistance again and again, and each time the resistance takes the shape the change has reached: " +
        forms.replace(/, and /, ", and finally ").replace(/^([^,]*) and /, CH.length === 2 ? "$1, and then " : "$1 and ") +
        ". With each step it moves closer to each person and further out of sight" +
        (hasGoal ? ", until the change looks adopted while the old order goes on inside it." : ".") +
        (helpAgg ? " Around it, support answers resistance in kind, and each side hardens the other." : "") +
        (wideMid ? " Between them lies a wide middle, neither for nor against, waiting to see which way things go." : ""),
    );''', '''    /* v286: AT A GLANCE names the forms when there are two or more; THE OPPORTUNITY says support answers in kind */
    EP.push(
      (CH.length >= 2
        ? "With each step the change takes, the resistance moves closer to each person and further out of sight"
        : "The change meets resistance again and again, and each time the resistance takes the shape the change has reached: " +
          forms.replace(/, and /, ", and finally ").replace(/^([^,]*) and /, CH.length === 2 ? "$1, and then " : "$1 and ") +
          ". With each step it moves closer to each person and further out of sight") +
        (hasGoal ? ", until the change looks adopted while the old order goes on inside it." : ".") +
        (wideMid ? " Between support and resistance lies a wide middle, neither for nor against, waiting to see which way things go." : ""),
    );''')

rep('''      : tv && "yes" !== tv && ts && (h += '<div><span class="tsl">WHAT STILL STANDS IN THE WAY</span> ' + ts + "</div>");''',
'''      : tv &&
        "yes" !== tv &&
        ts &&
        (function () {
          /* v286: not when THE TEST already says it word for word */
          var d = document.createElement("div");
          d.innerHTML = ts;
          var t = d.textContent.replace(/\\s+/g, " ").trim(),
            root = c.closest("#gsm"),
            cnt = function (x) {
              return x ? x.textContent.replace(/\\s+/g, " ").split(t).length - 1 : 0;
            };
          return !t || cnt(root) <= cnt(c);
        })() &&
        (h += '<div><span class="tsl">WHAT STILL STANDS IN THE WAY</span> ' + ts + "</div>");''')

rep('<div class="sh">THE FIVE PAGES</div>', '<div class="sh">THE PAGES</div>')
rep('t.textContent = "v285"', 't.textContent = "v286"')
open(p, 'w', encoding='utf-8').write(s); print('ok')
