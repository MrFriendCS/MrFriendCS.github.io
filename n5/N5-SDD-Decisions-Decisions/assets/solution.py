# Title: N5 SDD Decisions Decisions
# Author: Mr Friend
# Date 8 Sep 2023

# Declare variables
total = 0.0
discountType = ""
discountRate = 0
discount = 0.0
voucher = ""

# Get total amount from user
total = float(input("Total amount: £"))

# Discount card?
discountType = input("\nDiscount? ")

# Set student discount rate
if discountType == "student":
    discountRate = 10

# Set staff discount rate
if discountType == "staff":
    discountRate = 20

# IS discount to be applied?
if discountRate != 0:
    #Calculate discount amount
    discount = total / 100 * discountRate
    # Update total
    total = total - discount

# Display amount to pay
print("\nAmount to pay: £" + str(total))
    
# voucher?
voucher = input("\nVoucher? ")

# Apply vocuher if answer is 'yes'
if voucher == "yes":
    # Update total
    total = total - 10
    
    # Message
    print("£10 voucher applied")

# Set total to 0 if negative
if total < 0:
    # Update total
    total = 0.0

    # Message
    print("No change given when using a voucher")

# Display final amount to pay
print("\nFinal amount to pay: £" + str(total))
