Cribbage for your command line
============================== 

Implementation of cribbage_ for two players. Text-based GUI for use on your 
command line (so you can appear to be working). Several kinds of opponents. 

.. _cribbage: https://www.pagat.com/adders/crib6.html

Opponents
---------

- **Random**. This opponent plays a random legal move

- **Expert**. This opponent uses an enumerative strategy to determine the move
  with the greatest possible reward (points), and takes that move. The author
  wrote the optimal policy 

- **Student**. This opponent is a deep neural network that has been trained 
  via self-play using Google Keras_ and OpenAI Gym_ (see ``/train`` for details)
  to execute an optimal policy 

.. _Keras: https://keras.io
.. _Gym: https://gym.openai.com

Installation 
------------

Install using `pip`

.. code-block:: python 

	pip install cribbage 


Or install from the source 

.. code-block:: python

	git clone git@github.com:dacarlin/cribbage.git
	cd cribbage 
	python setup.py install 


How to use 
----------

From the command line, specify the kinds of players you want in the game 

.. code-block:: bash 

	cribbage human random 


You can also name the players  

.. code-block:: bash

	cribbage human random --name1 Osha --name2 Otto


If you would like to try playing one of the AI opponents, you can run with the
following

.. code-block:: bash

	cribbage human expert --name1 Alne --name2 Arin

Both the **Student** and the **Expert** players achieve performance that is 
better than most humans.   

Help
---- 

Run ``cribbage -h`` for an explanation of the command line arguments 
