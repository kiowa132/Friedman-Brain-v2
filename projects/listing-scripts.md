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

# PART 3 — LISTING PRESENTATION CLOSE  *(build out later, per Kyle)*

**Trial close:** "So that's the whole process — highest price, shortest time.
Does that make sense? Any questions on how any piece works?"

**The confirm:** "Okay, cool. So that's how we sell your home for the highest
price in the shortest amount of time. And you're looking to sell your property,
right?"

**Assumptive move:** "Great. Next step is the listing agreement so I can lock
in the photographer and start the Coming Soon. Let's run through it." Start
filling it in, narrate, go quiet.

**If they hesitate — isolate:** "Sounds like something's not quite there. Is it
the price, the commission, the timing, or something about me and my team?"

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
