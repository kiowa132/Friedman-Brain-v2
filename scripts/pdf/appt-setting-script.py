# -*- coding: utf-8 -*-
"""Branded one-page-ish Appointment-Setting Call Script - The Friedman Team.
Source: projects/listing-scripts.md (the single-flow version).
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\projects\Appointment-Setting-Script.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, textColor=TEAL, leading=18),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9, textColor=GREY, leading=12),
 "step":ParagraphStyle("step", fontName="Helvetica-Bold", fontSize=10.5, textColor=TEAL, leading=13, spaceBefore=2),
 "say": ParagraphStyle("say", fontName="Helvetica", fontSize=9.2, textColor=INK, leading=13),
 "lis": ParagraphStyle("lis", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY, leading=10.5),
 "obh": ParagraphStyle("obh", fontName="Helvetica-Bold", fontSize=8.4, textColor=INK, leading=11),
 "obb": ParagraphStyle("obb", fontName="Helvetica", fontSize=8.4, textColor=INK, leading=11),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.6, textColor=TEAL, leading=10, alignment=1),
}

def say_box(text):
    t = Table([[Paragraph(text, S["say"])]], colWidths=[7.2*inch])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),CREAM),("BOX",(0,0),(-1,-1),0.5,GOLD),
        ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
    return t

def step(n, title, say, listen=None):
    els = [Paragraph("%s &nbsp; %s" % (n, title), S["step"]), Spacer(1,3), say_box(say)]
    if listen:
        els += [Spacer(1,2), Paragraph("Listen for: " + listen, S["lis"])]
    els += [Spacer(1,7)]
    return KeepTogether(els)

story = []
iw, ih = 2000, 373
story += [Table([[Image(LOGO, width=1.5*inch, height=1.5*inch*ih/iw),
    Paragraph("THE FRIEDMAN TEAM", ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9,
        textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
    colWidths=[3.7*inch, 3.5*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)])),
    Spacer(1,3), HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceAfter=8),
    Paragraph("Appointment-Setting Call", S["h1"]),
    Paragraph("One flow, top to bottom. You are interviewing them. Ask more than you tell. "
    "The call's only job is to book the 30-minute meeting.", S["sub"]),
    Spacer(1,9)]

story += [
 step("1", "INTRO",
   "&ldquo;Hey [Name], how you doing today? ... This is Kyle Friedman with The Friedman Team. We "
   "[spoke the other day / you reached out] about possibly selling [address]. Did I catch you at a "
   "good time?&rdquo;"),
 step("2", "RAPPORT",
   "Looks like / sounds like / feels like. Talk about your day, listen to the background. Then: "
   "&ldquo;How long have you owned the place? ... How long have you been in the area?&rdquo;",
   "Are they a small-talker? What's the real reason this is coming up?"),
 step("3", "CONDITION",
   "&ldquo;Walk me through the house. How old&rsquo;s the roof? ... Anything major done to the "
   "kitchen or baths? ... How old&rsquo;s the HVAC? ... So it&rsquo;s pretty much original, or "
   "you&rsquo;ve kept it up?&rdquo; &nbsp; &ldquo;You living there now, is it vacant, or do you "
   "have tenants?&rdquo;"),
 step("4", "SELLING PROCESS + MOTIVATION",
   "&ldquo;How far along are you in this? Talked to any other agents, or am I the first? ... "
   "What&rsquo;s got you thinking about selling? ... Why now? ... Where are you headed, and when do "
   "you want to be there?&rdquo;",
   "Real deadline or &lsquo;someday&rsquo;? For-sure seller or still deciding?"),
 step("5", "MORTGAGE",
   "&ldquo;Do you still have a mortgage on it? ... Rough idea of the balance?&rdquo; &nbsp; React: "
   "&ldquo;Okay, sounds like you&rsquo;ve got good equity&rdquo; OR &ldquo;no problem, that&rsquo;s "
   "normal.&rdquo;"),
 step("6", "THEIR NUMBER",
   "&ldquo;If you don&rsquo;t mind me asking, what number do you have in your head for it? ... And "
   "where&rsquo;d that come from, Zillow, a neighbor, an agent?&rdquo; &nbsp; Then: &ldquo;Listen, "
   "I&rsquo;m sure if I told you it was worth a million you&rsquo;d be thrilled, and if I said a "
   "hundred grand you&rsquo;d hang up. I just want to know if we&rsquo;re in the same ballpark so "
   "I&rsquo;m not wasting your time or mine.&rdquo;",
   "Coachable, or married to a fantasy number?"),
 step("7", "ANCHOR + BOOK",
   "&ldquo;Here&rsquo;s where I&rsquo;m at. We just [sold / listed] one down the street for [$X] and "
   "another for [$Y]. From what you&rsquo;ve told me you&rsquo;re probably in that range, maybe a "
   "little more with the updates. The only way I give you a real number instead of a guess is to "
   "see it. That&rsquo;s 30 minutes, I look at it and show you exactly how I&rsquo;d price and "
   "market it to get you [their goal] by [their date]. Does tomorrow at 5 or Thursday at 3 work "
   "better?&rdquo;"),
 step("8", "ONE COMMITMENT NUDGE",
   "&ldquo;And real quick, if the plan and the number make sense when we sit down, are you ready to "
   "get it going, or are you still deciding whether to sell at all?&rdquo;"),
 step("9", "CONFIRM",
   "Who else needs to be there. Time, address, about 30 minutes. &ldquo;I&rsquo;ll text you a "
   "confirmation.&rdquo;"),
]

story += [HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceBefore=2, spaceAfter=7),
    Paragraph("OBJECTIONS", ParagraphStyle("o", fontName="Helvetica-Bold", fontSize=10, textColor=TEAL, leading=13)),
    Spacer(1,4)]

for h, b in [
 ("&ldquo;Zillow / the tax assessment says X&rdquo;",
  "We used to lean on those, but they over- and under-value all the time. The only accurate way is "
  "similar homes that actually sold near you. That&rsquo;s what I&rsquo;ll bring."),
 ("&ldquo;My friend&rsquo;s a realtor / another agent said higher&rdquo;",
  "That happens a lot. Some agents give you a high number to win the listing, then spend three "
  "months walking you back down while the house sits. I&rsquo;ll give you what the market will "
  "actually pay. If I&rsquo;m low, we adjust up, that&rsquo;s the good problem."),
 ("&ldquo;I want to think about it&rdquo;",
  "What specifically, me, the timing, or the price?"),
 ("&ldquo;I want to talk to my spouse&rdquo;",
  "No problem, you know them better than I do. What do you think they&rsquo;ll say? ... Let&rsquo;s "
  "just get all of us in the room when we meet so I&rsquo;m not answering through you."),
 ("&ldquo;Just send me something&rdquo;",
  "I can send a range, but it&rsquo;ll be off by 20 or 30 grand without seeing inside. 20 minutes "
  "in person and you get a real number and your net sheet."),
]:
    story += [Table([[Paragraph(h, S["obh"])],[Paragraph(b, S["obb"])]], colWidths=[7.2*inch],
        style=TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,0),1),("BOTTOMPADDING",(0,1),(-1,1),5)])),
    ]

story += [Spacer(1,4), HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
    Paragraph("The pass (when the answers are soft): &ldquo;Honestly, I don&rsquo;t think you&rsquo;re "
    "quite ready to list, and I&rsquo;d be doing you a disservice pretending you are. I&rsquo;ll send "
    "you the sold data for your street. When you&rsquo;ve got a real timeline, call me.&rdquo;",
    ParagraphStyle("p", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY, leading=10.5)),
    Spacer(1,5),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; "
    "kyle@friedmanreteam.com", S["foot"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.45*inch, bottomMargin=0.5*inch, title="Appointment-Setting Script - The Friedman Team",
    author="Kyle Friedman").build(story)
print("wrote", OUT)
