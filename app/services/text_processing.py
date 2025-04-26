import math
from collections import Counter
from typing import List
from app.models import WordStats

def process_text(text: str) -> List[WordStats]:
    words = [word.lower() for word in text.split() if word.isalpha()]
    tf_counter = Counter(words)
    total_words = len(words)

    result = []
    for word, count in tf_counter.items():
        tf = count
        idf = math.log(total_words / (1 + count))
        result.append(WordStats(word=word, tf=tf, idf=round(idf, 5)))
    return result
