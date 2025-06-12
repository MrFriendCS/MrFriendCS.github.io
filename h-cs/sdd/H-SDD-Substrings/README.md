# H SDD - Substrings


## Introduction

Create a file called `substrings.py`.  The file will contain the code for the following functions:

* _left_
* _right_
* _mid_


## Assumptions

The decimal part of any values passed to a function will be ignored.

The functions will return values of `(-1, -1)` if passed invalid values.


## Functions


### left

This function return a substring, starting with the first character on the right.

#### Example code

``` python
print(left("Hello world", 4))
```

#### Example output

```
'Hell'
```


### right

This function will convert whole hours to days and hours.

#### Example code

``` python
print(right("Hello world", 5))
```

#### Example output

```
'world'
```


### mid

This function will convert whole minutes to hours and minutes.

#### Example code

``` python
print(mid("Hello world", 2, 4))
```

#### Example output

```
'ello'
```


## Testing

Test the functions to ensure they work.  Apart from TAD, remove any code that is not in the functions.

Save the file [`substringsTests.py`](assets/substringsTests.py) to the same folder as `substrings.py`.  Open and run `substringsTests.py`.

