from pathlib import Path

from matplotlib import text

KEYWORDS = ["intinya", "jadi", "kesimpulannya", "yang penting", "tips"]

def score_segments(seg):
       text= seg["text"].lower()
       keyword_score = sum(k in text for k in KEYWORDS)

       length = len(text.split())
       length_score = 1 if 20 <= length <= 120 else -1

       filler_penalty = text.count("eee") + text.count("uh")

       return keyword_score + length_score - filler_penalty