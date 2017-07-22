# coding: utf-8

from itertools import combinations
from random import shuffle
import sys

class Card:
    '''
    A playing card
    '''

    suits = [ '♢', '♣', '♡', '♠']
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    def __init__(self, index):
        self.index = index
        self.ontable = False
        self.value = self.vals[index]

    def get_rank(self):
        return self.index % 13

    def get_suit(self):
        return self.index // 13

    def get_value(self):
        return

    def __repr__(self):
        rank = self.ranks[self.get_rank()]
        suit = self.suits[self.get_suit()]
        return '{}{}'.format(rank, suit)

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value + other

class Deck:
    '''
    Deck of cards
    '''

    def __init__(self, shuffled=True):
        self.cards = [Card(n) for n in range(52)]
        if shuffled:
            shuffle(self.cards)

    def draw(self, n=1):
        for i in range(n):
            yield self.cards.pop()
