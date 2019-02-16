import re


class Matrix(object):
    '''Turns a string representation of a matrix into an object with rows and
    columns'''

    def __init__(self, matrix_string):
        self._matrix_string = matrix_string
        # _numbers stores an array of strings, like ['1', '2', '3']
        self._numbers = re.findall(r'\d+', self._matrix_string)
        self._nrows = matrix_string.count('\n') + 1
        self._ncolumns = len(self._numbers) // self._nrows

    def row(self, index):
        '''Return row given row index. Index starts with 1, not 0!'''
        index = index - 1
        start = index * self._ncolumns
        row_strings = self._numbers[start: start + self._ncolumns]
        return [int(s) for s in row_strings]

    def column(self, index):
        '''Return column given column index. Index starts with 1, not 0!'''
        index = index - 1
        start = index
        col_strings = self._numbers[start:len(self._numbers):self._ncolumns]
        return [int(s) for s in col_strings]
