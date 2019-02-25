Other cool solutions from Exercism:  

You can check if the whole alphabet is a subset of your phrase:
```python
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(string):
    return ALPHABET.issubset(string.lower())
```

You can also do it like so:  
```python
def is_pangram(string):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(string.lower())
```  

You can also iterate through the whole array of characters in the alphabet and see if they are all present in the phrase (you want to get an array of `True`s):  
```python
from string import ascii_lowercase

def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)
```  

I guess the lesson from this is to try and see if you can make your code:  
>1) as readable as possible  

>2) as concise as possible
