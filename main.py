from game import game_with_gui
from argparse import ArgumentParser
from players import HumanPlayer, NondeterministicAIPlayer, EnumerativeAIPlayer

player_choices = {
    'human': HumanPlayer(),
    'ai': EnumerativeAIPlayer(),
    'random': NondeterministicAIPlayer(),
}

parser = ArgumentParser()
parser.add_argument('--player1', help='Player 1', choices=player_choices)
parser.add_argument('--player2', help='Player 2', choices=player_choices)
parser.add_argument('--debug', help="Enable debugging mode")
args = parser.parse_args()

def main():

    players = (player_choices[args.player1], player_choices[args.player2])
    score = game_with_gui(players, debug=args.debug)
    print('The final score is', score)

if __name__ == '__main__':
    main()
