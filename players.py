import numpy as np
from score import score, score_count
from itertools import combinations
from card import Deck
import cython

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

    def __init__( self, name='' ):
        self.name = name
        self.hand = []
        self.score = 0

    @property
    def sorted_hand(self):
        return sorted(self.hand, key=lambda c: c.value)

    def clean( self ):
        self.hand = []
        self.score = 0

    def peg( self, points ):
        self.score += points

    def __repr__( self ):
        if len(self.name) > 0:
            return self.name
        return 'Unnamed'

class NondeterministicAIPlayer(Player):
    '''
    A player who plays randomly from legal moves
    '''
    def ask_for_input(self, play_vector):
        # ignore play vector
        card = np.random.choice(self.hand)
        card.ontable = True
        return card
    def ask_for_discards(self):
        cards = self.hand[0:2]
        self.hand = [ n for n in self.hand if n not in cards ]
        return cards

class HumanPlayer(Player):

    def show_hand(self):
      print(' '.join([str(n) for n in self.sorted_hand if not n.ontable]))

    def ask_for_input(self, play_vector):
        print('Play vector:', play_vector, '({})'.format(sum(play_vector)))

        d = dict(enumerate(self.hand,1))
        print(d)

        discard_prompt = 'Choose a card to play: '
        done = None
        while not done:
            inp = input(discard_prompt)
            if len(inp) > 0 and int(inp) in d.keys():
                card = d[int(inp)]
                print('Selected', card)
                card.ontable = True
                return card

    def ask_for_discards( self ):
        self.show_hand()
        d = dict(enumerate(self.sorted_hand,1))
        discard_prompt = 'Choose two cards (numbered 1-6) for the crib: '
        inp = input( discard_prompt )
        cards = [ d[int(i)] for i in inp.replace(' ','') ]
        self.hand = [ n for n in self.hand if n not in cards ]
        print( 'Discarded {} {} to crib'.format(*cards) )
        return cards

class AIPlayer(Player):
    '''
    AI player
    '''

    def ask_for_discards(self):
        '''
        For each possible discard,
        calculate the points of the hand
        plus calculat the points
        of the crib
        assume a random crib that
        does not contain cards in your hand
        actually, prior for cards being
        in the crib should also reflect
        what you know about the oppontent

        '''


        max_levels = 50

        print("Amy is beginning to think about discards")

        biggest_total = (-np.inf, None) #score, cards
        for i, j in combinations(self.hand, 2):
            # score my hands
            combo_score = score([n for n in self.hand if n != i and n != j])

            # bayses approach
            prior = [1 for n in range(52)] # uniform prior (not normalized yet)
            deck = Deck()
            deck.shuffle()
            deck = list(deck.draw(52))
            dist = zip(prior, deck)

            # brute force approach
            possible_scores = []
            levels = 0
            for p, q, r in combinations(deck, 3):
                levels += 1
                if levels < max_levels:
                    if p != i and q != i and r != i and p != j and q != j and r != j:
                        hand = i, j, p, q, r
                        possible_scores.append(score(hand))
            possible_scores = np.array(possible_scores)

            total = combo_score - possible_scores.mean()
            total_pkg = (total, [i,j])
            if total > biggest_total[0]:
                biggest_total = total_pkg

            print('Discarding', i, j, '=', combo_score, 'for me',
                'and {0:2.2f} ± {1:2.2f} for you'.format(possible_scores.mean(), possible_scores.std()))

        best_score, cards = biggest_total
        print("Choosing best score", best_score, "by discarding", cards)
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

        print("Amy is deciding which card to play")
        print("Play vector:", play_vector)
        cards = [n for n in self.hand if not n.ontable]
        biggest_score = (-np.inf, None)
        for i in cards:
            pool = play_vector.append(i)
            my_score = score_count(pool)
            print('Playing', i, 'gives pool', pool, 'and score', my_score )
            if my_score > biggest_score[0]:
                biggest_score = (my_score, i)

        card = i
        print("Amy choose", card)
        card.ontable = True
        return card # one card from self.hand
