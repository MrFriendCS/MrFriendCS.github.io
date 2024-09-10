# Title: N5 Gradient Calculator
# Author: Mr Friend
# Date: 10 Sep 2024

# Initialise variables
rise = 0.0
run = 0.0
gradient = 0.0

# Display header
print("Gradient Calculator")
print("-------------------\n")

# Get rise from user
rise = float(input("Rise: "))

# Get run from user
run = int(input("Run: "))

# Calculate the gradient
gradient = rise / run

# Display the gradient
print("\nGradient: " + str(gradient))
print("=============")