# S1 SDD - Morse Code


## Introduction

Two micro:bits are needed to send and receive [Morse Code](https://morsecode.world/Titanic.html) dots and dashes.  If micro:bit V2 is used then the sounds can be heard using the built in speaker.  With a micro:bit V1, the dots and dashes can still be seen on the screen.


## Set up

### On start

Pick a radio group to send and receive messages on.  It can be from `0` to `255`.

![Radio group](assets/morse1.png "on start")


## Send

### On button A pressed

Send the number `0` to represent a dash, and display something on the screen to show that the button has been pressed.

![Radio send 0](assets/morse2.png "on button A")


### On button B pressed

Send the number `1` to represent a dot, and display something on the screen to show that the button has been pressed.

![Radio send 1](assets/morse3.png "on button B")


### On button A+B pressed

Send the number `2` to represent the end of a letter, and display something on the screen to show that the buttons have been pressed.

![Radio send 2](assets/morse4.png "on button A+B")


## Receive

When a number is received use logic to show the correct symbol, and then clear the screen ready for the next symbol.

![Number received](assets/morse5.png "Number received")


### If number is 0

When the number `0` is received, show a dash on the screen.

![Radio received 0](assets/morse6.png "Dash received")


### Else, if number is 1

When the number `1` is received, show a dot on the screen.

![Radio received 1](assets/morse7.png "Dot received")


### Else

When a number that is not a `0` or a `1` is received, show a symbol on the screen.

![Radio received 2](assets/morse8.png "End received")


### Sound

The micro:bit V2 has a built in speaker that can be used to hear the 'dots' and 'dashes'.  This part can be missed out if a micro:bit V1 is being used. 


#### Dash

![Radio received 0](assets/morse9.png "Dash received")


#### Dot

![Radio received 1](assets/morse10.png "Dot received")


#### End

![Radio received 2](assets/morse11.png "End received")


## Morse Code

[Morse Code sheet](assets/MorseCode.docx)
