#!/bin/bash
set -e
FF=~/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg
cd /home/ubuntu/aiprove/art
FPS=30
DURS=(4.62 4.18 8.27 8.03 6.53 6.25 6.57 9.31)
rm -f clip*.mp4 list.txt
i=1
for D in "${DURS[@]}"; do
  FRAMES=$(python3 -c "print(max(2,round($D*$FPS)))")
  $FF -hide_banner -loglevel error -y -i frames/s$i.png \
    -vf "zoompan=z='min(1.0+0.00035*on,1.09)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=${FRAMES}:s=1920x1080:fps=${FPS}" \
    -frames:v ${FRAMES} -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p clip$i.mp4
  echo "file 'clip$i.mp4'" >> list.txt
  i=$((i+1))
done
$FF -hide_banner -loglevel error -y -f concat -safe 0 -i list.txt -c copy silent.mp4
$FF -hide_banner -loglevel error -y -i silent.mp4 -i vo_tight.wav \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11,adelay=250|250,apad" \
  -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart video.mp4
~/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 video.mp4
