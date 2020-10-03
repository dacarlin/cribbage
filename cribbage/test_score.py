import pytest

from .card import Card, Deck, card_from_str, hand_from_str
from .score import (
    score_hand,
    score_runs,
    score_fifteens,
    score_sets,
    score_flush_and_right_jack,
)


def test_score_fifteens():
    cases = [(4, "Ad 2d 5d 5h 10d"), (0, "Ad As Ac Ah 5s")]
    for expected, hand_str in cases:
        hand, turn_card = hand_from_str(hand_str)
        score = score_fifteens(hand, turn_card)
        assert expected == score


def test_score_sets():
    cases = [(2, "Ad 2d 3d 4d 4h"), (6, "Ad 2d 4d 4h 4s")]
    for expected, hand_str in cases:
        hand, turn_card = hand_from_str(hand_str)
        score = score_sets(hand, turn_card)
        assert expected == score


def test_score_runs():
    deck = Deck(shuffled=False)
    hand = list(deck.draw(4))
    turn_card = list(deck.draw(1))[0]
    # that's Ad 2d 3d 4d | 5d
    # should be a 5-card run worth 5 points
    assert 5 == score_runs(hand, turn_card)


def test_score_raises_error_on_wrong_number_of_cards():
    deck = Deck()
    hand = list(deck.draw(3))
    turn_card = list(deck.draw(1))[0]
    with pytest.raises(ValueError):
        score_hand(hand, turn_card)


def test_score_of_a_hand():
    deck = Deck(shuffled=False)
    hand = list(deck.draw(4))
    turn_card = list(deck.draw(1))[0]

    for c in hand + [turn_card]:
        print(c)

    # K♠
    # Q♠
    # J♠
    # 10♠

    # 9♠ (turn)

    # run of 5 for 5
    # plus the flush for 5
    # plus the right jack for 1
    # for a total of 11 points
    assert 11 == score_hand(hand, turn_card)


def test_right_jack():
    hand, turn_card = hand_from_str("As Ac Ah Jd Ad")
    assert 1 == score_flush_and_right_jack(hand, turn_card) 


def test_perfect_hand():
    hand, turn_card = hand_from_str("Jh 5d 5c 5s 5h")
    assert 29 == score_hand(hand, turn_card)
