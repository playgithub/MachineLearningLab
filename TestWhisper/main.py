from pathlib import Path
import stable_whisper as whisper

# device = "cuda"
device = "cpu"
in_path = "~/Downloads/a.m4a"
out_format = "srt" # ass/srt
word_level = False

model = whisper.load_model("medium", device = device)

result = model.transcribe(in_path, language = "zh", fp16 = False)

if out_format == "srt":
    out_path = Path(in_path).with_suffix(".srt")
    result.to_srt_vtt(filepath = str(out_path), word_level = word_level)
elif out_format == "ass":
    out_path = Path(in_path).with_suffix(".ass")
    result.to_ass(filepath = str(out_path), karaoke = True)
else:
    print("Invalid output format: ", out_format)

