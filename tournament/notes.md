### Lessons:

**Strings**

• `str.ljust(width)` is the equivalent of `zfill` for padding string with spaces

• it's not possible to use f-strings as templates (`f'{} something {}'`) - this will throw an error.  
The alternative is to use `string.Template`, and then call `.substitute()` on it

**Dictionaries**

• the `key` keyword argument of `sorted()` needs to be a function. This can be a lambda, e.g.:

```python
sorted(dictionaries.items(), key=lambda k: k[1]['pts'])  
```

for sorting a list of dictionaries by values in a nested dictionary.
