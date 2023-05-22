# Training an AI player to play good cribbage 

Pone is an AI player that has been trained via self-play 
to play good cribbage 


## Problem setting 

There are two primary problems the AI player is trained 
to solve: 

1. Discarding. When discarding, the player receives 
   information about the current hand as well as the 
   current score (which is all available information) 
   in order to choose discards. The player is tasked
   with picking the indices of two of its cards to discards

2. Counting. When playing the counting game, the player
   receives a state vector containing the entire play in
   a structured format and is asked to pick the index of 
   one of its cards to play



### Problem 1: Discarding

Inputs state vector 1: (53, ) one hot, plus the current score scaled to 0-1 interval  
Inputs state vector 2: (53, ) one hot, plus the current score scaled to 0-1 interval
Outputs state vector 1: (52, ) one hot 
Outputs state vector 2: (52, ) one hot 


### Problem 2: Countig 

Inputs state vector: (52, 2) all one hot: cards in hand, cards on table, 
Output state vector: (52, ) the card to play 
