# H SDD - Summer Part 3

## Introduction

Create a file called `summer3.py`. The file will contain the code for the following functions:

* _contains(text, target)_
* _letterTypes(text)_


## Functions


### contains()

Create a function (`contains`) that will accept a string and a character.  If the character is anywhere in the string the function will return `True`, otherwise it will return `False`.  The function is not case sensitive.

#### Examples

| Input                  | Output | Comment |
| -----                  | ------ | ------- |
| contains("Help!", "!") | True   | |
| contains("Help!", "h") | True   | |
| contains("Help!", "a") | False  | |



## letterTypes

Create a function (`letterTypes`) that will accept a string.  The function will count the number of uppercase and lowercase characters and return the values.

#### Examples

| Input                         | Output | Comment |
| -----                         | ------ | ------- |
| letterTypes("Hello")          | (1, 4) | |
| letterTypes("Fun! Fun! Fun!") | (1, 3) | |
| letterTypes("####! ####!")    | (0, 0) | |


## Testing

Test the functions to ensure they work.  Apart from TAD, remove any code that is not in the functions.

Save the file [`summer3Tests.py`](assets/summer3Tests.py) to the same folder as `summer3.py`.  Open and run `summer3Tests.py`.
