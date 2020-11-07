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


        