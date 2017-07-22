# Cribbage for your command line 

Implementation of [cribbage](https://www.pagat.com/adders/crib6.html) for two players. Text-based GUI for use on your command line (so you can appear to be working). Several kinds of opponents

- **Random**: opponent that plays a random legal move
- **Enumerative**: AI that uses an enumerative (brute force) strategy 
- **Trained**: RL algorithm that has been trained by playing 100,000 games  

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

If you want to play an easy game, you can run with 

```bash 
cribbage human random --name1 Alex --name2 Amy  
```

If you would like to try playing the AI (you likely will not win), you can run with 

```bash 
cribbage human enumerative --name1 Alex --name2 Amy 
```

In either, replace "Alex" with your name and "Amy" for the name you wish to call the opponent, or omit them if you don't care about naming the players. Run `cribbage -h` for more. 
