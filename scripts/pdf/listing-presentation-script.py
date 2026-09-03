# -*- coding: utf-8 -*-
"""Branded printable script - the question-led Listing Presentation.
Source: projects/listing-scripts.md Part 3.
Run: C:\\Users\\kylej\\AppData\\Local\\Python\\bin\\python.exe
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\projects\Listing-Presentation-Script.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"
TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, textColor=TEAL, leading=18),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9, textColor=GREY, leading=12),
 "step":ParagraphStyle("step", fontName="Helvetica-Bold", fontSize=10.5, textColor=TEAL, leading=13, spaceBefore=2),
 "deck":ParagraphStyle("deck", fontName="Helvetica-Oblique", fontSize=7.6, textColor=GOLD, leading=10),
 "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.2, textColor=INK, leading=9.5),
 "say": ParagraphStyle("say", fontName="Helvetica", fontSize=9.2, textColor=INK, leading=13),
 "lis": ParagraphStyle("lis", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY, leading=10.5),
 "brdg":ParagraphStyle("brdg", fontName="Helvetica", fontSize=8.6, textColor=TEAL, leading=11.5),
 "cell":ParagraphStyle("cell", fontName="Helvetica", fontSize=8, textColor=INK, leading=10),
 "cellb":ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=8, textColor=colors.white, leading=10),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.4, textColor=TEAL, leading=10, alignment=1),
}

def box(txt, bg, bar):
    t = Table([[Paragraph(txt, S["say"])]], colWidths=[7.2*inch])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("LINEBEFORE",(0,0),(0,-1),3,bar),
        ("BOX",(0,0),(-1,-1),0.4,LINE),
        ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
    return t

def section(num, title, deck, ask=None, listen=None, present=None, bridge=None):
    els = [Paragraph("%s &nbsp; %s" % (num, title), S["step"])]
    if deck: els += [Paragraph("Deck: " + deck, S["deck"])]
    els += [Spacer(1,4)]
    if ask:
        els += [Paragraph("YOU ASK", S["lbl"]), Spacer(1,2), box(ask, CREAM, GOLD), Spacer(1,4)]
    if listen:
        els += [Paragraph("Listen for: " + listen, S["lis"]), Spacer(1,4)]
    if present:
        els += [Paragraph("THEN PRESENT (while showing the slide)", S["lbl"]), Spacer(1,2),
                box(present, colors.HexColor("#EFEBE2"), TEAL), Spacer(1,4)]
    if bridge:
        els += [Paragraph("Bridge &rarr;&nbsp; " + bridge, S["brdg"])]
    els += [Spacer(1,9)]
    return KeepTogether(els)

story = []
iw, ih = 2000, 373
story += [Table([[Image(LOGO, width=1.5*inch, height=1.5*inch*ih/iw),
    Paragraph("THE FRIEDMAN TEAM", ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9,
        textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
    colWidths=[3.7*inch, 3.5*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)])),
    Spacer(1,3), HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceAfter=8),
    Paragraph("The Listing Presentation", S["h1"]),
    Paragraph("Question-led. Never present a section cold. Ask, they answer, you show that "
    "section and tie it to what they said, then the next question opens the next section. The deck "
    "is your visual aid, not your script.", S["sub"]),
    Spacer(1,9)]

story += [section("0.", "Set the frame", "no deck",
    ask="&ldquo;Before I show you anything, this isn&rsquo;t a canned pitch. I&rsquo;m going to ask "
        "you some things, and every time you answer, I&rsquo;ll show you exactly how we handle it. "
        "By the end you&rsquo;ll know your number, the plan, and whether I&rsquo;m the right person. "
        "Sound good? ... Cool. First one.&rdquo;")]

story += [section("1.", "Why selling", "Your Home",
    ask="&ldquo;Walk me through why you&rsquo;re selling, and what the win looks like. Where are you "
        "going, and by when?&rdquo;",
    listen="real motivation, destination, timeline, what matters most (price / speed / a clean move).",
    present="&ldquo;Here&rsquo;s your home on paper. This is what a buyer&rsquo;s agent, and Zillow, "
        "price off of, and none of them have seen inside. That gap between the data and the real "
        "house is the first place we make you money.&rdquo;",
    bridge="&ldquo;So the question is what it&rsquo;s actually worth. Want to see what&rsquo;s really "
        "happening in your market?&rdquo;")]

story += [section("2.", "The market", "The Market Within 2 Miles + The Market",
    ask="&ldquo;What have you seen selling around here, anything catch your eye, good or bad?&rdquo;",
    present="&ldquo;Every sale within two miles the last few months, and the trend. The ones priced "
        "right were gone in [X] days. The ones that chased the market down sat for [Y] and sold for "
        "less.&rdquo;",
    bridge="&ldquo;So how do we make sure yours is the one that&rsquo;s gone in days, not the one "
        "that sits? That&rsquo;s pricing.&rdquo;")]

story += [section("3.", "Pricing", "Pricing Your Property (the decay chart)",
    ask="&ldquo;If you had to guess, when does a listing get the most attention: week one, week "
        "four, or week eight?&rdquo; &nbsp;<font color='#5B6B6E'>(Most say later. They&rsquo;re wrong. Good.)</font>",
    present="&ldquo;Week one. 7 days is peak attention. After that buyer activity drops, and "
        "perceived value drops with it. Homes that sit 24-plus weeks sell about 9% under market. So "
        "we don&rsquo;t price to test the ceiling and walk it down. We price to hit that first week "
        "hard and create competition.&rdquo;",
    bridge="&ldquo;That only works if enough buyers see it in week one. How do you think most buyers "
        "are going to find your house?&rdquo;")]

story += [section("4.", "Marketing", "Your Marketing Strategy (steps 1&ndash;10)",
    listen="they&rsquo;ll answer &ldquo;Zillow?&rdquo; / &ldquo;the sign?&rdquo;",
    present="&ldquo;Some of them. Here&rsquo;s the whole machine, ten steps. The part most agents "
        "skip is Coming Soon, we build a buyer pipeline before it&rsquo;s even live, so day one "
        "there&rsquo;s already demand. Then photography, the property site, brokers open, and a paid "
        "digital campaign, plus me personally on the phone to agents and neighbors.&rdquo;",
    bridge="&ldquo;And that reach isn&rsquo;t a guess. Want to see the actual numbers?&rdquo;")]

story += [section("5.", "Reach", "Social Media Online Reach + We Never Miss Buyer Calls",
    present="&ldquo;Last listing: 82,000 views, 37,000 people, 30 days. It takes about 12 touches for "
        "a buyer to decide, so we hit them across platforms, repeatedly. And every inquiry, the QR "
        "code, the 800 number, a 2am text, gets captured and followed up. Nothing leaks.&rdquo;",
    bridge="&ldquo;So that&rsquo;s the marketing. Who actually does all this while you&rsquo;re "
        "living your life?&rdquo;")]

story += [section("6.", "The team", "Your Team + Home Prep Advisor + Transaction Coordinator + Your Path to Success",
    ask="&ldquo;Have you sold a home before? ... What was the most stressful part?&rdquo;",
    listen="coordination, communication, the paperwork (usually).",
    present="&ldquo;That&rsquo;s exactly why it&rsquo;s not just me. I run strategy and negotiation. "
        "A Home Prep Advisor gets it show-ready, what to fix, what to skip, staging. A Transaction "
        "Coordinator owns every deadline and document from contract to keys, so nothing falls "
        "through. This slide is the whole track, start to finish.&rdquo;",
    bridge="&ldquo;Plan&rsquo;s solid, team&rsquo;s solid. Does all this actually get a different "
        "result?&rdquo;")]

story += [section("7.", "The proof", "Faster Sale + More Money + testimonials + About Kyle",
    present="&ldquo;It does. My listings sell at 101.6% of list versus 100.1% for the average agent, "
        "on a home like yours that&rsquo;s real money in your pocket. 7 days on market versus 16. And "
        "here&rsquo;s what that&rsquo;s like to go through, from people who did it.&rdquo;",
    bridge="&ldquo;Last thing before we talk number. What&rsquo;s your biggest worry about listing? "
        "Be honest.&rdquo;")]

story += [section("8.", "Peace of mind", "Communication Guarantee + Easy Exit Listing Agreement",
    listen="getting stuck with the wrong agent, being left in the dark (usually).",
    present="&ldquo;Both of those are covered in writing. Feedback in 48 hours, a call every week, "
        "I&rsquo;m reachable 1 to 5 every day. And if I&rsquo;m not doing what I said, you fire me. "
        "No lengthy contract, no fight. You&rsquo;re never stuck.&rdquo;",
    bridge="into the close.")]

story += [HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceBefore=2, spaceAfter=7),
    Paragraph("THE CLOSE", ParagraphStyle("o", fontName="Helvetica-Bold", fontSize=10, textColor=TEAL, leading=13)),
    Spacer(1,4),
    box("&ldquo;So, that&rsquo;s how we sell homes for the highest price in the shortest time. You "
        "do want to sell your home, right?&rdquo; &nbsp;<b>&mdash; Yes.</b><br/>"
        "&ldquo;And have I shown you that I&rsquo;m the best person to sell it, with the track record "
        "and the strategy?&rdquo; &nbsp;<b>&mdash; Yes.</b><br/>"
        "&ldquo;Perfect. Next step is the listing paperwork. We get it into the MLS as Coming Soon "
        "and start building a pipeline of buyers before it even hits the market. Let&rsquo;s fill it "
        "out.&rdquo;<br/>"
        "<font color='#5B6B6E'>&rarr; into paperwork; start filling it in, narrate, go quiet.</font>",
        CREAM, GOLD),
    Spacer(1,5),
    Paragraph("If either answer isn&rsquo;t a clean yes: &ldquo;What&rsquo;s the piece that&rsquo;s "
        "not quite there, the price, the plan, the commission, or me?&rdquo; Handle that one thing, "
        "then re-ask the two questions.", S["lis"]),
    Spacer(1,10),
    HRFlowable(width="100%", thickness=0.8, color=LINE, spaceAfter=6),
    Paragraph("THE SPINE (memorize this)", ParagraphStyle("o2", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12)),
    Spacer(1,3)]

rows = [[Paragraph("<font color='white'><b>#</b></font>", S["cellb"]),
         Paragraph("<font color='white'><b>You ask</b></font>", S["cellb"]),
         Paragraph("<font color='white'><b>Then present</b></font>", S["cellb"])]]
for n,q,p in [
 ("1","Why selling / where to / by when?","Your Home"),
 ("2","What have you seen selling nearby?","The Market"),
 ("3","When does a listing get the most attention?","Pricing decay chart"),
 ("4","How will buyers find it?","Marketing (10 steps)"),
 ("5","(show reach numbers)","Social reach + buyer capture"),
 ("6","Sold before? Most stressful part?","Team + Path + roles"),
 ("7","(show it gets a different result)","Stats + testimonials + About Kyle"),
 ("8","Biggest worry about listing?","Guarantees + Easy Exit"),
 ("9","The close","Listing paperwork"),
]:
    rows.append([Paragraph(n,S["cell"]), Paragraph(q,S["cell"]), Paragraph(p,S["cell"])])
tt = Table(rows, colWidths=[0.35*inch, 3.85*inch, 3.0*inch])
tt.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),TEAL),("BOX",(0,0),(-1,-1),0.5,LINE),
    ("INNERGRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#F7F4EE")]),
    ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
    ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6)]))
story += [tt, Spacer(1,10),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=4),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com", S["foot"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.45*inch, bottomMargin=0.5*inch, title="Listing Presentation Script - The Friedman Team",
    author="Kyle Friedman").build(story)
print("wrote", OUT)
