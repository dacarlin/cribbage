# coding: utf-8

from score import score, score_count
from card import Deck
import numpy as np

# game mechanincs

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
            card = current_player.ask_for_input(plays)
            if count + card < 32:
                done = True

        current_player.hand = [n for n in current_player.hand if n != card]
        print(current_player, 'hand:', current_player.hand)

        # end of turn
        turn = turn^1


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
        print("Crib:", crib)

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
