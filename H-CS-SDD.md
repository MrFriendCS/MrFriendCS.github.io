# Higher Computing Science
{:.no_toc}

[Home](index.md)

## Software Design and Development
{:.no_toc}

All the code examples use Python.   The code is available on  [Replit](https://replit.com/@esafriend1r/H-CS-Software).

**Note:** These notes are focused on Higher Computing Science so some terms are used differently.  Any reference to an `array` will actually use a `list`.

## Table of Contents {#toc}
{:.no_toc}

* TOC will be displayed here
{:toc}

### Example Data

The data used in the examples can be represented in a table:

| Name | Age | Height |
|--|--|--|
| Alan | 24 | 1.78 |
| Beth | 23 | 1.63 |
| Carl | 22 | 1.89 |
| Dina | 21 | 1.59 |

It can also be represented as comma separated values, e.g. `people.csv`:

```
Alan,24,1.78
Beth,23,1.63
Carl,22,1.89
Dina,21,1.59
```

## Data types and structures

### Parallel 1D arrays

Parallel arrays have the same number of elements in each array.

``` python
names = [""] * 4
ages = [0] * 4
heights = [0.0] * 4
```

### Records

The code to produce a record needs to be imported before it can be used.

A record is defined with attributes, which can have default values.

``` python
from dataclasses import dataclass

@dataclass
class person:
    name: str = ""
    age: int = 0
    height: float = 0.0
```

Individual records can be created, either with default values, or with specified values.

``` python
person1 = person()

person2 = person("Beth", 23, 1.63)
```

Attribute values can be accessed using the form:

```
recordName.attributeName
```

An attribute value from a record can retrieved.

``` python
name = person2.name
print(name)
```

An attribute value in a record can updated.

``` python
age = person2.age
age = age + 1

person2.age = age
print(person2)
```

### Arrays of records

Using default values.

``` python
people = [person()] * 4
```

[Back to Table of Contents](#toc)

## Computational constructs

### Sub-routines

When a sub-routine is defined it can have zero, one, or more parameters.  These are known as formal parameters.  The formal parameters will 'catch' values that are passed to the sub-routine.

``` python
def subroutineName(formalParameter):
    <sub-routine code>
```

When a sub-routine is called it can have parameters passed to it.  These are known as actual parameters.

``` python
subroutineName(actualParameter)
```

#### Procedures

A procedure is a type of sub-routine that ***does not*** return a value.  It must be defined before it can be used.

``` python
def square(number):
    squared = number ** 2
    print(squared)
```

A procedure can be called from the main program, or from another sub-routine.

``` python
square(2)
```

#### Functions

A function is another type of sub-routine that ***does*** return a value.  It must be defined before it can be used.

``` python
def toThePowerOf(number, power):
    value = number ** power
    return value
```

A function can be called from the main program, or from another sub-routine.

``` python
answer = toThePowerOf(2, 5)
print(answer)
```

[Back to Table of Contents](#toc)

### Substrings

Python does not have pre-defined functions for creating substrings.  Strings can be treated as an array of characters.  Python starts counting from zero.

```
Index: 0  1  2  3  4  5  6  7  8  9  10
Value: H  e  l  l  o     W  o  r  l  d
```

``` python
myString = "Hello world"

myCharacter = myString[0]
print(myCharacter)

myCharacter = myString[6]
print(myCharacter)
```

To extract more than a single character a second parameter is used.

```
string[start : stop]
```

**Note:** The `stop` value is always one more than the last element to be included.

``` python
myString = "Hello world"

mySubstring = myString[0:4]
print(mySubstring)

mySubstring = myString[6:11]
print(mySubstring)
```

If the first or the last character is included in the substring then the `start` or `stop` parameter can be omitted.

#### Left substring

``` python
myString = "Hello world"

mySubstring = myString[ :4]
print(mySubstring)
```

#### Right substring

``` python
myString = "Hello world"

mySubstring = myString[6: ]
print(mySubstring)
```

It is possible to use a negative value for the `start` parameter, with `-1` being the last element.

``` python
myString = "Hello world"

mySubstring = myString[-5: ]
print(mySubstring)
```


#### Mid substring

``` python
myString = "Hello world"

mySubstring = myString[3:8]
print(mySubstring)
```

[Back to Table of Contents](#toc)

### Character to ASCII and vice versa

#### Character to ASCII

``` python
myCharacter = "A"
myASCII = ord(myCharacter)
print(myASCII)
```

#### ASCII to character

``` python
myASCII = 97
myCharacter = chr(myASCII)
print(myCharacter)
```

### Floating-point numbers to integers

This removes the decimal part of the value.  It does not round.

``` python
myFloat = 4.95
myInt = int(myFloat)
print(myInt)
```

### Modulus

The modulus is the remainder when doing division.

13 &#xf7; 5 = 2 remainder 3

``` python
myModulus = 13 % 5
print(myModulus)
```

[Back to Table of Contents](#toc)

## File handling

Reading and writing a csv or txt file can be achieved using the same code, just change the file extension.

**Note:** Anything read from a file is a string.  If the value represents another data type then it must be cast to that data type.

### Reading parallel arrays from a file

Declare parallel arrays that are large enough to hold the data.

``` python
names = [""] * 4
ages = [0] * 4
heights = [0.0] * 4
```

Declare other variables

``` python
tempArray = [""] * 3
name = ""
age = 0
height = 0.0
line = ""
index = 0
```

Open the file that holds the data, in read only mode.

``` python
file = open("people.csv" ,"r" )
```

Read the first line of the file.

``` python
line = file.readline()
```

Start / continue the conditional loop if the variable `line` is not empty.

``` python
while line:
```

Split the content of the variable `line` at the commas.  Assign the elements to `tempArray`.

``` python
    tempArray = line.split(",")
```

Retrieve the individual elements from `tempArray` and cast appropriately.

``` python
    name = tempArray[0].strip()
    age = int(tempArray[1].strip())
    height = float(tempArray[2].strip())
```

Assign the data to the appropriate parallel array.

``` python
    names[index] = name
    ages[index] = age
    heights[index] = height
```

Read the next line of the file.

``` python
    line = file.readline()
```

Increase the index of where the next element will be stored, and back to `while` statement.

``` python
    index = index + 1
```

Close the file.

``` python
file.close()
```

### Reading an array of records from a file

Declare an array of records large enough to hold the data.

``` python
people = [person()] * 4
```

Declare all other variables.

``` python
tempArray = [""] * 3
name = ""
age = 0
height = 0.0
line = ""
index = 0
```

Open the file that holds the data, in read only mode.

``` python
file = open("people.csv" ,"r" )
```

Read the first line of the file.

``` python
line = file.readline()
```

Start / continue the conditional loop if the variable `line` is not empty.

``` python
while line:
```

Split the content of the variable `line` at the commas and assign the elements to `tempArray`.

``` python
    tempArray = line.split(",")
```

Retrieve the individual attributes from `tempArray`, remove leading and trailing spaces, and cast appropriately.

``` python
    name = tempArray[0].strip()
    age = int(tempArray[1].strip())
    height = float(tempArray[2].strip())
```

Assign a record to appropriate element in the array.

``` python
    people[index] = person(name, age, height)
```

Read the next line of the file.

``` python
    line = file.readline()
```

Increase the index of where the next record will be stored.

``` python
    index = index + 1
```

Close the file.

``` python
file.close()
```

[Back to Table of Contents](#toc)

### Writing parallel arrays to a file

**Note:** Only strings can be written to a file, anything else must be cast to a string.

Open the file that will hold the data, in write mode.  If the file does not exist it will be created, but if it does exist it will be overwritten.

``` python
file = open("newPeople.csv", "w")
```

Loop for each element in the arrays.

``` python
for index in range(len(names)):
```

Write the elements to the file, separated with commas, and finish with a newline `\n`.

``` python
    file.write(names[index] + ",")
    file.write(str(ages[index]) + ",")
    file.write(str(heights[index]) + "\n")
```

Close the file.

``` python
file.close()
```

[Back to Table of Contents](#toc)

## Standard algorithms

### Linear search - array

Finds the first occurrence.

``` python
names = ["Alan", "Beth", "Carl", "Dina"]
found = False
index = 0

while not(found) and index < len(names):
    if names[index] == "Carl":
        found = True

if found:
    print("Found")
else:
    print("Not found")
```

### Find minimum (or maximum) - array

Assign the value in the first element as the minimum. or maximum, value.  Loop from the second element.

``` python
heights = [1.78, 1.63, 1.89, 1.59]

minimum = heights[0]

for index in range(1, len(heights)):
    if heights[index] < minimum:
        minimum = heights[index]

print("Minimum: " + str(minimum))
```

### Count occurrences - array

``` python
names = ["Alan", "Beth", "Carl", "Dina"]
count = 0

for index in range(len(names)):
    if names[index] == "Carl":
        count = count + 1

print("Found " + str(count) + " occurence(s)")
```

[Back to Table of Contents](#toc)
