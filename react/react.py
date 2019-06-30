class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value
        self.observers = []

    def __add__(self, other):
        return self.value + other

    def __mul__(self, other):
        return self.value * other

    def __sub__(self, other):
        print(f"subtracting {other} from {self.value}")
        return self.value - other

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def register_observer(self, cell):
        print("Input cell registering observer")
        self.observers.append(cell)
        print("Input cell observers are", self.observers)


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        print("Current input value is", self.value)
        print("Setting new input value", new_value)
        if self._value != new_value:
            self._value = new_value
            print("calling callbacks")
            self.notify()

    def notify(self):
        print("Notifying observers of input cell")
        for o in self.observers:
            print(type(o))
            print("calling a callback in input cell")
            o.value

    # def register_observer(self, cell):
    #     self.observers.append(cell)
    # and add a setter?




class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.observers = []
        for input_cell in self.inputs:
            input_cell.register_observer(self)
        self.compute_function = compute_function
        self._value = compute_function(self.inputs)
        self.callbacks = []

    def __add__(self, other):
        if type(other) is not int:
            return self.value + other.value
        return self.value + other

    def __mul__(self, other):
        if type(other) is not int:
            return self.value * other.value
        return self.value * other

    def __sub__(self, other):
        if type(other) is not int:
            return self.value - other.value
        print(f"subtracting {other} from {self.value}")
        return self.value - other

    def __lt__(self, other):
        if type(other) is not int:
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if type(other) is not int:
            return self.value > other
        return self.value > other

    @property
    def value(self):
        new_value = self.compute_function(self.inputs)
        if new_value != self._value:
            self._value = new_value
            print("Compute cell value is", self._value)
            self.notify()
        return self._value

    @value.setter
    def value(self, new_value):
        print("setting value")
        if self._value != new_value:
            self._value = new_value
            print("calling callbacks output cell")
            self.notify()

    def notify(self):
        print("notify called")
        for callback in self.callbacks:
            print("calling a callback in output cell")
            callback(self._value)
        for o in self.observers:
            o.value

    def register_observer(self, cell):
        print(f"Output cell with value {self._value} registering observer")
        self.observers.append(cell)
        print("Output cell observers are", self.observers)

    def add_callback(self, callback):
        print("adding callback")
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
