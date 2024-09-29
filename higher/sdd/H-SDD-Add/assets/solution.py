# Title: H-SDD-ADD
# Author: Mr Friend
# Date: 29 Sep 2024


def getValue():
    """Asks user for a value and returns it."""
    
    # Initialise local variable
    value = 0.0
    
    # Get value from user
    value = float(input("Enter a value: "))
    
    # Return value
    return value


def addValues(value1, value2):
    """Adds two values together and returns the result."""
    
    # Initialise local varaibe
    sum = 0.0
    
    # Calculate result
    sum = value1 + value2
    
    # Return result
    return sum


def displayResult(value):
    """Displays value as result."""
    
    # Display result
    print("\nResult: " + str(value))
    

def main():
    """Main program."""
    
    # Initialise variables
    value1 = 0.0
    value2 = 0.0
    sum = 0.0
    
    # 1. Get first value
    value1 = getValue()
    
    # 2. Get second value
    value2 = getValue()
    
    # 3. Add values
    sum = addValues(value1, value2)
    
    # 4. Display result
    displayResult(sum)
    

# Call main()
main()