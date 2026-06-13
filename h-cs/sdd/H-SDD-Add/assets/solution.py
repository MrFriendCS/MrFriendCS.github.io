# Title: H-SDD-Add Two Values Together
# Author: Mr Friend
# Date: 29 Sep 2024


def getValue() -> float:
    """Asks user for a value and returns it."""
    
    # Initialise local variable
    value = 0.0
    
    # Get value from user
    value = float(input("Enter a value: "))
    
    # Return value
    return value


def addValues(value1: float, value2: float) -> float:
    """Adds two values together and returns the result."""
    
    # Initialise local varaibe
    sum = 0.0
    
    # Calculate result
    sum = value1 + value2
    
    # Return result
    return sum


def displayResult(value: float) -> None:
    """Displays value as result."""
    
    # Display result
    print("\nResult: " + str(value))
    

def main() -> None:
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