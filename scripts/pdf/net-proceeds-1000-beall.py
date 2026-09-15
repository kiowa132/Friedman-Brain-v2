# -*- coding: utf-8 -*-
"""Branded client-facing Net Proceeds PDF for 1000 Beall Dr (Eric Norman).
Copied from net-proceeds-pdf.py template, edited for this listing.
Run: py scripts/pdf/net-proceeds-1000-beall.py
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime, os

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\1000-beall-dr\Net-Proceeds-1000-Beall-Dr.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL  = colors.HexColor("#0F5C63")
GOLD  = colors.HexColor("#C9A96A")
CREAM = colors.HexColor("#FAF8F5")
INK   = colors.HexColor("#0D2226")
GREY  = colors.HexColor("#5B6B6E")
LINE  = colors.HexColor("#D9D2C4")

# ---------------- model ----------------
SCEN = [("Conservative", 300900), ("Recommended", 329900), ("Speculative", 364900)]
COMM = 0.05
XFER_SELLER = 0.0025 + 0.005 + 0.0033   # half MD state (0.5%) + half Harford county transfer (1.0%) + half Harford recordation ($6.60/1000)
FLAT = [
    ("Settlement / closing fee", 500),
    ("Deed &amp; document preparation", 200),
    ("Lien release, both loans", 250),
    ("Wire, courier &amp; notary", 150),
    ("Termite / WDI inspection", 100),
]
LOAN_BALANCE = 234785
PURCHASE = 175000

def costs(price):
    rows = []
    rows.append(("Real estate commission (5.0%)", price * COMM))
    rows.append(("MD state + Harford County transfer, recordation &mdash; seller&rsquo;s share (1.08%)", price * XFER_SELLER))
    for lbl, amt in FLAT:
        rows.append((lbl, amt))
    rows.append(("Estimated loan balance (not a payoff statement)", LOAN_BALANCE))
    return rows

def money(x):
    return "${:,.0f}".format(round(x))

# ---------------- styles ----------------
styles = {
    "h1":   ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=17, textColor=TEAL,
                           leading=20, spaceAfter=2),
    "sub":  ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
    "lbl":  ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD,
                           leading=10, spaceAfter=1),
    "val":  ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9, textColor=INK, leading=13),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9, textColor=INK, leading=11),
    "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=9, textColor=INK, leading=11, alignment=TA_RIGHT),
    "note": ParagraphStyle("note", fontName="Helvetica", fontSize=7.2, textColor=GREY, leading=9.6),
    "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8, textColor=TEAL, leading=11, alignment=TA_CENTER),
    "disc": ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7.3, textColor=GREY, leading=9.5, alignment=TA_CENTER),
    "boxh": ParagraphStyle("boxh", fontName="Helvetica-Bold", fontSize=8.5, textColor=TEAL, leading=12, spaceAfter=2),
    "boxb": ParagraphStyle("boxb", fontName="Helvetica", fontSize=8.2, textColor=INK, leading=11.5),
}

story = []

# ---------------- header ----------------
iw, ih = 2000, 373
logo_w = 1.7 * inch
logo = Image(LOGO, width=logo_w, height=logo_w * ih / iw)
hdr = Table([[logo,
              Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
                        ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9.5, textColor=TEAL,
                                       leading=12, alignment=TA_RIGHT))]],
             colWidths=[3.7 * inch, 3.6 * inch])
hdr.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                         ("LEFTPADDING", (0, 0), (-1, -1), 0),
                         ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
story += [hdr, Spacer(1, 4),
          HRFlowable(width="100%", thickness=1.4, color=GOLD, spaceAfter=9)]

# ---------------- title ----------------
story += [Paragraph("Estimated Net Proceeds", styles["h1"]),
          Paragraph("A seller&rsquo;s estimate comparing three price scenarios", styles["sub"]),
          Spacer(1, 8)]

# ---------------- property / prepared-for ----------------
today = datetime.date.today().strftime("%B %-d, %Y") if os.name != "nt" else datetime.date.today().strftime("%B %#d, %Y")
left = [Paragraph("PROPERTY", styles["lbl"]),
        Paragraph("1000 Beall Dr<br/>Joppa, MD 21085<br/>Harford County", styles["val"])]
right = [Paragraph("PREPARED FOR", styles["lbl"]),
         Paragraph("Eric Norman", styles["val"]),
         Spacer(1, 6),
         Paragraph("PREPARED BY", styles["lbl"]),
         Paragraph("Kyle Friedman, The Friedman Team<br/>%s" % today, styles["val"])]
pf = Table([[left, right]], colWidths=[3.65 * inch, 3.65 * inch])
pf.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                        ("TOPPADDING", (0, 0), (-1, -1), 7),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                        ("LEFTPADDING", (0, 0), (0, 0), 12),
                        ("LEFTPADDING", (1, 0), (1, 0), 12),
                        ("BACKGROUND", (0, 0), (-1, -1), CREAM)]))
story += [pf, Spacer(1, 8)]

story += [Paragraph(
    "The figures below estimate what you would net at closing at three different list prices. "
    "They are based on standard Maryland and Harford County seller costs and your estimated loan "
    "balance. Actual numbers are finalized on the title company&rsquo;s settlement statement.",
    styles["body"]), Spacer(1, 8)]

# ---------------- main table ----------------
col_item = 3.15 * inch
col_num = (7.3 * inch - col_item) / 3.0
prices = [p for _, p in SCEN]

def hcell(t):
    return Paragraph("<font color='white'><b>%s</b></font>" % t, ParagraphStyle(
        "h", fontName="Helvetica-Bold", fontSize=9, alignment=TA_CENTER, leading=11))

data = [[Paragraph("<font color='white'><b>&nbsp;</b></font>", styles["cell"])] +
        [hcell("%s<br/><font size=8>%s</font>" % (n, money(p))) for n, p in SCEN]]

# sale price row
data.append([Paragraph("<b>Sale price</b>", styles["cell"])] +
            [Paragraph("<b>%s</b>" % money(p), styles["cellR"]) for p in prices])

# cost rows
sample = costs(prices[0])
for i, (lbl, _) in enumerate(sample):
    row = [Paragraph(lbl, styles["cell"])]
    for p in prices:
        row.append(Paragraph(money(costs(p)[i][1]), styles["cellR"]))
    data.append(row)

# totals
tot = [sum(a for _, a in costs(p)) for p in prices]
data.append([Paragraph("<b>Total estimated costs of sale</b>", styles["cell"])] +
            [Paragraph("<b>&minus;%s</b>" % money(t), styles["cellR"]) for t in tot])

nets = [p - t for p, t in zip(prices, tot)]
netstyle = ParagraphStyle("net", fontName="Times-Bold", fontSize=13, textColor=TEAL, alignment=TA_RIGHT, leading=15)
data.append([Paragraph("<font color='#0F5C63'><b>ESTIMATED NET PROCEEDS</b></font>",
                       ParagraphStyle("nl", fontName="Helvetica-Bold", fontSize=10, textColor=TEAL, leading=13))] +
            [Paragraph(money(n), netstyle) for n in nets])

data.append([Paragraph("Net as % of sale price", styles["cell"])] +
            [Paragraph("{:.1f}%".format(100.0 * n / p), styles["cellR"]) for n, p in zip(nets, prices)])

t = Table(data, colWidths=[col_item] + [col_num] * 3, hAlign="LEFT")
nrows = len(data)
net_r = nrows - 2
tot_r = nrows - 3
style = [
    ("BACKGROUND", (0, 0), (-1, 0), TEAL),
    ("BACKGROUND", (1, 1), (-1, 1), CREAM),
    ("BACKGROUND", (0, net_r), (-1, net_r), GOLD),
    ("BACKGROUND", (0, net_r + 1), (-1, net_r + 1), CREAM),
    ("LINEBELOW", (0, 1), (-1, 1), 0.5, LINE),
    ("LINEABOVE", (0, tot_r), (-1, tot_r), 0.8, TEAL),
    ("LINEABOVE", (0, net_r), (-1, net_r), 1.0, TEAL),
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 3.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ("TOPPADDING", (0, net_r), (-1, net_r), 6),
    ("BOTTOMPADDING", (0, net_r), (-1, net_r), 6),
    ("LEFTPADDING", (0, 0), (0, -1), 10),
    ("RIGHTPADDING", (-1, 0), (-1, -1), 10),
    ("ROWBACKGROUNDS", (0, 2), (-1, tot_r - 1), [colors.white, colors.HexColor("#F7F4EE")]),
]
t.setStyle(TableStyle(style))
story += [t, Spacer(1, 8)]

# ---------------- side boxes ----------------
not_incl = Paragraph(
    "<b>Not included yet</b> &mdash; set once we finalize strategy: home warranty for the buyer, "
    "any buyer closing-cost concession, pre-listing repairs or prep, and property-tax proration "
    "(depends on the closing date). Each is $0 in this estimate.", styles["boxb"])
tax = Paragraph(
    "<b>Capital gains</b> &mdash; you bought in 2017 for $175,000. As your primary residence "
    "(owned and lived in 2 of the last 5 years), the first $250,000 of gain is excluded from "
    "federal tax &mdash; $500,000 if married filing jointly. At these prices the gain is well under "
    "that. Confirm with your CPA.", styles["boxb"])
bx = Table([[not_incl, tax]], colWidths=[3.55 * inch, 3.55 * inch])
bx.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#F4F1EA")),
                        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#EAF1F0")),
                        ("BOX", (0, 0), (0, 0), 0.5, LINE),
                        ("BOX", (1, 0), (1, 0), 0.5, LINE),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                        ("TOPPADDING", (0, 0), (-1, -1), 7),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                        ("INNERGRID", (0, 0), (-1, -1), 6, colors.white)]))
story += [bx, Spacer(1, 8)]

# ---------------- assumptions ----------------
story += [Paragraph("ASSUMPTIONS", styles["lbl"]),
          Paragraph(
    "1. Estimate only &mdash; not a closing disclosure or a guarantee of proceeds. &nbsp; "
    "2. Commission of 5.0% total is a placeholder; it is negotiable and set in the listing agreement, "
    "with buyer-agent compensation negotiated separately. &nbsp; "
    "3. Maryland state transfer (0.5%), Harford County transfer (1.0%), and Harford County recordation "
    "(~$6.60 per $1,000) are customarily split evenly with the buyer; the seller&rsquo;s combined half "
    "(1.08%) is shown. Exact split is set in the contract, confirm with title. &nbsp; "
    "4. Estimated loan balance is $234,785 (Sept 2026). This is an estimate, not a payoff statement, "
    "actual payoff may differ slightly with per-diem interest and fees. Confirm with a current "
    "statement before closing. &nbsp; "
    "5. Harford County property-tax proration is set at closing once a date is known.", styles["note"]),
          Spacer(1, 8)]

# ---------------- footer ----------------
story += [HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
          Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty &nbsp;|&nbsp; "
                    "(443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", styles["foot"]),
          Paragraph("8115 Maple Lawn Blvd, Suite 350, Fulton, MD 20759", styles["foot"]),
          Spacer(1, 4),
          Paragraph("This estimate is provided for planning purposes only and does not constitute tax, legal, or "
                    "accounting advice. Figures are subject to change based on final contract terms and the settlement statement.",
                    styles["disc"])]

doc = SimpleDocTemplate(OUT, pagesize=LETTER,
                        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                        topMargin=0.45 * inch, bottomMargin=0.5 * inch,
                        title="Estimated Net Proceeds - 1000 Beall Dr",
                        author="Kyle Friedman, The Friedman Team")
doc.build(story)
print("wrote", OUT)
for n, p in SCEN:
    c = sum(a for _, a in costs(p)); print(f"  {n:12} {p:,} -> costs {c:,.0f} net {p-c:,.0f} ({(p-c)/p*100:.1f}%)")
