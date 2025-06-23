# H SDD - Summer Part 1

## Introduction

Create a file called `summer1.py`. The file will contain the code for the following functions:

* _circumference_
* _radius_
* _diamter_
* _area_


## Assumptions

1. Pi is `3.1415`.
2. If invalid values are passed to a function, then `-1.0` (zero) will be returned.


## Functions


### circumference()

Create a function (`circumference`) that will accept a real value and a character.  The real value will represent the size of the radius or diameter, and the character will clarify which it is.  The function will calculate and return the circumference of a circle, rounded to 4 decimal places.

__Stretch task__: If only a single parameter is passed to the function, it will calculate the circumference with the value used as the diameter.

### Examples

| Input                 | Output | Comment |
| -----                 | ------ | ------- |
| circumference(1, "d") | 3.1415 | |
| circumference(1, "r") | 6.283  | |
| circumference(10)     | 31.415 | Stretch task |


### radius()

Create a function (`radius`) that will accept a real value and a character.  The real value will represent the size of the diameter or circumference, and the character will clarify which it is.  The function will calculate and return the radius of a circle, rounded to 4 decimal places.

__Stretch task__: If only a single parameter is passed to the function, it will calculate the radius with the value used as the diameter.

### Examples

| Input              | Output | Comment |
| -----              | ------ | ------- |
| radius(1, "d")     | 0.5    | |
| radius(6.283, "c") | 1.0    | |
| radius(10)         | 5.0    | Stretch task |


### diameter()

Create a function (`diameter`) that will accept a real value and a character.  The real value will represent the size of the radius or circumference, and the character will clarify which it is.  The function will calculate and return the diameter of a circle, rounded to 4 decimal places.

__Stretch task__: If only a single parameter is passed to the function, it will calculate the diameter with the value used as the radius.

### Examples

| Input                | Output | Comment |
| -----                | ------ | ------- |
| diameter(2, "r")     | 4.0    | |
| diameter(6.283, "c") | 5.0    | |
| diameter(10)         | 20.0   | Stretch task |


### area()

Create a function (`area`) that will accept a real value and a character.  The real value will represent the size of the radius, diameter, or circumference.  The character will clarify which it is.  The function will calculate and return the area of a circle, rounded to 4 decimal places.

__Stretch task__: If only a single parameter is passed to the function, it will calculate the area with the value used as the radius.

### Examples

| Input        | Output | Comment |
| -----        | ------ | ------- |
| area(1, "r") | 3.1415 | |
| area(6, "d") | 0.5    | |
| area(6, "c") | 0.5    | |
| area(2)      | 12.566 | Stretch task |
