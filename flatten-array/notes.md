Solution by Exercism user buck-yeh:  
```python
def flatten(iterable):
    ret = []
    for i in iterable:
        if not isinstance(i, str) and hasattr(i, '__iter__'):
            ret += flatten(i)
        elif i != None:
            ret.append(i)
    return ret
```

This solution has one fewer conditional statement than mine.  

Instead using an `elif` for None, and ignoring it explicitly, we can ignore along with any other types that are not in [str, int, list].  

Solution by Exercism user hop:  
```python
from collections.abc import Iterable


def _flatten(lst):
    for item in lst:
        if item is None:
            continue
        if isinstance(item, (str, bytes)):
            yield item
        elif isinstance(item, Iterable):
            yield from flatten(item)
        else:
            yield item


def flatten(lst):
    return list(_flatten(lst))
```

It's interesting how recursion can be implemented with generators, with `yield from`.  
The second solution seems much more readable, even though it requires a bit more code.  
Then again, the question is: do we want to read shorter, but less readable code, or longer,  
but cognitively easier code?  
