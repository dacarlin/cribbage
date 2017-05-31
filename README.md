# Cribbage for your command line!

Example gameplay: 

```bash
Player "Alex" is dealing … 
Your hand is 3♢ 4♣ 8♣ 9♢ K♠ K♡
Your discard (type two numbers): 
```

## Opponents 

### Nondeterministic AI ("Rando") 

[...]

### Expert Systems/Enumerative AI ("Amy") 

[...]

### Ranking/Deep Learning/Reinforcement Learning AI ("")

Here, the problem is as simple as taking the two actions ("decide which card to play in counting" and "decide which 2 cards to discard") and learning to rank the choices available. 

```python
cpdef ask_for_play(play_vector: list):
  ranked = rank_cards_for_play(self.hand, play_vector)
  return ranked[0]

cpdef ask_for_discards():
  discards = rank_cards_for_discard(self.hand)
  return discards[0:2]
```
