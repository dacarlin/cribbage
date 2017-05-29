import numpy as np

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

    def show_hand(self):
      print('{} {} {} {} {}'.format(self.sorted_hand()))

class NondeterministicAIPlayer(Player):
    '''
    A player who plays randomly from legal moves
    '''
    def ask_for_input(self):
        card = np.random.choice(self.hand)
        card.ontable = True
        return card
    def ask_for_discards(self):
        cards = self.hand[0:2]
        self.hand = [ n for n in self.hand if n not in cards ]
        return cards



class HumanPlayer(Player):
    def ask_for_input( self ):
        d = dict(enumerate(self.hand,1))
        discard_prompt = 'Your hand: ' + ' '.join([str(x) for x in d.values() if not x.ontable ]) + '\nChoose a card to play: '
        while 1:
            inp = input( discard_prompt )
            inp = int(inp)
            if inp in d.keys():
                card = d[inp]
                card.ontable = True
                return d[inp]

    def ask_for_discards( self ):
        d = dict(enumerate(self.sorted_hand,1))
        discard_prompt = 'Your hand: {} {} {} {} {} {}\nChoose two cards (numbered 1-6) for the crib: '.format(*d.values())
        inp = input( discard_prompt )
        cards = [ d[int(i)] for i in inp.replace(' ','') ]
        self.hand = [ n for n in self.hand if n not in cards ]
        print( 'Discarded {} {} to crib'.format(*cards) )
        return cards
