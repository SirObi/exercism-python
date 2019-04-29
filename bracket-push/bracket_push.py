def is_paired(input):
    open_to_close_map = {'{': '}', '(': ')', '[': ']'}
    only_brackets = [
        a for a in input if a in open_to_close_map.keys() + open_to_close_map.values()]

    stack = []
    for index, char in enumerate(only_brackets):
        if char in open_to_close_map.keys():
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            current_last_open_bracket = stack[-1]
            if char == open_to_close_map[current_last_open_bracket]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
