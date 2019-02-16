Useful link:  
https://dbader.org/blog/python-reverse-list  

Half of my tests were failing when I used the `.reverse()` in-place method.  
After using `list(reversed(....))`, I only had one failed test.  
Food for thought.  


This can be implemented differently:
```python
def personal_top(self):
    return list(reversed(sorted(self.scores)))[:3]
```

by using a library:  
```python
from heapq import nlargest

def top(self):
  return nlargest(3, self.scores)
```

or simply realizing Python list slicing CAN solve this problem:  
```python
def top(self):
    return sorted(self.scores)[-1:-4:-1]
```  

Someone on Exercism also realized scores should be a private variable:  
```python
def __init__(self, scores):
    self._scores = scores
```
