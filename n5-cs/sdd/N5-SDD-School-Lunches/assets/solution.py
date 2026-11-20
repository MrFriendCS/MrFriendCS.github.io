# Title: N5 SDD Five Lunches
# Author: Mr Friend
# Date: 14 Nov 2021

# Declare variables
lunch: float = 0.0
total: float = 0.0
costs: list[float] = [0.0 for index in range(5)]

# Display header
print("School Lunches")
print("--------------")

# Get the costs of 5 lunches from the user
print("Enter to cost of:")

# Blank line
print()

for day in range(5):
    lunch = float(input("Day " + str(day + 1) + ": £"))
    costs[day] = lunch

# Calculate the total
for meal in range(5):
    total = total + costs[meal]

# Blank line
print()

# Display the total
print("The total cost is: £" + str(total))

# Display footer
print("==============")
