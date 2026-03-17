# Video Provider: Browser Screen Recording

Records screen captures of web applications via headless browser for app demo videos.

**Status:** Phase 2 — Framework defined, implementation pending.

---

## Concept

1. Navigate to the web app in headless browser
2. Record a scripted interaction sequence (click through features)
3. Export as video file
4. Add text overlays and branding

---

## Prerequisites

- gstack/browse or Playwright available
- Web app running (dev server or live URL)
- ffmpeg for post-processing

---

## Workflow (To Be Implemented)

### Step 1: Script the Interaction
Based on the post concept, define a sequence of browser actions:
```
1. Navigate to homepage → pause 2s
2. Click "Get Started" → pause 2s
3. Fill in form fields → pause 1s
4. Click "Generate" → wait for result → pause 3s
5. Scroll through results → pause 2s
```

### Step 2: Record
```bash
# Using Playwright (if available)
npx playwright codegen --save-storage=auth.json {url}
# Or use gstack/browse with periodic screenshots stitched into video
```

### Step 3: Post-Process
- Add text overlays with ffmpeg drawtext filter
- Add branded intro/outro frames
- Resize to target platform dimensions
- Compress for social media upload limits

---

## Notes

- Browser recordings feel authentic and "real" for app demos
- Keep recordings smooth — avoid rapid mouse movements
- Add a slight zoom effect on key features for emphasis
