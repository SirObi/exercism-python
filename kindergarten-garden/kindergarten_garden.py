class Garden(object):

    DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David",
                        "Eve", "Fred", "Ginny", "Harriet",
                        "Ileana", "Joseph", "Kincaid", "Larry"]

    PLANT_LONG_NAMES = {
        "V": "Violets",
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes"
    }

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self._diagram = diagram.split('\n')
        self._students = sorted(students)

    def plants(self, name):
        pot_1 = self._students.index(name) * 2
        plant_names = (row[pot_1:pot_1 + 2] for row in self._diagram)
        return [self._plant_long_names[pn] for pn in ''.join(plant_names)]
