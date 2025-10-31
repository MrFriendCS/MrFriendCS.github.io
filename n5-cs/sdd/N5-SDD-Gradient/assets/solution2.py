# Title: N5 Gradient Calculator Part 2
# Author: Mr Friend
# Date: 31 Oct 2025

# Initialise variables
rise = 0.0
run = 0.0
gradient = 0.0

# Display header
print("Gradient Calculator")
print("-------------------")
print()
print("                   .")
print("               .   |")
print("           .       |")
print("       .           | Rise")
print("   .               |")
print("___________________|")
print("       Run")
print()
print("           Rise")
print("Gradient = ----")
print("           Run")
print()

# Get the rise
rise = float(input("What is the rise? "))

# Get the run
run = float(input("What is the run? "))

# Display the equeation
print()
print("           Rise   " + str(rise))
print("Gradient = ---- = ----")
print("           Run    " + str(run))

# Calculate the gradient
gradient = round(rise / run, 2)

# Display the gradient
print()
print("Gradient = " + str(gradient))
print("===================")