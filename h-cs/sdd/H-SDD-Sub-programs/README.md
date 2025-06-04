# H SDD - Sub-routines Example


## Introduction

The programs for Higher CS can be laid out in the following order:

1. Title, author, date
2. Import any extra code
3. Sub-routines - multiple - most of the code
4. Main programs - using the Sub-routines


## Example

``` python
# Title: Sub-routines Example
# Author: Mr Friend
# Date: 4 Jun 2025

#
# Sub-programs
#


def getValues():
    """Returns some values."""
    
    # Return values
    return 2, 3


def addValues(value1, value2):
    """Adds two values and returns result."""
    
    # Initialise local variable
    result = value1 + value2
    
    # Return result
    return result


def displayResult(result):
    """Display the result."""
    
    # Display result
    print("Result: " + str(result))


#
# Main program
#

# Initialise global variables
num1 = 0
num2 = 0
sum = 0

# Get values
num1, num2 = getValues()

# Add values together
sum = addValues(num1, num2)

# Display result
displayResult(sum)
```
