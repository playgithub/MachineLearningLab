#!/usr/bin/sh

# list input sources
# pactl list short sources

ffmpeg -f pulse -i default -ac 2 -af "highpass=200,lowpass=3000,afftdn=nf=-25" a.m4a
#ffmpeg -f pulse -i default -ac 2 a.m4a
#ffmpeg -f pulse -i 54 -ac 2 a.m4a