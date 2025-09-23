# Title: N5 SDD Shopping
# Author: Mr Friend
# Date 23 Sep 2025


# Initialise variables
total = 0.0
discount = 0.0
loyal = ""


# Display header
print("Baldi")
print("-----")


# Get total amount to pay
print()
total = float(input("Total amount: £"))


# Ask if shopper has a loyalty card
print()
loyal = input("Loyalty card? ")

# Apply discount if answer is 'yes'
if loyal == "yes":
    
    # Calculate 10% discount
    discount = total * 0.10
    
    # Round discount
    discount = round(discount, 2)

    # Display discount
    print()
    print("Discount: £" + str(discount))

    # Calculate final amount to pay
    total = total - discount


# Display final amount to pay
print()
print("Final amount: £" + str(total))


# Display footer
print("====================")
