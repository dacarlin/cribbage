import pytest 

from .players import WinGame, Player, RandomPlayer
from .card import Deck, hand_from_str


def test_peg():
    player = Player()
    player.peg(13)
    assert 13 == player.score


def test_win():
    player = Player()
    with pytest.raises(WinGame):
        player.peg(150)
        