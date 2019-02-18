class Garden(object):

    _default_students = ["Alice", "Bob", "Charlie", "David",
                         "Eve", "Fred", "Ginny", "Harriet",
                         "Ileana", "Joseph", "Kincaid", "Larry"]

    _plant_long_names = {
        "V": "Violets",
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes"
    }

    def __init__(self, diagram, students=None):
        self._diagram = diagram.split('\n')
        self._students = sorted(
            students) if students else self._default_students

    def plants(self, name):
        pot_1 = self._students.index(name) * 2
        plant_names = (row[pot_1:pot_1 + 2] for row in self._diagram)
        return [self._plant_long_names[pn] for pn in ''.join(plant_names)]
