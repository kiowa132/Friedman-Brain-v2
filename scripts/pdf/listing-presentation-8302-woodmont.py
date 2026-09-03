# -*- coding: utf-8 -*-
"""Branded Listing Presentation PDF - 8302 Woodmont Ave #203, Bethesda (Wendy Fossen).

Fallback for the Gamma deck (Gamma credits at 0). 5 pages with two charts:
the pricing case, two pricing options ($690k vs the $675k "stampede" play),
a detailed relaunch plan (90-day DOM reset, photography, Coming Soon), and
Zillow Showcase + why The Friedman Team.
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.graphics.shapes import Drawing, String, Line
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.barcharts import VerticalBarChart
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\8302-woodmont-ave-203\8302-Woodmont-Listing-Presentation.pdf"
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

def price_timeline():
    d = Drawing(460, 150)
    lc = HorizontalLineChart()
    lc.x, lc.y, lc.width, lc.height = 34, 24, 412, 104
    lc.data = [(775, 760, 750, 740, 735, 725, 700, 685)]
    lc.categoryAxis.categoryNames = ['Feb 20', 'Mar 12', 'Apr 14', 'May 25', 'Jun 18', 'Jul 2', 'Jul 24', 'Aug 11']
    lc.categoryAxis.labels.fontName = 'Helvetica'
    lc.categoryAxis.labels.fontSize = 6.5
    lc.categoryAxis.labels.fillColor = GREY
    lc.valueAxis.valueMin = 660
    lc.valueAxis.valueMax = 790
    lc.valueAxis.valueStep = 30
    lc.valueAxis.labels.fontName = 'Helvetica'
    lc.valueAxis.labels.fontSize = 6.5
    lc.valueAxis.labels.fillColor = GREY
    lc.valueAxis.labelTextFormat = lambda v: '$%dk' % v
    lc.lines[0].strokeColor = TEAL
    lc.lines[0].strokeWidth = 2
    lc.lines[0].symbol = None
    d.add(lc)
    d.add(String(34, 138, 'Six months, eight cuts, no sale', fontName='Helvetica-Bold', fontSize=8.5, fillColor=INK))
    d.add(String(60, 118, '$775k', fontName='Helvetica-Bold', fontSize=7, fillColor=TEAL))
    d.add(String(410, 34, '$685k', fontName='Helvetica-Bold', fontSize=7, fillColor=GOLD))
    return d

def comps_chart():
    # size-comparable set only, so the scale tells the truth
    names = ['4808 Moorland\n$565k (sold)', '#203 last list\n$685k (expired)',
             'Proposed\n$690k', 'Stampede\n$675k', '#305 in-bldg\n$730k (unsold)',
             '7710 #506\n$760k (sold)']
    vals = [565, 685, 690, 675, 730, 760]
    d = Drawing(460, 168)
    bc = VerticalBarChart()
    bc.x, bc.y, bc.width, bc.height = 30, 40, 418, 104
    bc.data = [vals]
    bc.categoryAxis.categoryNames = names
    bc.categoryAxis.labels.fontName = 'Helvetica'
    bc.categoryAxis.labels.fontSize = 6
    bc.categoryAxis.labels.fillColor = GREY
    bc.categoryAxis.labels.height = 22
    bc.categoryAxis.labels.dy = -3
    bc.valueAxis.valueMin = 540
    bc.valueAxis.valueMax = 780
    bc.valueAxis.valueStep = 60
    bc.valueAxis.labels.fontName = 'Helvetica'
    bc.valueAxis.labels.fontSize = 6.5
    bc.valueAxis.labels.fillColor = GREY
    bc.valueAxis.labelTextFormat = lambda v: '$%dk' % v
    bc.barWidth = 13
    bc.groupSpacing = 9
    palette = [TEAL, GREY, GOLD, GOLD, GREY, TEAL]
    for i, c in enumerate(palette):
        bc.bars[(0, i)].fillColor = c
        bc.bars[(0, i)].strokeColor = c
    d.add(bc)
    d.add(String(30, 156, 'Where $690,000 sits against the comparable sales', fontName='Helvetica-Bold', fontSize=8.5, fillColor=INK))
    return d

story = []
today = datetime.date.today().strftime("%B %#d, %Y")

# ===== PAGE 1 =====
story += header()
story += [Paragraph("Selling 8302 Woodmont Ave #203", S["h1"]),
    Paragraph("Stonehall Condominium, Bethesda MD 20814 &nbsp;&middot;&nbsp; a different approach", S["sub"]),
    Spacer(1,5),
    Paragraph("PREPARED FOR", S["lbl"]),
    Paragraph("Wendy Fossen &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; Kyle Friedman, The Friedman Team" % today, S["val"]),
    Spacer(1,9)]

story += [Paragraph("Your last listing did not sell. That is a pricing and launch problem, not a home problem.", S["sec"]),
    Paragraph("The unit listed February 20, 2026 at $775,000 and expired August 21 after <b>183 days</b> "
    "with no sale, following <b>eight price cuts</b>. It went on the market about $90,000 above where it "
    "ended, then chased the market down for six months.", S["body"]), Spacer(1,4),
    price_timeline(),
    Paragraph("Bright MLS price-change history, MLS #MDMC2217512.", S["cap"]), Spacer(1,8)]

story += [Paragraph("Why eight price cuts kill a listing", S["sec"]),
    Paragraph("&#8226; Buyers stop making offers and wait for the next cut.<br/>"
    "&#8226; They assume something is wrong with the unit.<br/>"
    "&#8226; After 180-plus days the listing goes stale and drops out of saved searches.<br/><br/>"
    "By the time the price was finally reasonable, the listing was invisible. The fix is not another "
    "cut. It is a clean relaunch at one correct price.", S["body"]),
    Spacer(1,7),
    box("<b>The unit itself is not the problem.</b> Built 2017, excellent condition, corner unit, "
    "private balcony, two deeded garage spaces (rare downtown), gourmet kitchen, full-service building "
    "with concierge and fitness center. This is a well-built, well-kept home that was mispriced and "
    "then mishandled on the way down.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 2 =====
story += header()
story += [Paragraph("What the market is telling us", S["sec"]),
    Paragraph("<b>Same building, your direct competitor.</b> Unit #305 (2 bed / 2 bath, 993 sq ft, 3rd "
    "floor) has been for sale most of 2026: listed $739,000 in January, canceled after 98 days, "
    "relisted at <b>$730,000</b> in April, and still unsold roughly 230 days in. Two nearly identical "
    "small 2-bedrooms in a 46-unit building, both sitting all year. That is the demand signal above "
    "$730,000: there is not enough of it.", S["body"]), Spacer(1,6)]

story += [Paragraph("2-bedroom condos that actually sold in downtown Bethesda (last ~4 months)", S["body"]), Spacer(1,3)]
rows = [[cell("Address"), cell("Sold", r=True), cell("Size", r=True), cell("$ / sq ft", r=True)]]
for a,p,z,ppsf in [
    ("7710 Woodmont Ave #506","$760,000","1,066 sf","$713"),
    ("8302 Woodmont Ave #407 (same building)","$1,030,000","1,668 sf","$617"),
    ("7710 Woodmont Ave #1011","$975,000","1,340 sf","$728"),
    ("4808 Moorland Ln #707","$565,000","884 sf","$639"),
]:
    rows.append([cell(a), cell(p, r=True), cell(z, r=True), cell(ppsf, r=True)])
story += [table(rows, [3.5*inch, 1.35*inch, 1.15*inch, 1.3*inch]), Spacer(1,7),
    comps_chart(),
    Paragraph("Size-comparable listings and sales only, so the scale reflects reality. Larger, "
    "higher-floor units in the building have sold for $975k to $1.03M and are a different product.", S["cap"]),
    Spacer(1,7),
    Paragraph("Where that puts your unit", S["sec"]),
    Paragraph("Recent sold prices for real downtown-Bethesda 2-bedrooms run about <b>$617 to $728 per "
    "square foot</b>. Your corner position, private balcony, and two deeded garage spaces push toward "
    "the upper half; the 2nd-floor location pulls back toward the middle. At roughly $650 to $675 per "
    "square foot on 1,033 square feet, that is about <b>$671,000 to $697,000</b> for a fresh, "
    "well-presented listing.", S["body"])]

story += [PageBreak()]

# ===== PAGE 3 =====
story += header()
story += [Paragraph("Two ways to price the relaunch", S["sec"]),
    Paragraph("Option A", S["sub2"]),
    Paragraph("<b>$690,000 &mdash; priced to sell.</b> A clean number, $40,000 under the competing unit "
    "(#305 at $730,000), about $668 per square foot, defensible against every recent sale. Expect "
    "showings quickly and an offer inside 30 days. One correct price, held firm; if activity is soft "
    "after about three weeks, one decisive move to $675,000, not another slow decline.", S["body"]),
    Spacer(1,4),
    Paragraph("Option B", S["sub2"]),
    Paragraph("<b>$675,000 &mdash; priced to create a stampede.</b> A brand-new listing at a number "
    "buyers and agents cannot argue with. Coming back <b>$55,000 under the competitor</b> and at or "
    "below the last comparable sale generates a wave of showings in the first weekend and a real shot "
    "at multiple offers, which can push the final price back toward &mdash; or past &mdash; $690,000. "
    "You trade $15,000 of list price for speed and negotiating leverage. This is the aggressive play "
    "if the priority is sold fast and talked about.", S["body"]),
    Spacer(1,8),
    box("<b>The proceeds reality.</b> Your loan balance ($625,690) sits close to today's value, so the "
    "net is thin and very sensitive to the final number (see the attached Net Proceeds estimate: about "
    "$7,000 at a $675,000 sale, $21,000 at $690,000, $45,000 at $715,000). Holding the unit costs "
    "roughly <b>$3,700 to $4,200 a month</b> in condo fee, taxes, and loan interest &mdash; more than "
    "the entire net at the lower end for every month it sits. That math is why both options above are "
    "built around <b>speed</b>. A stampede that closes in 30 days at $685,000 beats a $700,000 list "
    "that drifts for another six months.", colors.HexColor("#EAF1F0"), LINE),
    Spacer(1,8),
    box("<b>You are already selling below your 2021 purchase price</b> ($749,000), so there is no "
    "capital gain to worry about. The decision is not \"how much do I make\" &mdash; it is \"how do I "
    "get out cleanly and stop the carrying costs.\"", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 4 =====
story += header()
story += [Paragraph("The plan: a relaunch, not a re-list", S["sec"]),
    Paragraph("How the days-on-market reset works", S["sub2"]),
    Paragraph("Bright MLS tracks two counters: Days on Market and <b>Cumulative Days on Market</b>. "
    "The cumulative counter only resets to zero after a property has been <b>off the market for 90 "
    "consecutive days</b>. Zillow works the same way &mdash; \"days on Zillow\" resets once the home "
    "has been off Zillow for about 90 days; relist any sooner and Zillow keeps the old day count, "
    "shows the full price-cut history, and flags it as \"relisted.\" Your listing came off on "
    "<b>August 21</b>, so if it stays off, both counters are clean around <b>mid-to-late November</b>. "
    "We do not waste that window &mdash; all of the prep below happens during it, so we can launch the "
    "moment the clock is clean.", S["body"]),
    Spacer(1,3),
    Paragraph("From there, two good launch windows: a <b>early-December launch</b> into the winter "
    "relocation and year-end buyer pool, or <b>hold to mid-January</b> for the larger spring-adjacent "
    "pool. We pick based on where the competing inventory sits at the time.", S["body"]),
    Spacer(1,6),
    Paragraph("The photography has to be redone", S["sub2"]),
    Paragraph("The images on the last listing are soft in spots, underlit, and do not show how the "
    "corner exposure fills the unit with light or how the layout actually lives. Buyers scroll "
    "listings in seconds &mdash; dim, slightly blurry photos get skipped before the price is ever "
    "considered. The relaunch gets professional lighting and a wide-angle lens, a <b>twilight "
    "exterior</b> of the building, detail shots of the chef's kitchen and the balcony, a full "
    "<b>Matterport 3D tour</b>, an <b>interactive floor plan</b>, and a short video walkthrough.", S["body"]),
    Spacer(1,6),
    Paragraph("The off-market window (now to launch)", S["sub2"])]
rows = [[cell("Track", b=True), cell("What happens", b=True)]]
for n, t in [
    ("Listing stays off", "Bright CDOM and Zillow day count both reset at 90 days off market (about mid-to-late November)."),
    ("Media", "New photography, twilight exterior, Matterport 3D tour, interactive floor plan, video."),
    ("Prep", "Light staging where it helps; order the Montgomery County condo resale package early (1 to 2 weeks on its own)."),
    ("Build", "Dedicated property website, new remarks that lead with the corner unit and two deeded garage spaces, print piece for the building and block."),
    ("Coming Soon", "Pre-market runway 10 to 14 days before going live, to seed agent and buyer interest."),
]:
    rows.append([cell(n), cell(t)])
story += [table(rows, [1.25*inch, 6.05*inch]), Spacer(1,5),
    Paragraph("Launch day", S["sub2"]),
    Paragraph("Fresh MLS number, syndication to Zillow / Redfin / realtor.com, agent email blast, "
    "public open house weekend one, a brokers open, paid digital across the DC-Maryland buyer market, "
    "and direct calls to agents with active 2-bedroom buyers. Then the communication rhythm below.", S["body"])]

story += [PageBreak()]

# ===== PAGE 5 =====
story += header()
story += [Paragraph("Zillow Showcase", S["sec"]),
    Paragraph("Showcase is Zillow's premium, AI-powered listing format, and it is only available "
    "through a limited set of agents. Kyle's listings qualify. It gives your unit:", S["body"]),
    Spacer(1,2),
    Paragraph("&#8226; An elevated, immersive page layout that stands above standard listings in "
    "Zillow's search results<br/>"
    "&#8226; An <b>interactive floor plan</b> buyers explore room by room before they ever visit<br/>"
    "&#8226; A full virtual tour built into the listing page<br/>"
    "&#8226; Zillow's own data shows Showcase listings consistently outperform standard listings on "
    "views, saves, and shares", S["body"]),
    Spacer(1,4),
    box("For a relaunch, Showcase matters more than usual: it is how the new listing outshines the "
    "shadow of the old one and the competing unit in the same building. More views and saves in the "
    "first week is exactly what turns a $675,000 or $690,000 launch into competing offers.", CREAM, GOLD),
    Spacer(1,8),
    Paragraph("Why The Friedman Team", S["sec"]),
    Paragraph("&#8226; <b>Communication guarantee:</b> showing feedback within 48 hours, a weekly "
    "activity-and-pricing call, calls and emails returned same day.<br/>"
    "&#8226; <b>A team, not one person:</b> listing agent (Kyle) on strategy and negotiation, a Home "
    "Prep Advisor to make it show its best, and a Transaction Coordinator managing every deadline and "
    "document.<br/>"
    "&#8226; <b>Reach:</b> a recent listing drew over 82,000 views and 37,000 unique viewers on "
    "social in 30 days.<br/>"
    "&#8226; <b>Easy Exit:</b> cancel anytime, no binding contract, no questions asked.<br/>"
    "&#8226; <b>Experience:</b> licensed since 2018, 10 to 20 sales a year since 2020, residential "
    "sales blended with real estate investing.", S["body"]),
    Spacer(1,6),
    box("<i>\"I've been a homeowner for 45-plus years and dealt with a number of realtors, but none "
    "like Kyle. He is truly the best: professional, thorough, and an exceptional communicator.\"</i> "
    "&nbsp;&mdash; Seller of 7106 Stratos Ln", colors.HexColor("#F4F1EA"), LINE),
    Spacer(1,8),
    Paragraph("Next steps", S["sec"]),
    Paragraph("1. A 30-minute conversation, in person or by phone, to walk through this and your "
    "questions.<br/>"
    "2. Confirm the listing stays fully off market so the 90-day reset completes (about mid-to-late "
    "November).<br/>"
    "3. Book photography and order the Montgomery County condo resale package now, so we launch the "
    "day the clock is clean.", S["body"]),
    Spacer(1,10),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=5),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty "
    "&nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
    Paragraph("Equal Housing Opportunity. Information deemed reliable but not guaranteed and should be "
    "independently verified. For informational purposes only; not tax, legal, or financial advice. "
    "Comp and market figures from Bright MLS and public records, September 2026. Days-on-market reset "
    "timing reflects current Bright MLS and Zillow practice and can change.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.4*inch, bottomMargin=0.45*inch, title="Listing Presentation - 8302 Woodmont Ave 203",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
