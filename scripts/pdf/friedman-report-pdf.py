"""
Friedman Report PDF review draft (the "blueprint" built before every other
channel). Renders drafts/friedman-report/<week>/report-core.md into a branded
PDF, so the PDF can never disagree with the master narrative.

Weekly use: copy this file's WEEK block below, update it (title, tiles, FMMI,
chart series), point MD_PATH / PDF_PATH at the new week, and run:
    python friedman-report-pdf.py

The markdown subset it understands: ## / ### headings, paragraphs, **bold**,
*italic*, - bullets, 1. numbered lists, | pipe tables, --- (page break).
Special markers in report-core.md:
    <!-- TILES -->        stat-tile grid (from WEEK["tiles"]); the plain
                           markdown table right after it is skipped
    <!-- FMMI -->         the four component bars (from WEEK["fmmi"])
    <!-- CHART:days -->   / <!-- CHART:rate -->  (two in a row sit side by side)
No em/en dashes are ever emitted as punctuation (brand rule).
"""
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Flowable, KeepTogether, ListFlowable, ListItem,
                                PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

# ----------------------------------------------------------------------------
# THIS WEEK (edit weekly)
# ----------------------------------------------------------------------------
BASE = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\drafts\friedman-report\2026-09-14-to-09-20"
MD_PATH = os.path.join(BASE, "report-core.md")
PDF_PATH = os.path.join(BASE, "The-Friedman-Report-2026-09-14_09-20.pdf")

WEEK = {
    "label": "Week of September 14-20, 2026",
    "headline": "Prices Held. The Clock Didn't.",
    "sub": "Maryland Market Intelligence  |  Week of September 14-20, 2026",
    "byline": "Kyle Friedman  |  The Friedman Team at eXp Realty  |  Numbers Over Guesswork",
    "intro": "A hyperlocal, data-driven weekly Maryland market report.",
    # (label, value, delta text, tone)  tone: good | bad | flat
    "tiles": [
        ("HOMES SOLD", "984", "+39.0%", "good"),
        ("NEW LISTINGS", "2,269", "-4.1%", "flat"),
        ("PENDING", "482", "flat +0.2%", "flat"),
        ("MEDIAN SOLD PRICE", "$449,900", "+1.1%", "good"),
        ("MEDIAN DAYS TO CONTRACT", "25 days", "+5 from 20", "bad"),
        ("PRICE REDUCTIONS", "1,786", "-11.2%", "good"),
        ("30-YR FIXED RATE", "6.95%", "+19 bp", "bad"),
        ("FMMI SCORE", "44 / 100", "cooling", "bad"),
    ],
    "fmmi": [("DEMAND", 54), ("SELLER STRENGTH", 55), ("MARKET SPEED", 42), ("RATE ENVIRONMENT", 24)],
    "charts": {
        "days": {
            "title": "Median days to contract (closed sales)",
            "labels": ["Aug 24-30", "Aug 31-Sep 6", "Sep 7-13", "Sep 14-20"],
            "values": [18, 21, 20, 25],
        },
        "rate": {
            "title": "Freddie Mac 30-year fixed rate",
            "labels": ["Aug 27", "Sep 3", "Sep 10", "Sep 17"],
            "values": [6.66, 6.71, 6.76, 6.95],
        },
    },
}

TEAL = colors.HexColor("#0F5C63")
GOLD = colors.HexColor("#C9A96A")
INK = colors.HexColor("#0D2226")
CARD = colors.HexColor("#FAF8F5")
RED = colors.HexColor("#B5544A")
GRAY = colors.HexColor("#6B7280")
TRACK = colors.HexColor("#EAE3D6")
RULE = colors.HexColor("#E3DCCB")

# ----------------------------------------------------------------------------
# fonts
# ----------------------------------------------------------------------------
def _register_fonts():
    win = r"C:\Windows\Fonts"
    files = {"Arial": "arial.ttf", "Arial-Bold": "arialbd.ttf",
             "Arial-Italic": "ariali.ttf", "Arial-BoldItalic": "arialbi.ttf"}
    if all(os.path.exists(os.path.join(win, f)) for f in files.values()):
        for name, f in files.items():
            pdfmetrics.registerFont(TTFont(name, os.path.join(win, f)))
        pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                                      italic="Arial-Italic", boldItalic="Arial-BoldItalic")
        return "Arial", "Arial-Bold", "Arial-Italic"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"


F, FB, FI = _register_fonts()

ST = {
    "body": ParagraphStyle("body", fontName=F, fontSize=9.6, leading=14.2, textColor=INK, spaceAfter=7),
    "note": ParagraphStyle("note", fontName=FI, fontSize=8, leading=11.2, textColor=GRAY, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName=FB, fontSize=15, leading=18, textColor=TEAL,
                         spaceBefore=14, spaceAfter=7, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName=FB, fontSize=11, leading=14, textColor=INK,
                         spaceBefore=8, spaceAfter=4, keepWithNext=1),
    "cell": ParagraphStyle("cell", fontName=F, fontSize=8.4, leading=10.6, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName=FB, fontSize=8.4, leading=10.6, textColor=colors.white),
    "cell_s": ParagraphStyle("cell_s", fontName=F, fontSize=7, leading=8.8, textColor=INK),
    "cellb_s": ParagraphStyle("cellb_s", fontName=FB, fontSize=7, leading=8.8, textColor=colors.white),
    "li": ParagraphStyle("li", fontName=F, fontSize=9.6, leading=13.6, textColor=INK, spaceAfter=3),
}

EMOJI = re.compile("[\U00010000-\U0010ffff\u2600-\u27bf\ufe0f\u200d]")


def inline(text):
    text = EMOJI.sub("", text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    # never emit dash punctuation
    text = text.replace("\u2014", ", ").replace("\u2013", "-")
    return text.strip()


# ----------------------------------------------------------------------------
# custom flowables
# ----------------------------------------------------------------------------
class FmmiBars(Flowable):
    def __init__(self, items, width):
        super().__init__()
        self.items, self.width, self.height = items, width, 22 * len(items) + 6

    def draw(self):
        c = self.canv
        label_w, val_w = 118, 32
        bar_x, bar_w = label_w, self.width - label_w - val_w
        y = self.height - 20
        for name, score in self.items:
            c.setFont(FB, 8)
            c.setFillColor(INK)
            c.drawString(0, y + 3, name)
            c.setFillColor(TRACK)
            c.roundRect(bar_x, y, bar_w, 12, 6, stroke=0, fill=1)
            c.setFillColor(TEAL)
            c.roundRect(bar_x, y, max(12, bar_w * score / 100.0), 12, 6, stroke=0, fill=1)
            c.setFillColor(INK)
            c.setFont(FB, 9)
            c.drawRightString(self.width, y + 2, str(score))
            y -= 22


class BarChart(Flowable):
    def __init__(self, cfg, width, height=150):
        super().__init__()
        self.cfg, self.width, self.height = cfg, width, height

    def draw(self):
        c, cfg = self.canv, self.cfg
        c.setFillColor(INK)
        c.setFont(FB, 8.5)
        c.drawString(0, self.height - 10, cfg["title"])
        vals, labels = cfg["values"], cfg["labels"]
        top, bottom = self.height - 28, 22
        vmax = max(vals) * 1.18
        n = len(vals)
        slot = self.width / n
        bw = slot * 0.56
        for i, (v, lab) in enumerate(zip(vals, labels)):
            h = (top - bottom) * v / vmax
            x = i * slot + (slot - bw) / 2
            last = i == n - 1
            c.setFillColor(RED if last else TEAL)
            c.rect(x, bottom, bw, h, stroke=0, fill=1)
            c.setFillColor(INK)
            c.setFont(FB, 9)
            c.drawCentredString(x + bw / 2, bottom + h + 3, f"{v}")
            c.setFont(F, 6.8)
            c.setFillColor(GRAY)
            c.drawCentredString(x + bw / 2, bottom - 11, lab)
        c.setStrokeColor(RULE)
        c.line(0, bottom, self.width, bottom)


class LineChart(Flowable):
    def __init__(self, cfg, width, height=150):
        super().__init__()
        self.cfg, self.width, self.height = cfg, width, height

    def draw(self):
        c, cfg = self.canv, self.cfg
        c.setFillColor(INK)
        c.setFont(FB, 8.5)
        c.drawString(0, self.height - 10, cfg["title"])
        vals, labels = cfg["values"], cfg["labels"]
        top, bottom = self.height - 34, 24
        lo, hi = min(vals) - 0.05, max(vals) + 0.06
        n = len(vals)
        pad = 16
        xs = [pad + i * (self.width - 2 * pad) / (n - 1) for i in range(n)]
        ys = [bottom + (top - bottom) * (v - lo) / (hi - lo) for v in vals]
        c.setStrokeColor(RULE)
        c.line(0, bottom, self.width, bottom)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.8)
        for i in range(n - 1):
            c.line(xs[i], ys[i], xs[i + 1], ys[i + 1])
        for i, (x, y, v, lab) in enumerate(zip(xs, ys, vals, labels)):
            last = i == n - 1
            c.setFillColor(RED if last else TEAL)
            c.circle(x, y, 3.4 if last else 2.6, stroke=0, fill=1)
            c.setFillColor(INK)
            c.setFont(FB if last else F, 8 if last else 7)
            c.drawCentredString(x, y + 6, f"{v:.2f}%")
            c.setFont(F, 6.8)
            c.setFillColor(GRAY)
            c.drawCentredString(x, bottom - 11, lab)
        c.setLineWidth(1)


# ----------------------------------------------------------------------------
# blocks
# ----------------------------------------------------------------------------
def banner(width):
    inner = [
        [Paragraph('<font color="#C9A96A"><b>THE FRIEDMAN REPORT</b></font>',
                   ParagraphStyle("k", fontName=FB, fontSize=8.5, leading=11))],
        [Paragraph(WEEK["headline"], ParagraphStyle("t", fontName=FB, fontSize=25, leading=29, textColor=colors.white))],
        [Paragraph(f"<i>{WEEK['sub']}</i>", ParagraphStyle("s", fontName=FI, fontSize=10.5, leading=14, textColor=colors.white))],
        [Paragraph(WEEK["byline"], ParagraphStyle("b", fontName=F, fontSize=8, leading=11, textColor=colors.white))],
    ]
    t = Table(inner, colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (0, 0), 14), ("BOTTOMPADDING", (0, -1), (-1, -1), 12),
        ("LINEBELOW", (0, -1), (-1, -1), 3, GOLD),
    ]))
    return t


def tiles(width):
    tone = {"good": TEAL, "bad": RED, "flat": GRAY}
    cells = []
    for label, value, delta, t in WEEK["tiles"]:
        cells.append([
            Paragraph(label, ParagraphStyle("tl", fontName=FB, fontSize=6.6, leading=8.4, textColor=GRAY, alignment=1)),
            Paragraph(value, ParagraphStyle("tv", fontName=FB, fontSize=15, leading=18, textColor=INK, alignment=1)),
            Paragraph(delta, ParagraphStyle("td", fontName=FB, fontSize=7.4, leading=9, textColor=tone[t], alignment=1)),
        ])
    rows = [cells[0:4], cells[4:8]]
    cw = width / 4.0
    t = Table(rows, colWidths=[cw] * 4, rowHeights=[62, 62])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("BOX", (0, 0), (-1, -1), 0.8, GOLD), ("INNERGRID", (0, 0), (-1, -1), 0.8, GOLD),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


def md_table(lines, width):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    header, body = rows[0], rows[2:]
    ncol = len(header)
    small = ncol >= 7
    hs, cs = (ST["cellb_s"], ST["cell_s"]) if small else (ST["cellb"], ST["cell"])
    data = [[Paragraph(inline(c), hs) for c in header]]
    for r in body:
        r = (r + [""] * ncol)[:ncol]
        data.append([Paragraph(inline(c), cs) for c in r])
    if ncol == 2:
        cw = [width * 0.38, width * 0.62]
    elif ncol == 3 and not small:
        cw = [width * 0.36, width * 0.32, width * 0.32]
    elif ncol == 4:
        cw = [width * 0.28, width * 0.24, width * 0.24, width * 0.24]
        if "Metric" in header[0]:
            cw = [width * 0.30, width * 0.22, width * 0.22, width * 0.26]
    else:
        first = width * (0.15 if small else 0.22)
        cw = [first] + [(width - first) / (ncol - 1)] * (ncol - 1)
    t = Table(data, colWidths=cw, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE),
    ]
    for i in range(2, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), CARD))
    t.setStyle(TableStyle(style))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(F, 7.5)
    canvas.setFillColor(GRAY)
    canvas.drawString(0.75 * inch, 0.5 * inch, f"The Friedman Report  |  {WEEK['label']}")
    canvas.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build():
    width = letter[0] - 1.5 * inch
    text = open(MD_PATH, encoding="utf-8").read().splitlines()
    story = [banner(width), Spacer(1, 8), Paragraph(inline(WEEK["intro"]), ST["note"])]

    i, section, pending_charts, skip_table = 0, "", [], False

    def flush_charts():
        nonlocal pending_charts
        if not pending_charts:
            return
        half = (width - 14) / 2.0
        objs = []
        for key in pending_charts:
            cfg = WEEK["charts"][key]
            objs.append(BarChart(cfg, half - 6) if key == "days" else LineChart(cfg, half - 6))
        if len(objs) == 1:
            story.append(objs[0])
        else:
            t = Table([objs], colWidths=[half + 7] * 2)
            t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
            story.append(t)
        story.append(Spacer(1, 8))
        pending_charts = []

    # skip everything before the first ## heading (title block is the banner)
    while i < len(text) and not text[i].startswith("## "):
        i += 1

    while i < len(text):
        ln = text[i]
        s = ln.strip()

        if not s:
            i += 1
            continue

        m = re.match(r"<!--\s*CHART:(\w+)\s*-->", s)
        if m:
            pending_charts.append(m.group(1))
            i += 1
            continue
        if pending_charts:
            flush_charts()

        if s == "<!-- TILES -->":
            story.append(tiles(width))
            story.append(Spacer(1, 4))
            skip_table = True
            i += 1
            continue
        if s == "<!-- FMMI -->":
            story.append(FmmiBars(WEEK["fmmi"], width))
            story.append(Spacer(1, 6))
            i += 1
            continue
        if s.startswith("<!--"):
            i += 1
            continue

        if s.startswith("## "):
            section = s[3:].strip()
            story.append(Paragraph(inline(section), ST["h2"]))
            i += 1
            continue
        if s.startswith("### "):
            story.append(Paragraph(inline(s[4:]), ST["h3"]))
            i += 1
            continue
        if s == "---":
            story.append(PageBreak())
            i += 1
            continue

        if s.startswith("|"):
            block = []
            while i < len(text) and text[i].strip().startswith("|"):
                block.append(text[i])
                i += 1
            if skip_table:
                skip_table = False
                continue
            story.append(md_table(block, width))
            story.append(Spacer(1, 7))
            continue

        if re.match(r"^(-|\d+\.)\s+", s):
            numbered = bool(re.match(r"^\d+\.", s))
            items = []
            while i < len(text) and re.match(r"^\s*(-|\d+\.)\s+", text[i]):
                cur = re.sub(r"^\s*(-|\d+\.)\s+", "", text[i])
                i += 1
                while i < len(text) and text[i].startswith("  ") and text[i].strip():
                    cur += " " + text[i].strip()
                    i += 1
                items.append(ListItem(Paragraph(inline(cur), ST["li"]), leftIndent=14))
            story.append(ListFlowable(items, bulletType="1" if numbered else "bullet",
                                      bulletFontName=FB, bulletFontSize=8, leftIndent=14,
                                      bulletColor=TEAL, start=1 if numbered else "\u2022"))
            story.append(Spacer(1, 4))
            continue

        # paragraph: gather until blank line / structural line
        para = []
        while i < len(text):
            t = text[i]
            ts = t.strip()
            if (not ts or ts.startswith(("#", "|", "<!--", "---")) or re.match(r"^(-|\d+\.)\s+", ts)):
                break
            para.append(ts)
            i += 1
        keep_breaks = section == "Let's Talk" and not para[0].startswith("Ready to get started")
        body = "<br/>".join(inline(p) for p in para) if keep_breaks else inline(" ".join(para))
        whole_italic = (" ".join(para).startswith("*") and " ".join(para).endswith("*")
                        and not " ".join(para).startswith("**"))
        story.append(Paragraph(body, ST["note"] if whole_italic else ST["body"]))

    flush_charts()
    doc = SimpleDocTemplate(PDF_PATH, pagesize=letter, leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                            topMargin=0.7 * inch, bottomMargin=0.8 * inch,
                            title=f"The Friedman Report, {WEEK['label']}", author="Kyle Friedman, The Friedman Team")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("wrote", PDF_PATH, os.path.getsize(PDF_PATH) // 1024, "KB")


if __name__ == "__main__":
    build()
