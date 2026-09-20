from week_data import *

def pct(a, b): return (a - b) / b * 100
print("== checks against Kyle's statewide pull ==")
print("closed sum", sum(v[0] for v in CT.values()), "vs 984")
print("active sum", sum(v[6] for v in CT.values()), "vs 2269 (2 diff = timing)")
print("pending sum", sum(v[8] for v in CT.values()), "(used as statewide pending)")

print("\n== week over week ==")
for k, lab in [("closed","closed"),("med_sold","median sold"),("new","new listings"),
               ("med_new","median new-list price"),("pending","pending"),
               ("reductions","reductions"),("cdom","days to contract"),("volume","volume")]:
    a, b = ST[k] if k in ST else None, LAST[k]
    if k == "volume": a = ST["volume"]
    print(f"{lab}: {b:,} -> {a:,}  {a-b:+,}  {pct(a,b):+.1f}%")
print("sold/orig", LAST["sold_orig"], "->", ST["sold_orig"], round(ST["sold_orig"]-LAST["sold_orig"],1))
print("rate", LAST["rate"], "->", ST["rate"], round((ST["rate"]-LAST["rate"])*100), "bp")
print("closings vs 8/31-9/6:", f"{pct(984,1150):+.1f}%")
print("supply ratio statewide", round(ST["new"]/ST["closed"],2), "last", round(LAST["new"]/LAST["closed"],2))
print("gap first-ask vs final: last", round(100.0-99.6,1), "this", round(100.0-98.4,1))
print("1.2 pts on $450,000 =", round(450000*0.012))
print("1.6% on $450,000 =", round(450000*0.016))

print("\n== monthly payment effect, $400,000 loan, 30yr ==")
def pmt(P, rate, n=360):
    r = rate/100/12
    return P*r*(1+r)**n/((1+r)**n-1)
for a, b in [(6.76, 6.95), (6.66, 6.95)]:
    print(f"{a}% -> {b}%: ${pmt(400000,a):,.0f} -> ${pmt(400000,b):,.0f}  diff ${pmt(400000,b)-pmt(400000,a):,.0f}/mo, ${ (pmt(400000,b)-pmt(400000,a))*12:,.0f}/yr")

print("\n== county ratios (new listings / closings) ==")
rows = []
for c, v in CT.items():
    rows.append((c, v[6]/v[0], v[0], v[6]))
rows.sort(key=lambda x: -x[1])
for c, r, cl, nl in rows:
    print(f"{c:18s} {r:.1f}x  new {nl}  closed {cl}")

print("\n== fastest / slowest by avg DOM, >=10 closings ==")
ok = [(c, v[2], v[0]) for c, v in CT.items() if v[0] >= 10]
ok.sort(key=lambda x: x[1])
print("fastest:", ok[:6])
print("slowest:", ok[-7:][::-1])

print("\n== median sold price rank, >=10 closings ==")
ok = sorted([(c, v[1], v[0]) for c, v in CT.items() if v[0] >= 10], key=lambda x: -x[1])
print("highest:", ok[:4]); print("lowest:", ok[-3:])

print("\n== 3-week trend deltas ==")
for c, t in TREND.items():
    (c1,p1,d1),(c2,p2,d2),(c3,p3,d3) = t
    print(f"{c:18s} price {p1:>7,} {p2:>7,} {p3:>7,}  this wk vs last {pct(p3,p2):+.1f}%  DOM {d1}/{d2}/{d3}")

print("\n== county vs statewide list-price movement, new listings vs last week (from log) ==")
LASTNEW = {"Montgomery":420,"Anne Arundel":215,"Prince George's":281,"Baltimore County":248,
           "Baltimore City":291,"Frederick":134,"Harford":100,"Howard":107,"Charles":103,
           "Worcester":64,"Carroll":55}
for c, n in LASTNEW.items():
    print(f"{c:18s} new {n} -> {CT[c][6]}  {pct(CT[c][6],n):+.1f}%")
print("sum of new-listing changes (11 counties):", sum(CT[c][6] for c in LASTNEW), "vs", sum(LASTNEW.values()))
