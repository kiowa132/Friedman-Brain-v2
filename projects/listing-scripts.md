# Listing Scripts

Kyle's scripts for (1) setting the listing appointment, and (2) closing it at
the presentation.

**The frame for appointment setting: you are interviewing them.** They are
auditioning to be your client, not the other way around. Ask far more than you
tell. Be willing to disqualify out loud. Your time is scarce and you act like
it. If they're not a fit, you pass, politely, and they chase you.

Focus right now: **Part 1, appointment setting.** Parts 3–5 are drafted; build
those out later.

Draft 3, Sept 2026. Iterate here.

**Get to it fast:**
- Type **`/script`** in Claude Code — pulls up the flows and the tool link.
  `/script expired` (or `followup` / `warm` / `close` / `objections`) for one
  part. Command lives at `~/.claude/commands/script.md`.
- Interactive tap-through tool ("The Listing Call"): https://claude.ai/code/artifact/ff564382-e355-4101-99e0-ff66fa9b21a8
  (one step at a time, fill-in details, objections drawer, yes/soft branch.
  Bookmark on phone.)
- PDF (2pp): `Appointment-Setting-Script.pdf` — generator
  `scripts/pdf/appt-setting-script.py`
- **Part 3 (the question-led listing presentation) as its own printable PDF:**
  `Listing-Presentation-Script.pdf` — generator
  `scripts/pdf/listing-presentation-script.py`

---

# PART 1 — APPOINTMENT SETTING (you run the interview)

## 1.1 The status frame — say this early, every call

After the opener and 20 seconds of small talk:

> "Before I put any real time into your property, I want to make sure we're
> actually a fit — so I'm going to ask you a handful of questions first. That
> work for you?"

That one line flips the call. Now you're the one qualifying. Also useful:

> "I only take on a handful of listings at a time and I'm picky about which
> ones, because every one gets the full machine. So this first call is really
> just me figuring out if I can genuinely help you. Fair?"

Then ask your questions, and **let the silences sit.** Do not fill them.

---

## 1.2 The question bank — pull 6 to 10 per call

Mix and match by what you need to screen. The point is volume of questions and
letting them do the talking.

**Motivation (is this real?)**
- "What's actually driving this? Give it to me straight."
- "Why now, and not six months ago or six months from now?"
- "On a scale of 1 to 10, how committed are you to selling in the next 90 days?"
  *(under 8 — dig, or disqualify.)*
- "If the number comes back lower than you're hoping, are you still selling, or
  does that kill it?"
- "What would have to happen for you to decide NOT to sell?"

**Timeline (is there a real deadline?)**
- "When do you need to be out / into the next place?"
- "Is that a hard deadline or a nice-to-have?"
- "Have you already bought somewhere, or signed a lease?"
- "What happens if it's not sold by then?"

**For-sure seller**
- "Are you 100% selling, or still deciding whether to sell at all?"
- "Is this your decision, or are you still talking each other into it?"

**Decision process (who's really deciding?)**
- "Who else is part of this decision besides you?"
- "Are you both equally on board, or is one of you more into it than the other?"
- "When we sit down, can everyone who's part of the decision be in the room? I
  don't like doing this twice."

**Price realism**
- "What number do you have in your head — and where did it come from?"
- "If I walked you through the actual sold data and it said the market's here,
  and your number's up there, how would you take that?"
- "Would you rather I tell you what you want to hear, or what's true?"

**Condition and prep**
- "What kind of shape is it in — honestly, not the Zillow version."
- "Are you open to doing some prep before it goes live, or does it need to sell
  exactly as it sits?"
- "If a little paint and cleanup got you another 10 or 15 grand, are you in, or
  not your thing?"

**Agent shopping / how they decide**
- "How many agents are you talking to?"
- "What are you using to decide between them?" *(if the answer is "whoever says
  the highest number" — name it: "just so you know, that's how sellers end up
  overpriced and unsold. The highest number and the best agent are usually not
  the same person.")*
- "Have you sold a home before? How did that go?"

**Prior listing (expired / withdrawn especially)**
- "Walk me through the last listing. What do you think actually went wrong?"
- "What did the last agent do — and not do?"
- "What was the original plan when you decided to sell?"
- "If you knew it would sell this time, would you put it back on?"

---

## 1.3 The commitment question — after the interview

> "Okay. Last one. If I can show you a process that gets your home sold for the
> highest price in the quickest amount of time, are you prepared to move
> forward and start the listing paperwork when we meet?"

Then **stop talking.**

- **Yes:** "Perfect. That's what I needed to hear. Let's get a time down."
- **"I need to think / talk to my spouse / not sure":** go to the pass (1.5).
- **"Why do I have to decide before I've seen your number?":** "You don't — you
  decide after I show you everything. I'm only asking: if the plan and the
  price are right, is there anything else that would still stop you?"

---

## 1.4 Book it

- **Two times, never "when are you free":** "Does tomorrow at 5 or Thursday at
  3 work better?"
- **Decision-makers:** "And [spouse] will be there too, yeah?"
- **Confirm out loud:** day, time, address, who's there, about 30 minutes.
- "I'll text you a confirmation. See you [day]."

---

## 1.5 The polite pass (disqualify out loud — this is the "hot girl" move)

When the answers are soft — no real timeline, not a for-sure seller, won't get
the spouse in the room, only wants a price:

> "Honestly? From what you're telling me, I don't think you're quite ready to
> list, and I'd be doing you a disservice pretending you are. Here's what I'll
> do — I'll send you [the sold data for your street / a net sheet / a prep
> checklist]. When [you've got a real timeline / you're both on the same page /
> you're ready to actually move], call me and we'll set a time. Sound fair?"

Then get off the phone. Do not push. The follow-up does the work: day 3, day
10, day 24, then monthly — every touch a piece of value, never "just checking
in." People who weren't ready call back. People who were tire-kickers don't,
and that's a win.

---

## 1.6 Green / Yellow / Red — score them in real time

**Green (book it):** clear motivation, real deadline, "100% selling," all
decision-makers available, coachable on price, open to prep, not chasing the
highest number.

**Yellow (dig more, or book with conditions):** vague timeline, one spouse
lukewarm, a price number they're attached to but will "hear you out," talking
to 3+ agents.

**Red (pass):** "just curious what it's worth," no timeline, "we'll decide
after we see everyone's number," won't get the co-owner on the call, wants to
sell as-is for a fantasy price, hostile to questions.

---

# SCENARIO FLOWS  (this is what the interactive tool runs — 3 real call situations)

The order changes by situation. Not "same interview, different opener."

## FLOW A — Expired / Withdrawn  (first call)

**Book the appointment FAST, then qualify, then back out if they don't check
out.** Don't interview on the phone before you have a time.

1. **Open** — "Hi [Name], Kyle Friedman. Quick question about your house on
   [Street] — got 30 seconds? ... Is that one sold, or still available at the
   right price?"
2. **Plant confidence** — "We just listed one a few blocks from you, had a ton
   of showings the first weekend. Surprised yours didn't sell. I've looked at
   your area, I'm certain it should have, and I think I know why it didn't."
3. **Ask for the appointment now** — "I'm going to be over there tomorrow
   anyway. Let me swing by 15 or 20 minutes and show you what we'd do to
   relaunch it. Does 5 work, or is the morning better?"
4. **They agreed — now qualify** — "Perfect. Before I make the trip, couple
   quick things. What was the plan when you decided to sell, where were you
   headed and by when? ... Still 100% on selling? ... What did the last agent
   do, and not do? ... What number are you attached to, and where'd it come
   from?"
5. **Branch:**
   - *Checks out* → **Lock it** (day, time, address, spouse in the room, "I'll
     text a confirmation").
   - *Not a real seller* → **Back out** — "You know what, before I make the
     trip, let me just send you the breakdown of what sold on your street and
     why yours stalled. If it makes you want another swing, call me." Stays in
     follow-up.

## FLOW B — Follow-up  (you've been calling, they won't book)

**A downgrade ladder. Keep lowering the ask until they say yes to something.**

1. **Reconnect** — "Hey [Name], it's Kyle, following up on [Street]. Got a
   minute?"
2. **A reason for the call** (fresh every time, never "just checking in") —
   "A house near you just went pending around [$X]." / "Prices in your zip
   moved." / "I had a buyer asking about your street." → "Made me think of you."
3. **Status check** — "Where's your head at on selling these days? ... What's
   still holding you up from just getting a plan together?"  *(if they're
   ready → jump to Lock it.)*
4. **Ask direct** — "Let's just put 20 minutes on the calendar. I'll bring your
   real number and your net sheet, no pitch. Tomorrow or Thursday?"
5. **Lower the ask — the free evaluation** — "Okay, how about this. No meeting.
   I'll do a free evaluation and drop it by: what it'd sell for, what to fix
   and what not to, and your closing costs so you know your walkaway number.
   15 minutes, no pitch. Fair?"  *(The free eval is a technique to get in the
   door, not a lead type.)*
6. **If still no — set the next touch** — "No problem. I'll keep you posted
   when something sells nearby. When you're ready for real numbers, one call
   away." Log the next follow-up 2–3 weeks out with a new reason ready.

## FLOW C — Warm  (they reached out / you just talked, they're interested)

**Full discovery, then book.** This is the only one where you interview before
asking for the meeting.

1. **Reconnect** — "Hey [Name], it's Kyle. We talked about [Street]. I pulled
   the numbers. Got a few minutes?"
2. **Rapport** — looks like / sounds like / feels like. "How long have you
   owned it? ... How long in the area?"
3. **Motivation** — "What's got you thinking about selling? ... Why now? ...
   Where are you headed, and when? ... Besides top dollar, what matters most?"
4. **Condition** — "What shape is it in, honestly? Roof, kitchen, baths, HVAC?
   ... Open to a little prep if it gets you more?"
5. **Their number + ballpark** — "What number's in your head, and where'd it
   come from? ... I just want to know if we're in the same ballpark so I'm not
   wasting your time."
6. **Anchor + book** — "We just sold one down the street for [$X], another for
   [$Y]. You're probably in that range. The only way I give you a real number
   is to see it, 30 minutes. Tomorrow at 5 or Thursday at 3?"
7. **Lock it.**

---

# PART 2 — (folded into 1.3 above)

---

# PART 3 — THE LISTING PRESENTATION (question-led, mapped to the deck)

**Principle:** never present a section cold. Every section is the answer to a
question you just asked. Ask, they answer, you show that section and tie it to
what they said, then you ask the next question, which opens the next section. It
feels like a conversation because it is one. The deck (`Listing Presentation
NEW.pdf`) is your visual aid, not your script.

Open light. No question battery up front.

## 0. Set the frame (30 sec, no deck)
> "Before I show you anything, this isn't a canned pitch. I'm going to ask you
> some things, and every time you answer, I'll show you exactly how we handle
> it. By the end you'll know your number, the plan, and whether I'm the right
> person. Sound good? ... Cool. First one."

## 1. Why selling  →  deck: "Your Home"
- **Ask:** "Walk me through why you're selling, and what the win looks like.
  Where are you going, and by when?"
- **Listen for:** real motivation, destination, timeline, what matters most
  (price / speed / a clean move).
- **Show — "Your Home" slide:** "Here's your home on paper. This is what a
  buyer's agent, and Zillow, price off of, and none of them have seen inside.
  That gap between the data and the real house is the first place we make you
  money."
- **Bridge:** "So the question is what it's actually worth. Want to see what's
  really happening in your market?"

## 2. → deck: "The Market Within 2 Miles" + "The Market"
- **Ask:** "What have you seen selling around here, anything catch your eye,
  good or bad?"
- **Show — market slides:** "Every sale within two miles the last few months,
  and the trend. The ones priced right were gone in [X] days. The ones that
  chased the market down sat for [Y] and sold for less."
- **Bridge:** "So how do we make sure yours is the one that's gone in days, not
  the one that sits? That's pricing."

## 3. → deck: "Pricing Your Property" (the decay chart)
- **Ask:** "If you had to guess, when does a listing get the most attention:
  week one, week four, or week eight?"  *(Most say later. They're wrong. Good.)*
- **Show — pricing decay slide:** "Week one. 7 days is peak attention. After
  that buyer activity drops, and perceived value drops with it. Homes that sit
  24-plus weeks sell about 9% under market. So we don't price to test the
  ceiling and walk it down. We price to hit that first week hard and create
  competition."
- **Bridge:** "That only works if enough buyers see it in week one. How do you
  think most buyers are going to find your house?"

## 4. → deck: "Your Marketing Strategy" (steps 1–10)
- *(They answer "Zillow?" / "the sign?")*
- **Show — marketing slides, fast:** "Some of them. Here's the whole machine,
  ten steps. The part most agents skip is Coming Soon, we build a buyer
  pipeline before it's even live, so day one there's already demand. Then
  photography, the property site, brokers open, and a paid digital campaign,
  plus me personally on the phone to agents and neighbors."
- **Bridge:** "And that reach isn't a guess. Want to see the actual numbers?"

## 5. → deck: "Social Media Online Reach" + "We Never Miss Buyer Calls"
- **Show:** "Last listing: 82,000 views, 37,000 people, 30 days. It takes about
  12 touches for a buyer to decide, so we hit them across platforms,
  repeatedly. And every inquiry, the QR code, the 800 number, a 2am text, gets
  captured and followed up. Nothing leaks."
- **Bridge:** "So that's the marketing. Who actually does all this while you're
  living your life?"

## 6. → deck: "Your Team" + "Home Prep Advisor" + "Transaction Coordinator" + "Your Path to Success"
- **Ask:** "Have you sold a home before? ... What was the most stressful part?"
- **Listen for:** coordination, communication, the paperwork (usually).
- **Show — team slides:** "That's exactly why it's not just me. I run strategy
  and negotiation. A Home Prep Advisor gets it show-ready, what to fix, what to
  skip, staging. A Transaction Coordinator owns every deadline and document
  from contract to keys, so nothing falls through. This slide is the whole
  track, start to finish."
- **Bridge:** "Plan's solid, team's solid. Does all this actually get a
  different result?"

## 7. → deck: "Faster Sale + More Money" + testimonials + "About Kyle"
- **Show — stats slide:** "It does. My listings sell at 101.6% of list versus
  100.1% for the average agent, on a home like yours that's real money in your
  pocket. 7 days on market versus 16. And here's what that's like to go
  through, from people who did it."
- **Bridge:** "Last thing before we talk number. What's your biggest worry
  about listing? Be honest."

## 8. → deck: "Communication Guarantee" + "Easy Exit Listing Agreement"
- **Listen for:** getting stuck with the wrong agent, being left in the dark
  (usually).
- **Show — guarantee slides:** "Both of those are covered in writing. Feedback
  in 48 hours, a call every week, I'm reachable 1 to 5 every day. And if I'm
  not doing what I said, you fire me. No lengthy contract, no fight. You're
  never stuck."
- **Bridge into the close.**

## THE CLOSE  (Kyle's version — keep it)
> "So, that's how we sell homes for the highest price in the shortest time.
> You do want to sell your home, right?"
> — *Yes.*
> "And have I shown you that I'm the best person to sell it, with the track
> record and the strategy?"
> — *Yes.*
> "Perfect. Next step is the listing paperwork. We get it into the MLS as
> Coming Soon and start building a pipeline of buyers before it even hits the
> market. Let's fill it out."
> → into paperwork; start filling it in, narrate, go quiet.

**If either answer isn't a clean yes:** "What's the piece that's not quite
there — the price, the plan, the commission, or me?" Handle that one thing
(Part 4), then re-ask the two questions.

## The question chain alone (the spine to memorize)
1. Why selling / where to / by when?  → Your Home
2. What have you seen selling nearby?  → The Market
3. When does a listing get the most attention?  → Pricing decay
4. How will buyers find it?  → Marketing (10 steps)
5. *(show reach numbers)*  → Social reach + buyer capture
6. Sold before? Most stressful part?  → Team + Path + roles
7. *(show it gets a different result)*  → Stats + testimonials + About Kyle
8. Biggest worry about listing?  → Guarantees + Easy Exit
9. Close.

## Deck fixes to make (noted Sept 2026)
- "Friedman Real Estate Team" → **"The Friedman Team"** throughout.
- "17 years in real estate" (Faster Sale slide) contradicts the About-Kyle copy
  ("since 2020 / nearly a decade"). Pick one.

---

# PART 4 — OBJECTION HANDLERS  *(build out later, per Kyle)*

- **Price ("I was hoping for more"):** "I could list it there too. Above the
  market it sits, buyers wait for the cut, and it nets less than pricing it
  right on day one. If the market proves me low, we adjust up — better problem."
- **Commission ("can you do it for less"):** "You can find cheaper. You're
  paying for the gap between what a weak listing gets and what this process
  gets, and that gap is almost always bigger than the fee."
- **"We want to think about it":** "Of course. What specifically — the price,
  the plan, or whether it's me?"
- **"One more agent":** "Ask them two things: the sold comps they priced from,
  and their first 14 days. If they can't answer both, you have your answer."

---

# PART 5 — POSTURE RULES

1. You're interviewing them. They audition to be your client.
2. Ask way more than you tell. Let silences sit.
3. The pass is real. If they're not ready, you don't want the appointment yet.
4. Your time is scarce. Say so once, then act like it.
5. The phone call's only job is the appointment — don't price it, don't pitch
   the whole strategy.
6. Never chase. Value on every follow-up. The right ones come back.
7. Honest, not slick. The commitment question only works if you genuinely will
   deliver the process.
