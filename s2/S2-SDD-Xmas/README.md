# Python Xmas Turtle


## Introduction

'Tis the season to create festive scenes!

The turtle can be given instructions.  If the turtle understands an instruction it will carry it out.  It carrys them out in order, starting at `Line 1`.  Blank lines are allowed, even encouraged to make the instructions easier to read.


## Turtle Instructions

Turtles understand quite a few instructions.

| Instruction       | Comment |
| -----------       | ------- |
| xmas.rectangle()  | Draws a rectangle |
| xmas.triangle()   | Draws a triangle |
| xmas.leftTri()    | Draws a triangle |
| xmas.rightTri()   | Draws a triangle |
| xmas.circle()     | Draws a circle |
| xmas.star()       | Draws a star |
| xmas.tree()       | Draws a tree |
| xmas.snowman()    | Draws a snowman |
| xmas.reindeer()   | Draws a reindeer |
| xmas.santa()      | Draws a Santa |
| xmas.message()    | Writes a Message |
| xmas.background() | Changes the background colour |
| xmas.image()      | Displays an image |


### rectangle()

The following values can be sent to the `rectangle()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| width     | the width of the rectangle |
| height    | the height of the rectangle |
| colour    | the colour of the perimeter |
| thickness | the thickness of the perimeter |
| fill      | the colour inside the perimeter |


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
| width     | the width of the triangle |
| height    | the height of the triangle |
| colour    | the colour of the perimeter |
| thickness | the thickness of the perimeter |
| fill      | the colour inside the perimeter |


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
| width     | the width of the triangle |
| height    | the height of the triangle |
| colour    | the colour of the rectangle perimeter |
| thickness | the thickness of the perimeter |
| fill      | the colour inside the perimeter |


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
| width     | the width of the triangle |
| height    | the height of the triangle |
| colour    | the colour of the perimeter |
| thickness | the thickness of the perimeter |
| fill      | the colour inside the perimeter |


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
| radius    | the width of the circle |
| colour    | the colour of the circumference |
| thickness | the thickness of the circumference |
| fill      | the colour inside the circumference |


#### Example

```python
xmas.circle(50, -25, 50, "red", 6, "blue")
```


### star()

The following values can be sent to the `star()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| colour    | the colour of the star |
| scale     | scale the size of the star |


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
| scale     | scale the size of the tree |
| fir       | the colour of the fir |
| trunk     | the colour of the trunk |


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
| scale     | scale the size of the snowman |
| buttons   | the colour of the buttons |
| eyes      | the colour of the eyes |
| body      | the colour of the body |
| head      | the colour of the head |


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
| scale     | scale the size of the tree |
| fur       | the colour of the fur |
| legs      | the colour of the legs |
| eye       | the colour of the eye |


#### Example

```python
xmas.reindeer(50, -25, 1.5, "yellow", "blue", "red")
```


### santa()

The following values can be sent to the `santa()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| scale     | scale the size of the tree |
| suit      | the colour of the suit |
| hat       | the colour of the hat |


#### Example

```python
xmas.santa(50, 25, 1, "green", "red")
```


### message()

The following values can be sent to the `message()` command:

| Value     | Meaning |
| -----     | ------- |
| x         | _x_ value of the start coordinate |
| y         | _y_ value of the start coordinate |
| text      | the text to be displayed |
| size      | the font size |
| colour    | the colour of the text |


#### Example

```python
xmas.message(-50, 25, "Hello World!", 24, "red")
```


### image()

The following values can be sent to the `image()` command:

| Value     | Meaning |
| -----     | ------- |
| option    | selects a different image |


#### Example

```python
xmas.message(1)
```


### background()

The following values can be sent to the `background()` command:

| Value     | Meaning |
| -----     | ------- |
| colour    | the colour of the background |


#### Example

```python
xmas.background("pink")
```


## Colours

Turtles can draw with lots of different colours, such as `red`, `green`, `blue`, `yellow`, etc.

For longer list of colours visit: [Turtle Colours](https://cs111.wellesley.edu/reference/colors "Turtle colors")


## Grid

The grid uses cooridinates in the form __(__ ___x___, ___y___ __)__.
The centre of the grid is __(__ ___0___, ___0___ __)__.
