
# N5 Computing Science

## Software Design and Development

All code examples use Python.

**Note:** These notes are focused on N5 Computing Science so some terms are used differently.  Any reference to an `array` will actually use a `list`.

### Display information

``` Python
print("Hello world")

print(3.14)
```

### Implementation (computational constructs)

#### expressions to assign values

Variables are used to store values.  An assignment statement has 3 parts:

 1. An assignment operator **=** (an equals sign in maths)
 2. The value to the right of the assignment operator
 3. The variable name to the left of the assignment operator

The value is assigned to (stored in) the variable.  The value *might* need to be calculated first before being assigned.

``` python
myInteger = 5
```

``` python
myFloat = 3.14
```

``` python
myCharacter = "&"
```

``` python
myString = "Hello"
```

``` python
myBoolean = True
```

``` python
myArrayOfIntegers = [56, 34, 2, 85, 51]
```




#### expressions to return values using arithmetic operations

Addition
``` python
4 + 2
```

Subtraction
``` python
4 - 2
```

Multiplication
``` python
4 * 2
```

Division
``` python
4 / 2
```

Exponentiation (to the power of)
``` python
4 ** 2
```

Examples
``` python
myMultiplication = 3 * 2
print(myMultiplication)

mySquare = 3 ** 2
print(mySquare)

myAge = 21
myAge = myAge + 1
print(myAge)
```

#### expressions to concatenate strings

Concatenate means to join together.

``` python
part1 = "Ho"
part2 = "use"

word = part1 + part2

print(word)
```

Be sure to include a space between words when concatenating.

``` python
word1 = "Hello"
word2 = "world"

phrase = word1 + " " + word2

print(phrase)
```

#### selection constructs using simple conditional statement

##### Comparisons

Compare one value with another to produce a Boolean answer of `True` or `False`.

Equality (the same as)
``` python
16 == 18
```

Inequality (not the same as)
``` python
16 != 18
```

Greater than
``` python
16 > 18
```

Greater than or equal to
``` python
16 >= 18
```

Less than
``` python
16 < 18
```

Less than or equal to
``` python
16 <= 18
```

##### Selection

One section of code.  Code is only run if the comparison is `True`.

``` python
age = 21

if age >= 18:
	print("You can go to the pub.")
```

Two sections of code.  One section of code is always run.

``` python
age = 16

if age >= 18:
	print("You can go to the pub.")
else:
	print("You can't go to the pub.")
```

Two, or more, sections of code.  Only the section of code for the first comparison that is `True` is run.

The `else` is optional.

``` python
age = 21

if age >= 18:
	print("You can go to the pub.")
elif age >= 16:
	print("You can vote.")
else:
	print("You can't go to the pub or vote.")
```

#### logical operators

Compare more than one set of values to produce a Boolean answer of `True` or `False`.

##### AND

Both comparisons must be `True` to produce `True`.

``` python
16 <= 18 and "Night" == "Day"
```

|Comparison 1|Comparison 2|Result|
|--|--|--|
|False|False|False|
|False|True|False|
|True|False|False|
|True|True|True|

##### OR

One or both comparisons must be `True` to produce `True`.

``` python
16 <= 18 or "Night" == "Day"
```

|Comparison 1|Comparison 2|Result|
|--|--|--|
|False|False|False|
|False|True|True|
|True|False|True|
|True|True|True|

##### NOT

Reverses the result of the comparison.

``` python
not(16 <= 18)
```

|Comparison |Result|
|--|--|
|False|True|
|True|False|

#### selection constructs using complex conditional statements




#### iteration and repetition using fixed and conditional loops


#### predefined functions


##### random


##### round


##### length


### Implementation (algorithm specification)


#### input validation



#### running total within loop



#### traversing a 1-D array
