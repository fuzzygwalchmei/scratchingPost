from card_base import Playing_Card

class Deck():
    def __init__(self):
        self.deck = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['Ace','Two','Three','Four','Five','Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        scores = [1,2,3,4,5,6,7,8,9,10,10,10,10]

        for suit in suits:
            for value,score in zip(values, scores):
                self.deck.append(Playing_Card(suit, value, score))


    def shuffle(self):
        from random import randrange
        d = self.deck
        l = len(self.deck)
        for i in range(l-1, 0, -1):
            x = randrange(l)
            d[i], d[x] = d[x], d[i]

