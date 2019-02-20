
My initial solution for `plants` function, not very readable:
```Python
def plants(self, name):
    pot_1 = self._students.index(name) * 2
    pots = [pot_1, pot_1 + 1]
    plant_names = (self._diagram[row][pot] for row in range(
        len(self._diagram)) for pot in pots)
    return [self._plant_long_names[f] for f in plant_names]
```

New solution:
```Python
def plants(self, name):
    pot_1 = self._students.index(name) * 2
    plant_names = (row[pot_1:pot_1 + 2] for row in self._diagram)
    return [self._plant_long_names[pn] for pn in ''.join(plant_names)]
```  

Another solution, by Exercism user mariazverina:  
```Python
class Garden:
	STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
		'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

	FLOWERS = {'C': 'Clover', 'R': 'Radishes',
		'G': 'Grass', 'V': 'Violets'}

	def __init__(self, garden, students=STUDENTS):
		garden = garden.split()
		flowers = zip(*[iter(garden[0])]*2 + [iter(garden[1])]*2)
		self.pots = dict(zip(sorted(students), flowers))

	def plants(self, who):
		return map(self.FLOWERS.get, self.pots[who])
  ```

This is an awesome solution, which uses 4 iterators to build a dictionary mapping each student to his/her list of flowers.  
The only drawback is that it's not easily extendable to a case where there are >2 rows of flowers.  

(For clarity, the plants function seems to return a map, which makes the tests fail. It should probably read something like:  
  `return [self.FLOWERS.get(f) for f in self.pots[who]]`)

Lessons:  
• class variable names should have been capitalized  
• `split()` will split a string on any whitespace - you don't have to specify which kind of whitespace it is (space character, newline character etc.)  
• `zip()` returns an iterator, not a list of tuples    
• `zip()` requires arguments that support iteration  
• `zip()` can be used to combine several iterators into a group of iterators that yield in the same call
