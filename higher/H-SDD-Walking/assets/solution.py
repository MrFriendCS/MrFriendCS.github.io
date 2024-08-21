# Title: H SDD Walking
# Author: Mr Friend
# Date: 21 Aug 2024

# Initilise Global Variables

distance = 0.0
distances = [0.0] * 4
total = 0.0
average = 0.0

# Message
print("Enter the distance walked each week:")

# Loop for each week
for index in range(len(distances)):
    
    # Get distance walked
    distance = float(input("Week " + str(index+1) + ": "))
    
    # Re-enter if invalid
    while distance < 0:
        # Error message
        print("\nDistance must be 0 or more")
    
        # Get distance walked
        distance = float(input("Week " + str(index+1) + ": "))
        
    # Store distance
    distances[index] = distance
    
    # Calculate total
    total = total + distance
    
# Calculate average (1 dp)
average = round(total/4 , 1)

# Open a connect to the file
file = open("walking.txt", "w")

# Write heading
file.write("Walking Results - 4 Weeks\n")
file.write("-------------------------\n\n")

# Write distances walked
for index in range(len(distances)):
    file.write("Week " + str(index+1) + ": " + str(distances[index]) + "\n")
    
# Write total
file.write("\nTotal: " + str(total) + " miles\n")

# Write total
file.write("\nAverage: " +str(average) + "miles 1 (dp)")

# Close connection to file
file.close()