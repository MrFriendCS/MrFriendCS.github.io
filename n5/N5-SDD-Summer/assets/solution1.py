# Title: N5 SDD Summer Tasks
# Author: Mr Friend
# Date: 3 Aug 2024

#
# Task 1
#

# Initilise variables
value1 = 0
value2 = 0

add = 0
minus = 0
times = 0
divided = 0.0
power = 0

# Get values from user
value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))

# Calculate results
add = value1 + value2
minus = value1 - value2
times = value1 * value2
divided = value1 / value2
power = value1 ** value2

# Display results
print(str(value1) + " add " + str(value2) + " = " + str(add))
print(str(value1) + " minus " + str(value2) + " = " + str(minus))
print(str(value1) + " times " + str(value2) + " = " + str(times))
print(str(value1) + " divided by " + str(value2) + " = " + str(divided))
print(str(value1) + " to the power of " + str(value2) + " = " + str(power))


#
# Task 2
#

# Initilise variables
base = 0
height = 0

area = 0

# Get values from user
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

# Calculate result
area = 0.5 * base * height

# Display result
print("Area: " + str(area) + " units squared")


#
# Task 3
#

# Initilise variables
value = 0

root = 0

# Get value from user
value = int(input("Enter a value: "))

# Calculate result
root = value ** 0.5

# Display result
print("The root of " + str(value) + " is " + str(root))


#
# Task 4
#

# Initilise variables
name = ""
birthYear = 0
currentYear = 0

age = 0
year16 = 0
year40 = 0
year68 = 0


# Get values from user
name = input("Enter your name: ")
birthYear = int(input("Enter your birth year (4 digits): "))
currentYear = int(input("Enter the current year (4 digits): "))

# Calculate results
age = currentYear - birthYear
year16 = birthYear + 16
year40 = birthYear + 40
year68 = birthYear + 68

toRetire = 68 - age

# Display results
print("Hi " + name + ", you are " + str(age) + " this year.")

print("\nHere are some significant birthdays:")
print("16 - " + str(year16))
print("18 - " + str(year16 + 2))
print("21 - " + str(year16 + 5))
print("40 - " + str(year40))
print("60 - " + str(year40 + 20))
print("68 - " + str(year68))

print("\nIf you retire at 68, you have " +str(toRetire) + " years to go.")
