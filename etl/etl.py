def transform(legacy_data):
    '''Moves data to new format with letters as keys, and scores as values'''
    return {letter.lower(): score for (score, letters) in legacy_data.items()
            for letter in legacy_data[score]}
