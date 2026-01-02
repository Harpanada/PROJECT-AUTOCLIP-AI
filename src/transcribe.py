import whisper
import json
from pathlib import Path


def Transcribe(video_path: Path , out_path: Path) -> str:
    model = whisper.load_model("small")
    result= model.transcribe(video_path,word_timestamps=True)

    Path(out_path).write_text(json.dumps(result, indent=2))
    return result


#Function Testing
# BASE_DIR = Path(__file__).resolve().parent.parent
# VIDEO_PATH = BASE_DIR / "data" /  "input" / "input.mp4"
# OUT_PATH = BASE_DIR / "data" / "transcripts" / "transcript.json"
# print(VIDEO_PATH.exists())

# Transcribe(str(VIDEO_PATH),str(OUT_PATH))
