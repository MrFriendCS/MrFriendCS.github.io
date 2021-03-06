# N5 Computing Science
{:.no_toc}

[Home](index.md)

## Software Design and Development
{:.no_toc}

All the code examples use Python.  They will work with [Replit](https://replit.com/) and [Thonny](https://thonny.org/).

Python uses indentation (spaces at the beginning of a line) to show where code blocks are.

**Note:** These notes are focused on N5 Computing Science so some terms are used differently.  Any reference to an `array` will actually use a `list`.

## Table of Contents {#toc}
{:.no_toc}

* TOC will be displayed here
{:toc}

### Display information

``` python
print("Hello world")

print(3.14)
```

## Computational constructs

### Assign values

Variables are used to store values.  An assignment statement has 3 parts:

 1. **=** is the assignment operator (an equals sign in maths)
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

``` python
myArrayOfStrings = [""] * 4
```

### Arithmetic operations

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

[Back to Table of Contents](#toc)

### Concatenate strings

Concatenate means to join together.

**Note:**  Only strings can be concatenated.

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

Only strings can be concatenated, anything else must be cast (converted) to a string.

``` python
age = 18

phrase = "I am " + str(age)

print(phrase)
```

### User input

**Note:** Whenever the user enters anything using the keyboard it is treated as a *string* by Python.

```python
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

phrase = word1 + " " + word2

print(phrase)
```

Values that have a different datatype must be cast from string to the correct datatype, using one of the following functions:

```python
myInt = int("42")
myFloat = float("3.14")
myBool = bool("True")
```

Example:

```python
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))

addition = value1 + value2

print(addition)
```

### Selection - simple

#### Comparisons

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

#### Selection

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
score = 81

if score >= 80:
    print("Excellent score!")
elif score >= 50:
    print("Well done!")
else:
    print("Oh dear!")
```

[Back to Table of Contents](#toc)

### Logical operators

Compare more than one set of values to produce a Boolean answer of `True` or `False`.

#### AND

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

#### OR

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

#### NOT

Reverses the result of the comparison.

``` python
not(16 <= 18)
```

|Comparison |Result|
|--|--|
|False|True|
|True|False|

### Selection - complex

``` python
age = 21
banned = False

if age >= 18 and not(banned):
    print("You can go to the pub.")
```

[Back to Table of Contents](#toc)

###  Fixed and conditional loops

#### Fixed loop (for)

Before a fixed loop starts, the number of times it will run ***is*** stated.

``` python
for counter in range(10):
    print(counter)
```

The range function needs a minimum of one parameter but can have more.

``` python
range(stop)

range(start, stop)
```

If only the `stop` parameter is used then the `start` value is always zero.  A little confusingly, the largest value in the range is one less than the `stop` value.


#### Conditional loop (while)

Before a conditional loop starts, the number of times it will run ***is not*** stated.

It only runs if the comparison is `True`.  Each time the code is completed the comparison is checked again.  If it is still `True` the code is run again.

``` python
counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1
```

[Back to Table of Contents](#toc)

### Predefined functions


#### Random

The code to produce a random number needs to be imported before it can be used.

The code can be used to produce a random integer, with the lowest and highest possible values specified, or a random floating point value that ranges from 0 to 1.

``` python
import random

myInt = random.randint(1, 6)
print(myInt)

myFloat = random.random()
print(myFloat)
```

#### Round

The round function works with floating point values (decimals).  It returns (produces) a value that is rounded to a specified number of decimal places

``` python
myFloat = 3.14159265359

myRound = round(myFloat, 2)
print(myRound)
```

The round function can also be used to return a value without any decimal places (integer).

The following example will return a value of 4.

``` python
myFloat = 3.5

myRound = round(myFloat)
print(myRound)
```

The following example will ***also*** return a value of 4.

``` python
myFloat = 4.5

myRound = round(myFloat)
print(myRound)
```

**Note:** Python does not always round up when the value is 5.  Instead it rounds to the nearest even number!

#### Length

The length function works with strings and arrays.  It returns a number that is equal to the number of characters in a string or the number of elements in an array.

``` python
myLength = len("Hello world")
print(myLength)


myString = "Computing"
myLength = len(myString)
print(myLength)


myArrayOfIntegers = [56, 34, 2, 85, 51]
myLength = len(myArrayOfIntegers)
print(myLength)
```

[Back to Table of Contents](#toc)

## Standard algorithms

### Input validation

#### User input

The input function allows a user to enter information using the keyboard.

``` python
user = input("What is your name? ")

print("Hello " + user)
```

**Note:** Anything entered using the keyboard is a string.  If the value represents another data type then it must be cast (converted) to that data type.

``` python
age = int(input("How old are you? (In whole years) "))

height = float(input("How tall are you? (In metres) "))
```

#### Validation

User input can be checked using a conditional loop.  If it is not acceptable it can be re-entered until it is.

``` python
dice = int(input("Enter a value from 1 to 6: "))

while dice < 1 or dice > 6:
    print("You entered an invalid value.")
    dice = int(input("Enter a value from 1 to 6: "))

print("You entered " + str(dice))
```

### Running total within a loop

``` python
total = 0

for counter in range(4):
    age = int(input("Enter an age: "))

    total = total + age

print("The combined age is " + str(total))
```

### Traversing a 1-D array

Arrays store more than one value, called elements.  Each element has a position.  Python starts counting from zero.


Example.  Retrieve the value in the second element, and change the value of the the third element.

``` python
scores = [56, 34, 2, 85, 51]

score = scores[1]
print(score)

scores[2] = 82
print(scores)
```

#### Getting values out

``` python
scores = [56, 34, 2, 85, 51]

for index in range(len(scores)):
    print(scores[index])
```

#### Putting values in

``` python
heights = [0.0] * 5

for index in range(len(heights)):
    height = float(input("Enter a height: "))

    heights[index] = height

print(heights)
```

[Back to Table of Contents](#toc)
