# Video Provider: ElevenLabs AI Voiceover

Creates UGC-style (User Generated Content) videos with AI voiceover narration over app footage or graphics.

**Status:** Phase 2 — Framework defined, implementation pending.

---

## Concept

1. Write a script/narration based on the post concept
2. Generate voiceover audio via ElevenLabs API
3. Combine voiceover with app screenshots/recordings or animated graphics
4. Export as MP4 at platform-specific dimensions

---

## Prerequisites

- ElevenLabs API key in `.social-machine/credentials.env`:
  ```
  ELEVENLABS_API_KEY=
  ELEVENLABS_VOICE_ID=
  ```
- ffmpeg installed for audio/video combining
- App screenshots or screen recordings available

---

## Workflow (To Be Implemented)

### Step 1: Script Generation
Based on the ideation brief, write a 15-30 second narration script.
Keep it conversational and authentic — UGC style, not corporate.

### Step 2: Generate Voiceover
```bash
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "{script}", "model_id": "eleven_multilingual_v2"}' \
  --output .social-machine/output/voiceover.mp3
```

### Step 3: Create Visual Track
Either:
- Use captured app screenshots as a slideshow
- Use screen recording from simulator/browser
- Generate animated HTML and record it

### Step 4: Combine Audio + Video
```bash
ffmpeg -i visual_track.mp4 -i voiceover.mp3 \
  -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 \
  -shortest output.mp4
```

### Step 5: Add Captions/Subtitles
Auto-generate captions from the script and burn them into the video.
This is essential for social media where most videos are watched on mute.

---

## Notes

- ElevenLabs offers various voices — let the user pick one that matches their brand tone
- Keep videos short: 15-30 seconds for TikTok/Reels, up to 60 seconds for longer content
- Captions/subtitles are non-negotiable — 85% of social video is watched on mute
