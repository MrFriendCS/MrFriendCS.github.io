# Title: N5 CS 2018 Task 2
# Author: Mr Friend
# Date: 30 Sep 2026

# Declare variables and data structures
rawReading: float = 0.0
roundedReading: int = 0
readings: list[int] = [0 for _ in range(5)]
signalPattern: str = ""

# Loop 5 times
for index in range(5):

    # Get valid reading
    rawReading = float(input("Enter the reading: "))

    while rawReading < 0 or rawReading > 100:
        
        # Error message
        print("Reading must be from 0 to 100")
        
        # Get valid reading
        rawReading =float(input("Enter the reading: "))
    
    # Round reading to zero decimal places
    roundedReading = round(rawReading)

    # Store the reading
    readings[index] = roundedReading

    # Is reading greater than 80?
    if roundedReading > 80:
        
        # Add "S" on to signal pattern
        signalPattern = signalPattern + "S"
    
    # Is reading less than 30?
    elif roundedReading < 30:
        
        # Add "P" on to signal pattern
        signalPattern = signalPattern + "P"

    else:
        # Add "M" on to signal pattern
        signalPattern = signalPattern + "M"

# Display signal pattern with message
print("Signal Pattern is: " + signalPattern)

# Loop 5 times
for index in range(5):

    # Display rounded reading with message
    print("Reading " + str(index + 1) + " - " + str(readings[index]))
