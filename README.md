# Cribbage for your command line 

Implementation of [cribbage](https://www.pagat.com/adders/crib6.html) for two players. Text-based GUI for use on your command line (so you can appear to be working). Several kinds of opponents. 

## Opponents 

- **Random**. This opponent plays a random legal move. 
- **Brute Force**. This opponent uses an enumerative strategy to determine the move with the greatest possible reward (points), and takes that move. 
- **Trained**. This opponent plays according to predictions made by a machine learning model. The predictions are based the outcomes of the games in the training data set (see the `train` directory). 

## Installation 

Install using `pip`:

```bash
pip install cribbage 
``` 

Or install from the source 

```bash
git clone git@github.com:dacarlin/cribbage.git
cd cribbage 
python setup.py install 
```

## How to use 

If you want to play an easy game against the computer, you can run with the following. 

```bash 
cribbage human random --name1 Alex --name2 Amy  
```

If you would like to try playing one of the AI opponents (you likely will not win), you can run with the following. 

```bash 
cribbage human brute_force --name1 Alex --name2 Amy 
```

In either case, replace "Alex" with your name and "Amy" for the name you wish to call the opponent, or omit them if you don't care about naming the players. 

## Help 

Run `cribbage -h` for more.
