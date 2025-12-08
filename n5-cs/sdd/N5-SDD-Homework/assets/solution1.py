# Title: N5-SDD-Homwork
# Author: Mr Friend
# Date: 8 Dec 2025

# Initialise variables
minutes = 0
total = 0
average = 0
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Header
print("Homework Calculator")
print("-------------------")
print()

print("How many mintues did you do on:")
print()

# Loop for each day
for index in range(len(days)):
    
    # Get minutes studied
    minutes = int(input(days[index] + ": "))
    
    # Check if valid number of minutes
    while minutes < 0 or minutes > 240:
        
        # Error message
        print()
        print("Must be between 0 and 240 minutes")
        
        # Get minutes studied
        minutes = int(input(days[index] + ": "))
    
    # Update total
    total = total + minutes

# Calculate average (0 dp)
average = round(total / len(days))

# Display total
print()
print("You did a total of " + str(total) + " minutes last week.")

# Dsiplay average
print()
print("You did a average of " + str(average) + " minutes a day.")

# Footer
print()
print("===================")
