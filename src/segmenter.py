<<<<<<< HEAD
def Segments(words, min_dur=60, max_dur=120):
    print("On Segmenter...")
    segments = []
    cur = []
    start = words[0]["start"]
    print("Start:", start)
=======
# def Segments(words, min_dur=60, max_dur=120):
#     print("On Segmenter...")
#     segments = []
#     cur = []
#     start = words[0]["start"]
#     print("Start:", start)
>>>>>>> a22b40e (Stop tracking data folder)

#     for w in words:
#         cur.append(w)

#         dur = w["end"] - start
#         # print("Duration:", dur)
#         if dur >= min_dur:
#             if dur <= max_dur:
#                 segments.append({
#                     "start": start,
#                     "end": w["end"],  
#                     "text": " ".join(x["word"] for x in cur)
#                 })

#                 cur = []

#             else:
#                 cur = []

#         if len(cur) == 0 and w != words[-1]:
#             start = w["start"]

#     return segments

<<<<<<< HEAD
=======

#New method segmenter
def group_ideaof(segment):
    clips = []
    currrent = []
    dur =0

    for seg in segment:
        currrent.append(seg)
        dur += seg['end'] - seg['start']

        text = seg['text'].strip().lower()

        its_enough  = dur >= 25
        idea_end= text.endswith(".") or text.endswith('?') or text.endswith('!')
        its_to_loong= dur >=120

        if its_enough and idea_end or its_to_loong:
            clips.append(currrent)
            currrent = []
            dur = 0

    if currrent:
        clips.append(currrent)
    
    return clips
>>>>>>> a22b40e (Stop tracking data folder)
