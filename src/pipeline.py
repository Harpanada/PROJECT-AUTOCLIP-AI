from transcribe import Transcribe
from segmenter import Segments
from clipper import clip_video
from scorer import pick_top_segments

#Input Video 
VIDEO="data/input/subjecTest2.mp4"

#Transcribe Video
result= Transcribe(VIDEO,"data/" \
"transcripts/transcript.json")
words= result["segments"][0]["words"]

#Menggabungkan semua words dari segments
words= [
    w
    for seg in result["segments"]
    for w in seg.get("words", [])
        ]


#Memotong Segment Berdasarkan durasi
segments= Segments(words)
#Mencari 5 Segment Terbaik
top_segments= pick_top_segments(segments )

#Mengekspor Clip Terbaik
for i, seg in enumerate(top_segments):
    print("exporting clip:", seg)
    out = f"data/clips/clip_{i+1}.mp4"
    clip_video(VIDEO, seg["start"], seg["end"], out)
    print("saved:", out)

print("Berhasil..")

  
