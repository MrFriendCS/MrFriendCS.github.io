# H SDD - Summer Part 2

## Introduction

Create a file called `summer3.py`. The file will contain the code for the following functions:

* _letterTypes_
* _checkIBSN13_


## Assumptions

1. Pi is `3.1415`.
2. If invalid values are passed to a function, then `-1.0` will be returned.


## Functions


### letterTypes()

Create a function (`letterTypes`) that will accept a real value and a character.  The real value will represent the size of the radius or diameter, and the character will clarify which it is.  The function will calculate and return the circumference of a circle, rounded to 4 decimal places.

#### Examples

| Input                 | Output | Comment |
| -----                 | ------ | ------- |
| letterTypes(1, "d") | 3.1415 | |
| letterTypes(1, "r") | 6.283  | |
| letterTypes(10)     | 31.415 | Stretch task |


### checkIBSN13()

Create a function (`checkIBSN13`) that will check if a 13-digit [ISBN](https://en.wikipedia.org/wiki/ISBN#ISBN-13_check_digit_calculation) is valid.  It will accept a string, and return a Boolean value.  The function must be able to accept ISBNs with and without dashes that separate the values.

The book 'The Computers That Made Britain: The Home Computer Revolution of the 1980s' has an ISBN-13 of 9781912047857.  There are 12 digits plus the final check digit.  The check digit is calculated using the other 12 digits.

Each digit is multiplied by either 1 or 3, depending on its position.

| 1st, 3rd, ...   | 2nd, 4th, ... |
| -------------   | ------------- |
| 9 &times; 1 = 9 | 7 &times; 3 = 21 |
| 8 &times; 1 = 8 | 1 &times; 3 = 3 |
| 9 &times; 1 = 9 | 1 &times; 3 = 3 |
| 2 &times; 1 = 2 | 0 &times; 3 = 0 |
| 4 &times; 1 = 4 | 7 &times; 3 = 21 |
| 8 &times; 1 = 8 | 5 &times; 3 = 15 |

Calculate the sum (example of working):

```
Sum = 9 + 21 + 8 + 3 + 9 + 3 + 2 + 0 + 4 + 21 + 8 + 15
Sum = 103
```

Calculate the remainder (example of working):

```
Remainder = Sum mod 10
Remainder = 103 mod 10
Remainder = 3
```

Calculate the check digit (example of working):

```
Check digit = 10 - Remainder
Check digit = 10 - 3
Check digit = 7
```


#### Examples

| Input                            | Output | Comment |
| -----                            | ------ | ------- |
| checkIBSN13("9780306406157")     | True   | |
| checkIBSN13("978-0-306-40615-7") | True   | |


## Testing

Test the functions to ensure they work.  Apart from TAD, remove any code that is not in the functions.

Save the file [`summer3Tests.py`](assets/summer1Tests.py) to the same folder as `summer3.py`.  Open and run `summer3Tests.py`.
