def raindrops(number):
    '''Given a number outputs corresponding word in raindrop-speak'''
    output = "Pling" if number % 3 == 0 else ""
    output += "Plang" if number % 5 == 0 else ""
    output += "Plong" if number % 7 == 0 else ""
    return output if len(output) > 0 else str(number)
