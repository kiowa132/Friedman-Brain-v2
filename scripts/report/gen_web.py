import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from week_data import *

W = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\drafts\friedman-report\2026-09-14-to-09-20"
core = open(os.path.join(W, "report-core.md"), encoding="utf-8").read()
SLUG = "maryland-real-estate-market-report-week-of-september-14-20-2026"
IMG = "/images/uploads/"


def m(n): return f"${n:,.0f}"
def lab(c): return c if c in ("Baltimore City", "Baltimore County") else f"{c} County"


def tile(label, value, delta, tone):
    col = {"good": "#0F5C63", "bad": "#B5544A", "flat": "#0D222699"}[tone]
    return (f'<div style="background:#FAF8F5;border:1px solid #C9A96A55;border-radius:6px;padding:16px 14px;text-align:center;">\n'
            f'<div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:#0D222699;margin-bottom:6px;">{label}</div>\n'
            f'<div style="font-family:Georgia,serif;font-size:24px;font-weight:800;color:#0D2226;line-height:1.1;">{value}</div>\n'
            f'<div style="font-size:12px;font-weight:700;color:{col};margin-top:4px;">{delta}</div>\n</div>')


tiles = [
    ("Homes Sold", "984", "&#9650; +39.0%", "good"),
    ("New Listings", "2,269", "&#9660; -4.1%", "flat"),
    ("Pending Contracts", "482", "&#9650; +0.2%", "flat"),
    ("Median Sold Price", "$449,900", "&#9650; +1.1%", "good"),
    ("Median Days to Contract", "25 days", "&#9650; +5 from 20", "bad"),
    ("Price Reductions", "1,786", "&#9660; -11.2%", "good"),
    ("30-Yr Fixed Rate", "6.95%", "&#9650; +19 bp", "bad"),
]
TILES = ('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:24px 0;">\n'
         + "".join(tile(*t) for t in tiles) + "\n</div>")

# county tables
rows = ["| County | Homes Closed | Median Sold Price | Avg. Days on Market |", "|---|---|---|---|"]
for c in sorted(CT):
    v = CT[c]
    rows.append(f"| {lab(c)} | {v[0]} | {m(v[1])} | {v[2]} |")
COUNTY_TABLE = "\n".join(rows)

app = core.split("## Full County-by-County Data Table (all 24 jurisdictions)")[1].strip().split("\n")
APPENDIX = "\n".join(l for l in app if l.startswith("|"))
APPENDIX = APPENDIX.replace("| County |", "| County |", 1)
APPENDIX = re.sub(r"^\| (?!County|---|\*\*)([^|]+?) \|", lambda mm: f"| {lab(mm.group(1).strip())} |", APPENDIX, flags=re.M)

# spotlights
sp = core.split("## Market Spotlight")[1].split("### Three-Week Trend")[0]
paras = [p.strip() for p in sp.split("\n\n") if p.strip().startswith("**")]
SPOT = []
for p in paras:
    mm = re.match(r"\*\*(.+?)\.\*\*\s+(.*)", p, flags=re.S)
    if not mm:
        continue
    name = re.sub(r"\s*\(.*?\)", "", mm.group(1))
    txt = " ".join(mm.group(2).split())
    SPOT.append(f"### {name} Real Estate Market\n\n{txt}")
SPOT = "\n\n".join(SPOT)
assert SPOT.count("###") == 11, SPOT.count("###")

trend = core.split("### Three-Week Trend: Median Sold Price and Average Days on Market")[1].split("*Medians move")[0].strip()
CTREND = "\n".join(l for l in trend.split("\n") if l.startswith("|"))
heat_fast = core.split("**Hottest Markets, Fastest Average Days on Market**")[1].split("**Cooling")[0].strip()
heat_slow = core.split("**Cooling Markets, Slowest Average Days on Market**")[1].split("*(")[0].strip()
sup_hi = core.split("**Supply building fastest (new listings far outpacing closings):**")[1].split("**Tightest")[0].strip()
sup_lo = core.split("**Tightest counties (new supply barely ahead of closings):**")[1].split("Last week's leaders")[0].strip()
recipe = core.split("## Bonus From My Kitchen: Apple Cider Pork Chops")[1].split("## Your Next Move Starts Here")[0].strip()
recipe = recipe.split("\n\n", 1)
recipe_intro, recipe_rest = recipe[0], recipe[1]
story = core.split("## The Story of the Week")[1].split("## Maryland in 60 Seconds")[0].strip()
sp_paras = story.split("\n\n")
story = "\n\n".join(" ".join(p.split()) for p in sp_paras)
story_a, story_b = story.rsplit("\n\n", 1)
deep = core.split("## Deep Dive: The Number That Explains This Week")[1].split("## Bonus")[0].strip()
deep = "\n\n".join(" ".join(p.split()) for p in deep.split("\n\n"))
deep = deep.replace("**1.6 points**\n\nThat is the gap", "**1.6 points** is the gap")
assert "**1.6 points** is the gap" in deep

tpl = open(os.path.join(os.path.dirname(__file__), "web.template.md"), encoding="utf-8").read()
subs = {"TILES": TILES, "COUNTY_TABLE": COUNTY_TABLE, "APPENDIX": APPENDIX, "SPOT": SPOT, "CTREND": CTREND,
        "HEAT_FAST": heat_fast, "HEAT_SLOW": heat_slow, "SUP_HI": sup_hi, "SUP_LO": sup_lo,
        "RECIPE_INTRO": " ".join(recipe_intro.split()), "RECIPE_REST": recipe_rest.strip(),
        "STORY": story_a + "\n\n" + story_b, "DEEP": deep, "SLUG": SLUG, "IMG": IMG}
for k, v in subs.items():
    tpl = tpl.replace("{{%s}}" % k, v)
assert "{{" not in tpl, re.findall(r"\{\{.*?\}\}", tpl)
bad = [l for l in tpl.splitlines() if re.search("[\u2014\u2013]", l)]
assert not bad, bad[:3]
open(os.path.join(W, "website-seo.md"), "w", encoding="utf-8").write(tpl)
print("words", len(tpl.split()))
