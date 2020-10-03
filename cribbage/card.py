from random import shuffle


suits = "♢♣♡♠"
suits_ascii = "dchs"
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
run_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Card:
    """
    A playing card

    Attributes
    ----------
    index: int
        Canonical playing card sorting index in the range (0, 52)

    rank: int
        Numerical rank of the card in the range (0, 13). For a graphical
        string representation, use :meth:`rank_str`

    suit: int
        Integer representation of one of four suits

    rank_str: str
        String representation of a card's rank. For example `Card(0).rank_str`
        (the rank of the Ace of Diamonds) is "A"

    value: int
        Numerical value of the card. In Cribbage, Ace is one, number
        cards are their number, and face cards all count ten

    run_val: int
        Same as value except for Jack, Queen, King, which take the
        values 11, 12, 13. Used for scoring runs

    """

    def __init__(self, index=None):
        """Create a playing card from an index in the range (0, 52)"""

        assert index in range(0, 52), "Create a card with an integer in the range (0, 52)"

        self.index: int = index

        self.rank: int  = index % 13
        self.suit: int  = index // 13

        self.value: int = vals[self.rank]
        self.run_val: int = run_vals[self.rank]
        self.rank_str: str = ranks[self.rank]
        self.ascii_str: str = f"{ranks[self.rank]}{suits_ascii[self.suit]}"

    def __repr__(self):
        return f"{ranks[self.rank]}{suits[self.suit]}"

    def __eq__(self, other):
        return self.index == other.index


class Deck:
    """Deck of cards

    Methods
    -------
    draw: iterable of :class:`cribbage.Card`
        A generator that produces :class:`cribbage.Card` objects (from a
        shuffled deck, by default)
    """

    def __init__(self, shuffled=True):
        self.cards = [Card(n) for n in range(52)]
        if shuffled:
            shuffle(self.cards)

    def draw(self, n=1):
        for i in range(n):
            yield self.cards.pop()


def card_from_str(input_str):
    """Create a Card instance from a string"""

    deck = Deck()
    cards = list(deck.draw(52))

    for card in cards:
        if card.ascii_str == input_str:
            return card

    raise ValueError(f'"{input_str}" isn\'t recognized as a card. Expected something like "Qs", "6d", "Jh"')


def hand_from_str(input_str):
    """Create a hand from a string like "Ad 2d 5d 5h 10d"

    Parameters
    ----------
    input_str: str
        A string like "Ad 2d 5d 5h 10d" specifying five cards, with the 
        turn card as the fifth card

    Returns
    -------
    hand: list of Card
        A list of four :class:`cribbage.Card` objects as specified

    turn_card: Card
        A single card
    """

    hand = list(map(card_from_str, input_str.split()))
    return hand[:-1], hand[-1]
