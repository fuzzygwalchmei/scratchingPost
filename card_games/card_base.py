class Playing_Card(object):
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def __repr__(self):
        return f'Suit: {self.suit}, Value: {self.value}, Score: {self.score}'

    def __str__(self):
        return f'This is the {self.value} of {self.suit} and its worth {self.score} points'
