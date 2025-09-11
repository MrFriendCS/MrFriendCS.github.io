# N5 SDD - Pontoon Part 2


## Introduction

Pontoon is a popular card game, which is also known as Spanish 21 and Blackjack. It’s usually played with between two and eight players.

Pontoon uses standard decks of 52 playing cards.  Each player is dealt two cards.  Each player, in turn will, either `twist` or `stick`.  If they twist they are dealt another card.  This continues until the player sticks or go bust.  A player has bust if they score more than 21.


## Card values

* Number cards: face value
* Picture cards: 10
* Ace: 1 or 11


## Analysis

### Inputs

* Number of players
* Names of players - minimum of 2 letters
* Stick or twist

### Processes

* Calculate value of first two cards for each player
* Add value of new card(s) to each player's score

### Outputs

* Players' names
* Players' scores

### Assumptions

* `twist` and `stick` are lowercase


## Task

Using the structure diagram below, implement code to create a simplified version of the Pontoon.


### Top leve design (structure diagram)

![Structure diagram](assets/sd2.png)


### Example user interface

#### Start

```
Pontoon
-------

How many players? 2

Enter names
-----------
Player 1: Jim
Player 2: Jo
```


#### Game

```
Game
----

Jim: 13
Stick or twist? twist
Card value: 10
Bust!

Jo: 9
Stick or twist? twist
Card value: 2
Stick or twist? twist
Card value: 10
Stick or twist? stick
```


#### End

```
Results
-------
Jim: 23
Jo: 21
=======
```
