# Title: N5 Gradient Calculator
# Author: Mr Friend
# Date: 12 Nov 2026

# Initialise variables
rise: float = 2.5
run: float = 10
gradient: float = 0.0

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

# Calculate the gradient
gradient = round(rise / run, 2)

# Display the rise and run
print("Rise: : " + str(rise))
print("Run: : " + str(run))
print

# Display the gradient
print("Gradient: " + str(gradient))
print("==============")