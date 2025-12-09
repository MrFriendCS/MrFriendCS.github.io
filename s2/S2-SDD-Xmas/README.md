# Python Xmas Turtle


## Introduction

The turtle can be given instructions.  If the turtle understands an instruction it will carry it out.  It carrys them out in order, starting at `Line 1`.  Blank lines are allowed, even encouraged to make the instructions easier to read.


## Turtle Instructions

Turtles understand quite a few instructions.

| Instruction            | Example                            | Comment |
| -----------            | -------                            | ------- |
| forward()<br>fd()      | tim.forward(75)<br>tim.fd(75)      | move forward (pixels) |
| backward()<br>bk()     | tim.backward(25)<br>tim.bk(25)     | move backward (pixels) |
| right()<br>rt()        | tim.right(75)<br>tim.rt(75)        | turn right (degrees) |
| left()<br>lt()         | tim.left(75)<br>tim.lt(75)         | turn left (degrees) |
| speed()                | tim.speed(5)                       | speed: 0 to 10 |
| home()                 | tim.home()                         | move to centre of screen |
| setheading()<br>seth() | tim.setheading(45)<br>tim.seth(45) | direction: 0 = East |
| goto()                 | tim.goto(20, 40)                   | move to a position (x, y) |


### Colours

Turtles can draw with lots of different colours, such as `red`, `green`, `blue`, `yellow`, etc.

For longer list of colours visit: [Turtle Colours](https://cs111.wellesley.edu/reference/colors "Turtle colors")


## Grid

The grid uses cooridinates in the form __(__ ___x___, ___y___ __)__.
The centre of the grid is __(__ ___0___, ___0___ __)__.
