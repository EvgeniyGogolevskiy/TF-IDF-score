import math
from collections import Counter


def process_text(text: str):
    words = [word.lower() for word in text.split() if word.isalpha()]
    tf_counter = Counter(words)
    total_words = len(words)

    result = []
    for word, count in tf_counter.items():
        tf = count
        idf = math.log(total_words / (1 + count))
        result.append({
            "word": word,
            "tf": tf,
            "idf": round(idf, 5)
        })
    return result
