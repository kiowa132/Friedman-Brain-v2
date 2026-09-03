# -*- coding: utf-8 -*-
"""Net Proceeds / FSBO comparison PDF - 1705 Havre De Grace Dr, Edgewater
(Jefferson McBride). Copied from net-proceeds-8302-woodmont.py.

3 columns: sell to a door buyer as-is vs. list and sell at $470k / $485k.
Shown BEFORE mortgage payoff (her payoff is unknown - 2013 foreclosure notice
means it is not a near-paid-off 2005 loan). Point: listing nets more even
after commission, and she picks the buyer.
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\1705-havre-de-grace-dr\Net-Proceeds-1705-Havre-De-Grace.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

# ---------------- model ----------------
SCEN = [("Sell to a door buyer\n(as-is, no agent)", 435000, 0.0),
        ("List and sell\nat $470,000", 470000, 0.05),
        ("List and sell\nat $485,000", 485000, 0.05)]
XFER_SELLER = 0.010   # Anne Arundel transfer + recordation, seller's customary share (~1%) - confirm w/ title
FLAT = [
    ("Settlement / closing fee", 500),
    ("Deed &amp; document preparation", 150),
    ("Mortgage payoff processing &amp; lien release", 175),
    ("Wire, courier &amp; notary", 150),
]

def costs(price, comm):
    rows = [("Real estate commission (%s)" % ("5.0%, placeholder" if comm else "none"), price * comm),
            ("Anne Arundel transfer &amp; recordation &mdash; seller&rsquo;s share (~1.0%)", price * XFER_SELLER)]
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
        ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
    return b

story = []
iw, ih = 2000, 373
hdr = Table([[Image(LOGO, width=1.7*inch, height=1.7*inch*ih/iw),
    Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9.5, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
    colWidths=[3.7*inch, 3.6*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
story += [hdr, Spacer(1,4), HRFlowable(width="100%", thickness=1.4, color=GOLD, spaceAfter=9)]

story += [Paragraph("Door Offer vs. Listing: What You Actually Net", S["h1"]),
    Paragraph("Estimated proceeds, before paying off any mortgage", S["sub"]), Spacer(1,8)]

today = datetime.date.today().strftime("%B %#d, %Y")
left = [Paragraph("PROPERTY", S["lbl"]),
        Paragraph("1705 Havre De Grace Dr<br/>Edgewater, MD 21037<br/>Woodland Beach &middot; Anne Arundel County", S["val"])]
right = [Paragraph("PREPARED FOR", S["lbl"]),
         Paragraph("Jefferson McBride", S["val"]), Spacer(1,6),
         Paragraph("PREPARED BY", S["lbl"]),
         Paragraph("Kyle Friedman, The Friedman Team<br/>%s" % today, S["val"])]
pf = Table([[left, right]], colWidths=[3.65*inch, 3.65*inch])
pf.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),12),
    ("RIGHTPADDING",(0,0),(-1,-1),0),("BOX",(0,0),(-1,-1),0.5,LINE),
    ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("BACKGROUND",(0,0),(-1,-1),CREAM)]))
story += [pf, Spacer(1,8),
    Paragraph("The buyers knocking on your door during the renovation are almost all investors and "
    "flippers looking to buy near as-is value. This compares taking one of those offers against "
    "finishing the renovation and selling on the open market. Anne Arundel County seller costs; the "
    "mortgage payoff is the same subtraction in every column, so it does not change the comparison.",
    S["body"]), Spacer(1,8)]

# ---------------- table ----------------
col_item = 3.0*inch
col_num = (7.3*inch - col_item) / 3.0
def hcell(t):
    return Paragraph("<font color='white'><b>%s</b></font>" % t.replace("\n","<br/>"),
                     ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8.3, alignment=TA_CENTER, leading=10))

data = [[Paragraph("", S["cell"])] + [hcell(n) for n,_,_ in SCEN]]
data.append([cell("Sale price", b=True)] + [cell("<b>%s</b>" % money(p), r=True) for _,p,_ in SCEN])

sample = costs(SCEN[0][1], SCEN[0][2])
for i,(lbl,_) in enumerate(sample):
    row = [cell(lbl)]
    for _,p,c in SCEN:
        amt = costs(p,c)[i][1]
        row.append(cell(money(amt) if amt else "&mdash;", r=True))
    data.append(row)

tot = [sum(a for _,a in costs(p,c)) for _,p,c in SCEN]
data.append([cell("Total deductions", b=True)] + [cell("<b>&minus;%s</b>" % money(t), r=True) for t in tot])
nets = [p - t for (_,p,_),t in zip(SCEN, tot)]
netst = ParagraphStyle("net", fontName="Times-Bold", fontSize=12.5, textColor=TEAL, alignment=TA_RIGHT, leading=14)
data.append([Paragraph("<font color='#0F5C63'><b>NET BEFORE MORTGAGE PAYOFF</b></font>",
             ParagraphStyle("nl", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12))] +
            [Paragraph(money(n), netst) for n in nets])
data.append([cell("vs. the door offer", b=True)] +
            [cell("&mdash;" if i==0 else "<b>+%s</b>" % money(nets[i]-nets[0]), r=True) for i in range(3)])

t = Table(data, colWidths=[col_item] + [col_num]*3, hAlign="LEFT")
nr = len(data); net_r = nr-2; tot_r = nr-3
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),TEAL),
    ("BACKGROUND",(1,1),(-1,1),CREAM),
    ("BACKGROUND",(0,net_r),(-1,net_r),GOLD),
    ("BACKGROUND",(0,net_r+1),(-1,net_r+1),CREAM),
    ("LINEBELOW",(0,1),(-1,1),0.5,LINE),
    ("LINEABOVE",(0,tot_r),(-1,tot_r),0.8,TEAL),
    ("LINEABOVE",(0,net_r),(-1,net_r),1.0,TEAL),
    ("BOX",(0,0),(-1,-1),0.6,LINE),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("TOPPADDING",(0,net_r),(-1,net_r),6),("BOTTOMPADDING",(0,net_r),(-1,net_r),6),
    ("LEFTPADDING",(0,0),(0,-1),10),("RIGHTPADDING",(-1,0),(-1,-1),10),
    ("ROWBACKGROUNDS",(0,2),(-1,tot_r-1),[colors.white, colors.HexColor("#F7F4EE")]),
]))
story += [t, Spacer(1,9)]

story += [box(
    "<b>What this means.</b> Even after paying a full commission, finishing the renovation and "
    "selling on the open market nets you roughly <b>$15,000 to $25,000 more</b> than a door offer at "
    "as-is value, and more than that against a lowball. The renovation you are doing is exactly the "
    "value a door buyer wants to capture for themselves. Listing captures it for you.", CREAM, GOLD),
    Spacer(1,7),
    box(
    "<b>And you choose the buyer.</b> On the open market you will likely have several offers at "
    "$479,900. You can prioritize an owner-occupant family, review buyer letters, and put a "
    "no-assignment clause and an occupancy affidavit in the contract to keep wholesalers out. With "
    "one buyer at your door, you have one take-it-or-leave-it offer and no leverage.", colors.HexColor("#EAF1F0"), LINE),
    Spacer(1,6)]

story += [Paragraph("ASSUMPTIONS", S["lbl"]),
    Paragraph(
    "1. Estimate only, not a closing disclosure or a guarantee of proceeds. &nbsp; "
    "2. Door-offer price of $435,000 reflects recent as-is / un-renovated sales of this size in "
    "Woodland Beach ($415,000 to $430,000); an actual door offer could be higher or lower. &nbsp; "
    "3. List prices of $470,000 and $485,000 bracket recent renovated comps; 1604 Oriole Rd (same "
    "size, updated) sold at $480,000 in 13 days. Assumes the renovation is finished before listing. "
    "&nbsp; 4. Commission of 5.0% is a placeholder, negotiable and set in the listing agreement; "
    "buyer-agent compensation is negotiated separately. &nbsp; "
    "5. Anne Arundel County transfer and recordation taxes shown at the seller&rsquo;s customary "
    "portion (about 1.0%); the exact split is set by contract and confirmed by the title company. "
    "&nbsp; 6. Mortgage payoff is not shown because it reduces every column by the same amount. "
    "Provide the current payoff for a final net figure. &nbsp; "
    "7. Property-tax and any community-association proration are set at closing.", S["note"]),
    Spacer(1,6),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty &nbsp;|&nbsp; "
              "(443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
    Paragraph("8115 Maple Lawn Blvd, Suite 350, Fulton, MD 20759", S["foot"]),
    Paragraph("Planning purposes only. Not tax, legal, or accounting advice. Comp figures from Bright MLS and RPR, September 2026.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.45*inch, bottomMargin=0.5*inch, title="Door Offer vs Listing - 1705 Havre De Grace Dr",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
for (n,p,c) in SCEN:
    tc = sum(a for _,a in costs(p,c)); print(f"  {n[:22]:22} sale {p:,} deduct {tc:,.0f} net {p-tc:,.0f}")
