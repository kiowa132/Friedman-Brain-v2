# -*- coding: utf-8 -*-
"""Net Proceeds PDF - 261 Magothy Bridge Rd, Pasadena MD 21122 (Blaine Welker).
Copied from net-proceeds-1705-havre-de-grace.py.

Straight 3-scenario net proceeds at $475k / $490k / $510k. Shown BEFORE loan
payoff: RPR shows a possible first mortgage plus a HELOC plus a 2016 commercial
line, and Blaine has not confirmed what is still open. Anne Arundel County
seller costs.
Run: py scripts/pdf/net-proceeds-261-magothy.py
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\261-magothy-bridge-rd\Net-Proceeds-261-Magothy-Bridge.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

# ---------------- model ----------------
SCEN = [("List and sell\nat $475,000", 475000),
        ("List and sell\nat $490,000", 490000),
        ("List and sell\nat $510,000", 510000)]
COMMISSION = 0.05     # placeholder, negotiable, set in the listing agreement
XFER_SELLER = 0.010   # Anne Arundel transfer + recordation, seller's customary share (~1%) - confirm w/ title
FLAT = [
    ("Settlement / closing fee", 500),
    ("Deed &amp; document preparation", 250),
    ("Payoff processing &amp; lien release (per lien)", 200),
    ("Wire, courier &amp; notary", 150),
    ("Termite inspection (Maryland contract)", 75),
]

def costs(price):
    rows = [("Real estate commission (5.0%, placeholder)", price * COMMISSION),
            ("Anne Arundel transfer &amp; recordation, seller&rsquo;s share (~1.0%)", price * XFER_SELLER)]
    rows += FLAT
    return rows

def money(x):
    return "${:,.0f}".format(round(x))

S = {
 "h1":   ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17, textColor=TEAL, leading=20, spaceAfter=2),
 "sub":  ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
 "lbl":  ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
 "val":  ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
 "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9, textColor=INK, leading=13),
 "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=8.6, textColor=INK, leading=11),
 "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=8.6, textColor=INK, leading=11, alignment=TA_RIGHT),
 "note": ParagraphStyle("note", fontName="Helvetica", fontSize=7.2, textColor=GREY, leading=9.6),
 "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8, textColor=TEAL, leading=11, alignment=TA_CENTER),
 "disc": ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7.3, textColor=GREY, leading=9.5, alignment=TA_CENTER),
 "boxb": ParagraphStyle("boxb", fontName="Helvetica", fontSize=8.3, textColor=INK, leading=11.6),
}

def cell(t, r=False, b=False):
    st = ParagraphStyle("x", parent=S["cellR" if r else "cell"], fontName="Helvetica-Bold" if b else "Helvetica")
    return Paragraph(t, st)

def box(text, bg, bd):
    b = Table([[Paragraph(text, S["boxb"])]], colWidths=[7.1*inch])
    b.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("BOX",(0,0),(-1,-1),0.5,bd),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
    return b

story = []
iw, ih = 2000, 373
hdr = Table([[Image(LOGO, width=1.7*inch, height=1.7*inch*ih/iw),
    Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9.5, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
    colWidths=[3.7*inch, 3.6*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
story += [hdr, Spacer(1,3), HRFlowable(width="100%", thickness=1.4, color=GOLD, spaceAfter=6)]

story += [Paragraph("Estimated Net Proceeds", S["h1"]),
    Paragraph("What you walk away with at three list prices, before paying off any loan", S["sub"]), Spacer(1,5)]

today = datetime.date.today().strftime("%B %#d, %Y")
left = [Paragraph("PROPERTY", S["lbl"]),
        Paragraph("261 Magothy Bridge Rd<br/>Pasadena, MD 21122<br/>Magothy Forge &middot; Anne Arundel County", S["val"])]
right = [Paragraph("PREPARED FOR", S["lbl"]),
         Paragraph("Blaine Welker", S["val"]), Spacer(1,6),
         Paragraph("PREPARED BY", S["lbl"]),
         Paragraph("Kyle Friedman, The Friedman Team<br/>%s" % today, S["val"])]
pf = Table([[left, right]], colWidths=[3.65*inch, 3.65*inch])
pf.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),12),
    ("RIGHTPADDING",(0,0),(-1,-1),0),("BOX",(0,0),(-1,-1),0.5,LINE),
    ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("BACKGROUND",(0,0),(-1,-1),CREAM)]))
story += [pf, Spacer(1,6),
    Paragraph("Three list-price scenarios across the competitive range for a renovated home this "
    "size in Pasadena. Anne Arundel County seller costs. The loan payoff is the same subtraction in "
    "every column, so it is shown separately below rather than inside the comparison.", S["body"]),
    Spacer(1,6)]

# ---------------- table ----------------
col_item = 3.0*inch
col_num = (7.3*inch - col_item) / 3.0
def hcell(t):
    return Paragraph("<font color='white'><b>%s</b></font>" % t.replace("\n","<br/>"),
                     ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8.3, alignment=TA_CENTER, leading=10))

data = [[Paragraph("", S["cell"])] + [hcell(n) for n,_ in SCEN]]
data.append([cell("Sale price", b=True)] + [cell("<b>%s</b>" % money(p), r=True) for _,p in SCEN])

sample = costs(SCEN[0][1])
for i,(lbl,_) in enumerate(sample):
    row = [cell(lbl)]
    for _,p in SCEN:
        amt = costs(p)[i][1]
        row.append(cell(money(amt), r=True))
    data.append(row)

tot = [sum(a for _,a in costs(p)) for _,p in SCEN]
data.append([cell("Total estimated costs", b=True)] + [cell("<b>&minus;%s</b>" % money(t), r=True) for t in tot])
nets = [p - t for (_,p),t in zip(SCEN, tot)]
netst = ParagraphStyle("net", fontName="Times-Bold", fontSize=12.5, textColor=TEAL, alignment=TA_RIGHT, leading=14)
data.append([Paragraph("<font color='#0F5C63'><b>NET BEFORE LOAN PAYOFF</b></font>",
             ParagraphStyle("nl", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12))] +
            [Paragraph(money(n), netst) for n in nets])
data.append([cell("Net as % of sale price", b=True)] +
            [cell("%.1f%%" % (n / p * 100), r=True) for (_,p),n in zip(SCEN, nets)])
data.append([cell("Less: your loan and lien payoff", b=True)] +
            [cell("&minus; ( bring statement )", r=True) for _ in SCEN])
data.append([Paragraph("<font color='#0F5C63'><b>ESTIMATED NET TO YOU</b></font>",
             ParagraphStyle("nl", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12))] +
            [Paragraph("&mdash;", netst) for _ in SCEN])

t = Table(data, colWidths=[col_item] + [col_num]*3, hAlign="LEFT")
nr = len(data)
net_r = nr - 4          # NET BEFORE LOAN PAYOFF row
tot_r = net_r - 1       # Total estimated costs row
final_r = nr - 1        # ESTIMATED NET TO YOU row
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),TEAL),
    ("BACKGROUND",(1,1),(-1,1),CREAM),
    ("BACKGROUND",(0,net_r),(-1,net_r),GOLD),
    ("BACKGROUND",(0,final_r),(-1,final_r),CREAM),
    ("LINEBELOW",(0,1),(-1,1),0.5,LINE),
    ("LINEABOVE",(0,tot_r),(-1,tot_r),0.8,TEAL),
    ("LINEABOVE",(0,net_r),(-1,net_r),1.0,TEAL),
    ("LINEABOVE",(0,final_r),(-1,final_r),1.0,TEAL),
    ("BOX",(0,0),(-1,-1),0.6,LINE),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("TOPPADDING",(0,net_r),(-1,net_r),6),("BOTTOMPADDING",(0,net_r),(-1,net_r),6),
    ("TOPPADDING",(0,final_r),(-1,final_r),6),("BOTTOMPADDING",(0,final_r),(-1,final_r),6),
    ("LEFTPADDING",(0,0),(0,-1),10),("RIGHTPADDING",(-1,0),(-1,-1),10),
    ("ROWBACKGROUNDS",(0,2),(-1,tot_r-1),[colors.white, colors.HexColor("#F7F4EE")]),
]))
story += [t, Spacer(1,7)]

story += [box(
    "<b>The loan payoff.</b> Public records show a first mortgage, a home equity line, and a 2016 "
    "commercial line have all been recorded against the property over the years. Bring your current "
    "payoff statement for each loan that is still open. Subtract that total from the net above and "
    "that is your take-home. The renovation you put in raises the sale price and the net; it does "
    "not change the payoff.", CREAM, GOLD),
    Spacer(1,5),
    box(
    "<b>Taxes.</b> You bought in 2010 for $274,900. If this has been your primary residence for at "
    "least two of the last five years, the first $250,000 of gain (single) or $500,000 (married "
    "filing jointly) is excluded from federal capital gains tax. Your gain here is well under that "
    "before the renovation is even added to your cost basis, so the sale is very likely fully "
    "federal-tax-free. Confirm with your CPA.", colors.HexColor("#EAF1F0"), LINE),
    Spacer(1,5)]

story += [Paragraph("ASSUMPTIONS", S["lbl"]),
    Paragraph(
    "1. Estimate only, not a closing disclosure or a guarantee of proceeds. &nbsp; "
    "2. List prices of $475,000 to $510,000 bracket the competitive range for a renovated home this "
    "size in Pasadena 21122 (median sold price $478,500, median sold price per square foot about "
    "$272, August 2026). The exact list price is set at the walk-through. &nbsp; "
    "3. Commission of 5.0% is a placeholder, negotiable, and set in the listing agreement; "
    "buyer-agent compensation is negotiated separately. &nbsp; "
    "4. Anne Arundel transfer and recordation taxes shown at the seller&rsquo;s customary portion "
    "(about 1.0%); the exact split is set by contract and confirmed by title. &nbsp; "
    "5. Loan and lien payoff, property-tax proration, any community-association fee, seller "
    "concessions, a buyer home warranty, or agreed repairs are not included here and reduce the "
    "net. Provide payoff statements for a final figure.", S["note"]),
    Spacer(1,4),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=3),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty &nbsp;|&nbsp; "
              "(443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
    Paragraph("8115 Maple Lawn Blvd, Suite 350, Fulton, MD 20759", S["foot"]),
    Paragraph("Planning purposes only. Not tax, legal, or accounting advice. Market figures from RPR and Bright MLS, September 2026.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.4*inch, bottomMargin=0.4*inch, title="Net Proceeds - 261 Magothy Bridge Rd",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
for (n,p) in SCEN:
    tc = sum(a for _,a in costs(p)); print(f"  {n[:22]:22} sale {p:,} costs {tc:,.0f} net {p-tc:,.0f} ({(p-tc)/p*100:.1f}%)")
