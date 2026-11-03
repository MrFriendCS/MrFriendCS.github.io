# Title: N5 SDD Book Shop - Part 3
# Author: Mr Friend
# Date: 3 Nov 2026

# Initialise variables
total: float = 0.0
discountType: str = ""
discountRate: int = 0
discount: float = 0.0
voucher: str = ""

# Display header
print("UoB Book Shop")
print("-------------\n")

# Get total amount from user
total = float(input("Total amount: £"))

# Check total amount is valid
while total < 5 or total > 100:
    print("\nAmount must be from £5 to £100")
    total = float(input("Total amount: £"))

# Get discount type
discountType = input("\nDiscount? ")

# Is a student?
if discountType == "student" or discountType == "STUDENT":
    discountRate = 10

# Is a member of staff?
elif discountType == "staff" or discountType == "STAFF":
    discountRate = 20


# Is discount to be applied?
if discountRate != 0:
    #Calculate discount
    discount = total / 100 * discountRate
    
    # Update total
    total = total - discount
    
    # Display discount
    print("\nDiscount: £" + str(discount))

    # Display amount to pay
    print("Amount to pay: £" + str(total))


# Got a voucher?
voucher = input("\nVoucher? ")

# Apply vocuher if answer is 'yes'
if voucher == "yes" or voucher == "YES":
    # Update total
    total = total - 10
    
    # Message
    print("\n£10 voucher applied")

# Set total to 0 if negative
if total < 0:
    # Update total
    total = 0.0

    # Message
    print("No change given when using a voucher")


# Display final amount to pay
print("\nFinal amount to pay: £" + str(total))

# Footer
print("====================")