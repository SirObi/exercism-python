import re


def abbreviate(words):
    '''Finds all words in a string, builds acronym from their first letters'''
    return ''.join([w[0].upper() for w in re.findall(r'[a-zA-Z\']+', words)])
