class School(object):
    def __init__(self):
        self._roster = {}

    def add_student(self, name: str, grade: int):
        '''Add student name under corresponding grade. Dict keys are grades'''
        self._roster[str(grade)] = self._roster.get(str(grade), []) + [name]

    def roster(self):
        '''Return list of students, order first by grade, then by name'''
        return [nm for g in sorted(self._roster.keys()) for nm in self.grade(g)]

    def grade(self, grade_number: int):
        '''Return list of students sorted alphabetically given grade'''
        return sorted(self._roster.get(str(grade_number), []))
