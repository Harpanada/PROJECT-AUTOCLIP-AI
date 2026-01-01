def Segments(words, min_dur=25, max_dur=55):
    segments = []
    cur = []
    start = words[0]['start']

    for w in words:
        cur.append(w)
        dur = w['end'] - start

        if dur >= max_dur:
            segments.append({'start': start, 
                             'end': w['end'], 
                             'words': cur
            })
            cur = []

            if len(words) > words.index(w) + 1:
                start = words[words.index(w) + 1]['start']

        elif dur >= min_dur and w['text'].endswith(('.', '!', '?')):
            segments.append({'start': start, 
                             'end': w['end'], 
                             'words': cur
            })
            cur = []

            if len(words) > words.index(w) + 1:
                start = words[words.index(w) + 1]['start']

