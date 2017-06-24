from .players import EnumerativeAIPlayer
from .card import Card, Deck
from .score import score
import unittest


class TestCards(unittest.TestCase):

    deck = Deck()
    cards = list(deck.draw(10))

    def test_cards(self):

        for card in self.cards:
            print(card.get_rank(), card.get_suit())

    def test_scoring(self):


        print('score:', score(self.cards))

        self.assertTrue(True)


class TestDeck(unittest.TestCase):

    deck = Deck()
    cards = list(deck.draw(52))

    def test_drawing(self):

        ply = EnumerativeAIPlayer()

        self.assertTrue(True)


class TestPlayers(unittest.TestCase):

    deck = Deck()
    # print(list(deck.draw(10)))

    def test_enumerative_ai_player(self):


        ply = EnumerativeAIPlayer()

        self.assertTrue(True)


class MyEasyTestCase(unittest.TestCase):

    values = ['cat', 'dog']

    def test_my_test(self):
        '''testy test'''

        for n, val in enumerate(self.values):
            result = 2 + 2
            self.assertEqual(result, 4)
            # har de har har

    def test_my_testy_test(self):
        '''testy test 2'''

        self.assertEqual(self.values[0], 'cat')
        # har de har har

if __name__ == '__main__':
    unittest.main()
