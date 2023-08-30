#!/usr/bin/sh

ffmpeg -f lavfi -i color=c=black:s=1280x720:r=5 -i "/home/alg/Downloads/张靓颖 - 画心.mp3" -crf 0 -c:a copy -shortest "/home/alg/Downloads/张靓颖 - 画心.mp4"

