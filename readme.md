# Cribbage for your command line 

Implementation of [cribbage](https://www.pagat.com/adders/crib6.html) for two players. Text-based GUI for use on your command line (so you can appear to be working). Several kinds of opponents

- **Rando**: opponent that plays a random legal move
- **Amy**: AI that uses an enumerative strategy 
- **Andrew**: AI that has been trained by playing 100,000 games 

## How to use 

For regular use, you can run with 

```bash 
python main.py human ai --player1-name Alex --player2-name Amy
```

where you can replace "Alex" with your name and "Amy" for the name you wish to call the opponent. See `python main.py -h` for more. 
