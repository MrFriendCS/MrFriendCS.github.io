# H SDD - Standard Algorithms

## Introduction

Create a file called `standard.py`.
The file will contain the code for the following functions:

* _searchString(values, target)_
* _findMinReal(values)_
* _findMaxInteger(values)_
* _countString(values, target)_


## Assumptions

1. The array of `values` is not empty
2. Tthe `target` data type is the same as the array of `values` data type


## Functions


### searchString()

Create a function (`searchString`) that will accept an array of strings and a search value.
The function will return `True` if the search value is in the array, and `False` if it is not.


#### Examples

| Input                                      | Output | Comment |
| -----                                      | ------ | ------- |
| searchString([\"B\", \"B\", \"C\"], \"B\") | True   | |
| searchString([\"B\", \"B\", \"C\"], \"D\") | False  | |


### findMinReal()

Create a function (`findMinReal`) that will accept an array of real values.
The function will return the smallest value that is in the array.


#### Examples

| Input                        | Output | Comment |
| -----                        | ------ | ------- |
| findMinReal([2.1, 1.7, 3.2]) | 1.7    | |


### findMaxInt()

Create a function (`findMaxInt`) that will accept an array of intergers.
The function will return the largest value that is in the array.


#### Examples

| Input                    | Output | Comment |
| -----                    | ------ | ------- |
| findMaxInt([1, 7, 2, 4]) | 7      | |


### countString()

Create a function (`countString`) that will accept an array of strings and a search value.
The function will return how many of the search values are found.


#### Examples

| Input                                         | Output | Comment |
| -----                                         | ------ | ------- |
| countString([\"Hi\", \"de\", \"Hi\"], \"Hi\") | 2      | |
| countString([\"Hi\", \"de\", \"Hi\"], \"do\") | 0      | |


## Testing

Test the functions to ensure they work.
Apart from TAD, remove any code that is not in the functions.

Save the file [`standardTests.py`](assets/standardTests.py) to the same folder as `standard.py`.
Open and run `standardTests.py`.
