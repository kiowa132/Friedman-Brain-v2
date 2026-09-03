# -*- coding: utf-8 -*-
"""Branded client-facing Buyer Feasibility PDF - The Friedman Team.

REUSABLE. Copy + edit the DATA block for a new client. See
projects/feasibility-analysis.md for the method. Real Python:
C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe

Current instance: Jose Salas, move-up from 3002 Lewis Ln Havre de Grace.
Plan is to SELL Lewis Ln right after going under contract on the new home.
Grounded in a Bright MLS one-line pull (9/2/2026).
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\clients\Jose-Salas-Feasibility.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, textColor=TEAL, leading=19),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
 "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
 "val": ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
 "sec": ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=11.5, textColor=TEAL, leading=14, spaceBefore=3, spaceAfter=3),
 "body":ParagraphStyle("body", fontName="Helvetica", fontSize=8.6, textColor=INK, leading=11.9),
 "cell":ParagraphStyle("cell", fontName="Helvetica", fontSize=8.0, textColor=INK, leading=10.3),
 "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=8.0, textColor=INK, leading=10.3, alignment=TA_RIGHT),
 "boxb":ParagraphStyle("boxb", fontName="Helvetica", fontSize=8, textColor=INK, leading=11.3),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.8, textColor=TEAL, leading=10.5, alignment=TA_CENTER),
 "disc":ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7, textColor=GREY, leading=9, alignment=TA_CENTER),
}

def cellR(t, bold=False):
    st = ParagraphStyle("x", parent=S["cellR"], fontName="Helvetica-Bold" if bold else "Helvetica")
    return Paragraph(t, st)
def cell(t, bold=False):
    st = ParagraphStyle("x", parent=S["cell"], fontName="Helvetica-Bold" if bold else "Helvetica")
    return Paragraph(t, st)

def table(rows, col_w, header_row=True, pad=3.0):
    styc = [("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
            ("LEFTPADDING",(0,0),(0,-1),7),("RIGHTPADDING",(-1,0),(-1,-1),7),
            ("BOX",(0,0),(-1,-1),0.6,LINE),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#F7F4EE")])]
    if header_row:
        styc += [("BACKGROUND",(0,0),(-1,0),TEAL),("LINEBELOW",(0,0),(-1,0),0.4,LINE),
                 ("TEXTCOLOR",(0,0),(-1,0),colors.white),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")]
    t = Table(rows, colWidths=col_w, hAlign="LEFT")
    t.setStyle(TableStyle(styc))
    return t

def box(text, bg, border):
    b = Table([[Paragraph(text, S["boxb"])]], colWidths=[7.3*inch])
    b.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("BOX",(0,0),(-1,-1),0.5,border),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
    return b

story = []
iw, ih = 2000, 373
story += [Table([[Image(LOGO, width=1.7*inch, height=1.7*inch*ih/iw),
    Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9.5, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
    colWidths=[3.7*inch, 3.6*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)])),
    Spacer(1,4), HRFlowable(width="100%", thickness=1.4, color=GOLD, spaceAfter=9)]

today = datetime.date.today().strftime("%B %#d, %Y")
story += [Paragraph("Move-Up Feasibility", S["h1"]),
    Paragraph("Selling 3002 Lewis Ln and buying a larger home in the Havre de Grace area", S["sub"]),
    Spacer(1,7),
    Paragraph("PREPARED FOR", S["lbl"]),
    Paragraph("Jose Salas and family &nbsp;&middot;&nbsp; %s" % today, S["val"]),
    Spacer(1,8)]

story += [box(
    "<b>What this is.</b> A planning tool to see whether the move works on paper, not a loan "
    "application. It assumes you are approved. The plan: buy the new home first, then sell 3002 "
    "Lewis Ln right after we go under contract, using that equity as your down payment. Numbers "
    "below use real Bright MLS data pulled September 2, 2026 (4-plus beds, 3-plus full baths, "
    "2,800-plus sq ft, Havre de Grace / Aberdeen / Bel Air / Churchville). Rate 6.66%, 30-year "
    "fixed. Property tax about 1.15% of price.", CREAM, GOLD), Spacer(1,6)]

# ---- 1. Where the money starts ----
story += [Paragraph("1. Where the money starts: selling 3002 Lewis Ln", S["sec"])]
story += [Paragraph("We have not set a list price for 3002 Lewis Ln yet, so treat the proceeds as "
    "a wide range for now. Rough math: your likely sale price, minus the mortgage payoff, minus "
    "about 7% for commission and transfer and misc costs, lands somewhere around "
    "<b>$200,000 to $325,000</b> in net proceeds. We tighten this once we agree on a list price "
    "and you pull the exact payoff from your statement.", S["body"]), Spacer(1,5),
    Paragraph("<b>The gain should be tax-free.</b> You bought in 2012 for $250,900, so the gain "
    "is very likely well under the <b>$500,000 married-filing-jointly</b> exclusion for a primary "
    "residence. Sold as your primary home, that means <b>$0 federal and $0 Maryland tax</b> on it. "
    "Selling right after you buy keeps it that way, so there is no reason to rent it out.", S["body"]),
    Spacer(1,6)]

# ---- 2. What it costs ----
story += [Paragraph("2. What a home on your list costs here", S["sec"]),
    Paragraph("Detached homes, 4-plus bed / 3-plus full bath, roughly 4,000 to 6,000-plus sq ft "
    "total, in Havre de Grace, Aberdeen, Bel Air and Churchville are selling <b>$570K to $820K</b>, "
    "clustered <b>$650K to $760K</b>. Recent sales:", S["body"]), Spacer(1,4)]
rows = [[cell("Address"), cellR("Sold price"), cellR("Bd / Ba"), cellR("Sq Ft"), cell("City")]]
for a,p,bb,sf,c in [
    ("744 Falcon Ln","$625,000 &middot; Jun","4 / 3.1","4,884","Aberdeen"),
    ("555 Beards Hill Rd","$650,000 &middot; Apr","5 / 3.1","4,758","Aberdeen"),
    ("102 Flying Ebony Pl","$720,000 &middot; Jun","5 / 3.1","4,661","Havre de Grace"),
    ("1635 Vista Bay Ct","$730,000 &middot; May","5 / 3.1","4,404","Havre de Grace"),
    ("51 Fearless Ct","$737,500 &middot; Mar","4 / 4","6,382","Havre de Grace"),
    ("205 Glenville Rd","$800,000 &middot; Jun","4 / 3","5,724","Churchville"),
    ("1124 Oak Tree Dr","$815,000 &middot; Jun","5 / 4.1","5,882","Havre de Grace"),
]:
    rows.append([cell(a), cellR(p), cellR(bb), cellR(sf), cell(c)])
story += [table(rows, [1.7*inch, 1.5*inch, 0.85*inch, 0.8*inch, 1.6*inch]), Spacer(1,5),
    Paragraph("<b>Active or pending right now in your range:</b> 304 Sunrise Ct, HdG $675,000 "
    "(4/4.1) &nbsp;&bull;&nbsp; 41 Saturn Dr, HdG $694,000 (5/3.1) &nbsp;&bull;&nbsp; 583 Windsong "
    "Dr, Aberdeen $699,900 (5/4.1) &nbsp;&bull;&nbsp; 2809 Belcamp Rd, Bel Air $750,000 (5/3.1) "
    "&nbsp;&bull;&nbsp; 702 Monarchos Dr, HdG $750,000 (5/4.1).", S["body"]),
    Spacer(1,4),
    Paragraph("<b>What the market is telling us:</b> $650K to $760K is where homes this size "
    "actually trade and where the inventory is. About $825K is the resale ceiling, and only if it "
    "is priced right the first time (531 Risen Star Ct tried $875K twice, canceled both, cut to "
    "$825K and went pending). $850K-plus sits. The MLS sheet does not show garage bays or lot size, "
    "and a true <b>3-bay garage on real acreage</b> is the item most likely to push you to the "
    "<b>$775K to $850K</b> band, or toward new construction with a 3-car option (new builds near "
    "Bulle Rock run about $600K to $700K).", S["body"]),
    Spacer(1,6)]

# ---- 3. New monthly payment ----
story += [Paragraph("3. The new monthly payment", S["sec"]),
    Paragraph("Down payment funded by the Lewis Ln sale proceeds. The $200K and $250K rows below "
    "bracket the wide range above.", S["body"]), Spacer(1,3)]
rows = [[cell("Home price"), cellR("Down"), cellR("Loan"), cellR("P &amp; I"),
         cellR("+ Tax / ins."), cellR("New payment"), cellR("vs. ~$1,700 today")]]
for pr,dn,ln,pi,ti,piti,vs,bold in [
    ("$675,000","$250K","$425,000","$2,731","~$820","~$3,550","+$1,850 / mo",True),
    ("$675,000","$200K","$475,000","$3,052","~$820","~$3,870","+$2,170 / mo",False),
    ("$750,000","$250K","$500,000","$3,213","~$900","~$4,110","+$2,410 / mo",True),
    ("$750,000","$200K","$550,000","$3,534","~$900","~$4,430","+$2,730 / mo",False),
    ("$800,000","$250K","$550,000","$3,534","~$955","~$4,490","+$2,790 / mo",True),
    ("$800,000","$200K","$600,000","$3,856","~$955","~$4,810","+$3,110 / mo",False),
]:
    rows.append([cell(pr), cellR(dn), cellR(ln), cellR(pi), cellR(ti),
                 cellR("<b>%s</b>"%piti), cellR(("<b>%s</b>"%vs) if bold else vs)])
story += [table(rows, [0.9*inch, 0.6*inch, 0.85*inch, 0.75*inch, 0.75*inch, 0.95*inch, 1.15*inch]),
    Paragraph("No PMI at these down payments. Every extra $50K down drops the payment about "
    "$320 / month.", S["disc"]), Spacer(1,5)]

story += [box(
    "<b>The number that matters.</b> At $750,000 with your Lewis Ln equity down, the new payment "
    "is about <b>$4,100 / month</b>, roughly <b>$2,400 a month more</b> than you pay now. At $675K "
    "it is about +$1,850 / mo; at $800K about +$2,800 / mo. That is the trade for about double the "
    "house.", colors.HexColor("#EAF1F0"), LINE), Spacer(1,10)]

# ---- 4. Timing ----
story += [Paragraph("4. How the buy-before-sell timing works", S["sec"]),
    Paragraph(
    "You can buy before Lewis Ln sells. For the roughly 30 to 60 days both are in play, the new "
    "payment plus Lewis Ln (about $1,700) runs about <b>$5,250 to $6,200 / month</b> for that short "
    "window. Two ways to cover the down payment in the gap, your lender picks the cheaper one:<br/>"
    "&#8226; A <b>bridge loan or HELOC</b> against Lewis Ln before we list, paid off at "
    "settlement.<br/>"
    "&#8226; Put <b>less down from savings</b> now, then <b>recast</b> the new loan after Lewis Ln "
    "closes: a one-time re-amortization (about $250) that resets the payment down to the $250K-down "
    "row above.<br/>"
    "We list Lewis Ln the week you go under contract on the new home; a clean, updated Havre de "
    "Grace home in the low $400s should move in about 2 to 4 weeks.", S["body"]),
    Spacer(1,6)]

# ---- 5. Does it pencil ----
story += [Paragraph("5. Does it pencil?", S["sec"])]
rows = [[cell("Scenario"), cell("Read")]]
for sc, rd in [
    ("Buy $675K to $750K, sell Lewis Ln",
     "<b>Pencils</b> if a $3,550 to $4,110 / month payment is comfortable. The sale proceeds "
     "cover the down payment in this range and the gain is tax-free. This is the target."),
    ("Buy about $800K (3-car + acreage), sell Lewis Ln",
     "<b>Close.</b> About $4,490 / month. Works if the payment fits and you add a little cash to "
     "keep the loan near $550K."),
    ("Buy $850K-plus",
     "<b>Over</b> for a resale here. That tier sits, and the payment is $4,800-plus / month. Look "
     "at new construction with a 3-car option instead."),
]:
    rows.append([cell(sc), cell(rd)])
story += [table(rows, [2.2*inch, 5.1*inch]), Spacer(1,10)]

# ---- 6. Questions ----
story += [Paragraph("6. Questions to work through before we look", S["sec"]),
    Paragraph("Your answers set the real budget and the short list:", S["body"]), Spacer(1,3),
    Paragraph(
    "&#8226; <b>Garage:</b> must it be a true 3-bay attached garage, or would a 2-car plus a "
    "detached shop or extra parking pad work? (Biggest single price lever.)<br/>"
    "&#8226; <b>Land:</b> how much yard? A normal lot under an acre, or 1-plus acre with privacy?<br/>"
    "&#8226; <b>Town:</b> any preference or dealbreaker among Havre de Grace, Aberdeen, Bel Air, "
    "Churchville? Commutes for both of you?<br/>"
    "&#8226; <b>New vs. resale:</b> new builds around $600K to $700K exist in Havre de Grace with a "
    "3-car option. Open to that, or do you want mature trees and an established lot?<br/>"
    "&#8226; <b>Guest room:</b> does it need to be a main-level bedroom or suite, or is any spare "
    "bedroom fine? All bedrooms upstairs, or a main-level primary?<br/>"
    "&#8226; <b>Condition and timeline:</b> turnkey only, or would you take cosmetic updates for a "
    "better lot or price? When do you want to be in, and is there a school-year constraint?<br/>"
    "&#8226; <b>Comfortable payment:</b> what is the top monthly number you are okay with? That is "
    "the real ceiling, not the pre-approval.<br/>"
    "&#8226; <b>Down payment vs. cash kept back:</b> how much of the equity and savings goes down, "
    "how much stays liquid?<br/>"
    "&#8226; <b>Rank your list:</b> footprint, garage, yard, open concept, guest room, square "
    "footage, beds, baths. Which three are non-negotiable?", S["body"]),
    Spacer(1,6)]

# ---- Bottom line ----
story += [Paragraph("Bottom line", S["sec"]),
    Paragraph(
    "&#8226; A home matching your list trades <b>$650K to $760K</b> here; about <b>$825K</b> is "
    "the resale ceiling if it is priced right; $850K-plus sits.<br/>"
    "&#8226; Selling 3002 Lewis Ln should net somewhere around <b>$200,000 to $325,000</b> (we "
    "have not set a list price yet), and the gain should be <b>tax-free</b> because you are "
    "selling it as your primary home.<br/>"
    "&#8226; With those proceeds down, the new payment runs <b>$3,550 / mo at $675K</b> to "
    "<b>$4,490 / mo at $800K</b>, which is <b>+$1,850 to +$2,800 / month</b> over today.<br/>"
    "&#8226; You can <b>buy before you sell</b>. A bridge or HELOC, or a recast after the sale, "
    "covers the down payment during the short overlap.", S["body"]),
    Spacer(1,6)]

story += [box(
    "<b>To confirm on our call:</b> a list price and condition for 3002 Lewis Ln (that sets the "
    "proceeds range); the exact mortgage balance and monthly payment (assumed $180,000 and "
    "$1,700); cash on hand beyond the sale proceeds and how much to keep liquid; and your "
    "comfortable monthly payment and must-haves after seeing these numbers.", CREAM, GOLD),
    Spacer(1,5),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty "
    "&nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com", S["foot"]),
    Paragraph("Planning estimates only. Not tax, legal, lending, or investment advice. Payment "
    "figures are estimates at today's rate; a lender's Loan Estimate is the source of truth. "
    "Confirm any tax question with a CPA. MLS data from Bright MLS, pulled 9/2/2026.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.4*inch, bottomMargin=0.45*inch, title="Move-Up Feasibility - Jose Salas",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
