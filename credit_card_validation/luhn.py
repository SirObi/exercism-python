class Luhn(object):
    def __init__(self, card_num):
        if all(d.isnumeric() or d.isspace() for d in card_num):
            self._card_num_digits = [int(d) for d in card_num if d.isnumeric()]
            self._card_num_to_double = self._card_num_digits[-2::-2]
            self._card_num_no_double = self._card_num_digits[-1::-2]

    def is_valid(self):
        '''See README for Luhn algorithm details. This method uses a shortcut
        where indices in idx_to_luhn array correspond to target values. '''
        if hasattr(self, '_card_num_digits') and len(self._card_num_digits) > 1:
            idx_to_luhn = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
            doubled = sum(idx_to_luhn[d] for d in self._card_num_to_double)
            no_doubled = sum((self._card_num_no_double))
            return (doubled + no_doubled) % 10 == 0
        return False
