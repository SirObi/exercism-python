def flatten(iterable):
    flattened = []
    for o in iterable:
        if type(o) in [int, str]:
            flattened.append(o)
        elif isinstance(o, type(None)):
            pass
        else:
            flattened = flattened + flatten(o)
    return flattened
