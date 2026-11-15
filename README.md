# AIProve — poster, mascot, explainer

Three pieces in one visual system: cream newsprint, black ink, a single lime accent.
Built as HTML/CSS for the poster and character sheet, PIL + ffmpeg for the video.

- `index.html` — gallery with the video and both stills (served on GitHub Pages)
- `poster.png` — 2400×3200 broadsheet poster
- `mascot.png` — 2400×3200 character sheet for **PROOF**
- `video.mp4` — 53s explainer, 1920×1080, 30fps, narrated
- `poster.html`, `mascot.html` — sources, renderable in any browser
- `make_frames.py`, `build_video.sh` — how the video was made
- `transcript.txt` — narration with timestamps

## Why this fits

The brief says broadsheet meets terminal. So the system is a newspaper that a terminal
could have set: a high-contrast serif for the masthead and headlines, monospace for every
label, metric and table, hairline rules instead of boxes, crop marks at the corners, and
one accent colour used as a marker rather than decoration.

The poster carries a real board — six live bounties with their actual metrics and payouts —
so it reads as a front page, not a hero image. The mascot is the artifact the arena
produces: a folded sheet with a check for a smile, drawn in one ink. The video is the same
page in motion: eight cards, one idea each, no stock footage, no logos it does not own.

## Rebuild

```bash
python3 make_frames.py          # 8 frames at 1920x1080
bash build_video.sh             # zoompan + concat + narration -> video.mp4
```

Poster and mascot: open `poster.html` / `mascot.html`, screenshot at 1200×1600 @2x.

Original work. Type: Instrument Serif and JetBrains Mono, DejaVu fallbacks.
