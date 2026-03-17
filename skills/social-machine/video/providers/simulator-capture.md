# Video Provider: iOS Simulator Capture

Records screen captures from the iOS Simulator for mobile app demo videos.

**Status:** Phase 2 — Framework defined, implementation pending.

---

## Concept

1. Boot iOS Simulator with the app running
2. Record a scripted interaction sequence
3. Export as video file
4. Add text overlays and branding

---

## Prerequisites

- Xcode installed with iOS Simulator
- App built and running in simulator
- ffmpeg for post-processing

---

## Workflow (To Be Implemented)

### Step 1: Verify Simulator
```bash
# Check booted simulators
xcrun simctl list devices booted

# If not booted, the user needs to start it manually
# (building and booting simulators requires Xcode project context)
```

### Step 2: Record
```bash
# Start recording
xcrun simctl io booted recordVideo \
  --codec=h264 \
  --force \
  .social-machine/output/sim_recording.mp4

# Recording runs until interrupted (Ctrl+C or kill signal)
# Tell the user to interact with the simulator, then say "stop"
```

### Step 3: Post-Process

Trim, resize, and add overlays:
```bash
# Trim to relevant section
ffmpeg -i sim_recording.mp4 -ss 00:00:02 -to 00:00:17 -c copy trimmed.mp4

# Add branded frame/overlay
ffmpeg -i trimmed.mp4 -vf "drawtext=text='Yoked':fontsize=36:fontcolor=white:x=w-tw-20:y=h-th-20" output.mp4

# Resize for platform
ffmpeg -i output.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" final.mp4
```

### Step 4: Add Captions
If voiceover is added (via ElevenLabs provider), burn in captions.

---

## Notes

- Simulator recordings capture at the simulator's resolution — use iPhone 15 Pro for best quality
- Tell the user to hide the simulator toolbar for cleaner recordings
- Recordings include the status bar — consider cropping it out in post-processing
- For the best "authentic" feel, record at real speed (not sped up)
