# H SDD - Functions


## Introduction

Create a file called `functions.py`. The file will contain the code for the following functions:

- _gradient_
- _hypontenuse_
- _areaCircle_
- _areaTriangle_
- _areaSquare_
- _areaRectangle_
- _volPrism_
- _volCylinder_
- _volCone_
- _volSphere_


## Assumptions

1. Pi is `3.1415`.
2. If invalid values are passed to a function, then `-1.0` (Minus one) will be returned.


## Functions


### gradient()

Create a function (`gradient`) that will accept two real values.  The real values will represent `dy` (rise) and `dx` (run).
The function will calculate and return the gradient, rounded to 2 decimal places.

#### Examples

| Input               | Output |
| -----               | ------ |
| gradient(10, 5)     | 2.0    |
| gradient(5, 10)     | 0.5    |
| gradient(0.23, 5.5) | 0.42   |


### hypontenuse()

Create a function (`hypontenuse`) that will accept two real values.  The real values will represent the length of the short sides of a right angle triangle.
The function will calculate and return the length of the hypotenuse, rounded to 2 decimal places.

#### Examples

| Input                   | Output |
| -----                   | ------ |
| hypontenuse(3, 4)       | 5.0    |
| hypontenuse(6, 8)       | 10.0   |
| hypontenuse(3.75, 10.2) | 10.87  |


### areaCircle()

Create a function (`areaCircle`) that will accept a real value.  The real value will represent the radius of a circle.
The function will calculate and return the area of a circle, rounded to 2 decimal places.

#### Examples

| Input           | Output |
| -----           | ------ |
| areaCircle(1)   | 3.14   |
| areaCircle(10)  | 314.15 |
| areaCircle(7.5) | 176.71 |


### areaTriangle()

Create a function (`areaTriangle`) that will accept two real values.  The real values will represent the base and the height of triangle.
The function will calculate and return the area of the triangle, rounded to 2 decimal places.

#### Examples

| Input                    | Output |
| -----                    | ------ |
| areaTriangle(3, 4)       | 6.0    |
| areaTriangle(10, 2)      | 10.0   |
| areaTriangle(3.75, 10.2) | 19.13 |
