# Title: N5 SDD Gamble
# Author: Mr Friend
# Date: 10 Nov 2024

# Get extra code
import random


# Initialise variables
die = 0
multiplier = 0
price = 0.0
total = 0.0


# Header
print("\nPadula's 10-Sided Lucky Die")
print("---------------------------")
print("Only play if you can afford to lose.")
print("Throw a 2 and pay double!")
print("---------------------------")


# Get valid price

# Get price from user
price = float(input("\nPrice: £"))

# Check if valid
while price <= 0 or price >=5:
    
    # Display error message
    print("\nPrice most be more than £0 and less than £5")
    
    # Get price from user
    price = float(input("Price: £"))
    

# Roll the die
die = random.randint(1, 10)

# Note: used to test selection
#die = 1


# Select the multiplier
if die == 7:
    multiplier = 0
    
elif die == 1 or die == 9:
    multiplier = 0.5
    
elif die == 3 or die == 5:
    multiplier = 0.75
    
elif die == 2:
    multiplier = 2
    
else:
    multiplier = 1
    

# Calculate total
total = price * multiplier


# Round total
total = round(total, 2)


# Display die
print("\nYou threw a " + str(die))


# Display total
print("So you pay: £" +str(total))


# Footer
print("\nHave a nice day!")
print("----------------")
