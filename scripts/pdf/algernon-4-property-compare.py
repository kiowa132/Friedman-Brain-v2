# -*- coding: utf-8 -*-
"""Branded 1-page buyer comparison - 4 properties for Algernon Carter (Sept 2026).
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\people\Algernon-4-Property-Comparison.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"
TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, textColor=TEAL, leading=18),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=11),
 "rh": ParagraphStyle("rh", fontName="Helvetica-Bold", fontSize=7.6, textColor=INK, leading=9.5),
 "c": ParagraphStyle("c", fontName="Helvetica", fontSize=7.6, textColor=INK, leading=9.6),
 "ch": ParagraphStyle("ch", fontName="Helvetica-Bold", fontSize=8, textColor=colors.white, leading=10, alignment=TA_CENTER),
 "cc": ParagraphStyle("cc", fontName="Helvetica", fontSize=7.6, textColor=INK, leading=9.6, alignment=TA_CENTER),
 "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=7.3, textColor=TEAL, leading=10, alignment=TA_CENTER),
 "disc": ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=6.6, textColor=GREY, leading=8.5, alignment=TA_CENTER),
}
def c(t, ctr=True): return Paragraph(t, S["cc"] if ctr else S["c"])

COLS = ["6301 Liberty Rd<br/><font size=6 color='#5B6B6E'>Gwynn Oak &middot; Balt. County</font>",
        "6909 Digby Rd<br/><font size=6 color='#5B6B6E'>Gwynn Oak &middot; Balt. County</font>",
        "1018 Wilmington Ave<br/><font size=6 color='#5B6B6E'>SW Baltimore City</font>",
        "4315 W Forest Park Ave<br/><font size=6 color='#5B6B6E'>Forest Park &middot; Balt. City</font>"]

ROWS = [
 ("List price", ["$350,000", "$375,000", "$345,000", "$339,900"]),
 ("Beds / baths", ["4 / 2", "4 / 2", "3 / 2.5", "5 / 2.5"]),
 ("Sq ft ($/sq ft)", ["2,200 ($159)", "2,040 ($184)", "1,475 ($234)", "1,566 ($217)"]),
 ("Year built", ["1942", "1962", "1924", "1924"]),
 ("Lot / parking", ["0.19 ac &middot; garage + pad", "0.22 ac corner &middot; big driveway", "0.14 ac &middot; 4 spaces incl. rear", "0.14 ac corner &middot; street only"]),
 ("Cooling", ["Mini-split", "Central", "Window units", "Central"]),
 ("Basement", ["Finished: bed + full bath", "Finished: + full bath", "Unfinished / storage", "Unfinished"]),
 ("Est. taxes / yr", ["~$3,300", "~$2,400", "~$3,100", "~$4,000"]),
 ("Zoned high school", ["Woodlawn (2/10)", "Pikesville (5/10)", "Vivien Thomas (2/10)", "Forest Park (2/10)"]),
 ("Days on market", ["<b>56</b>", "<b>1</b> (fresh flip)", "<b>24</b>", "<b>6</b>"]),
 ("Price history", ["5 listings since 3/25; $420k &rarr; $350k; also unrented", "Sold $255k 7/26, now $375k", "One price, no cuts", "One price, no cuts"]),
 ("Room to negotiate", ["<b>High</b> &mdash; target $325&ndash;335k + closing help", "None yet &mdash; wait a month", "Some &mdash; $335&ndash;340k + credit", "Low now &mdash; near ask + VA credit"]),
 ("Fits ~$340k VA approval?", ["Over, but very workable", "No ($35k over)", "$5k over", "<b>Yes</b>"]),
 ("Watch-outs", ["On busy Liberty Rd (noise, resale)", "Priced firm; confirm solar owned", "Weak area/schools; window AC", "City taxes high; 1924 build, VA appraisal"]),
]

story = []
iw, ih = 2000, 373
story += [Table([[Image(LOGO, width=1.5*inch, height=1.5*inch*ih/iw),
    Paragraph("THE FRIEDMAN TEAM<br/><font size=6 color='#5B6B6E'>brokered by eXp Realty</font>",
        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=8.5, textColor=TEAL, leading=11, alignment=TA_RIGHT))]],
    colWidths=[5.0*inch, 5.0*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)])),
    Spacer(1,3), HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceAfter=7),
    Paragraph("Four Properties, Side by Side", S["h1"]),
    Paragraph("Prepared for Algernon Carter &middot; %s &middot; the negotiation read is driven by days on market and price history"
              % datetime.date.today().strftime("%B %#d, %Y"), S["sub"]),
    Spacer(1,8)]

data = [[Paragraph("", S["rh"])] + [Paragraph(h, S["ch"]) for h in COLS]]
for label, vals in ROWS:
    data.append([Paragraph(label, S["rh"])] + [c(v) for v in vals])

col0 = 1.35*inch
cw = (10.0*inch - col0) / 4.0
t = Table(data, colWidths=[col0] + [cw]*4, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),TEAL),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),3.4),("BOTTOMPADDING",(0,0),(-1,-1),3.4),
    ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
    ("BOX",(0,0),(-1,-1),0.6,LINE),
    ("INNERGRID",(0,0),(-1,-1),0.4,LINE),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#F7F4EE")]),
    ("BACKGROUND",(0,10),(0,10),CREAM),        # days on market row label
    ("BACKGROUND",(0,12),(-1,12),colors.HexColor("#EAF1F0")),  # room to negotiate row
    ("BACKGROUND",(1,1),(1,1),colors.HexColor("#F0EBDF")),
]))
story += [t, Spacer(1,8),
    Paragraph("<b>Bottom line.</b> 6301 Liberty is the one to push on: the seller has chased this for 18 months and can't sell or rent it, so a VA offer in the low $330s with closing costs covered is realistic (trade-off is the busy road). "
    "4315 W Forest Park already fits the approval, so offer near ask and have the seller pay closing costs. Digby only if you'll stretch and it's still around in a few weeks. Wilmington is the middle option but the weakest location.",
    ParagraphStyle("bl", fontName="Helvetica", fontSize=8, textColor=INK, leading=11.4)),
    Spacer(1,8),
    HRFlowable(width="100%", thickness=0.9, color=GOLD, spaceAfter=4),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com", S["foot"]),
    Paragraph("Prices, days on market, and history from Bright MLS via public listing data, September 2026. Estimates only; not an appraisal or a guarantee of negotiability. "
    "Loan and VA appraisal questions go to your lender.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=landscape(LETTER), leftMargin=0.5*inch, rightMargin=0.5*inch,
    topMargin=0.4*inch, bottomMargin=0.4*inch, title="4 Property Comparison - Algernon Carter",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
