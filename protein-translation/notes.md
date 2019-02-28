How does the following line work?:  
```python
next_codon = zip(*[iter(strand)] * 3)
```

In Python, it's possible to extend a list-type container with an `* int`.  
Examples:  

```python
>>>print("hey" *3)  
heyheyhey


def obi3(sth):
  print(sth)

>>>obi3("hey" *3)
heyheyhey

>>>obi3([0]*3)
[0, 0, 0]
```

In this case, we're extending a list with 1 iterator to a list of 3 iterators.  
Placing `*` before the list unpacks it, so the whole expression now looks like:  
```python
zip(iter(strand), iter(strand), iter(strand))
```  

The syntax above is just more compact and arguably nicer to use.


Solution by Exercism user dhefner:  
```python
def proteins(strand):
    proteins = []
    codonMap = {
        'AUG':'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        }

    for i in range(0,len(strand),3):
        codon = strand[i:i+3]
        if codon in codonMap:
            proteins.append(codonMap[codon])
        else:
            break

    return proteins
```
This is probably the most "correct" solution to the problem.  

**Lessons**:  
• range() can be passed a step. If the sequence is divisible by 3, using a step of 3 + list slicing is a very good solution.  
• `dict`s support the `if` a `in` b syntax  
