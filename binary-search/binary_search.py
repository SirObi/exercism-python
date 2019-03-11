def binary_search(list_of_numbers, number):
    '''Searches sorted list of numbers for given number.'''
    start = 0
    end = len(list_of_numbers) - 1
    counter = 0
    while len(list_of_numbers) > 0:
        middle = (start + end) // 2
        counter += 1

        if counter > len(list_of_numbers):
            return "Too many iterations"

        if list_of_numbers[middle] == number:
            return middle

        if start == end:
            raise ValueError("Number not in array")

        if number > list_of_numbers[middle]:
            start = middle + 1
        else:
            end = middle
    raise ValueError("Number not in array")
