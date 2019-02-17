LETTER_DATA = [(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
               (['D', 'G'], 2),
               (['B', 'C', 'M', 'P'], 3),
               (['F', 'H', 'V', 'W', 'Y'], 4),
               ('K', 5),
               (['J', 'X'], 8),
               (['Q', 'Z'], 10)]


def score(word):
    letter_values = {}
    for l, v in LETTER_DATA:
        letter_values.update(dict.fromkeys(l, v))
    return sum(letter_values.get(letter, 0) for letter in word.upper())
