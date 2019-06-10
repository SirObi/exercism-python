My original solution:

```Python
def binary_search(list_of_numbers, number):
    '''Searches sorted list of numbers for given number.'''
    start = 0
    end = len(list_of_numbers) - 1
    counter = 0
    while len(list_of_numbers) > 0:
        middle = (start + end) // 2
        counter += 1

        if counter > len(list_of_numbers):
            return "Too many iterations"

        if list_of_numbers[middle] == number:
            return middle

        if start == end:
            raise ValueError("Number not in array")

        if number > list_of_numbers[middle]:
            start = middle + 1
        else:
            end = middle
    raise ValueError("Number not in array")
```

There are several issues with this approach:  
1. The `while` condition is quite dangerous.  
It seems I originally intended to keep cutting the array in half and reassigning  
the new array to `list_of_numbers`.  
When `len(list_of_numbers)` the loop would end.  

Clearly I forgot to change the condition when I decided to manipulate indices  
instead.  

2. The `Too many iterations` check - this was an ugly fix necessitated by a  
logical error in this statement:  
```Python
else:
    end = middle
    # should have been end = middle + 1
```  
It might be worth noting that this was probably caused by the CS reality of the 5th element  
having the index of 4, 4th element having the index of 3 and 1st element having the index of 0.  
It pays to be extra careful when thinking in terms of indices.  

3. Minor, but the names `start` and `end` don't mean much to a person reading  
the code for the first time. `left_index` and `right_index` arguably make the code  
easier to parse for a human.  
It's nice to be succinct, but if it makes it harder for another person to read the code,  
it's clearly not great for everyone's productivity and flow.  
