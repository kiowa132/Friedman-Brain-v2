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
    Paragraph("One flow, top to bottom. Every step is the same rhythm: ask, say one thing back, "
    "then a question that opens the next step. You are interviewing them. The call's only job is "
    "to book the 30-minute meeting.", S["sub"]),
    Spacer(1,9)]

story += [
 step("1", "OPEN + FRAME",
   "<b>Ask.</b> &ldquo;Hey [Name], Kyle Friedman with The Friedman Team. We [spoke the other day / "
   "you reached out] about [address]. Catch you at an okay time?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;Before I put real time into your place, I want to make sure we&rsquo;re a "
   "fit, so I&rsquo;m going to ask you a handful of questions first. Fair?&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;How long have you owned it, and how long have you been in the area?&rdquo;"),
 step("2", "THE WHY",
   "<b>Ask.</b> &ldquo;What&rsquo;s got you thinking about selling? ... Why now, and not six months "
   "ago or six months from now?&rdquo;<br/>"
   "<b>Then.</b> Mirror it back in one line. &ldquo;Makes sense.&rdquo; Let the silence sit.<br/>"
   "<b>Lead in.</b> &ldquo;Where are you headed next, and when do you want to be there?&rdquo;",
   "The real reason this is coming up. For-sure seller, or testing the water."),
 step("3", "TIMELINE",
   "<b>Ask.</b> &ldquo;Is that a hard date or a nice-to-have? ... Have you bought anywhere yet, or "
   "signed a lease? ... What happens if it&rsquo;s not sold by then?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;Okay, so there&rsquo;s a real clock on this.&rdquo; If it&rsquo;s all soft, "
   "note it and head for the pass.<br/>"
   "<b>Lead in.</b> &ldquo;Who else is part of this decision besides you?&rdquo;",
   "A real deadline, or &lsquo;someday&rsquo;."),
 step("4", "DECISION + AGENT SHOPPING",
   "<b>Ask.</b> &ldquo;Is everyone equally on board, or is one of you more into it? ... Am I the "
   "first agent you&rsquo;re talking to, or have there been others? ... How are you deciding "
   "between agents?&rdquo;<br/>"
   "<b>Then.</b> If the answer is &lsquo;whoever gives the highest number&rsquo;: &ldquo;Just so you "
   "know, that is how sellers end up overpriced and sitting. The highest number and the best agent "
   "are usually not the same person.&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;Walk me through the house.&rdquo;",
   "For-sure seller, or still talking each other into it."),
 step("5", "CONDITION",
   "<b>Ask.</b> &ldquo;How old&rsquo;s the roof? ... Kitchen or baths done, and when? ... HVAC? ... "
   "Pretty much original, or you&rsquo;ve kept it up? ... Living there now, vacant, or tenants?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;Good. The condition tells me which comps to use and how much prep it needs "
   "before photos.&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;Has it been on the market before, with an agent or on your own?&rdquo;",
   "If yes, go to 5A. If no, skip to 6."),
 step("5A", "IF IT WAS LISTED BEFORE",
   "<b>Ask.</b> &ldquo;Walk me through that. What do you think went wrong? ... What did the last "
   "agent do, and not do? ... What was the plan when it went up?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;Here is what I will tell you. When a good house does not sell, it is almost "
   "never the house. It is the price or the marketing. Usually it launched wrong, chased the market "
   "down with cut after cut, or it never got in front of the right buyers.&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;If you knew it would actually sell this time, would you put it back on?&rdquo;",
   "Blames themselves, or ready for a real plan."),
 step("6", "MORTGAGE + EQUITY",
   "<b>Ask.</b> &ldquo;Do you still have a mortgage on it? ... Rough idea of the balance?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;Okay, sounds like solid equity,&rdquo; or &ldquo;no problem, that is "
   "normal.&rdquo; Either way: &ldquo;I&rsquo;ll build you a net sheet so you see your actual "
   "walk-away number.&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;What number do you have in your head for the place?&rdquo;"),
 step("7", "THEIR NUMBER",
   "<b>Ask.</b> &ldquo;Where&rsquo;d that come from, Zillow, a neighbor, an agent? ... If the sold "
   "data came back under that, are you still selling, or does that kill it?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;I&rsquo;m not going to tell you a million to make you happy or a hundred "
   "grand to scare you off. I just want to know if we&rsquo;re in the same ballpark. From what "
   "you&rsquo;ve told me, and what&rsquo;s sold near you, you&rsquo;re probably in [range], maybe a "
   "little more with the updates.&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;The only way I give you a real number instead of a guess is to see it. "
   "That&rsquo;s about 30 minutes. Does [day] at [time] or [day] at [time] work better?&rdquo;",
   "Coachable, or married to a fantasy number."),
 step("8", "BOOK + WHAT THE MEETING IS",
   "<b>Then.</b> &ldquo;When we sit down I bring the sold comps, your net sheet, and the exact "
   "plan. How I&rsquo;d price it and hold that price, and the marketing that gets you [their goal] "
   "by [their date]. I&rsquo;ll walk you through the whole roadmap, step by step.&rdquo;<br/>"
   "<b>One line to plant.</b> &ldquo;Most of your buyer traffic hits in the first week, so nothing "
   "goes live until every piece is ready. Photos, floor plan, 3D tour, Zillow Showcase, and the "
   "launch timed to the weekend buyers actually shop.&rdquo;<br/>"
   "<b>Lead in.</b> &ldquo;If the plan and the number make sense when we sit down, are you ready to "
   "fill out the listing paperwork and get it moving, or are you still deciding whether to sell at "
   "all?&rdquo;"),
 step("9", "CONFIRM",
   "<b>Ask.</b> &ldquo;Who else needs to be there? ... Best address and cell for you?&rdquo;<br/>"
   "<b>Then.</b> &ldquo;It&rsquo;s about 30 minutes. I&rsquo;ll text you a confirmation with a few "
   "things to look at first.&rdquo;<br/>"
   "<b>Close.</b> &ldquo;Talk [day].&rdquo;"),
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
  "months walking you back down with cut after cut while the house sits. I price it once, at what "
  "the market will actually pay, and we hold it. If I&rsquo;m low, we adjust up, that&rsquo;s the "
  "good problem."),
 ("&ldquo;Is now even a good time to sell?&rdquo;",
  "The buyers out right now are the serious ones, pre-approved and ready to move. A well-run "
  "listing in this market goes under contract in about three weeks. Timing isn&rsquo;t the "
  "problem, the plan is, and that&rsquo;s what I&rsquo;ll show you."),
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
