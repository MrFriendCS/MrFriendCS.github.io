# N5 SDD - Pontoon


## Introduction

Pontoon is a popular card game, which is also known as Spanish 21 and Blackjack. 
It’s usually played with between two and eight players.

Pontoon uses a standard deck of playing cards: 2-10, Jack, Queen, King, and Ace.
Picture cards are worth 10, and an ace can be 1 or 11.
The aim is to beat the dealer by having a hand closer to 21 than the dealer, without going bust.
A more than 21 is bust!


## Task

Using the pseudocode below, implement code to create a simple game of Pontoon to allow a single player to practise.


### Top level design (Pseudocode)

```
Initialise card value
Initialise total score
initialise twist answer

Loop 2 times

    Pick a random card value from 2 to 11

    If card value is 11 and total score > 10

        Set card value to 1

    End if

    Display card value

    Add card value to total score

End loop

Get valid stick or twist from user

Start conditional loop for twist and total < 21

    Pick a random card value from 2 to 11

    If card value is 11 and total score > 10

        Set card value to 1

    End if

    Display card value

    Add card value to total score

    If total score > 21

        Display "Bust!"

    Else

        Get valid stick or twist from user

    End if

End conditional loop

Display total score
```


## User Interface

An example of the expected user interface is shown below, with some possible input and output values.

```
Craigston Casino
    Pontoon!
----------------

Card 1: 10
Card 2: 2

Stick or twist? t

You drew a 9

Stick or twist? s

You scored 21

www.gambleaware.org
===================
```
