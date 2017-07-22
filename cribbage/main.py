from .game import game
from argparse import ArgumentParser
from .players import HumanPlayer, NondeterministicAIPlayer, EnumerativeAIPlayer, AIPlayer

player_choices = {
    'human': HumanPlayer,
    'enumerative': EnumerativeAIPlayer,
    'ai': AIPlayer,
    'random': NondeterministicAIPlayer,
}

parser = ArgumentParser()
parser.add_argument('player1', help='Type of player 1', choices=player_choices)
parser.add_argument('player2', help='Type of player 2', choices=player_choices)
parser.add_argument('--name1', help='Optional name for player 1')
parser.add_argument('--name2', help='Optional name for player 2') 
parser.add_argument('--debug', help="Enable debug mode (more verbose output)", action="store_true")
parser.add_argument('--no-gui', help="Print very little to the screen when running", action="store_false")
args = parser.parse_args()

def main():
    if not args.no_gui:
        print("Running game with no GUI")
    players = (
        player_choices[args.player1](name=args.player1_name), 
        player_choices[args.player2](name=args.player2_name))
    outcome = game(players, debug=args.debug, gui=args.no_gui)
    print('Score for this game:', outcome)

if __name__ == '__main__':
    main()
