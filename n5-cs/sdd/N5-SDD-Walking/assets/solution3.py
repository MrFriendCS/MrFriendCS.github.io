# Title: N5 SDD - Walking Distance Calculator Part 3
# Author: Mr Friend
# Date: 12 Nov 2026


# Initialise variables
weeks: int = 0
distance: float = 0.0
total: float = 0.0
roundedTotal: int = 0
average: float = 0.0


# Display header
print("Walking Calculator")
print("------------------")
print()


# Get number of weeks from user
weeks = int(input("How many weeks? "))
print()

# Validate number of weeks
while weeks < 2:
    
    # Error message
    print("Number of weeks must be 2 or more.")
    
    # Get number of weeks from user
    weeks = int(input("How many weeks? "))
    print()


# Loop for each week
for counter in range(weeks):
    
    # Get distance
    distance = float(input("Week " + str(counter+1) + " distance: "))
    
    # Validate number of weeks
    while distance < 0:
    
        # Error message
        print("NDistance must be 0 or more.")
        
        # Get number of weeks from user
        distance = float(input("Week " + str(counter+1) + " distance: "))
        print()
    
    # Add distance to total
    total = total + distance
    

# Round total to 0 dp
roundedTotal = round(total)


# Calculate average
average = roundedTotal / weeks


# Round average to 1 dp
average = round(average, 1)


# Display total
print()
print("Total: " + str(roundedTotal) + " units")


# Display average
print("Average: " + str(average) + " units per week")


# Display footer
print()
print("==================")
