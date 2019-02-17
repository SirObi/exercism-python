def is_isogram(string):
    '''Checks that each letter in string only appears once'''
    letters = string.lower().replace('-', '').replace(' ', '')
    return len(set(letters)) == len(letters)
