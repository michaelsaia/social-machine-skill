---
name: social-video
version: 0.1.0
description: |
  Create video content for social media using configured providers (ElevenLabs, browser recording,
  simulator capture). Use when the user wants to create video content or runs "/social-video".
  Phase 2 feature — not fully implemented yet.
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# Social Machine: Video (Phase 2)

You are running `/social-video`. This creates video content for social media platforms.

**Status:** Phase 2 — provider framework is in place, full implementation coming.

---

## Prerequisites

1. Read `.social-machine/config.md` — check `video_provider` setting
2. Read `.social-machine/brand.md` — brand context
3. If `video_provider: none`, tell the user: "Video creation is not configured. Run `/social-config` to set up a video provider."

---

## Provider Routing

| Provider | Instructions | Status |
|---|---|---|
| `none` | Not configured | — |
| `elevenlabs` | `video/providers/elevenlabs.md` | Phase 2 |
| `browser-recording` | `video/providers/browser-record.md` | Phase 2 |
| `simulator-capture` | `video/providers/simulator-capture.md` | Phase 2 |

Read the appropriate provider file and follow its instructions.

---

## Video Content Types (Phase 2 Roadmap)

1. **App Demo Reel** — Screen recording of app features with text overlays
2. **UGC-Style Video** — AI voiceover (ElevenLabs) over app footage
3. **Before/After Transformation** — Side-by-side video comparison
4. **Quick Tip Video** — Text + voiceover explaining a feature
5. **Trending Sound Remix** — App footage synced to trending audio

---

## Output

Videos should be saved to `.social-machine/output/` with format:
```
{date}_{content_type}_{platform}.mp4
```

Target specs per platform:
- **TikTok/Reels:** 1080x1920, 9:16, 15-60 seconds, MP4
- **X/Twitter:** 1280x720, 16:9, up to 2:20, MP4
- **LinkedIn:** 1920x1080, 16:9, up to 10 min, MP4
