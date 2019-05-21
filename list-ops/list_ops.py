def append(xs, ys):
    return xs + ys


def concat(lists):
    concatenated = []
    for item in lists:
        if type(item) == list:
            for i in item:
                concatenated.append(i)
        else:
            concatenated.append(item)
    return concatenated


def filter_clone(function, xs):
    return [s for s in xs if function(s)]


def length(xs):
    return len(xs)


def map_clone(function, xs):
    return [function(s) for s in xs]


def foldl(function, xs, acc):
    if len(xs) == 0:
        return acc
    for s in xs:
        acc = function(acc, s)
    return acc


def foldr(function, xs, acc):
    if len(xs) == 0:
        return acc
    for s in reversed(xs):
        acc = function(s, acc)
    return acc


def reverse(xs):
    return [*reversed(xs)]
