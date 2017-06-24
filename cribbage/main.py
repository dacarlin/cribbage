from .game import game
from argparse import ArgumentParser
from .players import (HumanPlayer, NondeterministicAIPlayer, EnumerativeAIPlayer,
                     AIPlayer)

player_choices = {
    'human': HumanPlayer,
    'enumerative': EnumerativeAIPlayer,
    'ai': AIPlayer,
    'random': NondeterministicAIPlayer,
}

parser = ArgumentParser()
parser.add_argument('player1', help='Player 1', choices=player_choices)
parser.add_argument('player2', help='Player 2', choices=player_choices)
parser.add_argument('--player1-name')
parser.add_argument('--player2-name')
parser.add_argument('--debug', help="Enable debug mode", action="store_true")
parser.add_argument('--no-gui', help="Disable GUI", action="store_false")
args = parser.parse_args()

def main():

    if not args.no_gui:
        print("Running game with no GUI")
    players = (player_choices[args.player1](name=args.player1_name), player_choices[args.player2](name=args.player2_name))
    outcome = game(players, debug=args.debug, gui=args.no_gui)
    print('Outcome:', outcome)

if __name__ == '__main__':
    main()
