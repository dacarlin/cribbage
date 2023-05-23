from cribbage.game import Game
from cribbage.players import NondeterministicAIPlayer, WinGame


def main():
    # main script for running game 
    player_1 = NondeterministicAIPlayer(name="Player 1")
    player_2 = NondeterministicAIPlayer(name="Player 2")
    game = Game(player_1, player_2)
    try:
        game.run()
    except WinGame as win_game:
        print(win_game)


if __name__ == "__main__":
    main() 
