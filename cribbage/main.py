from argparse import ArgumentParser
from .game import Game
from .players import (
    WinGame,
    HumanPlayer,
    NondeterministicAIPlayer,
    EnumerativeAIPlayer,
    TrainedAIPlayer,
)


def main():

    player_choices = {
        "human": HumanPlayer,
        "brute_force": EnumerativeAIPlayer,
        "trained": TrainedAIPlayer,
        "random": NondeterministicAIPlayer,
    }

    parser = ArgumentParser()
    parser.add_argument("player1", help="Type of player 1", choices=player_choices)
    parser.add_argument("player2", help="Type of player 2", choices=player_choices)
    parser.add_argument("--name1", help="Optional name for player 1")
    parser.add_argument("--name2", help="Optional name for player 2")
    args = parser.parse_args()

    player_1 = player_choices[args.player1](name=args.name1)
    player_2 = player_choices[args.player2](name=args.name2)
    game = Game(player_1, player_2)

    try:
        game.run()
    except WinGame as win_game:
        print(win_game)
