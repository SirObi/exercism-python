def is_armstrong(number):
    exp = len(str(number))
    return number == sum((int(d) ** exp for d in str(number)))
