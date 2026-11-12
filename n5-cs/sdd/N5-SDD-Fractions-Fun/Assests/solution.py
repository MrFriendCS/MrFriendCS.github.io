# Title: N5 SDD Fractions Fun
# Author: Mr Friend
# Date: 12 Nov 2026

# 1. Initialise variables
num1: int = 0
den1: int = 0
num2: int = 0
den2: int = 0

comm: int = 0
num1e: int = 0
num2e: int = 0
numA: int = 0

# 2. Assign first fraction numerator and denominator to variables
num1 = 2
den1 = 5

# 3. Assign second fraction numerator and denominator to variables
num2 = 3
den2 = 7

# 4. Calculate common denominator
comm = den1 * den2

# 5. Calculate first equivalent numerator
num1e = num1 * den2

# 6. Calculate second equivalent numerator
num2e = num2 * den1

# 7. Calcualte final numrator
numA = num1e + num2e

# Display results
print("Fractions Fun!")
print("--------------")
print()

# 8. Display initial fractions, equivalent fractions, and final fraction
print(str(num1) + "   " + str(num2) + "   " + str(num1e) + "   " + str(num2e) + "   " + str(numA))
print("- + - = -- + -- = --")
print(str(den1) + "   " + str(den2) + "   " + str(comm) + "   " + str(comm) + "   " + str(comm))
