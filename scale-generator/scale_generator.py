class Scale(object):
    _chromatic_scale = {
        "chromatic_as_sharps": ['A', 'A#', 'B', 'C', 'C#',
                             'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        "chromatic_as_flats": ['A', 'Bb', 'B', 'C', 'Db',
                            'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']}
    _starting_pitches = {
        "for_sharps": ['G', 'D', 'A', 'E', 'B',
                         'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#'],
        "for_flats": ['F', 'Bb', 'Eb', 'Ab',
                        'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb'],
        "no_sharps_or_flats": ['C', 'a']}
    _intervals = {'m': 1, 'M': 2, 'A': 3}

    def __init__(self, tonic):
        if Scale._is_valid_tonic_note(tonic):
            self.tonic_note = Scale._find_note_on_chromatic_scale(tonic)
            self.notation = Scale._get_notation(tonic)
        else:
            raise Exception("Invalid tonic note")


    @staticmethod
    def _is_valid_tonic_note(tonic_note):
        return tonic_note in sum(Scale._starting_pitches.values(), [])


    @staticmethod
    def _find_note_on_chromatic_scale(tonic):
        return tonic[0].upper() + tonic[1] if len(tonic) == 2 else tonic.upper()


    @staticmethod
    def _get_notation(tonic_note):
        notation = None
        starting_pitches = Scale._starting_pitches
        if tonic_note in starting_pitches["for_sharps"] + starting_pitches["no_sharps_or_flats"]:
            notation = Scale._chromatic_scale["chromatic_as_sharps"]
        elif tonic_note in starting_pitches["for_flats"]:
            notation = Scale._chromatic_scale["chromatic_as_flats"]
        return notation


    def chromatic(self):
        """Returns a chromatic scale"""
        tonic = self.notation.index(self.tonic_note)
        scale = self.notation[tonic:] + self.notation[:tonic]
        return scale

    def interval(self, intervals):
        """Returns scale given intervals. Ignores last interval."""
        current = self.notation.index(self.tonic_note)
        pitches = [self.tonic_note]
        for i in intervals:
            current = current + Scale._intervals[i]
            pitches.append(self.notation[current % 12])
        return pitches[:-1]
