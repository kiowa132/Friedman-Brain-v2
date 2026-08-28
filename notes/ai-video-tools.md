# AI Video Tools — Realistic Video of Kyle

Goal: make realistic short videos of Kyle (his own likeness, his consent)
for real-estate marketing — talking-head scripts, ideally in settings like
a closing table, a house, or talking with clients. Category name:
**AI avatar / digital twin video**.

## The one hard limitation (applies to every tool below)
Talking-head — Kyle chest-up, reading a script, real or virtual
background — works well today. **Full-body walking a house, gesturing at a
counter, handing a client a pen, multi-person scenes — does NOT look right
yet** on any tool, free or paid. The practical move is **hybrid**: AI
avatar (or filmed) for the spoken lines, real phone B-roll for the
environment/action, cut together.

Also: for a single one-off clip, just filming it on a phone (window light,
tripod, CapCut for captions — all free) beats an AI avatar. The avatar's
value is **volume without filming** (weekly market updates, per-listing
intros), which is where ~$29/mo starts to pay off.

## Paid SaaS (custom avatar of yourself is always a paid tier)
| Tool | Best for | Rough price |
|---|---|---|
| **HeyGen** | Overall quality + ease; voice clone; custom backgrounds | ~$29–89/mo (custom avatar needs a mid tier) |
| **Argil** | Short-form social (Reels/TikTok/Shorts); clone from phone footage; gesture control | ~$39+/mo |
| **Synthesia** | Polished, explainer/training tone; "Personal Avatar" from ~10 min footage | ~$18–89+/mo |
| **Captions (Mirage)** | Social-first, editing built in | trial then paid |
| **Veo 3 / Kling / Runway** | Environment B-roll, NOT "Kyle talking" | credit-based |

Free tiers only give generic **stock** avatars (not Kyle's face),
watermarked, ~1 min cap. No free path to a custom avatar of yourself on
the SaaS tools.

## Free / open-source stack (build the pipeline yourself)
Pipeline: `script → TTS in cloned voice → lip-sync model (audio + a
reference video of Kyle) → face-restore → export`.

- **Lip-sync:** Easy-Wav2Lip (re-lips existing footage of you with new
  audio — best fit), LatentSync / MuseTalk (newer, better mouth, heavier),
  SadTalker / LivePortrait (animate from a single photo — more "AI"-looking)
- **Voice clone (local):** F5-TTS, GPT-SoVITS, Chatterbox — ~2 min of
  clean audio
- **Cleanup:** CodeFormer / GFPGAN face-restore pass
- **Glue:** ComfyUI has nodes for most of these — wire it into one graph

Requirements / true cost of "free":
- NVIDIA GPU — 8GB handles Wav2Lip/SadTalker; 12–24GB for the good
  diffusion models. No GPU → rent cloud (RunPod, Vast.ai) ~$0.30–0.50/hr
- First-time setup is a real afternoon (Python, CUDA, model downloads)
- The genuinely good research models (EMO, OmniHuman) are NOT released —
  that's the gap between open source and the SaaS polish

## Manual vs automatic
**One-time setup — mostly manual (~an afternoon):** install
Python/CUDA/ComfyUI, download weights, film a ~45s base clip + 2 min voice
sample, build & test the workflow graph (reusable after).

**Per video — mostly automatic once wired:** paste script (manual) →
TTS (auto, ~1 min) → lip-sync (auto, 2–5 min) → face-restore (auto) →
export (auto). What stays manual every time: **scriptwriting + final
edit/captions/b-roll/posting** (~15–20 min in CapCut) — and that part is
manual on the paid tools too.

Full end-to-end automation (script in → captioned video out → auto-posted)
is buildable with n8n/Make + APIs, but that's its own project.

## Recommended path for Kyle
1. One-off video → film it on a phone, free.
2. Want weekly/volume without filming each → HeyGen Creator (~$29/mo),
   hybrid with real B-roll for any non-talking-head shots.
3. Only go the open-source route if comfortable in ComfyUI/Python and have
   (or will rent) a suitable GPU.

## Guardrails
- Kyle's own likeness + consent = fine. The ID-verification on these tools
  exists to stop doing it to other people.
- Don't stage things that didn't happen — no fake "just closed for $X",
  no fabricated client testimonials.
- Disclosure isn't legally required for delivering real info as your own
  avatar; most agents don't mention it. Kyle's call.

See [[blog-article]] deliverable 4 for the video-script format these feed.
