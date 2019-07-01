List of Python magic methods:  
https://www.python-course.eu/python3_magic_methods.php

I don't know how partial() is used in the observer_factory.

Materials on Reactive Programming:  
https://gist.github.com/staltz/868e7e9bc2a7b8c1f754

**Lessons**:  
• It makes sense to start with simple test cases and fix them first, rather than jumping at a failure for a more complex test case/use case  
• list has a `remove()` method, which you can use to delete a given object, by passing in the object itself, rather than passing an index `pop()` or `del()`  
• method overloading doesn't apply to Python, since Python can't discriminate between data types at compile time
• a Class that inherits from `ABC (Abstract Base Class)` can be made truly abstract by marking its `__init__` method with `@abstractmethod`:

```python
class Cell(ABC):
    @abstractmethod
    def __init__(self, initial_value):
        self._value = initial_value
        self.observers = []
```
