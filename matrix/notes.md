My solution was not ideal, since it needs a library (`re`).  

This solution, by Exercism user namelessjon is great, since it immediately  
transforms the string into the closest thing Python has to a matrix, which is
a nested list:  

```python
class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [[int(x) for x in line.split()] for line in matrix_string.split("\n")]
        pass

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self._matrix ]
        pass
```  

I guess the lesson from this is, whenever your code starts looking wordy,  
to ask yourself whether there exists a native data structure that can solve  
it for you.  

Also, it's worth remembering that the `str.split()` built-in method has
a useful characteristic:  
>If sep is not specified or is None:  
runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings.

This is helpful in avoiding a common pitfall (using the `' '` separator):  
`>>> [numbers.split() for numbers in '1 2 3\n4 5 6\n7 8 9\n8 7 6'.split('\n')]`  
`[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['8', '7', '6']]`  

`>>> [numbers.split(' ') for numbers in '1 2 3\n4 5 6\n7 8 9\n8 7 6'.split('\n')]`  
`[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['8', '7', '6']]`

Add some whitespaces between 1, 2 and 3:  
`>>>`[numbers.split() for numbers in '1  &nbsp; 2 &nbsp; 3\n4 5 6\n7 8 9\n8 7 6'.split('\n')]    
`[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['8', '7', '6']]`  

With the `' '` separator, you get 2 additional, non-digit items in the list:  

`>>>` [numbers.split(' ') for numbers in '1 &nbsp; 2 &nbsp; 3\n4 5 6\n7 8 9\n8 7 6'.split('\n')]  
`[['1', '', '2', '', '3'], ['4', '5', '6'], ['7', '8', '9'], ['8', '7', '6']]`
