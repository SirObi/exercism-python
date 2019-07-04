TO_ROMAN = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}


def roman(number):
    acc = ''
    ordered = ((k, v) for k, v in sorted(TO_ROMAN.items(), reverse=True))
    while number != 0:
        k, v = next(ordered)
        quot, number = divmod(number, k)
        acc += v * quot
    return acc
