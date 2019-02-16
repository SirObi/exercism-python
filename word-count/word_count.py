import re
from collections import Counter


def word_count(phrase):
    words = re.findall(r" [a-z]+'[a-z]+ | \d | [a-z]+ ", phrase.lower(), re.X)
    return Counter(words)
