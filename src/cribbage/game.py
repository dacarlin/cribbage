from random import choice

from rich import print

from cribbage.card import Deck
from cribbage.score import score_count


class Hand:
    def __init__(self, dealer, pone):
        """
        Create a new hand

        Parameters
        ----------
        dealer: cribbage.Player
            The player who is the dealer
        pone: cribbage.Player
            The player who is the opponent
        """

        self.dealer = dealer
        self.pone = pone
        self.turn_card = None
        self.turn_index = 0
        self.turn_map = {0: self.pone, 1: self.dealer}
        self.plays = []
        self.count = None

    def run(self):
        """Run the entire hand"""

        from rich.console import Console

        console = Console()

        print("cribbage: Beginning a [bold green]new hand[/bold green]")
        print(f"cribbage: {self.dealer} is the dealer for this hand")
        print(f"cribbage: {self.pone} is the opponent for this hand")
        print("cribbage: Shuffling cards")
        with console.status("cribbage: Shuffling cards ...") as status:
            from time import sleep
            sleep(2.5)
        print("cribbage: Dealing cards")
        print("cribbage: Each player was dealt 6 cards")
        self.deal()
        print("cribbage: Each player must now discard 2 cards into the crib")
        print(f"cribbage: The crib belongs to {self.dealer}")
        self.discards()
        print(f"cribbage: The crib for {self.dealer} is 4 cards") 

        print(f"cribbage: {self.pone} will cut the deck for turn card") 
        print(f"cribbage: {self.dealer} turned over the turn card {self.turn_card}")
        print(f"cribbage: The turn card for this hard is {self.turn_card}")
        if self.turn_card.rank == 10:
            print(f"cribbage: The turn card is a Jack! {self.turn_card}")
            print(f"cribbage: {self.dealer} pegs 2 points for his heels for {self.turn_card}")
            self.dealer.peg(2)
        print(f"cribbage: Beginning a [bold green]new counting round")
        self.counting()
        print(f"cribbage: Finished pegging")
        print(f"cribbage: Now it's time to count hands")
        print(f"cribbage: {self.pone} will count first")
        print(f"cribbage: {self.dealer} will count last")
        self.count_hands()
        print(f"cribbage: Finished counting hands")
        self.clean_up()

    def deal(self):
        """Create a new deck and deal cards to players"""
        deck = Deck()
        self.dealer.hand = list(deck.draw(6))
        self.pone.hand = list(deck.draw(6))
        self.turn_card = next(deck.draw(1))

    def discards(self):
        """Get discards from both players and add them to crib"""
        d1 = self.dealer.discards()
        d2 = self.pone.discards()
        self.dealer.crib = d1 + d2

    def count_to_31(self):
        """Starting with two players with at least one card between them,
        and a count of 0, start the counting portion of the game given
        information about who"""
        if not self.dealer.hand:
            print("dealer has no cards")
        if not self.pone.hand:
            print("pone has no cards")

        count = 0
        turn = 0  # index of whose turn it is
        plays = []
        done = None
        go_has_been_said = False

        while not done:
            print("counting:", plays, count)

            # player whose turn it is plays
            player = self.turn_map[turn]
            my_play = player.play(count, plays)  # can be `"Go!"` or a card object

            if isinstance(my_play, str):
                if go_has_been_said:
                    print('"Go!" has already been said, so starting a new count at 0')
                    done = True
                    count = 0
                    break

                print('that"s a "go", switching turns')
                go_has_been_said = True
            else:
                print(player, "played", my_play)
                count += my_play.value
                plays.append(my_play)
                # score the play
                score = score_count(plays)
                player.peg(score)
                print(f"{player} pegged {score} points for {plays}")
                # needs a rework of `score_hand` to accept < 4 cards and no turn card
                if count == 31:
                    print("counted to 31, point for", player)
                    player.peg(1)
                    done = True
                    count = 0

            turn = turn ^ 1

    def counting(self):
        print(f"cribbage: Counting starts with {self.pone}")
        while len(self.dealer.hand) + len(self.pone.hand) > 0:
            self.count_to_31()

    def count_hands(self):
        print("Counting hands")

        _ = self.pone.count_hand(self.turn_card)
        print("pone", self.pone, self.pone.table, _)

        _ = self.dealer.count_hand(self.turn_card)
        print("dealer", self.dealer, self.dealer.table, _)

        _ = self.dealer.count_crib(self.turn_card)
        print("crib", self.dealer, self.dealer.crib, _)

    def clean_up(self):
        self.dealer.table = []
        self.pone.table = []


class Game:
    """The game object

    Examples
    --------
    player_1 = HumanPlayer()
    player_2 = HumanPlayer()
    game = Game(player_1, player_2)
    game.run()
    """

    def __init__(self, A, B, deal=None):
        """Create a new Game object from two Player instances

        Parameters
        ----------
        A: cribbage.players.Player
            A cribbage player
        B: cribbage.players.Player
            A cribbage player

        Raises
        ------
        WinGame
            When game has been won by a player
        """

        self.A = A
        self.B = B
        if deal is None:
            self.deal = choice((0, 1))

    def run(self):
        start_message = f"""cribbage: Welcome to Cribbage!
cribbage: Starting a [bold][green]new game[/bold][/green]  
cribbage: Choosing a player to deal (pass `--deal` to specify) 
cribbage: Chose player {self.deal + 1}
cribbage: Player 1 is {self.A}
cribbage: Player 2 is {self.B}
cribbage: [bold]Enjoy your game!"""
        print(start_message)
        hands = 0
        while True:
            if self.deal == 0:
                hand = Hand(self.A, self.B)
                hand.run()
                self.deal = 1
            else:
                hand = Hand(self.B, self.A)
                hand.run()
                self.deal = 0
            hands += 1
