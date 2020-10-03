from itertools import combinations


def score_hand(hand, turn_card, is_crib=False):
    """Score a valid cribbage hand
    
    Parameters
    ----------
    hand: list of cribbage.Card
        Exactly four cards forming a hand 
        
    turn_card: cribbage.Card
        The turn card 
    """

    if len(hand) != 4:
        raise ValueError(
            "To score a hand, it must have 4 cards, not {}".format(len(hand))
        )

    points = 0
    points += score_fifteens(hand, turn_card)
    points += score_sets(hand, turn_card)
    points += score_runs(hand, turn_card)
    points += score_flush_and_right_jack(hand, turn_card)

    return points


def score_fifteens(hand, turn_card):
    points = 0
    for vector_length in [2, 3, 4, 5]:
        for vector in combinations(hand + [turn_card], vector_length):
            if sum(x.value for x in vector) == 15:
                points += 2

    return points


def score_flush_and_right_jack(hand, turn_card):

    points = 0
    suits = []
    suits.append(turn_card.suit)
    for card in hand:
        suits.append(card.suit)
        if card.rank_str == "J" and card.suit == turn_card.suit:
            # the right jack
            points += 1

    # flush
    if len(set(suits)) == 1:
        points += 5

    return points


def score_sets(hand, turn_card):
    points = 0
    # pairs (not necessary to account for more than pairs for ==)
    for i, j in combinations(hand + [turn_card], 2):
        if i.rank == j.rank:
            points += 2

    return points


def score_runs(hand, turn_card):
    points = 0
    for vector_len in [5, 4, 3]:
        for vec in combinations(hand + [turn_card], vector_len):
            vals = [card.run_val for card in vec]
            run = [n + min(vals) for n in range(vector_len)]
            if sorted(vals) == run:
                points += vector_len
                break
        if points > 0:
            break
    
    return points


def score_count(plays):
    """Score a play vector"""

    score = 0
    if not plays or len(plays) < 2:
        return score

    count = sum(plays)
    if count == 15 or count == 31:
        score += 2

    if plays[-1].rank == plays[-2].rank:
        score += 2
    if len(plays) > 2 and plays[-2].rank == plays[-3].rank:
        score += 4
        # hack? or does that actually make sense?

    return score
