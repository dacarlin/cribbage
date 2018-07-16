from nose.tools import assert_equal, assert_raises

from .players import WinGame, Player, RandomPlayer
from .card import Deck, hand_from_str


def test_peg():
    player = Player()
    player.peg(13)
    assert_equal(13, player.score)


def test_win():
    player = Player()
    with assert_raises(WinGame):
        player.peg(150)


# def test_random_player_play():
#     player = RandomPlayer()  # not really random!
#     player.hand = hand_from_str("Ad Ac Ah As")
#     card = player.play(previous_plays=[])
#     assert_equal(0, card.index)
