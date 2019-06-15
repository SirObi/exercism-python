Solution by Exercism user `aeriksson`
```
def leap_year(x):
    return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)
```

Lessons:  
• Whenever you see the following syntax:  
```python
if ...:
    return True
return False
```
you can try to go for a one-liner.  
The opportunity for refactoring becomes evident if you look at: 
```Python
if True:
  return True
return False
```
