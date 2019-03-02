Without the `re` module, the solution is much less clean:  
```python
def abbreviate(words):
    return ''.join([word[0].upper() for word in words.replace('-', ' ')
                    .replace('_', ' ')
                    .split(' ')
                    if word != ''])
```

Also, this solution feels brittle - imagine adding more complex use cases.  

**Lessons**  
• RegEx is difficult, but it can often make code much cleaner and easier to  
modify
