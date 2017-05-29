# coding: utf-8

from itertools import combinations
from random import shuffle
import numpy as np
import sys

display_suits = [ 's', 'h', 'c', 'd' ]
icon_suits =    [ '♠', '♡', '♣', '♢' ]
display_ranks = [ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K' ]
vals =          [  1 , 2, 3, 4, 5, 6, 7, 8, 9, 10,  10,  10,  10 ]
map_suits =     dict(zip(range(4),display_suits))
map_ranks =     dict(zip(range(13),display_ranks))
map_icons =     dict(zip(range(4),icon_suits))
map_vals =      dict(zip(range(13),vals))

class Card:
    '''
    A class for a playing card
    '''

    def __init__( self, suit, rank ):
        self.ontable = False
        self.suit = suit
        self.rank = rank
        self.index = (13*self.suit)+self.rank
        self.display_rank = map_ranks[ self.rank ]
        self.display_suit = map_suits[ self.suit ]
        self.icon_suit = map_icons[ self.suit ]
        self.value = map_vals[ self.rank ]

    #def __repr__( self ):
    #    return '{}{}'.format( self.display_rank, self.display_suit )

    def __repr__(self):
        return '{}{}'.format(self.display_rank, self.icon_suit)

    def __add__( self, other ):
        return self.value + other

    def __radd__( self, other ):
        return self.value + other

class Deck:
    '''
    Deck of cards

    Methods:

    deck.shuffle() -> None
        Shuffles the deck

    deck.draw(n=1) -> [Card, ]
        Returns iterable of card objects drawn from the top of the deck

    '''

    def __init__( self ):
        self.cards = []
        for s in range( 4 ):
            for r in range( 13 ):
                self.cards.append(Card(s, r))

    def shuffle( self ):
        shuffle( self.cards )

    def draw( self, n=1 ):
        result = []
        for i in range( n or 1 ):
            result.append( self.cards.pop() )
        return result


# this converts into a test!
#deck = Deck()
#deck.shuffle()
#sum(deck.draw(52))
