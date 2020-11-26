import pytest 

from .players import WinGame, Player, EnumerativeAIPlayer, StudentAIPlayer, RandomPlayer
from .game import Hand
from .card import cards_from_str


def test_peg():
    player = Player()
    player.peg(13)
    assert 13 == player.score


def test_win():
    player = Player()
    with pytest.raises(WinGame):
        player.peg(150)


@pytest.mark.slow
def test_enumerative_ai_chooses_good_crib():
    player = EnumerativeAIPlayer()
    player.hand = cards_from_str("5d 5h Ad 3s 7h 9s")
    discards = player.ask_for_discards(my_crib=True)
    assert all(x.value == 5 for x in discards)


@pytest.mark.slow
def test_enumerative_ai_chooses_bad_crib():
    player = EnumerativeAIPlayer()
    player.hand = cards_from_str("5d 5h Ad 3s 8h 9s")
    discards = player.ask_for_discards(my_crib=False)
    assert all(x.value != 5 for x in discards)


def test_enumerative_ai_counting():
    a = EnumerativeAIPlayer()
    b = RandomPlayer()
    a.hand = cards_from_str("Ad Ac 6d 9d")
    b.hand = cards_from_str("Ah As 6c 9c")
    hand = Hand(b, a)
    hand.counting()


def test_student_chooses_good_crib():
    player = StudentAIPlayer()
    player.hand = cards_from_str("5d 5h Ad 3s 7h 9s")
    discards = player.ask_for_discards()
    assert all(x.rank == 5 for x in discards)

