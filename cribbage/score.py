from itertools import combinations

def score(hand):
    '''
    Scores an unordered group of cards
    '''

    points = 0

    # fifteens
    for vector_length in [2, 3, 4, 5]:
        for vector in combinations(hand, vector_length):
            if sum(vector) == 15:
                points += 2

    # pairs (not necessary to account for more than pairs for ==)
    for i, j in combinations(hand, 2):
        if i.get_rank() == j.get_rank():
            points += 2

    # runs
    for vector_len in [ 5, 4, 3 ]:
        for vec in combinations(hand, vector_len):
            vals = [ card.value for card in vec ]
            run = [ n + min( vals ) for n in range( vector_len ) ]
            if sorted( vals ) == run:
                points += vector_len
                break
            break

    return points

def score_count(plays):
    '''Score a play vector'''
    
    score = 0

    if not plays or len(plays) < 2:
        return score

    count = sum(plays)
    if count == 15 or count == 31:
        score += 2

    if plays[-1].get_rank() == plays[-2].get_rank():
        score += 2
        # also implement triples!

    return score
