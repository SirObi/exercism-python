Another, slightly more pithy solution (by Exercism user pilino1234):  

```python
def distance(strand1, strand2):
    return sum(i != j for i, j in zip(strand1, strand2))
```  

**Lessons**:  
• using this: `a, b` tuple notation seems pretty safe  

• when passing a list comprehension to another function (like `sum()`), square brackets are not necessary - **you can instead use a generator expression**  

>Generator expressions are best used when the list is an intermediary, such as summing the results, or creating a dict out of the results.  

They are also great for infinitely long lists.  

More on that:  
https://djangostars.com/blog/list-comprehensions-and-generator-expressions/  
https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension

• it's worth remembering `True` has an integer value of 1 in Python. This: `True - 1` is actually a valid statement which evaluates to 0.  
