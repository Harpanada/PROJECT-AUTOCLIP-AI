from transcribe import Transcribe
from segmenter import Segments
from scorer import pick_top_segments
from clipper import clip_video

#Input Video
VIDEO="data/input/input.mp4"

result= Transcribe(VIDEO,"data/transcripts/transcript.json")
words= result["segments"][0]["words"]

segments= Segments(words)
top_segments= pick_top_segments(segments, k=5)

for i, seg in enumerate(top_segments):
    out = f"data/clips/clip_{i+1}.mp4"
    clip_video(VIDEO, seg["start"], seg["end"], out)
    print("saved:", out)