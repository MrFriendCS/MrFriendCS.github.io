# Title: N5 SDD Swimming
# Author: Mr Friend
# Date: 9 Nov 2023

# Declare Variables
swims = 0
lengths = 0
total = 0
average = 0.0

# Get valid number of swims from user
while swims < 2 or swims > 7:
    swims = int(input("\nHow many swims? "))

    # Check value
    if swims < 2 or swims > 7:
        # Error message
        print("Number of swims must be from 2 to 7")

# Loop for number of swims
for counter in range(swims):

    # Get valid number of lengths from user
    while lengths < 1 or lengths > 100:
        lengths = int(input("\nSwim " + str(counter + 1) + " lengths? "))

        # Check value
        if lengths < 1 or lengths > 100:
            # Error message
            print("Number of lengths must be from 1 to 100")

    # Update total
    total = total + lengths

    # Reset lengths
    lengths = 0

# Calculate average number of lengths
average = total / swims

# Round average to 1 dp
average = round(average, 1)

# Display results
print("\n" + str(total) + " lengths were swum over " + str(swims) + " swims.")

print("An average of " + str(average) + " lengths per swim.")
