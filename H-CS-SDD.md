# Higher Computing Science

## Software Design and Development

All the code examples use Python.  Python uses indentation (spaces at the beginning of a line) to show where code blocks are.

**Note:** These notes are focused on Higher Computing Science so some terms are used differently.  Any reference to an `array` will actually use a `list`.

### Example Data

The data used in the examples can be represented in a table:

| Name | Age | Height |
|--|--|--|
| Alan | 22 | 1.78 |
| Beth | 23 | 1.63 |
| Carl | 24 | 1.89 |
| Dina | 21 | 1.59 |

It can also be represented as a comma separated values, e.g. `people.csv`:

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

Describe, exemplify and implement the appropriate constructs in a procedural high-level (textual) language:

parameter passing (formal and actual)

the scope of local and global variables

sub-programs/routines, defined by their name and arguments (inputs and outputs):
— functions
— procedures

### create substrings


### convert from character to ASCII and vice versa


### convert floating-point numbers to integers


### modulus



### file handling:
— sequential CSV and txt files (open, create, read, write, close)

## Implementation (algorithm specification)

### implement standard algorithms using 1D arrays or arrays of records

#### linear search

#### find minimum and maximum

#### count occurrences
