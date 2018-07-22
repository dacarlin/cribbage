Cribbage for your command line
============================== 

Implementation of cribbage_ for two players. Text-based GUI for use on your command line (so you can appear to be working). Several kinds of opponents. 

.. _cribbage: https://www.pagat.com/adders/crib6.html

Opponents
---------

- **Random**. This opponent plays a random legal move. 
- **Expert**. This opponent uses an enumerative strategy to determine the move with the greatest possible reward (points), and takes that move. 

Installation 
------------

Install using `pip`:

.. code-block:: python 

	pip install cribbage 


Or install from the source 

.. code-block:: python

	git clone git@github.com:dacarlin/cribbage.git
	cd cribbage 
	python setup.py install 


How to use 
----------

If you want to play an easy game against the computer, you can run with the following. 

.. code-block:: bash

	cribbage human random --name1 Otto --name2 Osha  


If you would like to try playing one of the AI opponents (you likely will not win), you can run with the following. 

.. code-block:: bash

	cribbage human expert --name1 Alan --name2 Arin


In either case, replace "Alex" with your name and "Amy" for the name you wish to call the opponent, or omit them if you don't care about naming the players. 

Help
---- 

Run ``cribbage -h`` for an explanation of the command line arguments 
