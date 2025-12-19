# N5 SDD - Pontoon


## Introduction

Pontoon is a popular card game, which is also known as Spanish 21 and Blackjack. 
It’s usually played with between two and eight players.

Pontoon uses a standard deck of playing cards: 2-10, Jack, Queen, King, and Ace.
Picture cards are worth 10, and an ace can be 1 or 11.
The aim is to beat the dealer by having a hand closer to 21 than the dealer, without going bust.
A score of more than 21 is bust!


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

If total score < 21

    Get valid stick or twist from user

End if

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
    
        If total score < 21

            Get valid stick or twist from user
        
        End if

    End if

End conditional loop

Display total score
```


## User Interface

Examples of the expected user interface are shown below, with some possible input and output values.


### Example 1

```
Craigston Casino
    Pontoon!
----------------

Card 1: 10
Card 2: 2

Stick or twist? t

You drew a 9

You scored 21

www.gambleaware.org
===================
```


### Example 2

```
Craigston Casino
    Pontoon!
----------------

Card 1: 4
Card 2: 9

Stick or twist? t

You drew a 1

Stick or twist? t

You drew a 8

Bust!

You scored 22

www.gambleaware.org
===================
```
