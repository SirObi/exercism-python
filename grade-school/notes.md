My previous solutions:

```python
class School(object):
   def __init__(self):
       self._roster = []
   ...
```  
This started out using the wrong data structure for the problem.  
Essentially, I wanted a map from grade number to list of student names.  
Even though using a Python list may be tempting (indexes in an array are ints, and so are grade numbers), it would create additional overhead, such as:  
• creating a number of empty buckets, such so the indexes in list match up to the grades (imagine the school has no pupils in Grade 2 - things become ugly)  
• inserting new grades ('2a', '2b') is inefficient, since we're using an array  

Therefore a hash map is a more flexible, more efficient solution.  

 Next solution
 ```python
 return sum([self.grade(g) for g in sorted(self._roster.keys())], [])
 ```  

 Using `sum()` to flatten the list is fancy, but inefficient.  
 It's better to use a nested list comprehension (the syntax may be slightly unintuitive here).  

 Here's a solution to an old version of the problem, by Exercism user georgemarshall:  

```python
from collections import defaultdict
from typing import Callable, Dict, Iterable, Iterator, Set, Tuple, cast


class School:
    def __init__(self, name: str) -> None:
        self.db = defaultdict(
            cast(Callable[[], Set[str]], set)
        )  # type: Dict[int, Set[str]]

    def add(self, name: str, grade: int) -> None:
        self.db[grade].add(name)

    def grade(self, grade: int) -> Set[str]:
        return self.db[grade]

    def sort(self) -> Iterator[Tuple[int, Iterable[str]]]:
        for grade in sorted(self.db):
            yield grade, tuple(sorted(self.db[grade]))
```  

The solution no longer works for the current set of unit tests.  
However, it's interesting to see how adding types to Python:  
• makes the code faster to read and parse by a human
• forces the programmer to think through the code more deeply ("Which type do I use?")  


**Lessons**:  
• nested list comprehensions are easy to write if you remember the following rule of ordering:  

```python
# Good, ole' 'for' loops
parent_list = [[1, 2], [6, 1]]

result = []
for sublist in parent_list:  
  for digit in sublist:  
    result.append(digit)

# Thinking through the same thing with list comprehension, step by step
result = []
result = [for sublist in parent_list]
result = [for sublist in parent_list for digit in sublist]
result = [digit for sublist in parent_list for digit in sublist]

```  
In other words: the ordering is the same as with for loops, it's just the return value goes at the front in the comprehension.  

Inspired by this SO post:  
https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
