from score import score, score_count
from card import Deck
import numpy as np

def discards( players ):
    crib = []
    for player in players:
        discards = player.ask_for_discards()
        for c in discards:
            crib.append(c)
    return crib

def count( players, turn ):
    '''
    The counting game. Two loops. Inner loop is us counting to 31,
    outer loop runs until we run out of cards
    '''

    while True:
        # we are in counting phase

        plays = []
        while True:
            # we are couting to 31
            current_player = players[turn^1]
            count = sum(plays)

            # state of current player
            if count == 31:
                break
            print('current player:', current_player)
            if len([n for n in current_player.hand if not n.ontable]) == 0:
                # no cards
                print('Current player has no cards')
                turn = turn^1
                break
            if all([count+c>31 for c in [n for n in current_player.hand if not n.ontable]]):
                # no legal play
                print('Current player has no legal move: "Go!"')
                turn = turn^1
                break

            # actually do the turn
            done = None
            while not done:
                card = current_player.ask_for_input(plays)
                if count + card < 32:
                    card.ontable = True
                    done = True

            plays.append(card)
            print("Player {} played {} ({})".format( current_player, card, count+card))
            s = score_count(plays)
            print("Score for the play is", s, "to", current_player)
            current_player.peg(s)

            turn = turn^1

        # do we still have cards?
        # if so, we want to keep going
        if all([len([n for n in player.hand if not n.ontable]) < 1 for player in players]):
            # no players have cards
            break

        # otherwise, continue to another game of counting to 31

def scoring(players, turn_card):
    # goes with "score" function
    for player in players:
        pool = player.hand + turn_card
        player.score += score(pool)

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
        print("Scores after counting", [(player, player.score) for player in players])

        # "turn" card and final scoring
        # add nibs and nobs!
        players[turn^1].peg(s[turn^1])
        for i, player in enumerate(players):
            player.peg(s[i])
        players[turn].score += crib_s

        print('That is the end of hand {}'.format(hands, ))
        print("Scores after hands", [(player, player.score) for player in players])

    # end of game (one player has > 121 points)
    return_val = [ player.score for player in players ]
    for player in players:
        player.clean()
    return return_val
