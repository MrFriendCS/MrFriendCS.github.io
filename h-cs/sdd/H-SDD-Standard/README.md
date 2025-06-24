# H SDD - Standard Algorithms

## Introduction

Create a file called `standard.py`.  The file will contain the code for the following functions:

* _search(values, target)_
* _findMin(values)_
* _findMax(values)_
* _count(values, target)_


## Assumptions

1. Target datatypes are the same as the array of values datatype.


## Functions


### search()

Create a function (`search`) that will accept an array and a search value.  The function will return `True` if the search value is in the array, and `False` if it is not.

#### Examples

| Input                        | Output | Comment |
| -----                        | ------ | ------- |
| search([1, 2, 3], 3)         | True   | |
| search(["a", "b", "c"], "d") | False  | |
| search([1.3, 2.2, 3.1], 2.2) | True   | |


### findMin()

Create a function (`findMin`) that will accept an array.  The function will return the smallest value that is in the array.

#### Examples

| Input                  | Output | Comment |
| -----                  | ------ | ------- |
| findMin(1, 7, 2, 4)    | 1      | |
| findMin("o", "n", "e") | 'e'    | |
| findMin(2.1, 1.7, 3.2) | 1.7    | |


### findMax()

Create a function (`findMax`) that will accept an array.  The function will return the largest value that is in the array.

#### Examples

| Input                   | Output | Comment |
| -----                   | ------ | ------- |
| findMax(1, 7, 2, 4)     | 7      | |
| findMax("o", "n", "e")  | 'o'    | |
| findMax(2.1, 1.7, 3.2)  | 3.2    | |


### count()

Create a function (`count`) that will accept an array and a search value.  The function will return how many of the search values are found.

#### Examples

| Input                        | Output | Comment |
| -----                        | ------ | ------- |
| count([3, 1, 2, 3], 3)       | 2      | |
| count((["a", "b", "c"], "d") | 0      | |
| count(([1.3, 2.2, 3.1], 2.2) | 1      | |
