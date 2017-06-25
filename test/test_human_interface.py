from cribbage.players import EnumerativeAIPlayer
from cribbage.card import Card, Deck
from cribbage.score import score
import unittest


class TestHumanInterface(unittest.TestCase):

    deck = Deck()
    cards = list(deck.draw(10))

    def test_cards(self):

        for card in self.cards:
            print(card.get_rank(), card.get_suit())

    def test_scoring(self):


        print('score:', score(self.cards))

        self.assertTrue(True)


