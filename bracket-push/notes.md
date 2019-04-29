Exercism user helenst's solution:  

```python
PAIRS = dict(("{}", "()", "[]"))
OPENERS = PAIRS.keys()
CLOSERS = PAIRS.values()


def check_brackets(brackets):
    stack = []
    for char in brackets:
        if char in OPENERS:
            stack.append(char)
        elif char in CLOSERS:
            # Too many closers, or closer doesn't match expected
            if not stack or PAIRS[stack.pop()] != char:
                return False

    # Stack should be empty at the end
    return not stack
```


Lessons:  
• `dict()` can take an iterable as argument, provided that each item in the iterable
has exactly two elements  
• `len(some_list) == 0` can be also expressed as `not some_list`   
• if you have two `if` statements that both return `False`, it might be worth  
combining them with an `or`  
• maps, constants and config should be kept outside of functions  
