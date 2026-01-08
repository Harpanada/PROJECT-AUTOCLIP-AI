from transcribe import Transcribe
from segmenter import build_segment
# from segmenter import Segments
from clipper import clip_video
from scorer import pick_top_segments
from audio_fix import Fixed_audio
from build_clip_name import build_clip_name

 
#Input Video 
# url="https://youtu.be/ERUYQEgQ06o"
# video_path= download_youtube(url)
video_path="data/input/11 Pelajaran Hidup Termahal di 2025 - Timothy Ronald (1080p, h264).mp4"
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

# words = result["segments"]
seg = result['segments']


#Memotong Segment Berdasarkan durasi
# segments= Segments(words)
segments= build_segment(seg)
#Mencari 5 Segment Terbaik
top_segments= pick_top_segments(segments )


#Mengekspor Clip Terbaik
for i, seg in enumerate(top_segments):
    print("exporting clip:", seg)
    out = build_clip_name(video_path,i,"data/clips")
    clip_video(video_path, seg["start"], seg["end"], out)
    print("saved:", out)

print("Berhasil..")

  
