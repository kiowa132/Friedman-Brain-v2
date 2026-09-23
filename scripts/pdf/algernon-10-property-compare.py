"""
Client PDF: 10 homes Algernon Carter sent over, compared against his stated
must-haves (yard, basement, parking for 4 cars, 1,800-2,000+ sq ft, 3-4
bedrooms with room to finish a 4th downstairs). 6 Baltimore County properties
ranked best fit to worst, 4 Baltimore City properties listed unranked at the
bottom since he wants to stay in the County.
Branded teal/gold, matches the other listing PDFs in this repo.
Run: python algernon-10-property-compare.py
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

OUT_DIR = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\people"
PDF_PATH = os.path.join(OUT_DIR, "Algernon-10-Property-Comparison.pdf")

TEAL = colors.HexColor("#0F5C63")
GOLD = colors.HexColor("#C9A96A")
INK = colors.HexColor("#0D2226")
CARD = colors.HexColor("#FAF8F5")
GRAY = colors.HexColor("#6B7280")
RULE = colors.HexColor("#E3DCCB")
RED = colors.HexColor("#B5544A")
GREEN = colors.HexColor("#3D7A5C")

win = r"C:\Windows\Fonts"
for name, f in {"Arial": "arial.ttf", "Arial-Bold": "arialbd.ttf", "Arial-Italic": "ariali.ttf", "Arial-BoldItalic": "arialbi.ttf"}.items():
    pdfmetrics.registerFont(TTFont(name, os.path.join(win, f)))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-BoldItalic")
F, FB, FI = "Arial", "Arial-Bold", "Arial-Italic"

S = {
    "body": ParagraphStyle("body", fontName=F, fontSize=9.5, leading=13.5, textColor=INK, spaceAfter=6),
    "small": ParagraphStyle("small", fontName=FI, fontSize=7.8, leading=10.5, textColor=GRAY, spaceAfter=6),
    "h1": ParagraphStyle("h1", fontName=FB, fontSize=19, leading=23, textColor=TEAL, spaceAfter=3),
    "h2": ParagraphStyle("h2", fontName=FB, fontSize=14, leading=17, textColor=TEAL, spaceBefore=12, spaceAfter=6, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName=FB, fontSize=11.5, leading=14, textColor=INK, spaceBefore=4, spaceAfter=2, keepWithNext=1),
    "price": ParagraphStyle("price", fontName=FB, fontSize=13, leading=16, textColor=TEAL, alignment=2),
    "cell": ParagraphStyle("cell", fontName=F, fontSize=8.3, leading=11, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName=FB, fontSize=8, leading=10, textColor=colors.white),
    "cell_s": ParagraphStyle("cell_s", fontName=F, fontSize=7.3, leading=9.4, textColor=INK),
    "cellb_s": ParagraphStyle("cellb_s", fontName=FB, fontSize=7.3, leading=9.4, textColor=colors.white),
    "li": ParagraphStyle("li", fontName=F, fontSize=9.3, leading=13, textColor=INK, leftIndent=12, spaceAfter=3),
    "flag": ParagraphStyle("flag", fontName=F, fontSize=8.8, leading=12.4, textColor=RED, leftIndent=12, spaceAfter=3),
}


def P(t, st="body"):
    t = t.replace("&", "&amp;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    assert not re.search("[\u2014\u2013]", t)
    return Paragraph(t, S[st])


def bullets(items, st="li", mark="\u2022  "):
    return [Paragraph(mark + i.replace("&", "&amp;"), S[st]) for i in items]


def banner(width):
    inner = [
        [Paragraph('<font color="#C9A96A"><b>THE FRIEDMAN TEAM  |  eXp REALTY</b></font>', ParagraphStyle("k", fontName=FB, fontSize=8.5, leading=11))],
        [Paragraph("10 Homes, Compared", ParagraphStyle("t", fontName=FB, fontSize=25, leading=29, textColor=colors.white))],
        [Paragraph("Ranked Against What You Told Me Matters Most", ParagraphStyle("s", fontName=FI, fontSize=11.5, leading=15, textColor=colors.white))],
        [Paragraph("Prepared for Algernon Carter  |  September 25, 2026  |  Baltimore, MD", ParagraphStyle("b", fontName=F, fontSize=8.5, leading=11, textColor=colors.white))],
    ]
    t = Table(inner, colWidths=[width])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TEAL), ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("TOPPADDING", (0, 0), (0, 0), 14),
                           ("BOTTOMPADDING", (0, -1), (-1, -1), 12), ("LINEBELOW", (0, -1), (-1, -1), 3, GOLD)]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(F, 7.5)
    canvas.setFillColor(GRAY)
    canvas.drawString(0.75 * inch, 0.5 * inch, "Kyle Friedman  |  REALTOR\u00ae  |  443-789-3101  |  kyle@friedmanreteam.com")
    canvas.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def fact_table(rows, w):
    data = [[Paragraph(f"<b>{k}</b>", S["cell_s"]), Paragraph(v, S["cell_s"])] for k, v in rows]
    t = Table(data, colWidths=[1.2 * inch, w - 1.2 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
    ]))
    return t


def property_card(rank, address, subtitle, price, price_note, facts, fit_lines, flags, verdict, w):
    head_left = []
    if rank:
        head_left.append(Paragraph(f"#{rank}", ParagraphStyle("rk", fontName=FB, fontSize=18, textColor=GOLD)))
    head_left.append(P(f"**{address}**", "h3"))
    head_left.append(P(subtitle, "small"))
    price_block = [Paragraph(price, S["price"]), Paragraph(price_note, ParagraphStyle("pn", fontName=FI, fontSize=7.6, leading=9.6, textColor=GRAY, alignment=2))]
    head = Table([[head_left, price_block]], colWidths=[w * 0.68, w * 0.32])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))

    body = [Spacer(1, 3), fact_table(facts, w), Spacer(1, 5)]
    body.append(P("How it stacks up against your list:", "cell"))
    body += bullets(fit_lines, "li")
    if flags:
        body.append(Spacer(1, 2))
        body += bullets(flags, "flag", mark="Flag:  ")
    body.append(Spacer(1, 3))
    body.append(P(f"**Verdict:** {verdict}", "cell"))

    block = [head, Spacer(1, 4)] + body
    tbl = Table([[block]], colWidths=[w])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD), ("BOX", (0, 0), (-1, -1), 0.6, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return KeepTogether([tbl, Spacer(1, 10)])


def build():
    os.makedirs(OUT_DIR, exist_ok=True)
    w = letter[0] - 1.5 * inch
    s = [banner(w), Spacer(1, 10)]

    s.append(P("What You Told Me Matters Most", "h2"))
    s += bullets([
        "A yard",
        "A basement",
        "Parking for 4 cars",
        "1,800 to 2,000+ square feet",
        "3 to 4 bedrooms, and if it's only 3, a basement he can realistically finish into a 4th",
    ])
    s.append(P("You also want to stay in Baltimore County, not the City. Every property below is checked against all five, "
                "and the 4 City addresses you sent are included at the end for completeness, not ranked against your list."))

    s.append(P("The Field, at a Glance", "h2"))
    head = ["#", "Address", "County / City", "Price", "Beds", "Sq Ft", "Basement", "Parking"]
    rows = [
        ["1", "35 Glenwood Ave", "Baltimore Co.", "$330,000", "3", "1,803", "Unfinished", "4 spaces"],
        ["2", "3706 Parkfield Rd", "Baltimore Co.", "$360,000", "4", "2,100", "Finished", "2 spaces"],
        ["3", "3655 Forest Garden Ave", "Baltimore Co.", "$359,999", "3 + suite", "~2,000", "Finished", "Not stated"],
        ["4", "5412 W North Ave", "Baltimore Co.", "$335,000", "5", "1,626", "Unfinished", "Not stated"],
        ["5", "2909 Louisiana Ave", "Baltimore Co.", "$369,900", "4", "2,013 / 1,629*", "Finished", "Not stated"],
        ["6", "7165 Fairbrook Rd", "Baltimore Co.", "$325,000", "3", "1,504", "None", "Driveway"],
        ["\u2014", "5211 Bosworth Ave", "Baltimore City", "$325,000", "4", "2,008 / 1,845*", "Unknown", "Unknown"],
        ["\u2014", "5502 Fernpark Ave", "Baltimore City", "$365,000", "5", "2,184", "Finished", "2-car garage"],
        ["\u2014", "2913 Oakhill Ave", "Baltimore City", "$370,000", "4", "2,500", "Finished", "Off street"],
        ["\u2014", "5522 Bosworth Ave", "Baltimore City", "$369,900", "4", "2,187", "Finished", "On street"],
    ]
    data = [[Paragraph(h, S["cellb_s"]) for h in head]]
    for r in rows:
        data.append([Paragraph(str(c), S["cell_s"]) for c in r])
    colw = [0.28 * inch, 1.55 * inch, 0.9 * inch, 0.68 * inch, 0.55 * inch, 0.85 * inch, 0.62 * inch, 0.65 * inch]
    t = Table(data, colWidths=colw, repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), TEAL), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
             ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
             ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE), ("LINEBELOW", (0, 6), (-1, 6), 1, GOLD)]
    for i in range(2, len(rows) + 1, 2):
        style.append(("BACKGROUND", (0, i), (-1, i), CARD))
    t.setStyle(TableStyle(style))
    s += [t, Spacer(1, 3), P("*Two figures shown where the MLS square footage and the county tax record disagree, worth confirming before an offer.", "small")]

    s.append(PageBreak())
    s.append(P("The 6 in Baltimore County, Ranked", "h2"))
    s.append(P("Best fit to your list first."))

    s.append(property_card(
        1, "35 Glenwood Ave", "East Catonsville \u00b7 Baltimore County \u00b7 3 bed, 2 bath, 1,803 sq ft \u00b7 built 1926, remodeled 2007",
        "$330,000", "$30,000 under your approval",
        [("Lot", "6,969 sq ft"), ("Basement", "Unfinished, rear entrance, waterproofing system, 816 sq ft"),
         ("Parking", "4 total spaces: 1-car detached garage plus 3 more off street"),
         ("Listed", "1 day ago, open house Saturday 9/26, 2:00 to 4:00 PM"),
         ("Condition", "As-is. Recently replaced Pella windows, hardwood floors, a rear addition second living room. Description says it could use a little love, reads as cosmetic, not a gut job")],
        [
            "Parking: the only listing that spells out 4 total spaces, exactly what you need",
            "Basement: unfinished, but it's there to finish into a 4th bedroom",
            "Size: 1,803 sq ft, right at the low end of your 1,800 to 2,000+ range",
            "Bedrooms: 3 now, with the basement as your path to a 4th",
            "Yard: not explicitly described in the listing, worth confirming in person",
        ],
        ["The online Zestimate is $404,500, about $75,000 above the asking price. That's an unusually large gap, worth finding out why before assuming it's simply underpriced."],
        "Best match on paper for parking and price cushion. Tour it at Saturday's open house if the timing works.",
        w))

    s.append(property_card(
        2, "3706 Parkfield Rd", "Pikesville (Courthaven) \u00b7 Baltimore County \u00b7 4 bed, 2 bath, 2,100 sq ft \u00b7 built 1961, remodeled 2025",
        "$360,000", "At your approval, but seller offers a 2% credit",
        [("Lot", "8,360 sq ft, cul-de-sac, beautifully landscaped"),
         ("Basement", "Partially finished 2024: bedroom 4 (252 sq ft), family room, and a full bath with a walk-in shower, all engineered wood flooring"),
         ("Parking", "2 off-street spaces, concrete driveway"),
         ("Condition", "Excellent, major remodel 2025: updated kitchen with stainless appliances, all appliances 2 years old or less, roof 5 years old"),
         ("Seller offer", "2% credit toward buyer's closing costs, points, or prepaids"),
         ("Price history", "Cut about $11,000 around Sept 10, 42 days on market")],
        [
            "Yard: yes, landscaped, cul-de-sac lot",
            "Basement: already finished into bedroom 4 plus a family room and full bath, done in 2024, not a future project",
            "Size: 2,100 sq ft total fits your range",
            "Bedrooms: 4, already there, no conversion needed",
            "Parking: 2 spaces confirmed, short of the 4 you want",
        ],
        ["Only 2 parking spaces on a concrete driveway. Confirm whether street parking nearby is realistic for the other 2 cars before counting on this one for your parking need."],
        "Strong on everything except parking. The finished basement, the condition, and the 2% seller credit toward closing costs make this one worth a serious look despite sitting right at your approval.",
        w))

    s.append(property_card(
        3, "3655 Forest Garden Ave", "Lochearn / Villa Nova \u00b7 Baltimore County \u00b7 3 bed, 2.5 bath, ~2,000 sq ft \u00b7 built 1951",
        "$359,999", "At your approval, no cushion",
        [("Lot", "8,550 sq ft, level, cul-de-sac"), ("Basement", "Finished: rec room, full bath, kitchenette, previously used as an in-law suite"),
         ("Listed", "Open house Sunday 9/27, 12:00 to 2:00 PM"),
         ("Price history", "Started at $435,000 in Oct 2025, pulled, briefly relisted at $370,000 in May 2026, now $359,999 since Aug 13, a 17% cumulative cut")],
        [
            "Yard: level backyard, confirmed",
            "Basement: already finished with its own bath and kitchenette, turning it into a 4th bedroom is close to done, not a project",
            "Size: fits your 1,800 to 2,000+ range",
            "Bedrooms: 3 above grade plus the finished suite downstairs",
            "Parking: not specified in the listing, confirm before writing an offer",
        ],
        ["A 17% cut over 13 months with multiple relistings says there's room to negotiate below $359,999, not a reason to avoid it, but ask the listing agent directly why it hasn't sold yet before touring."],
        "Real contender, but Parkfield now beats it on condition and comes with a seller credit.",
        w))

    s.append(property_card(
        4, "5412 W North Ave", "Gwynn Oak \u00b7 Baltimore County \u00b7 5 bed, 2 bath, 1,626 sq ft finished \u00b7 built 1921",
        "$335,000", "$25,000 under your approval",
        [("Lot", "6,000 sq ft"), ("Basement", "Unfinished, 1,000+ sq ft, walkout with laundry, storage/workshop condition"),
         ("Price history", "Cut from $349,000 to $335,000 on Sept 17"), ("Condition", "Cape Cod, no updated/renovated language in the listing; laminate and carpet flooring")],
        [
            "Yard: fenced, level yard confirmed",
            "Basement: large and unfinished, real potential but real renovation cost to make it usable",
            "Size: 1,626 sq ft finished is under your 1,800 to 2,000+ target as-is",
            "Bedrooms: already 5, more than your 3 to 4 want",
            "Parking: not specified in the listing",
        ],
        ["Making the basement count toward bedrooms or square footage means real renovation money, which cuts against wanting to keep cash free for that."],
        "Good price cushion, but the extra space you'd need to hit your size target isn't free.",
        w))

    s.append(property_card(
        5, "2909 Louisiana Ave", "Halethorpe (Rosemont) \u00b7 Baltimore County \u00b7 4 bed, 2 bath, 2,013 sq ft \u00b7 built 1935",
        "$369,900", "$9,900 over your approval",
        [("Lot", "5,000 sq ft"), ("Basement", "Finished walkout: 4th bedroom, 2nd full bath, rec room, laundry"),
         ("Sq ft note", "MLS shows 2,013 sq ft, the county tax record shows 1,629 sq ft, confirm which the appraisal will use"),
         ("Price history", "4 separate listing cycles since Oct 2025, cumulative $30,000 in cuts despite being marketed as fully renovated"),
         ("Area", "Near BWI / Lansdowne, a different submarket than everywhere else on this list")],
        [
            "Basement: already finished into a legitimate 4th bedroom with its own bath, the best match on paper",
            "Size: fits your range on the MLS number, falls short on the tax record number",
            "Bedrooms: 4, already there",
        ],
        [
            "Over your approval by $9,900, which matters given you want to keep cash to close low.",
            "Relisted four times in under a year with real price cuts is a pattern that often means a past appraisal or inspection problem. Ask the listing agent directly before touring.",
        ],
        "Checks the most boxes on paper, but the price and the listing history are real reasons for caution.",
        w))

    s.append(property_card(
        6, "7165 Fairbrook Rd", "Windsor Mill \u00b7 Baltimore County \u00b7 3 bed, 2 bath (1 full, 1 half), 1,504 sq ft \u00b7 built 1971",
        "$325,000", "$35,000 under your approval",
        [("Lot", "10,080 sq ft (0.23 acre)"), ("Basement", "None, single-level ranch on a slab"),
         ("Condition", "Beautifully updated: LVP flooring throughout, updated kitchen, ensuite half bath in the primary")],
        [
            "Yard: yes, a genuinely sized lot",
            "Price: the cheapest and most move-in ready of the group",
        ],
        [
            "No basement at all, so there's nowhere to add a 4th bedroom the way you planned.",
            "1,504 sq ft is well under your 1,800 to 2,000+ target with no way to add space.",
        ],
        "Good price and condition can't make up for two must-haves it structurally can't deliver.",
        w))

    s.append(PageBreak())
    s.append(P("4 Baltimore City Addresses, Unranked", "h2"))
    s.append(P("You told me you want to stay in the County, so these aren't scored against your list. Included so you have the full picture."))

    s.append(property_card(
        None, "5211 Bosworth Ave", "Howard Park \u00b7 Baltimore City \u00b7 4 bed, 3 bath",
        "$325,000", "Asking, not yet fully listed",
        [("Status", "Compass \"Coming Soon,\" no photos or showings scheduled yet"), ("Sq ft", "2,008 (MLS) / 1,845 (tax record)"), ("Built", "1926")],
        [], [], "Not enough here yet to evaluate. Revisit once it's actually active.", w))

    s.append(property_card(
        None, "5502 Fernpark Ave", "Howard Park \u00b7 Baltimore City \u00b7 5 bed, 3 bath, 2,184 sq ft \u00b7 built 1923",
        "$365,000", "$5,000 over your approval",
        [("Basement", "Finished: den/bedroom, full bath, laundry, rec room"), ("Parking", "Detached 2-car garage"),
         ("Listed", "11 days, no price cuts, the cleanest history of anything on this list"),
         ("Worth checking", "The listing mentions possible eligibility for around $30,000 or more in homebuyer grant assistance, subject to buyer and program eligibility")],
        [], [], "If the grant program applies to you, this is worth a call to your lender regardless of the City/County preference, it could close the gap on price by itself.", w))

    s.append(property_card(
        None, "2913 Oakhill Ave", "Howard Park \u00b7 Baltimore City \u00b7 4 bed, 3 bath, 2,500 sq ft \u00b7 built 1923, remodeled 2022",
        "$370,000", "$10,000 over your approval",
        [("Basement", "Finished, counted in the 2,500 total"), ("Yard", "Fully fenced, level, with a deck and patio"),
         ("Condition", "\"Very good,\" quartz counters, custom cabinetry, stainless appliances")],
        [], [], "Nicely updated, but over your approval on top of being in the City.", w))

    s.append(property_card(
        None, "5522 Bosworth Ave", "Baltimore City \u00b7 4 bed, 3 bath, 2,187 sq ft \u00b7 built 1955",
        "$369,900", "$9,900 over your approval",
        [("Basement", "Finished, 100% of 882 sq ft"), ("Parking", "On street only"), ("Listed", "17 days")],
        ["The listing photos are virtually staged, meaning the home will not look like the pictures in person."],
        [], "Skip unless the City preference changes, and confirm the real condition in person either way.", w))

    s.append(Spacer(1, 4))
    s.append(P("**Bottom line.** Tour 35 Glenwood Ave and 3706 Parkfield Rd first. Glenwood wins on parking and price cushion, "
                "Parkfield wins on condition and already has a finished 4th bedroom plus a 2% seller credit toward closing costs, its only real gap is 2 parking "
                "spaces instead of 4. Forest Garden Ave is right behind both. Fairbrook Rd and the four City addresses are worth knowing about, but none of them "
                "get you what you told me you need without giving something up."))

    s.append(Spacer(1, 6))
    s.append(P("ASSUMPTIONS", "cell"))
    s.append(P("Prices, square footage, and listing details are from Bright MLS via public listing pages (Zillow, Redfin), pulled September 2026, and are "
                "subject to change. Square footage and condition claims are as the listing describes them, not independently verified. Loan approval, VA "
                "appraisal requirements, and any grant program eligibility should be confirmed with your lender before writing an offer.", "small"))

    SimpleDocTemplate(PDF_PATH, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                       topMargin=0.5 * inch, bottomMargin=0.7 * inch,
                       title="10 Homes Compared - Algernon Carter", author="Kyle Friedman, The Friedman Team"
                       ).build(s, onFirstPage=footer, onLaterPages=footer)
    print("wrote", PDF_PATH)


if __name__ == "__main__":
    build()
