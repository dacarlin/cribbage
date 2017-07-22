from cribbage.players import EnumerativeAIPlayer
from cribbage.card import Card, Deck
from cribbage.score import score
import unittest

class TestCards(unittest.TestCase):

    def test_a_card(self):
        card = Card(0)
        # this will be Ace of Diamonds
        self.assertEqual(card.__str__(), 'A♢')

    def test_scoring(self):
        deck = Deck()
        cards = list(deck.draw(5))
        # a score of 19 is not possible in cribbage 
        self.assertNotEqual(19, score(cards))

class TestDeck(unittest.TestCase):

    deck = Deck()
    cards = list(deck.draw(52))

    def test_draw(self):
        for n in range(1, 12):
            deck = Deck()
            cards = list(deck.draw(n))
            self.assertEqual(len(cards), n)

if __name__ == '__main__':
    unittest.main()
