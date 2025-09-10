# N5 SDD - Pontoon


## Introduction

Pontoon is a popular card game, which is also known as Spanish 21 and Blackjack. It’s usually played with between two and eight players.

Pontoon uses standard decks of 52 playing cards and the aim is to beat the dealer by having a hand closer to 21 than the dealer without going bust.  A total of more than 21 is bust.


## Task

Using the pseudocode below, implement code to create a simple game of Pontoon to allow a single player to practise.


### Top level design (Pseudocode)

```
Initialise card value
Initialise total score
initialise twist answer

Loop 2 times
    Pick a random card value from 2 to 11
    Display card value
    Add card value to total score
End loop

Get stick or twist from user

Start conditional loop for twist and total < 21

    Pick a random card value from 2 to 11
    
    If card value is 11 and total score > 10
        Set card value to 1
    End if

    Display card value

    Add card value to total score

    If total score <= 21
        Get stick or twist from user
    Else
        Display "Bust!"
    End if

End conditional loop

Display total score
```
