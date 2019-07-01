Some Exercism users add a default argument value `''`.

```python
def reverse(text=''):
    return text[::-1]
```

Solution by Exercism user `visitvinoth`:

```python
def reverse(input=''):
    output = ''
    for c in input:
      output = c + output
    return output
```

Appending is prepending in reverse!
