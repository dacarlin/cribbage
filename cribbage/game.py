from .score import score, score_count
from .card import Deck
from random import choice

def discards(players):
    crib = []
    for player in players:
        discards = player.ask_for_discards()
        for c in discards:
            crib.append(c)
    return crib

def count(players, turn, debug=False, gui=True):
    '''
    The counting game. Two loops.
    Inner loop is us counting to 31,
    outer loop runs until we run out of cards
    '''

    counting_vector = [] # to keep track of all plays for training RL model
    game_over = False # this is for if we win during counting
    while True:

        plays = []
        while True:
            # we are couting to 31
            current_player = players[turn^1]
            if gui and debug:
                print('Current player:', current_player)

            count = sum(plays)

            # state of current player
            if count == 31:
                # the previous player has made the count 31
                # we can't play on this, just break
                break

            current_cards = [n for n in current_player.hand if not n.ontable]
            if len(current_cards) == 0:
                # no cards
                if gui and debug:
                    print('Current player has no cards')
                turn = turn^1
                break

            pools = [count+c>31 for c in [n for n in current_player.hand if not n.ontable]]
            if all(pools):
                # no legal play
                if gui:
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
            s = score_count(plays)
            current_player.peg(s)
            if current_player.score > 120:
                game_over = True
            turn = turn^1

            if gui:
                print("Player {} played {} (count: {}, points: {})".format(current_player, card, count+card, s))

            if debug and gui:
                print("Score for the play is", s, "to", current_player)

        # do we still have cards?
        # if so, we want to keep going
        if all([len([n for n in player.hand if not n.ontable]) < 1 for player in players]):
            # no players have cards
            break

        # otherwise, continue to another game of counting to 31
        counting_vector.append(plays)

    # this is the level of the original while True
    if debug:
        print('Counting vector:', counting_vector)

    # return counting vector for training RL model
    return counting_vector

def game(players, debug=False, gui=True):

    turn = choice((0, 1))
    if gui:
        print('Welcome to cribbage')
        for i, player in enumerate(players):
            if i == turn:
                print('Player {}: {} (dealer)'.format(i+1, player))
            else:
                print('Player {}: {}'.format(i+1, player))

    game_play_vector = []
    hands = 0
    while all([p.score<121 for p in players]):
        hands +=1
        if gui:
            print('>>> Begin hand', hands)
            #print('Dealer is player', turn, '("{}")'.format( players[turn]))

        # create a fresh deck object
        deck = Deck()

        deal = []
        for player in players:
            player.hand = list(deck.draw(6)) # since it returns generator
            deal += player.hand

        # ask players for thier discards
        crib = discards(players)
        if gui and debug:
            print("Crib:", crib)

        # calculate scores (but do not assign yet)
        turn_card = next(deck.draw(1))
        if gui:
            print('>>> The turn card is', turn_card)

        # run the counting sub-game
        # players get scored in-game
        counting_vector = count(players, turn, debug=debug, gui=gui)
        #if gui:
        #    print("Scores after counting", [p.score for p in players])

        # "turn" card and final scoring
        # add nibs and nobs!

        if gui:
            print('>>> End of hand {}'.format(hands))
        for i, player in enumerate(players):
            my_score = score(player.hand + [turn_card])
            player.peg(my_score)
            if gui:
                print('{}: {} {} {} {} + {} ({})'.format(player, *player.sorted_hand, turn_card, my_score))
            if i == turn: # it's my crib
                crib_score = score(crib + [turn_card])
                player.peg(crib_score)
                if gui:
                    print('Crib ({}): {} {} {} {} + {} ({})'.format(player, *crib, turn_card, crib_score))

        turn =  turn^1
        if gui:
            print('>>> The scores are {} {} and {} {}'.format(players[0], players[0].score, players[1], players[1].score))
        game_play_vector += counting_vector

    # end of game (one player has > 121 points)
    scores = [player.score for player in players]
    for player in players:
        player.clean()
    return scores, game_play_vector, deal, crib 


# the game will eventually also be OO

class Game:
    '''
    A game object
    '''

    def __init__(self, players):
        self.players = players
        self.turn = 0
        self.final_score = None
        self.score = (0, 0)

    @property
    def player_whose_turn_it_is():
        self.players[self.turn]
