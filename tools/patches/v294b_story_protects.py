# v294 part 2: what the system protects, why that is not unreasonable, how it could be provided another
# way, and the levers in the user's own design, for each finding the detector can name.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
PROT = '''      trad: "a way of seeing and doing things that has stood for a long time and that people take for granted",
      liv: "the livelihoods built around the present way: people's work, income, and standing",
      fear: "safety from blame: no one wants to answer for the one time things go wrong",
      expect: "what the public and those in power expect to see, and the standing of those who deliver it",'''
rep('''      order: "the present order of control: knowing who decides, what counts as good work, and who is safe",
    }[K];''', '''      order: "the present order of control: knowing who decides, what counts as good work, and who is safe",
''' + PROT + '''
    }[K];''')
rep('''          order: "the present order of control: knowing who decides, what counts as good work, and who is safe",
        }[K],''', '''          order: "the present order of control: knowing who decides, what counts as good work, and who is safe",
''' + PROT.replace('      ', '          ') + '''
        }[K],''')
rep('''        (K === "legit"
          ? "Without that shared sense, every decision would have to be fought for again."
          : K === "ident"
            ? "Without that continuity, people lose the pride and competence their work carries."
            : "Without it, the system cannot coordinate under pressure.") +''', '''        ({
          legit: "Without that shared sense, every decision would have to be fought for again.",
          ident: "Without that continuity, people lose the pride and competence their work carries.",
          trad: "Without it, people would have to rebuild, all at once, what they rely on without thinking.",
          liv: "Without it, people lose work and standing they have earned.",
          fear: "Without it, each person would carry the risk of every failure alone.",
          expect: "Without it, those in charge would answer for every outcome that looks like failure.",
        }[K] || "Without it, the system cannot coordinate under pressure.") +''')
rep('''        (K === "legit"
          ? "a new arrangement people can hold as legitimately as the old one."
          : K === "ident"
            ? "a new way of working people can recognize themselves in."
            : "a new order as predictable as the old one.") +''', '''        ({
          legit: "a new arrangement people can hold as legitimately as the old one.",
          ident: "a new way of working people can recognize themselves in.",
          trad: "a new way people can come to take for granted just as they took the old one.",
          liv: "a way forward that keeps people's work and standing.",
          fear: "a way to take the risk that does not leave people to carry the blame alone.",
          expect: "results people can see and come to expect instead.",
        }[K] || "a new order as predictable as the old one.") +''')
# levers: the order people rely on only where order or identity is what is protected
rep('''    lever(
      anyAcc || K !== "legit",''', '''    lever(
      anyAcc || "order" === K || "ident" === K,''')
rep('''    lever(helpAgg, /oppos|across''', '''    lever(HAS("trad"), /narrativ|frame|story|stories|campaign|educat|curricul|messag|perspective/, "giving people a new story to see the work through", "what new story replaces the one people see the work through now");
    lever(HAS("liv"), /fund|financ|\\bjobs?\\b|career|train|incentive|reward|\\bpay|employ/, "giving people work and standing in the new way", "what the change offers the people whose work rests on the present way");
    lever(HAS("fear"), /liabil|\\brisk|safe|protect|insur|monitor|small|experiment|pilot|right conditions/, "lowering the risk people carry when they try it", "who carries the risk, and the blame, when something goes wrong");
    lever(HAS("expect"), /media|public|messag|campaign|communit|narrativ|frame/, "changing what the public expects to see", "what the public and those in power will expect instead");
    lever(helpAgg, /oppos|across''')
open(p, 'w', encoding='utf-8').write(s)
print('v294 part 2 applied')
