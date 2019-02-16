class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return list(reversed(sorted(self.scores)))[:3]

    def report(self):
        difference = self.latest() - self.personal_best()
        comparison = "That's your personal best!" if difference >= 0 else \
            f"That's {-difference} short of your personal best!"
        message = f"Your latest score was {self.latest()}. "
        return message + comparison
