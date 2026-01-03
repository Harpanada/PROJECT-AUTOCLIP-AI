def Segments(words, min_dur=60, max_dur=120):
    segments = []
    cur = []
    start = words[0]["start"]

    for w in words:
        cur.append(w)
        dur = w["end"] - start

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
