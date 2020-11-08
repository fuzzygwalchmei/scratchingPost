import card_base
import deck_base
import pytest

def test_Playing_Card():
    card = card_base.Playing_Card('Heart','Six', 6)
    assert card.suit == 'Heart'
    print(card)

def test_deck_base():
    my_deck = deck_base.Deck()
    assert len(my_deck.deck) == 52

def test_deck_shuffle():
    a = deck_base.Deck()
    
    assert a != a.shuffle()