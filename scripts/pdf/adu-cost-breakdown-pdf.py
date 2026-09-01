# -*- coding: utf-8 -*-
"""Branded 'Cost to Add a Rental Unit' PDF for Syed Imam.
Two itemized paths: basement suite vs. converting a detached structure to an ADU.
All-in: design, permits, county fees, septic/utilities, construction, licensing."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime, os

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\clients\Syed-Imam-Cost-to-Add-a-Rental-Unit.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL  = colors.HexColor("#0F5C63")
GOLD  = colors.HexColor("#C9A96A")
CREAM = colors.HexColor("#FAF8F5")
INK   = colors.HexColor("#0D2226")
GREY  = colors.HexColor("#5B6B6E")
LINE  = colors.HexColor("#D9D2C4")

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, textColor=TEAL, leading=19, spaceAfter=2),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
 "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
 "val": ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
 "body":ParagraphStyle("body", fontName="Helvetica", fontSize=8.7, textColor=INK, leading=12.5),
 "sec": ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=11, textColor=TEAL, leading=14, spaceBefore=4, spaceAfter=4),
 "grp": ParagraphStyle("grp", fontName="Helvetica-Bold", fontSize=8.3, textColor=INK, leading=11),
 "cell":ParagraphStyle("cell", fontName="Helvetica", fontSize=8.3, textColor=INK, leading=10.5),
 "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=8.3, textColor=INK, leading=10.5, alignment=TA_RIGHT),
 "tot": ParagraphStyle("tot", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12),
 "totR":ParagraphStyle("totR", fontName="Times-Bold", fontSize=10.5, textColor=TEAL, leading=13, alignment=TA_RIGHT),
 "note":ParagraphStyle("note", fontName="Helvetica", fontSize=7.6, textColor=GREY, leading=10),
 "boxb":ParagraphStyle("boxb", fontName="Helvetica", fontSize=7.6, textColor=INK, leading=10),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.8, textColor=TEAL, leading=10.5, alignment=TA_CENTER),
 "disc":ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7, textColor=GREY, leading=9, alignment=TA_CENTER),
}

story = []
iw, ih = 2000, 373
logo = Image(LOGO, width=1.7*inch, height=1.7*inch*ih/iw)
hdr = Table([[logo, Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9.5, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
        colWidths=[3.7*inch, 3.6*inch])
hdr.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
story += [hdr, Spacer(1,4), HRFlowable(width="100%", thickness=1.4, color=GOLD, spaceAfter=9)]

today = datetime.date.today().strftime("%B %#d, %Y")
story += [Paragraph("Cost to Add a Rental Unit", S["h1"]),
          Paragraph("Two paths, all-in &mdash; a basement suite vs. converting a detached structure to an ADU", S["sub"]),
          Spacer(1,8),
          Paragraph("PREPARED FOR", S["lbl"]),
          Paragraph("Syed Imam &nbsp;&middot;&nbsp; property to be identified &nbsp;&middot;&nbsp; %s" % today, S["val"]),
          Spacer(1,8),
          Paragraph("Planning estimates in 2026 Maryland pricing. Ranges are wide because the biggest costs "
                    "&mdash; septic capacity, waterproofing, and how far utilities must be trenched &mdash; depend "
                    "on the specific house. Get a contractor bid and confirm fees with the county before relying on "
                    "any number here. Figures cover Baltimore County (Sparks / Phoenix) and Howard County (Ellicott City); "
                    "where they differ, see the county note on page 2.", S["body"]),
          Spacer(1,10)]

CW_ITEM = 4.55*inch
CW_LO = (7.3*inch - CW_ITEM)/2.0
CW_HI = CW_LO

def money(x): return "${:,.0f}".format(x)

def cost_table(rows):
    """rows: list of ('group', label) or ('item', label, lo, hi) or ('total', label, lo, hi)"""
    data = [[Paragraph("<font color='white'><b>Line item</b></font>", ParagraphStyle("h",fontName="Helvetica-Bold",fontSize=8.3,leading=10)),
             Paragraph("<font color='white'><b>Low</b></font>", ParagraphStyle("h",fontName="Helvetica-Bold",fontSize=8.3,leading=10,alignment=TA_RIGHT)),
             Paragraph("<font color='white'><b>High</b></font>", ParagraphStyle("h",fontName="Helvetica-Bold",fontSize=8.3,leading=10,alignment=TA_RIGHT))]]
    styc = [("BACKGROUND",(0,0),(-1,0),TEAL),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("TOPPADDING",(0,0),(-1,-1),2.2),("BOTTOMPADDING",(0,0),(-1,-1),2.2),
            ("LEFTPADDING",(0,0),(0,-1),8),("RIGHTPADDING",(-1,0),(-1,-1),8),
            ("BOX",(0,0),(-1,-1),0.6,LINE),("LINEBELOW",(0,0),(-1,0),0.4,LINE)]
    r = 1
    for row in rows:
        if row[0] == "group":
            data.append([Paragraph(row[1], S["grp"]), "", ""])
            styc += [("BACKGROUND",(0,r),(-1,r),colors.HexColor("#EFEAE0")),("SPAN",(0,r),(-1,r))]
        elif row[0] == "total":
            _, lab, lo, hi = row
            data.append([Paragraph(lab, S["tot"]), Paragraph(money(lo), S["totR"]), Paragraph(money(hi), S["totR"])])
            styc += [("BACKGROUND",(0,r),(-1,r),GOLD),("TOPPADDING",(0,r),(-1,r),5),("BOTTOMPADDING",(0,r),(-1,r),5),
                     ("LINEABOVE",(0,r),(-1,r),0.8,TEAL)]
        else:
            _, lab, lo, hi = row
            data.append([Paragraph(lab, S["cell"]),
                         Paragraph(lo if isinstance(lo,str) else money(lo), S["cellR"]),
                         Paragraph(hi if isinstance(hi,str) else money(hi), S["cellR"])])
        r += 1
    t = Table(data, colWidths=[CW_ITEM, CW_LO, CW_HI], hAlign="LEFT")
    t.setStyle(TableStyle(styc))
    return t

# ---------- Section A ----------
A_rows = [
 ("group","DESIGN &amp; ENGINEERING"),
 ("item","Permit drawings / design set", 1500, 5000),
 ("item","Structural engineer (egress wells, framing changes)", 500, 1500),
 ("group","PERMITS &amp; COUNTY FEES"),
 ("item","Building permit", 200, 1200),
 ("item","Electrical / plumbing / mechanical permits", 150, 500),
 ("item","Plan review", 100, 400),
 ("item","Zoning / accessory-apartment or ADU permit", 150, 1000),
 ("item","Use &amp; occupancy certificate for the new unit", 50, 200),
 ("item","New-dwelling-unit fees (excise + school surcharge &mdash; see county note)", 0, 8400),
 ("group","SEPTIC &amp; UTILITIES  (most acreage homes are on well + septic)"),
 ("item","Health-dept septic evaluation / perc for an added bedroom", 250, 750),
 ("item","Septic capacity upgrade or expansion &mdash; only if required", 0, 45000),
 ("item","Separate electric subpanel + circuits", 4000, 10000),
 ("item","Separate electric meter or submeter (optional)", 500, 6000),
 ("item","HVAC &mdash; separate zone or mini-split", 4000, 9000),
 ("group","CONSTRUCTION"),
 ("item","Egress window(s) + wells (1&ndash;2 rooms)", 3000, 10000),
 ("item","Separate exterior entrance / areaway + door", 3000, 12000),
 ("item","Framing, insulation, drywall (~600&ndash;900 sf)", 15000, 35000),
 ("item","Kitchen / kitchenette (cabinets, counter, sink, range, fridge)", 6000, 20000),
 ("item","Full bathroom (add or renovate)", 8000, 18000),
 ("item","Plumbing rough-in + fixtures", 6000, 15000),
 ("item","Flooring", 3000, 7000),
 ("item","Waterproofing / drainage / sump pump", 1500, 18000),
 ("item","Fire separation + interconnected smoke/CO alarms", 1500, 4000),
 ("item","Sound insulation between units", 500, 2000),
 ("item","Separate laundry (stacked washer/dryer)", 1500, 3500),
 ("item","Paint, trim, doors, hardware", 2000, 6000),
 ("group","LICENSING &amp; SETUP TO RENT"),
 ("item","Rental license + county inspection (Balt. Co. ~$55/3 yr &middot; Howard $93.50/2 yr)", 55, 95),
 ("item","Lead rental registration + risk-reduction inspection (pre-1978 homes)", 350, 800),
 ("item","Landlord insurance increase (per year)", 400, 900),
 ("total","BASEMENT SUITE &mdash; ALL-IN (septic adequate)", 45000, 110000),
 ("total","Add if the septic system must be upgraded", 15000, 45000),
]

# ---------- Section B ----------
B_rows = [
 ("group","EVERYTHING IN SECTION A, PLUS:"),
 ("group","DESIGN &amp; ENGINEERING"),
 ("item","Full ADU plan set + site plan", 3000, 8000),
 ("item","Boundary / location survey", 800, 2500),
 ("group","STRUCTURE (existing garage shell)"),
 ("item","Foundation / footing / slab upgrade or replacement", 10000, 40000),
 ("item","Wall &amp; roof framing reinforcement, new roof", 8000, 30000),
 ("item","Full insulation package (walls, roof, slab edge)", 4000, 10000),
 ("item","Windows + exterior doors", 4000, 12000),
 ("group","UTILITIES TRENCHED FROM THE HOUSE / STREET  (the big variable)"),
 ("item","Water line + connection", 3000, 15000),
 ("item","Sewer line to septic or public main", 5000, 20000),
 ("item","Electric service / feeder / new meter", 5000, 20000),
 ("item","Gas line (if used)", 2000, 8000),
 ("group","BUILD-OUT"),
 ("item","Interior finish &mdash; drywall, floors, trim, paint (600&ndash;1,200 sf)", 25000, 60000),
 ("item","Kitchen (full)", 10000, 25000),
 ("item","Bathroom (full)", 10000, 20000),
 ("item","HVAC (mini-split or small system)", 5000, 12000),
 ("item","Water heater", 1500, 4000),
 ("item","Grading, sediment control, parking pad / walkway", 2000, 15000),
 ("item","County new-dwelling-unit fees (excise + school surcharge &mdash; see note)", 500, 8400),
 ("total","DETACHED STRUCTURE &rarr; ADU &mdash; ALL-IN", 120000, 260000),
 ("total","Build a NEW detached ADU from scratch instead", 180000, 400000),
]

story += [KeepTogether([Paragraph("Section A &nbsp;&mdash;&nbsp; Convert an existing basement into a legal rental suite", S["sec"]), Spacer(1,2)]),
          cost_table(A_rows), Spacer(1,10),
          Paragraph("Section B &nbsp;&mdash;&nbsp; Convert a detached structure (garage) into an ADU", S["sec"]), Spacer(1,3),
          cost_table(B_rows), Spacer(1,8)]

# ---------- county note ----------
note = Table([[Paragraph(
 "<b>County fee differences</b><br/>"
 "<b>Howard County (Ellicott City):</b> residential permit $0.25/sq ft; road excise tax $1.91/sq ft; school "
 "facilities surcharge $8.35/sq ft &mdash; but ADUs may be exempt from the school surcharge under Maryland SB 543 "
 "(confirm). ADU size limit: up to 75% of the main dwelling's footprint; allowed by-right in more zones since "
 "April 2026. Rental license $93.50, renewed every 2 years, inspection required.<br/>"
 "<b>Baltimore County (Sparks / Phoenix):</b> ADU size cap 800 sq ft on lots under 1 acre, 1,200 sq ft over 1 acre. "
 "The county's ADU ordinance is being finalized on Maryland's October 1, 2026 deadline &mdash; confirm the current "
 "permit path with Permits, Approvals &amp; Inspections. Rental registration ~$48&ndash;60/unit, renewed every 3 "
 "years, licensed inspection required; short-term rental is a separate $300/unit registration.<br/>"
 "<b>Both counties:</b> any pre-1978 home with a rented unit &mdash; Maryland MDE lead rental registration + "
 "risk-reduction inspection.", S["boxb"])]],
 colWidths=[7.3*inch])
note.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#EAF1F0")),("BOX",(0,0),(-1,-1),0.5,LINE),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
story += [note, Spacer(1,7)]

bl = Table([[Paragraph(
 "<b>Bottom line</b><br/>"
 "The basement suite is far cheaper &mdash; roughly <b>$45,000 to $110,000</b> all-in if the septic can take it &mdash; "
 "and the fastest to get rented. Converting a detached garage runs <b>$120,000 to $260,000+</b>; building a new "
 "detached ADU is <b>$180,000 to $400,000+</b>. Septic capacity, waterproofing, and utility trenching are what move "
 "these ranges the most, so those get checked on any specific house before an offer.", S["boxb"])]],
 colWidths=[7.3*inch])
bl.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),CREAM),("BOX",(0,0),(-1,-1),0.5,GOLD),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
story += [bl, Spacer(1,9),
          HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
          Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty &nbsp;|&nbsp; "
                    "(443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
          Spacer(1,3),
          Paragraph("Planning estimates only, not bids or quotes. Not tax, legal, or construction advice. Verify all "
                    "fees, size limits, and permit requirements with Baltimore County or Howard County and get "
                    "licensed-contractor bids before relying on these figures.", S["disc"])]

doc = SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
                        topMargin=0.4*inch, bottomMargin=0.5*inch,
                        title="Cost to Add a Rental Unit - Syed Imam", author="Kyle Friedman, The Friedman Team")
doc.build(story)
print("wrote", OUT)
