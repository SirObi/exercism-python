Exercism user hilary888 used a robust, functional approach:  
```python
def is_isogram(word):
    """Determine if word is an isogram"""
    word = list(filter(str.isalpha, word.lower()))

    return len(set(word)) == len(word)
```

**Lessons**  
• the built-in `str` type has a method `isalpha`, which can be used on each character in a string in turn.  
• also see: `str.isdecimal`, `str.isdigit`, `str.isnumeric` and `str.isalnum`  
• `filter()` returns a generator
