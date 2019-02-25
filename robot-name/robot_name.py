import random
from datetime import datetime
from string import ascii_uppercase


class Robot(object):
    def __init__(self):
        self.name = self.make_name()

    def make_name(self):
        '''Generates new name. New seed is used each time this function
        is called.'''
        random.seed(datetime.now())
        letters = (random.choice(ascii_uppercase) * 2)
        digits = (str(random.randint(0, 9)) * 3)
        return ''.join(letters + digits)

    def reset(self):
        self.name = self.make_name()
