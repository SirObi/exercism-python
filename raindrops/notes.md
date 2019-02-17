**Large numbers**  
I was wondering whether casting the number as str to get individual digits and then doing modulo over the (way smaller) sum of the digits will be faster (using the trick they taught us at primary school about a number being divisible by 3 if the sum of its digits is divisible by 3).  
The answer is: definitely not.    
```python
modulo = "'Pling' if 29842947823468436 % 3 == 0 else ''"

cast_and_sum = "'Pling' if sum(int(s) for s in str(29842947823468436)) % 3 == 0 else ''"

print("modulo:", timeit.timeit(modulo))
print("cast and sum:", timeit.timeit(cast_and_sum))
```  

```
modulo: 0.031004979999999994  
cast and sum: 4.305835275000001
```
Modulo is over 100x faster
