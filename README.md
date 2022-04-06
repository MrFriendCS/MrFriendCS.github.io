
# N5 Computing Science

## Software Design and Development

All code examples use Python.  Python uses indentation (spaces at the beginning of a line) to show where code blocks are.

**Note:** These notes are focused on N5 Computing Science so some terms are used differently.  Any reference to an `array` will actually use a `list`.

### Display information

``` python
print("Hello world")

print(3.14)
```

### Implementation (computational constructs)

#### expressions to assign values

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

``` python
age = 21
banned = False

if age >= 18 and not(banned):
    print("You can go to the pub.")
```

#### iteration and repetition using fixed and conditional loops

##### Fixed loop

Before a fixed loop starts, the number of times it will run ***is*** stated.

``` python
for counter in range(10):
    print(counter)
```

##### Conditional loop

Before a conditional loop starts, the number of times it will run ***is not*** stated.

It only runs if the comparison is `True`.  Each time the code is completed the comparison is checked again.  If it is still `True` the code is run again.

``` python
counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1
```


#### predefined functions


##### random

The code to produce a random number needs to be imported before it can be used.

The code can be used to produce a random integer, with the lowest and highest possible values specified, or a random floating point value that ranges from 0 to 1.

``` python
import random

myInt = random.randint(1, 6)
print(myInt)

myFloat = random.random()
print(myFloat)
```

##### round

The round function works with floating point values (decimals).  It returns (produces) a value that is rounded to a specified number of decimal places

``` python
myFloat = 3.14159265359

myRound = round(myFloat, 2)
print(myRound)
```

The round function can also be used to return values without any decimal places.

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

##### length

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


### Implementation (algorithm specification)

#### input validation

##### User input

Using the input function, the user can enter information with the keyboard.

``` python
user = input("What is your name? ")

print("Hello " + user)
```

Anything entered using the keyboard is a string.  If the value represents another data type then it must be cast (converted) to that data type.

``` python
age = int(input("How old are you? (In whole years) "))

height = float(input("How tall are you? (In metres) "))
```

##### Validation

User input can be checked using a conditional loop.  If it is not acceptable it can be re-entered until it is.

``` python
dice = int(input("Enter a value from 1 to 6: "))

while dice < 1 or dice > 6:
    print("You entered an invalid value.")
    dice = int(input("Enter a value from 1 to 6: "))

print("You entered " + str(dice))
```

#### running total within loop

``` python
total = 0

for counter in range(4):
    age = int(input("Enter an age: "))

    total = total + age

print("The combined age is " + str(total))
```

#### traversing a 1-D array

Arrays store more than one value, called elements.  Each element has a position.  Python starts counting from zero.

```
arrayName[indexValue]
```

**Example**.  Retrieve the value in the second element, and change the value of the the third element.

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

##### Putting values in

``` python
heights = [0.0] * 5

for index in range(len(heights)):
    height = float(input("Enter a height: "))

    heights[index] = height
```
