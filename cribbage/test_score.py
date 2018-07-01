from nose.tools import assert_equal, assert_raises

from .card import Card, Deck 
from .score import score_hand, score_runs

def test_score_runs():
    deck = Deck()
    hand = list(deck.draw(4))
    turn_card = list(deck.draw(1))[0]
    # that's Ad 2d 3d 4d | 5d 
    # should be a 5-card run worth 5 points 
    assert_equal(5, score_runs(hand, turn_card))
    
def test_score_raises_error_on_wrong_number_of_cards():
    deck = Deck()
    hand = list(deck.draw(3))
    turn_card = list(deck.draw(1))[0]
    with assert_raises(ValueError):
        score_hand(hand, turn_card)

def test_score_of_a_hand():
    deck = Deck(shuffled=False)
    hand = list(deck.draw(4))
    turn_card = list(deck.draw(1))[0]

    for c in hand + [turn_card]:
        print(c)

    # K♠
    # Q♠
    # J♠
    # 10♠

    # 9♠ (turn)

    # run of 5 for 5 
    # plus the flush for 5 
    # plus the right jack for 1 
    # for a total of 11 points 
    assert_equal(11, score_hand(hand, turn_card))

def test_right_jack():
    deck = Deck(shuffled=False)
    hand = list(deck.draw(5))

    #turn_card = list(deck.draw(1))[0]    

def test_score_of_another_hand():
    deck = Deck()
    hand = list(deck.draw(13))


# from itertools import combinations

# def score(hand, turn_card):
#     '''Scores a four-card hand plus a turn card
    
#     Parameters
#     ----------
#     hand: list of cribbage.Card
#         Exactly four cards forming a hand 
        
#     turn_card: cribbage.Card
#         The turn card 
#     '''

#     points = 0

#     suits = []
#     suits.append(str(turn_card[1]))
#     for card in hand:
#         suits.append(str(card)[1])
#         if str(card)[0] == 'J' and str(card)[1] == str(turn_card)[1]:
#             # the right jack
#             points += 1 
#     if len(set(suits)) == 1:
#         points += 5 

#     # fifteens
#     for vector_length in [2, 3, 4, 5]:
#         for vector in combinations(hand + [turn_card], vector_length):
#             if sum(vector) == 15:
#                 points += 2

#     # pairs (not necessary to account for more than pairs for ==)
#     for i, j in combinations(hand + [turn_card], 2):
#         if i.get_rank() == j.get_rank():
#             points += 2

#     # runs
#     for vector_len in [ 5, 4, 3 ]:
#         for vec in combinations(hand + [turn_card], vector_len):
#             vals = [card.value for card in vec]
#             run = [n + min(vals) for n in range(vector_len)]
#             if sorted(ggvals) == run:
#                 points += vector_len
#                 break
#             break

#     return points

# def score_count(plays):
#     '''Score a play vector'''
    
#     score = 0

#     if not plays or len(plays) < 2:
#         return score

#     count = sum(plays)
#     if count == 15 or count == 31:
#         score += 2

#     if plays[-1].get_rank() == plays[-2].get_rank():
#         score += 2
#         # also implement triples!

#     return score
