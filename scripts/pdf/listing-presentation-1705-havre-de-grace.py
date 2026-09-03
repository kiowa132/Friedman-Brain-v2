# -*- coding: utf-8 -*-
"""Branded Listing Presentation PDF - 1705 Havre De Grace Dr, Edgewater
(Jefferson McBride). Copied from listing-presentation-8302-woodmont.py.

Angle: seller has buyers knocking during a renovation and is weighing FSBO /
a door sale. This deck shows why listing wins: more buyers so she can pick a
family, more money after commission, less risk. 5 pages with a comps chart.
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\1705-havre-de-grace-dr\1705-Havre-De-Grace-Listing-Presentation.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, textColor=TEAL, leading=19),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
 "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
 "val": ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
 "sec": ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=12, textColor=TEAL, leading=15, spaceBefore=4, spaceAfter=4),
 "sub2":ParagraphStyle("sub2", fontName="Helvetica-Bold", fontSize=9.5, textColor=INK, leading=12, spaceBefore=3, spaceAfter=1),
 "body":ParagraphStyle("body", fontName="Helvetica", fontSize=8.7, textColor=INK, leading=12.3),
 "cap": ParagraphStyle("cap", fontName="Helvetica-Oblique", fontSize=7.4, textColor=GREY, leading=9.6, alignment=TA_CENTER),
 "cell":ParagraphStyle("cell", fontName="Helvetica", fontSize=8.2, textColor=INK, leading=10.5),
 "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=8.2, textColor=INK, leading=10.5, alignment=TA_RIGHT),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.8, textColor=TEAL, leading=10.5, alignment=TA_CENTER),
 "disc":ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7, textColor=GREY, leading=9, alignment=TA_CENTER),
 "boxb":ParagraphStyle("boxb", fontName="Helvetica", fontSize=8.3, textColor=INK, leading=11.6),
}

def cell(t, r=False, b=False):
    st = ParagraphStyle("x", parent=S["cellR" if r else "cell"], fontName="Helvetica-Bold" if b else "Helvetica")
    return Paragraph(t, st)

def table(rows, col_w, header=True, pad=3.2):
    sc = [("VALIGN",(0,0),(-1,-1),"MIDDLE"),
          ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
          ("LEFTPADDING",(0,0),(0,-1),7),("RIGHTPADDING",(-1,0),(-1,-1),7),
          ("BOX",(0,0),(-1,-1),0.6,LINE),
          ("ROWBACKGROUNDS",(0,1 if header else 0),(-1,-1),[colors.white, colors.HexColor("#F7F4EE")])]
    if header:
        sc += [("BACKGROUND",(0,0),(-1,0),TEAL),("TEXTCOLOR",(0,0),(-1,0),colors.white),
               ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("LINEBELOW",(0,0),(-1,0),0.4,LINE)]
    t = Table(rows, colWidths=col_w, hAlign="LEFT"); t.setStyle(TableStyle(sc)); return t

def box(text, bg, bd):
    b = Table([[Paragraph(text, S["boxb"])]], colWidths=[7.3*inch])
    b.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("BOX",(0,0),(-1,-1),0.5,bd),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
    return b

def header():
    iw, ih = 2000, 373
    h = Table([[Image(LOGO, width=1.55*inch, height=1.55*inch*ih/iw),
        Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
            ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
        colWidths=[3.7*inch, 3.6*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
    return [h, Spacer(1,3), HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceAfter=8)]

def comps_chart():
    names = ['1906 Ridgeville\n$415k (2bd)', '1622 Chesapeake\n$430k (as-is)',
             '1749 Havre De Grace\n$450k (reno)', '226 Maryland Way\n$470k (reno)',
             '1604 Oriole Rd\n$480k (reno, 13 days)', '1533 Mayfield\n$495k (withdrew)']
    vals = [415, 430, 450, 470, 480, 495]
    palette = [GREY, GREY, TEAL, TEAL, GOLD, GREY]
    d = Drawing(460, 172)
    bc = VerticalBarChart()
    bc.x, bc.y, bc.width, bc.height = 30, 44, 418, 104
    bc.data = [vals]
    bc.categoryAxis.categoryNames = names
    bc.categoryAxis.labels.fontName = 'Helvetica'
    bc.categoryAxis.labels.fontSize = 6
    bc.categoryAxis.labels.fillColor = GREY
    bc.categoryAxis.labels.height = 24
    bc.categoryAxis.labels.dy = -3
    bc.valueAxis.valueMin = 400
    bc.valueAxis.valueMax = 520
    bc.valueAxis.valueStep = 30
    bc.valueAxis.labels.fontName = 'Helvetica'
    bc.valueAxis.labels.fontSize = 6.5
    bc.valueAxis.labels.fillColor = GREY
    bc.valueAxis.labelTextFormat = lambda v: '$%dk' % v
    bc.barWidth = 15
    bc.groupSpacing = 9
    for i, c in enumerate(palette):
        bc.bars[(0, i)].fillColor = c
        bc.bars[(0, i)].strokeColor = c
    d.add(bc)
    d.add(String(30, 160, 'Renovated 3-bed comps: the target list is $479,900 (gold)',
                 fontName='Helvetica-Bold', fontSize=8.5, fillColor=INK))
    return d

story = []
today = datetime.date.today().strftime("%B %#d, %Y")

# ===== PAGE 1 =====
story += header()
story += [Paragraph("Selling 1705 Havre De Grace Dr", S["h1"]),
    Paragraph("Woodland Beach, Edgewater MD 21037 &nbsp;&middot;&nbsp; buyers at your door vs. the open market", S["sub"]),
    Spacer(1,5),
    Paragraph("PREPARED FOR", S["lbl"]),
    Paragraph("Jefferson McBride &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; Kyle Friedman, The Friedman Team" % today, S["val"]),
    Spacer(1,9)]

story += [Paragraph("You have buyers knocking. That is a good sign, and it still pays to list.", S["sec"]),
    Paragraph("While you renovate, buyers keep coming to the door asking to buy. That tells you the "
    "home is desirable. It does not tell you what it is worth, or that any one of those buyers is "
    "the right one. You want to sell to a family. The open market is where that family is, and it is "
    "where the price gets set by competition instead of by a single offer.", S["body"]),
    Spacer(1,7),
    Paragraph("Who actually knocks on a door mid-renovation", S["sub2"]),
    Paragraph("&#8226; Investors, flippers, and wholesalers who watch for renovation permits and "
    "dumpsters, looking for a discount.<br/>"
    "&#8226; They are betting you do not have an agent, do not have comps, and want a fast, quiet "
    "sale.<br/>"
    "&#8226; Their offer is built to capture the value your renovation is creating, for themselves.<br/>"
    "The family buyer who would love this house is not walking your street mid-reno. They are on "
    "Zillow, pre-approved, waiting for it to come on the market finished.", S["body"]),
    Spacer(1,7),
    box("<b>The renovation is the whole point.</b> An un-renovated 3 bedroom this size in Woodland "
    "Beach sells around $415,000 to $430,000 (1622 Chesapeake Dr, same 1,668 square feet, sold "
    "$430,000). Finished and on the open market, the same size sells at $470,000 to $480,000. That "
    "$50,000 spread is what a door buyer wants to keep. Listing keeps it for you.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 2 =====
story += header()
story += [Paragraph("What the market says your home is worth", S["sec"]),
    Paragraph("Renovated 3 bedroom homes, roughly 1,300 to 1,700 square feet, in Woodland Beach and "
    "the adjacent water-privileged communities:", S["body"]), Spacer(1,3)]
rows = [[cell("Address"), cell("Sold", r=True), cell("Bd/Ba", r=True), cell("SqFt", r=True), cell("Note")]]
for a,p,bb,sf,nt in [
    ("1604 Oriole Rd", "$480,000 &middot; Jun", "3 / 2.1", "1,620", "updated, Woodland Beach, sold in 13 days"),
    ("1749 Havre De Grace Dr", "$450,000 &middot; Jul", "3 / 2", "1,312", "same street, renovated 2026, smaller"),
    ("226 Maryland Way", "$470,000 &middot; Mar", "3 / 2", "1,568", "water community, 43 days"),
    ("1622 Chesapeake Dr", "$430,000 &middot; Jul", "3 / 2", "1,668", "same size, NOT renovated (the as-is number)"),
    ("415 Fairmount Dr", "$420,000 &middot; Aug", "3 / 2", "1,200", "smaller"),
]:
    rows.append([cell(a), cell(p, r=True), cell(bb, r=True), cell(sf, r=True), cell(nt)])
story += [table(rows, [1.75*inch, 1.45*inch, 0.75*inch, 0.7*inch, 2.65*inch]), Spacer(1,6),
    comps_chart(),
    Paragraph("For contrast: 1635 Fairhill Dr (same 1,632 square feet, one street over) listed at "
    "$569,000 and 1533 Mayfield Rd at $495,000. Both withdrew unsold. Above about $485,000, homes "
    "this size do not sell here.", S["cap"]),
    Spacer(1,7),
    Paragraph("Recommended list price: $479,900", S["sec"]),
    Paragraph("Right at the 1604 Oriole Rd ceiling for a renovated home this size, and defensible "
    "against every comparable sale. Priced to draw multiple offers and go under contract inside 30 "
    "days. Zillow will estimate around $465,000 and some tools higher; the actual closed sales are "
    "the truth, and they say $470,000 to $480,000. This assumes the renovation is finished before we "
    "photograph and list.", S["body"])]

story += [PageBreak()]

# ===== PAGE 3 =====
story += header()
story += [Paragraph("A door offer vs. the open market", S["sec"])]
rows = [[cell("", b=True), cell("Sell to a door buyer", b=True), cell("List on the open market", b=True)]]
for a,b,c in [
    ("Who the buyers are", "Mostly investors and flippers hunting a discount", "Everyone, including pre-approved families"),
    ("How many offers", "One at a time, take it or leave it", "Several likely at $479,900"),
    ("Who picks the buyer", "The buyer. You have no leverage.", "You do. Prioritize an owner-occupant family."),
    ("Likely price", "About $420,000 to $445,000 (near as-is)", "About $470,000 to $480,000"),
    ("Commission", "None", "About 5% (roughly $23,500)"),
    ("Net before mortgage payoff", "About $430,000", "About $445,000 to $455,000"),
    ("Your time and risk", "You handle disclosures, contract, financing, inspections", "Handled, with a transaction coordinator"),
]:
    rows.append([cell(a, b=True), cell(b), cell(c)])
story += [table(rows, [1.7*inch, 2.8*inch, 2.8*inch]), Spacer(1,5),
    Paragraph("Even after a full commission, listing nets roughly $15,000 to $25,000 more than a "
    "door offer at as-is value, and more than that against a lowball. Full figures are in the "
    "attached Net Proceeds sheet.", S["body"]),
    Spacer(1,8),
    Paragraph("You will still sell to a family, and you are more likely to", S["sub2"]),
    Paragraph("On the open market you control who buys it. We market to and prioritize owner-occupant "
    "buyers, read their cover letters, and put a no-assignment clause and a primary-residence "
    "occupancy affidavit in the contract so wholesalers and flippers are screened out. If a family's "
    "offer comes in a little under an investor's, that is your call to make, with my advice. With one "
    "buyer at your door you get one number and no choice at all.", S["body"]),
    Spacer(1,7),
    box("<b>Bottom line.</b> Listing gets you the buyer you want, more money after commission, and "
    "someone handling the paperwork and the financing risk. The only thing a door sale saves is a "
    "few weeks, and it costs $15,000 to $45,000 to save them.", colors.HexColor("#EAF1F0"), LINE)]

story += [PageBreak()]

# ===== PAGE 4 =====
story += header()
story += [Paragraph("How I would sell it", S["sec"]),
    Paragraph("The renovation deserves a launch that shows it off. We build all of this before we go "
    "live:", S["body"]),
    Spacer(1,3),
    Paragraph("&#8226; <b>Professional photography</b> of the finished renovation, with proper "
    "lighting and a wide angle lens, plus a twilight exterior.<br/>"
    "&#8226; A full <b>Matterport 3D tour</b>, an <b>interactive floor plan</b>, and a video "
    "walkthrough, so out-of-area and busy buyers can see the whole house before they visit.<br/>"
    "&#8226; <b>Zillow Showcase</b>, Zillow's premium AI-powered placement, available only through "
    "select agents. It puts your listing above standard listings in search with the 3D tour and "
    "floor plan built in, and Showcase listings get far more views, saves, and shares.<br/>"
    "&#8226; A <b>dedicated single-property website</b>, plus syndication to Zillow, Redfin, and "
    "realtor.com.<br/>"
    "&#8226; A <b>Coming Soon</b> runway of about two weeks to build a waiting list of buyers before "
    "launch.<br/>"
    "&#8226; An <b>agent email blast</b> to area brokerages, a <b>public open house</b> the first "
    "weekend, a <b>brokers open</b>, and <b>direct calls</b> to agents with active buyers in this "
    "price range and this community.<br/>"
    "&#8226; <b>Paid digital and social</b> across the Annapolis and Anne Arundel buyer market, and "
    "a <b>print piece</b> to Woodland Beach and the surrounding streets.", S["body"]),
    Spacer(1,7),
    Paragraph("How I protect your goal of selling to a family", S["sub2"]),
    Paragraph("&#8226; Market language and agent outreach aimed at owner-occupant buyers.<br/>"
    "&#8226; Offers reviewed with you, including buyer cover letters and lender letters.<br/>"
    "&#8226; No-assignment clause and a primary-residence occupancy affidavit in the contract.<br/>"
    "&#8226; You make the final call on which offer to take. It does not have to be the highest.", S["body"]),
    Spacer(1,7),
    box("<b>Communication.</b> Showing feedback to you within 48 hours, a weekly call on traffic and "
    "pricing, and calls and emails returned the same day.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 5 =====
story += header()
story += [Paragraph("Why The Friedman Team", S["sec"]),
    Paragraph("&#8226; <b>A team, not one person:</b> Kyle leads strategy, pricing, and negotiation, "
    "a Home Prep Advisor helps the finished renovation show its best, and a Transaction Coordinator "
    "manages every deadline and document.<br/>"
    "&#8226; <b>Reach:</b> a recent listing drew over 82,000 views and 37,000 unique viewers on "
    "social in 30 days, plus Zillow Showcase premium placement.<br/>"
    "&#8226; <b>Easy Exit:</b> cancel anytime, no binding contract, no questions asked.<br/>"
    "&#8226; <b>Experience:</b> licensed since 2018, 10 to 20 sales a year since 2020, residential "
    "sales blended with real estate investing, so I know exactly how the buyers at your door think.", S["body"]),
    Spacer(1,6),
    box("<i>\"I've been a homeowner for 45-plus years and dealt with a number of realtors, but none "
    "like Kyle. He is truly the best: professional, thorough, and an exceptional communicator.\"</i> "
    "&nbsp;&mdash; Seller of 7106 Stratos Ln", colors.HexColor("#F4F1EA"), LINE),
    Spacer(1,8),
    Paragraph("Next steps", S["sec"]),
    Paragraph("1. A 30-minute conversation with you and your husband, in person or by phone, to walk "
    "through this.<br/>"
    "2. A quick look at the renovation so I can pin down the list price and a photography date.<br/>"
    "3. If it is a fit, set the Coming Soon and launch dates.", S["body"]),
    Spacer(1,10),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=5),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty "
    "&nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
    Paragraph("Equal Housing Opportunity. Information deemed reliable but not guaranteed and should be "
    "independently verified. For informational purposes only; not tax, legal, or financial advice. "
    "Comp and market figures from Bright MLS and RPR, September 2026.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.4*inch, bottomMargin=0.45*inch, title="Listing Presentation - 1705 Havre De Grace Dr",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
