import whisper
import json
from pathlib import Path


def Transcribe(video_path: Path , out_path: Path) -> str:
    print("On Transcription:...")
    model = whisper.load_model("tiny")
    result= model.transcribe(video_path,word_timestamps=True)

    Path(out_path).write_text(json.dumps(result, indent=2))
    return result


