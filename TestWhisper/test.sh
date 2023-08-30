#!/usr/bin/sh

stable-ts --device=cpu --word_level=False --model=medium --fp16=False -o a.srt "/path/to/video_or_audio_file"
