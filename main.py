from game import game_with_gui
from players import HumanPlayer, NondeterministicAIPlayer

intro = '''
Command line cribbage 
By Alex Carlin 
'''

print(intro)
name = input("Type your name (enter for default)")
if len(name) == 0:
  name = "Human"


# choose a random name for the AI?

players = (HumanPlayer(name), NondeterministicAIPlayer("Jeff")) 
scores = game_with_gui(players)

# now, by definition, the game is over 
print(zip(players,scores))
print("Thanks for playing commmand line cribbage")
