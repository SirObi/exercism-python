WHOLE_ALPHABET = set('abcdefghijklmnopqrstuvwxyz')


def is_pangram(sentence):
    '''Compares the set of all letters in a sentence to the set of all letters
    in the alphabet'''
    letters_in_common = set(sentence.lower()).intersection(WHOLE_ALPHABET)
    return len(letters_in_common) == len(WHOLE_ALPHABET)
