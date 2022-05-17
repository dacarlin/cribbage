Cribbage for your command line
============================== 

Implementation of [cribbage][1] for two players. Text-based GUI for use on your 
command line (so you can appear to be working). Several kinds of opponents. 

[1]: https://www.pagat.com/adders/crib6.html

Opponents
---------

- **Random**. This opponent plays a random legal move

- **Expert**. This opponent uses an enumerative strategy to determine the move
  with the greatest possible reward (points), and takes that move. The author
  wrote the optimal policy 

- **Student**. This opponent is a deep neural network that has been trained 
  via self-play using Google [Keras][2] and OpenAI [Gym][3] (see `/train` for details)
  to execute an optimal policy 

[2]: https://keras.io
[3]: https://gym.openai.com

Installation 
------------

Install using `pip`

```
pip install cribbage 
```

Or install from the source using Poetry (for development, to run the tests)  

```
git clone git@github.com:dacarlin/cribbage.git
poetry install 
poetry run pytest 
```


How to use 
----------

From the command line, specify the kinds of players you want in the game 

```
cribbage human random 
```

You can also name the players  

```
cribbage human random --name1 Osha --name2 Otto
```

If you would like to try playing one of the AI opponents, you can run with the
following

```
cribbage human expert --name1 Alne --name2 Arin
```

Both the **Student** and the **Expert** players achieve performance that is 
better than most humans.   


Help
---- 

Run `cribbage --help`  for an explanation of the command line arguments 
