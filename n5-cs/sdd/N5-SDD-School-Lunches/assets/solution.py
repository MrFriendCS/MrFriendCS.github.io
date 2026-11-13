# Title: N5 SDD Five Lunches
# Author: Mr Friend
# Date: 14 Nov 2021

# Declare variables
lunch: float = 0.0
total: float = 0.0
costs: list[float] = [0.0 for _ in range(5)]

# Get the costs of 5 lunches from the user
for day in range(5):
    lunch = float(input("Enter to cost of day " + str(day + 1) + ": £"))
    costs[meal] = lunch

# Calculate the total
for meal in range(5):
    total = total + costs[meal]

# Display the total
print("The total cost is: £" + str(total))
