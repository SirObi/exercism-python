from math import floor

class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = hour * 60 + minute

    def __repr__(self):
        return f"{self._turn_into_clock_time(self.hour)}:" + \
               f"{self._turn_into_clock_time(self.minute)}"

    @property
    def hour(self):
        return floor(self.minutes / 60) % 24

    @property
    def minute(self):
        return self.minutes % 60

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        self.minutes += minutes
        return str(self)

    def __sub__(self, minutes):
        self.minutes -= minutes
        return str(self)

    def _turn_into_clock_time(self, int):
        return f"{int}" if int > 9 else f"0{int}"
