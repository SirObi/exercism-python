def binary_search(list_of_numbers, number):
    """Searches sorted list of numbers for given number."""
    if len(list_of_numbers) <= 0:
        raise ValueError("Empty array")

    start = 0
    end = len(list_of_numbers) - 1

    while start <= end:
        middle = (start + end) // 2

        if list_of_numbers[middle] == number:
            return middle
            
        if number > list_of_numbers[middle]:
            start = middle + 1
        else:
            end = middle - 1
    raise ValueError("Number not in array")
