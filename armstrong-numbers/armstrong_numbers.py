def is_armstrong(number):
    exp = len(str(number))
    return number == sum((int(digit) ** exp for digit in str(number)))
