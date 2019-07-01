import functools
from abc import ABC, abstractmethod

class CellWithOps(ABC):
    @abstractmethod
    def __init__(self, initial_value):
        self._value = initial_value

    def ops_on_cells(func):
        @functools.wraps(func)
        def wrapper_ops_on_cells(self, other, *args, **kwargs):
            if type(other) == int:
                return func(self, other, *args, **kwargs)
            elif type(other) in [InputCell, ComputeCell]:
                return func(self, other.value, *args, **kwargs)
            raise ValueError(f"Cannot perform operation on Cell and {type(other)}")
        return wrapper_ops_on_cells

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            self.notify()

    @ops_on_cells
    def __add__(self, other):
        return self.value + other

    @ops_on_cells
    def __mul__(self, other):
        return self.value * other

    @ops_on_cells
    def __sub__(self, other):
        return self.value - other

    @ops_on_cells
    def __lt__(self, other):
        return self.value < other

    @ops_on_cells
    def __gt__(self, other):
        return self.value > other


class Observable(ABC):
    @abstractmethod
    def __init__(self):
        self.observers = []

    def notify(self):
        for o in self.observers:
            o.value

    def register_observer(self, cell):
        self.observers.append(cell)


class InputCell(CellWithOps, Observable):
    def __init__(self, initial_value):
        CellWithOps.__init__(self,initial_value)
        Observable.__init__(self)


class ComputeCell(CellWithOps, Observable):
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        CellWithOps.__init__(self, compute_function(self.inputs))
        Observable.__init__(self)

        self.callbacks = []
        self.compute_function = compute_function
        for input_cell in self.inputs:
            input_cell.register_observer(self)

    @property
    def value(self):
        new_value = self.compute_function(self.inputs)
        if new_value != self._value:
            self._value = new_value
            self.notify()
        return self._value

    def notify(self):
        Observable.notify(self)
        for callback in self.callbacks:
            callback(self._value)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
