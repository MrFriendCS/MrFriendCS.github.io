# Title: N5 SDD - Walking Distance Calculator Part 2
# Author: Mr Friend
# Date: 22 Sep 2025


# Initialise variables
weeks = 0
distance = 0.0
total = 0.0
roundedTotal = 0
average = 0.0


# Display header
print("Walking Calculator")
print("------------------")
print()


# Get number of weeks from user
weeks = int(input("How many weeks? "))
print()


# Loop for each week
for counter in range(weeks):
    
    # Get distance
    distance = float(input("Week " + str(counter+1) + " distance: "))
    
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
