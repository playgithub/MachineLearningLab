from pathlib import Path
import stable_whisper as whisper

device = "cpu"
in_path = "/home/alg/nuc_share/Music/其它/张靓颖 - 画心.mp3"
out_path = Path(in_path).with_suffix(".srt")

model = whisper.load_model("medium", device = device)

result = model.transcribe(in_path, language = "zh", fp16 = False)

print("Output Path: ", str(out_path))
result.to_srt_vtt(filepath = str(out_path), word_level = False)
