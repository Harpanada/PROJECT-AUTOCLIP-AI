def Segments(words, min_dur=60, max_dur=120):
    segments = []
    cur = []
    start = words[0]["start"]
    print("Start:", start)

    for w in words:
        cur.append(w)

        dur = w["end"] - start
        # print("Duration:", dur)
        if dur >= min_dur:
            if dur <= max_dur:
                segments.append({
                    "start": start,
                    "end": w["end"],  
                    "text": " ".join(x["word"] for x in cur)
                })

                cur = []

            else:
                cur = []

        if len(cur) == 0 and w != words[-1]:
            start = w["start"]

    return segments


#Debug Method
# from pathlib import Path
# import json

# json_path = Path("./data/transcripts/transcript.json")

# with open(json_path, "r", encoding="utf-8") as f:
#     data = json.load(f)

# words=[]
# for seg in data["segments"]:
#     if "words" in seg:
#       words.extend(seg["words"])

# segments= Segments(words)
# # print("Total segments:", len(segments))
# # print("Total words:", len(words))

# for a in range(len(segments)):
#     print(f"segment {a}: {segments[a]}\n")