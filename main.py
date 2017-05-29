from game import game_with_gui
from argparse import ArgumentParser
from players import HumanPlayer, NondeterministicAIPlayer, AIPlayer

def main():

    parser = ArgumentParser()
    parser.add_argument('--ai', help='Enable AI player (default is nondeterministic (random) player)')
    parser.add_argument('--name', help='Debugging mode')
    args = parser.parse_args()

    pone_name = "Jeff" # random name?
    default = 'Human'
    #intro = '''Command line cribbage\nPlease type your name, "Enter" to use the default ("Human"): '''.format(default)

    # name = input(intro)
    # if len(name) == 0:
    #   name = default


    name = default # debugging!
    
    players = (HumanPlayer(name), NondeterministicAIPlayer(pone_name))
    if args.ai:
        players = (HumanPlayer(name), AIPlayer("Amy"))
    scores = game_with_gui(players)

    # now, by definition, the game is over
    print('The final scores are:', zip(players,scores))
    print("Thanks for playing a game of commmand line cribbage")

    return 0

if __name__ == '__main__':
    main()
