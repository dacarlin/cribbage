import numpy as np
from .score import score, score_count
from itertools import combinations
from .card import Deck
from .ai import load_trained_model

# here we define the classes for the various kinds of players
# in the cribbage game

# to define your own player
# inherit from the Player class
# and implement "ask_for_input"
# and "ask_for_discards"

class Player():

    '''
    Base class for a cribbage player
    '''

    def __init__(self, name=''):
        self.name = name
        self.hand = []
        self.score = 0
        self.debug = False

    def check_debug(debug):
        if debug:
            self.debug = True

    @property
    def sorted_hand(self):
        return sorted(self.hand, key=lambda c: c.value)

    @property
    def in_hand(self):
        'Cards in my hand that are not on the table'
        return [card for card in self.hand if not card.ontable]

    def clean( self ):
        self.hand = []
        self.score = 0

    def peg( self, points ):
        self.score += points

    def __repr__(self):
        if self.name:
            return self.name
        return str(self.__class__)


class NondeterministicAIPlayer(Player):
    '''
    A player who plays randomly from legal moves
    '''

    def ask_for_input(self, play_vector):
        card = np.random.choice(self.in_hand)
        card.ontable = True
        return card

    def ask_for_discards(self):
        cards = self.hand[0:2]
        self.hand = [n for n in self.hand if n not in cards]
        return cards

class HumanPlayer(Player):

    def ask_for_input(self, play_vector):
        '''
        Ask a human for a card, in the counting phase
        '''

        print('Play vector:', play_vector, '({})'.format(sum(play_vector)))
        count = sum(play_vector)
        d = dict(enumerate(self.in_hand,1))
        print(d)

        discard_prompt = 'Choose a card to play: '
        while 1:
            inp = input(discard_prompt)
            if len(inp) > 0 and int(inp) in d.keys():
                card = d[int(inp)]
                if count + card < 31:
                    card.ontable = True
                    return card

    def ask_for_discards( self ):
        '''After deal, ask a human for a card'''

        print(self.sorted_hand)
        d = dict(enumerate(self.sorted_hand,1))
        discard_prompt = 'Choose two cards (numbered 1-6) for the crib: '
        while True:
            inp = input(discard_prompt) or '12'
            cards = [d[int(i)] for i in inp.replace(' ','')]
            if len(cards) == 2:
                self.hand = [ n for n in self.hand if n not in cards ]
                print('Discarded {} {} to crib'.format(*cards))
                return cards

class EnumerativeAIPlayer(Player):
    '''
    "Expert systems" style AI player that systematically
    enumerates possible moves and chooses the move that
    maximizes its score after the move
    '''

    def ask_for_discards(self):
        '''
        For each possible discard, score and select
        highest scoring move
        '''

        max_levels = 1000
        possible = 10000
        #print("Amy is deciding on discard with thoroughness {}/1.0".format(max_levels/possible))

        biggest_total = (-np.inf, None) #score, cards
        for i, j in combinations(self.hand, 2):

            # score my hands
            pot_hand = [n for n in self.hand if n != i and n != j]
            indexes = [n.index for n in pot_hand]
            combo_score = score(pot_hand)

            # brute force approach
            deck = Deck()
            deck = [n for n in deck.draw(52) if n.index not in indexes]
            levels = 0
            possible_scores = []
            for pot_three in combinations(deck, 3):
                levels += 1
                if levels < max_levels:
                    hand = pot_hand + list(pot_three)
                    possible_scores.append(score(hand))
            possible_scores = np.array(possible_scores)
            total = combo_score - possible_scores.mean()
            total_pkg = (total, [i,j])
            if total > biggest_total[0]:
                biggest_total = total_pkg

            #print('Discarding', i, j, '=', combo_score, 'for me',
            #    'and {0:2.2f} ± {1:2.2f} for you'.format(possible_scores.mean(), possible_scores.std()))

        best_score, cards = biggest_total
        #print("Choosing best score", best_score, "by discarding", cards)
        self.hand = [n for n in self.hand if n != i and n != j]
        return cards # two cards from self.hand

    def ask_for_input(self, play_vector):
        '''
        decide which card to play
        based on play vector
        calculate points for each
        possible play in your hand
        and choose the one that maximizes the points
        '''

        #print("Amy is deciding which card to play")
        #print("Play vector:", play_vector)
        cards = [n for n in self.hand if not n.ontable]
        #print("Cards:", cards)
        biggest_score = (-np.inf, None)
        for card in cards:
            pool = play_vector + [card]
            cnt = sum(pool)
            my_score = score_count(pool)
            #print('Playing', card, 'gives pool', pool, 'count', cnt, 'and score', my_score )
            if my_score > biggest_score[0]:
                biggest_score = (my_score, card)

        card = biggest_score[1]
        #print("Amy choose", card)
        card.ontable = True
        return card # one card from self.hand

class AIPlayer(Player):
    '''
    A player that makes choices based on previous games it
    has "played" represented by "game vectors"
    '''

    def __init__(self):
        self.model = load_trained_model()
        # trained model we can ask directly for plays

    def ask_for_input(self, play_vector):
        card = self.model.ask_for_pegging_play(play_vector, self.hand)
        card.ontable = True
        return card

    def ask_for_discards(self):
        cards = self.model.ask_for_discards(self.hand) # note: returns card objects
        self.hand = [n for n in self.hand if n not in cards]
        return cards
