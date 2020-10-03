import pytest 

from .card import Card, Deck, card_from_str, hand_from_str


def test_card():
    card = Card(0) # this will be Ad (ace of diamonds)
    assert "A♢" == str(card)

def test_adding_cards_adds_values():
    a = Card(0)  # Ad
    b = Card(10) # Jd
    assert 11 == a.value + b.value

def test_draw():
    deck = Deck()
    cards = list(deck.draw(12))
    assert 12 == len(cards)

def test_card_from_str():
    s = "Ks"  # ace of diamonds
    card = card_from_str(s)
    assert "Ks" == card.ascii_str
    assert 12 == card.rank
    assert 3 == card.suit

def test_hand_from_str():
    s = "Ad Ac Ah As 10s"
    values = [1, 1, 1, 1, 10]
    hand, turn_card = hand_from_str(s)
    cards = hand + [turn_card]
    for expect, card in zip(values, cards):
        assert expect == card.value

def test_hand_from_bad_str():
    with pytest.raises(ValueError):
        _ = hand_from_str("Jh 5d 5c 5p 5h")