import functools
from abc import ABC

class Cell(ABC):
    def __init__(self, initial_value):
        self._value = initial_value
        self.observers = []

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


class InputCell(Cell):
    def register_observer(self, cell):
        self.observers.append(cell)

    def notify(self):
        for o in self.observers:
            o.value


class ComputeCell(Cell):
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.observers = []
        self.callbacks = []
        for input_cell in self.inputs:
            input_cell.register_observer(self)
        self.compute_function = compute_function
        self._value = compute_function(self.inputs)

    @property
    def value(self):
        new_value = self.compute_function(self.inputs)
        if new_value != self._value:
            self._value = new_value
            self.notify()
        return self._value

    def notify(self):
        for callback in self.callbacks:
            callback(self._value)
        for o in self.observers:
            o.value

    def register_observer(self, cell):
        self.observers.append(cell)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
