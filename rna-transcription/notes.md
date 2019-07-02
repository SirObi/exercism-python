Solution by Exercism user `amarano` (for an older version):

```python
from string import maketrans

trans = maketrans("GCTA", "CGAU")

class DNA():

    def __init__(self, dna_string):
        self.dna_string = dna_string

    def to_rna(self):
        return self.dna_string.translate(trans)
```

Solution by Exercism user `ChrisBeaumont`(for an older version):

```python
class DNA(object):

    def __init__(self, code):
        self._code = code

    def to_rna(self):
        translate = dict(G='C', C='G', T='A', A='U')
        return ''.join(translate[char] for char in self._code)
```

In hindsight, my solution could have been something like:

```python
DNA_TO_RNA = dict(G='C', C='G', T='A', A='U')

def to_rna(dna):
    return ''.join(DNA_TO_RNA[n] for n in dna)
```

###Lessons:

**Strings**

• when translating a string to another string, you can create a translation table,  
 and pass it to a string's `translate()` method

• you can convert a list into a string by passing the list (or generator expression) to `.join()` on an empty string:

```python
obi = ''.join(['o', 'b', 'i'])
#gives 'obi'
```

**Style**  
• using `dict()` instead of `{}` allows you to create more readable one-liner dictionaries (fewer `'`s). Compare:

```python
DNA_TO_RNA = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

DNA_TO_RNA = dict(G='C', C='G', T='A', A='U')
```
