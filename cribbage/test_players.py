from nose.tools import assert_equal

from .players import Player
from .card import Deck


def test_remove_card_from_hand():

    deck = Deck(shuffled=False) 
    player = Player() 
    player.hand = deck.draw(6)
    player.hand.remove(player.hand[0])

    assert_equal(5, len(player.hand))