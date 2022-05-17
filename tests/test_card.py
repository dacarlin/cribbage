import pytest

from cribbage.card import Card, Deck, card_from_str, cards_from_str


def test_card():
    card = Card(0)  # this will be Ad (ace of diamonds)
    assert "A♢" == str(card)


def test_adding_cards_adds_values():
    a = Card(0)  # Ad
    b = Card(10)  # Jd
    assert 11 == a.value + b.value


def test_draw():
    deck = Deck()
    cards = list(deck.draw(12))
    assert 12 == len(cards)


def test_card_from_str():
    card = card_from_str("Ks")
    assert "Ks" == card.ascii_str
    assert 12 == card.rank
    assert 3 == card.suit


def test_hand_from_str():
    s = "Ad Ac Ah As 10s"
    values = [1, 1, 1, 1, 10]
    cards = cards_from_str(s)
    for expect, card in zip(values, cards):
        assert expect == card.value


def test_hand_from_bad_str():
    with pytest.raises(ValueError):
        cards_from_str("Jh 5d 5c 5p 5h")
