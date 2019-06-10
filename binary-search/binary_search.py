def binary_search(list_of_numbers, number):
    """Searches sorted list of numbers for given number."""
    if len(list_of_numbers) <= 0:
        raise ValueError("Empty array")

    left_index = 0
    right_index = len(list_of_numbers) - 1

    while left_index <= right_index:
        middle = (left_index + right_index) // 2

        if list_of_numbers[middle] == number:
            return middle

        if number > list_of_numbers[middle]:
            left_index = middle + 1
        else:
            right_index = middle - 1
    raise ValueError("Number not in array")
