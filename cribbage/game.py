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

    def counting(self):

        print("Playing the counting game")

        whose_turn = {0: self.pone, 1: self.dealer}
        turn_index = 0 

        while len(self.dealer.hand) + len(self.pone.hand) > 0:
            whose_turn[turn_index].play([]) # prevoius plays is None 
            turn_index = turn_index ^ 1 # changes 0 to 1 and 1 to 0 

    def play_counting_hand(self, n):
        pass 

    def count_hands(self):
        self.pone.count_hand(self.turn_card)
        self.dealer.count_hand(self.turn_card)
        self.dealer.count_crib(self.turn_card)

    def clean_up(self):
        self.dealer.hand = []
        self.pone.hand = []


class Game:
    def __init__(self, A, B, deal=None):
        """Create a new Game object from two Player instances"""
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
