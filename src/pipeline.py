from transcribe import Transcribe
from segmenter import Segments
from scorer import pick_top_segments
from clipper import clip_video

#Input Video
VIDEO="data/input/sample.mp4"

result= Transcribe(VIDEO,"data/transcripts/transcript.json")
words= result["segments"][0]["words"]


# print("Keys:", result.keys())
# print("Jumlah Segments Whisper:", len(result["segments"]))
# print("Contoh segmen 1:", result["segments"][0])
# print("words di segmen 1:", result["segments"][0].get("words"))


words= [
    w
    for seg in result["segments"]
    for w in seg.get("words", [])
        ]
print("jumlah words:", len(words))


segments= Segments(words)
print("jumlah segments:", len(segments))
print("All Segments:", segments)

top_segments= pick_top_segments(segments, k=5)
print("Top Segments:", top_segments)

for i, seg in enumerate(top_segments):
    print("exporting clip:", seg)
    out = f"data/clips/clip_{i+1}.mp4"
    clip_video(VIDEO, seg["start"], seg["end"], out)
    print("saved:", out)