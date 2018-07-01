from nose.tools import assert_equal

from .card import Card, Deck, card_from_str


def test_card():
    card = Card(0)
    # this will be Ace of Diamonds
    assert_equal(str(card), 'A♢')

def test_draw():
    for n in range(1, 12):
        deck = Deck()
        cards = list(deck.draw(n))
        assert_equal(len(cards), n)

def test_card_from_str():
    s = 'Ks' # ace of diamonds 
    card = card_from_str(s)
    assert_equal('Ks', card.ascii_str)
