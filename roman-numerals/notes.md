A clean, readable example of how the data can be presented (Exercism user `mmakaay`):

```Python
roman_numbers = (
    ( 'M',  1000 ), ( 'CM',  900 ),
    ( 'D',   500 ), ( 'CD',  400 ),
    ( 'C',   100 ), ( 'XC',   90 ),
    ( 'L',    50 ), ( 'XL',   40 ),
    ( 'X',    10 ), ( 'IX',    9 ),
    ( 'V',     5 ), ( 'IV',    4 ),
    ( 'I',     1 )
)
```

Spans more lines, but requires much less horizontal eye movement as opposed to my arrangement:

```Python
TO_ROMAN = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
```

It also, highlights the special cases (4, 9 etc.) in a separate column, additionally  
reducing cognitive load.

### Lessons

**General programming**

• a `while` loop can be used instead of recursion, f.x. when you're looping through more than one iterable  
at a time

**Strings**:

• appending to a list and then `"".join(somelist)` is usually the more efficient, recommended way of accumulating a string.

This is because strings are immutable, so each `+=` creates a copy of the string.  
This works fine (is even faster) for small strings, so it's fine in this exercise, but in general it should be avoided.
