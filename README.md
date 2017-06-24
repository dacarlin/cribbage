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

For regular use, you can run with 

```bash 
python main.py human ai --player1-name Alex --player2-name Amy
```

where you can replace "Alex" with your name and "Amy" for the name you wish to call the opponent. See `python main.py -h` for more. 
