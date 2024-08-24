# H SDD – Various Functions

## Introduction

A number of files are provided in Repl.it, only the file functions.py is to be changed.

Do not change `main.py` as it calls functions from `functions.py` and displays the results.

When `main.py` is initially RUN only the first function in `functions.py` will return the correct value. All other functions will return 0, or False, as they are only skeleton code that needs to be completed.

```
The area of the square is 25 units squared

The area of the rectangle is 0 units squared

The area of the triangle is 0 units squared

The area of the circle is 0 units squared

The volume of the cube is 0 units cubed

The volume of the cuboid is 0 units cubed

The volume of the cylinder is 0 units cubed

The index of the @ symbol is -1

Character found: False
```

The working function in `functions.py` is shown below.

``` Python
def areaSquare(length):
    # Declare local variable
    area = 0

    # Calculate area
    area = length**2

    # return value
    return area
```

It receives a (formal) parameter and carries out a calculation. The result is returned to the line of code in `main.py` that called the function.

## Tasks

Complete each of the skeleton functions in `functions.py`.

Test your code by running `main.py`, if your code is correct then the output will be:

```
The area of the square is 25 units squared

The area of the rectangle is 20 units squared

The area of the triangle is 10.0 units squared

The area of the circle is 78.5 units squared

The volume of the cube is 125 units cubed

The volume of the cuboid is 24 units cubed

The volume of the cylinder is 113.04 units cubed

The index of the @ symbol is 4

Character found: True
```

Finally, run pytest to automatically test your code against different values.