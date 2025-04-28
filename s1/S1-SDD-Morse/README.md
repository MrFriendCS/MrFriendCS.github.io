# S1 SDD - Morse Code


## on start

### Set up the radio

Pick a radio group that you will send and receive messages on.  It can be from `0` to `255`.

![Radio group](assets/morse1.png "on start")


## Transmit

### Send a dash

Send the number `0` to represent a dash, and display something on the screen to show that the button has been pressed.

![Radio send 0](assets/morse2.png "on button A")


### Send a dot

Send the number `1` to represent a dot, and display something on the screen to show that the button has been pressed.

![Radio send 1](assets/morse3.png "on button B")


### Send a dot

Send the number `2` to represent the end of a letter, and display something on the screen to show that the buttons have been pressed.

![Radio send 2](assets/morse4.png "on button A+B")


## Receive

When a number is received use logic to show the correct symbol.

![Number received](assets/morse5.png "Number received")


### Receive a dash

When the number 0 is received, show a dash on the screen.

![Radio received 0](assets/morse6.png "Dash received")
