"""
Client PDF: 1341 Broening Hwy, options and value summary for Weijun Wang.
Branded teal/gold. Numbers come from Kyle's RPR CMA (9/22/2026) plus his local
knowledge (1118 Broening $168,000 June 2024, renovated ranges, tenant discount).
Run: python broening-options-pdf.py
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

OUT_DIR = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\1341-broening-hwy"
PDF_PATH = os.path.join(OUT_DIR, "1341-Broening-Hwy-Your-Options.pdf")

TEAL = colors.HexColor("#0F5C63")
GOLD = colors.HexColor("#C9A96A")
INK = colors.HexColor("#0D2226")
CARD = colors.HexColor("#FAF8F5")
GRAY = colors.HexColor("#6B7280")
RULE = colors.HexColor("#E3DCCB")

win = r"C:\Windows\Fonts"
for name, f in {"Arial": "arial.ttf", "Arial-Bold": "arialbd.ttf", "Arial-Italic": "ariali.ttf", "Arial-BoldItalic": "arialbi.ttf"}.items():
    pdfmetrics.registerFont(TTFont(name, os.path.join(win, f)))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-BoldItalic")
F, FB, FI = "Arial", "Arial-Bold", "Arial-Italic"

S = {
    "body": ParagraphStyle("body", fontName=F, fontSize=10, leading=14.5, textColor=INK, spaceAfter=6),
    "small": ParagraphStyle("small", fontName=FI, fontSize=8, leading=11, textColor=GRAY, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName=FB, fontSize=15, leading=19, textColor=TEAL, spaceBefore=12, spaceAfter=6, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName=FB, fontSize=11.5, leading=15, textColor=INK, spaceBefore=6, spaceAfter=3, keepWithNext=1),
    "cell": ParagraphStyle("cell", fontName=F, fontSize=9, leading=12, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName=FB, fontSize=9, leading=12, textColor=colors.white),
    "li": ParagraphStyle("li", fontName=F, fontSize=10, leading=14, textColor=INK, leftIndent=12, bulletIndent=0, spaceAfter=3),
}


def P(t, st="body"):
    t = t.replace("&", "&amp;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    assert not re.search("[\u2014\u2013]", t)
    return Paragraph(t, S[st])


def bullets(items):
    return [Paragraph("\u2022  " + i.replace("&", "&amp;"), S["li"]) for i in items]


def table(rows, widths, header=True, bold_first_col=False):
    data = []
    for ri, r in enumerate(rows):
        row = []
        for ci, c in enumerate(r):
            txt = str(c).replace("&", "&amp;")
            txt = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", txt)
            st = "cellb" if (header and ri == 0) else "cell"
            if bold_first_col and ci == 0 and ri > 0:
                txt = f"<b>{txt}</b>"
            row.append(Paragraph(txt, S[st]))
        data.append(row)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    st = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
          ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE)]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), TEAL))
    for i in range(2 if header else 1, len(rows), 2):
        st.append(("BACKGROUND", (0, i), (-1, i), CARD))
    t.setStyle(TableStyle(st))
    return t


def banner(width):
    inner = [
        [Paragraph('<font color="#C9A96A"><b>THE FRIEDMAN TEAM  |  eXp REALTY</b></font>', ParagraphStyle("k", fontName=FB, fontSize=8.5, leading=11))],
        [Paragraph("1341 Broening Hwy", ParagraphStyle("t", fontName=FB, fontSize=26, leading=30, textColor=colors.white))],
        [Paragraph("Your Options and What Each One Means", ParagraphStyle("s", fontName=FI, fontSize=12, leading=16, textColor=colors.white))],
        [Paragraph("Prepared for Weijun Wang  |  September 22, 2026  |  Baltimore, MD 21224", ParagraphStyle("b", fontName=F, fontSize=8.5, leading=11, textColor=colors.white))],
    ]
    t = Table(inner, colWidths=[width])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TEAL), ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("TOPPADDING", (0, 0), (0, 0), 14),
                           ("BOTTOMPADDING", (0, -1), (-1, -1), 12), ("LINEBELOW", (0, -1), (-1, -1), 3, GOLD)]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(F, 7.5)
    canvas.setFillColor(GRAY)
    canvas.drawString(0.75 * inch, 0.5 * inch, "Kyle Friedman  |  REALTOR\u00ae  |  443-789-3101  |  kyle@friedmanreteam.com")
    canvas.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build():
    os.makedirs(OUT_DIR, exist_ok=True)
    w = letter[0] - 1.5 * inch
    s = [banner(w), Spacer(1, 10)]

    s.append(P("The Property", "h2"))
    s.append(table([
        ["Address", "1341 Broening Hwy, Baltimore, MD 21224"],
        ["Type and size", "Brick townhouse, 1955. 2 bedrooms, 1 bath, 840 sq ft"],
        ["Systems", "Gas forced air heat, central air"],
        ["Basement", "Finished (public record)"],
        ["Occupancy", "Rented to a Section 8 tenant"],
        ["2026 tax assessment", "$111,500 (assessor market value $120,300)"],
        ["Last sold", "$55,150 in 1999"],
    ], [1.7 * inch, w - 1.7 * inch], header=False, bold_first_col=True))

    s.append(P("Where the Value Sits", "h2"))
    s.append(P("The value of your home depends on two things: its condition, and the tenant. Here are the three paths and what each is worth."))
    s.append(table([
        ["Path", "Estimated value"],
        ["**1. Sell now with the tenant in place**", "**About $100,000**"],
        ["**2. Wait for the lease to end, sell vacant as is**", "**$115,000 to $135,000**"],
        ["**3. Renovate, then sell**", "**$150,000 to $170,000**"],
    ], [w * 0.62, w * 0.38]))
    s.append(Spacer(1, 6))
    s.append(P("The highest sale for a 2 bedroom, 1 bath in your area is 1118 Broening Hwy at $168,000 (June 2024). Fully renovated 2 bedroom, 2 bath homes are selling around $200,000 to $220,000, but those are larger homes."))

    sales_block = [P("Recent Sales Nearby", "h2"), P("Closed sales of similar 2 bedroom, 1 bath townhomes (840 sq ft unless noted):")]
    sales_block.append(table([
        ["Address", "Sold", "Date", "Note"],
        ["1208 Broening Hwy", "$135,000", "June 2025", "Same street, same year built (1955)"],
        ["1108 Anglesea St", "$125,000", "Aug 2025", "4 days on market"],
        ["1106 Anglesea St", "$115,000", "Apr 2026", "Most recent sale, 1 day on market"],
        ["6436 Hartwait St", "$127,200", "Aug 2025", "Larger (1,050 sq ft), auction"],
        ["6313 Brown Ave", "$85,000", "Aug 2025", "Larger, estate sale, cash only, as is"],
    ], [1.7 * inch, 0.9 * inch, 0.95 * inch, w - 3.55 * inch]))
    sales_block.append(Spacer(1, 4))
    sales_block.append(P("The three closest comps average about **$125,000**."))
    s.append(KeepTogether(sales_block))

    s.append(P("What Buyers Are Asking Today", "h3"))
    s.append(table([
        ["Address", "Price", "Status", "Note"],
        ["6321 Brown Ave", "$154,900", "Active", "1,050 sq ft, listed Sept 10, 2026"],
        ["6302 Brown Ave", "$154,900", "Active", "1,112 sq ft, listed Sept 10, 2026"],
        ["1523 Elrino St", "$139,900", "Under contract", "840 sq ft, 300 days on the market"],
    ], [1.7 * inch, 0.9 * inch, 1.1 * inch, w - 3.7 * inch]))
    s.append(Spacer(1, 4))
    s.append(P("Asking prices sit above what has closed. Larger homes and updated homes are the ones that reach the top of the range."))

    s.append(P("The Three Paths", "h2"))

    def path(title, price, items):
        blk = [P(f"{title}", "h3"), P(f"**{price}**")] + bullets(items) + [Spacer(1, 6)]
        return KeepTogether(blk)

    s.append(path("Path 1: Sell now with the tenant in place", "About $100,000", [
        "Most buyers are investors, and they price the home on the rent and the lease.",
        "No repairs, no empty months, no renovation to manage. The fastest and simplest way to sell.",
        "You give up about $15,000 to $35,000 compared to selling vacant."]))
    s.append(path("Path 2: Wait, then sell vacant as is", "About $115,000 to $135,000", [
        "You gain roughly $15,000 to $35,000 over Path 1.",
        "You keep paying taxes, insurance, and upkeep while you wait.",
        "You cannot control when the lease ends or what condition the home is in afterward.",
        "Waiting only makes sense if it costs you less than what you gain."]))
    s.append(path("Path 3: Renovate, then sell", "About $150,000 to $170,000", [
        "The highest price, but not always the highest profit.",
        "Renovating adds roughly $35,000 compared to selling vacant as is.",
        "If the renovation costs more than that, Path 2 puts more money in your pocket.",
        "Managing a renovation from a distance adds risk and time."]))

    s.append(P("The Trade-Offs at a Glance", "h2"))
    s.append(table([
        ["", "Path 1", "Path 2", "Path 3"],
        ["Estimated price", "About $100,000", "$115,000 to $135,000", "$150,000 to $170,000"],
        ["Speed", "Fastest", "Slower, depends on the lease", "Slowest"],
        ["Effort", "Lowest", "Low", "Highest"],
        ["Risk", "Lowest", "Medium", "Highest"],
        ["Key question", "Is speed worth $15K to $35K?", "Will waiting cost less than you gain?", "Will the work cost less than $35K?"],
    ], [1.25 * inch, (w - 1.25 * inch) / 3, (w - 1.25 * inch) / 3, (w - 1.25 * inch) / 3], bold_first_col=True))

    s.append(P("Questions to Start Thinking About", "h2"))
    qs = ["How soon do you want the money? A faster sale and a higher price rarely go together.",
          "What is the monthly rent, and when does the lease end?",
          "Is the Section 8 contract current and in good standing? Does the tenant plan to stay?",
          "What condition is the home in, and would you want to manage a renovation?",
          "Would keeping it as a rental be better than selling?",
          "Have you talked to your accountant about the tax effect of selling?"]
    for i, q in enumerate(qs, 1):
        s.append(Paragraph(f"{i}.  {q}", S["li"]))

    s.append(P("Next Steps", "h2"))
    s.append(P("**What I need from you:** the monthly rent and lease end date; whether the Section 8 contract is current; the condition of the home and any updates you have made; and whether you prefer the money sooner or the highest price."))
    s.append(P("**What I will do:** give you a firm number for each path once I have the rent and lease details, run your estimated net proceeds for each path, and build the plan with you. I am ready to start as soon as you are."))
    s.append(Spacer(1, 6))
    s.append(P("**Kyle Friedman**  |  REALTOR\u00ae, The Friedman Team at eXp Realty<br/>443-789-3101  |  kyle@friedmanreteam.com<br/>8115 Maple Lawn Blvd, Suite 350, Fulton, MD 20759"))
    s.append(P("Estimates are based on public records, recent Baltimore area sales, and local market knowledge. This is not an appraisal. Comparable sale data from RPR, September 22, 2026. Equal Housing Opportunity.", "small"))

    doc = SimpleDocTemplate(PDF_PATH, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch, topMargin=0.7 * inch, bottomMargin=0.8 * inch,
                            title="1341 Broening Hwy: Your Options", author="Kyle Friedman, The Friedman Team")
    doc.build(s, onFirstPage=footer, onLaterPages=footer)
    print("wrote", PDF_PATH, os.path.getsize(PDF_PATH) // 1024, "KB")


if __name__ == "__main__":
    build()
