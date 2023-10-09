```sh
ffmpeg -i "/home/alg/nuc_share/Music/其它/卓依婷 - 明天会更好.flac" -ar 16000 -ac 1 -c:a pcm_s16le ./a.wav
whisper.cpp --file ./a.wav --language zh --output-srt --model ~/Develop/lib/whisper.cpp/models/ggml-model-large-v2.bin --threads 16
```
