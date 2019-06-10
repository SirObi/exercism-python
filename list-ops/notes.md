I wasn't sure what foldl and foldr stand for or what they do.  

Lessons:  
• `reversed()` actually gives you a `<list_reverseiterator object>`, not a list  
• folding is an functional programming pattern similar to reducing  
• it requires an operation, accumulated (starting) value and a data structure to fold (array, tree etc)  
• it can be a fold (random order), left fold (starting from beginning of data structure) or right fold (starts from end)  

This article explains folding in general:  
Exploring Folds: A Powerful Pattern Of Functional Programming  
https://link.medium.com/zHuIDWqdSW  

---

Interesting solution by Exercism user `hop`:  

```python
from functools import wraps


def listify(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return list(f(*args, **kwargs))
    return wrapper


@listify
def map_clone(f, a):
    while a:
        x, *a = a
        yield f(x)


def length(a):
    def inc(n, _):
        return n+1
    return foldl(inc, a, 0)


@listify
def filter_clone(f, a):
    while a:
        x, *a = a
        if f(x):
            yield x


@listify
def reverse(a):
    while a:
        *a, x = a
        yield x


@listify
def append(a, x):
    yield from a
    yield x


def foldl(f, a, z):
    while a:
        x, *a = a
        z = f(z, x)
    return z


def foldr(f, a, z):
    while a:
        *a, x = a
        z = f(x, z)
    return z


@listify
def flat(a):
    while a:
        x, *a = a
        if isinstance(x, list):
            yield from flat(x)
        else:
            yield x


@listify
def concat(a, b):
    yield from a
    if b:
        yield from b
```  
The `@listify` wrapper deals with the fact that the functions above all return generators (turns them back into lists, as expected by the tests).  

Lessons:  
• `yield from` takes an iterable and turns it into a generator  
• `x, *a = a` is valid syntax

Let's say `obi = [1, 2, 3, 4, 5]`  
`*obi2 = obi` will result in
> SyntaxError: starred assignment target must be in a list or tuple  

`*obi2,  = obi` is fine! (it will just essentially make a copy of `obi`)  

This comes from PEP 3132 -- Extended Iterable Unpacking.   
> This PEP proposes a change to iterable unpacking syntax, allowing to specify a "catch-all" name which will be assigned a list of all items not assigned to a "regular" name.

```python
>>> a, *b, c = range(5)
>>> a
0
>>> c
4
>>> b
[1, 2, 3]
```  

>Rationale
Many algorithms require splitting a sequence in a "first, rest" pair. With the new syntax,

```python
>first, rest = seq[0], seq[1:]
```

>is replaced by the cleaner and probably more efficient:

```python
first, *rest = seq
```

This syntax can be also used to pop values from end or beginning of a list, or, effectively, to iterate through a list:
```python
@listify
def filter_clone(f, a):
    while a:
        x, *a = a
        if f(x):
            yield x
```  
The question remains whether this is Pythonic (i.e. easily understandable to the majority of Python users).  
