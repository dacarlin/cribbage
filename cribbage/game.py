from .score import score_hand, score_count
from .card import Deck
from random import choice


class Hand:
    def __init__(self, dealer, pone):
        """Create a new hand

        Parameters
        ----------
        dealer: Player
            The player who is the dealer 
        
        pone: Player
            The player who is the opponent 
        """

        self.dealer = dealer
        self.pone = pone
        self.turn_card = None
        self.turn_index = 0 
        self.turn_map = {0: self.pone, 1: self.dealer}

    def run(self):
        """Run the entire hand"""
        self.deal()
        self.discards()
        self.counting()
        self.count_hands()
        self.clean_up()

    def deal(self):
        deck = Deck()
        self.dealer.hand = deck.draw(6)
        self.pone.hand = deck.draw(6)
        self.turn_card = deck.draw(1)[0]

    def discards(self):
        d1 = self.dealer.discards()
        d2 = self.pone.discards()
        self.dealer.crib = d1 + d2

    def count_to_31(self):
        count = 0 
        plays = []
        print('count, plays', count, plays)
        card_or_none = self.turn_map[self.turn_index].play(count, plays)
        if card_or_none is not None:
            count += card_or_none
        plays.append(card_or_none) 
        self.turn_index = self.turn_index ^ 1 

    def counting(self):
        while len(self.dealer.hand) + len(self.pone.hand) > 0:
            self.count_to_31()

    def count_hands(self):
        self.pone.count_hand(self.turn_card)
        self.dealer.count_hand(self.turn_card)
        self.dealer.count_crib(self.turn_card)

    def clean_up(self):
        self.dealer.table = []
        self.pone.table = []


class Game:
    def __init__(self, A, B, deal=None):
        """Create a new Game object from two Player instances
        
        Parameters
        ----------
        A: cribbage.players.Player
            A cribbage player 
        B: cribbage.players.Player
            A cribbage player
        
        Raises
        ------
        WinGame
            When game has been won by a player 
        """
        self.A = A
        self.B = B
        if deal is None:
            self.deal = choice((0, 1))
            print("Deal is", self.deal)

    def run(self):
        while True:
            if self.deal == 0:
                hand = Hand(self.A, self.B)
                hand.run()
                self.deal = 1
            else:
                hand = Hand(self.B, self.A)
                hand.run()
                self.deal = 0
