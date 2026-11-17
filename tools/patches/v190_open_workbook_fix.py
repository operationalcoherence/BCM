"""v190: Open workbook works from every tab. The "Replace what is on this device?" question (and the message when a
file cannot be opened) live on Mapping Context; opening from the button on another tab showed them on a hidden tab,
so nothing seemed to happen. Now the app goes to Mapping Context first. Combine (gsm-comb2) gets the same fix."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("""                    ? ((o = r), e.classList.add("show"), e.scrollIntoView({ block: "center" }))
                    : a(r));
              } catch (e) {
                t.textContent = "That file could not be opened: " + e.message + ".";
              }""", """                    ? ((o = r),
                      e.classList.add("show"),
                      !e.offsetParent && window.gsmTab && window.gsmTab(0),
                      e.scrollIntoView({ block: "center" }))
                    : a(r));
              } catch (e) {
                t.textContent = "That file could not be opened: " + e.message + ".";
                !t.offsetParent && window.gsmTab && window.gsmTab(0);
                t.scrollIntoView({ block: "center" });
                var pm = document.getElementById("gsm-pdfmsg");
                pm && (pm.textContent = t.textContent);
              }""")
rep("""      function l(t) {
        ((e.innerHTML = t), e.classList.add("show"), e.scrollIntoView({ block: "center" }));
      }""", """      function l(t) {
        ((e.innerHTML = t),
          e.classList.add("show"),
          !e.offsetParent && window.gsmTab && window.gsmTab(0),
          e.scrollIntoView({ block: "center" }));
      }""")
rep('t.textContent = "v189"', 't.textContent = "v190"')
open(P, "w").write(s)
