# Python Xmas Turtle


## Introduction

'Tis the season to create festive scenes!

A Python turtle can be given instructions to draw on the screen.  If the turtle understands an instruction it will carry it out.  It carrys them out in order, starting at `Line 1`.  Blank lines are allowed, even encouraged to make the instructions easier to read.


## Xmas Turtle Instructions

The xmas turtle understands quite a few instructions.

| Instruction       | Comment |
| -----------       | ------- |
| xmas.rectangle()  | Draws a rectangle |
| xmas.triangle()   | Draws a triangle - peak in the middle |
| xmas.leftTri()    | Draws a triangle - peak on the left |
| xmas.rightTri()   | Draws a triangle - peak on the right |
| xmas.circle()     | Draws a circle |
| xmas.line()       | Draws a line |
| xmas.star()       | Draws a star |
| xmas.tree()       | Draws a tree |
| xmas.snowman()    | Draws a snowman |
| xmas.reindeer()   | Draws a reindeer |
| xmas.santa()      | Draws Santa |
| xmas.message()    | Writes a message |
| xmas.background() | Changes the background colour |
| xmas.image()      | Displays an image |
| xmas.fast()       | Turtle draws quickly |
| xmas.medium()     | Turtle draws at a medium speed |
| xmas.slow()       | Turtle draws slowly |


### rectangle()

The following values can be sent to the `rectangle()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| width     | Width of the rectangle |
| height    | Height of the rectangle |
| colour    | Colour of the perimeter |
| thickness | Thickness of the perimeter |
| fill      | Colour inside the perimeter |


#### Example

```python
xmas.rectangle(50, 25, 100, 40, "red", 6, "blue")
```


### triangle()

The following values can be sent to the `triangle()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| width     | Width of the triangle |
| height    | Height of the triangle |
| colour    | Colour of the perimeter |
| thickness | Thickness of the perimeter |
| fill      | Colour inside the perimeter |


#### Example

```python
xmas.triangle(-50, 25, 100, 40, "red", 6, "blue")
```


### leftTri()

The following values can be sent to the `leftTri()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| width     | Width of the triangle |
| height    | Height of the triangle |
| colour    | Colour of the rectangle perimeter |
| thickness | Thickness of the perimeter |
| fill      | Colour inside the perimeter |


#### Example

```python
xmas.leftTri(-50, -25, 100, 40, "red", 6, "blue")
```


### rightTri()

The following values can be sent to the `rightTri()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| width     | Width of the triangle |
| height    | Height of the triangle |
| colour    | Colour of the perimeter |
| thickness | Thickness of the perimeter |
| fill      | Colour inside the perimeter |


#### Example

```python
xmas.rightTri(50, 25, 100, 40, "red", 6, "blue")
```


### circle()

The following values can be sent to the `circle()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| radius    | Width of the circle |
| colour    | Colour of the circumference |
| thickness | Thickness of the circumference |
| fill      | Colour inside the circumference |


#### Example

```python
xmas.circle(50, -25, 50, "red", 6, "blue")
```


### line()

The following values can be sent to the `line()` command:

| Value     | Meaning |
| -----     | ------- |
| x1        | _x_ value of the start coordinate |
| y1        | _y_ value of the start coordinate |
| x2        | _x_ value of the end coordinate |
| y2        | _y_ value of the end coordinate |
| colour    | Colour of the line |
| thickness | Thickness of the line |


#### Example

```python
xmas.line(50, 25, -50, -25, "purple", 6)
```


### star()

The following values can be sent to the `star()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| colour    | Colour of the star |
| scale     | Scale the size of the star |


#### Example

```python
xmas.star(50, 25, "red", 2)
```


### tree()

The following values can be sent to the `tree()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| scale     | Scale the size of the tree |
| fir       | Colour of the fir |
| trunk     | Colour of the trunk |


#### Example

```python
xmas.tree(-50, 25, 0.5, "yellow", "black")
```


### snowman()

The following values can be sent to the `snowman()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| scale     | Scale the size of the snowman |
| buttons   | Colour of the buttons |
| eyes      | Colour of the eyes |
| body      | Colour of the body |
| head      | Colour of the head |


#### Example

```python
xmas.snowman(-50, -25, 0.5, "yellow", "blue", "red", "green")
```


### reindeer()

The following values can be sent to the `reindeer()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| scale     | Scale the size of the tree |
| fur       | Colour of the fur |
| legs      | Colour of the legs |
| eye       | Colour of the eye |
| nose      | Colour of the nose |


#### Example

```python
xmas.reindeer(50, -25, 1.5, "yellow", "blue", "red", "green")
```


### santa()

The following values can be sent to the `santa()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| scale     | Scale the size of the tree |
| suit      | Colour of the suit |
| hat       | Colour of the hat |
| gloves    | Colour of the gloves |
| boots     | Colour of the boots |


#### Example

```python
xmas.santa(50, 25, 2, "green", "red", "pink", "purple", "blue")
```


### message()

The following values can be sent to the `message()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| text      | Text to be displayed |
| size      | Font size |
| colour    | Colour of the text |


#### Example

```python
xmas.message(-50, 25, "Hello World!", 24, "red")
```


### image()

The following values can be sent to the `image()` command:

| Value     | Meaning |
| -----     | ------- |
| option    | Selects a different image |


#### Example

```python
xmas.image(1)
```


### background()

The following values can be sent to the `background()` command:

| Value     | Meaning |
| -----     | ------- |
| colour    | Colour of the background |


#### Example

```python
xmas.background("pink")
```


## Colours

Turtles can draw with lots of different colours, such as `red`, `green`, `blue`, `yellow`, etc.

For longer list of colours visit:
[Turtle Colours](https://cs111.wellesley.edu/reference/colors "Turtle colours")


## Grid

The grid uses cooridinates in the form __(__ ___x___, ___y___ __)__.
The centre of the grid is __(__ ___0___, ___0___ __)__.


## Starter Code

```python
# Title: Xmas Scene
# Author: 
# Date: 

import xmas

```