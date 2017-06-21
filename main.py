from game import game
from argparse import ArgumentParser
from players import HumanPlayer, NondeterministicAIPlayer, EnumerativeAIPlayer

player_choices = {
    'human': HumanPlayer(),
    'ai': EnumerativeAIPlayer(),
    'random': NondeterministicAIPlayer(),
}

parser = ArgumentParser()
parser.add_argument('player1', help='Player 1', choices=player_choices)
parser.add_argument('player2', help='Player 2', choices=player_choices)
parser.add_argument('--debug', help="Enable debugging mode", type=bool, default=False)
# parser.add_argument('--gui', help="Enable GUI", type=bool, default=True)
parser.add_argument('--gui', type=lambda s: s.lower() in ['true', 't', 'yes', '1'], help="Enable GUI")
args = parser.parse_args()

def main():

    players = (player_choices[args.player1], player_choices[args.player2])
    score = game(players, debug=args.debug, gui=args.gui)
    print('The final score is', score)

if __name__ == '__main__':
    main()
