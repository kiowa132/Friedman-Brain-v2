# -*- coding: utf-8 -*-
"""Branded Listing Presentation PDF - 7721 Wilson Ave, Parkville MD 21234
(Nicole "Nikki" Fern). Copied from listing-presentation-1705-havre-de-grace.py.

Angle: renovated, vacant Cape Cod listed with the wrong ABOVE-GRADE square
footage (~1,287 vs the ~1,700 every other source shows), a fumbled launch
(AI staging bolted on late), and two fast price cuts, then withdrawn.
This deck gives her an honest read and a full relaunch plan.
6 pages, each filled. No em dashes (client rule).
Kyle uses Zillow Showcase interactive virtual staging, NOT physical staging.
Run: py scripts/pdf/listing-presentation-7721-wilson.py
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, HRFlowable, PageBreak)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import datetime

OUT = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\listings\7721-wilson-ave\7721-Wilson-Listing-Presentation.pdf"
LOGO = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\brand-assets\logo.png"

TEAL, GOLD, CREAM, INK, GREY, LINE = (
    colors.HexColor("#0F5C63"), colors.HexColor("#C9A96A"), colors.HexColor("#FAF8F5"),
    colors.HexColor("#0D2226"), colors.HexColor("#5B6B6E"), colors.HexColor("#D9D2C4"))

S = {
 "h1":  ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=16, textColor=TEAL, leading=19),
 "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13),
 "lbl": ParagraphStyle("lbl", fontName="Helvetica-Bold", fontSize=7.5, textColor=GOLD, leading=10, spaceAfter=1),
 "val": ParagraphStyle("val", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=12),
 "sec": ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=12.5, textColor=TEAL, leading=15.5, spaceBefore=4, spaceAfter=4),
 "sub2":ParagraphStyle("sub2", fontName="Helvetica-Bold", fontSize=9.7, textColor=INK, leading=12.5, spaceBefore=5, spaceAfter=1),
 "body":ParagraphStyle("body", fontName="Helvetica", fontSize=9.1, textColor=INK, leading=13.2),
 "cap": ParagraphStyle("cap", fontName="Helvetica-Oblique", fontSize=7.5, textColor=GREY, leading=9.8, alignment=TA_CENTER),
 "cell":ParagraphStyle("cell", fontName="Helvetica", fontSize=8.4, textColor=INK, leading=10.8),
 "cellR":ParagraphStyle("cellR", fontName="Helvetica", fontSize=8.4, textColor=INK, leading=10.8, alignment=TA_RIGHT),
 "foot":ParagraphStyle("foot", fontName="Helvetica", fontSize=7.8, textColor=TEAL, leading=10.5, alignment=TA_CENTER),
 "disc":ParagraphStyle("disc", fontName="Helvetica-Oblique", fontSize=7, textColor=GREY, leading=9, alignment=TA_CENTER),
 "boxb":ParagraphStyle("boxb", fontName="Helvetica", fontSize=8.6, textColor=INK, leading=12.2),
}

def cell(t, r=False, b=False):
    st = ParagraphStyle("x", parent=S["cellR" if r else "cell"], fontName="Helvetica-Bold" if b else "Helvetica")
    return Paragraph(t, st)

def table(rows, col_w, header=True, pad=3.6):
    sc = [("VALIGN",(0,0),(-1,-1),"MIDDLE"),
          ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
          ("LEFTPADDING",(0,0),(0,-1),7),("RIGHTPADDING",(-1,0),(-1,-1),7),
          ("BOX",(0,0),(-1,-1),0.6,LINE),
          ("ROWBACKGROUNDS",(0,1 if header else 0),(-1,-1),[colors.white, colors.HexColor("#F7F4EE")])]
    if header:
        sc += [("BACKGROUND",(0,0),(-1,0),TEAL),("TEXTCOLOR",(0,0),(-1,0),colors.white),
               ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("LINEBELOW",(0,0),(-1,0),0.4,LINE)]
    t = Table(rows, colWidths=col_w, hAlign="LEFT"); t.setStyle(TableStyle(sc)); return t

def box(text, bg, bd):
    b = Table([[Paragraph(text, S["boxb"])]], colWidths=[7.3*inch])
    b.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),("BOX",(0,0),(-1,-1),0.5,bd),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9)]))
    return b

def header():
    iw, ih = 2000, 373
    h = Table([[Image(LOGO, width=1.55*inch, height=1.55*inch*ih/iw),
        Paragraph("THE FRIEDMAN TEAM<br/><font size=7 color='#5B6B6E'>brokered by eXp Realty</font>",
            ParagraphStyle("r", fontName="Helvetica-Bold", fontSize=9, textColor=TEAL, leading=12, alignment=TA_RIGHT))]],
        colWidths=[3.7*inch, 3.6*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
    return [h, Spacer(1,3), HRFlowable(width="100%", thickness=1.3, color=GOLD, spaceAfter=8)]

story = []
today = datetime.date.today().strftime("%B %#d, %Y")

# ===== PAGE 1 =====
story += header()
story += [Paragraph("Selling 7721 Wilson Ave, Parkville", S["h1"]),
    Paragraph("An honest read on the first listing run, and the full plan to relaunch it and get it sold.", S["sub"]),
    Spacer(1,5),
    Paragraph("PREPARED FOR", S["lbl"]),
    Paragraph("Nicole Fern &nbsp;&middot;&nbsp; %s &nbsp;&middot;&nbsp; Kyle Friedman, The Friedman Team" % today, S["val"]),
    Spacer(1,10)]

story += [Paragraph("Your house did not fail. The marketing did.", S["sec"]),
    Paragraph("You already did the hard part. The home is fully renovated, the big systems are handled, and it "
    "is vacant and ready to show. A move-in ready home in Parkville does not sit for six weeks with no offers "
    "because of the house or the neighborhood. It sits because of how it was listed, presented, and launched. "
    "Every one of those things is fixable, and none of them are on you.", S["body"]),
    Spacer(1,5),
    Paragraph("This packet lays out exactly what happened, what the comparable homes are doing, and the "
    "step-by-step plan to put it back on the market so it sells this time.", S["body"]),
    Spacer(1,5),
    Paragraph("The Parkville market is not working against you. Homes here that are priced and presented "
    "right are going under contract in about three and a half weeks, at close to full price. A renovated, "
    "move-in ready home with a finished lower level should be one of the faster sales on the block, not one "
    "that sits for six weeks and comes off unsold. The timing is right too. Fall is the year's second "
    "selling season, and the buyers shopping in September and October are the serious ones: pre-approved, "
    "motivated, and looking to be settled before the holidays and the new year.", S["body"]),
    Spacer(1,9),
    Paragraph("What the first listing run looked like", S["sub2"])]
rows = [[cell("Date"), cell("Event"), cell("Price", r=True)]]
for d,e,p in [
    ("Jul 17", "Coming Soon", ""),
    ("Jul 24", "Listed", "$340,000"),
    ("Aug 6", "Price cut, about 2 weeks in", "$334,900"),
    ("Aug 18", "Price cut, about 3.5 weeks in", "$324,900"),
    ("Sep 6", "Came off the market", ""),
]:
    rows.append([cell(d), cell(e), cell(p, r=True)])
story += [table(rows, [1.1*inch, 4.6*inch, 1.6*inch]), Spacer(1,5),
    Paragraph("About six weeks live, two price cuts, a handful of showings, and no offers. There were no "
    "showings at all in the first week, which is when the photos were re-ordered and AI staging was added.", S["body"]),
    Spacer(1,9),
    box("<b>The home shows well.</b> Brand new kitchen. Main-level primary bedroom with a full bath. A fully "
    "finished lower level with a large rec room, a second full bath, and a walk-up exit. Sun-filled dining "
    "room. One of the bigger fenced yards on the block. New roof (2018), boiler (2022), mini-split system "
    "(2023), new sewer line (2023). This is a turn-key home. It is also unusual in this pocket, because most "
    "competing homes do not have a finished lower level with its own bathroom. The first listing did not sell "
    "any of that.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 2 =====
story += header()
story += [Paragraph("The number one problem: the square footage on the MLS was wrong", S["sec"]),
    Paragraph("Listings show above-grade square footage. That is the number buyers filter on when they search, "
    "and it is the number every price-per-foot comparison runs on. On the MLS, 7721 Wilson was entered at "
    "about <b>1,287 above-grade square feet</b>. Zillow, Redfin, and the prior sale records all put the home "
    "at roughly <b>1,700 above-grade square feet</b>. That is a 400 square foot gap, and it did real damage.", S["body"]),
    Spacer(1,6),
    Paragraph("1. It made the home invisible in a big share of buyer searches", S["sub2"]),
    Paragraph("A large number of buyers set a minimum size, commonly 1,400 or 1,500 square feet and up, "
    "because they need the room. At 1,287 square feet, 7721 Wilson was filtered out of every one of those "
    "searches before anyone ever saw a photo. A renovated 3 bedroom Cape Cod with a finished lower level "
    "should have been landing in searches as a comfortably sized home. Instead it read as one of the smallest "
    "listings in the area.", S["body"]),
    Spacer(1,4),
    Paragraph("2. It made the price look high", S["sub2"])]
rows = [[cell("Above-grade sf used"), cell("$324,900 works out to", r=True), cell("How a buyer reads it")]]
for a,b,c in [
    ("1,287 sf (as listed on the MLS)", "$252 / sf", "Expensive. Priced above the comparable homes."),
    ("~1,700 sf (what every other source shows)", "~$191 / sf", "Right in line with the market."),
]:
    rows.append([cell(a), cell(b, r=True), cell(c)])
story += [table(rows, [2.5*inch, 1.6*inch, 3.2*inch]), Spacer(1,4),
    Paragraph("Same house, same price, opposite impression. And this is before the finished lower level is "
    "even counted. That space, a rec room plus a full bath plus a walk-up, is real living area that most "
    "competing homes do not have. It should be adding value on top of a correct above-grade number, not "
    "getting buried under a wrong one.", S["body"]),
    Spacer(1,5),
    Paragraph("The buyers and agents who did find the listing were comparing a fully renovated home against "
    "smaller, more dated ones, because on paper the size put it in the same class of home. On screen, 7721 "
    "Wilson looked like it was asking more money for less house. It is actually the opposite.", S["body"]),
    Spacer(1,9),
    box("<b>The fix.</b> Have the home professionally measured, correct the above-grade square footage on the "
    "MLS with a floor plan as the source, and present the finished lower level clearly as bonus space. A "
    "60-year-old assessor card is not a measurement. This one change alone puts the listing back into "
    "hundreds of searches it was locked out of, and it resets the price-per-foot story from expensive to "
    "smart buy.", colors.HexColor("#EAF1F0"), LINE)]

story += [PageBreak()]

# ===== PAGE 3 =====
story += header()
story += [Paragraph("Plan first, then prepare, then execute", S["sec"]),
    Paragraph("The order matters more than any single tactic. The first listing run went the other way. It "
    "executed first: it went live, then sat with no showings, then the photos were re-ordered, then AI "
    "staging was added several weeks in, then the price was cut, then cut again, then the listing was pulled. "
    "That is executing, then planning, then executing again, in public, while buyers watch.", S["body"]),
    Spacer(1,4),
    Paragraph("The agent's photos were about as good as they could be for the situation. The problem was not "
    "effort. It was sequence. Staging, pricing, and the launch schedule are decisions you make and lock in "
    "<b>before</b> the home is ever visible, because you only get one first week and you cannot re-run it.", S["body"]),
    Spacer(1,4),
    Paragraph("A relaunch is the reverse. We build the entire plan first, walk through all of it with you, "
    "the square footage fix, the floor plan, the Showcase media, the ad campaign, the Coming Soon schedule, "
    "the price and how we hold it, and then we execute it one time, cleanly.", S["body"]),
    Spacer(1,8),
    Paragraph("How a home actually sells, and where the first run lost it", S["sub2"])]
rows = [[cell("Step"), cell("What it does"), cell("What happened the first time")]]
for a,b,c in [
    ("1. Get Found",
     "Show up in the searches buyers are running. Correct above-grade square footage, the right price band, complete listing data, syndicated everywhere.",
     "Lost. Listed at 1,287 sf, so it dropped out of every search with a size filter."),
    ("2. Get the Click",
     "The first photo, the price, and the headline earn the tap. Zillow Showcase places the listing above standard listings in the results.",
     "Weak. Photos re-ordered and basic AI staging added in week two, no Showcase, listing already stale."),
    ("3. Get the Showing",
     "The online experience makes a buyer need to see it in person. 3D tour, interactive floor plan, interactive staging, video.",
     "Partial. No floor plan and no 3D tour, so the main-level primary and the finished lower level did not read."),
    ("4. Get the Offer",
     "Read the showing feedback, hold one correct price with a plan, and negotiate.",
     "Lost. Two cuts in 25 days trained buyers to wait for the next one, then the listing was withdrawn."),
]:
    rows.append([cell(a, b=True), cell(b), cell(c)])
story += [table(rows, [1.15*inch, 3.15*inch, 3.0*inch]), Spacer(1,8),
    box("<b>Kyle's rule.</b> Exposure is not an option, it is the whole job. Get the home in front of every "
    "buyer who should see it, make it impossible to scroll past, and give them a reason to act now.", CREAM, GOLD)]

story += [PageBreak()]

# ===== PAGE 4 =====
story += header()
story += [Paragraph("What the market says", S["sec"]),
    Paragraph("Parkville, 21234, is a working market. Homes that are priced and presented right go under "
    "contract in about three and a half weeks at close to full price. Here are comparable homes with a "
    "similar total finished footprint to 7721 Wilson.", S["body"]), Spacer(1,4),
    Paragraph("Under contract right now", S["sub2"])]
rows = [[cell("Address"), cell("List", r=True), cell("Bd/Ba", r=True), cell("Total fin. sf", r=True), cell("Note")]]
for a,p,bb,sf,nt in [
    ("7719 1/2 Daniels Ave", "$349,900", "3 / 2", "2,190", "about the same finished size as yours"),
    ("3324 Texas Ave", "$359,000", "3 / 2", "2,225", "went pending in early August"),
    ("2917 Linganore Ave", "$300,000", "4 / 2.1", "2,280", "the lower end of the band"),
]:
    rows.append([cell(a), cell(p, r=True), cell(bb, r=True), cell(sf, r=True), cell(nt)])
story += [table(rows, [1.75*inch, 1.0*inch, 0.8*inch, 1.15*inch, 2.55*inch]), Spacer(1,6),
    Paragraph("Sold in the last six months, roughly 1,850 to 2,000 total finished sf", S["sub2"])]
rows = [[cell("Address"), cell("Sold", r=True), cell("Bd/Ba", r=True), cell("Total fin. sf", r=True), cell("Note")]]
for a,p,bb,sf,nt in [
    ("2702-B Wildberger Ave", "$360,000", "3 / 2", "1,994", "renovated, the top of the set"),
    ("3033 Parktowne Rd", "$355,600", "3 / 2", "~1,694", "May"),
    ("8204 Wilson Ave", "$350,000", "3 / 2", "~1,691", "your street, June"),
    ("3224 Acton Rd", "$330,000", "3 / 2", "1,936", "August"),
    ("3007 Texas Ave", "$309,000", "3 / 2", "1,875", "dated, the lower end"),
]:
    rows.append([cell(a), cell(p, r=True), cell(bb, r=True), cell(sf, r=True), cell(nt)])
story += [table(rows, [1.75*inch, 1.0*inch, 0.8*inch, 1.15*inch, 2.55*inch]), Spacer(1,7),
    Paragraph("Where 7721 Wilson prices", S["sec"]),
    Paragraph("Renovated, about 1,700 above grade with a finished lower level that has its own bath and a "
    "walk-up, a main-level primary bedroom, and updated systems throughout. That is a stronger package than "
    "most of the homes that sold, and two homes with the same finished footprint are under contract right "
    "now at $349,900 and $359,000. With the square footage corrected and the listing presented properly, "
    "you have two good ways to price the relaunch.", S["body"]),
    Spacer(1,4)]
rows = [[cell("Option", b=True), cell("List price", b=True), cell("The idea", b=True)]]
for a,b,c in [
    ("Priced to dominate", "$319,000",
     "Clearly the best value in the pocket. Renovated, more finished space than the homes that sold, and under every active competitor. Pulls a wave of showings the first weekend and sets up multiple offers that can bid back toward $330,000 or higher. Best if the priority is a fast, clean sale."),
    ("Priced right, held firm", "$324,900 to $329,900",
     "Defensible against every comparable home. One number, set correctly, and held. A single decisive move only if activity is genuinely soft after about three weeks. No ladder of cuts."),
]:
    rows.append([cell(a, b=True), cell(b), cell(c)])
story += [table(rows, [1.45*inch, 1.3*inch, 4.95*inch]),
    Paragraph("Comparable sales and status from Bright MLS and public sources, September 2026.", S["cap"])]

story += [PageBreak()]

# ===== PAGE 5 =====
story += header()
story += [Paragraph("The presentation: give every buyer a reason to fall for it", S["sec"]),
    Paragraph("Buyers decide with emotion and then justify it with logic. An offer happens when a buyer has "
    "spent enough time with a home to picture their family living in it. The whole job of the online "
    "presentation is to create that time and that picture. Here is the difference between what the first "
    "listing had and what this one gets.", S["body"]),
    Spacer(1,7),
    Paragraph("Basic AI staging (the first listing)", S["sub2"]),
    Paragraph("A few photos were given one AI-generated furniture look, and it was added weeks into the "
    "listing after it had already gone quiet. One style, applied late, on a listing buyers had stopped "
    "watching. It does not hold anyone's attention and it does not build attachment.", S["body"]),
    Spacer(1,5),
    Paragraph("Zillow Showcase (the relaunch)", S["sub2"]),
    Paragraph("&#8226; <b>A full 3D Matterport tour</b> the buyer walks through room by room, from their "
    "couch, at 11pm, as many times as they want.<br/>"
    "&#8226; <b>An interactive floor plan</b> tied to the photos and the tour, so the main-level primary and "
    "the finished lower level are obvious in two seconds.<br/>"
    "&#8226; <b>Interactive virtual staging in multiple design styles.</b> A buyer who likes contemporary "
    "sees every room contemporary. One who likes traditional, modern farmhouse, or transitional flips it to "
    "that. Each buyer views the home in the style they would actually live in, which is what makes it feel "
    "like theirs.<br/>"
    "&#8226; <b>Premium placement.</b> Showcase listings sit above standard listings in Zillow search "
    "results, available only through select agents.", S["body"]),
    Spacer(1,7),
    box("<b>Why it works.</b> Showcase listings are 20% more likely to get an accepted offer within 14 days, "
    "sell for about 2% more, and earn 75% more page views, 68% more saves, and 75% more shares than "
    "comparable listings. That is not a coincidence. More time on the listing means more emotional "
    "attachment, and emotional attachment is what produces an offer.<br/>"
    "<font size=7.5 color='#5B6B6E'>See how it works: "
    "<a href='https://www.zillowgroup.com/news/zillow-showcase-brings-listings-to-life/' color='#0F5C63'>"
    "zillowgroup.com/news/zillow-showcase-brings-listings-to-life</a></font>", colors.HexColor("#EAF1F0"), LINE),
    Spacer(1,7),
    Paragraph("The rest of the launch package", S["sub2"]),
    Paragraph("&#8226; Professional photography and video, plus a twilight exterior.<br/>"
    "&#8226; Google and social paid ads across the Baltimore metro buyer market from day one. A recent "
    "listing reached over 82,000 views and 37,000 unique viewers in 30 days.<br/>"
    "&#8226; A single-property website, and syndication to Zillow, Redfin, and realtor.com.<br/>"
    "&#8226; A print piece to the block and the surrounding streets, and clean signage with a QR code that "
    "captures every drive-by.", S["body"])]

story += [PageBreak()]

# ===== PAGE 6 =====
story += header()
story += [Paragraph("The launch: Coming Soon Thursday, live the next Thursday, open house that weekend", S["sec"]),
    Paragraph("Most of a listing's offers come out of its first week on the market, and buyers do most of "
    "their touring on weekends. The whole schedule is built around landing the home in front of the biggest "
    "possible weekend audience, at its freshest.", S["body"]),
    Spacer(1,4)]
rows = [[cell("When"), cell("What happens"), cell("Why it works")]]
for a,b,c in [
    ("Thursday<br/>Coming Soon",
     "The listing goes public on Zillow and the MLS as Coming Soon, with the photos and the 3D tour, but not yet bookable. It gets boosted placement in Zillow search. Ads start.",
     "Thursday is when buyers plan their weekend, so the home lands fresh in mind. It banks a full week of saves and tour requests before going live, and that activity tells us the price is right before it counts."),
    ("The next Thursday<br/>Active",
     "The listing converts to Active. Every buyer who saved it during Coming Soon, plus every new buyer, gets it right before their weekend tours. Showings open.",
     "Redfin's data: homes that go active on Thursday go under contract about 5 days faster than homes listed Sunday. We launch to a full, warmed-up audience, not an empty room."),
    ("That Saturday and Sunday<br/>Open house + brokers open",
     "A public open house and a brokers open across the first weekend, when the listing is newest and traffic peaks. Direct calls to agents with buyers in this range.",
     "Most of a listing's views happen in week one. Concentrating that demand into set windows puts buyers in the house at the same time, and seeing other buyers is what creates urgency and produces offers."),
    ("The following week<br/>Offers",
     "Offers come in early the next week, ideally more than one, and we review them together.",
     "About 250 views a day in week one puts a home on pace to be under contract inside a week. More than one interested buyer means we can set a deadline and let them compete."),
]:
    rows.append([cell(a, b=True), cell(b), cell(c)])
story += [table(rows, [1.2*inch, 3.05*inch, 3.05*inch]), Spacer(1,4),
    Paragraph("Sources: "
    "<a href='https://www.redfin.com/news/best-day-to-list-your-home-for-sale-2019/' color='#0F5C63'>"
    "Redfin best-day-to-list study</a> and "
    "<a href='https://www.zillow.com/research/save-shares-views-35038/' color='#0F5C63'>"
    "Zillow listing-engagement research</a>. "
    "<a href='https://zillow.mediaroom.com/2024-04-16-Showcase-listings-on-Zillow-are-more-than-just-cutting-edge-featured-homes-sell-faster-and-for-more-money' color='#0F5C63'>"
    "Zillow Showcase performance data</a>.", S["cap"]),
    Spacer(1,6),
    box("<b>It comes back as a new listing.</b> We relaunch with a new MLS number, which resets the "
    "days-on-market count to zero. New photos, a new floor plan, the corrected square footage, Showcase, "
    "and a new price. To every buyer scrolling, it is a brand new listing, because in every way that "
    "matters it is. And the timing is good: fall is a strong selling season, and the serious, ready buyers "
    "are out looking right now.", CREAM, GOLD),
    Spacer(1,8),
    Paragraph("What you get from me", S["sub2"]),
    Paragraph("&#8226; Showing feedback within 48 hours, and a weekly call on activity, feedback, and pricing.<br/>"
    "&#8226; A team. I lead pricing and negotiation, a home prep advisor helps the home show its best, and a "
    "transaction coordinator manages every deadline from contract to close.<br/>"
    "&#8226; Easy Exit. Cancel anytime, no binding contract, no questions asked.<br/>"
    "&#8226; Licensed since 2018, 10 to 20 sales a year since 2020. Two homes that sat six months with "
    "another agent, relisted with this plan, went under contract in 30 days and at the open house.", S["body"]),
    Spacer(1,7),
    box("<i>\"I've been a homeowner for 45-plus years and dealt with a number of realtors, but none like "
    "Kyle. He is truly the best: professional, thorough, and an exceptional communicator.\"</i><br/>"
    "<font size=7.5 color='#5B6B6E'>Seller of 7106 Stratos Ln</font>", colors.HexColor("#F4F1EA"), LINE),
    Spacer(1,7),
    Paragraph("Next steps", S["sec"]),
    Paragraph("1. Our call today, to walk through this and answer your questions.<br/>"
    "2. A quick walk-through of the home so I can confirm the measurement, set the list price, and book a "
    "photography date.<br/>"
    "3. Lock in the plan and set the Coming Soon and launch dates.", S["body"]),
    Spacer(1,10),
    HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=5),
    Paragraph("Kyle Friedman &nbsp;|&nbsp; The Friedman Team &nbsp;|&nbsp; brokered by eXp Realty "
    "&nbsp;|&nbsp; (443) 789-3101 &nbsp;|&nbsp; kyle@friedmanreteam.com &nbsp;|&nbsp; friedmanreteam.com", S["foot"]),
    Paragraph("Equal Housing Opportunity. Information deemed reliable but not guaranteed and should be "
    "independently verified. For informational purposes only; not tax, legal, or financial advice. "
    "Comparable sales and market figures from Bright MLS and public sources, September 2026.", S["disc"])]

SimpleDocTemplate(OUT, pagesize=LETTER, leftMargin=0.6*inch, rightMargin=0.6*inch,
    topMargin=0.4*inch, bottomMargin=0.45*inch, title="Listing Presentation - 7721 Wilson Ave, Parkville",
    author="Kyle Friedman, The Friedman Team").build(story)
print("wrote", OUT)
