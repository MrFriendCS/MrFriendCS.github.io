# H SDD - Summer Part 2

## Introduction

Create a file called `summer2.py`. The file will contain the code for the following functions:

* _makeUsername(name)_
* _reverse(text)_


## Assumptions

1. Pi is `3.1415`.
2. If invalid values are passed to a function, then `-1.0` will be returned.


## Functions


### makeUsername()

Create a function (`makeUsername`) that will accept a string.  It will use the string to create a username and return it as a lowercase string, in the format:

* Characters: es
* Characters: first 4 characters of actual parameter, if long enough
* Integer: random single digit (1 to 9)
* Character: random single character (a to z)

#### Examples

| Input                   | Output     | Comment |
| -----                   | ------     | ------- |
| makeUsername("William") | 'eswill2f' | __eswill__ + random parts |
| makeUsername("SUE")     | 'essue5t'  | __essue__ + random parts  |
| makeUsername("KC")      | 'invalid'  | Less than 3 characters in name |


### reverse()

Create a function (`reverse`) that will reverse the characters in a string and return the new string.

#### Examples

| Input                      | Output            | Comment |
| -----                      | ------            | ------- |
| reverse("William")         | 'mailliW'         | |
| reverse("How are you m8?") | '?8m uoy era woH' | |
| reverse(10)         | 5.0    | Stretch task |


## Testing

Test the functions to ensure they work.  Apart from TAD, remove any code that is not in the functions.

Save the file [`summer2Tests.py`](assets/summer1Tests.py) to the same folder as `summer2.py`.  Open and run `summer2Tests.py`.
