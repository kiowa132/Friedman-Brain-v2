from week_data import *

def m(n): return f"${n:,.0f}"
def lab(c): return c if c in ("Baltimore City", "Baltimore County") else f"{c} County"

def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)

# three-week trend
trend_rows = []
for c, t in TREND.items():
    trend_rows.append([c] + [f"{m(p)} / {d} days" for (_, p, d) in t])
TREND_T = table(["County", "8/31-9/6", "9/7-9/13", "9/14-9/20"], trend_rows)

big = [(c, v) for c, v in CT.items() if v[0] >= 10]
fast = sorted(big, key=lambda x: x[1][2])[:5]
slow = sorted(big, key=lambda x: -x[1][2])[:5]
HEAT_FAST = table(["County", "Avg. DOM", "Closings"],
                  [[lab(c), f"{v[2]} days", v[0]] for c, v in fast])
HEAT_SLOW = table(["County", "Avg. DOM", "Closings"],
                  [[lab(c), f"{v[2]} days", v[0]] for c, v in slow])

ratio = lambda v: v[6] / v[0]
hi = sorted(big, key=lambda x: -ratio(x[1]))[:5]
lo = sorted(big, key=lambda x: ratio(x[1]))[:5]
def sup_rows(lst): return [[lab(c), v[6], v[0], f"{ratio(v):.1f}x"] for c, v in lst]
SUPPLY_HIGH = table(["County", "New Listings", "Closed", "Ratio"], sup_rows(hi))
SUPPLY_LOW = table(["County", "New Listings", "Closed", "Ratio"], sup_rows(lo))

app_rows = []
for c in sorted(CT):
    v = CT[c]
    app_rows.append([c, v[6], m(v[7]), v[8], v[0], m(v[1]), v[2], f"{ratio(v):.1f}x"])
app_rows.append(["**Statewide**", f"**{ST['new']:,}**", f"**{m(ST['med_new'])}**", f"**{ST['pending']}**",
                 f"**{ST['closed']}**", f"**{m(ST['med_sold'])}**", "n/a", f"**{ST['new']/ST['closed']:.1f}x**"])
APPENDIX = table(["County", "New Listings", "Median New-List Price", "Pending", "Closed",
                  "Median Sold Price", "Avg. DOM", "New:Closed Ratio"], app_rows)

tpl = open("report-core.template.md", encoding="utf-8").read()
for k, v in {"{{TREND}}": TREND_T, "{{HEAT_FAST}}": HEAT_FAST, "{{HEAT_SLOW}}": HEAT_SLOW,
             "{{SUPPLY_HIGH}}": SUPPLY_HIGH, "{{SUPPLY_LOW}}": SUPPLY_LOW, "{{APPENDIX}}": APPENDIX}.items():
    assert k in tpl, k
    tpl = tpl.replace(k, v)
assert "{{" not in tpl
out = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\drafts\friedman-report\2026-09-14-to-09-20\report-core.md"
open(out, "w", encoding="utf-8").write(tpl)
print("wrote", out, len(tpl.split()), "words")
print(HEAT_FAST); print(); print(HEAT_SLOW); print(); print(SUPPLY_HIGH); print(); print(SUPPLY_LOW)
# em/en dash guard
import re
bad = [l for l in tpl.splitlines() if re.search("[\u2014\u2013]", l)]
print("\nlines with em/en dashes:", len(bad)); [print(b) for b in bad]
