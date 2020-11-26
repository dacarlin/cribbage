import pytest 

from .game import Hand, Game
from .players import RandomPlayer, WinGame


def test_deal():
    dealer = RandomPlayer()
    pone = RandomPlayer()
    hand = Hand(dealer, pone)

    hand.deal()

    cases = [(6, dealer), (6, pone)]
    for expected, player in cases:
        assert expected == len(player.hand)


def test_discards():
    dealer = RandomPlayer()
    pone = RandomPlayer()
    hand = Hand(dealer, pone)

    hand.deal()
    hand.discards()

    cases = [(4, dealer), (4, pone)]
    for expected, player in cases:
        assert expected == len(player.hand)


def test_counting():
    dealer = RandomPlayer()
    pone = RandomPlayer()
    hand = Hand(dealer, pone)

    hand.deal()
    hand.discards()

    cases = [(4, dealer), (4, pone)]

    for expected, player in cases:
        assert expected == len(player.hand)

    hand.counting()

    cases = [(0, dealer), (0, pone)]

    for expected, player in cases:
        assert expected == len(player.hand)

    cases = [(4, dealer), (4, pone)]

    for expected, player in cases:
        assert expected == len(player.table)


def test_count_hands():
    dealer = RandomPlayer()
    pone = RandomPlayer()
    hand = Hand(dealer, pone)

    hand.deal()
    hand.discards()
    hand.counting()
    hand.count_hands()

    cases = [(4, dealer), (4, pone)]

    for expected, player in cases:
        assert expected == len(player.table)

    cases = [(4, dealer), (0, pone)]

    for expected, player in cases:
        assert expected == len(player.crib)


@pytest.mark.parametrize('n', range(50))
def test_single_hand(n):
    dealer = RandomPlayer()
    pone = RandomPlayer()
    hand = Hand(dealer, pone)
    hand.run()

    cases = [
        (0, dealer), 
        (0, pone), 
    ]

    for expected, player in cases:
        assert expected == len(player.hand)


def test_single_game():
    dealer = RandomPlayer()
    pone = RandomPlayer()
    game = Game(dealer, pone)
    
    with pytest.raises(WinGame):
        game.run()


@pytest.mark.parametrize('n', range(10))
def test_many_games(n):
    dealer = RandomPlayer()
    pone = RandomPlayer()
    game = Game(dealer, pone)

    with pytest.raises(WinGame):
        game.run()
