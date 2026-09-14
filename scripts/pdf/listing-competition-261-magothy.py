# -*- coding: utf-8 -*-
"""Branded Competitive Analysis PDF - 261 Magothy Bridge Rd, Pasadena MD 21122
(Blaine Welker). Companion to Kyle's Canva listing strategy deck.

Data from RPR CMA + Market Trends pulled 9/10/2026. Focus: the area
competition, days on market, where to price to be competitive, and a
their-marketing vs our-marketing comparison. 5 pages. No em dashes.
Run: py scripts/pdf/listing-competition-261-magothy.py
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\261-magothy-bridge-rd\261-Magothy-Competitive-Analysis.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, textColor=TEAL, leading=19),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
 "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
 "val": ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
 "sec": ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=12.5, textColor=TEAL, leading=15.5, spaceBefore=4, spaceAfter=4),
 "sub2":ParagraphStyle("sub2", fontName="Helvetica-Bold", fontSize=9.7, textColor=INK, leading=12.5, spaceBefore=5, spaceAfter=1),
 "body":ParagraphStyle("body", fontName="Helvetica", fontSize=9.1, textColor=INK, leading=13.2),
 "cap": ParagraphStyle("cap", fontName="Helvetica-Oblique", fontSize=7.5, textColor=GREY, leading=9.8, alignment=TA_CENTER),
 "cell":ParagraphStyle("cell", fontName="Helvetica", fontSize=8.1, textColor=INK, leading=10.4),
 "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=8.1, textColor=INK, leading=10.4, alignment=TA_RIGHT),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.8, textColor=TEAL, leading=10.5, alignment=TA_CENTER),
 "disc":ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7, textColor=GREY, leading=9, alignment=TA_CENTER),
 "boxb":ParagraphStyle("boxb", fontName="Helvetica", fontSize=8.6, textColor=INK, leading=12.2),
 "big": ParagraphStyle("big", fontName="Helvetica-Bold", fontSize=18, textColor=TEAL, leading=20, alignment=TA_CENTER),
 "bigl":ParagraphStyle("bigl", fontName="Helvetica", fontSize=7.5, textColor=GREY, leading=9.5, alignment=TA_CENTER),
}

def cell(t, r=False, b=False):
    st = ParagraphStyle("x", parent=S["cellR" if r else "cell"], fontName="Helvetica-Bold" if b else "Helvetica")
    return Paragraph(t, st)

def table(rows, col_w, header=True, pad=3.4):
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
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9)]))
    return b

def stat(v, l):
    return Table([[Paragraph(v, S["big"])],[Paragraph(l, S["bigl"])]], colWidths=[1.72*inch],
        style=TableStyle([("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
            ("BACKGROUND",(0,0),(-1,-1),CREAM),("BOX",(0,0),(-1,-1),0.5,GOLD)]))

def header():
    iw, ih = 2000, 373
    h = Table([[Image(LOGO, width=1.55*inch, height=1.55*inch*ih/iw),
        Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
            ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
        colWidths=[3.7*inch, 3.6*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
    return [h, Spacer(1,3), HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceAfter=8)]

story = []
today = datetime.date.today().strftime("%B %#d, %Y")

# ===== PAGE 1 =====
story += header()
story += [Paragraph("261 Magothy Bridge Rd: the competition, and how we beat it", S["h1"]),
    Paragraph("What is for sale near you, how fast this market is moving, where we need to price, "
    "and what we do that the other listings do not.", S["sub"]),
    Spacer(1,5),
    Paragraph("PREPARED FOR", S["lbl"]),
    Paragraph("Blaine Welker &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; Kyle Friedman, The Friedman Team" % today, S["val"]),
    Spacer(1,10)]

story += [Paragraph("The Pasadena market right now (21122, single family, August 2026)", S["sec"]),
    Paragraph("This is a fast seller's market. A home that is priced to the data and presented "
    "properly is going under contract in about a week, at full price. That is the bar your listing "
    "has to clear, and it is very clearable.", S["body"]),
    Spacer(1,8)]
row = Table([[stat("4 days", "MEDIAN DAYS ON MARKET"), stat("100%", "SOLD TO LIST PRICE"),
    stat("$478,500", "MEDIAN SOLD PRICE"), stat("2.17 mo", "MONTHS OF INVENTORY")]],
    colWidths=[1.83*inch]*4, style=TableStyle([("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
story += [row, Spacer(1,8),
    Paragraph("&#8226; Median days on market dropped about 69% month over month. Homes are not "
    "sitting.<br/>"
    "&#8226; Average list-to-sale price is 99.95%. Sellers who price right are getting essentially "
    "all of their asking price.<br/>"
    "&#8226; Median sold price is up 9.7% month over month, and the median sold price per square "
    "foot is about $272.<br/>"
    "&#8226; Most sales in the last three months landed between $400,000 and $600,000.", S["body"]),
    Spacer(1,9),
    box("<b>The takeaway.</b> In this market, the listings that stall are not stalling because of "
    "the market. They are priced ahead of it, or they launched flat with weak photos and no plan. "
    "Your house is renovated and this is the right season. Priced and marketed correctly, this is a "
    "one-week sale.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 2 =====
story += header()
story += [Paragraph("Your competition", S["sec"]),
    Paragraph("Comparable homes near 261 Magothy Bridge Rd, from the CMA. Watch the days on market.", S["body"]),
    Spacer(1,4)]
rows = [[cell("Address"), cell("Status"), cell("Bd/Ba", r=True), cell("Sq ft", r=True),
         cell("Price", r=True), cell("Days on mkt", r=True)]]
for a,st_,bb,sf,p,dom in [
    ("252 Magothy Bridge Rd &nbsp;<font size=7 color='#5B6B6E'>next door, renovated 2021, 0.67 ac</font>",
     "Active", "4 / 2", "2,404", "$499,900", "<b>63</b>"),
    ("207 Oak Hollow Ct &nbsp;<font size=7 color='#5B6B6E'>1985 split foyer, 0.39 ac</font>",
     "Active", "3 / 2", "1,354", "$450,000", "11"),
    ("550 Sunset Knoll Rd &nbsp;<font size=7 color='#5B6B6E'>1969, already had a price cut</font>",
     "Active", "3 / 2", "2,496", "$584,900", "22"),
    ("162 Barbara Rd, Severna Park &nbsp;<font size=7 color='#5B6B6E'>came back on with a price cut</font>",
     "Under contract", "3 / 3", "1,506", "$515,000", "111"),
    ("565 Sunset Knoll Rd &nbsp;<font size=7 color='#5B6B6E'>updated, sold at 100% of list</font>",
     "SOLD $550,000", "3 / 2", "1,712", "$550,000", "<b>7</b>"),
]:
    rows.append([cell(a), cell(st_), cell(bb, r=True), cell(sf, r=True), cell(p, r=True), cell(dom, r=True)])
story += [table(rows, [2.85*inch, 1.05*inch, 0.7*inch, 0.7*inch, 0.9*inch, 0.85*inch]), Spacer(1,4),
    Paragraph("Active comps average: $511,600 list, $258 per square foot, 32 days on market.", S["cap"]),
    Spacer(1,7),
    Paragraph("The pattern is clear", S["sub2"]),
    Paragraph("&#8226; <b>565 Sunset Knoll</b> was priced to the market and shown well. It went "
    "under contract in <b>7 days at 100% of list</b>. That is what a correct launch looks like here.<br/>"
    "&#8226; <b>252 Magothy Bridge, the house right next to yours,</b> is renovated, on a bigger "
    "lot, and has sat <b>63 days at $499,900</b> with no contract. That tells us $499,900 is a "
    "ceiling this pocket is not paying right now, at least not the way that home is being sold.<br/>"
    "&#8226; <b>550 Sunset Knoll</b> came out at $584,900, already cut the price, and is still "
    "sitting at 22 days.<br/>"
    "&#8226; <b>162 Barbara Rd</b> took 111 days and a price cut to finally go under contract.<br/>"
    "The homes that launched high and hoped are stuck. The one that launched right is sold.", S["body"])]

story += [PageBreak()]

# ===== PAGE 3 =====
story += header()
story += [Paragraph("Your house against that field", S["sec"]),
    Paragraph("261 Magothy Bridge Rd: 4 bedrooms, 2 full and 1 half bath, a 1967 home fully "
    "renovated top to bottom, with a finished lower level, a 1-car garage, and a 0.3 acre lot. New "
    "kitchen, cabinets, countertops, flooring, plumbing, drywall, paint, and carpet.", S["body"]),
    Spacer(1,5),
    Paragraph("Public records list the above-grade area at about 1,228 square feet, with the "
    "finished lower level bringing the total finished space to roughly 2,400. The first thing we do "
    "is get the home professionally measured, because the number that ends up on the MLS decides "
    "which searches you show up in and how your price per foot reads. We do not let a stale public "
    "record set that.", S["body"]),
    Spacer(1,7),
    Paragraph("Where we price", S["sec"]),
    Paragraph("&#8226; Your home is renovated more recently than 252 Magothy next door, and priced "
    "right it should not sit the way that one has.<br/>"
    "&#8226; 565 Sunset Knoll, updated and smaller, sold at $550,000 in a week. It sold fast "
    "because the number was right, not because it was cheap.<br/>"
    "&#8226; The zip's median sold price is $478,500 and median sold price per foot is about $272.<br/>"
    "&#8226; RPR's automated 'refined value' of about $792,000 is a software artifact from a square "
    "footage adjustment. Ignore it. The actual sold data is the truth, and it puts a renovated home "
    "this size in the <b>high $400s</b>.", S["body"]),
    Spacer(1,6),
    box("<b>The competitive zone is roughly $475,000 to $500,000.</b> We set the exact list price "
    "at the walk-through, against your finishes and your net proceeds sheet. The goal is to be the "
    "clear best value against the house next door and to sell in the one week this market is giving "
    "a well-run listing. One price, set to the data, and held. No cut ladder.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 4 =====
story += header()
story += [Paragraph("Their marketing vs. ours", S["sec"]),
    Paragraph("This is why the sitting listings are sitting, and why yours will not.", S["body"]),
    Spacer(1,4)]
rows = [[cell("", b=True), cell("The typical listing in this pocket", b=True), cell("Your listing with The Friedman Team", b=True)]]
for a,b,c in [
    ("Launch", "Straight to Active, cold, on whatever day.",
     "7-day Coming Soon on a Thursday. Build a buyer waiting list before the doors open, then go active right before the weekend."),
    ("Photos", "Agent phone photos or a quick shoot.",
     "Professional photography, twilight exterior, and video."),
    ("Tour", "A handful of flat listing photos.",
     "Full 3D Matterport tour and an interactive floor plan, so the finished lower level actually reads."),
    ("Staging", "Basic virtual staging, or none.",
     "Zillow Showcase: interactive virtual staging in multiple design styles, plus premium placement above standard listings in Zillow search."),
    ("Reach", "MLS and Zillow, and that is about it.",
     "MLS, Zillow, Redfin, realtor.com, a single-property website, neighborhood print, and QR sign capture. Paid Google and social ads from day one."),
    ("Agents", "Hope a buyer's agent stumbles on it.",
     "Agent email blast to the area brokerages, a brokers open, and direct calls to agents who have buyers in this price range."),
    ("Pricing", "List high, then cut, then cut again. (252 Magothy: 63 days. 550 Sunset: already reduced.)",
     "One price, set to the sold data, and held. An open house the first weekend when traffic peaks."),
    ("Result", "Sits 30 to 60-plus days.",
     "Sells in about the one week this market gives a listing that is done right."),
]:
    rows.append([cell(a, b=True), cell(b), cell(c)])
story += [table(rows, [0.85*inch, 3.0*inch, 3.45*inch]), Spacer(1,7),
    box("<b>Bottom line.</b> The market is not the problem in Pasadena right now. Execution is. The "
    "listings around you that are stuck skipped the launch, skimped on the media, and priced on "
    "hope. We do the opposite, in that order.", colors.HexColor("#EAF1F0"), LINE)]

story += [PageBreak()]

# ===== PAGE 5 =====
story += header()
story += [Paragraph("What it takes to beat the competition", S["sec"]),
    Paragraph("&#8226; <b>Measure it right.</b> Professional measurement and an accurate floor "
    "plan, so the home lands in the right searches and the finished lower level counts.<br/>"
    "&#8226; <b>Price to the sold data, not the estimate.</b> High $400s, set exactly at the "
    "walk-through, and held. No cut ladder.<br/>"
    "&#8226; <b>Build the media before we go live.</b> Professional photos and video, 3D Matterport "
    "tour, interactive floor plan, and Zillow Showcase with interactive staging.<br/>"
    "&#8226; <b>Launch on the buyer's schedule.</b> Coming Soon on a Thursday, go active the next "
    "Thursday, open house and brokers open that first weekend.<br/>"
    "&#8226; <b>Advertise it.</b> Paid Google and social from day one, agent email blast, brokers "
    "open, direct agent calls. A recent listing reached over 82,000 views in 30 days.<br/>"
    "&#8226; <b>Sell into the fall market.</b> September and October are the year's second-best "
    "selling window, right behind spring, and the buyers out now are serious and ready.", S["body"]),
    Spacer(1,8),
    Paragraph("The timeline (home ready October 8)", S["sub2"])]
rows = [[cell("When"), cell("What happens")]]
for a,b in [
    ("This week", "Walk the home, confirm the measurement, set the list price and the net proceeds sheet, fill out the listing paperwork, book the photographer and the home prep advisor."),
    ("Now to Oct 8", "Prep and any punch-list items. Home ready by October 8."),
    ("Week of Oct 8", "Photography, 3D tour, video, floor plan, Showcase built. MLS entered."),
    ("Thursday Oct 16", "Coming Soon goes live. Paid ads start. We track saves and tour requests. (Thursday Oct 9 if the media comes together fast.)"),
    ("The next Thursday", "Active, showings open, full syndication."),
    ("That weekend", "Open house and brokers open."),
    ("The following week", "Offers."),
]:
    rows.append([cell(a, b=True), cell(b)])
story += [table(rows, [1.25*inch, 6.05*inch]), Spacer(1,8),
    Paragraph("Next step", S["sec"]),
    Paragraph("Our meeting is the walk-through. We measure the house, lock the number against your "
    "net proceeds, set the Coming Soon and launch dates, and fill out the listing paperwork so we "
    "are marketing to our network of buyers before it hits the open market.", S["body"]),
    Spacer(1,10),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=5),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty "
    "&nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
    Paragraph("Equal Housing Opportunity. Comparable sales and market data from RPR and Bright MLS, "
    "pulled September 10, 2026, deemed reliable but not guaranteed. For informational purposes only. "
    "Not tax, legal, or financial advice.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.4*inch, bottomMargin=0.45*inch, title="Competitive Analysis - 261 Magothy Bridge Rd",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
