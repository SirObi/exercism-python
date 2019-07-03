def is_valid(isbn):
    if len(isbn) < 10 or (not isbn[-1].isdigit() and isbn[-1] != 'X'):
        return False

    nums, check_char = [int(c) for c in isbn[:-1:] if c.isdigit()], isbn[-1]
    if len(nums) != 9:
        return False

    nums.append(10 if check_char == 'X' else int(check_char))
    return sum(a*b for a,b in zip(nums, reversed(range(1, 11)))) % 11 == 0
