from transcribe import Transcribe
<<<<<<< HEAD
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
=======
from segmenter import group_ideaof
from clipper import clip_video
from scorer import pick_top_segments
from audio_fix import Fixed_audio
from build_clip_name import build_clip_name

 
#Input Video 
# url="https://youtu.be/ERUYQEgQ06o"
# video_path= download_youtube(url)
video_path="data/input/IDE ITU TIDAK MAHAL! - Ferry Irwandi (1080p, h264)_fixed.mp4"
video_path= Fixed_audio(video_path)


#Transcribe Video
result= Transcribe(video_path,"data/" \
"transcripts/transcript.json")

# words= result["segments"][0]["words"]
#Menggabungkan semua words dari segments
# words= [
#     w
#     for seg in result["segments"]
#     for w in seg.get("words", [])
#     ]

words = result["segments"]

#Memotong Segment Berdasarkan durasi
segments= group_ideaof(words)
#Mencari 5 Segment Terbaik
top_segments= pick_top_segments(segments )


#Mengekspor Clip Terbaik
for i, seg in enumerate(top_segments):
    print("exporting clip:", seg)
    out = build_clip_name(video_path,i,"data/clips")
    clip_video(video_path, seg["start"], seg["end"], out)
>>>>>>> a22b40e (Stop tracking data folder)
    print("saved:", out)

print("Berhasil..")

<<<<<<< HEAD
=======
  
>>>>>>> a22b40e (Stop tracking data folder)
