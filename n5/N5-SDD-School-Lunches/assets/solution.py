# Title: N5 SDD Five Lunches
# Author: Mr Friend
# Date: 14 Nov 2021

# Declare variables
day = 0
lunch = 0.0
total = 0.0
costs = [0.0] * 5

# Get the costs of 5 lunches from the user
for meal in range(5):
    lunch = float(input("Enter to cost of lunch " + str(day + 1) + ": £"))
    costs[meal] = lunch

# Calculate the total
for meal in range(5):
    total = total + costs[day]

# Display the total
print("The total cost is: £" + str(total))
