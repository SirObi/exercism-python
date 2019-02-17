Exercism user yosnoop implemented the following solution:  
```python
scores = {}
for k, v in {
            "AEIOULNRST": 1,
            "DG": 2,
            "BCMP": 3,
            "FHVWY": 4,
            "K": 5,
            "JX": 8,
            "QZ": 10
        }.items():
    scores.update({x: v for x in k})


def score(word):
    return sum([scores[char] for char in word.upper()])
```  

This looks cleaner than my solution, and more readable.  

**Lessons**:  
• a letters-only list is essentially a string, so it's better to use that built-in type right out of the gate. The additional benefit is that you can use it as a key in a dictionary (strings are hashable)  

• whenever your code starts looking ugly (see my list of tuples), it's often a sign that there's a better way to implement things  
