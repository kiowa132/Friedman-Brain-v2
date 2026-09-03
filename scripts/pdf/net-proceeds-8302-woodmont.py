# -*- coding: utf-8 -*-
"""Branded Net Proceeds PDF - 8302 Woodmont Ave #203, Bethesda (Wendy Fossen).

Copied from net-proceeds-pdf.py. Edits: Montgomery County costs, condo resale
fees, high loan payoff ($625,690), 3 sale-price scenarios ($675k/$690k/$715k),
and a "what this means" carry-cost box (margins are thin here).
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime, os

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\8302-woodmont-ave-203\Net-Proceeds-8302-Woodmont-203.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL  = colors.HexColor("#0F5C63")
GOLD  = colors.HexColor("#C9A96A")
CREAM = colors.HexColor("#FAF8F5")
INK   = colors.HexColor("#0D2226")
GREY  = colors.HexColor("#5B6B6E")
LINE  = colors.HexColor("#D9D2C4")

# ---------------- model ----------------
SCEN = [("Sell at $675,000", 675000), ("Sell at $690,000", 690000), ("Sell at $715,000", 715000)]
COMM = 0.05                       # total commission, PLACEHOLDER - Kyle to confirm
XFER_SELLER = 0.010              # Montgomery Co. transfer + recordation, seller's customary portion (~1.0%) - confirm w/ title
PAYOFF = 625690                  # seller-provided loan balance; add per-diem interest at settlement
PURCHASE = 749000               # bought Mar 2021
FLAT = [
    ("Settlement / closing fee", 600),
    ("Deed &amp; document preparation", 175),
    ("Mortgage payoff processing &amp; lien release", 175),
    ("Condo resale package + lender questionnaire", 450),
    ("HOA / condo account transfer &amp; status letter", 150),
    ("Wire, courier &amp; notary", 150),
]

def costs(price):
    rows = []
    rows.append(("Real estate commission (5.0%, placeholder)", price * COMM))
    rows.append(("Montgomery County transfer &amp; recordation &mdash; seller&rsquo;s share (~1.0%)", price * XFER_SELLER))
    for lbl, amt in FLAT:
        rows.append((lbl, amt))
    rows.append(("Mortgage payoff (balance provided by seller)", PAYOFF))
    return rows

def money(x):
    return "${:,.0f}".format(round(x))

# ---------------- styles ----------------
styles = {
    "h1":   ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17, textColor=TEAL, leading=20, spaceAfter=2),
    "sub":  ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
    "lbl":  ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
    "val":  ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9, textColor=INK, leading=13),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9, textColor=INK, leading=11),
    "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=9, textColor=INK, leading=11, alignment=TA_RIGHT),
    "note": ParagraphStyle("note", fontName="Helvetica", fontSize=7.2, textColor=GREY, leading=9.6),
    "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8, textColor=TEAL, leading=11, alignment=TA_CENTER),
    "disc": ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7.3, textColor=GREY, leading=9.5, alignment=TA_CENTER),
    "boxb": ParagraphStyle("boxb", fontName="Helvetica", fontSize=8.2, textColor=INK, leading=11.5),
}

story = []

# ---------------- header ----------------
iw, ih = 2000, 373
logo = Image(LOGO, width=1.7 * inch, height=1.7 * inch * ih / iw)
hdr = Table([[logo,
              Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
                        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9.5, textColor=TEAL,
                                       leading=12, alignment=TA_RIGHT))]],
             colWidths=[3.7 * inch, 3.6 * inch])
hdr.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                         ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
story += [hdr, Spacer(1, 4), HRFlowable(width="100%", thickness=1.4, color=GOLD, spaceAfter=9)]

story += [Paragraph("Estimated Net Proceeds", styles["h1"]),
          Paragraph("What you would walk away with at three sale prices", styles["sub"]), Spacer(1, 8)]

today = datetime.date.today().strftime("%B %#d, %Y")
left = [Paragraph("PROPERTY", styles["lbl"]),
        Paragraph("8302 Woodmont Ave, Unit 203<br/>Bethesda, MD 20814<br/>Stonehall Condominium &middot; Montgomery County", styles["val"])]
right = [Paragraph("PREPARED FOR", styles["lbl"]),
         Paragraph("Wendy Fossen", styles["val"]), Spacer(1, 6),
         Paragraph("PREPARED BY", styles["lbl"]),
         Paragraph("Kyle Friedman, The Friedman Team<br/>%s" % today, styles["val"])]
pf = Table([[left, right]], colWidths=[3.65 * inch, 3.65 * inch])
pf.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                        ("BACKGROUND", (0, 0), (-1, -1), CREAM)]))
story += [pf, Spacer(1, 8)]

story += [Paragraph(
    "The figures below estimate what you would net at settlement if the home sells at each price. "
    "They use standard Montgomery County seller costs and the loan balance you provided. Final "
    "numbers are set on the title company&rsquo;s settlement statement.", styles["body"]), Spacer(1, 8)]

# ---------------- main table ----------------
col_item = 3.15 * inch
col_num = (7.3 * inch - col_item) / 3.0
prices = [p for _, p in SCEN]

def hcell(t):
    return Paragraph("<font color='white'><b>%s</b></font>" % t, ParagraphStyle(
        "h", fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER, leading=11))

data = [[Paragraph("<font color='white'><b>&nbsp;</b></font>", styles["cell"])] +
        [hcell(money(p)) for _, p in SCEN]]
data.append([Paragraph("<b>Sale price</b>", styles["cell"])] +
            [Paragraph("<b>%s</b>" % money(p), styles["cellR"]) for p in prices])

sample = costs(prices[0])
for i, (lbl, _) in enumerate(sample):
    row = [Paragraph(lbl, styles["cell"])]
    for p in prices:
        row.append(Paragraph(money(costs(p)[i][1]), styles["cellR"]))
    data.append(row)

tot = [sum(a for _, a in costs(p)) for p in prices]
data.append([Paragraph("<b>Total deductions at closing</b>", styles["cell"])] +
            [Paragraph("<b>&minus;%s</b>" % money(t), styles["cellR"]) for t in tot])

nets = [p - t for p, t in zip(prices, tot)]
netstyle = ParagraphStyle("net", fontName="Times-Bold", fontSize=13, textColor=TEAL, alignment=TA_RIGHT, leading=15)
data.append([Paragraph("<font color='#0F5C63'><b>ESTIMATED NET TO YOU</b></font>",
                       ParagraphStyle("nl", fontName="Helvetica-Bold", fontSize=10, textColor=TEAL, leading=13))] +
            [Paragraph(money(n), netstyle) for n in nets])

t = Table(data, colWidths=[col_item] + [col_num] * 3, hAlign="LEFT")
nrows = len(data)
net_r = nrows - 1
tot_r = nrows - 2
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), TEAL),
    ("BACKGROUND", (1, 1), (-1, 1), CREAM),
    ("BACKGROUND", (0, net_r), (-1, net_r), GOLD),
    ("LINEBELOW", (0, 1), (-1, 1), 0.5, LINE),
    ("LINEABOVE", (0, tot_r), (-1, tot_r), 0.8, TEAL),
    ("LINEABOVE", (0, net_r), (-1, net_r), 1.0, TEAL),
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ("TOPPADDING", (0, net_r), (-1, net_r), 6), ("BOTTOMPADDING", (0, net_r), (-1, net_r), 6),
    ("LEFTPADDING", (0, 0), (0, -1), 10), ("RIGHTPADDING", (-1, 0), (-1, -1), 10),
    ("ROWBACKGROUNDS", (0, 2), (-1, tot_r - 1), [colors.white, colors.HexColor("#F7F4EE")]),
]))
story += [t, Spacer(1, 9)]

# ---------------- what this means ----------------
carry = Paragraph(
    "<b>What this means.</b> Your loan balance ($625,690) sits close to today&rsquo;s value, so the "
    "net is thin at every price and very sensitive to the final number. Holding the unit costs "
    "roughly <b>$3,700&ndash;$4,200 a month</b> (condo fee $967, taxes, loan interest). Each extra "
    "month on the market is more than the entire net at $675,000. The prior listing spent six months "
    "and eight price cuts getting from $775,000 to $685,000 without selling &mdash; repeating that "
    "slow decline would erase the proceeds. The goal this round is one correct price that sells "
    "inside 30 days.", styles["boxb"])
cb = Table([[carry]], colWidths=[7.1 * inch])
cb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EAF1F0")),
                        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
story += [cb, Spacer(1, 8)]

# ---------------- assumptions ----------------
story += [Paragraph("ASSUMPTIONS", styles["lbl"]),
          Paragraph(
    "1. Estimate only, not a closing disclosure or a guarantee of proceeds. &nbsp; "
    "2. Commission of 5.0% total is a placeholder, negotiable and set in the listing agreement; "
    "buyer-agent compensation is negotiated separately. &nbsp; "
    "3. Montgomery County transfer and recordation taxes are shown at the seller&rsquo;s customary "
    "portion (about 1.0% combined); the exact split is set by contract and confirmed by the title "
    "company. &nbsp; "
    "4. Mortgage payoff uses the balance provided by the seller; the lender&rsquo;s payoff letter "
    "will add per-diem interest and a small processing fee. Assumes no HELOC or other liens. &nbsp; "
    "5. Property-tax and condo-fee prorations are set at closing once a date is known and are not "
    "included above. &nbsp; "
    "6. Sale price shown is the contract price; homes typically sell 1&ndash;4% below list, so use "
    "the column at or below your list price to gauge a realistic net. &nbsp; "
    "7. You bought in 2021 for $749,000; these prices are below that, so there is no capital gain to "
    "tax. Confirm your situation with a CPA.", styles["note"]), Spacer(1, 8)]

# ---------------- footer ----------------
story += [HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
          Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty &nbsp;|&nbsp; "
                    "(443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", styles["foot"]),
          Paragraph("8115 Maple Lawn Blvd, Suite 350, Fulton, MD 20759", styles["foot"]),
          Spacer(1, 4),
          Paragraph("Provided for planning purposes only. Not tax, legal, or accounting advice. Figures change with "
                    "final contract terms and the settlement statement.", styles["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                  topMargin=0.45 * inch, bottomMargin=0.5 * inch,
                  title="Estimated Net Proceeds - 8302 Woodmont Ave 203",
                  author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
for n, p in SCEN:
    c = sum(a for _, a in costs(p)); print(f"  {n:18} sale {p:,} -> deductions {c:,.0f}  net {p-c:,.0f}")
