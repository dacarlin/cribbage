from nose.tools import assert_equal

from .game import game
from .players import RandomPlayer

def test_game():
    p1 = RandomPlayer()
    p2 = RandomPlayer()
    scores, game_play_vector, deal, crib = game((p1, p2), gui=False)
    win_lose = [x > 120 for x in sorted(scores)]
    assert_equal([False, True], win_lose)
