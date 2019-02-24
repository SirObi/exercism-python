class School(object):
    def __init__(self):
        self._roster = {}

    def add_student(self, name=str, grade=int):
        self._roster[str(grade)] = self._roster.get(str(grade), []) + [name]

    def roster(self):
        return [nm for g in sorted(self._roster.keys()) for nm in self.grade(g)]

    def grade(self, grade_number):
        return sorted(self._roster.get(str(grade_number), []))
