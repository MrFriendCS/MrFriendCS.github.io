# Higher Computing Science

## Software Design and Development

All the code examples use Python.  Python uses indentation (spaces at the beginning of a line) to show where code blocks are.

**Note:** These notes are focused on Higher Computing Science so some terms are used differently.  Any reference to an `array` will actually use a `list`.

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

## Implementation (data types and structures) 

### parallel 1D arrays

Parallel arrays have the same number of elements in each array.

``` python
names = [""] * 4
ages = [0] * 4
heights = [0.0] * 4
```

### records

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

### arrays of records

``` python
people = [person()] * 4
```



## Implementation (computational constructs)

### sub-routines

When a sub-routine if defined it can zero, one, or more parameters.  These are known as formal parameters.  The formal parameters will 'catch' values that are passed to the sub-routine.

``` python
def subroutineName(formalParameter):
    <sub-routine code>
```

When a sub-routine is called it can have parameters passed to it.  These are known as actual parameters.

``` python
subroutineName(actualParameter):
```

### procedures

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

### functions

A function is another type of sub-routine that ***does*** return a value.  It must be defined before it can be used.

``` python
def square(number):
    squared = number ** 2
    return squared
```

A function can be called from the main program, or from another sub-routine.

``` python
squareNumber = square(2)
print(squareNumber)
```

### create substrings

Python does not have pre-defined functions for creating substrings.  Strings can be treated like an array.  Python starts counting from zero.

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

It is possible to use a negative value for the `start` parameter.

``` python
myString = "Hello world"

mySubstring = myString[-5: ]
print(mySubstring)
```


#### Mid substring

``` python
myString = "Hello world"

mySubstring = myString[1:5]
print(mySubstring)
```

### convert from character to ASCII and vice versa

#### character to ASCII

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

### convert floating-point numbers to integers

This removes the decimal part of the value.  It does not round.

``` python
myFloat = 3.95
myInt = int(myFloat)
print(myInt)
```

### modulus

The modulus is the remainder when doing division.

``` python
myModulus = 12 // 5
print(myModulus)
```

### file handling:

#### Reading parallel arrays from a file

Declare large enough parallel arrays to hold the data.

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

Assign the data the appropriate parallel array.

``` python
	names[index] = name
	ages[index] = age
	height[index] = height
```

Read the next line of the file.

``` python
	line = file.readline()
```

Increase the index of where the next element will be stored.

``` python
	index = index + 1
```

Close the file.

``` python
file.close()
```

#### Reading an array of records from a file

Declare a large enough array of records to hold the data.

``` python
people = [person()] * 4
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

Retrieve the individual attributes from `tempArray` and cast appropriately.

``` python
	name = tempArray[0].strip()
	age = int(tempArray[1].strip())
	height = float(tempArray[2].strip())
```

Assign the record to appropriate element in the array.

``` python
	people[index] = person(name, age, height)
```

Read the next line of the file.

``` python
	line = file.readline()
```

Increase the index of where the next element will be stored.

``` python
	index = index + 1
```

Close the file.

``` python
file.close()
```

## Implementation (algorithm specification)

### implement standard algorithms using 1D arrays or arrays of records

#### linear search - array

Finds the first occurrence.

``` python
names = ["Alan", "Beth", "Carl", "Dina"]
found = False
pointer = -1

for index in range(len(names)):
    if found == False and names[index] == "Carl":
        found = True
        pointer = index

if found:
    print("Found at index " + str(pointer))
else:
    print("Not found")
```

#### find minimum and maximum - array

Assign the value in the first element as the highest. or lowest, value.  Loop from the second element.

``` python
heights = [1.78, 1.63, 1.89, 1.59]

highest = heights[0]

for index in range(1, len(heights)):
    if heights[index] > highest:
        highest = heights[index]

print("Highest: " + str(highest))
```

#### count occurrences - array

``` python
names = ["Alan", "Beth", "Carl", "Dina"]
count = 0

for index in range(len(names)):
    if names[index] == "Carl":
        count = count + 1

print("Found " + str(count) + " occurence(s)")
```
