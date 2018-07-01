from nose.tools import assert_equal

from .card import Card, Deck, card_from_str, hand_from_str


def test_card():
    card = Card(0)
    # this will be Ace of Diamonds
    assert_equal(str(card), "A♢")


def test_draw():
    for n in range(1, 12):
        deck = Deck()
        cards = list(deck.draw(n))
        assert_equal(len(cards), n)


def test_card_from_str():
    s = "Ks"  # ace of diamonds
    card = card_from_str(s)
    assert_equal("Ks", card.ascii_str)


def test_hand_from_str():
    s = "Ad Ac Ah As 10s"
    values = [1, 1, 1, 1, 10]
    hand, turn_card = hand_from_str(s)
    cards = hand + [turn_card]
    for expect, card in zip(values, cards):
        yield assert_equal, expect, card.value
