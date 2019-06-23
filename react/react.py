class InputCell(object):
    def __init__(self, initial_value):
        self.value = initial_value

    def __add__(self, other):
        return self.value + other

    def __mul__(self, other):
        return self.value + other


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.value = None
        self.callbacks = []
        self.compute_and_notify(inputs, compute_function)

    def compute_and_notify(self, inputs, compute_function):
        old_value = self.value
        print("old value:", old_value)
        new_value = compute_function(inputs)
        print("new value:", new_value)
        if new_value != old_value:
            print("calling callbacks")
            self.value = new_value
            for callback in self.callbacks:
                "calling a callback"
                callback(self.value)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.pop()
