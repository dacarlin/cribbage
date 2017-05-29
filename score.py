from itertools import combinations

# cribbage scoring
# ai may never know this
def score( hand ):

    points = 0
    #assert len(hand) == 5

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

    # all same suit

    # right jack?

    return points


def score_count(plays):
    '''
    Score a play vector
    '''

    if not plays or len(plays) < 2:
        return 0

    score = 0
    count = sum(plays)
    if count == 15 or count == 31:
        score += 2

    if plays[-1].rank == plays[-2].rank:
        score += 2
        # also implement triples!

    return score
