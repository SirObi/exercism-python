I was getting nowhere trying to use both minutes an hours.
Debbuging and reasoning was difficult, which was reflected in development time.

I also made some logical errors due to the cognitive effort of using two different, non-decimal units.

```python
from math import floor

class Clock(object):
    def __init__(self, hour, minute):
        self.hour = abs((hour + floor(minute / 60)) % 24)
        self.minute = minute % 60

    def __str__(self):
        return f"{self._turn_into_clock_time(self.hour)}:" + \
               f"{self._turn_into_clock_time(self.minute)}"

    def __eq__(self, other):
        return self.__str__ == other

    def __add__(self, minutes):
        self.hour = abs((self.hour + floor(self.minute + minutes / 60)) % 24)
        self.minute = (self.minute + minutes) % 60
        return self.__str__()

    def __sub__(self, minutes):
        self.hour = abs((self.hour - floor(self.minute - minutes / 60)) % 24)
        self.minute = (self.minute - minutes) % 60
        return self.__str__()

    def _turn_into_clock_time(self, int):
        return f"{int}" if int > 9 else f"0{int}"
```

---

Trying to use **str** to represent an object led to maximum recursion error when eq was called  
between two `Clock`s.

---

Alternative ways of formatting string:

Add necessary zeroes `zfill` (Exercism user `jennelba`):

```python
str(self.hour).zfill(2) + ':' + str(self.minute).zfill(2)
```

Using `.format` and supplying required format (user `sm1th`):

```python
"{:02d}:{:02d}".format(self.hrs, self.mins)
```

---

To get hours and minutes separately, you can also use the "better" version of modulo (`%`) - `divmod` (user `sm1th`):

```python
hours, self.mins = divmod(mins, 60)
```

###Lessons:

**OOP**

• using `__repr__` to represent an object is better than modifying its `__str__`

**General programming**:

• tracking the same value with two different counters (e.g. hours and minutes) is a bad idea and can slow  
down development

• `divmod` is a function which gives you both the quotient and remainder, whereas `%` only gives you the remainder
