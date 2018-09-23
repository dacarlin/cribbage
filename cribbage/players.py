from itertools import combinations
from random import choice
import numpy as np
from tqdm import tqdm

from .score import score_hand, score_count
from .card import Deck

# Here we define the classes for the various kinds of players
# in the cribbage game. To define your own player, inherit from
# the Player class and implement "ask_for_input" and "ask_for_discards"


class WinGame(Exception):
    pass


class Player:
    """
    Base class for a cribbage player
    """

    def __init__(self, name=None):
        self.name = name
        self.hand = []  # cards in player's hand
        self.table = []  # cards on table in front of player
        self.crib = []  # cards in player's crib
        self.score = 0

    # Discards

    def ask_for_discards():
        """Should return two cards from the player"""
        raise Exception("You need to implement `ask_for_discards` yourself")


    def update_after_discards(self, discards):
        for discard in discards:
            self.hand.remove(discard)


    def discards(self):
        cards = self.ask_for_discards()
        self.update_after_discards(cards)
        return cards


    # Counting plays

    def ask_for_play(self):
        """Should return a single card from the player

        Private method"""
        raise Exception("You need to implement `ask_for_play` yourself")


    def update_after_play(self, play):
        """Private method"""
        # Mark the card
        self.table.append(play)
        self.hand.remove(play)


    def play(self, count, previous_plays):
        """Public method"""
        if all(count + card > 31 for card in self.hand):
            # say "Go"
            return None 
        while True:
            card = self.ask_for_play(previous_plays)  # need to implement this
            print("Nominated card", card)
            if sum(previous_plays) + card.value < 32:
                self.update_after_play(card)
                return card


    # Scoring

    def peg(self, points):
        self.score += points
        if self.score > 121:
            self.win_game()


    def count_hand(self, turn_card):
        """Count the hand (which should be on the table)"""
        score = score_hand(self.table, turn_card)
        self.peg(score)
        return score 


    def count_crib(self, turn_card):
        """Count crib, with side effect of pegging the score"""
        score = score_hand(self.crib, turn_card)
        self.peg(score)
        return score 


    def win_game(self):
        raise WinGame("Game was won by {}".format(self))


    @property
    def sorted_hand(self):
        return sorted(self.hand, key=lambda c: c.index)

    def __repr__(self):
        if self.name:
            return self.name
        return str(self.__class__)


class RandomPlayer(Player):
    """
    A player who plays randomly from legal moves
    """


    def ask_for_play(self, previous_plays):
        return self.hand[0]


    def ask_for_discards(self):
        return self.hand[0:2]


class HumanPlayer(Player):
    """
    A human player 
    """

    def ask_for_play(self, previous_plays):
        """
        Ask a human for a card, in the counting phase
        """

        # First, print out the play vector and our options
        d = dict(enumerate(self.hand, 1))
        print("Plays (count):", previous_plays, "({})".format(sum(previous_plays)))
        print("Your hand:", " ".join([str(c) for c in self.hand]))

        # Let us nominate a card
        while True:
            inp = input("Card number to play: ") or "1"
            if len(inp) > 0 and int(inp) in d.keys():
                card = d[int(inp)]
                return card

    def ask_for_discards(self):
        """After deal, ask a human for a card"""

        print(self.sorted_hand)
        d = dict(enumerate(self.sorted_hand, 1))
        discard_prompt = "Type two numbers followed by <Enter>, for example 16<Enter> to discard the first and the sixth (last) card: "
        while True:
            inp = input(discard_prompt) or "12"
            cards = [d[int(i)] for i in inp.replace(" ", "").replace(",", "")]
            if len(cards) == 2:
                print("Chose {} {} for crib".format(*cards))
                return cards


class EnumerativeAIPlayer(Player):
    """
    "Expert systems" style AI player that systematically
    enumerates possible moves and chooses the move that
    maximizes its score after the move
    """

    def ask_for_discards(self):
        """
        For each possible discard, score and select
        highest scoring move
        """

        print("{} is choosing discards ...".format(self))
        deck = Deck().draw(52)
        potential_cards = [n for n in deck if n not in self.hand]
        bar = tqdm(total=227700)
        discards = []
        mean_scores = []
        for discard in combinations(self.hand, 2):  # 6 choose 2 == 15
            inner_scores = []
            for pot in combinations(potential_cards, 3):  # 46 choose 3 == 15,180
                inner_scores.append(score_hand([*discard, *pot[:-1]], pot[-1]))
                bar.update(1)
            inner_scores = np.array(inner_scores)
            discards.append(discard)
            mean_scores.append(inner_scores.mean())
        max_index = np.argmax(mean_scores)
        return discards[max_index]

    def ask_for_input(self, play_vector):
        """
        Calculate points for each possible play in your hand
        and choose the one that maximizes the points
        """

        scores = []
        plays = []
        for card in self.hand:
            plays.append(card)
            scores.append(score_count(play_vector + [card]))
        max_index = np.argmax(scores)
        return plays[max_index]


# class TrainedAIPlayer(Player):
#     """
#     A player that makes choices based on previous games
#     """

#     def __init__(self, name=""):
#         # override this constructor becasue I want to
#         # load the ML model in when we init AIPlayer instance
#         self.name = name
#         self.hand = []
#         self.score = 0
#         self.debug = False
#         self.model = load_trained_model()  # trained model we can ask directly for plays

#     def ask_for_input(self, play_vector):
#         card = self.model.ask_for_pegging_play(play_vector, self.in_hand)
#         card.ontable = True
#         return card

#     def ask_for_discards(self):
#         cards = self.model.ask_model_for_discard(
#             self.hand
#         )  # note: returns card objects
#         self.hand = [n for n in self.hand if n not in cards]
#         return cards


NondeterministicAIPlayer = RandomPlayer
