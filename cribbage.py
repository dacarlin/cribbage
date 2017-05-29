
# coding: utf-8

# In[1]:

from itertools import combinations 
from random import shuffle 
import numpy as np 
import sys


# In[22]:

display_suits = [ 's', 'h', 'c', 'd' ]
icon_suits =    [ '♠', '♡', '♣', '♢' ] 
display_ranks = [ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K' ]
vals =          [  1 , 2, 3, 4, 5, 6, 7, 8, 9, 10,  10,  10,  10 ]
map_suits = dict(zip(range(4),display_suits))
map_ranks = dict(zip(range(13),display_ranks))
map_icons = dict(zip(range(4),icon_suits))
map_vals = dict(zip(range(13),vals))

class Card:

    def __init__( self, suit, rank ):
        self.ontable = False
        self.suit = suit
        self.rank = rank 
        self.index = (13*self.suit)+self.rank
        self.display_rank = map_ranks[ self.rank ]
        self.display_suit = map_suits[ self.suit ]
        self.icon_suit = map_icons[ self.suit ] 
        self.value = map_vals[ self.rank ]
    
    def __repr__( self ):
        return '{}{}'.format( self.display_rank, self.display_suit )
    
    def __repr__(self):
        return '{}{}'.format(self.display_rank, self.icon_suit) 
    
    def __add__( self, other ):
        return self.value + other 
    
    def __radd__( self, other ):
        return self.value + other 
        
class Deck:
    
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
    


# In[23]:

deck = Deck()
deck.shuffle()


# In[24]:

sum(deck.draw(52))


# In[25]:

#plyers


# In[26]:

# players 
#######################################################

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
    def ask_for_input(self):
        card = np.random.choice(self.hand) 
        card.ontable = True 
        return card
    def ask_for_discards(self):
        cards = self.hand[0:2]
        self.hand = [ n for n in self.hand if n not in cards ] 
        return cards
    
# class NondeterministicAIPlayer(Player):
class TemplateAIPlayer(Player):
    '''
    A not very smart AI
    '''
    def ask_for_input(self, hand):
        card = np.random.choice(hand) 
        return card


# In[27]:

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


# In[28]:

# cribbage scoring 
# ai may never know this 
def score( hand ):

    points = 0
    assert len(hand) == 5

    # fifteens  
    for vector_length in [ 2, 3, 4, 5 ]:
        for vector in combinations( hand, vector_length ):
            if sum( [ card.value for card in vector ] ) == 15:
                points += 2 

    # pairs (not necessary to account for more than pairs for ==)
    for i, j in combinations( hand, 2 ):
        if i.rank == j.rank:
            points += 2 

    # runs
    for vector_len in [ 5, 4, 3 ]:
        for vec in combinations( hand, vector_len ):
            vals = [ card.value for card in vec ]
            run = [ n + min( vals ) for n in range( vector_len ) ]
            if sorted( vals ) == run:
                points += vector_len
                break
            break 
                      
    return points 


# In[29]:

def discards( players ):
    crib = []
    for player in players:            
        discards = player.ask_for_discards()
        for c in discards:
            crib.append(c) 
    return crib 

def scoring(players, turn_card):
    # goes with "score" function 
    for player in players:
        pool = player.hand + turn_card 
        player.score += score(pool) 


# In[31]:

def score_count(plays):
    '''
    Score the table, from the point of view of the last-played card
    '''
    score = 0 
    count = sum([n.value for n in plays])
    if count == 15 or count == 31:
        score = 2   
    return score 


# In[32]:

def count( players, turn ):
    n = 0
    while True:
        print('turn:', players[turn])
        turn = turn^1 
        n += 1
        if n > 10:
            break 


# In[34]:

def count( players, turn ):
    
    plays = []
    while True:
        # start of turn 
        current_player = players[turn^1]
        count = sum(plays)
        
        # state of current player 
        print('current player:', current_player)
        if len(current_player.hand) == 0:
            # no cards 
            break 
        if all([count+c>31 for c in current_player.hand]):
            # no legal play 
            print('go')
            break 
        
        # actually do the turn 
        done = None 
        while not done:
            card = current_player.ask_for_input()
            if count + card < 32:
                done = True 
        
        current_player.hand = [n for n in current_player.hand if n != card] 
        print(current_player, 'is current player', current_player.hand)
        
        # end of turn
        turn = turn^1 


# In[35]:

def game_with_gui(players):
    
    print( 'Players are:', players )
    for i, player in enumerate( players ):
        print( 'Player', i, 'is:', player )
    
    hands = 0
    while all([p.score<121 for p in players]):
        hands +=1
        print('Hand', hands)
        
        # create a fresh deck object 
        deck = Deck()
        deck.shuffle()
        
        # decide whose turn it is 
        turn = np.random.randint(2) # 0 or 1, whose crib is it? 
        print( 'Dealer is player', turn, '("{}")'.format( players[turn] ) )
        
        for player in players:
            player.hand = deck.draw(6)    

        # ask players for thier discards 
        crib = discards(players)
        
        # calculate scores (but do not assign yet)
        turn_card = deck.draw(1)
        s = [score(player.hand+turn_card) for player in players]
        crib_s = score(crib+turn_card)
        print('The turn card is', turn_card)
        
        # run the counting sub-game 
        # players get scored in-game
        count(players, turn)
        
        # "turn" card and final scoring 
        # add nibs and nobs! 
        players[turn^1].peg(s[turn^1])
        for i, player in enumerate(players):
            player.peg(s[i])
        players[turn].score += crib_s
            
        print('That is the end of hand {}'.format(hands, ))
    
    # end of game (one player has > 121 points)
    return_val = [ player.score for player in players ] 
    for player in players:
        player.clean()
    return return_val 


# In[36]:

game_with_gui([NondeterministicAIPlayer('Jeff'), NondeterministicAIPlayer('Lazarus')])


# In[ ]:



