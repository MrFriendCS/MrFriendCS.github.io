# Title: N5 SDD Book Shop
# Author: Mr Friend
# Date 31 Aug 2024

# Initialise variables
total = 0.0
discount = 0.0
student = ""
voucher = ""

# Display header
print("UoB Book Shop")
print("-------------")

# Get total amount to pay
print()
total = float(input("Total amount: £"))

# Ask if student
print()
student = input("Student? ")

# Apply discount if answer is 'yes'
if student == "yes":
    
    #Calculate 10% discount
    discount = total * 0.10

    # Display updated amount to pay
    print()
    print("Discount: £" + str(discount))

    # Reduce amount to pay by discount amount
    total = total - discount

    # Display updated amount to pay
    print("Amount to pay: £" + str(total))
    
# Ask if voucher being used
print()
voucher = input("Voucher? ")

# Apply voucher if answer is 'yes'
if voucher == "yes":
    
    # Reduce amount to pay by £10
    total = total - 10
    
    # Display discount message
    print("£10 voucher applied")

# Is amount to pay < £0?
if total < 0:
    
    # Set amount to pay to £0
    total = 0.0

    # Display no change given message
    print("No change given when using a voucher")

# Display final amount to pay
print()
print("Final amount to pay: £" + str(total))

# Display footer
print("====================")